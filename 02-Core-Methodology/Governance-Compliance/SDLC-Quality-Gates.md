# SDLC Quality Gates

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology (Governance & Compliance)
**Status**: ACTIVE - Production Standard
**Authority**: CTO Office
**Industry Standards**: ISO 12207, CMMI, DORA Metrics

---

## Purpose

Define **quantitative quality thresholds** that MUST be met at each gate before proceeding to the next stage. Quality is not subjective - it's measured.

---

## Quality Requirements by Tier

### LITE Tier (1-2 people)

```yaml
Code Quality:
  - Linting: Manual (IDE warnings addressed)
  - Tests: Unit tests for critical paths
  - Coverage: No minimum (but encouraged)
  - Review: Self-review or AI review

CI/CD:
  - Build: Manual or basic CI
  - Deploy: Manual deployment acceptable

Metrics:
  - None required (tracking optional)
```

### STANDARD Tier (3-10 people)

```yaml
Code Quality:
  - Linting: PASS (ESLint, Ruff, etc.)
  - Formatting: Enforced (Prettier, Black)
  - Tests: Unit + basic integration
  - Coverage: ≥60% unit test coverage
  - Review: 1+ reviewer required

CI/CD:
  - Build: Automated (GitHub Actions, GitLab CI)
  - Tests: Run on every PR
  - Deploy: Automated staging deployment

Metrics (DORA - Monthly):
  - Deployment Frequency: Weekly to monthly
  - Lead Time: 1 week to 1 month
  - MTTR: <1 week
  - Change Failure Rate: <30%
```

### PROFESSIONAL Tier (10-50 people)

```yaml
Code Quality:
  - Linting: PASS (zero warnings in CI)
  - Formatting: Auto-enforced (pre-commit hooks)
  - Type Checking: PASS (mypy, TypeScript strict)
  - Tests: Unit + Integration + E2E
  - Coverage:
      Unit: ≥80%
      Integration: ≥70%
      E2E: Critical paths covered
  - Review: 2+ reviewers required
  - ADRs: Required for architectural decisions

CI/CD:
  - Build: Automated with caching
  - Tests: Parallel execution
  - Security: SAST scan (Semgrep)
  - Deploy: Blue-green or canary

Metrics (DORA - Weekly):
  - Deployment Frequency: Daily to weekly
  - Lead Time: 1 day to 1 week
  - MTTR: <1 day
  - Change Failure Rate: <20%

Performance:
  - API Latency: <200ms p95
  - Page Load: <3s
  - Database Query: <100ms p95
```

### ENTERPRISE Tier (50+ people)

```yaml
Code Quality:
  - All PROFESSIONAL requirements, PLUS:
  - Coverage:
      Unit: ≥95%
      Integration: ≥90%
      E2E: All critical + edge cases
  - Review: 2+ senior reviewers for core changes
  - Architecture Review: Required for cross-team changes

CI/CD:
  - Build: <5 minutes
  - Tests: <10 minutes total
  - Security: SAST + DAST + dependency scan
  - Deploy: Feature flags, gradual rollout

Metrics (DORA - Daily):
  - Deployment Frequency: Multiple per day
  - Lead Time: <1 hour to <1 day
  - MTTR: <1 hour
  - Change Failure Rate: <15%

Performance:
  - API Latency: <100ms p95
  - Page Load: <1s
  - Database Query: <50ms p95
  - Concurrent Users: Defined capacity tested
```

---

## Gate-Specific Quality Requirements

### G0.1 (Problem Definition)

```yaml
Quality Gate Checklist:
  □ Problem Statement documented
  □ User interviews completed (5+ users for PROFESSIONAL+)
  □ Business case validated
  □ Success metrics defined

Exit Criteria:
  - Problem validated with real users
  - ROI estimate documented
  - Stakeholder sign-off obtained
```

### G0.2 (Solution Diversity)

```yaml
Quality Gate Checklist:
  □ 100+ ideas generated (PROFESSIONAL+)
  □ Top 3-5 concepts evaluated
  □ Technical feasibility assessed
  □ Risk assessment completed

Exit Criteria:
  - Selected solution documented
  - Alternatives considered (ADR format)
  - Resource estimates provided
```

### G1 (Legal + Market Validation)

```yaml
Quality Gate Checklist:
  □ Legal review completed
  □ License compliance verified
  □ Market research documented
  □ Competitive analysis done

Exit Criteria:
  - No blocking legal issues
  - Market opportunity validated
  - Go/No-Go decision documented
```

### G2 (Design Ready)

```yaml
Quality Gate Checklist:
  □ System architecture documented
  □ API contracts defined (OpenAPI)
  □ Database schema designed
  □ Security review completed
  □ ADRs for key decisions

Exit Criteria:
  - Architecture approved (CTO)
  - API contracts validated
  - Security baseline defined
  - Estimated timeline accurate (±20%)
```

### G3 (Ship Ready)

```yaml
Quality Gate Checklist:
  □ All features implemented
  □ Test coverage targets met
  □ Security scan PASS
  □ Performance budget met
  □ Documentation complete
  □ Runbooks created
  □ Rollback tested

Exit Criteria:
  - Zero P0 bugs
  - Zero critical security issues
  - Performance under load validated
  - UAT sign-off (PROFESSIONAL+)
  - CTO + CPO approval
```

---

## Code Quality Thresholds

### Linting Rules

```yaml
Python (Ruff):
  - All default rules enabled
  - Line length: 120 chars
  - Import sorting: isort compatible
  - Docstrings: Google style

TypeScript (ESLint):
  - @typescript-eslint/recommended
  - No 'any' type (strict mode)
  - Consistent return types

React:
  - react-hooks/rules-of-hooks
  - react-hooks/exhaustive-deps
  - jsx-a11y for accessibility
```

### Test Quality

```yaml
Unit Tests:
  - Arrange-Act-Assert pattern
  - One assertion per test (preferred)
  - No test interdependencies
  - Deterministic (no flaky tests)

Integration Tests:
  - Real services (no mocks for external APIs)
  - Database transactions (rollback after test)
  - Contract validation (OpenAPI)

E2E Tests:
  - User journey focused
  - Stable selectors (data-testid)
  - Retry logic for flakiness
  - Screenshot on failure
```

---

## DORA Metrics Tracking

### Metric Definitions

```yaml
Deployment Frequency (DF):
  Definition: How often code is deployed to production
  Measurement: Count of production deployments per time period
  Target by Tier:
    LITE: Any (tracking optional)
    STANDARD: Weekly to monthly
    PROFESSIONAL: Daily to weekly
    ENTERPRISE: Multiple per day

Lead Time for Changes (LT):
  Definition: Time from code commit to production
  Measurement: Median time (commit timestamp → production deploy)
  Target by Tier:
    LITE: Any
    STANDARD: 1 week to 1 month
    PROFESSIONAL: 1 day to 1 week
    ENTERPRISE: <1 hour to <1 day

Mean Time to Recovery (MTTR):
  Definition: Time to restore service after failure
  Measurement: Median time (incident start → service restored)
  Target by Tier:
    LITE: Any
    STANDARD: <1 week
    PROFESSIONAL: <1 day
    ENTERPRISE: <1 hour

Change Failure Rate (CFR):
  Definition: Percentage of deployments causing failure
  Measurement: (Failed deployments / Total deployments) × 100
  Target by Tier:
    LITE: Any
    STANDARD: <30%
    PROFESSIONAL: <20%
    ENTERPRISE: <15%
```

### Dashboard Template

```yaml
Weekly DORA Dashboard:
  Deployment Frequency: [N] deploys this week (target: [X])
  Lead Time: [N] hours median (target: <[X] hours)
  MTTR: [N] minutes (target: <[X] minutes)
  Change Failure Rate: [N]% (target: <[X]%)

  Trend: [↑/↓/→] vs last week
  Action Items: [If below target, list improvements]
```

---

## Quality Gate Automation

### Pre-commit Hook Example

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: lint
        name: Lint code
        entry: ruff check .
        language: system

      - id: format
        name: Check formatting
        entry: ruff format --check .
        language: system

      - id: typecheck
        name: Type check
        entry: mypy .
        language: system

      - id: test
        name: Run fast tests
        entry: pytest -x --timeout=30
        language: system
```

### CI Pipeline Quality Gates

```yaml
# GitHub Actions example
quality-gates:
  runs-on: ubuntu-latest
  steps:
    - name: Lint
      run: ruff check . --output-format=github

    - name: Format
      run: ruff format --check .

    - name: Type Check
      run: mypy . --strict

    - name: Unit Tests
      run: pytest --cov=src --cov-fail-under=80

    - name: Security Scan
      run: semgrep --config=auto .

    - name: Check Coverage
      run: |
        coverage report --fail-under=80
```

---

## Enforcement

### Blocking vs Non-Blocking

```yaml
BLOCKING (Fail CI):
  - Lint errors
  - Type errors
  - Test failures
  - Coverage below threshold
  - Security critical/high

NON-BLOCKING (Warning only):
  - Coverage warning (within 5% of threshold)
  - Security medium/low
  - Performance warning (within 10% of target)
```

### Escalation for Quality Failures

```yaml
Quality Issue Escalation:
  Level 1 (Team): Coverage dropped 5%, lint warnings
  Level 2 (Lead): Coverage below threshold, security medium
  Level 3 (CTO): Security critical, P0 bug in production
```

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for all SDLC projects
**Last Updated**: December 5, 2025
**Owner**: CTO Office
