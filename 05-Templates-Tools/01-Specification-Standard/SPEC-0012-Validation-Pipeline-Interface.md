# SPEC-0012: Validation Pipeline Interface

## Frontmatter

```yaml
spec_id: SPEC-0012
title: Validation Pipeline Interface - AI Safety Layer for Code Quality
version: 1.0.0
status: approved
tier: PROFESSIONAL
pillar: Section 7 - Quality Assurance System
owner: Backend Lead + CTO
last_updated: 2026-02-03
tags:
  - validation
  - pipeline
  - ai-safety
  - code-quality
related_specs:
  - SPEC-0006  # Multi-Provider Codegen
  - SPEC-0020  # Quality Gates Codegen
epic: EP-06 IR-Based Codegen Engine
sprint: Sprint 48
```

---

## 1. Overview

### 1.1 Purpose

Validation Pipeline Interface defines the **AI Safety Layer** that orchestrates parallel quality checks (Lint, Tests, Coverage) for AI-generated code. Part of EP-02 (Auto-Fix Engine), this pipeline ensures AI-generated PRs meet quality standards before merging, with <6 minute p95 latency and non-blocking validator failures.

### 1.2 Scope

**In Scope:**
- ValidationPipeline orchestration service (parallel execution with asyncio.gather)
- BaseValidator abstract class interface (validate() method contract)
- LintValidator implementation (ruff for Python, ESLint for TypeScript)
- TestValidator implementation (pytest for Python, vitest for TypeScript)
- CoverageValidator implementation (pytest-cov, threshold 80%)
- Redis queue architecture (FIFO queue, retry sorted set, processing hash)
- ValidatorResult and PipelineResult data structures
- Prometheus metrics (duration histograms, result counters, queue gauges)
- Background worker with automatic retry (exponential backoff: 10s, 20s, 40s)

**Out of Scope:**
- SecurityValidator (SAST) - covered in SPEC-0001 (Semgrep integration)
- ContextValidator - covered in SPEC-0002 (5 CTX checks)
- Auto-fix generation - separate service in EP-02

### 1.3 Key Metrics

| Metric | Target | Tier | Measurement |
|--------|--------|------|-------------|
| Pipeline p95 Latency | <6 minutes | ALL | End-to-end validation time |
| Lint p95 Latency | <2 minutes | ALL | ruff + ESLint execution time |
| Test p95 Latency | <5 minutes | STANDARD+ | pytest + vitest execution time |
| Coverage p95 Latency | <5 minutes | PROFESSIONAL+ | pytest-cov execution time |
| Queue Wait p95 | <30 seconds | ALL | Redis queue → worker pickup time |
| Blocking Rate | <20% | ALL | % PRs blocked by validation failures |
| False Positive Rate | <5% | ALL | % incorrect FAILED results |

---

## 2. Functional Requirements

### FR-001: ValidationPipeline Orchestration Service

**Description**: ValidationPipeline orchestrates parallel execution of validators (Lint, Test, Coverage) using asyncio.gather, aggregates results, and applies tier-based pass/fail logic.

**BDD Requirements:**

```gherkin
Feature: ValidationPipeline Orchestration
  As a Backend Service
  I want to orchestrate parallel validator execution
  So that AI-generated PRs are validated in <6 minutes

  Background:
    Given ValidationPipeline is initialized with tier "PROFESSIONAL"
    And validators are registered: [LintValidator, TestValidator, CoverageValidator]
    And Redis queue "validation:queue" is available
    And Prometheus metrics exporter is running

  Scenario: Successful parallel validation (all validators PASSED)
    Given PR #123 has 3 files changed (2 Python, 1 TypeScript)
    When ValidationPipeline.validate(pr_id="123", files=["auth.py", "user.py", "utils.ts"]) is called
    Then all 3 validators execute in parallel (asyncio.gather)
    And LintValidator completes in <2 minutes (ruff + ESLint)
    And TestValidator completes in <5 minutes (pytest + vitest)
    And CoverageValidator completes in <5 minutes (pytest-cov)
    And PipelineResult.status = "PASSED"
    And PipelineResult.total_duration_ms <= 360000 (6 minutes)
    And Prometheus histogram "validation_pipeline_duration_seconds" is incremented
    And Prometheus counter "validation_pipeline_passed_total" is incremented

  Scenario: Partial failure (Lint FAILED, Tests PASSED, Coverage PASSED)
    Given PR #124 has Python code with linting errors (ruff: line too long, unused import)
    When ValidationPipeline.validate(pr_id="124", files=["models.py"]) is called
    Then LintValidator returns ValidatorResult(status="FAILED", message="2 linting errors found")
    And TestValidator returns ValidatorResult(status="PASSED", message="All 15 tests passed")
    And CoverageValidator returns ValidatorResult(status="PASSED", message="Coverage 92%")
    And PipelineResult.status = "FAILED"
    And PipelineResult.blocking_validators = ["LintValidator"]
    And PipelineResult.non_blocking_validators = []
    And PR #124 is blocked from merging (tier=PROFESSIONAL, lint is blocking)
    And Prometheus counter "validation_pipeline_failed_total" is incremented

  Scenario: Timeout protection (validator exceeds 10 minutes)
    Given TestValidator is running slow tests (execution time >10 minutes)
    When ValidationPipeline.validate(pr_id="125", files=["slow_test.py"]) is called with timeout=600s
    Then TestValidator is cancelled after 10 minutes (asyncio.wait_for timeout)
    And ValidatorResult(status="TIMEOUT", message="Validation exceeded 600s limit") is returned
    And PipelineResult.status = "ERROR"
    And PR #125 validation is retried (moved to validation:retry queue with retry_count=1)
    And Prometheus counter "validation_pipeline_timeout_total" is incremented

  Scenario: Non-blocking validator failure (Coverage FAILED in STANDARD tier)
    Given tier="STANDARD" (coverage is RECOMMENDED, not MANDATORY)
    And PR #126 has test coverage 75% (below 80% threshold)
    When ValidationPipeline.validate(pr_id="126", files=["service.py"]) is called
    Then CoverageValidator returns ValidatorResult(status="FAILED", message="Coverage 75% < 80%")
    And PipelineResult.status = "PASSED" (non-blocking failure)
    And PipelineResult.non_blocking_validators = ["CoverageValidator"]
    And PipelineResult.warnings = ["Coverage below 80% (current: 75%)"]
    And PR #126 is allowed to merge with warning (tier=STANDARD)
```

**Tier-Specific Requirements:**

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| Lint validator | RECOMMENDED | MANDATORY | MANDATORY | MANDATORY |
| Test validator | OPTIONAL | RECOMMENDED | MANDATORY | MANDATORY |
| Coverage validator | OPTIONAL | RECOMMENDED | MANDATORY | MANDATORY |
| Coverage threshold | N/A | 70% | 80% | 90% |
| Parallel execution | YES | YES | YES | YES |
| Timeout per validator | 10 min | 10 min | 10 min | 10 min |
| Max pipeline duration | 15 min | 15 min | 15 min | 15 min |
| Retry on timeout | 1 retry | 2 retries | 3 retries | 3 retries |
| Blocking on lint failure | NO | YES | YES | YES |
| Blocking on test failure | NO | NO | YES | YES |
| Blocking on coverage failure | NO | NO | YES | YES |

**Acceptance Criteria:**

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-001 | Pipeline executes 3 validators in parallel | Unit test with asyncio.gather mock | All validators start simultaneously (within 100ms) |
| AC-002 | Pipeline p95 latency <6 minutes | Load test with 100 PRs | 95% complete in <360s |
| AC-003 | Timeout protection at 10 minutes per validator | Integration test with slow validator | Validator cancelled, TIMEOUT status returned |
| AC-004 | Tier-based blocking logic (PROFESSIONAL blocks on coverage failure) | Unit test with tier="PROFESSIONAL", coverage=75% | PipelineResult.status = "FAILED", blocking |
| AC-005 | Non-blocking failure warning (STANDARD allows coverage failure) | Unit test with tier="STANDARD", coverage=75% | PipelineResult.status = "PASSED", warning added |
| AC-006 | Prometheus metrics incremented | Integration test with metrics mock | Histograms + counters updated correctly |

---

### FR-002: BaseValidator Abstract Class Interface

**Description**: BaseValidator defines the contract all validators must implement, with abstract validate() method, ValidatorResult return type, and timeout handling.

**BDD Requirements:**

```gherkin
Feature: BaseValidator Abstract Class
  As a Validator Developer
  I want a standard interface contract
  So that new validators can be added without changing pipeline code

  Background:
    Given BaseValidator abstract class is defined in validators/base.py
    And ValidatorResult dataclass is imported from validators/models.py
    And ABC (Abstract Base Class) module is available

  Scenario: Validator implements required interface
    Given CustomValidator class inherits from BaseValidator
    When CustomValidator defines async def validate(self, context: ValidationContext) -> ValidatorResult
    Then CustomValidator can be registered with ValidationPipeline
    And ValidationPipeline.validate() calls CustomValidator.validate() via polymorphism

  Scenario: Validator missing validate() method (abstract method not implemented)
    Given IncompleteValidator class inherits from BaseValidator
    But IncompleteValidator does NOT define validate() method
    When IncompleteValidator() is instantiated
    Then TypeError is raised with message "Can't instantiate abstract class IncompleteValidator with abstract method validate"
    And IncompleteValidator cannot be registered with ValidationPipeline

  Scenario: ValidatorResult return type validation
    Given LintValidator.validate() is called with ValidationContext(pr_id="123", files=["main.py"])
    When LintValidator returns invalid type (dict instead of ValidatorResult)
    Then ValidationPipeline raises TypeError: "Expected ValidatorResult, got <class 'dict'>"
    And Prometheus counter "validation_type_error_total" is incremented

  Scenario: Timeout handling via asyncio.wait_for
    Given BaseValidator.validate() has no built-in timeout (relies on pipeline timeout)
    When ValidationPipeline wraps validator with asyncio.wait_for(validator.validate(), timeout=600)
    And validator execution exceeds 600 seconds
    Then asyncio.TimeoutError is raised
    And ValidationPipeline catches exception, returns ValidatorResult(status="TIMEOUT")
```

**Tier-Specific Requirements:**

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| Abstract validate() method | YES | YES | YES | YES |
| ValidatorResult return type | YES | YES | YES | YES |
| ValidationContext input type | YES | YES | YES | YES |
| Timeout handling (pipeline-level) | YES | YES | YES | YES |
| Exception handling (pipeline-level) | YES | YES | YES | YES |
| Type hints (Python 3.11+) | YES | YES | YES | YES |
| Docstring (Google style) | RECOMMENDED | RECOMMENDED | MANDATORY | MANDATORY |

**Acceptance Criteria:**

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-007 | BaseValidator is abstract (cannot instantiate directly) | Unit test: BaseValidator() | TypeError raised |
| AC-008 | Subclass must implement validate() method | Unit test: class without validate() | TypeError on instantiation |
| AC-009 | validate() method signature enforced | Static type check with mypy | No type errors |
| AC-010 | ValidatorResult return type enforced | Runtime type check in pipeline | TypeError if wrong type returned |
| AC-011 | ValidationContext contains pr_id, files, tier, config | Unit test with ValidationContext creation | All fields populated correctly |

---

### FR-003: LintValidator Implementation

**Description**: LintValidator implements BaseValidator interface, executes ruff (Python) and ESLint (TypeScript) linters, and returns ValidatorResult with linting errors.

**BDD Requirements:**

```gherkin
Feature: LintValidator for Python and TypeScript
  As a Code Quality Engineer
  I want automatic linting of AI-generated code
  So that style violations are caught before merge

  Background:
    Given LintValidator class inherits from BaseValidator
    And ruff CLI is installed (version 0.1.0+)
    And ESLint CLI is installed (version 8.0.0+)
    And linting config files exist (.ruffignore, .eslintrc.json)

  Scenario: Python file linting (ruff) - no errors
    Given PR #127 has Python file "auth_service.py" with clean code
    When LintValidator.validate(context) is called with files=["auth_service.py"]
    Then ruff command is executed: "ruff check auth_service.py --format json"
    And ruff returns exit code 0 (no errors)
    And ValidatorResult(status="PASSED", message="No linting errors (ruff)", details={}) is returned
    And execution time <2 minutes (p95)

  Scenario: Python file linting (ruff) - errors found
    Given PR #128 has Python file "models.py" with 2 linting errors:
      | Line | Rule | Message |
      | 42 | E501 | Line too long (120 > 88 characters) |
      | 55 | F401 | Unused import 'datetime' |
    When LintValidator.validate(context) is called with files=["models.py"]
    Then ruff command is executed: "ruff check models.py --format json"
    And ruff returns exit code 1 (errors found)
    And ValidatorResult(status="FAILED", message="2 linting errors found", details={"errors": [...]}) is returned
    And details contain exact line numbers and error messages

  Scenario: TypeScript file linting (ESLint) - no errors
    Given PR #129 has TypeScript file "utils.ts" with clean code
    When LintValidator.validate(context) is called with files=["utils.ts"]
    Then ESLint command is executed: "eslint utils.ts --format json"
    And ESLint returns exit code 0 (no errors)
    And ValidatorResult(status="PASSED", message="No linting errors (ESLint)", details={}) is returned

  Scenario: Mixed files (Python + TypeScript) - errors in both
    Given PR #130 has files: ["auth.py", "api.ts"]
    And "auth.py" has 1 ruff error (F401 unused import)
    And "api.ts" has 1 ESLint error (no-console)
    When LintValidator.validate(context) is called with files=["auth.py", "api.ts"]
    Then ruff and ESLint execute in parallel (asyncio.gather)
    And ValidatorResult(status="FAILED", message="2 linting errors found (1 ruff, 1 ESLint)", details={...}) is returned
    And details contain errors grouped by linter type

  Scenario: Linter command timeout (ruff exceeds 2 minutes)
    Given PR #131 has large Python file "huge_module.py" (10,000 LOC)
    When LintValidator.validate(context) is called with timeout=120s
    And ruff execution exceeds 2 minutes
    Then subprocess is killed (asyncio.wait_for timeout)
    And ValidatorResult(status="TIMEOUT", message="Linting exceeded 120s limit") is returned
```

**Tier-Specific Requirements:**

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| ruff linter (Python) | RECOMMENDED | MANDATORY | MANDATORY | MANDATORY |
| ESLint linter (TypeScript) | RECOMMENDED | MANDATORY | MANDATORY | MANDATORY |
| Linting config files | RECOMMENDED | MANDATORY | MANDATORY | MANDATORY |
| Max line length (Python) | 120 | 100 | 88 | 88 |
| Max line length (TypeScript) | 120 | 100 | 100 | 100 |
| Blocking on lint failure | NO | YES | YES | YES |
| p95 latency target | <3 min | <2 min | <2 min | <2 min |
| Parallel execution (multi-file) | YES | YES | YES | YES |

**Acceptance Criteria:**

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-012 | ruff linter executes for Python files | Integration test with sample .py file | ruff command called, exit code checked |
| AC-013 | ESLint executes for TypeScript files | Integration test with sample .ts file | eslint command called, exit code checked |
| AC-014 | Linting errors returned in ValidatorResult.details | Unit test with mock ruff output | Errors parsed correctly from JSON |
| AC-015 | p95 latency <2 minutes for 10 files | Load test with 10 files (500 LOC each) | 95% complete in <120s |
| AC-016 | Timeout protection at 2 minutes | Integration test with slow linter | Subprocess killed, TIMEOUT status returned |
| AC-017 | Parallel execution for mixed Python+TypeScript | Unit test with 2 files | ruff and ESLint run concurrently |

---

### FR-004: TestValidator Implementation

**Description**: TestValidator implements BaseValidator interface, executes pytest (Python) and vitest (TypeScript) test suites, and returns ValidatorResult with test results.

**BDD Requirements:**

```gherkin
Feature: TestValidator for Python and TypeScript
  As a QA Engineer
  I want automatic test execution for AI-generated code
  So that functional regressions are caught before merge

  Background:
    Given TestValidator class inherits from BaseValidator
    And pytest CLI is installed (version 7.0.0+)
    And vitest CLI is installed (version 1.0.0+)
    And test files exist in tests/ directory

  Scenario: Python tests (pytest) - all passing
    Given PR #132 has Python file "auth_service.py" with corresponding tests in "tests/test_auth_service.py"
    And "tests/test_auth_service.py" contains 5 test cases
    When TestValidator.validate(context) is called with files=["auth_service.py"]
    Then pytest command is executed: "pytest tests/test_auth_service.py -v --json-report"
    And pytest returns exit code 0 (all tests passed)
    And ValidatorResult(status="PASSED", message="5/5 tests passed", details={"total": 5, "passed": 5, "failed": 0}) is returned
    And execution time <5 minutes (p95)

  Scenario: Python tests (pytest) - failures detected
    Given PR #133 has Python file "user_service.py" with tests in "tests/test_user_service.py"
    And 2 out of 8 test cases fail:
      | Test | Failure Reason |
      | test_create_user_invalid_email | AssertionError: Email validation failed |
      | test_delete_user_not_found | Expected 404, got 500 |
    When TestValidator.validate(context) is called with files=["user_service.py"]
    Then pytest command is executed: "pytest tests/test_user_service.py -v --json-report"
    And pytest returns exit code 1 (test failures)
    And ValidatorResult(status="FAILED", message="2/8 tests failed", details={"failures": [...]}) is returned
    And details contain exact test names and failure reasons

  Scenario: TypeScript tests (vitest) - all passing
    Given PR #134 has TypeScript file "utils.ts" with tests in "tests/utils.test.ts"
    And "tests/utils.test.ts" contains 3 test suites with 12 test cases
    When TestValidator.validate(context) is called with files=["utils.ts"]
    Then vitest command is executed: "vitest run tests/utils.test.ts --reporter=json"
    And vitest returns exit code 0 (all tests passed)
    And ValidatorResult(status="PASSED", message="12/12 tests passed", details={...}) is returned

  Scenario: Mixed tests (Python + TypeScript) - failures in both
    Given PR #135 has files: ["auth.py", "api.ts"]
    And "tests/test_auth.py" has 1 failing test
    And "tests/api.test.ts" has 2 failing tests
    When TestValidator.validate(context) is called with files=["auth.py", "api.ts"]
    Then pytest and vitest execute in parallel (asyncio.gather)
    And ValidatorResult(status="FAILED", message="3 tests failed (1 pytest, 2 vitest)", details={...}) is returned

  Scenario: Test timeout (pytest exceeds 5 minutes)
    Given PR #136 has slow integration tests (execution time >5 minutes)
    When TestValidator.validate(context) is called with timeout=300s
    And pytest execution exceeds 5 minutes
    Then subprocess is killed (asyncio.wait_for timeout)
    And ValidatorResult(status="TIMEOUT", message="Testing exceeded 300s limit") is returned
```

**Tier-Specific Requirements:**

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| pytest (Python) | OPTIONAL | RECOMMENDED | MANDATORY | MANDATORY |
| vitest (TypeScript) | OPTIONAL | RECOMMENDED | MANDATORY | MANDATORY |
| Test files required | NO | YES | YES | YES |
| Minimum test coverage (files tested) | N/A | 50% | 80% | 100% |
| Blocking on test failure | NO | NO | YES | YES |
| p95 latency target | <10 min | <7 min | <5 min | <5 min |
| Parallel execution (multi-file) | YES | YES | YES | YES |
| Test report format | Plain text | JSON | JSON | JSON |

**Acceptance Criteria:**

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-018 | pytest executes for Python files | Integration test with sample test file | pytest command called, exit code checked |
| AC-019 | vitest executes for TypeScript files | Integration test with sample test file | vitest command called, exit code checked |
| AC-020 | Test failures returned in ValidatorResult.details | Unit test with mock pytest output | Failures parsed correctly from JSON |
| AC-021 | p95 latency <5 minutes for 20 test files | Load test with 20 test files (10 tests each) | 95% complete in <300s |
| AC-022 | Timeout protection at 5 minutes | Integration test with slow tests | Subprocess killed, TIMEOUT status returned |
| AC-023 | Parallel execution for mixed Python+TypeScript | Unit test with 2 test files | pytest and vitest run concurrently |

---

### FR-005: CoverageValidator Implementation

**Description**: CoverageValidator implements BaseValidator interface, executes pytest-cov (Python coverage.py wrapper) to measure test coverage, and returns ValidatorResult with coverage percentage.

**BDD Requirements:**

```gherkin
Feature: CoverageValidator for Python Test Coverage
  As a QA Engineer
  I want automatic coverage measurement for AI-generated code
  So that untested code is caught before merge

  Background:
    Given CoverageValidator class inherits from BaseValidator
    And pytest-cov plugin is installed (version 4.0.0+)
    And coverage threshold is configured per tier (PROFESSIONAL: 80%)

  Scenario: Python coverage (pytest-cov) - meets threshold
    Given PR #137 has Python file "auth_service.py" with 100 LOC
    And "tests/test_auth_service.py" covers 85 LOC
    And tier="PROFESSIONAL" (threshold 80%)
    When CoverageValidator.validate(context) is called with files=["auth_service.py"]
    Then pytest command is executed: "pytest --cov=auth_service --cov-report=json"
    And pytest-cov returns coverage report: {"totals": {"percent_covered": 85.0}}
    And ValidatorResult(status="PASSED", message="Coverage 85% >= 80%", details={"coverage": 85.0}) is returned
    And execution time <5 minutes (p95)

  Scenario: Python coverage (pytest-cov) - below threshold
    Given PR #138 has Python file "user_service.py" with 200 LOC
    And "tests/test_user_service.py" covers 140 LOC (70% coverage)
    And tier="PROFESSIONAL" (threshold 80%)
    When CoverageValidator.validate(context) is called with files=["user_service.py"]
    Then pytest command is executed: "pytest --cov=user_service --cov-report=json"
    And pytest-cov returns coverage report: {"totals": {"percent_covered": 70.0}}
    And ValidatorResult(status="FAILED", message="Coverage 70% < 80%", details={"coverage": 70.0, "missing_lines": [...]}) is returned

  Scenario: Coverage non-blocking in STANDARD tier
    Given PR #139 has Python file "utils.py" with 75% coverage
    And tier="STANDARD" (coverage is RECOMMENDED, threshold 70%)
    When CoverageValidator.validate(context) is called
    Then pytest-cov returns coverage 75% >= 70%
    And ValidatorResult(status="PASSED", message="Coverage 75% >= 70%", details={...}) is returned
    And PR is allowed to merge (coverage is RECOMMENDED in STANDARD tier)

  Scenario: Coverage blocking in ENTERPRISE tier
    Given PR #140 has Python file "payment.py" with 88% coverage
    And tier="ENTERPRISE" (threshold 90%)
    When CoverageValidator.validate(context) is called
    Then pytest-cov returns coverage 88% < 90%
    And ValidatorResult(status="FAILED", message="Coverage 88% < 90%", details={...}) is returned
    And PR is blocked from merging (coverage is MANDATORY in ENTERPRISE tier)

  Scenario: Coverage timeout (pytest-cov exceeds 5 minutes)
    Given PR #141 has large test suite (1000+ tests)
    When CoverageValidator.validate(context) is called with timeout=300s
    And pytest-cov execution exceeds 5 minutes
    Then subprocess is killed (asyncio.wait_for timeout)
    And ValidatorResult(status="TIMEOUT", message="Coverage measurement exceeded 300s limit") is returned
```

**Tier-Specific Requirements:**

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| pytest-cov plugin | OPTIONAL | RECOMMENDED | MANDATORY | MANDATORY |
| Coverage threshold | N/A | 70% | 80% | 90% |
| Blocking on coverage failure | NO | NO | YES | YES |
| Coverage report format | N/A | JSON | JSON | JSON |
| Missing lines reported | NO | YES | YES | YES |
| p95 latency target | N/A | <7 min | <5 min | <5 min |
| Branch coverage (not just line coverage) | NO | NO | RECOMMENDED | MANDATORY |

**Acceptance Criteria:**

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-024 | pytest-cov executes for Python files | Integration test with sample test file | pytest --cov command called |
| AC-025 | Coverage threshold enforced per tier | Unit test with tier="PROFESSIONAL", coverage=75% | ValidatorResult.status = "FAILED" |
| AC-026 | Coverage percentage returned in details | Unit test with mock coverage report | details["coverage"] = 85.0 |
| AC-027 | Missing lines reported in details | Unit test with mock coverage report | details["missing_lines"] = [42, 55, 67] |
| AC-028 | p95 latency <5 minutes for 50 test files | Load test with 50 test files | 95% complete in <300s |
| AC-029 | Timeout protection at 5 minutes | Integration test with slow tests | Subprocess killed, TIMEOUT status returned |

---

### FR-006: Redis Queue Architecture

**Description**: Redis queue architecture provides asynchronous validation processing with FIFO queue, retry sorted set, and processing hash for distributed worker coordination.

**BDD Requirements:**

```gherkin
Feature: Redis Queue for Async Validation
  As a Backend Engineer
  I want asynchronous validation processing
  So that API responses are not blocked by long-running validators

  Background:
    Given Redis server is running (version 7.0+)
    And Redis queues are configured:
      | Queue Key | Type | Purpose |
      | validation:queue | LIST | FIFO queue for new validation requests |
      | validation:retry | ZSET | Sorted set for retry scheduling (score = retry_at timestamp) |
      | validation:processing | HASH | Hash of currently processing validations (key = pr_id, value = worker_id) |
    And ValidationWorker background process is running

  Scenario: Enqueue validation request (async API response)
    Given POST /api/v1/validations endpoint receives request: {"pr_id": "142", "files": ["auth.py"]}
    When ValidationService.enqueue_validation(pr_id="142", files=["auth.py"]) is called
    Then Redis RPUSH validation:queue '{"pr_id": "142", "files": ["auth.py"], "enqueued_at": "2026-01-31T10:00:00Z"}'
    And HTTP 202 Accepted response is returned immediately (no blocking)
    And Response body contains: {"validation_id": "val_142", "status": "PENDING", "queue_position": 5}
    And API response time <100ms (p95)

  Scenario: Worker dequeues and processes validation request
    Given validation:queue contains 3 pending requests
    When ValidationWorker calls Redis BLPOP validation:queue timeout=30
    Then oldest request is dequeued: {"pr_id": "142", "files": ["auth.py"]}
    And Redis HSET validation:processing "142" "worker_abc123"
    And ValidationPipeline.validate(pr_id="142", files=["auth.py"]) is executed
    And PipelineResult is stored in database (validation_results table)
    And Redis HDEL validation:processing "142" (remove from processing hash)
    And Prometheus gauge "validation_queue_processing_count" is decremented

  Scenario: Retry on timeout (exponential backoff)
    Given PR #143 validation timed out (retry_count=0)
    When ValidationWorker encounters timeout (ValidatorResult.status="TIMEOUT")
    Then retry_at = current_time + (10s * 2^retry_count) = current_time + 10s
    And Redis ZADD validation:retry retry_at {"pr_id": "143", "retry_count": 1}
    And ValidationWorker continues processing next item in queue (non-blocking)
    And After 10 seconds, ValidationWorker moves item from validation:retry to validation:queue
    And PR #143 is retried (retry_count=1)

  Scenario: Max retries exceeded (3 retries)
    Given PR #144 validation timed out 3 times (retry_count=3)
    When ValidationWorker encounters timeout again
    Then retry_count=4 exceeds max_retries=3
    And ValidatorResult(status="ERROR", message="Max retries (3) exceeded") is stored
    And Redis HDEL validation:processing "144"
    And PR #144 is marked as FAILED (no further retries)
    And Prometheus counter "validation_max_retries_exceeded_total" is incremented

  Scenario: Queue wait time monitoring (<30s p95)
    Given validation:queue has 10 pending requests
    When new validation is enqueued at timestamp T0
    And ValidationWorker dequeues request at timestamp T1
    Then queue_wait_time = T1 - T0
    And Prometheus histogram "validation_queue_wait_seconds" records queue_wait_time
    And Alert fires if p95 queue_wait_time >30 seconds
```

**Tier-Specific Requirements:**

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| Redis queue enabled | YES | YES | YES | YES |
| FIFO queue (validation:queue) | YES | YES | YES | YES |
| Retry sorted set (validation:retry) | YES | YES | YES | YES |
| Processing hash (validation:processing) | YES | YES | YES | YES |
| Max retries | 1 | 2 | 3 | 3 |
| Retry backoff base | 10s | 10s | 10s | 10s |
| Retry backoff max | 60s | 120s | 300s | 300s |
| Queue wait p95 target | <60s | <45s | <30s | <30s |
| Worker count | 1 | 2 | 4 | 8 |
| Queue priority (multiple queues) | NO | NO | YES (high/normal/low) | YES (high/normal/low) |

**Acceptance Criteria:**

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-030 | Enqueue validation returns 202 Accepted immediately | Integration test with API call | Response time <100ms |
| AC-031 | Worker dequeues FIFO (oldest request first) | Unit test with 3 enqueued requests | Requests processed in order |
| AC-032 | Retry on timeout with exponential backoff | Unit test with retry_count=0,1,2 | Backoff = 10s, 20s, 40s |
| AC-033 | Max retries (3) enforced | Unit test with retry_count=4 | STATUS = "ERROR", no retry |
| AC-034 | Queue wait time <30s (p95) | Load test with 100 requests | 95% dequeued in <30s |
| AC-035 | Processing hash tracks active validations | Integration test with worker | HSET on start, HDEL on complete |

---

### FR-007: Prometheus Metrics Integration

**Description**: Prometheus metrics track validation pipeline performance (duration histograms, result counters, queue gauges) for monitoring and alerting.

**BDD Requirements:**

```gherkin
Feature: Prometheus Metrics for Validation Pipeline
  As a DevOps Engineer
  I want Prometheus metrics for validation monitoring
  So that performance issues and failures are alerted

  Background:
    Given Prometheus exporter is running on port 9090
    And Grafana dashboard "Validation Pipeline" is configured
    And AlertManager is configured with validation alerts

  Scenario: Duration histogram (validation_pipeline_duration_seconds)
    Given ValidationPipeline.validate() completes in 3.5 minutes (210 seconds)
    When PipelineResult is returned
    Then Prometheus histogram "validation_pipeline_duration_seconds" is incremented with value 210
    And Histogram buckets: [30, 60, 120, 180, 240, 300, 360] (30s to 6min)
    And p95 latency can be queried: histogram_quantile(0.95, validation_pipeline_duration_seconds)

  Scenario: Result counters (validation_pipeline_passed_total, validation_pipeline_failed_total)
    Given ValidationPipeline.validate() returns PipelineResult(status="PASSED")
    When PipelineResult is returned
    Then Prometheus counter "validation_pipeline_passed_total" is incremented
    And Counter has labels: {tier="PROFESSIONAL", blocking="true"}
    And Counter can be queried: rate(validation_pipeline_passed_total[5m])

  Scenario: Queue gauges (validation_queue_size, validation_queue_processing_count)
    Given validation:queue has 15 pending requests
    And validation:processing has 3 active workers
    When ValidationWorker queries Redis queue
    Then Prometheus gauge "validation_queue_size" is set to 15
    And Prometheus gauge "validation_queue_processing_count" is set to 3
    And Gauges can be queried: validation_queue_size / validation_queue_processing_count (queue/worker ratio)

  Scenario: Alert firing (p95 latency >6 minutes)
    Given validation_pipeline_duration_seconds p95 is 8 minutes (480 seconds)
    And alerting rule: histogram_quantile(0.95, validation_pipeline_duration_seconds) > 360
    When AlertManager evaluates rule
    Then alert "ValidationPipelineSlowP95" fires
    And alert severity: WARNING
    And alert message: "Validation pipeline p95 latency (480s) exceeds 6 minutes threshold"
    And Slack notification sent to #platform-alerts channel
```

**Tier-Specific Requirements:**

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| Prometheus metrics enabled | YES | YES | YES | YES |
| Duration histogram | YES | YES | YES | YES |
| Result counters (passed/failed/timeout/error) | YES | YES | YES | YES |
| Queue gauges (size/processing) | YES | YES | YES | YES |
| Validator-specific metrics | NO | YES | YES | YES |
| Grafana dashboard | NO | YES | YES | YES |
| AlertManager alerts | NO | NO | YES | YES |
| Metrics retention | 7 days | 14 days | 30 days | 90 days |

**Acceptance Criteria:**

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-036 | Duration histogram incremented on pipeline complete | Integration test with mock Prometheus | Histogram value = actual duration |
| AC-037 | Result counters incremented per status | Unit test with PASSED/FAILED/TIMEOUT/ERROR | Counters increment correctly |
| AC-038 | Queue gauges reflect current queue state | Integration test with Redis queue | Gauges = actual queue size/processing count |
| AC-039 | Metrics exposed on /metrics endpoint | HTTP GET /metrics | Prometheus format metrics returned |
| AC-040 | Alert fires when p95 latency >6 minutes | Integration test with AlertManager mock | Alert triggered, Slack notification sent |

---

## 3. Non-Functional Requirements

### 3.1 Performance

| Metric | Target | Tier | Measurement |
|--------|--------|------|-------------|
| Pipeline p95 Latency | <6 minutes | ALL | End-to-end validation time |
| Lint p95 Latency | <2 minutes | ALL | ruff + ESLint execution time |
| Test p95 Latency | <5 minutes | STANDARD+ | pytest + vitest execution time |
| Coverage p95 Latency | <5 minutes | PROFESSIONAL+ | pytest-cov execution time |
| Queue Wait p95 | <30 seconds | ALL | Redis queue → worker pickup time |
| API Response Time (enqueue) | <100ms | ALL | POST /api/v1/validations response time |

### 3.2 Reliability

| Metric | Target | Tier |
|--------|--------|------|
| Validator Timeout Protection | 10 minutes per validator | ALL |
| Max Pipeline Duration | 15 minutes | ALL |
| Retry on Timeout | 1-3 retries (tier-dependent) | ALL |
| Non-blocking Validator Failures | Warnings only (tier-dependent) | LITE, STANDARD |
| Blocking Rate | <20% | ALL |
| False Positive Rate | <5% | ALL |

### 3.3 Scalability

| Metric | Target | Tier |
|--------|--------|------|
| Concurrent Validations | 100+ | ENTERPRISE |
| Queue Throughput | 500+ validations/hour | ENTERPRISE |
| Worker Count | 1-8 (tier-dependent) | ALL |
| Redis Queue Size | 1000+ pending requests | ENTERPRISE |

---

## 4. Data Models

### 4.1 ValidatorResult (Dataclass)

```python
@dataclass
class ValidatorResult:
    """Result from a single validator execution"""
    status: ValidatorStatus  # Enum: PASSED, FAILED, SKIPPED, ERROR, TIMEOUT
    message: str  # Human-readable message (e.g., "2 linting errors found")
    details: dict  # Validator-specific details (e.g., {"errors": [...]})
    duration_ms: int  # Execution time in milliseconds
    validator_name: str  # Class name (e.g., "LintValidator")
```

### 4.2 PipelineResult (Dataclass)

```python
@dataclass
class PipelineResult:
    """Aggregated result from validation pipeline"""
    status: ValidationStatus  # Enum: PENDING, RUNNING, PASSED, FAILED, ERROR
    message: str  # Overall message (e.g., "Validation passed")
    validator_results: list[ValidatorResult]  # Results from each validator
    blocking_validators: list[str]  # Validators that blocked (FAILED status)
    non_blocking_validators: list[str]  # Validators that failed but didn't block
    warnings: list[str]  # Non-blocking warnings
    total_duration_ms: int  # Total pipeline execution time
    started_at: datetime  # Validation start timestamp
    completed_at: datetime  # Validation complete timestamp
```

### 4.3 ValidationContext (Dataclass)

```python
@dataclass
class ValidationContext:
    """Context passed to validators"""
    pr_id: str  # Pull request ID
    files: list[str]  # Files to validate
    tier: str  # Project tier (LITE, STANDARD, PROFESSIONAL, ENTERPRISE)
    config: dict  # Validator-specific config (e.g., {"coverage_threshold": 80})
    enqueued_at: datetime  # When validation was enqueued
    retry_count: int  # Number of retry attempts (default: 0)
```

---

## 5. Cross-References

### 5.1 Related Specifications

- **SPEC-0001**: Anti-Vibecoding Specification (SecurityValidator integration)
- **SPEC-0002**: Quality Gates Specification (ContextValidator integration)
- **SPEC-0009**: Codegen Service Specification (code generation triggers validation)
- **SPEC-0010**: IR Processor Specification (backend scaffold validation)
- **SPEC-0011**: AI Task Decomposition (task-based validation triggers)

### 5.2 External Dependencies

- **ruff**: Python linter (0.1.0+)
- **ESLint**: TypeScript linter (8.0.0+)
- **pytest**: Python testing framework (7.0.0+)
- **vitest**: TypeScript testing framework (1.0.0+)
- **pytest-cov**: Python coverage plugin (4.0.0+)
- **Redis**: Queue backend (7.0+)
- **Prometheus**: Metrics exporter (2.40.0+)

---

## 6. Glossary

| Term | Definition |
|------|------------|
| **ValidationPipeline** | Orchestration service that executes validators in parallel |
| **BaseValidator** | Abstract class defining validator contract (validate() method) |
| **LintValidator** | Validator that executes ruff (Python) and ESLint (TypeScript) |
| **TestValidator** | Validator that executes pytest (Python) and vitest (TypeScript) |
| **CoverageValidator** | Validator that measures test coverage with pytest-cov |
| **ValidatorResult** | Dataclass containing single validator execution result |
| **PipelineResult** | Dataclass containing aggregated pipeline result |
| **ValidationContext** | Dataclass containing context passed to validators |
| **Blocking Validator** | Validator that prevents PR merge on failure (tier-dependent) |
| **Non-blocking Validator** | Validator that allows PR merge with warning on failure |
| **FIFO Queue** | First-In-First-Out queue for validation requests (Redis LIST) |
| **Retry Sorted Set** | Redis ZSET for retry scheduling (score = retry_at timestamp) |
| **Processing Hash** | Redis HASH tracking active validations (worker coordination) |
| **Exponential Backoff** | Retry delay strategy: 10s, 20s, 40s, 80s, max 300s |
| **p95 Latency** | 95th percentile latency (95% of requests complete within this time) |

---

**Specification Complete** - SPEC-0012: Validation Pipeline Interface v1.0.0

**Total**: ~700 LOC, 7 functional requirements, 40 acceptance criteria, 3 validators (Lint/Test/Coverage), Redis queue architecture, Prometheus metrics integration

---
