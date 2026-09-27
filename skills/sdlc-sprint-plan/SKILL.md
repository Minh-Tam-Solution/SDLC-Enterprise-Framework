---
name: sdlc-sprint-plan
description: Use when planning the next sprint, rewriting docs/04-build/current-sprint.md, deciding what to commit to, or closing a sprint. Builds the plan from the repo's state and the SDLC Enterprise Framework (SEF) sprint template, and checks every item for demand evidence, riskiest assumptions, kill criteria and controls proportional to risk.
---

# Sprint plan

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents planning or closing a sprint; the sprint owner
**Review by**: 2026-12-26

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7.

A sprint is 5–10 working days of committed work, recorded in one file with one owner (`standards/project-structure.md` "Planning files"). Stages are questions, not phases: one sprint may touch several (`core/lifecycle.md`).

## Plan

1. **Read the state**, in the newcomer order of `standards/project-structure.md` "Reading order for a newcomer": `README.md` → `AGENTS.md` → the current sprint file → the sprint index → the last five merged PRs → `docs/00-foundation/` and `docs/02-design/` when the item needs the why or the how; then the roadmap (`standards/project-structure.md` "Planning files"). Take paths from `AGENTS.md` if the repo uses another layout. Never guess the sprint number; read it.
2. **Tier** of the repo (see `sdlc-gate-check` step 2). It decides which stages and which evidence the sprint must produce (`core/lifecycle.md`), and how much ritual is allowed (`controls/tiers.md` "Ritual budget").
3. **Goal**: one sentence, stated as the user outcome. Progress is measured as time until a real user tries the real thing; fix the date and cut scope to meet it (`core/design-thinking.md` "Keep scope honest").
4. **Each candidate item** must answer, or it does not enter the sprint:
   - **Demand before surface** — who uses it and what breaks without it; "future users" or "compliance with §X" is not an answer (`core/constitution.md` "Demand before surface").
   - **Evidence strength** — label the demand evidence near zero / weak / medium / strong (`core/design-thinking.md` "Weigh evidence by strength"). Conviction alone leaves it a discovery item, not a build item.
   - **Riskiest assumptions** — for new product or feature work, the few assumptions that would kill it if false, each with a test and a success criterion written before the test runs; build the cheapest thing that answers the question (`core/design-thinking.md` "Test the riskiest assumptions").
   - **Kill criteria in numbers**, written before building (`core/design-thinking.md`; `adoption/adoption.md` "Kill criteria").
   - **Size** — finishable in hours to a few days; split larger ones (`standards/change-and-deployment.md` "Small changes, short branches").
   - **Stage and acceptance** — which stage question it answers, acceptance criteria as testable Given/When/Then scenarios (`standards/testing.md` "Tests prove requirements").
   - **Controls proportional to risk** — the tier's gates plus the change's harm: a risk-floor path or a restricted data class raises the control for that item only (`controls/tiers.md` "Two axes", `controls/risk-floor-paths.md`). Do not load a low-risk sprint with governance work.
5. **Governance vs product.** Count governance items (rules, gates, docs, rituals) against product items. Governance can grow faster than the product and still look like progress (`core/systems-thinking.md` "Measures get gamed"); name the consumer of each governance item or drop it.
6. **Write the plan** in the shape of `templates/project/current-sprint.md`: goal, dates, tier, committed items (issue, stage, one owner, state), stage gates expected this sprint with the evidence each needs, decisions (ADR or PR), open risks and missing evidence. Backlog items stay in the issue tracker, linked (`standards/project-structure.md`).
7. **Show it** to the user. Save to the repo's sprint file only when asked; the plan is committed when the owner merges it.

## Close

At sprint end (`core/lifecycle.md` "Sprint closure"): for each stage touched, what exited, what was re-opened and what evidence is still missing. Move the sprint section to the sprint index with its outcome, then rewrite the current sprint file for the next sprint. The sprint closes when the file is updated, not when the calendar says so.

## Rules

- No sprint gate and no scored rule list: sprint planning gates and the golden rules are retired (`MIGRATION-MAP.md`), and SEF builds no sprint governance (`core/constitution.md` "What the framework does NOT build").
- Measure outcomes, not output: lines, files, PRs and tokens are activity (`practices/lessons-to-rules.md` "Never measure agent output as progress").
- An item an agent adds "helpfully" is still unplanned work: compare the sprint's diffs with this plan before closing (`standards/change-and-deployment.md`).
