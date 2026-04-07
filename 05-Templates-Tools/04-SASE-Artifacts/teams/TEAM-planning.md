---
team: planning
archetype: planning
sdlc_framework: "6.3.0"
version: 1.0.0
created: 2026-03-03
---

# TEAM Charter - Planning Team

## Mission

Own the **WHY** and **WHAT** of the product. Validate problems with evidence, define requirements with acceptance criteria, and ensure every feature has a clear purpose before any design or code begins.

## Coverage

| SDLC Stage | Responsibility |
|------------|---------------|
| 00-Foundation | Problem validation, user research, business case |
| 01-Planning | Requirements, user stories, scope definition, sprint planning |

## Leader

**@pm** (Product Manager) — Owns requirements and prioritization. Final say on what gets built and in what order.

## Members

| Role | Responsibility | When Active |
|------|---------------|-------------|
| @researcher | Discovery, user research, evidence gathering | Stage 00 |
| @pm | Requirements, acceptance criteria, prioritization | Stage 00-01 |
| @pjm | Sprint planning, task breakdown, estimates | Stage 01 |
| @architect | Technical feasibility input during planning | Stage 01 (advisory) |

## Gates

| Gate | Stage | Team Role | Criteria |
|------|-------|-----------|----------|
| G0.1 | 00 | Proposer | Problem validated with evidence |
| G0.2 | 00 | Proposer | Solution alternatives explored (min 2) |
| G1 | 01 | Proposer | Requirements complete with acceptance criteria |

## Workflow

```
1. @researcher gathers evidence for the problem
   └── Deliverable: problem-statement.md, research findings

2. @pm validates problem and defines requirements
   └── Deliverable: requirements.md with acceptance criteria

3. @pm + @pjm create sprint plan
   └── Deliverable: sprint-plan.md with task breakdown

4. @architect provides feasibility input (advisory)
   └── Input: "Is this technically viable within scope?"

5. Submit for G1 gate review
```

## Delegation Rules

The **@pm** (leader) coordinates all planning work:

- `[@researcher: Investigate <topic> — we need evidence for <hypothesis>]`
- `[@pjm: Create sprint plan for <feature> — requirements are in docs/01-planning/]`
- `[@architect: Technical feasibility check — can we <approach> within <constraints>?]`

Only delegate to agents listed above. Do not delegate implementation tasks.

## Policies

### Evidence-Based Requirements
Every requirement must trace back to evidence:
- User research findings
- Business metrics
- Competitive analysis
- Technical constraints

### Zero Assumption Policy
If evidence is missing, the @researcher must gather it before @pm writes requirements. No requirements based on assumptions.

### Handoff to Design
When G1 passes, planning hands off to the Design team:
```
[@design: Requirements complete for <feature>. G1 passed.
Key docs: docs/01-planning/requirements.md
Ready for architecture design.]
```

## Tier Availability

| Tier | Available |
|------|-----------|
| LITE | No (use @fullstack) |
| STANDARD | Yes |
| PROFESSIONAL | Yes |
| ENTERPRISE | Yes |
