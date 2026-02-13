# SDLC Team Collaboration Standards - Universal Framework

**Version**: 6.0.5
**Date**: January 28, 2026
**Status**: ACTIVE - Production Standard
**Authority**: CPO Office
**Pillar**: 2 - Sprint Planning Governance × Pillar 6 - Documentation Permanence
**Stage**: 02 - Core Methodology (Documentation Standards)
**Industry Standards**: Team Topologies, SAFe 6.0, ITIL 4, DORA
**AI Governance**: Aligned with 03-AI-GOVERNANCE principles (Human Accountability, CRP Escalation)

---

## Table of Contents

1. [Part 1: Overview & Core Principles](#part-1-overview--core-principles)
2. [Part 2: Team Structure Framework](#part-2-team-structure-framework)
3. [Part 3: Communication Standards by Tier](#part-3-communication-standards-by-tier)
4. [Part 4: RACI Matrix & Handoff Protocols](#part-4-raci-matrix--handoff-protocols)
5. [Part 5: Escalation Framework](#part-5-escalation-framework)
6. [Part 6: Meeting Standards](#part-6-meeting-standards)
7. [Part 7: Conflict Resolution & Metrics](#part-7-conflict-resolution--metrics)
8. [Part 8: Quick Reference](#part-8-quick-reference)

---

## Part 1: Overview & Core Principles

### Purpose

Define **team collaboration standards** for multi-team coordination across distributed, hybrid, and co-located teams. These standards are **methodology-agnostic** - they work regardless of team location or structure.

This document consolidates:
- Team Structure Framework (roles, types, governance)
- Communication Standards (tiered requirements)
- RACI Matrix & Handoff Protocols
- Escalation Path Standards (4-level framework)

### Core Principles

```yaml
Principle 1: Teams, Not Locations
  Old Thinking (Wrong):
    - "Remote Team" vs "Local Team"
    - Location-based protocols
    - Timezone as primary concern

  New Thinking (Correct):
    - Team A, Team B, Team C...
    - Function-based protocols
    - Deliverables as primary concern
    - Location = implementation detail

Principle 2: Explicit Handoffs
  Every team-to-team interaction needs:
    1. Clear trigger (when does handoff happen?)
    2. Acceptance criteria (DoD for handoff)
    3. Documentation requirements
    4. Feedback loop (how to request changes?)

Principle 3: Escalation Before Assumption
  Rule: "Ask Before You Guess"
    - When unclear → Ask immediately
    - Never self-assume business logic
    - Follow escalation path (Level 0 → Level 3)
    - Document decisions made

Principle 4: RACI Clarity
  For every deliverable:
    R - Responsible: Who does the work?
    A - Accountable: Who approves?
    C - Consulted: Who provides input?
    I - Informed: Who needs updates?
```

### Consolidation Note

This document merges four previous standards from Team-Collaboration/:
- SDLC-Team-Collaboration-Protocol.md → Parts 2, 4
- SDLC-Team-Communication-Protocol.md → Parts 3, 6
- SDLC-Escalation-Path-Standards.md → Part 5
- README.md → Part 1

---

## Part 2: Team Structure Framework

### 2.1 Governance Roles

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

### 2.2 Governance by Tier

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

### 2.3 Team Types (Team Topologies)

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

### 2.4 Team Definition Template

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

### 2.5 Example: 3-Team Product Setup

```yaml
Team A - Design & Architecture:
  Type: Enabling (design) + Stream-aligned (architecture)
  Role: Create designs, define API contracts, architectural decisions
  Members: 3 (Architect, 2 Designers)
  Deliverables: ADRs, UI/UX designs (Figma), API contracts (OpenAPI)
  Dependencies:
    Upstream: None (starting point)
    Downstream: Team B (receives designs)
  Sync: Daily 9AM, Wed 3PM with Team B

Team B - Implementation:
  Type: Stream-aligned
  Role: Build features based on designs
  Members: 5 (2 Backend, 2 Frontend, 1 DevOps)
  Deliverables: Working code, tests, documentation
  Dependencies:
    Upstream: Team A (receives designs)
    Downstream: Team C (provides code)
  Sync: Daily 10AM, Wed 3PM with A, Fri 2PM with C

Team C - QA & Operations:
  Type: Stream-aligned (QA) + Platform (Ops)
  Role: Test, deploy, and operate the system
  Members: 3 (QA Lead, SRE, DevOps)
  Deliverables: Test reports, runbooks, alerts
  Dependencies:
    Upstream: Team B (receives code)
    Downstream: Production
  Sync: Daily 11AM, Fri 2PM with Team B
```

---

## Part 3: Communication Standards by Tier

### 3.1 LITE Tier (1-2 people)

```yaml
Synchronous:
  - No formal meetings required
  - Ad-hoc calls as needed

Asynchronous:
  - Slack/Discord (preferred)
  - Email for external stakeholders
  - GitHub/GitLab for code discussions

Documentation:
  - Commit messages describe changes
  - README updates for major changes

Escalation:
  - Self-service (docs, wikis)
  - Direct to stakeholder if blocked
```

### 3.2 STANDARD Tier (3-10 people)

```yaml
Synchronous:
  - Daily async updates (Slack standup bot)
  - Weekly sync meeting (30 min max)
  - Sprint planning/retro (bi-weekly)

Asynchronous:
  - Slack channels organized:
    - #general (announcements)
    - #dev (technical discussions)
    - #questions (blockers, clarifications)
  - PR descriptions include:
    - What changed
    - Why it changed
    - How to test
    - Rollback plan

Documentation:
  - CLAUDE.md for AI onboarding
  - /docs/README.md as entry point
  - 3-5 key documents maintained

Response SLAs:
  - Team members: <4 hours (business hours)
  - PM/Lead: <4 hours
  - Blocking issues: <2 hours
```

### 3.3 PROFESSIONAL Tier (10-50 people)

```yaml
Synchronous:
  - Daily standup (15 min, time-boxed)
  - Weekly planning (1 hour)
  - Sprint retrospective
  - Cross-team sync (as needed)

Asynchronous:
  - Slack channels per team:
    - #team-{name} (internal)
    - #team-{name}-external (cross-team)
    - #sprint-{number}-questions
  - Structured PR reviews:
    - 2+ reviewers required
    - Review SLA: 24 hours
    - Use PR templates

Documentation:
  - Full /docs structure (10 stages)
  - ADRs for architectural decisions
  - Team protocol documented
  - SSOT document references

Response SLAs:
  - Team members: <4 hours
  - Tech Lead: <4 hours
  - PM/PJM: <4 hours
  - CTO/CPO: <8 hours
  - External: <24 hours

Meeting Cadence:
  | Meeting | Frequency | Duration | Attendees |
  |---------|-----------|----------|-----------|
  | Daily Standup | Daily | 15 min | Team |
  | Planning | Weekly | 1 hour | Team + PM |
  | Retro | Bi-weekly | 1 hour | Team |
  | Cross-team Sync | Weekly | 30 min | Leads |
  | Steering | Bi-weekly | 1 hour | PM + PO |
```

### 3.4 ENTERPRISE Tier (50+ people)

```yaml
Synchronous:
  - Multiple team standups (per team)
  - Cross-team sync (weekly)
  - Program Increment Planning (SAFe-inspired)
  - Town halls (monthly)

Asynchronous:
  - Slack workspace structure:
    - Team channels (private)
    - Program channels (cross-team)
    - Announcement channels (broadcast)
    - Incident channels (on-demand)
  - Formal processes:
    - RFC process for major decisions
    - ADR templates mandatory
    - Escalation documented

Response SLAs (Strict):
  - P0 (Critical): <15 minutes
  - P1 (High): <1 hour
  - P2 (Medium): <4 hours
  - P3 (Low): <24 hours
  - External: SLA per contract

Meeting Hierarchy:
  | Level | Meeting | Frequency | Attendees |
  |-------|---------|-----------|-----------|
  | Team | Standup | Daily | Team members |
  | Team | Planning | Weekly | Team + Lead |
  | Program | Sync | Weekly | All Leads |
  | Program | PI Planning | Quarterly | All teams |
  | Executive | Steering | Bi-weekly | PM + PO + Exec |
  | Executive | Town Hall | Monthly | All |
```

### 3.5 Channel Naming Convention

```yaml
Format: #{scope}-{purpose}[-{qualifier}]

Examples:
  #team-backend           (team internal)
  #team-backend-external  (team external communication)
  #sprint-28-questions    (sprint-specific)
  #escalation             (cross-team escalation)
  #incident-2025-12-05    (dated incident channel)
  #release-v5             (release coordination)
```

---

## Part 4: RACI Matrix & Handoff Protocols

### 4.1 RACI Definitions

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

### 4.2 RACI Matrix Template

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

### 4.3 Handoff Protocol Template

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

### 4.4 Handoff Example: Design → Implementation

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

Process:
  1. Design team posts in #handoff: "Design ready for [Feature X]"
  2. Implementation team has 24 hours to review
  3. Questions posted in #handoff thread
  4. Design team clarifies within 4 hours
  5. If major changes needed → Schedule sync meeting
  6. Implementation team replies: "Accepted" or "Changes needed"
  7. Handoff complete when Implementation says "Handoff accepted"
```

### 4.5 Dependency Management

```yaml
Dependency Map Template:
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

  Risk Areas:
    - Team A delay → cascades to all teams
    - Team B API delay → blocks Team C
    - Team D capacity → bottleneck at end
```

---

## Part 5: Escalation Framework

### 5.1 4-Level Escalation Framework

```yaml
Level 0 - Self-Service:
  What: Information lookup, documentation
  SLA: Immediate
  For: Documentation questions, FAQ lookups, previous sprint references
  Action: Check docs, wiki, previous ADRs before escalating

Level 1 - Team Lead / PM:
  What: Design clarifications, task prioritization
  SLA: <4 hours (business hours)
  For: Design clarifications, scope questions, resource allocation
  Action: Ask in team channel, tag Lead/PM

Level 2 - Technical Lead / Architect:
  What: Technical blockers, architecture decisions
  SLA: <4 hours (business hours)
  For: Technical blockers, architecture decisions, integration issues
  Action: Create issue/thread, schedule sync if complex

Level 3 - Executive (CEO/CTO/CPO):
  What: Strategic decisions, budget, major scope changes
  SLA: <8 hours (business hours)
  For: Strategic decisions, budget approvals, major scope changes
  Action: Prepare brief, request decision meeting

Level 4 - External:
  What: Vendor issues, partner coordination, legal
  SLA: <24 hours (or per SLA)
  For: Vendor escalations, partner coordination, legal/compliance
  Action: PM coordinates with external parties
```

### 5.2 Escalation by Category

#### Technical Escalation
```yaml
Path: Self-Service → Tech Lead → Architect → CTO

Level 0: Check documentation, search codebase, review ADRs
Level 1: Code-level decisions, PR conflicts, testing strategy
Level 2: Cross-service integration, database design, security
Level 3: Technology stack decisions, major architectural changes
```

#### Product Escalation
```yaml
Path: Self-Service → PM/PJM → CPO → CEO

Level 0: Check requirements document, review user stories
Level 1: Requirement clarifications, sprint scope adjustments
Level 2: Product strategy, major feature decisions
Level 3: Business strategy, major pivots
```

#### Incident Escalation
```yaml
Severity Definitions:
  P0 - Critical: Service completely down, data breach (<15 min)
  P1 - High: Major feature broken, significant impact (<1 hour)
  P2 - Medium: Feature degraded, workaround exists (<4 hours)
  P3 - Low: Minor issue, no immediate impact (<24 hours)

P0 Response:
  Initial: On-Call Engineer
  Escalate to: Incident Commander immediately
  Notify: CTO, Security Lead, PM
  War Room: Yes (mandatory)
  Executive: CEO notified within 1 hour
```

### 5.3 Escalation by Tier

```yaml
LITE (1-2 people):
  Path: Self → Stakeholder
  Process: No formal escalation, direct communication

STANDARD (3-10 people):
  Path: Self → Team Lead → PM
  SLAs: Lead <4h, PM <8h

PROFESSIONAL (10-50 people):
  Path: Self → Lead → Manager → Executive
  SLAs: L1 <4h, L2 <4h, L3 <8h
  Required: Document all escalations

ENTERPRISE (50+ people):
  Path: Self → Lead → Manager → Director → Executive
  SLAs: L1 <2h, L2 <4h, L3 <8h, L4 <24h
  Required: Formal escalation form, ticketing system
```

### 5.4 Escalation Request Template

```markdown
## Escalation Request

**ID**: ESC-YYYY-MM-DD-###
**Date**: [YYYY-MM-DD HH:MM]
**Requester**: [Name, Team]
**Category**: Technical | Product | Process | Incident
**Severity**: P0 | P1 | P2 | P3
**Current Level**: Level [X]
**Escalating To**: Level [Y]

### Issue Description
[Clear, concise description of the issue]

### Business Impact
- Who is affected?
- What is the impact (revenue, users, timeline)?
- How urgent is resolution?

### Steps Already Taken
1. [What you tried at Level 0]
2. [What you tried at Level 1]
3. [Why escalation is needed]

### Options Considered
| Option | Pros | Cons | Effort |
|--------|------|------|--------|
| A | | | |
| B | | | |

### Recommendation
[Your recommended option and rationale]

### Decision Needed
[Specific decision you need from escalation target]

### Decision Deadline
[When decision is needed by]
```

### 5.5 Escalation Anti-Patterns

```yaml
Anti-Pattern 1: Skip Levels
  ❌ Go directly to CEO for technical question
  ✅ Follow escalation path (Self → Lead → Manager → Executive)

Anti-Pattern 2: No Documentation
  ❌ Verbal escalation only
  ✅ Document in channel/ticket, track resolution

Anti-Pattern 3: Premature Escalation
  ❌ Escalate before trying to solve
  ✅ Complete Level 0 (self-service) first

Anti-Pattern 4: Escalation Avoidance
  ❌ Wait too long, miss deadlines
  ✅ Escalate when SLA at risk

Anti-Pattern 5: Unclear Ask
  ❌ "I need help"
  ✅ "I need decision on X by Y because Z"
```

---

## Part 6: Meeting Standards

### 6.1 Standup Format (15 min)

```yaml
Format: Round-robin, time-boxed

Each Person (2 min max):
  1. What I completed yesterday
  2. What I'm working on today
  3. Any blockers

Parking Lot:
  - Discussions needing more time → schedule separately
  - Don't solve problems in standup

Remote/Hybrid:
  - Video ON (preferred for engagement)
  - Use async standup bot if timezone issues
  - Record key decisions in channel
```

### 6.2 Planning Meeting (1 hour)

```yaml
Agenda:
  1. Sprint Review (15 min)
     - What got done vs planned
     - Demo completed work

  2. Retrospective (15 min)
     - What went well
     - What to improve
     - Action items

  3. Sprint Planning (30 min)
     - Review backlog
     - Estimate stories
     - Commit to sprint scope

Output:
  - Sprint backlog committed
  - Action items assigned
  - Risks identified
```

### 6.3 Cross-Team Sync (30 min)

```yaml
Agenda:
  1. Dependency Check (10 min)
     - Upstream blockers
     - Downstream impacts

  2. Integration Status (10 min)
     - API contracts
     - Shared components
     - Timeline alignment

  3. Escalations (10 min)
     - Blocked items
     - Resource needs
     - Decision requests

Attendees:
  - Team Leads (required)
  - PM/PJM (required)
  - Tech Lead (as needed)
```

### 6.4 Remote/Distributed Considerations

```yaml
Timezone Management:
  1. Find overlap hours (minimum 2-4 hours)
  2. Rotate meeting times fairly
  3. Record all sync meetings
  4. Async-first for non-urgent items

Async Best Practices:
  ✅ Context first: "Regarding the auth API..."
  ✅ Specific ask: "I need X by Y"
  ✅ Deadline stated: "Please respond by EOD Friday"
  ✅ Thread replies: Keep discussions organized
  ✅ Summarize decisions: "Decision: We'll use X because Y"
```

---

## Part 7: Conflict Resolution & Metrics

### 7.1 Conflict Types & Resolution

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

### 7.2 Resolution Process

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

### 7.3 Collaboration Health Metrics

```yaml
Measure Monthly:
  - Handoff cycle time (hours from ready to accepted)
  - Dependency block rate (% of time blocked on other teams)
  - Cross-team satisfaction (survey)
  - RACI clarity score (can everyone name A for each deliverable?)
  - Response time (average, p95)
  - SLA compliance rate

Targets:
  - Handoff cycle time: <24 hours (STANDARD+)
  - Dependency block rate: <10% of sprint time
  - Cross-team satisfaction: 4.0+ (out of 5)
  - RACI clarity: 100%
  - SLA compliance: 95%+ (PROFESSIONAL), 99%+ (ENTERPRISE)
```

### 7.4 Escalation Metrics

```yaml
Track Monthly:
  - Total escalations by level
  - Average resolution time per level
  - Escalation causes (category breakdown)
  - Repeat escalations (same issue)

Targets:
  - SLA compliance: >95%
  - Repeat escalations: <5%
  - Level 3+ escalations: <10% of total
```

---

## Part 8: Quick Reference

### Quick Start by Tier

| Tier | Team Size | Key Requirements |
|------|-----------|-----------------|
| LITE | 1-2 | Basic async communication |
| STANDARD | 3-10 | Daily updates, weekly sync, basic escalation |
| PROFESSIONAL | 10-50 | Full RACI, handoff protocols, 4-level escalation |
| ENTERPRISE | 50+ | CAB, SLAs <4h, multiple team types |

### RACI Quick Reference

| Letter | Meaning | Count | Example |
|--------|---------|-------|---------|
| R | Responsible (does work) | 1+ | Developer writes code |
| A | Accountable (approves) | Exactly 1 | Tech Lead approves PR |
| C | Consulted (input before) | 0+ | Architect advises on design |
| I | Informed (notified after) | 0+ | PM gets status update |

### Escalation Quick Card

```markdown
📋 ESCALATION QUICK REFERENCE

BEFORE ESCALATING:
✅ Checked documentation? (Level 0)
✅ Tried to solve yourself?
✅ Clear description ready?
✅ Impact assessed?

ESCALATION LEVELS:
  Level 0: Self-service (docs, wiki)      | Immediate
  Level 1: Team Lead / PM                 | <4 hours
  Level 2: Tech Lead / Architect          | <4 hours
  Level 3: CTO / CPO / Executive          | <8 hours
  Level 4: External / Vendor              | <24 hours

INCIDENT SEVERITY:
  P0: Service down, data breach           | <15 min
  P1: Major feature broken                | <1 hour
  P2: Feature degraded                    | <4 hours
  P3: Minor issue                         | <24 hours

REMEMBER:
  "Ask Before You Guess"
  Follow the path, don't skip levels
  Document everything
```

### Communication Anti-Patterns

```yaml
Over-Meeting:
  ❌ 5+ hours of meetings per day
  ✅ Max 2-3 hours, rest is deep work

Information Silos:
  ❌ Knowledge in private DMs only
  ✅ Share in public channels, document decisions

Async for Urgent:
  ❌ Slack message for production outage
  ✅ Phone call / PagerDuty for P0

No Documentation:
  ❌ "We discussed this in the call"
  ✅ "Decision documented in #decisions channel"
```

---

## Sprint Governance Integration (Pillar 2)

### Sprint-Level Collaboration

Per **Pillar 2: Sprint Planning Governance**:

| Sprint Event | Collaboration Protocol | Document Output |
|--------------|----------------------|-----------------|
| Sprint Planning | All teams attend, scope negotiation | Sprint Plan with RACI |
| Daily Standup | Per-team async + cross-team sync | Progress logs |
| Sprint Review | Demo to stakeholders | Review minutes |
| Sprint Retrospective | Intra-team reflection | Retro action items |

### Sprint Escalation Path

| Sprint Blocker Type | Escalation Level | SLA | Action |
|---------------------|-----------------|-----|--------|
| Scope clarification | L1 - PM | <2h | Tag PM in sprint channel |
| Cross-team dependency | L2 - Tech Lead | <4h | Create cross-team issue |
| Sprint scope change | L3 - PO | <4h | Request scope change approval |
| Sprint cancellation | L3 - Executive | <8h | Emergency steering meeting |

---

## Industry Standards Alignment

| Standard | Integration Point |
|----------|------------------|
| **Team Topologies** | 4 team types (Stream-aligned, Platform, Enabling, Complicated-Subsystem) |
| **SAFe 6.0** | Lean governance, PI Planning concepts |
| **DORA Metrics** | Team performance measurement |
| **ITIL 4** | Escalation and incident management |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 6.0.0 | Jan 28, 2026 | Folder flattening (remove layer 3), version upgrade |
| 5.3.0 | Jan 28, 2026 | Consolidated from 4 files (Collaboration, Communication, Escalation, README) |
| 5.2.0 | Jan 22, 2026 | Added AI Governance alignment |
| 5.0.0 | Dec 5, 2025 | Initial SDLC 5.0.0 version |

---

## Related Documents

- [SDLC-Sprint-Governance.md](../Governance-Compliance/SDLC-Sprint-Governance.md) - Sprint Planning Governance
- [When-Planning-Sprint.md](./Situation-Specific-Guides/When-Planning-Sprint.md) - Sprint planning checklist
- [SDLC-Core-Methodology.md](../SDLC-Core-Methodology.md) - 8-Pillar Architecture
- [03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) - AI Governance principles

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: January 28, 2026
**Owner**: CPO Office

---

*"Teams, not locations. Deliverables, not timezones."* 🤝
