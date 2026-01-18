# When Planning a Sprint

**Version**: 5.1.3
**Date**: January 18, 2026
**Type**: Situation-Specific Guide
**Status**: ACTIVE
**Authority**: CTO Office

---

## Overview

This guide provides a step-by-step process for planning a new sprint in compliance with SDLC 5.1.3 Sprint Planning Governance.

**When to use this guide**:
- Starting a new sprint
- Transitioning from one sprint to another
- Setting up sprint governance for a new project

**Prerequisites**:
- Familiarity with [SDLC-Sprint-Planning-Governance.md](../Governance-Compliance/SDLC-Sprint-Planning-Governance.md)
- Access to [SPRINT-TEMPLATE.md](../../03-Templates-Tools/5-Project-Templates/PLANNING-HIERARCHY-TEMPLATE/SPRINT-TEMPLATE.md)

---

## Pre-Sprint Checklist

### 1. Verify Previous Sprint Closed ✅

Before planning a new sprint, ensure the previous sprint is properly closed:

```yaml
□ G-Sprint-Close gate passed
□ CURRENT-SPRINT.md updated (status: COMPLETED)
□ SPRINT-INDEX.md updated (entry added)
□ Sprint retro documented
□ Metrics captured (velocity, completion rate)
□ Carryover items identified and documented
```

**If previous sprint not closed**: STOP. Complete G-Sprint-Close first.

### 2. Review Roadmap Alignment ✅

```yaml
□ Check current Phase objective
□ Identify roadmap goal this sprint supports
□ Verify sprint number is correct (next sequential)
□ Run SSOT validation script (if available)
□ Confirm no conflicting sprint references
```

**Traceability Check**:
```
Roadmap Goal: [What strategic goal?]
└── Phase Objective: [What phase objective?]
    └── Sprint Goal: [What will this sprint achieve?]
```

### 3. Capacity Planning ✅

```yaml
□ Calculate team availability
    - Total working days
    - Subtract PTO, holidays, meetings
    - Account for on-call duties

□ Review historical velocity
    - Last 3 sprints average
    - Adjust for team changes

□ Set sprint capacity
    - Story points = velocity × availability factor
    - Leave 10-20% buffer for unknowns
```

**Capacity Formula**:
```
Sprint Capacity = Historical Velocity × (Available Days / Standard Sprint Days)
```

### 4. Backlog Refinement ✅

```yaml
□ Review and prioritize backlog items
    - P0: Must have (required for sprint goal)
    - P1: Should have (high value, fits capacity)
    - P2: Could have (nice to have)

□ Ensure items are sprint-ready
    - Acceptance criteria defined
    - Story points estimated
    - Dependencies identified

□ Identify carryover items from previous sprint
    - Re-prioritize as needed
    - Update estimates if scope changed
```

### 5. Draft Sprint Plan ✅

Create `SPRINT-XX.md` using the template:

```yaml
□ Sprint number (sequential)
□ Sprint goal (single sentence)
□ Start and end dates
□ Committed work (user stories, tasks, bugs)
□ Sprint events scheduled
□ Dependencies listed
□ Risks identified
□ Definition of Done agreed
```

---

## G-Sprint Gate Evaluation

### Checklist

Before sprint kickoff, evaluate G-Sprint gate:

```yaml
Alignment:
  □ Sprint goal aligns with Phase objective
  □ Sprint goal aligns with Roadmap goal
  □ Priorities explicit (P0/P1/P2 labeled)
  □ No "options" for P0 items

Capacity:
  □ Team capacity calculated correctly
  □ Story points within velocity (+10% max)
  □ Key personnel availability confirmed
  □ PTO/holidays accounted for

Dependencies:
  □ External dependencies identified
  □ Blocker mitigation planned
  □ Cross-team coordination scheduled

Risk:
  □ Top 3 risks identified
  □ Mitigation strategies defined
  □ Escalation path clear

Documentation:
  □ SPRINT-XX.md created
  □ SPRINT-XX.md committed to repo
  □ Definition of Done documented
  □ Sprint events in calendar
```

### Approval

| Tier | Approver | Method |
|------|----------|--------|
| LITE | Self | Commit to repo |
| STANDARD | Tech Lead | PR approval or Slack ack |
| PROFESSIONAL | CTO or PM | Meeting + document sign-off |
| ENTERPRISE | CPO + CTO | Formal meeting |

---

## During Sprint

### Daily Activities

```yaml
Daily Standup (15 min):
  - What did I complete yesterday?
  - What will I work on today?
  - Any blockers?

Progress Tracking:
  - Update task status daily
  - Move items across board (Todo → In Progress → Done)
  - Flag blockers immediately

Sprint Document Updates:
  - Update Daily Progress section in SPRINT-XX.md
  - Record blockers and resolutions
```

### Blocker Escalation

```yaml
Level 1 (Team, <4h):
  - Discuss in standup
  - Pair with teammate
  - Check documentation

Level 2 (Lead, 4-24h):
  - Escalate to Tech Lead
  - Request unblocking assistance
  - Adjust sprint scope if needed

Level 3 (CTO, >24h):
  - Escalate to CTO/PM
  - May trigger scope change
  - Document in risk log
```

### Mid-Sprint Check (Day 5 of 10-day sprint)

```yaml
□ Progress on track? (50% complete)
□ Any scope creep?
□ Blockers resolved or escalated?
□ Still aligned with sprint goal?
□ Any risks materialized?
```

---

## Post-Sprint Checklist

### Within 24 Business Hours

```yaml
Sprint Completion:
  □ All committed work Done or Carried Over
  □ No silent drops (all items accounted for)
  □ Quality checks passed

Sprint Review:
  □ Demo to stakeholders
  □ Feedback captured
  □ Acceptance confirmed

Sprint Retrospective:
  □ What went well?
  □ What could improve?
  □ Action items assigned

Documentation (MANDATORY):
  □ Update CURRENT-SPRINT.md
      - Status: COMPLETED
      - Final metrics
  □ Update SPRINT-INDEX.md
      - Add completed sprint entry
  □ Review Roadmap
      - Update if needed
  □ Update CHANGELOG.md
      - If release shipped
```

### G-Sprint-Close Evaluation

```yaml
Work:
  □ All items accounted for (done/carryover)
  □ Carryover documented with reason
  □ No P0 items dropped

Quality:
  □ Definition of Done met
  □ No P0 bugs shipped
  □ Test coverage maintained

Retrospective:
  □ Retro completed
  □ Action items assigned
  □ Improvements documented

Metrics:
  □ Velocity calculated
  □ Completion rate recorded
  □ Bug escape rate recorded

Documentation:
  □ All docs updated within 24h
  □ SSOT validation passed
```

---

## Common Pitfalls

### 1. Direction Confusion

**Symptom**: Team unclear on what to build

**Prevention**:
- Single, clear sprint goal
- P0 priorities explicit (not "options")
- Sprint goal traces to roadmap

**Fix**:
- Stop and clarify with CTO/PM
- Update sprint plan with clarity
- Re-communicate to team

### 2. Documentation Lag

**Symptom**: Sprint ends but docs not updated for days

**Prevention**:
- Block next sprint until G-Sprint-Close passes
- Set calendar reminder at sprint end
- Assign documentation owner

**Fix**:
- Complete documentation immediately
- Add automation (CI checks)
- Review process in retro

### 3. Scope Creep

**Symptom**: Sprint grows beyond capacity

**Prevention**:
- Protect sprint scope after kickoff
- New items go to backlog, not current sprint
- Any addition requires removal

**Fix**:
- Escalate to CTO/PM
- Formally adjust scope with documentation
- Track as risk for future sprints

### 4. Carryover Accumulation

**Symptom**: Same items carried over multiple sprints

**Prevention**:
- Investigate why items not completing
- Break down large items
- Address blockers aggressively

**Fix**:
- Re-estimate carryover items
- Consider dropping or redesigning
- Discuss in retro

### 5. Sprint Numbering Conflicts

**Symptom**: Multiple documents show different sprint numbers

**Prevention**:
- Run SSOT validation before commit
- Follow numbering conventions strictly
- Use Roadmap Change Request for renumbering

**Fix**:
- File Roadmap Change Request
- Update all documents atomically
- Run SSOT validation to confirm

---

## Templates Reference

| Template | Location | Purpose |
|----------|----------|---------|
| SPRINT-TEMPLATE.md | `03-Templates-Tools/5-Project-Templates/PLANNING-HIERARCHY-TEMPLATE/` | Sprint plan structure |
| ROADMAP-TEMPLATE.md | Same location | Roadmap structure |
| Roadmap Change Request | `SDLC-Sprint-Planning-Governance.md` Section 5 | Change control |

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│                    SPRINT PLANNING FLOW                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. CLOSE PREVIOUS SPRINT                                       │
│     □ G-Sprint-Close passed                                     │
│     □ Documentation updated (<24h)                              │
│                                                                 │
│  2. PLAN NEW SPRINT                                             │
│     □ Check roadmap alignment                                   │
│     □ Calculate capacity                                        │
│     □ Create SPRINT-XX.md                                       │
│     □ Prioritize backlog (P0/P1/P2)                            │
│                                                                 │
│  3. PASS G-SPRINT GATE                                          │
│     □ All checklist items verified                              │
│     □ Approved by authority                                     │
│     □ Sprint kickoff scheduled                                  │
│                                                                 │
│  4. EXECUTE SPRINT                                              │
│     □ Daily standups                                            │
│     □ Track progress                                            │
│     □ Escalate blockers                                         │
│                                                                 │
│  5. CLOSE SPRINT (repeat)                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

**Document Status**: ACTIVE
**Last Updated**: January 18, 2026
**Owner**: CTO Office
