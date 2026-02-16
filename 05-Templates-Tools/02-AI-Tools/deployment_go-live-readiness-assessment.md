# 📊 Go-Live Readiness Assessment - Stage 06 + 09 (DEPLOY + GOVERN)

**Version**: 6.0.6
**Date**: February 14, 2026
**Stage**: 06 - DEPLOY + 09 - GOVERN
**Pillar**: 1 (10-Stage Lifecycle) + 4 (Quality Gates)
**Time Savings**: 80% (12 hours → 2.5 hours)
**Authority**: CTO Office
**Origin**: Bflow SDLC 6.0.6 Framework Assessment (Feb 2026)

---

## Purpose

**Strategic go-live readiness assessment** with weighted scoring model, Go/No-Go decision framework, and 8-week countdown timeline. Use this to make data-driven launch decisions with risk quantification.

> **Related**: For tactical 100-item checklist, see [deployment_go-live-readiness-checklist.md](./deployment_go-live-readiness-checklist.md)

---

## AI Prompt

```yaml
System Prompt:
  You are conducting a Go-Live Readiness Assessment for SDLC 6.0.6.
  Score each category with weighted percentages.
  Produce a Go/No-Go recommendation with quantified risk.
  Apply tier-appropriate thresholds.
  Reference: SDLC-Core-Methodology.md, deployment standards, gate criteria.

User Prompt Template:
  "Conduct a Go-Live Readiness Assessment for:

   Project: [Name]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]
   Go-Live Date: [YYYY-MM-DD]
   Current Stage: [Stage number and name]

   Assess these categories with weighted scoring:
   1. Infrastructure Readiness (20% weight)
   2. Security Posture (25% weight)
   3. Testing Coverage (20% weight)
   4. Operations Readiness (15% weight)
   5. Documentation (10% weight)
   6. Communication (10% weight)

   For each category, provide:
   - Score (0-100%)
   - Evidence references
   - Blocking issues (P0)
   - Risk assessment (Likelihood × Impact)

   Produce Go/No-Go recommendation with conditions."
```

---

## Scoring Model

### Category Weights by Tier

| Category | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|----------|------|----------|--------------|------------|
| Infrastructure | 25% | 20% | 20% | 20% |
| Security | 15% | 20% | 25% | 30% |
| Testing | 25% | 20% | 20% | 20% |
| Operations | 15% | 15% | 15% | 15% |
| Documentation | 10% | 15% | 10% | 10% |
| Communication | 10% | 10% | 10% | 5% |

### Score Thresholds

| Score Range | Status | Decision |
|-------------|--------|----------|
| 90-100% | GREEN | **GO** - Launch approved |
| 75-89% | YELLOW | **CONDITIONAL GO** - Launch with mitigations, CTO approval required |
| 60-74% | ORANGE | **DELAY** - Critical gaps must be resolved (1-2 week delay) |
| <60% | RED | **NO-GO** - Significant readiness gaps, major remediation required |

### Automatic NO-GO Conditions

Regardless of overall score, a **NO-GO** is triggered if:

1. Any category scores **<50%**
2. **Security** category scores **<70%** (PROFESSIONAL+)
3. Any **P0 blocker** remains unresolved
4. No **rollback procedure** has been tested
5. **Zero on-call coverage** defined (STANDARD+)

---

## Assessment Template

### Executive Summary

```markdown
# Go-Live Readiness Assessment

**Project**: [Name]
**Assessment Date**: [YYYY-MM-DD]
**Go-Live Target**: [YYYY-MM-DD]
**Tier**: [Tier]
**Assessor**: [Name/Role]

## Overall Score: [X]% — [GO / CONDITIONAL GO / DELAY / NO-GO]

| Category | Weight | Score | Weighted | Status |
|----------|--------|-------|----------|--------|
| Infrastructure | [W]% | [S]% | [W×S]% | 🟢/🟡/🟠/🔴 |
| Security | [W]% | [S]% | [W×S]% | 🟢/🟡/🟠/🔴 |
| Testing | [W]% | [S]% | [W×S]% | 🟢/🟡/🟠/🔴 |
| Operations | [W]% | [S]% | [W×S]% | 🟢/🟡/🟠/🔴 |
| Documentation | [W]% | [S]% | [W×S]% | 🟢/🟡/🟠/🔴 |
| Communication | [W]% | [S]% | [W×S]% | 🟢/🟡/🟠/🔴 |
| **Total** | **100%** | — | **[X]%** | **[Status]** |
```

### Per-Category Assessment

```markdown
## [Category Name] — [Score]% [Status Emoji]

### Evidence
- [List evidence documents, test results, screenshots]

### Strengths
- [What's working well]

### Gaps
| Gap | Priority | Risk | Mitigation | Owner | ETA |
|-----|----------|------|------------|-------|-----|
| [Gap description] | P0/P1/P2 | H/M/L | [Plan] | [Person] | [Date] |

### Score Breakdown
| Sub-category | Score | Notes |
|--------------|-------|-------|
| [Sub-item 1] | [X]% | [Details] |
| [Sub-item 2] | [X]% | [Details] |
```

---

## Risk Assessment Matrix

### Likelihood × Impact Scoring

|  | **Low Impact (1)** | **Medium Impact (2)** | **High Impact (3)** | **Critical Impact (4)** |
|---|---|---|---|---|
| **Very Likely (4)** | 4 - Medium | 8 - High | 12 - Critical | 16 - Critical |
| **Likely (3)** | 3 - Low | 6 - Medium | 9 - High | 12 - Critical |
| **Possible (2)** | 2 - Low | 4 - Medium | 6 - Medium | 8 - High |
| **Unlikely (1)** | 1 - Low | 2 - Low | 3 - Low | 4 - Medium |

### Risk Response Rules

| Risk Score | Response |
|------------|----------|
| 1-3 (Low) | Accept — Monitor post-launch |
| 4-6 (Medium) | Mitigate — Document mitigation plan before launch |
| 7-9 (High) | Reduce — Must resolve or have approved mitigation before launch |
| 10-16 (Critical) | **BLOCK** — Must resolve before launch (auto NO-GO) |

---

## 8-Week Countdown Timeline

### STANDARD+ Go-Live Preparation

| Week | Milestone | Key Activities |
|------|-----------|---------------|
| T-8 | Planning | Define go-live criteria, assign owners, establish war room schedule |
| T-7 | Infrastructure | Provision production environment, configure networking |
| T-6 | Security | Complete security scan, address critical findings |
| T-5 | Testing | Complete load/stress testing, validate performance SLAs |
| T-4 | Integration | End-to-end integration testing, data migration dry run |
| T-3 | Operations | Deploy monitoring, configure alerts, document runbooks |
| T-2 | Dry Run | Full deployment rehearsal, rollback validation |
| T-1 | Final Check | **Go-Live Readiness Assessment**, Go/No-Go decision |
| T-0 | Launch | Execute deployment, monitor, communicate |
| T+1 | Stabilize | Hyper-care period, rapid response, daily war room |

### ENTERPRISE Additional Activities

| Week | Additional Activities |
|------|----------------------|
| T-8 | Vendor/partner notification, compliance review kickoff |
| T-6 | Penetration test scheduled, DR drill planned |
| T-4 | DR drill executed, compliance evidence collected |
| T-2 | Executive briefing, external communication approved |
| T+1 | 24/7 war room, executive daily status |
| T+4 | Post-launch review, lessons learned |

---

## Go/No-Go Decision Framework

### Decision Meeting Agenda

```markdown
1. **Assessment Results** (15 min)
   - Present overall score and per-category breakdown
   - Highlight blocking issues (P0)

2. **Risk Review** (15 min)
   - Walk through risk matrix
   - Review mitigation plans for High/Critical risks

3. **Open Issues** (10 min)
   - Review unresolved P1 items
   - Agree on post-launch tracking plan

4. **Decision** (5 min)
   - GO / CONDITIONAL GO / DELAY / NO-GO
   - Document conditions (if CONDITIONAL GO)
   - Set review date (if DELAY)

5. **Action Items** (5 min)
   - Assign owners for remaining items
   - Confirm communication plan
```

### Decision Record Template

```markdown
## Go/No-Go Decision Record

**Project**: [Name]
**Decision Date**: [YYYY-MM-DD]
**Decision**: [GO / CONDITIONAL GO / DELAY / NO-GO]
**Overall Score**: [X]%

### Conditions (if CONDITIONAL GO)
1. [Condition 1 — Owner — Deadline]
2. [Condition 2 — Owner — Deadline]

### Participants
| Name | Role | Vote |
|------|------|------|
| [Name] | CTO | GO/NO-GO |
| [Name] | Engineering Manager | GO/NO-GO |
| [Name] | Tech Lead | GO/NO-GO |

### Next Review Date: [YYYY-MM-DD] (if DELAY)
```

---

## BFlow Example Assessment

**Project**: BFlow Platform v3.2
**Tier**: PROFESSIONAL
**Assessment Date**: February 14, 2026
**Go-Live Target**: March 15, 2026

| Category | Weight | Score | Weighted | Status |
|----------|--------|-------|----------|--------|
| Infrastructure | 20% | 94% | 18.8% | 🟢 |
| Security | 25% | 78% | 19.5% | 🟡 |
| Testing | 20% | 88% | 17.6% | 🟡 |
| Operations | 15% | 76% | 11.4% | 🟡 |
| Documentation | 10% | 85% | 8.5% | 🟡 |
| Communication | 10% | 92% | 9.2% | 🟢 |
| **Total** | **100%** | — | **85.0%** | **🟡 CONDITIONAL GO** |

**Decision**: CONDITIONAL GO — CTO approved with 6 conditions for April 8 go-live.

**Conditions**:
1. UAT coverage ≥80% — QA Lead — Feb 28
2. On-call rotation established — DevOps Lead — Feb 21
3. Data privacy self-assessment — Security Lead — Mar 1
4. Risk register formalized — PM — Feb 28
5. SDLC naming compliance — Tech Lead — Feb 21
6. Gate evidence collection ≥60% — PM — Mar 7

---

## Related Templates

- [deployment_go-live-readiness-checklist.md](./deployment_go-live-readiness-checklist.md) - Tactical 100-item checklist
- [governance_maturity-assessment-framework.md](./governance_maturity-assessment-framework.md) - Per-stage maturity scoring
- [governance_risk-register-analyzer.md](./governance_risk-register-analyzer.md) - Risk identification and tracking
- [governance_audit-report-generator.md](./governance_audit-report-generator.md) - Compliance audit reports
- [deployment_deployment-checklist-generator.md](./deployment_deployment-checklist-generator.md) - Deployment execution checklist
