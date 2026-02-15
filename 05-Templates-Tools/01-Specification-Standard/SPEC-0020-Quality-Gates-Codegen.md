# SPEC-0020: Quality Gates for Generated Code

## Frontmatter

```yaml
spec_id: SPEC-0020
title: Quality Gates for Generated Code
version: 2.0.0
status: approved
tier: PROFESSIONAL
pillar: Section 7 - Quality Assurance System
owner: Backend Lead + QA Lead
last_updated: 2026-01-29
tags:
  - codegen
  - quality-gates
  - validation
  - ep-06
  - ollama
  - vietnamese
related_specs:
  - SPEC-0009  # Codegen Service Specification
  - SPEC-0010  # IR Processor Specification
  - SPEC-0012  # Validation Pipeline Interface
epic: EP-06 IR-Based Codegen Engine
sprint: Sprint 48 (Feb 17-28, 2026)
implementation_ref: "SDLC-Orchestrator/docs/02-design/14-Technical-Specs/Quality-Gates-Codegen-Specification.md"
```

---

## 1. Overview

### 1.1 Purpose

Define a 4-gate quality validation pipeline that ensures all AI-generated code meets production standards before delivery to users, targeting ≥95% pass rate for cost-effective Vietnamese SME deployments.

### 1.2 Strategic Context

**EP-06 Founder Plan Targets**:
- Infrastructure cost: <$50/month per project
- Generation + validation latency: <3s (p95)
- Quality gate pass rate: ≥95%
- Vietnamese error messages: 100% coverage

```
┌─────────────────────────────────────────────────────────────────────┐
│                    QUALITY GATE PIPELINE                             │
│                                                                      │
│  Generated Code → [Gate 1] → [Gate 2] → [Gate 3] → [Gate 4] → ✅    │
│                   Syntax     Security   Arch      Tests              │
│                   <500ms     <1s        <800ms    <60s               │
│                                                                      │
│  If ANY gate fails:                                                  │
│  → Return detailed errors in Vietnamese                              │
│  → Suggest auto-fixes (Gate 1-2 only)                                │
│  → Option to retry with fallback provider                            │
│  → Store failure patterns for learning                               │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.3 Scope

| **In Scope** | **Out of Scope** |
|--------------|------------------|
| 4 validation gates (Syntax, Security, Architecture, Tests) | Runtime performance profiling |
| Vietnamese error translation (100% coverage) | Load/stress testing |
| Auto-fix suggestions (Gate 1-2) | Security penetration testing |
| Ollama optimization (caching, prompt tuning) | External API integration tests |
| Cost tracking per project/provider | Multi-region deployment |
| Validation metrics dashboard | Real-time monitoring alerts |

---

## 2. Functional Requirements

### FR-01: Four-Gate Validation Pipeline

**Requirement Statement**: System SHALL implement a sequential 4-gate pipeline (Syntax → Security → Architecture → Tests) that validates all generated code with deterministic pass/fail criteria and Vietnamese error reporting.

**BDD Specification**:

```gherkin
Feature: Four-Gate Validation Pipeline
  As a Vietnamese SME developer
  I want generated code validated through 4 quality gates
  So that I receive production-ready code with Vietnamese error explanations

  Background:
    GIVEN user has generated Python code from IR blueprint
    AND code contains 3 files: models/user.py, services/user_service.py, tests/test_user.py

  Scenario: All gates pass - Code is production-ready
    GIVEN Gate 1 (Syntax) validates all files with ast.parse
    AND Gate 2 (Security) runs Semgrep with 0 critical/high issues
    AND Gate 3 (Architecture) validates layer dependencies (no violations)
    AND Gate 4 (Tests) executes pytest with 100% pass rate
    WHEN QualityGatePipeline.run(files, blueprint) is called
    THEN result.passed == True
    AND result.total_duration_ms < 3000
    AND result.vietnamese_summary == "✅ Tất cả các gate đều PASS. Code sẵn sàng sử dụng."
    AND all 4 gates return passed=True

  Scenario: Gate 1 fails - Syntax errors detected
    GIVEN models/user.py contains "def create_user(name:" (missing closing paren)
    WHEN Gate 1 (SyntaxValidator) validates the file
    THEN gate_result.passed == False
    AND issues[0].file == "models/user.py"
    AND issues[0].vietnamese_message == "Cú pháp không hợp lệ"
    AND pipeline stops at Gate 1 (Gates 2-4 not executed)

  Scenario: Gate 2 fails - Security vulnerability detected
    GIVEN user_service.py contains "cursor.execute(query % user_input)"
    WHEN Gate 2 (SecurityValidator) runs Semgrep
    THEN gate_result.passed == False
    AND issues[0].rule_id == "sql-injection"
    AND issues[0].severity == "high"
    AND issues[0].vietnamese_message == "Lỗ hổng SQL Injection - Dữ liệu người dùng không được escape"
    AND issues[0].fix_suggestion contains "Use parameterized queries"

  Scenario: Gate 3 fails - Architecture violation detected
    GIVEN models/user.py imports "from app.services.auth_service import AuthService"
    WHEN Gate 3 (ArchitectureValidator) checks layer dependencies
    THEN gate_result.passed == False
    AND issues[0].rule == "layer-dependency"
    AND issues[0].vietnamese_message == "Tầng 'models' không nên import từ 'services'"

  Scenario: Gate 4 fails - Tests fail execution
    GIVEN tests/test_user.py has assertion "assert result == 5" but result == 4
    WHEN Gate 4 (TestValidator) runs pytest
    THEN gate_result.passed == False
    AND result.tests_run == 1
    AND result.tests_passed == 0
    AND result.tests_failed == 1
    AND results[0].error_message contains "AssertionError"
```

**Data Requirements**:

Validation Record Structure:

| Field | Purpose | Required |
|-------|---------|----------|
| Validation ID | Unique identifier | Yes |
| Project reference | Link to owning project | Yes |
| Generation reference | Link to code generation | Yes |
| Pipeline status | passed/failed/error | Yes |
| Total duration | Execution time in milliseconds | Yes |
| Gate 1 result | Syntax validation JSON | Yes |
| Gate 2 result | Security validation JSON | Yes |
| Gate 3 result | Architecture validation JSON | Yes |
| Gate 4 result | Test validation JSON | Yes |
| Total issues | Issue count | Yes |
| Critical issues | Critical issue count | Yes |

Validation Issue Record Structure:

| Field | Purpose | Required |
|-------|---------|----------|
| Issue ID | Unique identifier | Yes |
| Validation reference | Link to validation record | Yes |
| Gate name | syntax/security/architecture/tests | Yes |
| File path | Source file location | Yes |
| Line number | Issue location | No |
| Column number | Issue column | No |
| Issue type | Error classification | Yes |
| Severity | critical/high/medium/low | Yes |
| Message | English error message | Yes |
| Vietnamese message | Localized error message | Yes |
| Fix suggestion | Remediation guidance | No |

> **Implementation Reference**: For database schemas (SQL DDL, indexes), see SDLC-Orchestrator documentation.

**Pipeline Execution Requirements**:

| Requirement | Description |
|-------------|-------------|
| Sequential execution | Gates 1-4 execute in order |
| Fail-fast option | Pipeline stops on Gate 1 failure (syntax) |
| Full report option | Gates 2-4 continue even on failures |
| Timing capture | Each gate duration tracked in milliseconds |
| Vietnamese summary | All results include Vietnamese summary message |
| Error handling | Gate failures captured with error details |

Gate Result Structure:

| Field | Type | Description |
|-------|------|-------------|
| gate_name | String | syntax/security/architecture/tests |
| passed | Boolean | Gate pass/fail status |
| duration_ms | Integer | Execution time in milliseconds |
| details | Object | Gate-specific result data |

Pipeline Result Structure:

| Field | Type | Description |
|-------|------|-------------|
| passed | Boolean | Overall pass/fail status |
| total_duration_ms | Integer | Total execution time |
| gates | Array | List of gate results |
| summary | Object | Gates run/passed/failed counts |
| vietnamese_summary | String | Localized result message |

> **Implementation Reference**: For service classes and validation logic, see SDLC-Orchestrator documentation.

---

### FR-02: Vietnamese Error Translation

**Requirement Statement**: System SHALL translate ALL validation error messages to Vietnamese with context-specific explanations and fix suggestions, achieving 100% coverage for common error types.

**BDD Specification**:

```gherkin
Feature: Vietnamese Error Translation
  As a Vietnamese SME developer
  I want all validation errors in Vietnamese
  So that I can quickly understand and fix issues

  Scenario: Syntax error translation
    GIVEN Python code with "def foo(:" (invalid syntax)
    WHEN SyntaxValidator detects SyntaxError
    THEN error.message == "invalid syntax"
    AND error.vietnamese_message == "Cú pháp không hợp lệ"
    AND error.line and error.column are populated

  Scenario: Security vulnerability translation
    GIVEN code with "password = 'admin123'" (hardcoded secret)
    WHEN SecurityValidator detects hardcoded-secret rule
    THEN error.message == "Hardcoded secret detected"
    AND error.vietnamese_message == "Secret được hardcode - Nên dùng biến môi trường"
    AND error.fix_suggestion == "Use environment variables: os.getenv('PASSWORD')"

  Scenario: Architecture violation translation
    GIVEN models/ layer imports from services/ layer
    WHEN ArchitectureValidator detects layer-dependency violation
    THEN error.rule == "layer-dependency"
    AND error.vietnamese_message == "Tầng 'models' không nên import từ 'services'"
    AND error provides layer dependency diagram

  Scenario: Test failure translation
    GIVEN pytest assertion fails with "assert 5 == 4"
    WHEN TestValidator runs tests
    THEN error.test_name is populated
    AND error.error_message contains "AssertionError: assert 5 == 4"
    AND system provides Vietnamese context in UI
```

**Vietnamese Translation Categories**:

Syntax Errors:

| English Message | Vietnamese Translation |
|-----------------|------------------------|
| invalid syntax | Cú pháp không hợp lệ |
| unexpected indent | Thụt lề không đúng |
| expected an indented block | Thiếu khối thụt lề |
| unexpected EOF | Kết thúc file không mong đợi |
| name 'X' is not defined | Tên 'X' chưa được định nghĩa |

Security Issues:

| Rule ID | Vietnamese Translation |
|---------|------------------------|
| sql-injection | Lỗ hổng SQL Injection - Dữ liệu người dùng không được escape |
| xss | Lỗ hổng XSS - Output không được sanitize |
| hardcoded-secret | Secret được hardcode - Nên dùng biến môi trường |
| insecure-random | Sử dụng random không an toàn - Dùng secrets module |
| path-traversal | Lỗ hổng Path Traversal - Đường dẫn file không được validate |
| command-injection | Lỗ hổng Command Injection - Input không được sanitize |
| eval-usage | Sử dụng eval() nguy hiểm - Tránh dùng eval() |
| shell-injection | Lỗ hổng Shell Injection - Dùng subprocess với shell=False |

Architecture Violations:

| Violation Type | Vietnamese Translation |
|----------------|------------------------|
| layer-dependency | Vi phạm phụ thuộc tầng |
| circular-import | Import vòng được phát hiện |
| naming-convention | Vi phạm quy ước đặt tên |

Test Failures:

| Error Type | Vietnamese Translation |
|------------|------------------------|
| test-timeout | Test chạy quá thời gian cho phép (>120s) |
| test-error | Test gặp lỗi khi thực thi |

> **Implementation Reference**: For complete translation dictionary, see SDLC-Orchestrator documentation.

---

### FR-03: Ollama Cost Optimization

**Requirement Statement**: System SHALL optimize Ollama usage through prompt caching, context window management, and model selection to achieve <$50/month per project operational cost.

**BDD Specification**:

```gherkin
Feature: Ollama Cost Optimization
  As a platform operator
  I want to minimize Ollama inference costs
  So that we achieve <$50/month per project target

  Scenario: Prompt caching for repeated validations
    GIVEN user generates code from same IR blueprint twice
    WHEN OllamaOptimizer receives validation request
    THEN cache_key is computed from (model + prompt) hash
    AND cached response is returned if exists and <1 hour old
    AND no Ollama API call is made (0 tokens used)

  Scenario: Context window management
    GIVEN IR blueprint contains 10,000 tokens
    AND Ollama model has 4096 token context limit
    WHEN OllamaOptimizer.should_use_ollama(10000) is called
    THEN returns False (exceeds 80% of limit)
    AND system falls back to Claude with larger context

  Scenario: Optimized prompt templates
    GIVEN user requests Python FastAPI code generation
    WHEN OllamaOptimizer.optimize_prompt("generate", context) is called
    THEN prompt is concise Vietnamese template (no verbose English explanations)
    AND prompt includes only essential IR fields
    AND estimated tokens reduced by ~40% vs verbose prompt
```

**Ollama Optimization Requirements**:

Caching Requirements:

| Requirement | Description |
|-------------|-------------|
| Cache key | SHA256 hash of (model + prompt) |
| Cache TTL | 1 hour (STANDARD), 24 hours (PROFESSIONAL+) |
| Cache backend | In-memory (STANDARD), Redis (PROFESSIONAL+) |
| Cache hit handling | Return cached response, skip API call |

Context Window Management:

| Requirement | Description |
|-------------|-------------|
| Token estimation | Vietnamese text: ~3 characters per token |
| Threshold | 80% of model context limit |
| Fallback trigger | Exceeds threshold → use Claude |
| Context limits | Ollama: 4096 tokens, Claude: 100K tokens |

Prompt Optimization:

| Prompt Type | Purpose | Token Reduction Target |
|-------------|---------|----------------------|
| generate | Code generation from IR | ~40% vs verbose |
| validate | Code validation | ~40% vs verbose |

Optimization Strategy:

| Strategy | Description |
|----------|-------------|
| Vietnamese prompts | Concise Vietnamese instructions |
| Essential fields only | Include only required IR fields |
| No explanations | Request code only, no comments |

> **Implementation Reference**: For OllamaOptimizer class implementation, see SDLC-Orchestrator documentation.

---

### FR-04: Cost Tracking & Usage Monitoring

**Requirement Statement**: System SHALL track codegen costs per project/user/provider with monthly usage reports and budget alerts when approaching $50/month limit.

**BDD Specification**:

```gherkin
Feature: Cost Tracking & Usage Monitoring
  As a project owner
  I want to monitor codegen costs
  So that I stay within $50/month budget

  Scenario: Track successful generation
    GIVEN user generates code using Ollama (500 tokens, 2000ms)
    WHEN generation completes successfully
    THEN CostTracker.track_usage() is called
    AND codegen_usage record is created with:
      | project_id | user_id | provider | tokens_used | cost_usd | generation_time_ms |
      | proj-123   | user-1  | ollama   | 500         | 0.0005   | 2000               |

  Scenario: Monthly usage report
    GIVEN project has 100 generations in last 30 days
    WHEN CostTracker.get_project_usage(project_id, 30) is called
    THEN returns:
      | total_tokens | total_cost_usd | total_requests | avg_latency_ms |
      | 50000        | 0.50           | 100            | 2500           |

  Scenario: Budget alert triggered
    GIVEN project has used $48 in current month
    WHEN new generation costs $3 (would exceed $50 limit)
    THEN BudgetAlertService sends warning to project owner
    AND suggests upgrading to higher tier or optimizing usage
```

**Cost Tracking Data Requirements**:

Usage Record Structure:

| Field | Purpose | Required |
|-------|---------|----------|
| Usage ID | Unique identifier | Yes |
| Project reference | Link to owning project | Yes |
| User reference | Link to requesting user | Yes |
| Generation reference | Link to code generation | Yes |
| Provider | ollama/claude/gpt4 | Yes |
| Tokens used | Token count | Yes |
| Cost USD | Calculated cost | Yes |
| Generation time | Execution time in ms | Yes |

Budget Record Structure:

| Field | Purpose | Required |
|-------|---------|----------|
| Project reference | Primary key | Yes |
| Monthly limit USD | Budget threshold (default: $50) | Yes |
| Alert threshold | Warning percentage (default: 80%) | Yes |
| Current month usage | Running total | Yes |
| Last alert sent | Alert tracking | No |

> **Implementation Reference**: For database schemas (SQL DDL, indexes), see SDLC-Orchestrator documentation.

---

### FR-05: Validation Performance Budget

**Requirement Statement**: System SHALL complete all 4 gates within 3s (p95) with per-gate budgets: Syntax <500ms, Security <1s, Architecture <800ms, Tests <60s (excluded from budget).

**BDD Specification**:

```gherkin
Feature: Validation Performance Budget
  As a platform operator
  I want fast validation
  So that users receive code within 3s

  Scenario: Performance budget met
    GIVEN generated code has 5 Python files
    WHEN QualityGatePipeline.run() executes
    THEN Gate 1 (Syntax) completes in <500ms
    AND Gate 2 (Security) completes in <1000ms
    AND Gate 3 (Architecture) completes in <800ms
    AND total_duration_ms (Gates 1-3) < 3000

  Scenario: Performance budget violated
    GIVEN Semgrep scan takes 1500ms (exceeds 1000ms budget)
    WHEN pipeline completes
    THEN performance_metrics.gate_2_exceeded == True
    AND alert is sent to operations team
    AND metrics are logged for optimization analysis
```

**Performance Budget Requirements**:

Gate Performance Budgets:

| Gate | Budget (ms) | Counted in 3s SLA |
|------|-------------|-------------------|
| Syntax | 500 | Yes |
| Security | 1000 | Yes |
| Architecture | 800 | Yes |
| Tests | 60000 | No (excluded) |

Monitoring Requirements:

| Requirement | Description |
|-------------|-------------|
| Histogram metrics | Track gate duration by gate_name and project_id |
| Budget alerts | Log warning when budget exceeded |
| Overage tracking | Calculate and log overage milliseconds |
| Operations alerting | Notify operations team on repeated violations |

Performance Tracking Output:

| Field | Description |
|-------|-------------|
| gate | Gate name |
| duration_ms | Actual execution time |
| budget_ms | Budget threshold |
| exceeded | Boolean budget violation flag |

> **Implementation Reference**: For PerformanceTracker class and Prometheus metrics, see SDLC-Orchestrator documentation.

---

### FR-06: Auto-Fix Suggestion System

**Requirement Statement**: System SHALL provide actionable auto-fix suggestions for Syntax and Security gates with one-click apply capability for simple fixes (string escaping, import corrections).

**BDD Specification**:

```gherkin
Feature: Auto-Fix Suggestion System
  As a developer
  I want auto-fix suggestions
  So that I can quickly resolve validation errors

  Scenario: Syntax error auto-fix
    GIVEN code has "def foo(:" (missing closing paren)
    WHEN SyntaxValidator detects error
    THEN fix_suggestion == "Add closing parenthesis: def foo():"
    AND fix_type == "syntax_auto"
    AND user can click "Apply Fix" button

  Scenario: Security vulnerability auto-fix
    GIVEN code has "cursor.execute(f'SELECT * FROM users WHERE id = {user_id}')"
    WHEN SecurityValidator detects SQL injection
    THEN fix_suggestion == "Use parameterized query: cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))"
    AND fix_type == "security_manual"
    AND user must manually review before applying

  Scenario: Architecture violation - no auto-fix
    GIVEN models/ layer imports from services/ layer
    WHEN ArchitectureValidator detects violation
    THEN fix_suggestion explains layer rules
    AND fix_type == "manual_refactor"
    AND no auto-fix button shown
```

---

## 3. Tier-Specific Requirements

| **Feature** | **LITE** | **STANDARD** | **PROFESSIONAL** | **ENTERPRISE** |
|-------------|----------|--------------|------------------|----------------|
| **Gate 1: Syntax Validation** | ✅ Python only | ✅ Python + JS | ✅ Python + JS + TS + YAML | ✅ All languages + custom rules |
| **Gate 2: Security Validation** | ⚠️ Basic (4 rules) | ✅ Standard (12 rules) | ✅ OWASP Top 10 (25 rules) | ✅ Custom Semgrep rules + CWE mapping |
| **Gate 3: Architecture Validation** | ❌ | ⚠️ Basic layer rules | ✅ Full layer rules + circular import detection | ✅ Custom architecture rules + ADR enforcement |
| **Gate 4: Test Execution** | ❌ | ⚠️ Unit tests only | ✅ Unit + Integration tests | ✅ All test types + coverage reports |
| **Vietnamese Error Messages** | ✅ Common errors | ✅ All gates | ✅ All gates + context | ✅ All gates + custom translations |
| **Auto-Fix Suggestions** | ❌ | ⚠️ Syntax only | ✅ Syntax + Security | ✅ All gates + ML-powered suggestions |
| **Cost Tracking** | ❌ | ⚠️ Monthly summary | ✅ Real-time + alerts | ✅ Multi-project + chargebacks |
| **Ollama Caching** | ❌ | ✅ 1-hour TTL | ✅ 24-hour TTL | ✅ Persistent cache + Redis |
| **Performance Budget** | ⚠️ <5s | ✅ <3s (p95) | ✅ <3s (p95) | ✅ <2s (p95) + SLA |
| **Validation Metrics** | ❌ | ⚠️ Basic dashboard | ✅ Grafana dashboard | ✅ Custom dashboards + alerts |

**Legend**:
- ✅ Full feature
- ⚠️ Limited feature
- ❌ Not available

---

## 4. Acceptance Criteria

### AC-01: Four-Gate Pipeline Accuracy

**Test Method**: Integration test with 100 code samples (25 per gate failure type)

**Criteria**:
- ✅ Gate 1 detects 100% of syntax errors (no false negatives)
- ✅ Gate 2 detects ≥95% of OWASP Top 10 vulnerabilities
- ✅ Gate 3 detects ≥90% of architecture violations (layer, circular imports)
- ✅ Gate 4 executes tests with 100% reliability (no timeouts on valid tests)
- ✅ False positive rate <5% across all gates

**Test Requirements**:

Gate 1 Syntax Detection Tests:

| Test Scenario | Input | Expected Result |
|---------------|-------|-----------------|
| Missing parenthesis | `def foo(:` | passed=False, issue detected |
| Missing colon | `if True\n  pass` | passed=False, issue detected |
| Multiple errors | 2 syntax errors | len(issues) == 2 |
| Vietnamese messages | Any syntax error | vietnamese_message populated |

Gate 2 Security Detection Tests:

| Test Scenario | Input | Expected Result |
|---------------|-------|-----------------|
| SQL injection | `cursor.execute(query % user_id)` | passed=False, rule_id contains "sql-injection" |
| Severity classification | Security vulnerability | critical_count + high_count > 0 |

Pipeline Performance Tests:

| Test Scenario | Constraint | Expected Result |
|---------------|------------|-----------------|
| Total pipeline | 5 files | duration_ms < 3000 |
| Gate 1 (Syntax) | Individual gate | duration_ms < 500 |
| Gate 2 (Security) | Individual gate | duration_ms < 1000 |
| Gate 3 (Architecture) | Individual gate | duration_ms < 800 |

> **Implementation Reference**: For pytest test implementations, see SDLC-Orchestrator test suite.

---

### AC-02: Vietnamese Translation Coverage

**Test Method**: Automated test validating 100% coverage of error types

**Criteria**:
- ✅ All syntax error types have Vietnamese translations
- ✅ All security rule IDs have Vietnamese explanations
- ✅ All architecture violations have Vietnamese messages
- ✅ All translations are contextually accurate (reviewed by native speaker)

**Test Requirements**:

Translation Coverage Tests:

| Category | Required Coverage | Verification |
|----------|-------------------|--------------|
| Syntax errors | All common errors | Translation exists and non-empty |
| Security rules | All OWASP Top 10 | Translation exists and meaningful (>10 chars) |
| Architecture violations | All layer rules | Translation exists |
| Test failures | Timeout, error types | Translation exists |

Test Validation Criteria:

| Test | Expected Result |
|------|-----------------|
| Syntax error coverage | "invalid syntax", "unexpected indent", "unexpected EOF" all translated |
| Security rule coverage | "sql-injection", "xss", "hardcoded-secret", "command-injection" all translated |
| Message quality | Translation length > 10 characters (meaningful content) |

> **Implementation Reference**: For translation coverage tests, see SDLC-Orchestrator test suite.

---

### AC-03: Cost Optimization Effectiveness

**Test Method**: Load test simulating 1000 generations over 30 days

**Criteria**:
- ✅ Ollama cache hit rate ≥40% for repeated validations
- ✅ Average cost per project <$50/month (1000 generations)
- ✅ Cost tracking accuracy within 1% of actual provider costs
- ✅ Budget alerts sent when usage reaches 80% of limit

**Test Requirements**:

Cost Optimization Load Test:

| Parameter | Value |
|-----------|-------|
| Test volume | 1000 generations |
| Repeat ratio | 30% repeated IR (same seed) |
| Model | qwen3-coder:30b |
| Cost calculation | $0.001 per 1K tokens |

Expected Results:

| Metric | Target | Verification |
|--------|--------|--------------|
| Cache hit rate | ≥40% | cache_hits / total_requests |
| Total cost | <$50 | Sum of all generation costs |

Test Flow:

| Step | Description |
|------|-------------|
| 1 | Generate IR (30% repeated, 70% random) |
| 2 | Compute cache key from (model + prompt) |
| 3 | Check cache, increment hit counter if found |
| 4 | Calculate cost for cache misses |
| 5 | Validate final metrics against targets |

> **Implementation Reference**: For load test implementations, see SDLC-Orchestrator test suite.

---

### AC-04: Validation Performance SLA

**Test Method**: Performance benchmark with real-world code samples

**Criteria**:
- ✅ p50 latency <1.5s (Gates 1-3 only)
- ✅ p95 latency <3s (Gates 1-3 only)
- ✅ p99 latency <5s (Gates 1-3 only)
- ✅ Gate 4 excluded from SLA (test execution time varies)

**Test Requirements**:

Performance Benchmark Test:

| Parameter | Value |
|-----------|-------|
| File count | 10 files |
| Avg LOC | 100 lines per file |
| Rounds | 100 iterations |
| Measurement | total_duration_ms per run |

SLA Validation Criteria:

| Percentile | Target | Measurement |
|------------|--------|-------------|
| p50 | <1500ms | np.percentile(latencies, 50) |
| p95 | <3000ms | np.percentile(latencies, 95) |
| p99 | <5000ms | np.percentile(latencies, 99) |

Benchmark Methodology:

| Step | Description |
|------|-------------|
| 1 | Generate realistic test files |
| 2 | Load sample IR blueprint |
| 3 | Run pipeline 100 times |
| 4 | Collect latency measurements |
| 5 | Calculate percentiles |
| 6 | Assert against SLA targets |

> **Implementation Reference**: For pytest-benchmark implementations, see SDLC-Orchestrator test suite.

---

### AC-05: Auto-Fix Application Success Rate

**Test Method**: Integration test applying auto-fixes to 50 validation errors

**Criteria**:
- ✅ Syntax auto-fixes applied successfully ≥95% of cases
- ✅ Security auto-fixes applied successfully ≥80% of cases
- ✅ Applied fixes pass validation on retry ≥98% of cases
- ✅ No auto-fix introduces new errors (100% safety)

**Test Requirements**:

Auto-Fix Test Cases:

| Original Code | Expected Fix | Error Type |
|---------------|--------------|------------|
| `def foo(:` | `def foo():` | Missing closing paren |
| `if True\n  pass` | `if True:\n  pass` | Missing colon |

Test Flow:

| Step | Validation |
|------|------------|
| 1 | Validate original code (expect failure) |
| 2 | Verify fix_suggestion is populated |
| 3 | Apply auto-fix to code |
| 4 | Validate fixed code matches expected |
| 5 | Re-validate fixed code (expect pass) |

Success Criteria:

| Criteria | Expected Result |
|----------|-----------------|
| Initial validation | passed=False |
| Fix suggestion | Non-empty |
| Fixed content | Matches expected fix |
| Retry validation | passed=True |

> **Implementation Reference**: For auto-fix test implementations, see SDLC-Orchestrator test suite.

---

## 5. API Endpoints

### POST /api/v1/codegen/validate

Validate generated code through 4-gate pipeline.

**Request Parameters**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| generation_id | UUID | Yes | Reference to code generation |
| files | Array | Yes | List of files to validate |
| files[].path | String | Yes | File path |
| files[].content | String | Yes | File content |
| files[].language | String | Yes | Programming language |
| blueprint | Object | Yes | IR blueprint for context |
| blueprint.ir_version | String | Yes | IR schema version |
| blueprint.entities | Array | Yes | Entity definitions |
| options | Object | No | Validation options |
| options.skip_tests | Boolean | No | Skip Gate 4 (default: false) |
| options.fail_fast | Boolean | No | Stop on first failure (default: true) |

**Response Parameters**:

| Field | Type | Description |
|-------|------|-------------|
| validation_id | UUID | Validation record identifier |
| passed | Boolean | Overall pass/fail status |
| total_duration_ms | Integer | Total execution time |
| vietnamese_summary | String | Localized result message |
| gates | Array | Individual gate results |
| gates[].gate_name | String | Gate identifier |
| gates[].passed | Boolean | Gate pass/fail status |
| gates[].duration_ms | Integer | Gate execution time |
| gates[].details | Object | Gate-specific result data |

---

### GET /api/v1/projects/{project_id}/usage

Get codegen cost and usage statistics.

**Response Parameters**:

| Field | Type | Description |
|-------|------|-------------|
| project_id | UUID | Project identifier |
| period_days | Integer | Reporting period (days) |
| total_tokens | Integer | Total tokens used |
| total_cost_usd | Decimal | Total cost in USD |
| total_requests | Integer | Total generation requests |
| avg_latency_ms | Integer | Average latency |
| budget | Object | Budget information |
| budget.monthly_limit_usd | Decimal | Budget threshold |
| budget.current_usage_usd | Decimal | Current usage |
| budget.percentage_used | Decimal | Usage percentage |
| budget.alert_threshold | Decimal | Alert threshold |
| by_provider | Array | Per-provider breakdown |
| by_provider[].provider | String | Provider name |
| by_provider[].requests | Integer | Request count |
| by_provider[].tokens | Integer | Token count |
| by_provider[].cost_usd | Decimal | Cost for provider |

> **Implementation Reference**: For OpenAPI specification and API implementation details, see SDLC-Orchestrator documentation.

---

## 6. Success Metrics

| **Metric** | **Target** | **Measurement Method** | **Reporting Frequency** |
|------------|------------|------------------------|-------------------------|
| Gate pass rate | ≥95% | Production metrics | Daily |
| Total validation latency (Gates 1-3) | <3s (p95) | Prometheus histogram | Real-time |
| False positive rate | <5% | Manual review (100 samples/week) | Weekly |
| Vietnamese translation coverage | 100% | Automated test | CI/CD |
| Cost per project | <$50/month | CostTracker database | Monthly |
| Cache hit rate | ≥40% | Redis metrics | Daily |
| Auto-fix success rate | ≥90% | Production retry metrics | Weekly |

---

## 7. Implementation Checklist

### Week 1 (Feb 17-21, 2026)

- [ ] Implement SyntaxValidator with Python/JS/TS support
- [ ] Implement SecurityValidator with Semgrep integration (12 rules)
- [ ] Implement ArchitectureValidator with layer dependency rules
- [ ] Create QualityGatePipeline orchestrator
- [ ] Implement Vietnamese translation dictionary (50+ error types)
- [ ] Write unit tests for each validator (95%+ coverage)

### Week 2 (Feb 24-28, 2026)

- [ ] Implement TestValidator with pytest/jest execution
- [ ] Implement OllamaOptimizer with caching (Redis backend)
- [ ] Implement CostTracker with database persistence
- [ ] Implement AutoFixSuggestionService
- [ ] Integration test full pipeline (100 test cases)
- [ ] Performance optimization to meet <3s p95 target
- [ ] Create Grafana dashboard for validation metrics

---

## 8. Dependencies

**Upstream Dependencies**:
- SPEC-0009: Codegen Service (IR → Code generation)
- SPEC-0010: IR Processor (Blueprint validation)

**Downstream Dependencies**:
- SPEC-0012: Validation Pipeline Interface (retry orchestration)
- SPEC-0017: Feedback Learning Service (validation failure patterns)

**External Dependencies**:
- Semgrep CLI (security scanning)
- pytest/jest (test execution)
- Ollama API (cost optimization)
- Redis (caching)

---

## 9. Risks & Mitigations

| **Risk** | **Impact** | **Probability** | **Mitigation** |
|----------|------------|-----------------|----------------|
| Semgrep scan >1s (budget exceeded) | High | Medium | Implement parallel scanning + rule optimization |
| False positives >5% (user friction) | High | Medium | Manual review + rule tuning + whitelist support |
| Ollama context limit exceeded | Medium | High | Automatic fallback to Claude for large blueprints |
| Vietnamese translation inaccuracy | Medium | Low | Native speaker review + user feedback loop |
| Test execution timeout (Gate 4) | Low | Medium | 120s timeout + skip tests option |

---

## 10. Related Specifications

- [SPEC-0001: Anti-Vibecoding Specification](./SPEC-0001-Anti-Vibecoding.md) - Quality assurance context
- [SPEC-0002: Specification Standard](./SPEC-0002-Specification-Standard.md) - Document format compliance
- [SPEC-0009: Codegen Service Specification](./SPEC-0009-Codegen-Service-Specification.md) - IR → Code generation
- [SPEC-0010: IR Processor Specification](./SPEC-0010-IR-Processor-Specification.md) - Blueprint validation
- [SPEC-0012: Validation Pipeline Interface](./SPEC-0012-Validation-Pipeline-Interface.md) - Retry orchestration
- [SPEC-0017: Feedback Learning Service](./SPEC-0017-Feedback-Learning-Service.md) - Validation failure patterns

---

## Document Control

| Field | Value |
|-------|-------|
| **Spec ID** | SPEC-0020 |
| **Version** | 2.0.0 |
| **Status** | APPROVED |
| **Author** | Backend Lead + QA Lead |
| **Reviewer** | CTO |
| **Last Updated** | 2026-01-29 |
| **Framework Version** | 6.0.5 |

---

**Pure Methodology Notes**:
- This specification defines WHAT quality gates require for generated code validation
- For HOW to implement (service classes, SQL schemas, API endpoints), see SDLC-Orchestrator documentation
- Gate definitions are governance standard; implementation approaches may vary
- Vietnamese translations define coverage requirements, not dictionary implementation
- Performance budgets are SLA targets; monitoring implementation is tool-specific

---

**End of Specification**
