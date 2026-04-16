---
document_id: "TRAINING-MODULE-11"
title: "Module 11: Remote Team Governance"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "1 hour (4 parts + exercises)"
audience: "All team members — developers, pod leads, architects, product managers (especially distributed teams)"
prerequisite: "Module 01-10 (SDLC Overview, Pillars, Zero Mock, Code Quality, Workflow, AI Tools, SASE, Authority, Quality Gate, ADR & Sprint Plan)"
format: "Workshop (theory + real-world scenarios)"
---

# Module 11: Remote Team Governance

> **Core principle**: "If it is not written down, it does not exist."

---

## 1. Remote Team Challenges (15 minutes)

Distributed and remote teams face unique challenges that co-located teams do not encounter, even when sharing the same timezone:

| Challenge | Description | Consequence If Not Addressed |
|-----------|-------------|------------------------------|
| **Async communication** | Decisions can be missed if not documented | Developers implement in the wrong direction, requiring rework |
| **No hallway conversations** | Everything must be written in team channels or SDLC Orchestrator | Information is lost, context is missing |
| **Context loss** | New members read code but do not know WHY decisions were made | Code conflicts with itself -- fixes break other things |
| **Trust deficit** | Difficult to assess contribution when you cannot observe directly | Team members do significant work that goes unnoticed |
| **Review delay** | Cannot walk over to someone's desk for a quick approval | PRs wait 3 days, sprint falls behind |

### Why Do Remote Teams Need More Governance?

Co-located teams can:
- Ask quickly across the desk: "Can I change this schema?" -- 30 seconds
- Demo on a screen: "Here, I am done, take a look" -- 2 minutes
- CEO walks by and sees what a dev is working on -- passive visibility

Remote teams have **none of this**. Everything must be:
1. **Written down** (team channel, PR description, ADR)
2. **Committed to git** (code, tests, docs)
3. **Uploaded as evidence** (SDLC Orchestrator)

> **Golden rule**: "Code not pushed = does not exist." Local code is invisible to governance. Only when `git push` succeeds does the team know what you have done.

---

## 2. Supplementary Rules for Remote Teams (15 minutes)

In addition to the standard rules (Module 08-10), remote teams follow 8 supplementary rules:

| # | Rule | Rationale |
|---|------|-----------|
| 1 | **Sprint plan MUST be CTO pre-approved BEFORE starting** | Remote members cannot ask clarifying questions in person -- the plan must be 100% clear |
| 2 | **Structural changes: 72-hour review window** | Async review needs time -- you cannot get approval in a hallway |
| 3 | **PR size limit: maximum 500 LOC per PR** | Small PRs = faster review in async workflows |
| 4 | **Daily standup in {TEAM_CHANNEL} before 10:00 AM** | Visibility -- the team knows what everyone is working on |
| 5 | **Response SLA: <4 hours during business hours** | Do not leave others blocked for too long |
| 6 | **Use threads in messaging** | Keep conversations organized and easy to find later |
| 7 | **Tag relevant people (@name)** | Do not assume everyone reads everything |
| 8 | **Screenshots for UI changes** | Remote reviewers cannot see your screen |

### Daily Standup Format

Every developer posts in the team channel before 10:00 AM:

```
Daily -- [Name] -- [date]
Yesterday: [task completed -- link PR if applicable]
Today: [planned task]
Blocker: [None or describe]
Estimate: [hours estimated for today's task]
```

**Example**:
```
Daily -- Alex -- 04/16
Yesterday: S53-02 payment handler -- PR #87 merged
Today: S53-03 invoice PDF export
Blocker: None
Estimate: 6h
```

Pod Lead checks by 10:30 AM. If a developer has not posted -- tag them directly.

---

## 3. Collaborator vs Fork Workflow (15 minutes)

There are 2 working models on GitHub/GitLab. The choice depends on the contributor's role:

### Model A -- Collaborator (for internal team members)

```
1. Added as GitHub/GitLab collaborator -> clone repo
2. Create branch: feature/<pod>/<task-name>
3. Code + test on branch
4. Push branch -> Create PR/MR
5. SDLC Orchestrator auto-review (Check Run)
6. Pod Lead reviews -> CTO reviews (if architecture)
7. Pod Lead merges after gate approval
```

### Model B -- Fork (for external/freelance contributors)

```
1. Fork repo -> clone fork
2. Code + test on fork
3. Push to fork -> Create PR/MR to upstream main
4. Same review process as Model A
5. Owner/Admin merges (not the contributor)
```

### Comparison

| Criterion | Collaborator | Fork |
|-----------|:------------:|:----:|
| Who uses it | Internal team | External, freelance |
| Clone from | Main repo | Personal fork |
| Push to | Branch on main repo | Personal fork |
| PR/MR target | Branch -> main (same repo) | Fork -> upstream main |
| Who merges | Pod Lead | Owner/Admin |
| SDLC Check Run | Automatic | Automatic |

### Rules for BOTH Models

- **NEVER push directly to main** -- branch protection is enforced
- **PR must pass Check Run** -- SDLC Orchestrator auto-review is mandatory
- **Code not pushed = does not exist** -- local code is invisible to governance
- Branch naming: `feature/<pod>/<task>` or `fix/<pod>/<task>`

### Workflow Diagram

```
Developer                    GitHub/GitLab              SDLC Orchestrator
   |                              |                           |
   |-- git push branch ---------->|                           |
   |                              |                           |
   |-- Create PR/MR ------------>|                           |
   |                              |-- webhook notification -->|
   |                              |                           |
   |                              |<-- Check Run (pass/fail) -|
   |                              |                           |
   |<-- PR status updated --------|                           |
   |                              |                           |
   |   Pod Lead reviews PR        |                           |
   |   Pod Lead merges ---------->|                           |
   |                              |-- gate evidence recorded->|
```

---

## 4. Exercises -- 5 Remote Team Scenarios (15 minutes)

### Scenario 1
A remote developer wants to change the database schema (adding a column to the `projects` table). What must they do BEFORE writing code?

### Scenario 2
A developer pushes code at 10:00 PM on Wednesday. When must the Pod Lead review it?

### Scenario 3
A PR has 800 LOC. How should it be handled?

### Scenario 4
A developer has not posted a daily standup for 2 consecutive days (Monday and Tuesday). How should the Pod Lead respond?

### Scenario 5
The CTO needs to merge an urgent PR (security fix) -- what is the expedited process?

---

### Answer Key

**Scenario 1**: Database schema change = structural change -> requires an ADR (Module 10). Process:
1. Write an ADR describing the schema change (context, decision, alternatives, consequences)
2. Commit the ADR to git with status PROPOSED
3. Wait for CTO review (72-hour review window for structural changes)
4. After ADR is ACCEPTED -> write migration + tests + code
5. Create PR (maximum 500 LOC)

**Scenario 2**: Response SLA is <4 hours **during business hours**. 10:00 PM is outside business hours -> Pod Lead reviews the next morning (before 10:00 AM Thursday). No requirement for after-hours review.

**Scenario 3**: 800 LOC exceeds the 500 LOC/PR limit. Split into 2 PRs:
- PR 1: Backend logic + tests (~400 LOC)
- PR 2: Frontend + integration (~400 LOC)
Each PR can be reviewed and merged independently.

**Scenario 4**: Pod Lead responds in escalating steps:
1. Day 1 (Monday): Tag directly in {TEAM_CHANNEL} -- "@[Name] daily report?"
2. Day 2 (Tuesday): Direct message asking the reason. There may be a blocker that needs support.
3. If it continues: Report to CTO in the weekly review.
Important: Ask first, do not assume. The developer may be sick, facing an emergency, or unaware of the process.

**Scenario 5**: Security fixes follow an expedited process:
1. CTO creates branch + fix + tests (no ADR required for bug fixes -- Module 10)
2. Creates PR -- SDLC Check Run still runs
3. CTO tags CEO in PR: "@CEO/CPO -- security fix, needs urgent merge"
4. CEO approves within <1 hour (not the standard 72h window)
5. CTO merges immediately after Check Run passes + CEO approves
Note: Still requires PR + Check Run + 1 approval. Only the review time is shortened, no steps are skipped.

---

## 5. Reference Materials

| Document | Location |
|----------|----------|
| Team Working Protocol | Project `docs/08-collaborate/team-protocol.md` |
| SDLC Orchestrator User Guide (Collaborator vs Fork) | Project `docs/08-collaborate/user-guides/` |
| SDLC Orchestrator WebUI | Your organization's SDLC Orchestrator instance |
| Sprint Workflow Enforcement Rules | Project `CLAUDE.md` |
| Module 08: Authority & Decision Governance | `08-Training-Materials/Module-08-Authority-Decision.md` |
| Module 10: ADR & Sprint Plan Workflow | `08-Training-Materials/Module-10-ADR-Sprint-Plan.md` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | Remote Team Challenges -- 5 challenges + golden rule | 15 min |
| 2 | Supplementary Rules -- 8 rules + daily standup format | 15 min |
| 3 | Collaborator vs Fork Workflow -- 2 models + comparison + diagram | 15 min |
| 4 | Exercises -- 5 real-world scenarios + answer key | 15 min |
| | **Total** | **1h** |

### After completing this module, participants must be able to:

1. Understand the 5 unique challenges of remote teams and how governance addresses them.
2. Apply the 8 supplementary rules for remote work (daily standup, 500 LOC limit, 72h review window).
3. Distinguish Collaborator vs Fork workflow and know when to use each model.
4. Handle real-world scenarios: schema change, oversized PR, missing standup, urgent security fix.

> **Remember**: "If it is not written down, it does not exist." Remote teams live and die by governance. Every rule in this module exists because someone violated it and the team paid the price. Doing it right from the start saves time for everyone.

---

## Assessment Questions

**Q1.** What is the maximum PR size for remote teams?
> **Answer**: 500 LOC. PRs exceeding this limit must be split into smaller, independently reviewable PRs.

**Q2.** What is the review window for structural changes?
> **Answer**: 72 hours. Structural changes (architecture, schema, restructure) require a 72-hour async review window because remote reviewers cannot provide hallway approvals.

**Q3.** What is the daily standup deadline?
> **Answer**: 10:00 AM. Every developer must post their daily standup in the team channel before 10:00 AM. Pod Lead checks by 10:30 AM.

**Q4.** Which model should external contributors use?
> **Answer**: The Fork model (Model B). External and freelance contributors fork the repo, work on their fork, and create PRs to the upstream main branch. Only Owner/Admin can merge.

**Q5.** True or False: Code not pushed to remote does not exist in governance.
> **Answer**: True. Local code is invisible to governance. Only code that has been `git push`-ed to the remote repository is visible to the team, reviewable, and trackable by SDLC Orchestrator. Until pushed, it does not exist from a governance perspective.
