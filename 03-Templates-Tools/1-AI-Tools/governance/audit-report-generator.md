# 📊 AI Audit Report Generator - Stage 09 (GOVERN)

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 09 - GOVERN (Governance & Compliance)
**Time Savings**: 85%
**Authority**: CTO Office

---

## Purpose

Generate **comprehensive audit reports** for SDLC 5.0.0 projects covering compliance, security, operations, and governance. Supports tiered requirements from STANDARD to ENTERPRISE.

---

## AI Prompts by Report Type

### 1. SDLC Compliance Audit Report

```yaml
System Prompt:
  You are generating SDLC 5.0.0 compliance audit reports.
  Check: 10 stages (00-09), 6 pillars, gate evidence, documentation standards.
  Apply tier-appropriate requirements (LITE/STANDARD/PROFESSIONAL/ENTERPRISE).
  Reference: SDLC-Core-Methodology.md and sdlc_validator.py

User Prompt Template:
  "Generate an SDLC compliance audit report for:

   Project: [Name]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]
   Audit Period: [Start Date] - [End Date]

   Areas to Audit:
   - [ ] Stage completion (00-09)
   - [ ] Gate evidence (G0.1, G0.2, G1, G2, G3)
   - [ ] Documentation standards
   - [ ] Team collaboration protocols
   - [ ] Code file naming compliance

   Current Status:
   - Stage: [Current stage]
   - Last Gate Passed: [Gate]
   - Known Issues: [Any known gaps]"

Output Format:
  # SDLC Compliance Audit Report

  **Project**: [Name]
  **Tier**: [Tier]
  **Audit Period**: [Dates]
  **Auditor**: AI Audit Generator v5.0.0
  **Compliance Score**: [X]%

  ---

  ## Executive Summary

  | Category | Score | Status |
  |----------|-------|--------|
  | Stage Completion | [X]% | 🟢/🟡/🔴 |
  | Gate Evidence | [X]% | 🟢/🟡/🔴 |
  | Documentation | [X]% | 🟢/🟡/🔴 |
  | Team Collaboration | [X]% | 🟢/🟡/🔴 |
  | **Overall** | [X]% | 🟢/🟡/🔴 |

  ---

  ## Stage Compliance (10 Stages)

  | Stage | Name | Status | Evidence | Gap |
  |-------|------|--------|----------|-----|
  | 00 | Foundation | ✅ Complete | 5/5 docs | None |
  | 01 | Planning | ✅ Complete | 4/4 docs | None |
  | 02 | Design | ✅ Complete | 8/8 docs | None |
  | 03 | Development | 🔄 In Progress | 3/5 docs | Sprint docs pending |
  | 04-09 | [Remaining] | ⏳ Not Started | - | Expected |

  ---

  ## Gate Evidence Audit

  | Gate | Required Evidence | Provided | Status |
  |------|------------------|----------|--------|
  | G0.1 | Problem Statement, Stakeholder Interviews | ✅ All | PASS |
  | G0.2 | Solution Options, Decision Record | ✅ All | PASS |
  | G1 | Legal Review, Market Validation | ✅ All | PASS |
  | G2 | Architecture Doc, Security Baseline, ADRs | 🟡 2/3 | PENDING |
  | G3 | - | ⏳ | Not Yet |

  ---

  ## Documentation Standards Audit

  | Standard | Requirement | Status | Issues |
  |----------|-------------|--------|--------|
  | File Naming | Kebab-case, no versions | ✅ PASS | - |
  | Headers | Version, Date, Stage, Status | ✅ PASS | - |
  | Team Collaboration | Communication Protocol | 🟡 PARTIAL | Missing RACI |
  | Code Naming | snake_case (Python), camelCase (TS) | ✅ PASS | - |

  ---

  ## Team Collaboration Audit (NEW in 5.0.0)

  | Document | Required | Present | Status |
  |----------|----------|---------|--------|
  | Team Communication Protocol | STANDARD+ | ✅ | PASS |
  | Team Collaboration Protocol | PROFESSIONAL+ | 🟡 | PARTIAL |
  | Escalation Path Standards | PROFESSIONAL+ | ✅ | PASS |
  | RACI Matrix | PROFESSIONAL+ | ❌ | MISSING |

  ---

  ## Findings and Recommendations

  ### Critical (Must Fix)
  1. **[Finding]**: [Description]
     - **Impact**: [Business impact]
     - **Recommendation**: [Action]
     - **Owner**: [Role]
     - **Due**: [Date]

  ### High Priority
  1. **[Finding]**: [Description]
     - **Recommendation**: [Action]

  ### Improvements (Optional)
  1. **[Finding]**: [Description]
     - **Recommendation**: [Action]

  ---

  ## Action Plan

  | # | Action | Owner | Priority | Due | Status |
  |---|--------|-------|----------|-----|--------|
  | 1 | [Action] | [Name] | P0 | [Date] | ⏳ |
  | 2 | [Action] | [Name] | P1 | [Date] | ⏳ |

  ---

  ## Sign-off

  - [ ] CTO Review: _______________
  - [ ] CPO Review: _______________
  - [ ] PM Acknowledgment: _______________
```

### 2. Security Audit Report

```yaml
System Prompt:
  You are generating security audit reports following OWASP ASVS and NIST SSDF.
  Check: Authentication, authorization, data protection, vulnerability management.
  Apply tier-appropriate security baselines.
  Reference: Security-Baseline.md

User Prompt Template:
  "Generate a security audit report for:

   Project: [Name]
   Security Baseline: [OWASP ASVS Level 1 | 2 | 3]
   Audit Period: [Start Date] - [End Date]

   Areas to Audit:
   - [ ] Authentication (JWT, OAuth, MFA)
   - [ ] Authorization (RBAC, RLS)
   - [ ] Data Protection (encryption, secrets)
   - [ ] Vulnerability Management (SAST, DAST, SBOM)
   - [ ] Incident Response (logging, alerting)

   Recent Changes:
   - [Change 1]
   - [Change 2]"

Output Format:
  # Security Audit Report

  **Project**: [Name]
  **Baseline**: OWASP ASVS Level [X]
  **Audit Period**: [Dates]
  **Security Score**: [X]% ([Y]/[Z] requirements met)

  ---

  ## Executive Summary

  | Category | Score | Findings | Critical |
  |----------|-------|----------|----------|
  | Authentication | [X]% | [Y] | [Z] |
  | Authorization | [X]% | [Y] | [Z] |
  | Data Protection | [X]% | [Y] | [Z] |
  | Vulnerability Mgmt | [X]% | [Y] | [Z] |
  | **Total** | [X]% | [Y] | [Z] |

  ---

  ## Authentication Audit

  | Requirement | ASVS Ref | Status | Notes |
  |-------------|----------|--------|-------|
  | Password Policy (12+ chars) | V2.1.1 | ✅ PASS | bcrypt cost=12 |
  | JWT Expiry (<15 min) | V3.5.1 | ✅ PASS | 15 min + refresh |
  | MFA Support | V2.8.1 | ✅ PASS | TOTP implemented |
  | Rate Limiting | V2.2.1 | 🟡 PARTIAL | Only on login |

  ---

  ## Vulnerability Assessment

  | Tool | Scan Date | Critical | High | Medium | Low |
  |------|-----------|----------|------|--------|-----|
  | Semgrep (SAST) | [Date] | 0 | 2 | 5 | 12 |
  | Grype (Dependencies) | [Date] | 0 | 1 | 3 | 8 |
  | Trivy (Container) | [Date] | 0 | 0 | 2 | 4 |

  ### Critical/High Findings

  | ID | Tool | Severity | Description | Remediation |
  |----|------|----------|-------------|-------------|
  | V001 | Semgrep | High | SQL injection in [file] | Use parameterized queries |
  | V002 | Grype | High | CVE-2024-XXXX in [package] | Upgrade to v[X] |

  ---

  ## Remediation Plan

  | Finding | Owner | Priority | Due | Status |
  |---------|-------|----------|-----|--------|
  | V001 | Dev Lead | P0 | 48h | ⏳ |
  | V002 | DevOps | P0 | 24h | ⏳ |

  ---

  ## Next Audit
  - **Date**: [Date]
  - **Focus**: [Areas]
```

### 3. Operations Audit Report

```yaml
System Prompt:
  You are generating operations audit reports with DORA metrics and SRE practices.
  Check: Availability, performance, incident management, change management.
  Reference: DORA metrics targets and SLO definitions.

User Prompt Template:
  "Generate an operations audit report for:

   Project: [Name]
   Period: [Start Date] - [End Date]

   SLOs:
   - Availability: [X]%
   - Latency p95: [X]ms
   - Error Rate: <[X]%

   Metrics to Audit:
   - [ ] DORA metrics (DF, LT, MTTR, CFR)
   - [ ] Uptime and availability
   - [ ] Incident management
   - [ ] Change management
   - [ ] Capacity planning"

Output Format:
  # Operations Audit Report

  **Project**: [Name]
  **Period**: [Dates]
  **SLO Compliance**: [X]%

  ---

  ## DORA Metrics

  | Metric | Target | Actual | Status | Trend |
  |--------|--------|--------|--------|-------|
  | Deployment Frequency | Weekly | [X]/week | 🟢 Elite | ↑ |
  | Lead Time | <1 day | [X] hours | 🟢 Elite | ↓ |
  | MTTR | <1 hour | [X] min | 🟢 Elite | ↓ |
  | Change Failure Rate | <15% | [X]% | 🟢 Elite | ↓ |

  **DORA Classification**: [Elite | High | Medium | Low]

  ---

  ## SLO Compliance

  | SLO | Target | Actual | Budget Remaining |
  |-----|--------|--------|------------------|
  | Availability | 99.9% | 99.95% | 50% |
  | Latency p95 | 100ms | 85ms | N/A |
  | Error Rate | <0.1% | 0.05% | 50% |

  ---

  ## Incident Summary

  | Severity | Count | Total Duration | MTTR |
  |----------|-------|----------------|------|
  | P0 | [X] | [Y] hours | [Z] min |
  | P1 | [X] | [Y] hours | [Z] min |
  | P2 | [X] | [Y] hours | [Z] min |

  ### Notable Incidents
  | Date | Severity | Duration | Root Cause | Postmortem |
  |------|----------|----------|------------|------------|
  | [Date] | P1 | 45 min | [Cause] | [Link] |

  ---

  ## Recommendations

  1. **[Recommendation]**: [Action]
  2. **[Recommendation]**: [Action]
```

### 4. Governance Maturity Assessment (NEW in 5.0.0)

```yaml
System Prompt:
  You are assessing governance maturity against CMMI and SDLC 5.0.0 standards.
  Map current practices to maturity levels (1-5).
  Provide upgrade path recommendations.
  Reference: SDLC-Maturity-Assessment-Guide.md

User Prompt Template:
  "Assess governance maturity for:

   Project: [Name]
   Current Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]

   Areas to Assess:
   - Process definition and documentation
   - Measurement and metrics
   - Team collaboration standards
   - Quality gates and evidence
   - Continuous improvement practices"

Output Format:
  # Governance Maturity Assessment

  **Project**: [Name]
  **Current Tier**: [Tier]
  **Maturity Level**: [1-5] ([Name])
  **Target Level**: [1-5] ([Name])

  ---

  ## Maturity Level Mapping

  | CMMI Level | SDLC Tier | Current Status |
  |------------|-----------|----------------|
  | L1 Initial | - | ✅ Achieved |
  | L2 Managed | LITE/STANDARD | ✅ Achieved |
  | L3 Defined | STANDARD/PROFESSIONAL | 🔄 In Progress |
  | L4 Quantitative | PROFESSIONAL | ⏳ Planned |
  | L5 Optimizing | ENTERPRISE | ⏳ Future |

  ---

  ## Area Assessment

  | Area | Score | Level | Gap |
  |------|-------|-------|-----|
  | Process Documentation | 3.5/5 | L3 | Need standard templates |
  | Metrics & Measurement | 2.8/5 | L2 | Need DORA dashboard |
  | Team Collaboration | 4.0/5 | L4 | None |
  | Quality Gates | 3.2/5 | L3 | Need automated gates |
  | Continuous Improvement | 2.5/5 | L2 | Need retrospective cadence |

  ---

  ## Upgrade Path

  ### To Reach Level 3 (Defined)
  1. [ ] Standardize all process templates
  2. [ ] Document Team Collaboration protocols
  3. [ ] Implement automated quality gates

  ### To Reach Level 4 (Quantitative)
  1. [ ] Deploy DORA metrics dashboard
  2. [ ] Set quantitative targets per sprint
  3. [ ] Implement statistical process control

  ---

  ## Timeline Recommendation

  | Milestone | Target Level | Actions | Effort |
  |-----------|--------------|---------|--------|
  | Q1 2026 | L3 | Templates, protocols | 2 weeks |
  | Q2 2026 | L4 | Metrics, automation | 4 weeks |
  | Q4 2026 | L5 | Optimization | 8 weeks |
```

---

## Tier-Appropriate Audit Requirements

| Audit Type | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|------------|------|----------|--------------|------------|
| SDLC Compliance | N/A | Annual | Quarterly | Monthly |
| Security | Basic | Annual | Quarterly | Monthly |
| Operations | N/A | Quarterly | Monthly | Weekly |
| Maturity | N/A | Annual | Semi-annual | Quarterly |

---

## Success Metrics

**Audit Efficiency** (Stage 09):
- ✅ 85% time savings on audit preparation
- ✅ 100% audit trail completeness
- ✅ <5 min violation detection (automated)
- ✅ Zero compliance surprises

**BFlow Validation**:
- Monthly internal audits automated
- Passed external audit Dec 2025
- Complete audit trail maintained

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: December 5, 2025
**Owner**: CTO Office
