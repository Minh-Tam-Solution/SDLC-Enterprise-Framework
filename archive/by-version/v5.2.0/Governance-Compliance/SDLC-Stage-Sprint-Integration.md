# SDLC Stage × Sprint Integration

**Framework**: SDLC 5.3.0  
**Last Updated**: January 28, 2026  
**Status**: PRODUCTION-READY  
**Related**: [ADR-041 Stage Dependency Matrix](../ADR-041-Stage-Dependency-Matrix.md), [Stage Exit Criteria](../SDLC-Stage-Exit-Criteria.md)

---

## Purpose

This document defines how **sprint methodology** (Pillar 2: Planning & Roadmap) integrates with **10-stage lifecycle** (Pillar 1: Core Methodology).

**Key Challenge**: Sprints are **time-boxed iterations** (1-2 weeks), while stages are **deliverable-based phases** (duration varies). Sprints can span multiple stages or stay within one stage.

**This Document Provides**:
- Multi-stage sprint handling guidelines
- G-Sprint gate integration with stage transitions
- Stage-specific sprint responsibilities
- Real examples (Sprint 106: 3-stage sprint)

---

## Multi-Stage Sprint Scenarios

### Scenario 1: Sprint Spans Multiple Stages

**Example**: Sprint 106 (App Builder Integration)
- **Stages Affected**: 02-DESIGN, 03-INTEGRATE, 04-BUILD
- **Duration**: 4 days (Day 0-3)
- **Challenge**: Must track stage transitions within sprint

**Sprint 106 Timeline**:

| Day | Stage | Deliverable | Gate |
|-----|-------|-------------|------|
| **Day 0** | 02-DESIGN | ADR-040 (Strategic Decision), ADR-041 (Stage Dependencies) | G2 (Architecture) |
| **Day 1** | 03-INTEGRATE | TemplateBlueprint schema (API contracts) | G2 (Integration) |
| **Day 1-2** | 04-BUILD | 5 templates (4,811 LOC) | G3 (Code) |
| **Day 2** | 04-BUILD | AppBuilderProvider, unit tests (1,088 LOC) | G3 (Code) |
| **Day 3** | 04-BUILD | Intent Router integration, E2E tests (552 LOC) | G3 (Code) |

**Documentation Requirements**:

```yaml
SPRINT-106-APP-BUILDER-INTEGRATION.md:
  metadata:
    stages_affected: [02-DESIGN, 03-INTEGRATE, 04-BUILD]
    primary_stage: 04-BUILD  # Where most work happens
    stage_transitions:
      - from: 02-DESIGN
        to: 03-INTEGRATE
        gate: G2
        date: 2026-01-27
        exit_criteria_met: true
      - from: 03-INTEGRATE
        to: 04-BUILD
        gate: G2
        date: 2026-01-27
        exit_criteria_met: true
  
  documentation_updates:
    stage_02: [ADR-040, ADR-041]
    stage_03: [TemplateBlueprint schema]
    stage_04: [Sprint 106 plan, 5 templates, provider, tests]
```

**G-Sprint Gates for Multi-Stage Sprint**:

**G-Sprint-Start** (Before sprint begins):
- ✅ Verify all prerequisite stages complete
- ✅ Verify current stage entry criteria met (Stage 02: G1 passed)
- ✅ Identify stage transition points in sprint plan
- ✅ Document expected stage transitions

**G-Sprint-Close** (After sprint ends):
- ✅ Verify each stage exit criteria met (Stage 02, 03, 04)
- ✅ Update all affected stage folders (docs/02-design/, docs/03-integrate/, docs/04-build/)
- ✅ Document stage transitions in CURRENT-SPRINT.md
- ✅ Commit evidence artifacts to Evidence Vault

**Rollback Procedure**:
If G-Sprint-Close fails because stage exit criteria not met:
1. Identify which stage failed exit criteria
2. Mark sprint as PARTIAL COMPLETE
3. Create follow-up sprint to complete stage
4. Do NOT advance to next stage until exit criteria met

**Example Rollback**:
```yaml
Sprint 106 Rollback Scenario (hypothetical):
  Issue: Stage 02 exit criteria not met (missing 1 ADR)
  Action:
    - Sprint 106 status: PARTIAL COMPLETE
    - Stage 02 status: INCOMPLETE (80% done)
    - Stage 03 status: BLOCKED (cannot start until Stage 02 complete)
    - Stage 04 status: BLOCKED
  Resolution:
    - Create Sprint 106.1 to complete Stage 02 ADR
    - Re-run G-Sprint-Close after completion
```

---

### Scenario 2: Sprint Entirely Within One Stage

**Example**: Sprint 105 (Quality Pipeline Enhancement)
- **Stage**: 04-BUILD (entire sprint)
- **Duration**: 5 days
- **Challenge**: None (simple scenario)

**Documentation Requirements**:

```yaml
SPRINT-105.md:
  metadata:
    stages_affected: [04-BUILD]
    primary_stage: 04-BUILD
    stage_transitions: []  # No transitions
  
  documentation_updates:
    stage_04:
      - backend/app/services/codegen/quality_pipeline.py
      - docs/04-build/02-Sprint-Plans/SPRINT-105.md
```

**G-Sprint Gates for Single-Stage Sprint**:

**G-Sprint-Start**:
- ✅ Verify Stage 04 entry criteria met (G2 passed)
- ✅ Verify prerequisite stages complete (Stage 02-DESIGN)

**G-Sprint-Close**:
- ✅ Update Stage 04 documentation
- ✅ No stage transition tracking needed
- ✅ Commit code to Stage 04 folder structure

---

### Scenario 3: Sprint Starts Mid-Stage

**Example**: Sprint 107 (Quality Gates Integration) - starts in middle of Stage 04
- **Stage**: 04-BUILD (already in progress)
- **Previous Sprint**: Sprint 106 completed Stage 04 partially
- **Challenge**: Track stage continuation, not stage entry

**Documentation Requirements**:

```yaml
SPRINT-107.md:
  metadata:
    stages_affected: [04-BUILD]
    primary_stage: 04-BUILD
    stage_status: IN_PROGRESS  # Not starting fresh
    previous_sprint: SPRINT-106
  
  stage_continuation:
    stage_04:
      entry_date: 2026-01-27 (Sprint 106)
      continuation_date: 2026-01-30 (Sprint 107)
      progress: 60% (after Sprint 106)
      remaining: Quality Gates integration
```

**G-Sprint Gates for Mid-Stage Sprint**:

**G-Sprint-Start**:
- ✅ Verify stage entry criteria already met (from previous sprint)
- ✅ Review stage progress from previous sprint
- ✅ Confirm no stage exit criteria missed

**G-Sprint-Close**:
- ✅ Update stage documentation (append to existing)
- ✅ Check if stage exit criteria now met (if yes, stage complete)
- ✅ If stage incomplete, document progress for next sprint

---

## Stage-Specific Sprint Responsibilities

### Stage 00: FOUNDATION (Strategic Discovery)

**Sprint Work**: Design Thinking workshops, user research, business case development

**Sprint Artifacts**:
- User interview recordings/transcripts
- Workshop facilitation notes
- Problem statement drafts
- Business case documents

**Sprint Documentation Location**: `docs/00-foundation/`

**Sprint Responsibilities**:
- Facilitate Design Thinking workshops
- Conduct user interviews
- Draft business case
- Validate problem statement with stakeholders

**G-Sprint Integration**:
- **G-Sprint-Start**: No prerequisites (Stage 00 is first)
- **G-Sprint-Close**: Verify G0.1 and G0.2 gates passed

**Typical Sprint Count**: 1-2 sprints (LITE: 1 sprint)

---

### Stage 01: PLANNING (Requirements & Architecture Planning)

**Sprint Work**: Requirements gathering, API design, user story creation

**Sprint Artifacts**:
- Requirements documents
- API specifications (OpenAPI)
- User stories with acceptance criteria
- Data models

**Sprint Documentation Location**: `docs/01-planning/`

**Sprint Responsibilities**:
- Gather functional and non-functional requirements
- Draft API contracts
- Create user stories
- Define acceptance criteria
- Select technology stack

**G-Sprint Integration**:
- **G-Sprint-Start**: Verify G0.2 passed (Stage 00 complete)
- **G-Sprint-Close**: Verify G1 passed (Legal + Market validated)

**Typical Sprint Count**: 1-2 sprints (LITE: 1 sprint)

---

### Stage 02: DESIGN (Architecture & Technical Design)

**Sprint Work**: Architecture design, ADR creation, design reviews

**Sprint Artifacts**:
- Architecture diagrams (C4 model)
- ADRs (minimum 3 for LITE, 5+ for PRO)
- Design review notes
- Security architecture documents

**Sprint Documentation Location**: `docs/02-design/`

**Sprint Responsibilities**:
- Create architecture diagrams
- Write ADRs for major technical decisions
- Conduct design reviews
- Define security architecture
- Review and approve ADRs

**G-Sprint Integration**:
- **G-Sprint-Start**: Verify G1 passed (Stage 01 complete)
- **G-Sprint-Close**: Verify G2 passed (Architecture validated)

**Typical Sprint Count**: 1-2 sprints (LITE: 1 sprint)

**Example**: Sprint 106 Day 0 created ADR-040 and ADR-041 in Stage 02

---

### Stage 03: INTEGRATE (API Contracts & Integration Points)

**Sprint Work**: API contract definition, integration design, contract testing

**Sprint Artifacts**:
- API contract specifications (OpenAPI/AsyncAPI)
- Integration test strategies
- Error handling designs
- Third-party API documentation

**Sprint Documentation Location**: `docs/03-integrate/`

**Sprint Responsibilities**:
- Define API contracts
- Design integration architecture
- Plan contract testing
- Document error handling strategies

**G-Sprint Integration**:
- **G-Sprint-Start**: Verify G2 passed (Stage 02 complete)
- **G-Sprint-Close**: Verify G2 passed (Integration design validated)

**Typical Sprint Count**: 0-1 sprints (LITE: Skip if no integrations)

**Can Run Parallel**: Stage 03 can run parallel to Stage 04 (BUILD) per ADR-041

**Example**: Sprint 106 Day 1 created TemplateBlueprint schema (API contract) in Stage 03

---

### Stage 04: BUILD (Development & Implementation)

**Sprint Work**: Feature development, code reviews, unit testing

**Sprint Artifacts**:
- Source code
- Unit tests
- Code review notes
- Sprint retrospectives

**Sprint Documentation Location**: `docs/04-build/02-Sprint-Plans/`

**Sprint Responsibilities**:
- Implement features per user stories
- Write unit tests (60%+ coverage for PRO)
- Conduct code reviews
- Update sprint plans
- Run CI/CD pipelines

**G-Sprint Integration**:
- **G-Sprint-Start**: Verify G2 passed (Stage 02 complete)
- **G-Sprint-Close**: Verify G3 passed (Code + Tests validated)

**Typical Sprint Count**: 2-10 sprints (depends on project size)

**Example**: Sprint 106 Day 1-3 implemented 5 templates, provider, tests in Stage 04 (7,258 LOC)

---

### Stage 05: TEST (Quality Assurance & Validation)

**Sprint Work**: Integration testing, E2E testing, bug fixing

**Sprint Artifacts**:
- Test plans
- Test execution reports
- Bug tracking logs
- Code coverage reports

**Sprint Documentation Location**: `docs/05-test/`

**Sprint Responsibilities**:
- Execute integration tests
- Run E2E test suites
- Triage and fix bugs
- Generate code coverage reports
- QA signoff

**G-Sprint Integration**:
- **G-Sprint-Start**: Verify G3 passed (Stage 04 complete)
- **G-Sprint-Close**: Verify G3 passed (Tests validated)

**Typical Sprint Count**: 1-2 sprints (LITE: 0-1 sprints)

---

### Stage 06: DEPLOY (Release & Production Deployment)

**Sprint Work**: Deployment automation, production rollout, smoke testing

**Sprint Artifacts**:
- Deployment guides
- Rollback plans
- Deployment logs
- Smoke test results

**Sprint Documentation Location**: `docs/06-deploy/`

**Sprint Responsibilities**:
- Prepare production environment
- Execute deployment
- Run smoke tests
- Monitor initial production metrics
- Document rollback procedures

**G-Sprint Integration**:
- **G-Sprint-Start**: Verify G3 passed (Stage 05 complete)
- **G-Sprint-Close**: Verify G4 passed (Deployment successful)

**Typical Sprint Count**: 0.5-1 sprints (3-5 days)

---

### Stage 07: OPERATE (Monitoring & Operations)

**Sprint Work**: Monitoring setup, incident response, performance optimization

**Sprint Artifacts**:
- Monitoring dashboards
- Incident response runbooks
- Alerting configurations
- SLA/SLO definitions

**Sprint Documentation Location**: `docs/07-operate/`

**Sprint Responsibilities**:
- Configure monitoring (Grafana, Datadog)
- Set up alerting
- Create incident response runbooks
- Define SLAs/SLOs
- Run incident drills

**G-Sprint Integration**:
- **G-Sprint-Start**: Verify G4 passed (Stage 06 complete)
- **G-Sprint-Close**: Verify monitoring operational

**Typical Sprint Count**: 1 sprint (setup), then ongoing operations

**Note**: Stage 07 is ongoing - no formal exit, continuous operations

---

### Stage 08: COLLABORATE (Team Coordination & Knowledge Sharing)

**Sprint Work**: Code reviews, standup meetings, knowledge sharing

**Sprint Artifacts**:
- Meeting notes
- Code review comments
- Knowledge base articles
- Team communication logs

**Sprint Documentation Location**: `docs/08-collaborate/`

**Sprint Responsibilities**:
- Facilitate daily standups
- Coordinate code reviews
- Share knowledge across team
- Resolve conflicts
- Synchronize cross-team work

**G-Sprint Integration**:
- **G-Sprint-Start**: No prerequisites (runs throughout)
- **G-Sprint-Close**: Document collaboration activities

**Typical Sprint Count**: Ongoing (throughout project)

**Can Run Parallel**: Stage 08 supports all other stages (01-07) per ADR-041

---

### Stage 09: GOVERN (Compliance & Governance)

**Sprint Work**: Audits, compliance reviews, policy enforcement

**Sprint Artifacts**:
- Audit reports
- Compliance checklists
- Policy documents
- ADR compliance reviews

**Sprint Documentation Location**: `docs/09-govern/`

**Sprint Responsibilities**:
- Conduct security audits
- Review ADRs for compliance
- Execute compliance audits (SOC 2, HIPAA, GDPR)
- Validate AI Governance Principles (if AI/ML)
- Obtain certifications

**G-Sprint Integration**:
- **G-Sprint-Start**: Verify G4 passed (Stage 06 complete) OR early start for regulated industries
- **G-Sprint-Close**: Document audit findings

**Typical Sprint Count**: 1-2 sprints (audit execution), then ongoing governance

**Early Start**: Can start at Stage 01 for regulated industries per ADR-041

**Can Run Parallel**: Stage 09 runs parallel to Stages 02, 04, 06, 07 if early start

---

## G-Sprint Gate Integration Summary

### G-Sprint-Start (Before Sprint)

**Checklist**:
- [ ] Identify stages affected by sprint (single or multi-stage)
- [ ] Verify prerequisite stages complete (check ADR-041 dependencies)
- [ ] Verify current stage entry criteria met (check Stage Exit Criteria doc)
- [ ] If multi-stage: Document expected stage transitions
- [ ] If mid-stage: Review progress from previous sprint

**Documentation**:
```yaml
# SPRINT-XXX.md header
metadata:
  stages_affected: [02-DESIGN, 04-BUILD]
  primary_stage: 04-BUILD
  stage_transitions:
    - from: 02-DESIGN
      to: 04-BUILD
      expected_date: 2026-XX-XX
      gate: G2
```

### G-Sprint-Close (After Sprint)

**Checklist**:
- [ ] Verify all stage exit criteria met (per Stage Exit Criteria doc)
- [ ] Update all affected stage folders
- [ ] Document stage transitions in CURRENT-SPRINT.md
- [ ] Commit evidence artifacts to Evidence Vault (if applicable)
- [ ] Run sprint retrospective
- [ ] If stage incomplete: Document progress for next sprint
- [ ] If stage complete: Mark stage exit date

**Documentation**:
```yaml
# CURRENT-SPRINT.md closure
status: COMPLETE
stages_completed: [02-DESIGN, 04-BUILD]
stage_transitions:
  - from: 02-DESIGN
    to: 04-BUILD
    gate: G2
    actual_date: 2026-01-27
    exit_criteria_met: true
evidence_artifacts:
  - ADR-040.md (hash: abc123...)
  - TemplateBlueprint.py (hash: def456...)
```

---

## Real Example: Sprint 106 (3-Stage Sprint)

**Sprint**: 106 - App Builder Integration  
**Duration**: 4 days (Day 0-3)  
**Stages**: 02-DESIGN → 03-INTEGRATE → 04-BUILD

### Day 0: Stage 02 (DESIGN)

**Work**:
- Created ADR-040 (Strategic Decision)
- Created ADR-041 (Stage Dependencies)
- Designed TemplateBlueprint architecture

**Stage Transition**: Stage 02 → Stage 03
- **Gate**: G2 (Architecture Validated)
- **Exit Criteria Met**:
  - ✅ ADRs created (2 ADRs)
  - ✅ Architecture design complete
  - ✅ CTO approval received

### Day 1: Stage 03 (INTEGRATE)

**Work**:
- Created TemplateBlueprint schema (API contract)
- Defined IntentRouter interface
- Documented QualityGateProfile schema

**Stage Transition**: Stage 03 → Stage 04
- **Gate**: G2 (Integration Design Validated)
- **Exit Criteria Met**:
  - ✅ API contracts defined (TemplateBlueprint)
  - ✅ Integration points documented
  - ✅ Tech Lead approval received

### Day 1-3: Stage 04 (BUILD)

**Work**:
- Day 1: 5 templates (4,811 LOC)
- Day 2: AppBuilderProvider + tests (1,088 LOC)
- Day 3: Intent Router integration + E2E tests (552 LOC)

**Stage Exit**: Stage 04 complete
- **Gate**: G3 (Code + Tests Validated)
- **Exit Criteria Met**:
  - ✅ Code complete (7,258 LOC)
  - ✅ Unit tests passing (28 test cases)
  - ✅ Integration tests passing (18 test cases)
  - ✅ CI/CD pipeline passing
  - ✅ Code review approved
  - ✅ Sprint retrospective complete

### G-Sprint-Close Summary

```yaml
sprint: 106
status: COMPLETE
duration: 4 days
stages_affected: [02-DESIGN, 03-INTEGRATE, 04-BUILD]
stage_transitions:
  - from: 02-DESIGN
    to: 03-INTEGRATE
    gate: G2
    date: 2026-01-27
    exit_criteria_met: true
  - from: 03-INTEGRATE
    to: 04-BUILD
    gate: G2
    date: 2026-01-27
    exit_criteria_met: true
  - stage: 04-BUILD
    status: COMPLETE
    gate: G3
    date: 2026-01-28
    exit_criteria_met: true

deliverables:
  stage_02: [ADR-040, ADR-041]
  stage_03: [TemplateBlueprint schema, IntentRouter interface]
  stage_04: [5 templates, AppBuilderProvider, 64 test cases]

total_loc: 7,258
test_coverage: 64 test cases
business_impact: 95% cost reduction
```

**Lessons Learned**:
- Multi-stage sprints require explicit stage transition tracking
- G-Sprint-Close must verify exit criteria for each stage
- Documentation updates must span multiple stage folders
- Stage transitions can happen mid-sprint (Day 0 → Day 1)

---

## Rollback Procedure (Stage Exit Criteria Not Met)

**Scenario**: Sprint closes but stage exit criteria not met

**Step 1: Identify Failed Criteria**
```yaml
sprint: 107
status: PARTIAL COMPLETE
stage: 04-BUILD
failed_criteria:
  - "Code coverage < 60% (actual: 45%)"
  - "Missing code review approval"
```

**Step 2: Mark Sprint as Partial**
```yaml
# CURRENT-SPRINT.md
status: PARTIAL COMPLETE (80% done)
next_sprint: SPRINT-107.1 (cleanup sprint)
blocked_stages: [05-TEST]  # Cannot start until Stage 04 complete
```

**Step 3: Create Follow-Up Sprint**
```yaml
# SPRINT-107.1.md
type: CLEANUP_SPRINT
duration: 1-2 days
goal: Complete Stage 04 exit criteria
tasks:
  - Increase code coverage to 60%
  - Get code review approval
  - Re-run G-Sprint-Close
```

**Step 4: Re-Run G-Sprint-Close**
- After follow-up sprint completes
- Verify all exit criteria now met
- Mark sprint as COMPLETE
- Unblock next stage (Stage 05-TEST)

---

## Sprint Planning Template (With Stage Tracking)

**Template**: `docs/04-build/02-Sprint-Plans/SPRINT-XXX.md`

```markdown
# Sprint XXX: [Sprint Name]

**Status**: ACTIVE | COMPLETE | PARTIAL COMPLETE  
**Duration**: X days  
**Stages Affected**: [XX-STAGE, XX-STAGE]  
**Primary Stage**: XX-STAGE  

## Stage Tracking

### Stages Affected
- **XX-STAGE**: [Entry criteria met? | In progress | Complete]
- **XX-STAGE**: [Entry criteria met? | In progress | Complete]

### Stage Transitions (if multi-stage)
| From | To | Gate | Expected Date | Actual Date | Exit Criteria Met? |
|------|----|----|---------------|-------------|--------------------|
| XX | XX | GX | YYYY-MM-DD | YYYY-MM-DD | ✅ Yes / ❌ No |

## Work Breakdown by Stage

### Stage XX: [STAGE NAME]
**Work**:
- Task 1
- Task 2

**Deliverables**:
- Artifact 1 (location: docs/XX-stage/...)
- Artifact 2

**Exit Criteria Checklist**:
- [ ] Documentation complete
- [ ] Stakeholder signoff received
- [ ] Gate passed

### Stage XX: [STAGE NAME]
[... repeat ...]

## G-Sprint Gates

### G-Sprint-Start Checklist
- [ ] Prerequisite stages verified
- [ ] Entry criteria met for current stage(s)
- [ ] Stage transitions documented

### G-Sprint-Close Checklist
- [ ] All stage exit criteria met
- [ ] Documentation updated
- [ ] Evidence artifacts committed
- [ ] Sprint retrospective complete
```

---

## Related Documents

- [ADR-041: Stage Dependency Matrix](../ADR-041-Stage-Dependency-Matrix.md) - Stage dependencies and prerequisites
- [SDLC-Stage-Exit-Criteria.md](../SDLC-Stage-Exit-Criteria.md) - Stage completion criteria
- [SDLC-Tier-Stage-Requirements.md](../Documentation-Standards/SDLC-Tier-Stage-Requirements.md) - Tier-specific guidance
- [Sprint 106 Completion Summary](../../../docs/04-build/02-Sprint-Plans/SPRINT-106-COMPLETION-SUMMARY.md) - Real multi-stage sprint example

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-01-28 | Initial version - Stage-sprint integration with Sprint 106 example | CTO (Tai) |

---

**Last Updated**: January 28, 2026  
**Framework Version**: SDLC 5.3.0  
**Status**: PRODUCTION-READY
