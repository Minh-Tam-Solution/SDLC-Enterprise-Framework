# Experiment: spec review (S1) and doc-vs-code drift check (S2)

> Who reads this: the owner deciding keep or drop; whoever runs the two experiments.
> When: while they run, and on the review date.

**SDLC Framework Version**: 7.0.0
**Status**: DRAFT
**Owner**: @cto SCB
**Consumer**: lanes writing specs (Bflow2, KIP); maintainers of `sdlc-cross-review` and the rule register
**Review by**: 2026-12-01

*Experiment, not in force beyond the advisory row DOC-3. Shortens:* design errors found after code is written, and docs that quietly stop matching the code. Source idea: google/elephant-goldfish-model (Apache-2.0; "design with an elephant, review with a goldfish"; its effect is the README's claim, not measured here). External practice is a trial to compare, never assumed better than ours ([`lessons-to-rules.md`](../practices/lessons-to-rules.md) "Vendor radar").

## S1 — spec review by a clean-context reviewer before code

- **What:** `skills/sdlc-cross-review/SKILL.md` "Spec review mode". The reviewer reads only the spec or plan and its linked decisions; independence and data-class checks are the skill's steps 1-3. Triggered by risk, not size ([`context-and-hats.md`](../ai-engineering/context-and-hats.md) "Plan before code").
- **Hypothesis:** [`Plan before code`](../ai-engineering/context-and-hats.md) has the reviewer check the diff against the plan, so a wrong plan survives to code. A fresh reader of the plan catches it earlier.
- **Signal:** share of specs whose design changed after the first implementation commit (a later commit to the spec that edits requirements or design decisions, not typos). Four weeks before vs four weeks after, on Bflow2 and KIP, each counted separately.
- **Keep** if the after-share is at most half the before-share on both repos, with at least 8 specs per period per repo. **Drop** if it is not lower, or the added review rounds delay specs without lowering the share. Fewer than 8 specs ⇒ "not measured": extend four weeks once, then decide on what exists.
- **Cost to watch:** spec content goes to a model vendor; a path of a class the lane may not read ⇒ `insufficient_evidence`, never a trimmed review.

## S2 — advisory drift check, DOC-3

- **What:** `scripts/check-doc-cites.sh`, rule DOC-3 (`ADVISORY`, `PRODUCT_CI`, in the [register](rule-contract.md#rule-register)). Counts `file:line` citations in `docs/*.md` that point outside the cited file or at a missing file, and anchors (a fence tagged `anchors`, one `path:line|text` per line) whose text is no longer on that line. Never blocks unless run with `--block`.
- **Hypothesis:** most citations that stop matching are real drift a reader would trip on.
- **Signal:** precision = findings a person confirms as real drift ÷ findings reported, on 5 sample specs from Bflow2 and KIP. Thresholds published before the run: **keep if ≥ 50%**; below 50% ⇒ drop the row, or narrow it once and re-measure. Zero findings on all five ⇒ precision is "not measured" (no positive control from the field); plant one citation in a sample and confirm it is reported before counting.
- **Known limits:** it checks that a line exists and a text is on it, not that the prose still describes the code; a line number that moved but stays inside the file is only caught by an anchor.

## Decision

On 2026-12-01 @cto SCB records for each of S1 and S2: `keep` (S2: move toward `REVIEW` along the [ladder](gates.md#the-ladder--switch-gates-on-by-trajectory-not-as-a-wall)), `drop` (remove the skill section or the DOC-3 row and script), or `extended→YYYY-MM-DD` with the reason. DOC-3's `deadline=` in the register is the same date; past it with count > 0 the rule is promoted or deleted (G4).
