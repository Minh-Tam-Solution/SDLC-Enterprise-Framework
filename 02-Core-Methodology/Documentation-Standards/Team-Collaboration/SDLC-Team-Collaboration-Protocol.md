# SDLC Team Collaboration Protocol

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology (Documentation Standards / Team Collaboration)
**Status**: ACTIVE - Production Standard
**Authority**: CPO Office
**Industry Standards**: Team Topologies, SAFe 6.0

---

## Purpose

Define **multi-team collaboration protocols** for coordinating N teams within an SDLC project. This document provides:
- Team structure templates
- RACI matrix framework
- Handoff protocols
- Dependency management

**Key Insight**: Focus on **deliverables and handoffs**, not team locations. A team in the same office still needs explicit handoff protocols.

---

## Project Governance Structure

### Governance Roles

```yaml
Project Owner (PO):
  Responsibility:
    - Strategic direction
    - Final sign-off on major decisions
    - Budget approval
    - Stakeholder communication
  Authority: Strategic, Budget
  Escalation To: Sponsor/Executive

Project Manager (PM):
  Responsibility:
    - Cross-team coordination
    - Stakeholder management
    - Risk escalation
    - Timeline management
  Authority: Cross-team, Stakeholders
  Escalation To: PO

Project Manager (PJM):
  Responsibility:
    - Day-to-day execution
    - Sprint management
    - Team sync facilitation
    - Blocker resolution
  Authority: Execution, Sprint
  Escalation To: PM
```

### Governance by Tier

```yaml
LITE (1-2 people):
  - No formal governance
  - Owner = PM = PJM = Developer

STANDARD (3-10 people):
  - PM/Tech Lead as combined role
  - Weekly governance sync

PROFESSIONAL (10-50 people):
  - Separate PM, PJM roles
  - Bi-weekly steering meetings
  - Formal escalation path

ENTERPRISE (50+ people):
  - PMO (Project Management Office)
  - Multiple PMs/PJMs
  - Weekly executive reviews
  - CAB (Change Advisory Board)
```

---

## Team Structure Framework

### Team Definition Template

```yaml
Team [X]:
  Name: [Team Name]
  Type: Stream-aligned | Platform | Enabling | Complicated-Subsystem
  Role: [Primary responsibility - what does this team own?]
  Members:
    Count: [Number]
    Key Roles:
      - [Role 1]: [Name]
      - [Role 2]: [Name]
  Deliverables: [What this team produces]
  Dependencies:
    Upstream:
      - [Team providing input]: [What they provide]
    Downstream:
      - [Team receiving output]: [What we provide them]
  Sync Cadence:
    Intra-team: [Daily standup time]
    Inter-team: [With whom, when]
  Communication:
    Primary Channel: [#team-name]
    External Channel: [#team-name-external]
```

### Team Types (Team Topologies)

```yaml
Stream-Aligned Team:
  Definition: Aligned to single flow of work (feature, product, user journey)
  Responsibility: End-to-end delivery of value
  Example: "Product Team Alpha" owns user authentication feature
  Dependency: Minimal (ideally autonomous)

Platform Team:
  Definition: Provides internal services to other teams
  Responsibility: Accelerate stream-aligned teams
  Example: "Platform Team" provides CI/CD, monitoring, auth services
  Dependency: Other teams consume their services

Enabling Team:
  Definition: Helps other teams adopt new skills/technologies
  Responsibility: Temporary capability boost
  Example: "DevOps Enablement" helps teams adopt K8s
  Dependency: Provides expertise, then moves on

Complicated-Subsystem Team:
  Definition: Owns complex components requiring specialist knowledge
  Responsibility: Build and maintain complex subsystems
  Example: "ML Team" owns recommendation engine
  Dependency: Other teams consume their APIs
```

### Example: 3-Team Product Setup

```yaml
Team A - Design & Architecture:
  Type: Enabling (for design) + Stream-aligned (for architecture)
  Role: Create designs, define API contracts, make architectural decisions
  Members:
    Count: 3
    Key Roles:
      - Solutions Architect: [Name]
      - UI/UX Designer: [Name]
      - API Designer: [Name]
  Deliverables:
    - Architecture Decision Records (ADRs)
    - UI/UX designs (Figma)
    - API contracts (OpenAPI specs)
    - Technical specifications
  Dependencies:
    Upstream: None (starting point for most features)
    Downstream:
      - Team B: Receives designs for implementation
  Sync Cadence:
    Intra-team: Daily 9:00 AM
    Inter-team: Wed 3:00 PM with Team B (design handoff)
  Communication:
    Primary: #team-design
    External: #design-reviews

Team B - Implementation:
  Type: Stream-aligned
  Role: Build features based on designs
  Members:
    Count: 5
    Key Roles:
      - Tech Lead: [Name]
      - Backend Developer (x2): [Names]
      - Frontend Developer (x2): [Names]
  Deliverables:
    - Working code (backend + frontend)
    - Unit tests (95%+ coverage)
    - Integration tests
    - Documentation updates
  Dependencies:
    Upstream:
      - Team A: Provides designs and API specs
    Downstream:
      - Team C: Provides code for testing
  Sync Cadence:
    Intra-team: Daily 10:00 AM
    Inter-team:
      - Wed 3:00 PM with Team A (receive designs)
      - Fri 2:00 PM with Team C (code handoff)
  Communication:
    Primary: #team-backend, #team-frontend
    External: #implementation-status

Team C - QA & Operations:
  Type: Stream-aligned (QA) + Platform (Ops)
  Role: Test, deploy, and operate the system
  Members:
    Count: 3
    Key Roles:
      - QA Lead: [Name]
      - SRE: [Name]
      - DevOps Engineer: [Name]
  Deliverables:
    - Test plans and reports
    - Deployment pipelines
    - Runbooks and alerts
    - Performance reports
  Dependencies:
    Upstream:
      - Team B: Provides code to test and deploy
    Downstream:
      - Production: Deploys to users
  Sync Cadence:
    Intra-team: Daily 11:00 AM
    Inter-team: Fri 2:00 PM with Team B (receive code)
  Communication:
    Primary: #team-qa, #team-ops
    External: #release-coordination
```

---

## RACI Matrix Framework

### What is RACI?

```yaml
R - Responsible:
  Definition: Does the work
  Count: One or more per deliverable
  Identifies: Who executes the task

A - Accountable:
  Definition: Final decision authority
  Count: Exactly ONE per deliverable
  Identifies: Who approves the work

C - Consulted:
  Definition: Provides input before decision
  Count: Zero or more
  Identifies: Who has expertise to share

I - Informed:
  Definition: Kept updated after decision
  Count: Zero or more
  Identifies: Who needs to know
```

### RACI Matrix Template

```markdown
| Deliverable | Team A | Team B | Team C | PM | PO |
|-------------|--------|--------|--------|----|----|
| Architecture Design | R, A | C | I | I | I |
| API Contract | R, A | C | I | I | I |
| UI Design | R, A | C | I | I | I |
| Backend Code | C | R, A | I | I | I |
| Frontend Code | C | R, A | I | I | I |
| Unit Tests | I | R, A | C | I | I |
| Integration Tests | I | C | R, A | I | I |
| E2E Tests | I | C | R, A | I | I |
| Deployment | I | C | R, A | I | I |
| Release Decision | C | C | C | R | A |
| Scope Change | I | I | I | C | A |
```

### RACI Example: Feature Development

```yaml
Feature: User Authentication with MFA

RACI Matrix:
  | Task | Design | Backend | Frontend | QA | PM |
  |------|--------|---------|----------|----|----|
  | Requirements | C | I | I | I | A |
  | Architecture ADR | A | C | C | I | I |
  | API Contract | A | C | I | I | I |
  | UI Mockups | A | I | C | I | I |
  | Backend API | C | A | I | I | I |
  | Frontend UI | C | I | A | I | I |
  | Unit Tests | I | A | A | C | I |
  | Integration Tests | I | C | C | A | I |
  | Security Review | C | C | C | A | I |
  | Documentation | C | A | A | C | I |
  | Release Decision | I | C | C | C | A |

Key: A=Accountable, R=Responsible, C=Consulted, I=Informed
```

---

## Handoff Protocol Framework

### Handoff Definition

```yaml
Handoff:
  Definition: Formal transfer of work from one team to another
  Trigger: When upstream team completes their deliverable
  Requirement: Clear acceptance criteria (Definition of Done)
  Documentation: What must be provided with the handoff
  Feedback Loop: How receiving team requests changes
```

### Handoff Protocol Template

```markdown
## Handoff: [Source Team] → [Target Team]

### Trigger
[When does this handoff happen?]

### Acceptance Criteria (DoD)
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

### Documentation Required
- [ ] Document 1
- [ ] Document 2

### Process
1. Source team posts in #handoff channel
2. Target team has [X hours] to review
3. Q&A session scheduled if needed
4. Target team accepts or requests changes
5. Source team addresses feedback
6. Handoff complete when target team signs off

### Sign-off
- Source Team Lead: [Name] - Date: [YYYY-MM-DD]
- Target Team Lead: [Name] - Date: [YYYY-MM-DD]
```

### Handoff Example: Design → Implementation

```yaml
Handoff: Team A (Design) → Team B (Implementation)

Trigger:
  - Design marked "Ready for Review" in project board
  - All design documents in /docs/02-Design-Architecture/

Acceptance Criteria (DoD):
  - [ ] ADR(s) documented for major decisions
  - [ ] API contract (OpenAPI 3.0) complete
  - [ ] UI designs in Figma with component specs
  - [ ] Data model changes documented
  - [ ] Security considerations documented
  - [ ] Estimated effort provided

Documentation Required:
  - [ ] ADR document(s)
  - [ ] OpenAPI spec (openapi.yml)
  - [ ] Figma link with design specs
  - [ ] ERD changes (if any)
  - [ ] Sequence diagrams (for complex flows)

Process:
  1. Design team posts in #handoff:
     "Design ready for [Feature X]. Docs: [links]. Ready for review."
  2. Implementation team has 24 hours to review
  3. Questions posted in #handoff thread
  4. Design team clarifies within 4 hours
  5. If major changes needed → Schedule sync meeting
  6. Implementation team replies: "Accepted" or "Changes needed: [list]"
  7. Design team addresses feedback
  8. Handoff complete when Implementation team says "Handoff accepted"

Sign-off:
  - Design Lead: _____________ Date: _______
  - Implementation Lead: _____________ Date: _______
```

### Handoff Example: Implementation → QA

```yaml
Handoff: Team B (Implementation) → Team C (QA)

Trigger:
  - PR merged to develop branch
  - Feature flag enabled in staging
  - Dev team declares "Ready for QA"

Acceptance Criteria (DoD):
  - [ ] All code merged to develop
  - [ ] Unit tests passing (95%+ coverage)
  - [ ] Integration tests passing
  - [ ] No critical/high linting errors
  - [ ] Staging environment updated
  - [ ] Test data prepared

Documentation Required:
  - [ ] Test scenarios / user journeys to test
  - [ ] Known limitations / edge cases
  - [ ] Environment configuration
  - [ ] Rollback procedure (if issues found)

Process:
  1. Dev team posts in #handoff:
     "Feature [X] ready for QA. Staging: [URL]. Test scenarios: [link]"
  2. QA team acknowledges within 4 hours
  3. QA executes test plan (1-3 days depending on scope)
  4. Bugs logged in issue tracker with severity
  5. Dev team fixes bugs (P0/P1 immediately, P2/P3 scheduled)
  6. Re-test after fixes
  7. QA signs off: "QA Approved" or "Blocked: [issues]"

Sign-off:
  - Dev Lead: _____________ Date: _______
  - QA Lead: _____________ Date: _______
```

---

## Dependency Management

### Dependency Map Template

```yaml
Project: [Project Name]
Date: [YYYY-MM-DD]

Teams:
  Team A: Design & Architecture
  Team B: Backend Implementation
  Team C: Frontend Implementation
  Team D: QA & Operations

Dependency Graph:
  Team A → Team B (designs, API specs)
  Team A → Team C (UI designs)
  Team B → Team C (backend APIs)
  Team B → Team D (backend code)
  Team C → Team D (frontend code)
  Team D → Production (deployment)

Critical Path:
  Team A (Day 1-3) → Team B (Day 4-10) → Team D (Day 11-13)

Parallel Work:
  Team C (Day 4-10) parallel with Team B
  Both feed into Team D

Risk Areas:
  - Team A delay → cascades to all teams
  - Team B API delay → blocks Team C
  - Team D capacity → bottleneck at end
```

### Dependency Sync Meeting

```yaml
Purpose: Review cross-team dependencies
Frequency: Weekly (or as needed)
Duration: 30 minutes
Attendees: Team Leads + PM

Agenda:
  1. Dependency Status Check (10 min)
     - Each team reports:
       - What we're waiting on
       - What we're providing
       - Any delays

  2. Blocker Review (10 min)
     - Blocked items
     - Required decisions
     - Resource needs

  3. Timeline Adjustment (10 min)
     - Update milestones if needed
     - Communicate changes

Output:
  - Updated dependency status
  - Action items assigned
  - Timeline adjustments documented
```

---

## Conflict Resolution

### Conflict Types

```yaml
Technical Conflict:
  Definition: Disagreement on technical approach
  Resolution: ADR process, Tech Lead decision
  Escalation: CTO if unresolved

Resource Conflict:
  Definition: Multiple teams need same resource
  Resolution: PM prioritization
  Escalation: PO if unresolved

Timeline Conflict:
  Definition: Deadline impossible with current scope
  Resolution: Scope negotiation with PM/PO
  Escalation: Executive if unresolved

Process Conflict:
  Definition: Teams disagree on how to work together
  Resolution: Retrospective, process improvement
  Escalation: CPO if unresolved
```

### Resolution Process

```yaml
Step 1: Direct Discussion
  - Teams discuss directly
  - Document positions
  - Seek consensus

Step 2: Mediation
  - PM/Tech Lead facilitates
  - Evaluate trade-offs
  - Propose compromise

Step 3: Decision Authority
  - Escalate to appropriate authority
  - Present both sides
  - Authority makes final call

Step 4: Document & Implement
  - Document decision (ADR if technical)
  - Communicate to all affected
  - Implement agreed approach
```

---

## Success Metrics

### Collaboration Health Metrics

```yaml
Measure Monthly:
  - Handoff cycle time (hours from ready to accepted)
  - Dependency block rate (% of time blocked on other teams)
  - Cross-team satisfaction (survey)
  - RACI clarity score (can everyone name A for each deliverable?)

Targets:
  - Handoff cycle time: <24 hours (STANDARD+)
  - Dependency block rate: <10% of sprint time
  - Cross-team satisfaction: 4.0+ (out of 5)
  - RACI clarity: 100% (everyone knows who's accountable)
```

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: December 5, 2025
**Owner**: CPO Office

