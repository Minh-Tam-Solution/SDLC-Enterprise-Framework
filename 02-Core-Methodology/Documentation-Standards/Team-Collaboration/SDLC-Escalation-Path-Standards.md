# SDLC Escalation Path Standards

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology (Documentation Standards / Team Collaboration)
**Status**: ACTIVE - Production Standard
**Authority**: CPO Office
**Industry Standards**: ITIL 4, SAFe 6.0

---

## Purpose

Define **standardized escalation paths** for resolving blockers, making decisions, and managing incidents across all SDLC projects.

**Key Principle**: "Ask Before You Guess" - Never self-assume. Follow the escalation path to get decisions from the right authority.

---

## Escalation Levels

### 4-Level Escalation Framework

```yaml
Level 0 - Self-Service:
  What: Information lookup, documentation
  SLA: Immediate
  For:
    - Documentation questions
    - FAQ lookups
    - Previous sprint references
    - Standard procedures
  Action: Check docs, wiki, previous ADRs before escalating

Level 1 - Team Lead / PM:
  What: Design clarifications, task prioritization
  SLA: <4 hours (business hours)
  For:
    - Design clarifications
    - Scope questions
    - Resource allocation
    - Priority decisions
  Action: Ask in team channel, tag Lead/PM

Level 2 - Technical Lead / Architect:
  What: Technical blockers, architecture decisions
  SLA: <4 hours (business hours)
  For:
    - Technical blockers
    - Architecture decisions
    - Integration issues
    - Performance concerns
  Action: Create issue/thread, schedule sync if complex

Level 3 - Executive (CEO/CTO/CPO):
  What: Strategic decisions, budget, major scope changes
  SLA: <8 hours (business hours)
  For:
    - Strategic decisions
    - Budget approvals
    - Major scope changes
    - Cross-project conflicts
  Action: Prepare brief, request decision meeting

Level 4 - External:
  What: Vendor issues, partner coordination, legal
  SLA: <24 hours (or per SLA)
  For:
    - Vendor escalations
    - Partner coordination
    - Legal/compliance issues
    - External dependencies
  Action: PM coordinates with external parties
```

---

## Escalation by Category

### Technical Escalation Path

```yaml
Category: Technical Issue (Code, Architecture, Integration)

Path:
  Self-Service → Tech Lead → Architect → CTO

Level 0 - Self-Service:
  - Check documentation
  - Search codebase
  - Review existing ADRs
  - Check Stack Overflow / internal wiki

Level 1 - Tech Lead:
  - Code-level technical decisions
  - PR review conflicts
  - Testing strategy questions
  - Local environment issues

Level 2 - Architect:
  - Cross-service integration
  - Database design decisions
  - Security architecture
  - Performance optimization

Level 3 - CTO:
  - Technology stack decisions
  - Major architectural changes
  - Build vs buy decisions
  - Technical debt prioritization

Example:
  Issue: "Database query taking 10s, need optimization"
  Path:
    1. Self-service: Check EXPLAIN plan, review indexes
    2. Tech Lead: If unclear, discuss approach
    3. Architect: If major schema change needed
    4. CTO: If requires new technology or budget
```

### Product Escalation Path

```yaml
Category: Product Issue (Requirements, Scope, Priorities)

Path:
  Self-Service → PM/PJM → CPO → CEO

Level 0 - Self-Service:
  - Check requirements document
  - Review user stories
  - Check product roadmap
  - Review previous sprint decisions

Level 1 - PM/PJM:
  - Requirement clarifications
  - User story acceptance criteria
  - Sprint scope adjustments
  - Feature prioritization

Level 2 - CPO:
  - Product strategy questions
  - Major feature decisions
  - UX/UI direction
  - Cross-product conflicts

Level 3 - CEO:
  - Business strategy decisions
  - Market positioning
  - Major pivots
  - Resource allocation (significant)

Example:
  Issue: "Customer requests feature not in roadmap"
  Path:
    1. Self-service: Check if similar feature exists
    2. PM: Assess priority, impact
    3. CPO: If impacts product strategy
    4. CEO: If requires budget/timeline change
```

### Process Escalation Path

```yaml
Category: Process Issue (Workflow, Communication, Collaboration)

Path:
  Self-Service → PJM → PM → CPO

Level 0 - Self-Service:
  - Check process documentation
  - Review team protocols
  - Check SDLC standards

Level 1 - PJM:
  - Sprint process questions
  - Team workflow issues
  - Meeting effectiveness
  - Tool configuration

Level 2 - PM:
  - Cross-team process issues
  - Stakeholder communication
  - Project methodology
  - Vendor process alignment

Level 3 - CPO:
  - SDLC framework decisions
  - Organization-wide process
  - Training and adoption
  - Process exceptions

Example:
  Issue: "Team disagrees on PR review process"
  Path:
    1. Self-service: Check code review standards
    2. PJM: Facilitate team discussion
    3. PM: If cross-team impact
    4. CPO: If SDLC standard change needed
```

### Incident Escalation Path

```yaml
Category: Production Incident

Path:
  On-Call → Incident Commander → CTO → Executive

Severity Definitions:
  P0 - Critical: Service completely down, data breach
  P1 - High: Major feature broken, significant user impact
  P2 - Medium: Feature degraded, workaround exists
  P3 - Low: Minor issue, no immediate impact

Escalation by Severity:

  P0 (Critical):
    SLA: <15 minutes
    Initial: On-Call Engineer
    Escalate to: Incident Commander immediately
    Notify: CTO, Security Lead, PM
    War Room: Yes (mandatory)
    Executive: CEO notified within 1 hour

  P1 (High):
    SLA: <1 hour
    Initial: On-Call Engineer
    Escalate to: Tech Lead within 30 min if unresolved
    Notify: PM, relevant team
    War Room: If needed

  P2 (Medium):
    SLA: <4 hours
    Initial: On-Call Engineer
    Escalate to: Tech Lead if unresolved after 2 hours
    Notify: PM (for visibility)

  P3 (Low):
    SLA: <24 hours
    Initial: On-Call Engineer
    Escalate to: Tech Lead if unresolved by EOD
    Notify: None required

Example:
  Incident: "Production API returning 500 errors"
  Path:
    1. On-Call: Assess severity (P0 if widespread)
    2. Incident Commander: Coordinate response
    3. CTO: If architecture change needed
    4. CEO: If customer communication needed
```

---

## Escalation by Tier

### LITE Tier (1-2 people)

```yaml
Escalation Path:
  Self → Stakeholder

Process:
  - No formal escalation required
  - Direct communication with stakeholder
  - Document decisions in commit messages / README

Example:
  Blocker: "Unclear requirement"
  Action: Message stakeholder directly
```

### STANDARD Tier (3-10 people)

```yaml
Escalation Path:
  Self → Team Lead → PM

Process:
  - Check documentation first (Level 0)
  - Ask Team Lead for most issues (Level 1)
  - Escalate to PM for scope/priority (Level 2)

SLAs:
  - Team Lead: <4 hours
  - PM: <8 hours

Example:
  Blocker: "Two features conflict, unclear priority"
  Action:
    1. Check roadmap (Self)
    2. Ask PM for priority decision (Level 1)
```

### PROFESSIONAL Tier (10-50 people)

```yaml
Escalation Path:
  Self → Lead → Manager → Executive

Process:
  - Full 4-level escalation
  - Document all escalations
  - Use escalation channel (Slack #escalation)

SLAs:
  - Level 1: <4 hours
  - Level 2: <4 hours
  - Level 3: <8 hours

Required Documentation:
  - Issue description
  - Business impact
  - Options considered
  - Recommendation

Example:
  Blocker: "Third-party API deprecated, need replacement"
  Action:
    1. Research alternatives (Self)
    2. Tech Lead for technical options (Level 1)
    3. Architect for architecture impact (Level 2)
    4. CTO for budget approval (Level 3)
```

### ENTERPRISE Tier (50+ people)

```yaml
Escalation Path:
  Self → Lead → Manager → Director → Executive

Process:
  - 5-level escalation for major issues
  - Formal escalation request form
  - Tracking in ticketing system
  - SLA monitoring and reporting

SLAs (Strict):
  - Level 1: <2 hours
  - Level 2: <4 hours
  - Level 3: <8 hours
  - Level 4: <24 hours

Required Documentation:
  - Escalation form completed
  - Impact assessment
  - Root cause (if known)
  - Proposed resolution
  - Decision required

Escalation Form Fields:
  - Escalation ID
  - Requester
  - Date/Time
  - Category (Technical/Product/Process/Incident)
  - Severity (P0-P3)
  - Description
  - Business Impact
  - Options Considered
  - Recommendation
  - Decision Needed By
```

---

## Escalation Request Template

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

---

### Resolution (To be filled by escalation target)

**Decision**: [Decision made]
**Rationale**: [Why this decision]
**Next Steps**: [Action items]
**Resolved By**: [Name]
**Resolution Date**: [YYYY-MM-DD]
```

---

## Escalation Anti-Patterns

### What NOT to Do

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

Anti-Pattern 6: No Follow-Up
  ❌ Escalate and forget
  ✅ Track resolution, confirm closure
```

---

## Escalation Metrics

### Track Monthly

```yaml
Metrics:
  - Total escalations by level
  - Average resolution time per level
  - Escalation causes (category breakdown)
  - SLA compliance rate
  - Repeat escalations (same issue)

Targets:
  - SLA compliance: >95%
  - Repeat escalations: <5%
  - Level 3+ escalations: <10% of total

Review:
  - Monthly escalation review meeting
  - Identify patterns
  - Improve processes to reduce escalations
```

---

## Quick Reference Card

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
  Level 2: Tech Lead / Architect / Manager | <4 hours
  Level 3: CTO / CPO / Executive          | <8 hours
  Level 4: External / Vendor              | <24 hours

INCIDENT SEVERITY:
  P0: Service down, data breach           | <15 min
  P1: Major feature broken                | <1 hour
  P2: Feature degraded                    | <4 hours
  P3: Minor issue                         | <24 hours

CHANNELS:
  Technical: #escalation-tech
  Product: #escalation-product
  Incident: #incident-response

REMEMBER:
  "Ask Before You Guess"
  Follow the path, don't skip levels
  Document everything
```

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: December 5, 2025
**Owner**: CPO Office

