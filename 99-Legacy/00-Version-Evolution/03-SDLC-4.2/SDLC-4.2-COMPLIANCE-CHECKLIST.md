# SDLC 4.2 COMPLIANCE CHECKLIST (v0.1)

## Purpose

Operational checklist to enforce Design-First + AI+Human orchestration. Updated weekly by Compliance Bot.

## Phase / Gate Matrix

| Phase | Gate | Mandatory Artefacts | Pass Criteria | Evidence Location | Status | Notes |
|-------|------|---------------------|---------------|-------------------|--------|-------|
| Foundation | G0 Init | Project Charter, Vision, Risk Log | All approved | docs/00-Project-Foundation |  |  |
| Planning | G1 Requirements Freeze | Req Spec, Use Case Set, Risk Update | ≥95% requirements ID'd; no critical TBD | docs/01-Planning-Analysis |  |  |
| Design | G2 Design Approval | Architecture Briefs, API Contracts, Data Models | 100% high-risk features have design IDs | docs/02-Design-Architecture |  |  |
| Dev Prep | G3 Dev Readiness | Traceability Map v1, Test Strategy, Env Spec | Trace coverage ≥70% | docs/03-Development-Implementation |  |  |
| Implementation | G4 Iteration Cycle | Updated Trace Map, Drift Report, Coverage Report | Drift <10%, Design coverage ≥90% | reports/ (to add) |  |  |
| Verification | G5 Pre-UAT | Test Pass Report, Perf Baseline, Security Scan | No Sev1 open, Sev2<=3, p95 < target+15% | tests/reports |  |  |
| UAT | G6 UAT Exit | UAT Summary, Cultural Eval, DR Drill Log | UAT pass ≥95%, cultural accuracy ≥98% | tests/reports |  |  |
| Release | G7 Go-Live | Runbook, Rollback Plan, Final Coverage | Coverage (critical paths) ≥85% | deployment/ |  |  |
| Post-Release | G8 Stabilization | Incident Log, Post-mortems, Metrics Pack | MTTR Sev1 <60m, 0 cross-tenant leak | ops/reports |  |  |

## KPI Dashboard (Snapshot placeholders)

| KPI | Target | Current | Source | Status |
|-----|--------|---------|--------|--------|
| Design Coverage | ≥95% |  | coverage_report.json |  |
| Traceability Completeness | ≥90% |  | traceability_map.md |  |
| API Drift | <10% |  | api_drift_report.json |  |
| Critical Path Test Coverage | ≥85% |  | coverage_report.json |  |
| UAT Pass Rate | ≥95% |  | uat_report.json |  |
| Cultural Accuracy | ≥98% |  | cultural_eval_report.json |  |
| Perf p95 Core APIs | <100ms |  | perf_report.json |  |
| Sev1 MTTR | <60m |  | incident_log.md |  |

## Gate Violation Escalation

| Level | Condition | Action | Owner |
|-------|-----------|--------|-------|
| L1 | Single gate failed | Fix within 24h | Feature Dev Lead |
| L2 | Same gate fails 2 sprints | Root cause retro | CTO |
| L3 | ≥3 gates fail in sprint | Exec review | CPO/CTO |
| L4 | Repeated systemic (3 consecutive sprints) | Process overhaul plan | CTO |

## Definition of Done (Augmented)

- Requirement mapped (REQ-*) in TRACEABILITY-MAP
- Design ID (DES-*) referenced in PR
- Tests (Unit+Integration) added & green
- API spec updated & drift check passed
- Logging & basic metrics added
- Documentation section updated (CHANGELOG if user-visible)
- No new security high severity issues

## Cultural Intelligence Compliance

| Dimension | Check | Tool/Artefact | Status |
|-----------|-------|---------------|--------|
| Vietnamese Hierarchy | Role mapping present | cultural_eval_report.json |  |
| MVV Case Link (DNA0) | Business case ID linked | traceability_map.md |  |
| Process Lifecycle (DNA3) | Workflow state transitions tested | tests/ |  |
| AI WHY (DNA8) | Explanation consistency test | cultural_eval_report.json |  |
| Knowledge Monetization (DNA9) | Tagging in code comments | code scan |  |

## Automation Ownership

| Domain | Script / Tool | Path (planned) | Owner |
|--------|---------------|----------------|-------|
| API Drift | api_drift_check.py | scripts/compliance/ | Platform |
| Coverage | coverage_report.py | scripts/compliance/ | QA |
| Compliance Aggregate | compliance_report.py | scripts/compliance/ | QA |
| Cultural Eval | cultural_eval_runner.py | scripts/compliance/ | AI Team |
| Perf Baseline | perf_smoke.py | scripts/perf/ | SRE |

## Open Items

- [ ] Populate current metrics
- [ ] Integrate scripts & CI jobs
- [ ] Add links once reports generated

Last updated: initial scaffold v0.1
