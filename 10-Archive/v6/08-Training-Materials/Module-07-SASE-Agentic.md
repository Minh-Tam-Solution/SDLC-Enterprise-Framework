---
document_id: "TRAINING-MODULE-07"
title: "Module 07: SASE Agentic Principles (SE 3.0)"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "4 hours (8 parts)"
audience: "All team members — developers, pod leads, architects, product managers"
prerequisite: "Module 01-06 (SDLC Overview through AI Tools)"
format: "Lecture + Case Study + Hands-on Exercises"
---

# Module 07: SASE Agentic Principles (SE 3.0)

> **Core principle**: "Human accountability is non-negotiable." AI agents execute, but humans own every line of code that ships to production.

---

## 1. What Is SASE? (30 minutes)

### Definition

**SASE (SE 3.0)** = Software Agentic Software Engineering — a structured approach to AI-assisted development with clear role separation, standardized artifacts, and graduated autonomy levels.

**Origin**: arXiv:2509.06216v2 — research on software engineering in the age of AI agents.

### The Evolution of Software Engineering

```
SE 1.0 (Traditional):
  Human writes all code
  AI used only as autocomplete
  No structured collaboration

SE 2.0 (AI-Assisted):
  AI generates code suggestions
  Human reviews and accepts/rejects
  Tools: Copilot, ChatGPT, Claude

SE 3.0 (SASE — Current):
  AI agents execute tasks independently
  Human guides and validates
  Structured artifacts and protocols
  Clear role separation (SE4H vs SE4A)
```

### Why SASE Matters

| Benefit | Explanation |
|---------|-------------|
| **Productivity** | 10x-50x improvement with proper agent orchestration |
| **Quality** | Consistent output through standardized artifacts |
| **Accountability** | Human remains responsible for shipped code |
| **Scalability** | Agents handle repetitive tasks, humans focus on strategy |

---

## 2. SE4H vs SE4A — The Two Core Roles (45 minutes)

### Role Definitions

| Aspect | SE4H (Agent Coach) | SE4A (Agent Executor) |
|--------|--------------------|-----------------------|
| **Full name** | Software Engineering FOR Humans | Software Engineering FOR Agents |
| **Role** | Guide and supervise AI agents | Execute human-specified intent |
| **Key skill** | Intent specification, quality validation | Code generation, pattern consistency |
| **Artifacts created** | BRS, MTS, VCR | LPS, CRP, MRP |
| **Decision authority** | **FINAL** (has veto power) | **NONE** (propose only) |

### SE4H (Human Coach) — Responsibilities

```
Creates:
  BRS (BriefingScript)     — Describes intent clearly
  MTS (MentorScript)       — Defines coding standards and patterns
  VCR (Validation Report)  — Final validation certificate

Active in:
  Stage 00 (Foundation):   100% human — strategic planning
  Stage 01 (Planning):     80% — requirements with AI assist
  Stage 02 (Design):       60% — architecture with AI patterns
  Stage 09 (Govern):       90% — strategic oversight
```

### SE4A (AI Executor) — Responsibilities

```
Creates:
  LPS (LoopScript)         — Iterative execution plan
  CRP (Consultation Report)— Handles uncertainty (asks human)
  MRP (Merge Request)      — Evidence-based merge request

Active in:
  Stage 03 (Integrate):    60% — API contract generation
  Stage 04 (Build):        70% — code implementation
  Stage 05 (Test):         70% — test generation
  Stage 08 (Collaborate):  60% — code review automation
```

### The Critical Principle

```
"Human Accountability Principle"

  Human ALWAYS bears responsibility for code shipped to production.
  AI only PROPOSES — it never decides.
  Every output must pass through human validation.

  If a bug ships: the human who approved the VCR is accountable.
  If AI generates bad code: the human who merged it is accountable.
  There is no "the AI did it" defense.
```

---

## 3. The 6 SASE Artifacts (45 minutes)

### Overview

```
Human-Created Artifacts (SE4H):
  BRS — BriefingScript:  Describes intent and context
  MTS — MentorScript:    Coding standards and patterns
  VCR — Validation Certificate Report: Final validation

Agent-Created Artifacts (SE4A):
  LPS — LoopScript:      Iterative execution plan
  CRP — Consultation Report Protocol: Uncertainty handling
  MRP — Merge Request Protocol: Evidence-based merge
```

### 3.1 BRS — BriefingScript

**Created by**: Human (SE4H)
**Purpose**: Describe intent clearly so AI agents understand what to build.

```markdown
# BRS-{Feature}-{Date}

## Intent
[Clear description of what needs to be done]

## Context
[Background information, business context]

## Constraints
[Technical limitations, time constraints]

## Success Criteria
[How to know when the task is complete]

## Out of Scope
[What NOT to do]
```

### 3.2 MTS — MentorScript

**Created by**: Human (SE4H)
**Purpose**: Define coding standards and patterns for agents to follow.

```markdown
# MTS-{Project}-{Version}

## Coding Standards
  Python: snake_case, max 50 chars
  TypeScript: camelCase, max 50 chars
  React: PascalCase, max 50 chars

## Architectural Patterns
  FastAPI microservices, repository pattern, clean architecture

## Quality Gates
  80%+ test coverage, zero mocks, <50ms API response

## Anti-Patterns
  No mock data, no placeholder implementations, no technical debt
```

### 3.3 LPS — LoopScript

**Created by**: Agent (SE4A)
**Purpose**: Plan iterative execution of the task.

```markdown
# LPS-{Task}-{Iteration}

## Current State
[What exists now]

## Target State
[What should exist after execution]

## Execution Steps
1. [Step 1 with expected outcome]
2. [Step 2 with expected outcome]
...

## Checkpoints
[How to verify progress at each step]
```

### 3.4 CRP — Consultation Report Protocol

**Created by**: Agent (SE4A) when uncertain
**Purpose**: Ask the human for clarification instead of guessing.

```markdown
# CRP-{Issue}-{Date}

## Uncertainty Description
[What is unclear]

## Options Analysis
### Option A
  Pros: ...   Cons: ...

### Option B
  Pros: ...   Cons: ...

## Agent Recommendation
[Suggested approach with reasoning]

## Human Decision Required
[Specific question that needs human input]
```

**Key rule**: "Better to ask than to assume wrong." If the agent is uncertain, it MUST generate a CRP rather than guessing.

### 3.5 MRP — Merge Request Protocol

**Created by**: Agent (SE4A)
**Purpose**: Provide evidence that the code is ready to merge.

**5-Point Evidence Required:**

| # | Check | Standard |
|---|-------|---------|
| 1 | Tests Passing | All tests green |
| 2 | Coverage Met | >=80% |
| 3 | Quality Score | >=95% compliance |
| 4 | Performance | <50ms response |
| 5 | Zero Mocks | 0 mock patterns found |

### 3.6 VCR — Validation Certificate Report

**Created by**: Human (SE4H) — NEVER by AI
**Purpose**: Final validation and approval for merge.

```markdown
# VCR-{Feature}-{Date}

## Validation Summary
  Code Review:    APPROVED / REJECTED
  Tests Review:   APPROVED / REJECTED
  Performance:    APPROVED / REJECTED
  Security:       APPROVED / REJECTED

## Validator
  Name: [Human validator name]
  Date: [Validation date]

## Decision
  APPROVED FOR MERGE / REQUIRES CHANGES
```

---

## 4. Agentic Maturity Levels (L0 to L3) (20 minutes)

| Level | Name | Human/AI Split | Artifacts Used | Description |
|-------|------|:--------------:|----------------|-------------|
| **L0** | Tool-Assisted | 90% / 10% | None | AI as autocomplete (e.g., Copilot suggestions) |
| **L1** | Agent-Assisted | 70% / 30% | BRS, MRP, VCR (basic) | Structured handoff (e.g., Claude with clear instructions) |
| **L2** | Structured Agentic | 30% / 70% | All 6 + ACE/AEE | Full SASE workflow (typical mid-stage organization) |
| **L3** | Lifecycle Agentic | 10% / 90% | All 6 + Memory/Learning | Proactive agents (target 2026+) |

**Typical organization**: L2 (Structured Agentic)
**Target**: L3 by end of 2026

---

## 5. The 7 Agentic Principles (30 minutes)

| # | Principle | Description |
|---|-----------|-------------|
| 1 | **Brief-First** | BriefingScript BEFORE any agent work. "No BRS, No Code." |
| 2 | **Evidence-Based MRP** | Every merge needs 5-point evidence. No evidence = no merge. |
| 3 | **Human Accountability** | Human owns shipped code. Agent proposes, never decides. |
| 4 | **Consultation Protocol** | CRP when uncertain. Do not guess — ask the human. |
| 5 | **Mentorship-as-Code** | Standards codified in MTS. Consistent patterns across the codebase. |
| 6 | **Dual Workbenches** | ACE (human workspace) + AEE (agent workspace). Clear separation. |
| 7 | **Gradual Autonomy** | Trust earned from L0 to L3. More autonomy requires more validation. |

---

## 6. ACE/AEE Architecture (15 minutes)

### Dual Workbench Concept

```
ACE (Agent Command Environment):
  Purpose:  Human workspace to guide agents
  Users:    SE4H (humans)
  Tools:    BRS editor, MTS configuration, VCR dashboard
  Example:  VS Code with SASE extensions

AEE (Agent Execution Environment):
  Purpose:  Agent workspace to execute tasks
  Users:    SE4A (AI agents)
  Tools:    LPS executor, CRP generator, MRP builder
  Example:  Claude Code execution environment
```

### Workflow Integration

```
1. Human -> ACE -> Creates BRS
2. BRS -> AEE -> Agent reads intent
3. Agent -> AEE -> Executes LPS
4. Agent -> AEE -> Generates MRP (or CRP if uncertain)
5. MRP -> ACE -> Human reviews
6. Human -> ACE -> Creates VCR (approve/reject)
7. If approved -> Merge
```

---

## 7. SASE Mapped to SDLC 6.3.0 Stages (15 minutes)

| Stage | SE4H % | SE4A % | Primary SASE Activity |
|-------|:------:|:------:|----------------------|
| 00 Foundation | 100% | 0% | Human-only strategic work |
| 01 Planning | 80% | 20% | Create BRS for features |
| 02 Design | 60% | 40% | Design LPS, define MTS |
| 03 Integrate | 40% | 60% | CRP generation, API contracts |
| 04 Build | 30% | 70% | Code execution with ACE/AEE |
| 05 Test | 30% | 70% | Execute LPS, generate MRP |
| 06 Deploy | 40% | 60% | Validation, coverage checks |
| 07 Operate | 50% | 50% | Monitoring, verification |
| 08 Collaborate | 40% | 60% | Code review, team coordination |
| 09 Govern | 90% | 10% | Policy, audit, strategic alignment |

**Key insight**: Stages 00 and 09 are human-dominant (strategic decisions). Stages 04 and 05 are agent-dominant (execution). Other stages require balanced collaboration.

---

## 8. Hands-on Exercises (30 minutes)

### Exercise 1: Write a BRS (15 minutes)

Write a BRS for the following feature: "Add a dashboard widget showing monthly BHXH contributions per employee."

Your BRS must include: Intent, Context, Constraints, Success Criteria, and Out of Scope.

### Exercise 1 — Expected Answer

```markdown
# BRS-BHXH-Dashboard-Widget-20260416

## Intent
Create a dashboard widget showing monthly BHXH contributions
(employer 17.5% and employee 8%) for each employee.

## Context
HR module needs visibility into social insurance costs per employee.
Data already exists in the payroll service.

## Constraints
- Render time <100ms
- Real database queries (zero mocks)
- Multi-tenant isolation required

## Success Criteria
- Widget renders contribution breakdown per employee
- Data matches payroll service calculations exactly
- Unit test coverage >=80%
- Performance <100ms render

## Out of Scope
- Historical trend charts (separate feature)
- Export to Excel (Phase 2)
```

### Exercise 2: Identify the Correct Artifact (15 minutes)

For each scenario, name the SASE artifact that should be created:

**1.** A developer wants to describe what a new feature should do before AI starts coding.
**2.** An AI agent is not sure whether the VAT rate should be 5% or 10% for a specific product category.
**3.** An AI agent has finished implementing a feature and wants to submit it for review.
**4.** A human reviewer has validated the AI's work and wants to approve the merge.
**5.** A project lead wants to define coding standards that all AI agents must follow.

### Exercise 2 Answers

**1.** **BRS** (BriefingScript) — describes intent before agent work begins.
**2.** **CRP** (Consultation Report Protocol) — agent asks human when uncertain.
**3.** **MRP** (Merge Request Protocol) — evidence-based merge request from agent.
**4.** **VCR** (Validation Certificate Report) — human approval for merge.
**5.** **MTS** (MentorScript) — coding standards and patterns for agents.

---

## Reference Materials

| Document | Location |
|----------|----------|
| Agentic Core Principles | `03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` |
| Agentic Maturity Model | `03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md` |
| Long-Running Agent Protocol | `03-AI-GOVERNANCE/16-LONG-RUNNING-AGENT-PROTOCOL.md` |
| Multi-Agent Patterns | `07-Implementation-Guides/MULTI-AGENT-PATTERNS.md` |
| SASE Artifact Templates | `05-Templates-Tools/04-SASE-Artifacts/` |
| SOUL Role Templates | `05-Templates-Tools/04-SASE-Artifacts/souls/` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | What Is SASE — definition, evolution, benefits | 30 min |
| 2 | SE4H vs SE4A — the two core roles | 45 min |
| 3 | The 6 SASE Artifacts — BRS, MTS, VCR, LPS, CRP, MRP | 45 min |
| 4 | Agentic Maturity Levels — L0 to L3 | 20 min |
| 5 | The 7 Agentic Principles | 30 min |
| 6 | ACE/AEE Architecture — dual workbench concept | 15 min |
| 7 | SASE Mapped to SDLC Stages — SE4H/SE4A split | 15 min |
| 8 | Hands-on Exercises — write BRS, identify artifacts | 30 min |
| | **Total** | **4h** |

### After completing this module, participants must be able to:

1. Explain the difference between SE 1.0, SE 2.0, and SE 3.0 (SASE).
2. Clearly distinguish the responsibilities of SE4H (Human Coach) and SE4A (AI Executor).
3. Name all 6 SASE artifacts and state who creates each one.
4. Write a proper BRS for a new feature.
5. Identify the correct maturity level (L0-L3) for a given team's practices.
6. Apply the Human Accountability Principle in daily work.

> **Remember**: "Human accountability is non-negotiable." The AI is a powerful tool, but the human who approves the VCR owns the outcome.

---

## Assessment Questions

**Q1.** What does SASE stand for?
> **Answer**: Software Agentic Software Engineering (SE 3.0).

**Q2.** Who creates the VCR (Validation Certificate Report)?
> **Answer**: SE4H (Human). The VCR is NEVER created by an AI agent.

**Q3.** What should an AI agent do when it is uncertain about a requirement?
> **Answer**: Generate a CRP (Consultation Report Protocol) asking the human for clarification. Never guess.

**Q4.** What are the 5 evidence points required in an MRP?
> **Answer**: (1) Tests passing, (2) Coverage >=80%, (3) Quality score >=95%, (4) Performance <50ms, (5) Zero mocks confirmed.

**Q5.** At which SASE maturity level does a typical mid-stage organization operate?
> **Answer**: L2 (Structured Agentic) — full SASE workflow with all 6 artifacts, 30% human / 70% AI in execution stages.
