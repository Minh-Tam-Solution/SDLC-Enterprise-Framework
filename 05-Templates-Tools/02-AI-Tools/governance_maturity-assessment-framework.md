# 📈 Maturity Assessment Framework - Stage 09 (GOVERN)

**Version**: 6.0.6
**Date**: February 14, 2026
**Stage**: 09 - GOVERN (with all-stage evaluation)
**Pillar**: 1 (10-Stage Lifecycle) + 3 (4-Tier Classification) + 4 (Quality Gates)
**Time Savings**: 85% (16 hours → 2.5 hours)
**Authority**: CTO Office
**Origin**: Bflow SDLC 6.0.6 Framework Assessment (Feb 2026)

---

## Purpose

**Evidence-based maturity assessment** for SDLC 6.0.6 projects. Evaluates each stage (00-09) using weighted category scoring, produces gap analysis with P0/P1/P2 prioritization, and generates action plans with timelines. Based on Bflow's assessment methodology.

---

## AI Prompt

```yaml
System Prompt:
  You are conducting an SDLC 6.0.6 Maturity Assessment.
  Evaluate all 10 stages (00-09) with weighted category scoring.
  Produce maturity percentages with color coding (Red/Yellow/Green).
  Generate prioritized gap analysis (P0/P1/P2) and action plans.
  Apply tier-appropriate requirements.
  Reference: SDLC-Core-Methodology.md, stage requirements, gate criteria.

User Prompt Template:
  "Conduct an SDLC Maturity Assessment for:

   Project: [Name]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]
   Assessment Date: [YYYY-MM-DD]
   Current Stage: [Stage number]
   Project Age: [X months]

   For each stage (00-09), evaluate:
   1. Documentation completeness (% of required docs present)
   2. Evidence quality (gate artifacts, review records)
   3. Process maturity (adherence to SDLC methodology)
   4. Tool adoption (AI tools, automation, CI/CD)
   5. Team collaboration (protocols, RACI, reviews)

   Weight categories per tier and produce:
   - Per-stage maturity score (0-100%)
   - Overall project maturity score
   - Gap analysis with priority (P0/P1/P2)
   - 90-day action plan"
```

---

## Assessment Methodology

### Maturity Levels

| Score | Level | Color | Description |
|-------|-------|-------|-------------|
| 90-100% | ADVANCED | 🟢 Green | Exceeds requirements, exemplary practices |
| 75-89% | ESTABLISHED | 🟢 Green | Meets requirements, minor improvements needed |
| 60-74% | DEVELOPING | 🟡 Yellow | Partially meets requirements, gaps identified |
| 40-59% | INITIAL | 🟠 Orange | Significant gaps, needs structured improvement |
| 0-39% | AD-HOC | 🔴 Red | Missing or unstructured, urgent action required |

### Category Weights by Tier

| Category | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|----------|------|----------|--------------|------------|
| Documentation | 40% | 30% | 25% | 20% |
| Evidence Quality | 10% | 20% | 25% | 25% |
| Process Maturity | 20% | 20% | 20% | 20% |
| Tool Adoption | 20% | 15% | 15% | 15% |
| Team Collaboration | 10% | 15% | 15% | 20% |

---

## Per-Stage Assessment Template

### Stage Assessment Card

```markdown
## Stage [XX] — [Name] — [Score]% [Status Emoji]

### Category Scores

| Category | Weight | Score | Weighted | Evidence |
|----------|--------|-------|----------|----------|
| Documentation | [W]% | [S]% | [W×S]% | [Ref] |
| Evidence Quality | [W]% | [S]% | [W×S]% | [Ref] |
| Process Maturity | [W]% | [S]% | [W×S]% | [Ref] |
| Tool Adoption | [W]% | [S]% | [W×S]% | [Ref] |
| Team Collaboration | [W]% | [S]% | [W×S]% | [Ref] |
| **Stage Total** | **100%** | — | **[X]%** | — |

### Key Strengths
- [Strength 1]
- [Strength 2]

### Gaps (Priority Ordered)
| # | Gap | Priority | Impact | Effort | Owner |
|---|-----|----------|--------|--------|-------|
| 1 | [Gap description] | P0 | High | [Days] | [Name] |
| 2 | [Gap description] | P1 | Medium | [Days] | [Name] |

### Recommendations
1. [Actionable recommendation with timeline]
2. [Actionable recommendation with timeline]
```

---

## Stage-Specific Evaluation Criteria

### Stage 00 — Foundation (WHY?)

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Problem Statement | README exists | Formal problem doc | Design Thinking artifacts |
| Stakeholder Analysis | Informal | Documented | RACI + stakeholder map |
| Project Charter | Optional | Required | Required + approved |
| Risk Assessment | Optional | Basic risks listed | Formal risk register |

### Stage 01 — Planning (WHAT?)

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Requirements | User stories | BRD/PRD | BRD + PRD + NFRs |
| Data Model | Informal | ERD documented | ERD + data dictionary |
| API Design | Ad-hoc | OpenAPI spec | OpenAPI + contract tests |
| Sprint Planning | Kanban | Sprint backlog | Sprint + velocity tracking |

### Stage 02 — Design (HOW?)

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Architecture | Informal | SAD documented | SAD + C4 diagrams + ADRs |
| Security Design | Basic auth | Threat model | Formal threat model + ASVS |
| Tech Stack | Documented | ADR for decisions | ADRs + PoC evidence |
| Design Review | Self-review | Peer review | Architecture board review |

### Stage 03 — Integrate

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| API Contracts | Informal | OpenAPI documented | SSOT + versioned |
| Third-party | README notes | Integration docs | Integration + SLA docs |
| Data Flow | Informal | Documented | Documented + validated |

### Stage 04 — Build

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Code Quality | Linting | Linting + review | Linting + review + SAST |
| Test Coverage | >60% | >80% | >90% |
| CI/CD | Manual deploy | Basic pipeline | Full pipeline + gates |
| Sprint Docs | Optional | Sprint close doc | Sprint close + velocity |

### Stage 05 — Test

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Test Strategy | Ad-hoc | Test plan | Formal test strategy |
| UAT | Informal | Scripted UAT | UAT + sign-off |
| Performance | Manual check | Load test | Load + stress + benchmark |
| Security Test | Dependency scan | SAST | SAST + DAST + pentest |

### Stage 06 — Deploy

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Deployment | Manual | Scripted | Automated + blue-green |
| Go-Live Check | Basic checklist | Formal checklist | Full readiness assessment |
| Rollback | Documented | Tested | Automated + validated |
| Release Notes | Informal | Structured | Structured + published |

### Stage 07 — Operate

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Monitoring | Error tracking | Dashboard + alerts | Full observability |
| Incident Response | Ad-hoc | Documented process | Playbooks + escalation |
| On-Call | Best effort | Rotation defined | 24/7 + SLA |
| Post-mortems | Optional | After P0 incidents | After P0/P1 incidents |

### Stage 08 — Collaborate

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Team Protocols | Informal | Documented | Documented + enforced |
| Knowledge Sharing | Ad-hoc | Regular meetings | Wiki + ADRs + runbooks |
| RACI | Informal | Documented | Documented + reviewed |
| Onboarding | README | Guide + checklist | Structured + mentoring |

### Stage 09 — Govern

| Sub-category | LITE | STANDARD | PROFESSIONAL+ |
|--------------|------|----------|---------------|
| Compliance | Informal | Self-assessment | Formal audit |
| Risk Management | Ad-hoc | Risk register | Risk register + review |
| Metrics | Basic | DORA metrics | DORA + custom KPIs |
| Gate Evidence | Optional | Required artifacts | Full evidence vault |

---

## Overall Summary Template

```markdown
# SDLC 6.0.6 Maturity Assessment Summary

**Project**: [Name]
**Tier**: [Tier]
**Assessment Date**: [YYYY-MM-DD]
**Overall Score**: [X]% — [Level] [Emoji]

## Stage Maturity Heatmap

| Stage | Name | Score | Level | Trend |
|-------|------|-------|-------|-------|
| 00 | Foundation | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 01 | Planning | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 02 | Design | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 03 | Integrate | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 04 | Build | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 05 | Test | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 06 | Deploy | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 07 | Operate | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 08 | Collaborate | [X]% | [Level] | ⬆️/➡️/⬇️ |
| 09 | Govern | [X]% | [Level] | ⬆️/➡️/⬇️ |

## Top 5 Gaps (Priority Ordered)

| # | Stage | Gap | Priority | Impact | Action | Owner | ETA |
|---|-------|-----|----------|--------|--------|-------|-----|
| 1 | [XX] | [Gap] | P0 | Critical | [Action] | [Owner] | [Date] |
| 2 | [XX] | [Gap] | P0 | High | [Action] | [Owner] | [Date] |
| 3 | [XX] | [Gap] | P1 | High | [Action] | [Owner] | [Date] |
| 4 | [XX] | [Gap] | P1 | Medium | [Action] | [Owner] | [Date] |
| 5 | [XX] | [Gap] | P2 | Medium | [Action] | [Owner] | [Date] |
```

---

## 90-Day Action Plan Template

### Phase 1: Quick Wins (Day 1-30)

| # | Action | Stage | Priority | Owner | Target | Status |
|---|--------|-------|----------|-------|--------|--------|
| 1 | [Quick win action] | [XX] | P0 | [Owner] | [Date] | ⏳ |

### Phase 2: Structural Improvements (Day 31-60)

| # | Action | Stage | Priority | Owner | Target | Status |
|---|--------|-------|----------|-------|--------|--------|
| 1 | [Improvement action] | [XX] | P1 | [Owner] | [Date] | ⏳ |

### Phase 3: Excellence (Day 61-90)

| # | Action | Stage | Priority | Owner | Target | Status |
|---|--------|-------|----------|-------|--------|--------|
| 1 | [Excellence action] | [XX] | P2 | [Owner] | [Date] | ⏳ |

---

## Benchmark Comparison

### Maturity Benchmarks by Tier

| Stage | LITE Avg | STANDARD Avg | PROFESSIONAL Avg | ENTERPRISE Avg |
|-------|----------|--------------|------------------|----------------|
| 00 Foundation | 60% | 75% | 85% | 95% |
| 01 Planning | 55% | 70% | 82% | 92% |
| 02 Design | 50% | 68% | 80% | 90% |
| 03 Integrate | 40% | 65% | 78% | 88% |
| 04 Build | 65% | 78% | 88% | 95% |
| 05 Test | 45% | 70% | 82% | 92% |
| 06 Deploy | 50% | 72% | 85% | 93% |
| 07 Operate | 35% | 60% | 76% | 88% |
| 08 Collaborate | 40% | 65% | 78% | 90% |
| 09 Govern | 30% | 55% | 72% | 85% |

> **Note**: Benchmarks based on SDLC Orchestrator portfolio data (Bflow, NQH-Bot, MTEP). Updated quarterly.

---

## BFlow Example

**Overall Score**: 77% — DEVELOPING 🟡

| Stage | Score | Level | Key Gap |
|-------|-------|-------|---------|
| 05 Test | 82% | ESTABLISHED 🟢 | UAT coverage 40% (target 80%) |
| 06 Deploy | 88% | ESTABLISHED 🟢 | Go-live checklist not formalized |
| 07 Operate | 76% | DEVELOPING 🟡 | On-call rotation at 30% |
| 08 Collaborate | 68% | DEVELOPING 🟡 | Cross-team protocols informal |
| 09 Govern | 71% | DEVELOPING 🟡 | Risk register at 45%, data privacy at 50% |

**Top P0 Actions**:
1. Establish on-call rotation (Operate) — DevOps Lead — 2 weeks
2. Create formal risk register (Govern) — PM — 3 weeks
3. Achieve UAT coverage ≥80% (Test) — QA Lead — 4 weeks

---

## Related Templates

- [deployment_go-live-readiness-assessment.md](./deployment_go-live-readiness-assessment.md) - Go/No-Go scoring
- [deployment_go-live-readiness-checklist.md](./deployment_go-live-readiness-checklist.md) - Tactical checklist
- [governance_risk-register-analyzer.md](./governance_risk-register-analyzer.md) - Risk tracking
- [governance_audit-report-generator.md](./governance_audit-report-generator.md) - Compliance audit
- [governance_compliance-checker.md](./governance_compliance-checker.md) - Automated compliance
