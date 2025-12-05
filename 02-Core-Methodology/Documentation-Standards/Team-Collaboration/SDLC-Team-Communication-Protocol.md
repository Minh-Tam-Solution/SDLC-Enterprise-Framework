# SDLC Team Communication Protocol

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology (Documentation Standards / Team Collaboration)
**Status**: ACTIVE - Production Standard
**Authority**: CPO Office
**Industry Standards**: Team Topologies, SAFe 6.0, DORA

---

## Purpose

Define **tiered communication standards** for SDLC projects across all team structures:
- Co-located teams
- Remote/distributed teams
- Hybrid teams
- Multi-timezone teams

**Key Principle**: Communication requirements scale with team size and project complexity.

---

## Communication Requirements by Tier

### LITE Tier (1-2 people)

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

### STANDARD Tier (3-10 people)

```yaml
Synchronous:
  - Daily async updates (Slack standup bot)
  - Weekly sync meeting (30 min max)
  - Sprint planning/retro (bi-weekly)

Asynchronous:
  - Slack channels organized by function:
    - #general (announcements)
    - #dev (technical discussions)
    - #questions (blockers, clarifications)
  - PR descriptions include:
    - What changed
    - Why it changed
    - How to test
    - Rollback plan (for significant changes)

Documentation:
  - CLAUDE.md for AI onboarding
  - /docs/README.md as entry point
  - 3-5 key documents maintained

Response SLAs:
  - Team members: <4 hours (business hours)
  - PM/Lead: <4 hours
  - Blocking issues: <2 hours
```

### PROFESSIONAL Tier (10-50 people)

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
    - #sprint-{number}-questions (sprint-specific)
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

### ENTERPRISE Tier (50+ people)

```yaml
Synchronous:
  - Multiple team standups (per team)
  - Cross-team sync (weekly)
  - Program Increment (PI) Planning (SAFe-inspired)
  - Town halls (monthly)

Asynchronous:
  - Slack workspace structure:
    - Team channels (private)
    - Program channels (cross-team)
    - Announcement channels (broadcast)
    - Incident channels (on-demand)
  - Formal communication protocols:
    - RFC process for major decisions
    - ADR templates mandatory
    - Escalation documented

Documentation:
  - Everything in PROFESSIONAL
  - Weekly executive reports (CTO/CPO)
  - Gate reviews documented
  - Compliance evidence collected

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

---

## Communication Channels Matrix

### Channel Types

```yaml
Internal Team:
  Purpose: Day-to-day team discussion
  Access: Team members only
  Example: #team-backend, #team-frontend

Cross-Team:
  Purpose: Inter-team coordination
  Access: Multiple teams
  Example: #handoff, #integration, #api-sync

Sprint-Specific:
  Purpose: Sprint questions and blockers
  Access: All sprint participants
  Example: #sprint-28-questions
  Lifecycle: Archive after sprint

Escalation:
  Purpose: Blocked items requiring attention
  Access: Leads + PM
  Example: #escalation, #blockers

Incident:
  Purpose: Production issues
  Access: On-call + relevant teams
  Example: #incident-{date}, #sev1-response
```

### Channel Naming Convention

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

## Meeting Standards

### Standup Format (15 min)

```yaml
Format: Round-robin, time-boxed

Each Person (2 min max):
  1. What I completed yesterday
  2. What I'm working on today
  3. Any blockers

Parking Lot:
  - Discussions that need more time → schedule separately
  - Don't solve problems in standup

Remote/Hybrid:
  - Video ON (preferred for engagement)
  - Use async standup bot if timezone issues
  - Record key decisions in channel
```

### Planning Meeting (1 hour)

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

### Cross-Team Sync (30 min)

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

---

## Remote/Distributed Team Considerations

### Timezone Management

```yaml
Golden Rules:
  1. Find overlap hours (minimum 2-4 hours)
  2. Rotate meeting times fairly
  3. Record all sync meetings
  4. Async-first for non-urgent items

Example (PST + IST teams):
  Overlap: 6-10 AM PST / 7:30-11:30 PM IST
  Sync meetings: 8 AM PST (9:30 PM IST)
  Async updates: Anytime via Slack
```

### Async Communication Best Practices

```yaml
Writing Clear Messages:
  ✅ Context first: "Regarding the auth API..."
  ✅ Specific ask: "I need X by Y"
  ✅ Deadline stated: "Please respond by EOD Friday"
  ✅ Visual aids: Screenshots, diagrams

Responding:
  ✅ Acknowledge receipt: "Saw this, will respond by..."
  ✅ Thread replies: Keep discussions organized
  ✅ Summarize decisions: "Decision: We'll use X because Y"
  ✅ Update status: "Done ✅" or "Blocked, see thread"
```

### Tools for Distributed Teams

```yaml
Required:
  - Slack/Teams: Real-time communication
  - GitHub/GitLab: Code collaboration
  - Zoom/Meet: Video meetings
  - Loom/Screen recordings: Async demos

Recommended:
  - Miro/FigJam: Collaborative whiteboards
  - Notion/Confluence: Documentation
  - Standup bots: Geekbot, Standup Alice
  - Time zone tools: World Time Buddy
```

---

## Decision Documentation

### When to Document Decisions

```yaml
Always Document:
  - Architectural decisions (ADR format)
  - API contract changes
  - Process changes
  - Security decisions
  - Scope changes

Document Format:
  - Decision: What was decided
  - Context: Why this decision was needed
  - Options Considered: What alternatives existed
  - Rationale: Why this option was chosen
  - Consequences: What changes as a result
  - Date + Participants: Who was involved
```

### Decision Log Template

```markdown
## Decision: [Title]

**Date**: YYYY-MM-DD
**Participants**: [Names]
**Status**: Proposed | Accepted | Superseded

### Context
[Why this decision is needed]

### Decision
[What was decided]

### Consequences
[What changes as a result]

### Alternatives Considered
1. [Option A]: [Why rejected]
2. [Option B]: [Why rejected]
```

---

## Communication Anti-Patterns

### What NOT to Do

```yaml
Anti-Pattern 1: Over-Meeting
  ❌ 5+ hours of meetings per day
  ✅ Max 2-3 hours, rest is deep work

Anti-Pattern 2: Information Silos
  ❌ Knowledge in private DMs only
  ✅ Share in public channels, document decisions

Anti-Pattern 3: Async for Urgent
  ❌ Slack message for production outage
  ✅ Phone call / PagerDuty for P0

Anti-Pattern 4: Meeting for Everything
  ❌ Schedule meeting to share status
  ✅ Write status update, meet only if discussion needed

Anti-Pattern 5: No Documentation
  ❌ "We discussed this in the call"
  ✅ "Decision documented in #decisions channel"
```

---

## Metrics & Success Criteria

### Communication Health Metrics

```yaml
Measure Monthly:
  - Response time (average, p95)
  - Meeting efficiency (outcomes per meeting)
  - Decision documentation rate
  - Information findability (<1 min to find answer)

Targets:
  LITE: N/A (informal)
  STANDARD: 90% SLA compliance
  PROFESSIONAL: 95% SLA compliance
  ENTERPRISE: 99% SLA compliance
```

### Team Satisfaction Survey (Quarterly)

```yaml
Questions:
  1. "I can find information I need easily" (1-5)
  2. "Meetings are productive" (1-5)
  3. "Communication blockers are resolved quickly" (1-5)
  4. "I understand what other teams are working on" (1-5)

Target: Average 4.0+ across all questions
```

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for all SDLC projects (scaled by tier)
**Last Updated**: December 5, 2025
**Owner**: CPO Office

