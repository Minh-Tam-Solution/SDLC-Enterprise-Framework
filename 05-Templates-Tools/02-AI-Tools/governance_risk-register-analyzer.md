# 🛡️ Risk Register Analyzer - Stage 00 + 09 (FOUNDATION + GOVERN)

**Version**: 6.0.6
**Date**: February 14, 2026
**Stage**: 00 - FOUNDATION + 09 - GOVERN
**Pillar**: 1 (10-Stage Lifecycle) + 4 (Quality Gates)
**Time Savings**: 80% (8 hours → 1.5 hours)
**Authority**: CTO Office
**Origin**: Bflow SDLC 6.0.6 Framework Assessment (Feb 2026)

---

## Purpose

**Risk identification, assessment, and tracking** for SDLC 6.0.6 projects. Covers Technical, Operational, Business, Security, and Compliance risk categories with Likelihood × Impact scoring matrix. Supports risk ownership, mitigation planning, and review cadence by tier.

---

## 4-Tier Requirements

| Aspect | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|--------|------|----------|--------------|------------|
| Risk Categories | Technical only | Tech + Security | All 5 categories | All 5 + Custom |
| Review Cadence | Ad-hoc | Quarterly | Monthly | Monthly + Board |
| Top-N Tracking | Top 3 | Top 5 | Top 10 | Top 15 + KRI |
| Risk Owner | Optional | Required | Required + backup | Required + RACI |
| Mitigation Plan | Informal | Documented | Documented + timeline | Documented + budget |
| Gate Integration | None | At major gates | Every gate | Every gate + sprint |

---

## AI Prompt

```yaml
System Prompt:
  You are analyzing and managing a Risk Register for SDLC 6.0.6.
  Identify risks across 5 categories (Technical, Operational, Business, Security, Compliance).
  Score each risk using Likelihood × Impact matrix (1-4 scale).
  Assign risk owners and generate mitigation plans.
  Apply tier-appropriate requirements.
  Reference: SDLC-Core-Methodology.md, project charter, threat models.

User Prompt Template:
  "Create/Update a Risk Register for:

   Project: [Name]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]
   Current Stage: [Stage number and name]
   Project Age: [X months]
   Team Size: [N people]

   Risk Categories to Assess:
   1. Technical (architecture, dependencies, performance)
   2. Operational (deployment, monitoring, incident response)
   3. Business (market, budget, timeline, stakeholder)
   4. Security (vulnerabilities, data protection, access control)
   5. Compliance (regulatory, licensing, audit)

   For each identified risk, provide:
   - Description and root cause
   - Likelihood (1-4: Unlikely → Very Likely)
   - Impact (1-4: Low → Critical)
   - Risk Score (Likelihood × Impact)
   - Risk Response (Accept/Mitigate/Transfer/Avoid)
   - Mitigation plan with owner and deadline
   - Residual risk after mitigation"
```

---

## Risk Assessment Matrix

### Likelihood × Impact Scoring

|  | **Low Impact (1)** | **Medium Impact (2)** | **High Impact (3)** | **Critical Impact (4)** |
|---|---|---|---|---|
| **Very Likely (4)** | 4 — Medium | 8 — High | 12 — Critical | 16 — Critical |
| **Likely (3)** | 3 — Low | 6 — Medium | 9 — High | 12 — Critical |
| **Possible (2)** | 2 — Low | 4 — Medium | 6 — Medium | 8 — High |
| **Unlikely (1)** | 1 — Low | 2 — Low | 3 — Low | 4 — Medium |

### Risk Score Classification

| Score | Level | Color | Response Requirement |
|-------|-------|-------|---------------------|
| 12-16 | CRITICAL | 🔴 Red | Immediate action required, CTO escalation |
| 7-9 | HIGH | 🟠 Orange | Active mitigation required before next gate |
| 4-6 | MEDIUM | 🟡 Yellow | Documented mitigation plan, monitor monthly |
| 1-3 | LOW | 🟢 Green | Accept and monitor, review quarterly |

### Risk Response Types

| Type | When to Use | Example |
|------|-------------|---------|
| **Avoid** | Eliminate the risk entirely | Change technology to avoid AGPL contamination |
| **Mitigate** | Reduce likelihood or impact | Add automated testing to catch regressions |
| **Transfer** | Shift risk to another party | Use managed database service (AWS RDS) |
| **Accept** | Risk is within tolerance | Accept minor UI inconsistency in legacy browser |

---

## Risk Categories & Common Risks

### 1. Technical Risks

| Risk ID | Risk | Likelihood | Impact | Common In |
|---------|------|------------|--------|-----------|
| T-001 | Single point of failure in architecture | 2 | 4 | All tiers |
| T-002 | Technical debt accumulation | 3 | 3 | STANDARD+ |
| T-003 | Dependency vulnerability (CVE) | 3 | 3 | All tiers |
| T-004 | Performance degradation under load | 2 | 3 | PROFESSIONAL+ |
| T-005 | Data migration failure | 2 | 4 | All tiers |
| T-006 | API breaking change impact | 2 | 3 | STANDARD+ |
| T-007 | AI model quality regression | 2 | 3 | Projects with AI |

### 2. Operational Risks

| Risk ID | Risk | Likelihood | Impact | Common In |
|---------|------|------------|--------|-----------|
| O-001 | No rollback procedure tested | 2 | 4 | STANDARD+ |
| O-002 | Insufficient monitoring coverage | 3 | 3 | All tiers |
| O-003 | No on-call rotation defined | 3 | 3 | STANDARD+ |
| O-004 | Backup restoration not validated | 2 | 4 | STANDARD+ |
| O-005 | Incident response undefined | 3 | 3 | STANDARD+ |

### 3. Business Risks

| Risk ID | Risk | Likelihood | Impact | Common In |
|---------|------|------------|--------|-----------|
| B-001 | Timeline overrun (>20% delay) | 3 | 3 | All tiers |
| B-002 | Key person dependency | 3 | 3 | LITE/STANDARD |
| B-003 | Scope creep without gate approval | 3 | 2 | All tiers |
| B-004 | Budget overrun (>15%) | 2 | 3 | PROFESSIONAL+ |
| B-005 | Stakeholder misalignment | 2 | 3 | PROFESSIONAL+ |

### 4. Security Risks

| Risk ID | Risk | Likelihood | Impact | Common In |
|---------|------|------------|--------|-----------|
| S-001 | Unauthorized data access | 2 | 4 | All tiers |
| S-002 | Credential exposure in code | 2 | 4 | All tiers |
| S-003 | OWASP Top 10 vulnerability | 3 | 3 | All tiers |
| S-004 | Third-party supply chain attack | 2 | 4 | PROFESSIONAL+ |
| S-005 | Data privacy violation (GDPR/PDPA) | 2 | 4 | ENTERPRISE |

### 5. Compliance Risks

| Risk ID | Risk | Likelihood | Impact | Common In |
|---------|------|------------|--------|-----------|
| C-001 | AGPL license contamination | 2 | 4 | Projects using OSS |
| C-002 | Missing gate evidence | 3 | 2 | STANDARD+ |
| C-003 | Audit trail gaps | 2 | 3 | PROFESSIONAL+ |
| C-004 | Regulatory non-compliance | 2 | 4 | ENTERPRISE |
| C-005 | SDLC process deviation | 3 | 2 | All tiers |

---

## Risk Register Template

```markdown
# Risk Register — [Project Name]

**Last Updated**: [YYYY-MM-DD]
**Review Cadence**: [Quarterly / Monthly]
**Risk Owner**: [PM / Tech Lead]
**Next Review**: [YYYY-MM-DD]

## Active Risks (Top N)

| # | ID | Category | Risk Description | L | I | Score | Response | Mitigation | Owner | Deadline | Status |
|---|-----|----------|-----------------|---|---|-------|----------|------------|-------|----------|--------|
| 1 | [ID] | [Cat] | [Description] | [1-4] | [1-4] | [L×I] | [Type] | [Plan] | [Name] | [Date] | 🔴/🟡/🟢 |
| 2 | [ID] | [Cat] | [Description] | [1-4] | [1-4] | [L×I] | [Type] | [Plan] | [Name] | [Date] | 🔴/🟡/🟢 |

## Closed/Accepted Risks

| # | ID | Risk | Original Score | Residual Score | Closure Reason | Date |
|---|-----|------|---------------|----------------|----------------|------|
| 1 | [ID] | [Risk] | [Score] | [Score] | [Mitigated/Accepted/Avoided] | [Date] |

## Risk Trend

| Review Date | Critical | High | Medium | Low | Total |
|-------------|----------|------|--------|-----|-------|
| [YYYY-MM-DD] | [N] | [N] | [N] | [N] | [N] |
| [YYYY-MM-DD] | [N] | [N] | [N] | [N] | [N] |
```

---

## Review Cadence

### STANDARD Tier (Quarterly)

```markdown
Quarterly Risk Review Agenda (30 min):
1. Review active risks — status update (10 min)
2. Identify new risks from recent sprints (10 min)
3. Close/downgrade mitigated risks (5 min)
4. Update risk trend chart (5 min)
```

### PROFESSIONAL Tier (Monthly)

```markdown
Monthly Risk Review Agenda (45 min):
1. Top-10 risk status update (15 min)
2. New risk identification — post-mortems, security scans (10 min)
3. Mitigation plan progress review (10 min)
4. Risk score re-evaluation (5 min)
5. Action items and owners (5 min)
```

### ENTERPRISE Tier (Monthly + Board)

```markdown
Monthly Risk Review (45 min) — same as PROFESSIONAL

Quarterly Board Risk Report:
1. Executive risk summary — top 5 with trend (5 min)
2. Critical/High risk deep-dive (10 min)
3. KRI (Key Risk Indicator) dashboard review (5 min)
4. Budget impact of risk mitigation (5 min)
5. Board decisions/approvals needed (5 min)
```

---

## Gate Integration

### Risk Assessment at Quality Gates

| Gate | Risk Activity |
|------|--------------|
| G0.1 (Problem Definition) | Initial risk identification — Technical + Business |
| G0.2 (Solution Diversity) | Architecture risk assessment |
| G1 (Market Validation) | Business + Compliance risk review |
| G2 (Design Ready) | Full risk register review — all 5 categories |
| G3 (Ship Ready) | Pre-launch risk assessment — Go/No-Go input |
| G4 (Internal Validation) | Post-launch risk retrospective |

---

## BFlow Example

**Project**: BFlow Platform v3.2
**Tier**: PROFESSIONAL
**Assessment Date**: February 14, 2026

### Top 5 Active Risks

| # | ID | Category | Risk | L | I | Score | Response | Owner | Status |
|---|-----|----------|------|---|---|-------|----------|-------|--------|
| 1 | S-003 | Security | OWASP vulnerabilities in legacy endpoints | 3 | 3 | 9 🟠 | Mitigate | Security Lead | In progress |
| 2 | O-003 | Operations | No formal on-call rotation (30% coverage) | 3 | 3 | 9 🟠 | Mitigate | DevOps Lead | In progress |
| 3 | C-002 | Compliance | Gate evidence gaps (40% collected) | 3 | 2 | 6 🟡 | Mitigate | PM | Planned |
| 4 | T-002 | Technical | Technical debt in payment module | 2 | 3 | 6 🟡 | Mitigate | Tech Lead | Planned |
| 5 | B-001 | Business | Go-live timeline risk (March → April) | 2 | 3 | 6 🟡 | Accept | PM | Monitoring |

### Risk Summary

| Category | Critical | High | Medium | Low |
|----------|----------|------|--------|-----|
| Technical | 0 | 0 | 2 | 1 |
| Operational | 0 | 2 | 1 | 0 |
| Business | 0 | 0 | 1 | 2 |
| Security | 0 | 1 | 1 | 0 |
| Compliance | 0 | 0 | 2 | 1 |
| **Total** | **0** | **3** | **7** | **4** |

---

## Related Templates

- [deployment_go-live-readiness-assessment.md](./deployment_go-live-readiness-assessment.md) - Risk-informed Go/No-Go
- [governance_maturity-assessment-framework.md](./governance_maturity-assessment-framework.md) - Gap analysis with priorities
- [governance_audit-report-generator.md](./governance_audit-report-generator.md) - Compliance audit
- [governance_compliance-checker.md](./governance_compliance-checker.md) - Automated compliance
- [testing_security-testing-checklist.md](./testing_security-testing-checklist.md) - Security risk validation
