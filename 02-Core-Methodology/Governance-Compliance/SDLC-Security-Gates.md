# SDLC Security Gates

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology (Governance & Compliance)
**Status**: ACTIVE - Production Standard
**Authority**: CTO + Security Lead
**Industry Standards**: NIST SSDF, OWASP ASVS, ISO 27001

---

## Purpose

Define **security requirements** that MUST be met at each stage of the SDLC. Security is integrated throughout the lifecycle, not bolted on at the end.

---

## Security Requirements by Tier

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

## Gate-Specific Security Requirements

### G0.1 (Problem Definition)

```yaml
Security Consideration:
  □ Data sensitivity classification identified
  □ Regulatory requirements noted (GDPR, HIPAA, etc.)
  □ Initial threat landscape assessed
```

### G0.2 (Solution Diversity)

```yaml
Security Consideration:
  □ Security implications of each solution evaluated
  □ Third-party components security reviewed
  □ Attack surface compared between options
```

### G1 (Legal + Market Validation)

```yaml
Security Checklist:
  □ License compliance verified (AGPL contamination check)
  □ Data residency requirements identified
  □ Privacy requirements documented
  □ Security budget allocated
```

### G2 (Design Ready)

```yaml
Security Checklist:
  □ Threat model completed (STRIDE/PASTA)
  □ Security architecture documented
  □ Authentication/Authorization design reviewed
  □ Data encryption strategy defined
  □ API security requirements specified
  □ OWASP ASVS checklist started

Exit Criteria:
  - Security Lead sign-off on architecture
  - No unmitigated HIGH/CRITICAL threats
  - SBOM tooling configured
```

### G3 (Ship Ready)

```yaml
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
  - Security Lead sign-off
  - Zero Critical security issues
  - High issues have mitigation plan
```

---

## SBOM (Software Bill of Materials)

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

## SAST Rules

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

## OWASP ASVS Checklist Summary

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

## Threat Modeling

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

## Incident Response

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

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: December 5, 2025
**Owner**: CTO + Security Lead
