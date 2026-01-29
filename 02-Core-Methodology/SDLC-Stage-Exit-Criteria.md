# SDLC Stage Exit Criteria

**Framework**: SDLC 6.0.0  
**Last Updated**: January 28, 2026  
**Status**: PRODUCTION-READY  
**Related**: [ADR-041 Stage Dependency Matrix](./ADR-041-Stage-Dependency-Matrix.md), Quality Gates

---

## Purpose

This document defines **stage completion criteria** that go beyond quality gates. While gates validate quality checkpoints, stage exit criteria ensure **all stage deliverables are complete**.

**Key Distinction**:
- **Quality Gate**: Validates quality at a specific checkpoint (e.g., G2 = architecture reviewed)
- **Stage Exit**: Validates all work for that stage is complete (documentation, artifacts, approvals)

**Example**:
```yaml
Stage 02 (DESIGN):
  Gate: G2 passed (architecture reviewed, ADRs approved)
  Exit Criteria:
    - All ADRs written and approved ✅
    - Architecture diagrams created ✅
    - API specifications documented ✅
    - Design review meeting held ✅
    - Stakeholder signoff received ✅
    - Sprint closed in CURRENT-SPRINT.md ✅
```

**Relationship to Dependencies**: See [ADR-041](./ADR-041-Stage-Dependency-Matrix.md) for stage prerequisites and enables relationships.

---

## Exit Criteria by Stage

### Stage 00: FOUNDATION (Strategic Discovery)

**Gate Requirement**: G0.2 passed (Solutions Explored)

**Documentation Requirements**:
- ✅ `docs/00-foundation/01-Business-Case.md` exists and complete
- ✅ `docs/00-foundation/02-User-Research/` contains 5+ user interviews (or documented reason for fewer)
- ✅ `docs/00-foundation/03-Problem-Statement.md` validated by stakeholders
- ✅ `docs/00-foundation/04-Personas/` contains primary user personas (minimum 2)
- ✅ Design Thinking workshops documented (if applicable)

**Evidence Requirements** (NEW - Sprint 106+):
- 📄 User interview recordings/transcripts (if available, not mandatory for LITE tier)
- 📄 Business case approval email/screenshot from CEO/CPO
- 📄 Problem validation evidence (user feedback, market research)
- 🔒 Evidence artifacts stored in Evidence Vault with integrity hash (optional for LITE)

**Artifact Integrity** (NEW):
- SHA256 checksum of critical deliverables:
  - `Business-Case.md`: Hash stored in metadata
  - `Problem-Statement.md`: Hash stored in metadata
  - Purpose: Detect post-approval modifications

**Stakeholder Signoff**: CEO or Product Owner

**Sprint Closure**:
- ✅ Sprint retrospective complete (if using sprint methodology)
- ✅ `CURRENT-SPRINT.md` status = COMPLETE
- ✅ All Stage 00 tasks marked as done

**Minimum (LITE Tier)**: Business case + problem statement + 3 user interviews

**Recommended (PRO/ENTERPRISE)**: Full documentation + 5+ interviews + evidence vault

**Failure Recovery**: If exit criteria not met → Refine problem statement, conduct additional user research, update business case

---

### Stage 01: PLANNING (Requirements & Architecture Planning)

**Gate Requirement**: G1 passed (Legal + Market Validated)

**Documentation Requirements**:
- ✅ `docs/01-planning/01-Requirements/` complete with functional and non-functional requirements
- ✅ `docs/01-planning/05-API-Design/API-Specification.md` exists (OpenAPI/AsyncAPI spec)
- ✅ User stories with acceptance criteria defined in `01-planning/02-User-Stories/`
- ✅ Data model drafted in `01-planning/03-Data-Model/`
- ✅ Technology stack selected and documented in `01-planning/04-Tech-Stack/`

**Evidence Requirements**:
- 📄 Requirements review meeting notes
- 📄 Stakeholder approval of requirements (email/screenshot)
- 📄 API specification validated by frontend/backend teams
- 📄 Legal review confirmation (if compliance required)

**Artifact Integrity**:
- SHA256 checksum of:
  - `API-Specification.md` (API contracts are critical!)
  - `Requirements/` folder hash
  - Purpose: Prevent scope creep after approval

**Stakeholder Signoff**: CTO or Tech Lead

**Sprint Closure**:
- ✅ Requirements review meeting held
- ✅ `CURRENT-SPRINT.md` references Stage 01 completion
- ✅ All planning tasks closed

**Minimum (LITE Tier)**: Requirements doc + API spec + user stories

**Recommended (PRO/ENTERPRISE)**: Full documentation + legal review + data model

**Failure Recovery**: If requirements unclear → Return to Stage 00 for more problem discovery

---

### Stage 02: DESIGN (Architecture & Technical Design)

**Gate Requirement**: G2 passed (Architecture Validated)

**Documentation Requirements**:
- ✅ `docs/02-design/01-Architecture/` contains architecture diagrams (C4 model recommended)
- ✅ `docs/02-design/03-ADRs/` contains ADRs for all major technical decisions
- ✅ Minimum 3 ADRs required (technology choice, architecture pattern, data storage)
- ✅ Design review meeting documented
- ✅ Security architecture documented (threat model, attack surface analysis)

**Evidence Requirements**:
- 📄 Architecture review meeting notes
- 📄 ADR approval from CTO/Tech Lead
- 📄 Design review presentation (if conducted)
- 📄 Security review signoff (if security-critical)

**Artifact Integrity**:
- SHA256 checksum of:
  - All ADRs in `03-ADRs/` folder
  - Architecture diagrams
  - Purpose: Track ADR evolution, detect unauthorized changes

**Stakeholder Signoff**: CTO or Principal Engineer

**Sprint Closure**:
- ✅ Design review complete
- ✅ All ADRs approved
- ✅ `CURRENT-SPRINT.md` references Stage 02 completion

**Minimum (LITE Tier)**: 2 ADRs + basic architecture diagram

**Recommended (PRO/ENTERPRISE)**: 5+ ADRs + C4 diagrams + security architecture

**Failure Recovery**: If architecture flawed → Revise ADRs, conduct additional design reviews

**Multi-Stage Sprint Consideration**: If sprint crosses Stage 02 → 03 → 04, ensure Stage 02 exit criteria met before advancing (see [SDLC-Stage-Sprint-Integration.md](./Governance-Compliance/SDLC-Stage-Sprint-Integration.md))

---

### Stage 03: INTEGRATE (API Contracts & Integration Points)

**Gate Requirement**: G2 passed (same as Stage 02, validates integration design)

**Documentation Requirements**:
- ✅ `docs/03-integrate/01-API-Contracts/` contains all API contract definitions
- ✅ OpenAPI/AsyncAPI specs for all external integrations
- ✅ Third-party API documentation reviewed
- ✅ Integration test strategy documented
- ✅ Error handling strategy for integrations defined

**Evidence Requirements**:
- 📄 API contract review meeting notes
- 📄 Integration partner agreements (if applicable)
- 📄 API contract validation (Postman collections, integration tests)

**Artifact Integrity**:
- SHA256 checksum of:
  - API contract specifications
  - Purpose: API contracts are critical, changes must be tracked

**Stakeholder Signoff**: Tech Lead or Integration Engineer

**Sprint Closure**:
- ✅ API contracts approved
- ✅ Integration strategy reviewed
- ✅ `CURRENT-SPRINT.md` references Stage 03 completion

**Minimum (LITE Tier)**: SKIP if no integrations, else basic API specs

**Recommended (PRO/ENTERPRISE)**: Full contract testing + integration tests

**Failure Recovery**: If API contracts incomplete → Update contracts, revise integration architecture

**Skip Conditions** (LITE Tier): No third-party APIs, monolithic app, no microservices

---

### Stage 04: BUILD (Development & Implementation)

**Gate Requirement**: G3 passed (Code + Tests Validated)

**Documentation Requirements**:
- ✅ `docs/04-build/01-Code-Review-Notes/` contains review feedback
- ✅ `docs/04-build/02-Sprint-Plans/` contains sprint documentation
- ✅ README.md in project root with setup instructions
- ✅ Code comments for complex logic
- ✅ Database migration scripts (if applicable)

**Evidence Requirements**:
- 📄 Code review approvals (GitHub/GitLab PR approvals)
- 📄 CI/CD pipeline passing (build + tests)
- 📄 Sprint retrospective notes
- 📄 Code coverage report (minimum 60% for PRO, 40% for LITE)

**Artifact Integrity**:
- Git commit hashes for all merged PRs
- Build artifact checksums (if applicable)
- Purpose: Track code changes, ensure build reproducibility

**Stakeholder Signoff**: Tech Lead or Senior Developer

**Sprint Closure**:
- ✅ All sprint tasks complete
- ✅ Code reviewed and merged
- ✅ `CURRENT-SPRINT.md` status = COMPLETE

**Minimum (LITE Tier)**: Code complete + basic tests + README

**Recommended (PRO/ENTERPRISE)**: Code review + CI/CD + 60%+ coverage

**Failure Recovery**: If code quality insufficient → Refactor, address code review feedback

**Multi-Stage Sprint Consideration**: Sprint 106 example - BUILD stage crossed with INTEGRATE stage (parallel execution allowed per ADR-041)

---

### Stage 05: TEST (Quality Assurance & Validation)

**Gate Requirement**: G3 passed (same as Stage 04, validates test coverage)

**Documentation Requirements**:
- ✅ `docs/05-test/01-Test-Plans/` contains test strategy
- ✅ Test results documented (unit, integration, E2E)
- ✅ Bug tracking log (if bugs found)
- ✅ Performance test results (if applicable)
- ✅ Accessibility audit results (for user-facing apps)

**Evidence Requirements**:
- 📄 Test execution reports (JUnit XML, pytest reports)
- 📄 Code coverage report (HTML/XML)
- 📄 Bug fix verification screenshots
- 📄 QA signoff (if separate QA team)

**Artifact Integrity**:
- Test report checksums
- Purpose: Ensure test results not tampered with

**Stakeholder Signoff**: QA Lead or Tech Lead

**Sprint Closure**:
- ✅ All tests passing
- ✅ Bugs triaged and fixed (or documented for later)
- ✅ `CURRENT-SPRINT.md` references Stage 05 completion

**Minimum (LITE Tier)**: Unit tests passing + smoke tests

**Recommended (PRO/ENTERPRISE)**: Unit + integration + E2E tests + performance testing

**Skip Conditions** (LITE Tier): Unit tests only, single developer, internal prototype

**Skip Risk**: HIGH - No QA validation, bugs reach production

**Failure Recovery**: If tests failing → Fix bugs, add missing test coverage

---

### Stage 06: DEPLOY (Release & Production Deployment)

**Gate Requirement**: G4 passed (Deployment Successful)

**Documentation Requirements**:
- ✅ `docs/06-deploy/01-Deployment-Guide.md` complete
- ✅ Rollback plan documented
- ✅ Production environment checklist complete
- ✅ DNS/CDN configuration documented (if applicable)
- ✅ Database migration plan (if schema changes)

**Evidence Requirements**:
- 📄 Deployment logs (successful deployment screenshot)
- 📄 Smoke test results (post-deployment validation)
- 📄 Stakeholder approval for production release
- 📄 Rollback plan tested (if high-risk deployment)

**Artifact Integrity**:
- Deployment artifact checksums (Docker image SHA256, build artifacts)
- Purpose: Ensure deployed code matches tested code

**Stakeholder Signoff**: CTO or DevOps Lead

**Sprint Closure**:
- ✅ Deployment successful
- ✅ Smoke tests passing in production
- ✅ `CURRENT-SPRINT.md` references Stage 06 completion

**Minimum (LITE Tier)**: Deployment guide + successful deployment

**Recommended (PRO/ENTERPRISE)**: Full deployment automation + rollback tested + monitoring configured

**Skip Conditions** (LITE Tier): Local development only, no production users

**Skip Risk**: MEDIUM - No production deployment strategy

**Failure Recovery**: If deployment fails → Rollback, fix issues, redeploy

---

### Stage 07: OPERATE (Monitoring & Operations)

**Gate Requirement**: G4 passed (same as Stage 06, validates deployment)

**Documentation Requirements**:
- ✅ `docs/07-operate/01-Monitoring-Setup.md` complete
- ✅ Incident response runbook created
- ✅ Alerting configured (uptime, errors, performance)
- ✅ Backup strategy documented
- ✅ SLA/SLO defined (if applicable)

**Evidence Requirements**:
- 📄 Monitoring dashboard screenshots (Grafana, Datadog, etc.)
- 📄 Alert test results (trigger test alerts)
- 📄 Incident response drills (if critical system)
- 📄 Backup verification (restore test)

**Artifact Integrity**:
- Monitoring configuration checksums
- Purpose: Ensure monitoring not disabled post-deployment

**Stakeholder Signoff**: DevOps Lead or SRE

**Sprint Closure**:
- ✅ Monitoring operational
- ✅ Alerts configured and tested
- ✅ `CURRENT-SPRINT.md` references Stage 07 setup (ongoing stage)

**Minimum (LITE Tier)**: Basic uptime monitoring + error logging

**Recommended (PRO/ENTERPRISE)**: Full observability stack + SLO tracking + on-call rotation

**Skip Conditions** (LITE Tier): No production monitoring needed, internal tool

**Skip Risk**: HIGH - No production monitoring, outages undetected

**Failure Recovery**: N/A (ongoing operations, incident response applies)

**Exit Criteria**: Stage 07 is **ongoing** - no formal exit, transitions to Stage 09 (Govern) for audits

---

### Stage 08: COLLABORATE (Team Coordination & Knowledge Sharing)

**Gate Requirement**: None (ongoing stage, runs throughout)

**Documentation Requirements**:
- ✅ `docs/08-collaborate/01-Team-Communication.md` exists
- ✅ Code review process documented
- ✅ Standup/meeting notes captured (if applicable)
- ✅ Knowledge base articles created (if complex project)

**Evidence Requirements**:
- 📄 Code review history (GitHub/GitLab PR comments)
- 📄 Meeting notes (sprint planning, retrospectives)
- 📄 Knowledge sharing session recordings (if conducted)

**Artifact Integrity**:
- Not applicable (collaboration artifacts are transient)

**Stakeholder Signoff**: Tech Lead or Project Manager

**Sprint Closure**:
- ✅ Team coordination activities documented
- ✅ `CURRENT-SPRINT.md` references collaboration activities

**Minimum (LITE Tier)**: SKIP if solo developer, no team

**Recommended (PRO/ENTERPRISE)**: Full collaboration process + code reviews + knowledge sharing

**Skip Conditions** (LITE Tier): Solo developer, no external stakeholders

**Skip Risk**: LOW - But reduces code quality (no peer reviews)

**Failure Recovery**: N/A (ongoing activities)

**Exit Criteria**: Stage 08 is **ongoing** - no formal exit, runs throughout project lifecycle

---

### Stage 09: GOVERN (Compliance & Governance)

**Gate Requirement**: G4 passed (standard start post-deployment)  
**Early Start**: Can start at Stage 01 for regulated industries (see ADR-041)

**Documentation Requirements**:
- ✅ `docs/09-govern/01-Compliance-Reports/` contains audit reports
- ✅ Security audit results documented
- ✅ Policy compliance checklist complete
- ✅ ADR compliance review (all ADRs reviewed for compliance)
- ✅ AI Governance Principles validation (if AI/ML system)

**Evidence Requirements**:
- 📄 Audit reports (SOC 2, ISO 27001, HIPAA, GDPR)
- 📄 Penetration test results
- 📄 Compliance certification documents
- 📄 Policy approval signatures

**Artifact Integrity**:
- Audit report checksums
- Purpose: Ensure audit results not tampered with

**Stakeholder Signoff**: CEO, CPO, or Compliance Officer

**Sprint Closure**:
- ✅ Audit complete (if scheduled)
- ✅ Compliance gaps documented and tracked
- ✅ `CURRENT-SPRINT.md` references governance activities

**Minimum (LITE Tier)**: SKIP if internal tool, no compliance requirements

**Recommended (PRO/ENTERPRISE)**: Full audit + certification + ongoing compliance monitoring

**Skip Conditions** (LITE Tier): Internal tool, no regulated data, no AI/ML components

**Skip Risk**: CRITICAL - Legal/compliance violations possible

**Failure Recovery**: If audit fails → Remediation plan, compliance gap closure, re-audit

**Exit Criteria**: Stage 09 is **ongoing** - no formal exit, runs throughout product lifecycle

**AI/ML Exception**: Always required for AI/ML systems regardless of tier (AI Governance Principles 1-6 required)

---

## Exit Criteria Matrix (Summary)

| Stage | Gate | Docs Required | Evidence Required | Stakeholder | Can Skip? | Skip Risk |
|-------|------|---------------|-------------------|-------------|-----------|-----------|
| **00-FOUNDATION** | G0.2 | Business case, user research, problem statement | User interviews, approval emails | CEO/CPO | ❌ No | N/A |
| **01-PLANNING** | G1 | Requirements, API specs, user stories | Requirements review notes | CTO | ❌ No | N/A |
| **02-DESIGN** | G2 | ADRs, architecture diagrams | Design review notes | CTO | ❌ No | N/A |
| **03-INTEGRATE** | G2 | API contracts, integration strategy | API validation | Tech Lead | ✅ Yes (LITE) | LOW |
| **04-BUILD** | G3 | Code reviews, sprint plans, README | CI/CD passing, code coverage | Tech Lead | ❌ No | N/A |
| **05-TEST** | G3 | Test plans, test results | Test reports, QA signoff | QA Lead | ✅ Yes (LITE) | HIGH |
| **06-DEPLOY** | G4 | Deployment guide, rollback plan | Deployment logs, smoke tests | CTO | ✅ Yes (LITE) | MEDIUM |
| **07-OPERATE** | G4 | Monitoring setup, incident runbook | Monitoring dashboards | DevOps | ✅ Yes (LITE) | HIGH |
| **08-COLLABORATE** | None | Team communication process | Code reviews, meeting notes | PM | ✅ Yes (Solo) | LOW |
| **09-GOVERN** | G4 | Audit reports, compliance docs | Certifications, audit results | CEO/CPO | ✅ Yes (LITE) | CRITICAL |

---

## Tier-Specific Exit Criteria

### LITE Tier (1-2 developers)

**Required Stages**: 00, 01, 02, 04  
**Optional Stages**: 03, 05, 06, 07, 08, 09

**Simplified Exit Criteria**:
- Minimum documentation (no evidence vault)
- No artifact integrity hashing
- Stakeholder signoff can be informal (Slack approval)
- Sprint closure optional (if not using sprints)

**Example LITE Exit**:
```yaml
Stage 02 (DESIGN) - LITE:
  gate: G2 passed
  docs:
    - 2 ADRs minimum (not 3)
    - Basic architecture diagram (not C4 model)
  evidence: None (no evidence vault)
  signoff: CTO approval via Slack (not formal review)
```

### PRO Tier (3-10 developers)

**Required Stages**: 00, 01, 02, 03, 04, 05, 06, 07  
**Optional Stages**: 08 (if team < 3), 09 (if no compliance)

**Standard Exit Criteria**: As documented above

### ENTERPRISE Tier (10+ developers)

**Required Stages**: All 10 stages (00-09)  
**Optional Stages**: None (all mandatory)

**Enhanced Exit Criteria**:
- Evidence vault mandatory for all artifacts
- Artifact integrity hashing required
- Formal stakeholder signoff (not Slack approvals)
- Sprint closure mandatory with retrospectives

---

## Automation Hooks (Future)

**Planned `sdlcctl` commands**:

```bash
# Validate stage exit criteria
sdlcctl validate --stage-exit 02  # Check if Stage 02 exit criteria met

# Show exit criteria checklist
sdlcctl show-exit-criteria --stage 05 --tier LITE

# Generate exit criteria report
sdlcctl report --stage-exit 00-09 --format markdown

# Validate artifact integrity
sdlcctl verify-integrity --stage 02 --artifact ADR-041.md
```

---

## Related Documents

- [ADR-041: Stage Dependency Matrix](./ADR-041-Stage-Dependency-Matrix.md) - Stage dependencies and prerequisites
- [SDLC-Stage-Sprint-Integration.md](./Governance-Compliance/SDLC-Stage-Sprint-Integration.md) - Sprint-stage coordination
- [SDLC-Tier-Stage-Requirements.md](./Documentation-Standards/SDLC-Tier-Stage-Requirements.md) - Tier-specific guidance
- [Stage-Transition-Checklist.md](../../05-Templates-Tools/2-Checklists/Stage-Transition-Checklist.md) - Actionable checklists

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-01-28 | Initial version - Stage exit criteria with evidence requirements | CTO (Tai) |

---

**Last Updated**: January 28, 2026  
**Framework Version**: SDLC 6.0.0  
**Status**: PRODUCTION-READY
