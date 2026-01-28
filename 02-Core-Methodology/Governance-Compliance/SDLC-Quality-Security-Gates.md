# SDLC Quality & Security Gates

**Version**: 5.3.0
**Date**: January 28, 2026
**Stage**: 02 - Core Methodology (Governance & Compliance)
**Pillar**: 4 - Quality Gates + Pillar 5 - SASE Integration
**Status**: ACTIVE - Production Standard
**Authority**: CTO + Security Lead
**Industry Standards**: ISO 12207, CMMI, DORA Metrics, NIST SSDF, OWASP ASVS, ISO 27001
**Related**: [SDLC-Quality-Assurance-System.md](../SDLC-Quality-Assurance-System.md) - Pillar 7 (Vibecoding Index)

---

## Purpose

This document defines **quantitative quality and security thresholds** that MUST be met at each gate before proceeding to the next stage. Quality and security are integrated throughout the lifecycle, not bolted on at the end.

**Key Principle**: Quality is not subjective - it's measured.

---

## Part 1: Quality Requirements by Tier

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

## Part 2: Security Requirements by Tier

### LITE Tier (1-2 people)

```yaml
Minimum Security:
  - Secrets: .env files (NOT committed to git)
  - Dependencies: Basic awareness of major vulnerabilities
  - Authentication: Standard framework auth (NextAuth, Auth.js)

CI/CD Security:
  - None required (manual review acceptable)

Audit:
  - None required
```

### STANDARD Tier (3-10 people)

```yaml
Secrets Management:
  - .env files with .env.example template
  - No secrets in code (pre-commit hook)
  - Basic secret rotation (manual, quarterly)

Dependencies:
  - npm audit / pip-audit on PRs
  - Renovate or Dependabot enabled
  - Critical CVEs addressed within 7 days

Authentication:
  - OAuth 2.0 or standard auth
  - Password policy enforced (12+ chars)
  - Session management (timeouts)

CI/CD Security:
  - Dependency scanning (npm audit, pip-audit)
  - Basic SAST (optional)
```

### PROFESSIONAL Tier (10-50 people)

```yaml
Secrets Management:
  - HashiCorp Vault or AWS Secrets Manager
  - Automatic rotation (90 days)
  - Audit logging for secret access

Software Bill of Materials (SBOM):
  Required: YES
  Tools: Syft, CycloneDX
  Format: SPDX or CycloneDX JSON
  Update: Every release

SAST (Static Application Security Testing):
  Required: YES
  Tools: Semgrep, SonarQube, CodeQL
  Rules: OWASP Top 10
  Enforcement: Block on Critical/High

Dependency Scanning:
  Required: YES
  Tools: Grype, Snyk, Dependabot
  Critical: Block PR
  High: Block PR
  Medium: Warning (fix within 14 days)
  Low: Informational

OWASP ASVS Level:
  Required: Level 1 (minimum)
  Categories Covered:
    - V1: Architecture, Design, Threat Modeling
    - V2: Authentication
    - V3: Session Management
    - V4: Access Control
    - V5: Validation, Sanitization, Encoding
    - V6: Stored Cryptography
    - V7: Error Handling, Logging
    - V8: Data Protection
    - V9: Communications
    - V10: Malicious Code
    - V11: Business Logic
    - V12: Files and Resources
    - V13: API and Web Service
    - V14: Configuration

Threat Modeling:
  Required: For new features with user data
  Method: STRIDE or PASTA
  Documentation: ADR format
```

### ENTERPRISE Tier (50+ people)

```yaml
All PROFESSIONAL requirements, PLUS:

OWASP ASVS Level:
  Required: Level 2 (recommended Level 3 for sensitive)

DAST (Dynamic Application Security Testing):
  Required: YES
  Tools: OWASP ZAP, Burp Suite
  Frequency: Weekly automated, monthly manual

Penetration Testing:
  Required: YES (annually minimum)
  Scope: Full application + infrastructure
  Provider: Third-party certified (CREST, OSCP)
  Remediation: Critical within 72h, High within 7 days

Security Champions:
  Required: 1 per team
  Training: Annual security training
  Responsibilities: Code review, threat modeling

Incident Response:
  Plan: Documented and tested
  Contacts: 24/7 security team
  SLA: P0 security <15 minutes response

Compliance:
  Audits: Quarterly internal, annual external
  Certifications: As required (SOC 2, ISO 27001, HIPAA)
  Evidence: Continuous compliance monitoring
```

---

## Part 3: Gate-Specific Requirements

### G0.1 (Problem Definition)

```yaml
Quality Checklist:
  □ Problem Statement documented
  □ User interviews completed (5+ users for PROFESSIONAL+)
  □ Business case validated
  □ Success metrics defined

Security Consideration:
  □ Data sensitivity classification identified
  □ Regulatory requirements noted (GDPR, HIPAA, etc.)
  □ Initial threat landscape assessed

Exit Criteria:
  - Problem validated with real users
  - ROI estimate documented
  - Stakeholder sign-off obtained
```

### G0.2 (Solution Diversity)

```yaml
Quality Checklist:
  □ 100+ ideas generated (PROFESSIONAL+)
  □ Top 3-5 concepts evaluated
  □ Technical feasibility assessed
  □ Risk assessment completed

Security Consideration:
  □ Security implications of each solution evaluated
  □ Third-party components security reviewed
  □ Attack surface compared between options

Exit Criteria:
  - Selected solution documented
  - Alternatives considered (ADR format)
  - Resource estimates provided
```

### G1 (Legal + Market Validation)

```yaml
Quality Checklist:
  □ Legal review completed
  □ License compliance verified
  □ Market research documented
  □ Competitive analysis done

Security Checklist:
  □ License compliance verified (AGPL contamination check)
  □ Data residency requirements identified
  □ Privacy requirements documented
  □ Security budget allocated

Exit Criteria:
  - No blocking legal issues
  - Market opportunity validated
  - Go/No-Go decision documented
```

### G2 (Design Ready)

```yaml
Quality Checklist:
  □ System architecture documented
  □ API contracts defined (OpenAPI)
  □ Database schema designed
  □ ADRs for key decisions

Security Checklist:
  □ Threat model completed (STRIDE/PASTA)
  □ Security architecture documented
  □ Authentication/Authorization design reviewed
  □ Data encryption strategy defined
  □ API security requirements specified
  □ OWASP ASVS checklist started

Exit Criteria:
  - Architecture approved (CTO)
  - API contracts validated
  - Security baseline defined
  - Security Lead sign-off on architecture
  - No unmitigated HIGH/CRITICAL threats
  - SBOM tooling configured
  - Estimated timeline accurate (±20%)
```

### G3 (Ship Ready)

```yaml
Quality Checklist:
  □ All features implemented
  □ Test coverage targets met
  □ Performance budget met
  □ Documentation complete
  □ Runbooks created
  □ Rollback tested

Security Checklist:
  □ SAST scan: PASS (zero Critical/High)
  □ Dependency scan: PASS (zero Critical/High)
  □ SBOM generated and stored
  □ Secrets rotation verified
  □ OWASP ASVS checklist completed (per tier level)
  □ Security documentation complete
  □ Incident response plan tested

Enterprise Additional:
  □ DAST scan completed
  □ Penetration test completed (if applicable)
  □ Compliance evidence collected
  □ Security training verified for all team members

Exit Criteria:
  - Zero P0 bugs
  - Zero critical security issues
  - Performance under load validated
  - UAT sign-off (PROFESSIONAL+)
  - CTO + CPO + Security Lead approval
  - High security issues have mitigation plan
```

---

## Part 4: SBOM (Software Bill of Materials)

### What is SBOM?

A complete inventory of all software components, dependencies, and their versions used in your application.

### SBOM Requirements

```yaml
Required for: PROFESSIONAL+ tiers
Format: SPDX or CycloneDX (JSON)
Generation: Automated in CI/CD
Storage: With each release artifact
Retention: Minimum 3 years

Content Must Include:
  - Package name and version
  - License information
  - Supplier/maintainer
  - Dependency relationships
  - Known vulnerabilities (linked)
```

### SBOM Generation Example

```yaml
# GitHub Actions
- name: Generate SBOM
  uses: anchore/sbom-action@v0
  with:
    format: spdx-json
    output-file: sbom.spdx.json

- name: Scan SBOM for vulnerabilities
  uses: anchore/scan-action@v3
  with:
    sbom: sbom.spdx.json
    fail-build: true
    severity-cutoff: high
```

---

## Part 5: SAST Rules & Configuration

### Semgrep Configuration

```yaml
# .semgrep.yml
rules:
  # OWASP Top 10
  - id: sql-injection
    patterns:
      - pattern: execute($QUERY)
      - pattern-not: execute($QUERY, $PARAMS)
    message: "Potential SQL injection"
    severity: ERROR

  - id: xss-vulnerability
    pattern: innerHTML = $USER_INPUT
    message: "Potential XSS vulnerability"
    severity: ERROR

  - id: hardcoded-secret
    patterns:
      - pattern: password = "..."
      - pattern: api_key = "..."
    message: "Hardcoded secret detected"
    severity: ERROR

  - id: insecure-crypto
    pattern: md5($DATA)
    message: "MD5 is cryptographically weak"
    severity: WARNING
```

### SAST Enforcement

```yaml
CI Pipeline:
  Critical: Block merge
  High: Block merge
  Medium: Warning (must fix before release)
  Low: Informational

Exceptions:
  - Documented false positives (suppression with comment)
  - Reviewed and approved by Security Lead
  - Expiration date for suppression (max 90 days)
```

---

## Part 6: OWASP ASVS Checklist Summary

### Level 1 (PROFESSIONAL tier minimum)

```yaml
V2 - Authentication:
  □ V2.1: Password requirements enforced (12+ chars)
  □ V2.2: Credential recovery secure
  □ V2.5: Account lockout after failures

V3 - Session Management:
  □ V3.2: Session tokens generated securely
  □ V3.3: Session timeout implemented
  □ V3.7: Session invalidation on logout

V4 - Access Control:
  □ V4.1: Access control enforced server-side
  □ V4.2: Principle of least privilege

V5 - Validation:
  □ V5.1: Input validation on all data
  □ V5.3: Output encoding for XSS prevention

V7 - Error Handling:
  □ V7.1: Errors don't leak sensitive info
  □ V7.2: Security events logged

V9 - Communications:
  □ V9.1: TLS for all connections
  □ V9.2: TLS 1.2+ only
```

### Level 2 (ENTERPRISE tier minimum)

```yaml
All Level 1 requirements, PLUS:

V1 - Architecture:
  □ V1.2: Threat model documented
  □ V1.5: Security controls defined

V2 - Authentication:
  □ V2.8: MFA for sensitive operations
  □ V2.9: Cryptographic authentication for APIs

V8 - Data Protection:
  □ V8.1: Sensitive data identified
  □ V8.2: Encryption at rest
  □ V8.3: Data minimization practiced

V13 - API Security:
  □ V13.1: Rate limiting implemented
  □ V13.2: Input validation on API
  □ V13.4: Anti-CSRF tokens
```

---

## Part 7: Threat Modeling

### When Required

```yaml
LITE: Not required
STANDARD: Recommended for user-facing features
PROFESSIONAL: Required for:
  - New features handling user data
  - Authentication/authorization changes
  - Third-party integrations
  - Infrastructure changes

ENTERPRISE: Required for all significant changes
```

### STRIDE Method

```yaml
Threat Categories:
  S - Spoofing: Can attacker pretend to be someone else?
  T - Tampering: Can data be modified maliciously?
  R - Repudiation: Can attacker deny actions?
  I - Information Disclosure: Can data be exposed?
  D - Denial of Service: Can service be disrupted?
  E - Elevation of Privilege: Can attacker gain higher access?

Template:
  | Threat | Category | Asset | Mitigation | Risk Level |
  |--------|----------|-------|------------|------------|
  | [Description] | S/T/R/I/D/E | [What's at risk] | [Control] | H/M/L |
```

---

## Part 8: DORA Metrics Tracking

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

## Part 9: Incident Response

### Security Incident Classification

```yaml
P0 - Critical:
  - Data breach confirmed
  - System compromise
  - Active exploitation
  Response: <15 minutes
  Escalation: CTO + Security Lead + Legal

P1 - High:
  - Vulnerability actively exploited
  - Significant security gap discovered
  Response: <1 hour
  Escalation: Security Lead + Tech Lead

P2 - Medium:
  - Vulnerability discovered (not exploited)
  - Security misconfiguration
  Response: <4 hours
  Escalation: Security Champion + Team Lead

P3 - Low:
  - Security improvement opportunity
  - Minor policy violation
  Response: Next business day
  Escalation: Team Lead
```

---

## Part 10: Quality Gate Automation

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

## Part 11: Enforcement & Escalation

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

### Escalation for Quality/Security Failures

```yaml
Quality Issue Escalation:
  Level 1 (Team): Coverage dropped 5%, lint warnings
  Level 2 (Lead): Coverage below threshold, test failures
  Level 3 (CTO): Build broken >24h, P0 bug in production

Security Issue Escalation:
  Level 1 (Team): Security medium findings
  Level 2 (Lead): Security high findings
  Level 3 (CTO): Security critical, active exploitation
```

---

## Part 12: Code Quality Thresholds

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

## Related Documents

- [SDLC-Sprint-Governance.md](./SDLC-Sprint-Governance.md) - Sprint gates (G-Sprint, G-Sprint-Close)
- [SDLC-Quality-Assurance-System.md](../SDLC-Quality-Assurance-System.md) - Pillar 7 (Vibecoding Index)
- [SDLC-Observability-Checklist.md](./SDLC-Observability-Checklist.md) - Monitoring requirements

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 5.3.0 | Jan 28, 2026 | Consolidated Quality Gates + Security Gates into single document |
| 5.2.0 | Jan 22, 2026 | AI Governance integration |
| 5.1.3 | Jan 18, 2026 | Sprint gate integration |

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for all SDLC projects
**Version**: 5.3.0
**Last Updated**: January 28, 2026
**Owner**: CTO + Security Lead
