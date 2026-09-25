---
document_id: "TRAINING-MODULE-10"
title: "Module 10: ADR & Sprint Plan Workflow"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "2 hours (6 parts)"
audience: "All team members — developers, pod leads, architects, product managers"
prerequisite: "Module 01-09 (SDLC Overview, Pillars, Zero Mock, Code Quality, Workflow, AI Tools, SASE, Authority, Quality Gate)"
format: "Workshop (theory + hands-on ADR and Sprint Plan writing)"
---

# Module 10: ADR & Sprint Plan Workflow

> **Core principle**: "Design first, code later. Plan first, sprint later. No exceptions."

---

## 1. When Is an ADR Required? (30 minutes)

An ADR (Architecture Decision Record) documents an **architecture decision** -- why solution A was chosen over solution B. Not every change needs an ADR. The table below clarifies the distinction:

| Type of Change | ADR Required? | Example |
|---------------|:------------:|---------|
| Architecture change | **Mandatory** | Database migration, new service, API protocol change |
| Tech stack change | **Mandatory** | New framework (e.g., Tailwind v4), new language, new provider |
| Schema change (breaking) | **Mandatory** | Drop column, rename table, change FK |
| Codebase restructure | **Mandatory** | Move folders, rename modules, change project structure |
| Major dependency | Recommended | New npm package >100KB, new Python package with C extensions |
| New API endpoint | Not required | Standard CRUD following existing patterns |
| Bug fix | Not required | Unless the fix changes architecture |
| Refactor (<500 LOC) | Not required | Internal cleanup, variable rename |
| New UI page | Not required | Unless using a new framework or pattern |

> **Quick rule**: If the change affects **system structure**, **tech stack**, or **how components communicate with each other** -- an ADR is required. If it is only an implementation detail within existing boundaries -- no ADR needed.

### Case Study 1: A Well-Written ADR (ACCEPTED) -- Gold Standard

An ADR deciding to use a **GitHub App** instead of an **OAuth App** for SCM integration:

- **Clear context**: Needed to create Check Runs on GitHub PRs. OAuth App does not support `checks:write`.
- **Alternatives evaluated**: Compared OAuth App vs GitHub App across 6 criteria (Check Runs, setup complexity, token management, branch protection, rate limit, per-repo control).
- **Consequences include both positive and negative**: Identified that setup is more complex and tokens expire in 1h requiring refresh logic.
- **Specific decision**: "Use GitHub App (not OAuth App) starting from Sprint 45."

This is a model ADR. The reader immediately understands: why the decision was made, which alternatives were rejected, and what the consequences are.

### Case Study 2: A Post-Hoc ADR (REJECTED) -- Anti-pattern

A CTO restructured an entire codebase (14,565 files) before writing the ADR:

- **ADR written AFTER implementation** -- violates the "design first, code later" principle
- **No alternatives listed** -- only describes what was done, no analysis of other options
- **No approval** -- CPO was not notified before the change occurred
- **Result**: ADR was REJECTED; remediation took far more time than doing it correctly from the start

> **Lesson**: An ADR written after implementation is a post-mortem, not governance. The ADR must come BEFORE code.

---

## 2. How to Write an ADR (30 minutes)

### Standard Template

```markdown
---
document_id: "ADR-{NNN}"
title: "ADR-{NNN}: {Decision Title}"
stage: "02-DESIGN"
status: "PROPOSED"
created: "{date}"
---

# ADR-{NNN}: {Decision Title}

## Status
PROPOSED (awaiting CTO + CPO review)

## Context
[Why is this decision needed? What problem needs to be solved?]

## Decision
[The specific decision -- technology, pattern, or approach chosen.]

## Alternatives Considered
[What other options were evaluated? Why were they rejected?]

## Consequences
### Positive
[What improves?]
### Negative
[What becomes harder? What risks exist?]
### Risks
[What could go wrong? How to mitigate?]
```

### Lifecycle

```
1. Dev/CTO writes ADR draft
   -> File: docs/02-design/01-ADRs/ADR-{NNN}-{title}.md
   -> Status: PROPOSED

2. Commit ADR to git (PROPOSED)

3. CTO + CPO review within 48h
   -> Comment on file or PR

4. ADR approved -> status: ACCEPTED

5. ONLY AFTER ACCEPTED -> begin implementation
```

### 4 Common Anti-patterns

| # | Anti-pattern | Why It Is Wrong | How to Fix |
|---|-------------|-----------------|------------|
| 1 | **ADR written AFTER implementation** | Defeats the purpose of governance. An ADR is a decision tool, not documentation. | Write the ADR BEFORE code. If already implemented, still write it but mark "retroactive" and do not repeat the mistake. |
| 2 | **ADR with no alternatives** | If there is only 1 option, no ADR is needed. An ADR is for DECIDING between multiple choices. | List at least 2 alternatives. If truly only 1 option exists, explain why. |
| 3 | **ADR that is too long** | The best ADRs are 1-2 pages. Longer documents lose the reader's focus. | Separate into ADR (decision) + Tech Spec (technical details). |
| 4 | **ADR without review** | A PROPOSED ADR that no one reviews is a rubber stamp. | Require CTO + CPO review before ACCEPTED. Tag reviewers on the PR. |

---

## 3. Sprint Plan Workflow (30 minutes)

### Enforcement Rules (from CLAUDE.md)

These are 6 mandatory rules, derived from a PM Audit that found 7 violations:

```
MANDATORY -- Before Writing ANY Code:

1. Sprint plan MUST be committed BEFORE code begins
   - File: docs/04-build/02-Sprint-Plans/SPRINT-{NNN}-{TITLE}.md
   - Must be in git (committed, not just local file)
   - Violation example: plan created 13 minutes AFTER code

2. Design docs MUST exist for the sprint's scope
   - Stage 01: Requirements or user stories referencing the sprint
   - Stage 02: ADR if architectural decision involved
   - Stage 03: API contract if new endpoints
   - Violation example: 13 docs untracked

3. Tests MUST be written BEFORE or WITH code (TDD)
   - Backend: backend/tests/unit/test_sprint{NNN}_*.py
   - Frontend: frontend/src/__tests__/
   - Violation example: 450 LOC with zero tests

MANDATORY -- Before Claiming "SHIPPED":

4. All artifacts MUST be committed to git
   - Code + tests + docs + CLAUDE.md update = ONE commit or PR
   - Nothing is "shipped" until git push origin main succeeds
   - Violation example: CTO approval only in chat, not committed

5. Build MUST pass
   - Backend: pytest tests/unit/ --tb=no -q = 0 failures
   - Frontend: npx next build = 0 errors
   - Violation example: "SHIPPED" claimed without verification

6. CLAUDE.md MUST be updated
   - Sprint number in Version line
   - Sprint entry in Sprint History table
   - Test count updated
```

### Sprint Plan Format

File: `docs/04-build/02-Sprint-Plans/SPRINT-{NNN}-{TITLE}.md`

```markdown
---
document_id: "SPRINT-{NNN}"
title: "Sprint {NNN}: {Title}"
stage: "04-BUILD"
status: "PLANNED"
created: "{date}"
phase: "Phase {N}"
depends: ["SPRINT-{NNN-1}"]
---

# Sprint {NNN}: {Title}

## Sprint Goal
[1-2 sentences describing the sprint objective]

## Backlog

| # | Task | Owner | Est | Priority |
|---|------|-------|-----|----------|
| 1 | ... | Dev A | 4h | P0 |
| 2 | ... | Dev B | 2h | P1 |

## Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] All tests pass
- [ ] CLAUDE.md updated

## Dependencies
- Sprint {NNN-1} shipped
- ADR-{NNN} approved (if applicable)
```

### Walkthrough: The Correct Process

```
Step 1: PM/Dev writes sprint plan
        -> File SPRINT-{NNN}-{TITLE}.md

Step 2: git add + git commit sprint plan
        -> Plan MUST be in git BEFORE code begins

Step 3: Write design docs (ADR, API contract) if needed
        -> Commit design docs

Step 4: Write tests (TDD)
        -> Commit tests

Step 5: Implement code
        -> Commit code

Step 6: Verify build passes
        -> pytest + next build

Step 7: Update CLAUDE.md
        -> Version + Sprint History + test count

Step 8: git push origin main
        -> Only NOW can it be called "SHIPPED"
```

### Real Comparison: Compliant vs Non-Compliant Sprint

| Criterion | Non-Compliant Sprint (VIOLATION) | Compliant Sprint |
|-----------|--------------------------------|-----------------|
| Sprint plan | Created **13 min AFTER** code | Committed **BEFORE** code |
| Design docs | 13 docs untracked | Docs committed before implementation |
| Tests | 450 LOC, zero tests | Tests written with code (TDD) |
| Build check | "SHIPPED" without verification | `pytest` + `next build` pass |
| CLAUDE.md | Not updated | Updated in the same commit |
| Result | 7 violations, PM Audit triggered | 0 violations, clean sprint |

> **Instructor note**: Ask participants: "How much extra time does following the correct process take compared to the non-compliant sprint?" -- Answer: ~30 minutes (write plan + commit before starting). Time to fix violations: 2+ days (audit + remediation + training module).

---

## 4. Document-First Culture (15 minutes)

### Core Principle

> "A governance platform must govern itself." -- PM Audit Report

If your organization's governance platform -- an SDLC framework -- cannot follow its own process, it loses credibility with every user.

### 4 Document-First Rules

| # | Rule | Explanation |
|---|------|-------------|
| 1 | **CLAUDE.md is the SSOT** | All project metadata (version, sprint history, test count, tech stack) lives in CLAUDE.md. If CLAUDE.md is not updated, the project metadata is wrong. |
| 2 | **Sprint history must be updated EVERY sprint** | No skipping. No "I will update later." Sprint done = update immediately. |
| 3 | **Test count must be exact** | Do not round (625 is not "~600"). Do not estimate. Run `pytest` and record the exact number. |
| 4 | **"SHIPPED" = committed + pushed + build passes** | Saying "I wrote the code" is not SHIPPED. Only when `git push origin main` succeeds AND the build passes is it SHIPPED. |

### PM Audit -- 7 Violations

| Violation | Description | Enforcement Rule Broken |
|-----------|-------------|------------------------|
| V1 | Sprint plan created 13 min AFTER code | Rule #1: Plan before code |
| V2 | 13 docs untracked | Rule #2: Design docs exist |
| V3 | No sprint checklist | Process checklist |
| V4 | 450 LOC, zero tests | Rule #3: TDD |
| V5 | Dependencies not documented | Sprint plan format |
| V6 | CTO approval only in chat, not committed | Rule #4: All artifacts in git |
| V7 | "SHIPPED" without running build | Rule #5: Build must pass |

> **Lesson**: These 7 violations led to: a PM Audit report, 3 supplementary training modules, new pre-commit hooks, and Enforcement Rules written into CLAUDE.md. The cost of fixing mistakes vastly exceeds the cost of doing it right the first time.

---

## 5. Exercises (15 minutes)

### Exercise 1: Write an ADR

**Scenario**: The team wants to replace PostgreSQL with MongoDB for the `agent_conversations` table (reason: conversations are document-oriented, schema changes frequently, PostgreSQL JSONB is not flexible enough).

**Requirements**: Write a complete ADR following the template in Part 2, including:
- Context (why the change is needed)
- Decision (the specific choice)
- Alternatives Considered (at least 2 other options)
- Consequences (positive + negative + risks)

### Exercise 2: Write a Sprint Plan

**Scenario**: Scope is "Add email verification for signup" -- users must confirm their email before their account is activated.

**Requirements**: Write a complete sprint plan following the template in Part 3, including:
- Sprint Goal (1-2 sentences)
- Backlog table (at least 5 tasks)
- Acceptance Criteria (at least 4 criteria)
- Dependencies

### Evaluation Rubric (CTO Review)

| Criterion | Pass | Fail |
|-----------|------|------|
| **Context/Goal** | Clearly explains the problem being solved | Vague, unclear why it is needed |
| **Decision/Scope** | Specific, immediately actionable | Too generic, not actionable |
| **Alternatives** | At least 2 options with reasons for rejection | Only 1 option or no rationale |
| **Consequences/Criteria** | Includes both positive and negative | Only lists benefits, ignores risks |
| **Format** | Follows template, has frontmatter | Missing sections, no frontmatter |
| **Testability** | Acceptance criteria are verifiable | Criteria are vague ("make it good") |

---

## 6. Reference Materials

| Document | Location |
|----------|----------|
| ADR Directory (all ADRs) | Project `docs/02-design/01-ADRs/` |
| Sprint Plans Directory | Project `docs/04-build/02-Sprint-Plans/` |
| Sprint Workflow Enforcement Rules | Project `CLAUDE.md` |
| Module 08: Authority & Decision Governance | `08-Training-Materials/Module-08-Authority-Decision.md` |
| Module 09: Quality Gate Workshop | `08-Training-Materials/Module-09-Quality-Gate-Workshop.md` |
| SDLC 6.3.0 Framework | `SDLC-Enterprise-Framework/README.md` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | When Is an ADR Required -- decision table + 2 case studies | 30 min |
| 2 | How to Write an ADR -- template + lifecycle + 4 anti-patterns | 30 min |
| 3 | Sprint Plan Workflow -- 6 enforcement rules + compliant vs non-compliant comparison | 30 min |
| 4 | Document-First Culture -- 4 rules + PM Audit case study | 15 min |
| 5 | Exercises -- write ADR + sprint plan + evaluation rubric | 15 min |
| | **Total** | **2h** |

### After completing this module, participants must be able to:

1. Distinguish when an ADR is required and when it is not.
2. Write a complete ADR following the standard template (Context, Decision, Alternatives, Consequences).
3. Understand and comply with the 6 Sprint Workflow Enforcement Rules.
4. Write a sprint plan with a backlog table and acceptance criteria.
5. Apply Document-First culture: CLAUDE.md is the SSOT, "SHIPPED" = committed + pushed + build passes.

> **Remember**: "Design first, code later. Plan first, sprint later." The cost of asking and doing it right = 30 minutes. The cost of fixing mistakes = 5 days + audit + training module. Choose wisely.

---

## Assessment Questions

**Q1.** When is an ADR mandatory?
> **Answer**: When the change involves architecture, schema (breaking), tech stack, or codebase restructure. In short: anything that affects system structure, tech stack, or how components communicate.

**Q2.** What status must an ADR have before implementation begins?
> **Answer**: ACCEPTED. Implementation must not start until the ADR has been reviewed and approved (status changed from PROPOSED to ACCEPTED).

**Q3.** What is the anti-pattern of writing an ADR after implementation?
> **Answer**: Post-hoc justification. An ADR written after implementation is a post-mortem, not a governance tool. It defeats the purpose of design-first decision-making because the decision has already been made and executed.

**Q4.** What file must be committed before writing any code?
> **Answer**: The sprint plan. File: `docs/04-build/02-Sprint-Plans/SPRINT-{NNN}-{TITLE}.md`. It must be committed to git (not just a local file) before any code work begins (Enforcement Rule #1).

**Q5.** What does Enforcement Rule #6 require?
> **Answer**: CLAUDE.md must be updated every sprint with: the sprint number in the Version line, a new entry in the Sprint History table, and the updated test count.
