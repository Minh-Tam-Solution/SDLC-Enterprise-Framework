---
name: sdlc-sprint-plan
description: Use when planning the next sprint, rewriting the repo's current sprint file, deciding what to commit to, or closing a sprint. Builds the plan from the repo's state and the SDLC Enterprise Framework (SEF) sprint template, and checks every item for demand evidence, riskiest assumptions, kill criteria and controls proportional to risk.
---

# Sprint plan

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents planning or closing a sprint; the sprint owner
**Review by**: 2026-12-26

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7.

What a sprint is — its length, its file, its owner, where history and backlog go: `standards/project-structure.md` "Planning files". How stages relate to a sprint: `core/lifecycle.md` "Ten stages".

## Plan

1. **Read the state** in the order of `standards/project-structure.md` "Reading order for a newcomer", then the roadmap named in `standards/project-structure.md` "Planning files". Take paths from `AGENTS.md` if the repo uses another layout. Never guess the sprint number; read it.
2. **Tier** of the repo (see `sdlc-gate-check` step 2). With it, read which stages and evidence the sprint must produce (`core/lifecycle.md` "Which stages each tier must cover", `core/lifecycle.md` "Exit evidence per stage") and how much ritual the tier allows (`controls/tiers.md` "Per-tier controls").
3. **Goal**: one sentence, stated as the user outcome. Fix the date and scope as `core/design-thinking.md` "Keep scope honest" says.
4. **Each candidate item** answers every question below from the section named, or it does not enter the sprint:

   | Question | Answer it from |
   |---|---|
   | Who uses it, and what breaks without it? | `core/constitution.md` "Demand before surface" |
   | How strong is the demand evidence? Label it with that section's scale. | `core/design-thinking.md` "Weigh evidence by strength" |
   | Which assumptions would kill it if false; the test and success criterion for each? | `core/design-thinking.md` "Test the riskiest assumptions" |
   | What are its kill criteria? | `core/design-thinking.md` "Write kill criteria in numbers before building" · `adoption/adoption.md` "Kill criteria" |
   | Is it small enough? Split it if not. | `standards/change-and-deployment.md` "Small changes, short branches" |
   | Which stage question does it answer; how are its acceptance criteria written? | `core/lifecycle.md` "Ten stages" · `standards/testing.md` "Tests prove requirements" |
   | Which controls does it need? | `controls/tiers.md` "Two axes" · `controls/risk-floor-paths.md` |

5. **Governance vs product.** Count governance items (rules, gates, docs, rituals) against product items, and read `core/systems-thinking.md` "Measures get gamed". Name the consumer of each governance item or drop it.
6. **Write the plan** with the sections of `templates/project/current-sprint.md`, as they are in the template. Backlog stays where `standards/project-structure.md` "Planning files" puts it, linked.
7. **Show it** to the user. Save to the repo's sprint file only when asked; the plan is committed when the owner merges it.

## Close

At sprint end, write what `core/lifecycle.md` "Sprint closure" requires for each stage touched, and move the sprint record as `standards/project-structure.md` "Planning files" says; then rewrite the current sprint file for the next sprint.

## Rules

- Before adding any sprint-level gate, score or ritual, check `core/constitution.md` "What the framework does NOT build" and `sdlc-framework` ("What SEF no longer has").
- Report outcomes, not output (`practices/lessons-to-rules.md` "Never measure agent output as progress").
- An item an agent adds "helpfully" is still unplanned work: compare the sprint's diffs with this plan before closing (`standards/change-and-deployment.md` "Small changes, short branches").
