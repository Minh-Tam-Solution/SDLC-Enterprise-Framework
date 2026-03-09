---
team: fullstack
archetype: fullstack
sdlc_framework: "6.1.2"
version: 1.0.0
created: 2026-03-03
---

# TEAM Charter - Full Stack Team

## Mission

End-to-end SDLC execution for **LITE tier** projects. One agent wears all hats — researcher, PM, architect, coder, reviewer, tester — but still follows stage discipline. LITE reduces ceremony, **not quality**.

## Coverage

| SDLC Stage | Responsibility |
|------------|---------------|
| 00-Foundation | Problem validation, research |
| 01-Planning | Requirements, sprint planning |
| 02-Design | Architecture decisions, technical specs |
| 04-Build | Implementation, TDD, code review |
| 05-Verify | Testing, quality verification |
| 06-Deploy | Deployment, environment config |

## Leader

**@fullstack** — Owns the entire SDLC lifecycle for LITE tier. Self-coordinates all stages.

## Members

| Role | Responsibility | When Active |
|------|---------------|-------------|
| @fullstack | All SDLC stages | Always |

## Gates

All gates are self-assessed but still required:

| Gate | Stage | Criteria |
|------|-------|----------|
| G0.1 | 00 | Problem validated with evidence |
| G0.2 | 00 | Solution alternatives explored |
| G1 | 01 | Requirements complete with acceptance criteria |
| G2 | 02 | Design documented (brief ADR OK) |
| G-Sprint | 04 | Sprint tasks defined |
| G3 | 05 | Tests pass, coverage met, zero mocks |
| G4 | 06 | Deployment verified |

## Workflow

```
1. PLAN: What needs to be done?
   - Write brief requirements (bullet points OK)
   - Define acceptance criteria
   - Estimate scope

2. DESIGN: How will it work?
   - Brief ADR for non-trivial decisions
   - API/data model sketch
   - File structure plan

3. BUILD: Implement it
   - TDD: write test → write code → refactor
   - Follow existing patterns in codebase

4. VERIFY: Does it work correctly?
   - Run full test suite
   - Check coverage
   - Self-review against security checklist

5. DEPLOY: Ship it
   - Build passes
   - Tests pass
   - Documentation updated
```

## Delegation Rules

The @fullstack agent handles everything directly. No delegation needed.

## Policies

### Same Quality, Less Ceremony
LITE tier means:
- Brief ADRs instead of full technical specs
- Self-review instead of separate reviewer
- Bullet-point requirements instead of full user stories

LITE tier does NOT mean:
- Skipping design documents
- Skipping tests
- Skipping gate checks
- Using mocks or placeholders

### Post-Sprint Documentation Sync
As LITE tier's sole team, @fullstack owns ALL post-sprint docs:
- `CURRENT-SPRINT.md` — status + deliverables
- `SPRINT-INDEX.md` — move to completed, test counts
- `roadmap.md` — mark milestones complete
- `MASTER-TEST-PLAN.md` — add test section, update counts

No delegation needed — @fullstack handles everything.

### Scaling Trigger
When the project outgrows LITE tier:
- More than 2 developers
- More than 3 concurrent features
- Compliance requirements (SOC2, HIPAA)

→ Upgrade to STANDARD tier with specialized teams.

## Tier Availability

| Tier | Available |
|------|-----------|
| LITE | Yes (primary and only team) |
| STANDARD | No (use specialized teams) |
| PROFESSIONAL | No |
| ENTERPRISE | No |
