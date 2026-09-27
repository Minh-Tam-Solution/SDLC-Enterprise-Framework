---
name: sdlc-cross-review
description: Use when a change needs an independent review — acting as the reviewer in a fresh context, or preparing the diff and criteria for a reviewer in another session, model or tool. Enforces reviewer independence (not the author's context, not the author's operator), checks data classes before any content leaves for a model, and returns a typed verdict. The review is evidence, never an approval.
---

# Independent review

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents reviewing a change in a fresh context, or preparing one for another reviewer
**Review by**: 2026-12-26

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7.

"Independent" depends on the tier (`controls/tiers.md` "Per-tier controls"): STANDARD — a fresh-context AI review, recorded, not counted · PROFESSIONAL — a fresh-context AI review artifact bound to `commit_sha` + `diff_hash` (presence and binding are machine-checked, content is `REVIEW`) · ENTERPRISE — plus a human who is not the author approving the deploy tag on the exact SHA. The production reviewer lane is a CI check-run with its own key and a budget cap; the author cannot edit a check-run (`controls/tiers.md` "Model reviewer lane"). A review run in a developer session is not that lane; say which lane produced it (`adoption/adoption.md`: test the reviewer in the CI lane it will run in).

## Steps

1. **Independence.** If this session wrote or edited the change, or has seen the reasoning that produced it, do not review it: return `insufficient_evidence` with `abstain_reason: same_context` (`templates/agent/SOUL-example.md`, `ai-engineering/context-and-hats.md` "Reviewer = fresh context"). Offer step 3 instead.
2. **Author and operator.** Identify the author. If it is a bot or agent identity, its operator (per the repo's approvers file, `bot:<login> operated_by=<human>`) counts as the author: that person's review or approval is not independent (`controls/gates.md` "Approver independence"). A listed bot with no operator ⇒ cannot measure.
3. **Data classes, before any content moves.** Map every changed path to its class from the policy repo (`standards/security.md` "Data classes and model access"): `public` · `internal` · `confidential` · `restricted` · `no-ai`. Unlisted path with no declared default ⇒ unclassified ⇒ ask first. A lane (this model, or the model you would export to) reads a class only if the policy repo authorizes that lane for it; `no-ai` is authorized for none. Any path the lane is not authorized for ⇒ `insufficient_evidence` with `abstain_reason: restricted_data`, name the paths, hand over to a person. Never trim the file out and review the rest as if complete.
4. **Inputs.** The reviewer gets the diff and the criteria only: the issue or acceptance criteria, the tier, risk-floor paths touched (`controls/risk-floor-paths.md`), and the relevant standards (`standards/security.md`, `standards/testing.md`, `standards/change-and-deployment.md`). Not the author's chat, plan or self-assessment. Bind the review to the exact `commit_sha` and a hash of the diff.
   - **Acting as reviewer** (fresh context, e.g. a reviewer subagent): continue to step 5.
   - **Preparing for another reviewer:** write the inputs to one file (diff, criteria, SHA, diff hash, the verdict schema below), with no secrets, and tell the user where it is. The user chooses the reviewer and sends it; do not call external APIs yourself. A review in another vendor's model counts as cross-vendor only when CI records the provider; otherwise it is `ADVISORY` (`controls/tiers.md`).
5. **Review.** Check the diff against the criteria. Every finding carries file, line, the claim and its evidence (a quote or a command you ran with its output). On risk-floor paths, also re-derive any headline number in the diff independently (`controls/risk-floor-paths.md` "Rule").
6. **Verdict**, typed (`ai-engineering/context-and-hats.md` "Typed verdict"):

   ```yaml
   verdict: approve | changes_requested | insufficient_evidence
   abstain_reason: ""        # required with insufficient_evidence, e.g. same_context, restricted_data
   reviewer_type: <model or human, and the lane>
   commit_sha: <sha>
   diff_hash: <hash>
   findings:
     - {severity: BLOCKER | MAJOR | MINOR, file: <path>, line: <n>, claim: <what is wrong>, evidence: <quote or command output>}
   ```

   `approve` with any `BLOCKER` counts as `changes_requested`. Cannot run or see what is needed ⇒ `insufficient_evidence`, never a silent approve.

## Rules

- An AI review is `REVIEW`-class evidence. It is not a human approval and never a `MACHINE` gate by itself (`controls/rule-contract.md` §2).
- A new commit after the review makes it stale: the `diff_hash` no longer matches (`controls/tiers.md`).
- One responsible reviewer; no review of a review (`core/constitution.md` "Demand before surface").
- Do not approve, merge or post the verdict anywhere the user did not ask for.
