# Review and CI evidence

> Who reads this: whoever approves, merges or automates the merge of a change written by a person or an agent.
> When: when setting up review rules for a repo, before approving a change, and before trusting a green check.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: framework maintainers
**Consumer**: reviewers and approvers; maintainers of merge rules and product CI
**Review by**: 2026-12-26

*Shortens:* the argument about how closely a change must be read, review rounds that do not converge, and the gap between "a check was green" and "this exact change was tested".

Tiers and `change_harm` live in [`tiers.md`](tiers.md); the paths in [`risk-floor-paths.md`](risk-floor-paths.md); approver independence in [`gates.md`](gates.md#approver-independence); what a good test is in [`standards/testing.md`](../standards/testing.md). This page says how a review tier is assigned and what CI evidence an approval may rely on. MUST / SHOULD carry their RFC 2119 meaning.

## Review tiers by reversibility

Two review tiers per change, decided by what a mistake would cost to undo:

| Review tier | A change is in it when it touches | Review |
|---|---|---|
| **irreversible** | money or ledger code · migrations and production data · authentication, authorization and security controls · anything external-facing (messages to people outside the team, public interfaces, published content) · the risk floor | one change, one approval, at its head SHA |
| **reversible** | everything else: a revert restores the previous state | may be approved in a batch, recorded per change |

- **MUST** assign the tier by machine from the paths the diff touches, using the repo's declared path classes (risk floor plus its own additions). An author's or agent's label may raise the tier, never lower it.
  *Why:* a self-declared tier is set by the party with the most reason to set it low; a path cannot be talked down.
- **MUST** treat an unclassifiable diff (the classifier failed, a path list is missing) as irreversible and report "cannot measure".
  *Why:* a classifier that fails open sends the riskiest changes down the cheapest lane ([`gates.md`](gates.md), G2).
- **MUST** bind every approval to the exact head SHA it was given on. A new commit voids it; the code host enforces this (dismiss stale approvals on push; require approval of the most recent push).
  *Why:* otherwise a reviewer approves diff A and diff B is merged.
- **MAY** approve reversible changes in a batch, but **MUST** record the approval per change at its own head SHA. Irreversible changes **MUST NOT** be batch-approved.
  *Why:* batching saves reviewer time where a revert is cheap; a per-change record keeps each merge traceable to a decision on the code that was merged.
- **SHOULD** measure the time each change waits for approval, per tier ([`ai-engineering/agent-operations.md`](../ai-engineering/agent-operations.md#observability)).
  *Why:* heavyweight approval slows delivery without lowering the change fail rate (DORA); a tier whose queue grows is a sign to move work to automated checks, not to approve faster.

## CI is the oracle

An agent's report that tests pass is a claim. The evidence is a check-run the agent cannot edit.

- **MUST** accept only check-runs whose head SHA equals the full head SHA of the change being merged. A green run on an earlier commit, on another branch, or reported in a comment does not count.
  *Why:* a pass belongs to a commit, not to a pull request; matching on a short or stale SHA accepts tests of different code.
- **MUST** treat a required check that is missing, pending or skipped as "cannot measure", never as a pass.
  *Why:* absence of a red result is not a green result ([`gates.md`](gates.md), G1).
- **SHOULD** run required checks on the change as it will land: up to date with the base branch, or through a merge queue that tests the change on top of the latest base and the changes ahead of it.
  *Why:* two changes that pass alone can fail together.
- **MUST** show fail-first evidence for a fix or new behaviour on the irreversible tier, and **SHOULD** elsewhere: the new or changed test runs red against the base code and green against the head, both runs recorded in CI or the review.
  *Why:* a test that was never red has not been shown to detect the defect it claims to cover.
- **MUST** flag, by machine, a diff that touches test files and lowers the number of collected tests or adds skip, expected-failure or focus markers. The change then needs an independent review and a written reason ([`standards/testing.md`](../standards/testing.md#agents-and-tests)).
  *Why:* agents optimise for a passing run; removing the test that fails is the cheapest way to get one.

## Review goal and metrics

The goal of review is to **minimise the human time spent per change without raising reverts or incidents**. A rule that adds human time must show it lowers one of the guardrails; a rule that removes human time must show the guardrails did not rise.

| Kind | Metric | Read as |
|---|---|---|
| cost | human approvals per change (median, p95) | per review level, below |
| cost | human review comments per change | per review level |
| cost | time a change waits on a person (first request to last approval) | per review level ([`agent-operations.md`](../ai-engineering/agent-operations.md#observability)) |
| guardrail | revert rate: merged changes reverted or rolled back within 14 days | per review level |
| guardrail | incident rate: incidents attributed to a merged change | per review level |

- **SHOULD** record each approval, its reviewer identity and its head SHA by machine, so the cost metrics come from the code host, not from memory.
- **MUST** read a cost drop next to the guardrails for the same period. Fewer approvals with more reverts is not an improvement.

## Human approvals by change level

The level belongs to the **change**, never to its author: an agent's change and a senior engineer's change on the same paths get the same level. The levels refine the two review tiers above; they are not a second taxonomy. Map them onto whatever classification the repo already uses, and never below what its service tier requires ([`tiers.md`](tiers.md)).

| Level | Review tier | The change is | Human approvals at merge |
|---|---|---|---|
| **Low** | reversible | docs; internal-only code; additive code behind a flag whose flip is itself a reviewed change | 0, once required automated checks and the security review are green on the head SHA |
| **Medium** | reversible | any other reversible change, including additive code behind a flag that can be flipped without review | 1 |
| **High** | irreversible | anything in the irreversible tier | 2; where the organisation has only one eligible approver: 1 human + a blocking security review + a review by a model from a different vendor, recorded as an exception on the change |

- **MUST** start strict and loosen a level only with measured evidence from the metrics above (a period of baseline numbers, the guardrails flat). Loosening is a recorded decision.
- **MUST NOT** count an agent's approval as a human approval, whatever account it uses ([`gates.md`](gates.md#approver-independence)).
- **MUST** bind every approval to a specific commit. A new commit needs re-approval, unless the change's diff (base..head) is byte-identical to the approved one and the merge tree is clean; then the approval may carry over, recorded by machine.
  *Why:* a rebase that changes nothing should not cost a person's time; anything else is a different change.

## Converging a review

A review that never ends spends the time the levels were meant to save.

- **MUST** label every finding **Important** (blocks merge: a defect, a security issue, a broken contract), **Nit** (style, naming, optional) or **Pre-existing** (present on the base; not attributed to the change, tracked separately). Only Important blocks.
- **MUST** close every review thread with a reason: fixed (with the commit), disputed (with the argument), intentional, or out of scope (with a tracking link).
- **MUST NOT** repeat a finding already posted on the change. Name the **class** of the bug when it can recur elsewhere, so the fix covers the class, not one line.
- **SHOULD** review only the new diff after round 2.
- **MUST** stop after 3 rounds with Important findings still open and reconsider the approach (split, redesign, or close), rather than start round 4.

## Evaluating the AI reviewer

An AI reviewer is a measured instrument, not a trusted one.

- **SHOULD** turn every revert and incident into an evaluation case: the change that caused it, and the finding a reviewer should have raised.
- **MUST** re-score the reviewer against the evaluation set whenever its prompts, tools or model change, and compare with the previous score before switching.
- **SHOULD** measure noise by the author's response to each finding (fixed / disputed / intentional / dismissed), and by running the reviewer on known-clean changes, where every Important finding is a false positive.

## Circuit breaker

An extension beyond the source below, which lists automatic tightening as not yet built there.

- **SHOULD** raise the level automatically (more approvals, or Low → Medium) when the revert or incident rate of a level rises above a declared threshold over a declared window, and lower it back only when the rate has recovered for the same window.
- The threshold, window and current state are visible to everyone who merges; a change of state is recorded like any other decision.

## Checklist

- [ ] The review level comes from the change's paths, not from the author.
- [ ] Human approvals match the level; no agent approval counted as human.
- [ ] Approvals are on the current head SHA, or carried over only for a byte-identical diff with a clean merge tree.
- [ ] Findings are labelled Important / Nit / Pre-existing; only Important blocks; every thread closed with a reason.
- [ ] At most 3 rounds; after round 2 only the new diff is reviewed.
- [ ] Approvals per change, wait time, revert rate and incident rate are recorded per level.
- [ ] Reverts and incidents feed the reviewer's evaluation set; the reviewer is re-scored on every prompt, tool or model change.

## Candidate rules

Each enters at `ADVISORY` through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md).

| Candidate | Command idea |
|---|---|
| review tier from paths | classify the diff's paths against the declared path classes; unknown ⇒ irreversible, exit `1` |
| approval on head | the latest approval by an eligible approver was given on the current full head SHA |
| check on head | every required check-run for the full head SHA is `success`; missing or pending ⇒ exit `1` |
| fail-first | run the changed tests on base (expect red) and on head (expect green) |
| test count | collected tests on head ≥ on base, and no new skip or focus markers, unless the change carries an independent review |
| review level | Low / Medium / High from paths; human approvals on the head SHA ≥ the level's count |
| review metrics | approvals, comments and wait time per change, revert and incident rate, per level |
| open thread | no unresolved Important finding on the head SHA |
| circuit breaker | revert or incident rate above threshold for the window ⇒ level raised |

## Sources

Current practice, each opened on the date shown:

- GitHub Docs — Available rules for rulesets (dismiss stale approvals when new commits are pushed; require approval of the most recent reviewable push; required status checks pass on the commits being merged, strict mode up to date with base) — <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets> (accessed 2026-10-08)
- GitHub Docs — Managing a merge queue (required checks pass when applied to the latest target branch and the changes ahead in the queue) — <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue> (accessed 2026-10-08)
- GitHub Docs — REST API, check runs (list check runs for a commit ref) — <https://docs.github.com/en/rest/checks/runs> (accessed 2026-10-08)
- Addy Osmani, Morgan Westlee Lunt, Qing Wang — Solving code review at Anthropic, claude.dev blog, 2026-10-15 (review goal and metrics, risk-based approval counts, convergence and finding labels, reviewer evaluation; lists automatic tightening as not yet built) — cited from a reviewed summary on 2026-10-17
- DORA — Streamlining change approval (no evidence that formal external review lowers change fail rates; peer review in the development platform; automated checks) — <https://dora.dev/capabilities/streamlining-change-approval/> (accessed 2026-10-08)
