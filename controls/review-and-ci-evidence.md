# Review and CI evidence

> Who reads this: whoever approves, merges or automates the merge of a change written by a person or an agent.
> When: when setting up review rules for a repo, before approving a change, and before trusting a green check.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: framework maintainers
**Consumer**: reviewers and approvers; maintainers of merge rules and product CI
**Review by**: 2026-12-26

*Shortens:* the argument about how closely a change must be read, and the gap between "a check was green" and "this exact change was tested".

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

## Candidate rules

Each enters at `ADVISORY` through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md).

| Candidate | Command idea |
|---|---|
| review tier from paths | classify the diff's paths against the declared path classes; unknown ⇒ irreversible, exit `1` |
| approval on head | the latest approval by an eligible approver was given on the current full head SHA |
| check on head | every required check-run for the full head SHA is `success`; missing or pending ⇒ exit `1` |
| fail-first | run the changed tests on base (expect red) and on head (expect green) |
| test count | collected tests on head ≥ on base, and no new skip or focus markers, unless the change carries an independent review |

## Sources

Current practice, each opened on the date shown:

- GitHub Docs — Available rules for rulesets (dismiss stale approvals when new commits are pushed; require approval of the most recent reviewable push; required status checks pass on the commits being merged, strict mode up to date with base) — <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets> (accessed 2026-10-08)
- GitHub Docs — Managing a merge queue (required checks pass when applied to the latest target branch and the changes ahead in the queue) — <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue> (accessed 2026-10-08)
- GitHub Docs — REST API, check runs (list check runs for a commit ref) — <https://docs.github.com/en/rest/checks/runs> (accessed 2026-10-08)
- DORA — Streamlining change approval (no evidence that formal external review lowers change fail rates; peer review in the development platform; automated checks) — <https://dora.dev/capabilities/streamlining-change-approval/> (accessed 2026-10-08)
