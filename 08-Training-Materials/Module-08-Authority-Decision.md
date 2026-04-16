---
document_id: "TRAINING-MODULE-08"
title: "Module 08: Authority & Decision Governance"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "2 hours 30 minutes (5 parts)"
audience: "All team members — developers, pod leads, architects, product managers, executives"
prerequisite: "Module 01-07 (SDLC Overview, Pillars, Zero Mock, Code Quality, Workflow, AI Tools, SASE)"
format: "Lecture + Case Study + Hands-on Exercises"
---

# Module 08: Authority & Decision Governance

> **Core principle**: "Ask first, act later." If you are unsure whether you have the authority, ASK before you act.

---

## 1. Authority Boundaries (30 minutes)

Every role in the team has a **clearly defined decision scope**. Acting outside that scope is a governance violation, regardless of seniority or tenure.

| Role | Decision Authority | NO Authority (must ask) |
|------|-------------------|------------------------|
| **CEO/Chairman** | Strategic vision, M&A, investment, organizational structure, senior hires, product roadmap, feature priority, UX/UI direction, SDLC methodology | Technical architecture, tech stack selection, security decisions, infrastructure |
| **CPO** | Product roadmap, feature priority, UX/UI design, user stories, SDLC methodology, folder structure (Stage 01-09) | System architecture changes, infrastructure management, security policy |
| **CTO** | System architecture, tech stack, security policy, infrastructure, code review, performance optimization | **NOT**: change product direction; restructure SDLC folders (Stage 01-09); bypass quality gates; modify SOUL templates; merge code without gate approval; self-approve ADRs for structural changes |
| **Pod Lead** | Sprint planning (within pod), PR review (1st reviewer), member mentoring, task assignment within pod | NOT approve gate G3/G4; NOT change tier/pricing; NOT restructure codebase; NOT add major dependencies without CTO approval |
| **Developer** | Code implementation, test writing, PR creation, bug fixes within assigned scope | NOT approve/reject gates; NOT change SDLC process; NOT self-approve PRs; NOT deploy to production |

### Key Principles

1. **Technical authority is not change authority**: A CTO has architecture authority but does NOT have authority to execute structural changes without approval.
2. **Seniority does not exempt governance**: Even a CEO must create a gate when deploying to production.
3. **"I know how" is not "I am allowed to"**: Knowing how to restructure a codebase does not mean you are permitted to do it unilaterally.

---

## 2. Decision Matrix (30 minutes)

The table below defines clearly: who proposes, who approves, and whether an ADR and gate are required.

| Decision Type | Proposed By | Approved By | ADR Required? | Gate Required? |
|--------------|------------|------------|:-------------:|:--------------:|
| New feature (product) | PM/BA | CPO | No | G0 -> G1 |
| Architecture change | CTO/Architect | CTO + CPO review | **Yes** | G2 |
| Tech stack change | CTO | CTO + CPO approve | **Yes** | G2 |
| SDLC process change | CPO | CPO + CTO review | **Yes** | -- |
| Security policy | CTO | CTO (consult CPO) | Yes | -- |
| Hiring decision | Pod Lead proposes | CEO/CPO approve | No | -- |
| Budget > $500/mo | Requester | CEO | No | -- |
| Database migration | Dev/CTO | CTO approve, CPO aware | No | G2 |
| **SDLC folder restructure** | **Prohibited without CPO approval** | CPO + CTO joint | **Mandatory** | G2 |
| Codebase restructure | CTO proposes | CTO + CPO approve | **Yes** | G2 |
| Deployment to production | CTO | CTO + CEO (G4 gate) | No | G3 -> G4 |
| Major dependency (>1000 LOC) | Dev | CTO approve | Optional | -- |
| Refactor > 500 LOC | Dev | Pod Lead + CTO aware | No | -- |

### ADR (Architecture Decision Record) Process

When the table above shows "Yes" in the ADR column, the mandatory process is:

```
1. Proposer writes ADR draft
   -> File: docs/02-design/01-ADRs/ADR-{NNN}-{title}.md
   -> Format: Context -> Decision -> Alternatives -> Consequences

2. ADR committed to git (status: PROPOSED)

3. Reviewer(s) review within 48h
   -> Comment directly on file or PR

4. ADR approved -> status: ACCEPTED

5. ONLY AFTER ADR IS ACCEPTED -> begin implementation
```

**Anti-pattern**: Writing an ADR AFTER implementation is complete renders the ADR meaningless. The ADR must come BEFORE code.

---

## 3. Escalation Protocol (15 minutes)

```
Level 1: Dev -> Pod Lead
         Channel: Team chat (pod channel)
         SLA: Same day
         Examples: technical blocker, urgent PR review needed

Level 2: Pod Lead -> CTO (tech issues)
         Channel: {TEAM_CHANNEL}, tag CTO
         SLA: Same day
         Examples: architecture decision, security concern, infra issue

Level 3: Pod Lead -> CEO/CPO (product/priority issues)
         Channel: {TEAM_CHANNEL}, tag CEO/CPO
         SLA: Next business day
         Examples: feature priority conflict, scope change, resource request

Level 4: CEO + CTO + CPO joint decision
         Channel: Meeting (online or in-person) + documented in team channel
         SLA: 48 hours
         Examples: structural changes, codebase restructure, tech stack migration
```

### Escalation Rules

1. **No skipping levels** -- A developer must not go directly to the CEO for a technical issue. Escalate through the Pod Lead first.
2. **Must be documented in writing** -- Write it in the team channel or create a gate in SDLC Orchestrator. Verbal agreements do NOT count.
3. **Unsure who to escalate to? Ask the CTO first** -- The CTO will classify whether the issue is tech or product and route it to the right person.
4. **Urgent does not mean undocumented** -- Handle the emergency first, but you MUST document it within 24 hours.

---

## 4. Case Study: Unauthorized Restructuring Incident (30 minutes)

### The Scenario

A CTO performed a full codebase restructure on a production platform:

- **Action**: Moved 14,565 files into a new directory structure (`/dev/` + `/business/`), renamed folders, changed the directory architecture.
- **Missing**: No ADR, no sprint plan, no gate approval, no notification to the CPO.
- **This was the second violation in 3 days**.

### Analysis: What Went Wrong?

| Step | Should Have Done | Actually Did |
|------|-----------------|-------------|
| 1 | Write an ADR explaining the restructuring rationale | No ADR written |
| 2 | Commit ADR, wait for CPO + CEO review | No one was notified |
| 3 | Create a sprint plan for the restructuring | No sprint plan |
| 4 | Create a G2 (Architecture) gate in SDLC Orchestrator | No gate created |
| 5 | Wait for G2 gate approval | No approval obtained |
| 6 | Execute restructuring per the approved plan | Acted unilaterally |
| 7 | Upload evidence (test results, file mapping) | No evidence collected |

### Specific Violations per SDLC 6.3.0

1. **Decision Matrix violation**: Codebase restructure requires CTO proposal + CPO approval + mandatory ADR + Gate G2. None of these steps were followed.
2. **Escalation Protocol violation**: Structural change belongs to Level 4 (CEO + CTO + CPO joint decision). The CTO decided alone.
3. **Sprint Workflow violation**: Enforcement Rule #1 -- Sprint plan MUST be committed BEFORE code. No sprint plan existed.
4. **Gate System violation**: No gate created, no evidence, no approval chain.

### Consequences

- **Drift between docs and code**: 14,565 files moved but documentation not updated, creating inconsistency.
- **CI/CD break risk**: Untested restructuring could cause build failures and broken import paths.
- **Team confusion**: Other team members did not know the new structure, wasting time finding files.
- **Trust erosion**: When governance is bypassed, the team loses confidence in the process.
- **Remediation cost**: Required violation report, training module, pre-commit hooks -- far more time than doing it correctly from the start.

### The Correct Process (If Done Over)

```
Day 1:  CTO writes ADR-XXX-platform-restructure.md
        -> Context: why restructuring is needed
        -> Decision: proposed /dev/ + /business/ structure
        -> Alternatives: keep as-is, restructure incrementally
        -> Consequences: impact on CI/CD, import paths, team workflow

Day 1:  CTO commits ADR -> creates PR -> tags CPO for review

Day 2:  CPO reviews ADR -> approves or requests changes

Day 3:  CTO creates sprint plan: SPRINT-XXX-RESTRUCTURE.md
        -> Commits sprint plan -> creates Gate G2 in SDLC Orchestrator

Day 3:  Gate G2 approved -> BEGIN implementation

Day 4-5: CTO executes restructuring per approved plan
          -> Runs tests -> uploads evidence -> submits Gate G3

Day 5:  CEO/CPO reviews Gate G3 -> approves -> merge
```

**Additional time**: 2-3 days. **Risk reduction**: Near zero.

### Core Lesson

> "Having technical authority does NOT mean having change authority. Architecture decisions ARE product decisions."

---

## 5. Hands-on Exercises (45 minutes)

For each scenario below, answer 3 questions:
- **Who decides?** (who gives final approval)
- **Is an ADR required?**
- **Is a gate required? Which one?**

### Scenarios

**1.** A Pod Lead wants to change the database schema for a new feature (adding 3 tables, 2 FKs).

**2.** The CTO wants to migrate the entire system from PostgreSQL to MongoDB.

**3.** A developer wants to refactor a large module (>500 LOC) to improve performance.

**4.** The CPO wants to add a major new feature to the product roadmap (estimated at 3 sprints).

**5.** The CTO wants to switch CI/CD from Docker Compose to Kubernetes for production.

**6.** A BA writes a user story for the next sprint (small feature, 1 new endpoint).

**7.** A developer discovers a critical security vulnerability (SQL injection) -- needs immediate patching.

**8.** The CTO wants to restructure the `docs/02-design/` folder into a new format (renaming subfolders, moving files).

**9.** A Pod Lead wants to bring in a freelance developer to meet a deadline.

**10.** The CEO wants to pivot product direction (from B2B to B2C for one product).

---

### Answer Key

**1. Database schema change (3 tables, 2 FKs)**
- Who decides: **CTO approves** (schema change = architecture decision)
- ADR: **No** (additive schema, not changing overall architecture)
- Gate: **G2** (Architecture review)

**2. Migrate PostgreSQL to MongoDB**
- Who decides: **CTO proposes + CPO approves** (tech stack change)
- ADR: **Mandatory** (fundamental tech stack change)
- Gate: **G2** (Architecture)
- Note: This is a Level 4 decision -- requires CEO + CTO + CPO joint agreement.

**3. Refactor module > 500 LOC**
- Who decides: **Pod Lead approves + CTO aware** (large refactor but no architecture change)
- ADR: **No** (refactor, not an architectural change)
- Gate: **No** (but requires PR review from Pod Lead)

**4. New feature spanning 3 sprints**
- Who decides: **CPO** (product roadmap decision)
- ADR: **No** (product decision, not architecture)
- Gate: **G0 -> G1** (Discovery -> Requirements)

**5. Docker Compose to Kubernetes**
- Who decides: **CTO proposes + CPO approves** (major infrastructure change)
- ADR: **Mandatory** (fundamental infrastructure change)
- Gate: **G2** (Architecture)

**6. BA writes user story**
- Who decides: **CPO reviews** (user story = product scope)
- ADR: **No**
- Gate: **G0 -> G1** (Discovery -> Requirements)

**7. Critical security vulnerability -- immediate patch needed**
- Who decides: **CTO** (security policy is CTO domain)
- ADR: **No** (emergency fix)
- Gate: **No blocking gate** -- patch immediately, but MUST document within 24h and create evidence afterward.
- Escalation: Level 2 (Pod Lead -> CTO), same day. CTO has authority to decide on immediate patching.

**8. Restructure `docs/02-design/` folder**
- Who decides: **CPO + CTO joint approval** (SDLC folder restructure)
- ADR: **Mandatory**
- Gate: **G2**
- Note: This is exactly the type of violation described in the case study. SDLC folders are protected.

**9. Bring in a freelance developer**
- Who decides: **CEO/CPO approve** (hiring/team composition)
- ADR: **No**
- Gate: **No**
- Note: Pod Lead proposes, but staffing decisions belong to CEO.

**10. CEO pivots product direction**
- Who decides: **CEO** (strategic vision)
- ADR: **Yes** (major change affecting the entire product)
- Gate: **G0** (Discovery -- re-evaluate product direction)
- Note: Although the CEO has strategic decision authority, the change must still be documented via ADR so the team understands the rationale.

---

## 6. Reference Materials

| Document | Location |
|----------|----------|
| Team Protocol (Pod structure, escalation, sprint cadence) | Project `docs/08-collaborate/team-protocol.md` |
| ADR Directory (all Architecture Decision Records) | Project `docs/02-design/01-ADRs/` |
| SDLC Orchestrator -- Gate Management | SDLC Orchestrator WebUI |
| SDLC 6.3.0 Framework | `SDLC-Enterprise-Framework/README.md` |
| Sprint Workflow Enforcement Rules | Project `CLAUDE.md` (section: Sprint Workflow Enforcement Rules) |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | Authority Boundaries -- who can do what, and who cannot | 30 min |
| 2 | Decision Matrix -- which decisions require whose approval | 30 min |
| 3 | Escalation Protocol -- 4 levels, no skipping | 15 min |
| 4 | Case Study -- analysis of a real governance violation | 30 min |
| 5 | Hands-on Exercises -- 10 scenarios | 45 min |
| | **Total** | **2h 30m** |

### After completing this module, participants must be able to:

1. Clearly distinguish the authority boundaries of CEO, CPO, CTO, Pod Lead, and Developer.
2. Correctly identify who approves each type of decision.
3. Know when an ADR is required and when it is not.
4. Apply the escalation protocol at the correct level.
5. Understand the real-world consequences of bypassing governance -- through the case study.

> **Remember**: "Ask first, act later." If unsure -- ask. The cost of asking = 5 minutes. The cost of fixing a mistake = 5 days.

---

## Assessment Questions

**Q1.** Who approves architecture decisions?
> **Answer**: CTO (with CPO review for major changes)

**Q2.** Can a CTO restructure the codebase without CPO approval?
> **Answer**: No. Codebase restructure requires CTO proposal + CPO approval + mandatory ADR + Gate G2.

**Q3.** What document is required for a tech stack change?
> **Answer**: An ADR (Architecture Decision Record)

**Q4.** What is the escalation path for a product priority issue?
> **Answer**: Pod Lead -> CEO/CPO (Level 3)

**Q5.** True or False: Having technical authority means having change authority.
> **Answer**: False. Technical authority (knowing how) is separate from change authority (being permitted to act). A CTO has architecture authority but must still obtain approval before executing structural changes.
