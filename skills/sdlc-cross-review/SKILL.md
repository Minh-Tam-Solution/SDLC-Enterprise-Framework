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

| Question | Read |
|---|---|
| What "independent" means at this repo's tier, and how a review is bound to a commit | `controls/tiers.md` "Per-tier controls" |
| Which lane a review counts in; cross-vendor review | `controls/tiers.md` "Model reviewer lane" · `controls/tiers.md` "Cross-vendor review" |
| Why the reviewer must be a fresh context | `ai-engineering/context-and-hats.md` "Reviewer = fresh context" |
| Who counts as the author (bots and their operators) | `controls/gates.md` "Approver independence" |
| Data classes, and which lane may read which | `standards/security.md` "Data classes and model access" |
| What a review of a risk-floor diff must add | `controls/risk-floor-paths.md` "Rule" |
| The verdict schema, severities and abstain reasons | `ai-engineering/context-and-hats.md` "Typed verdict" · `templates/agent/SOUL-example.md` |
| What class of evidence a review is | `controls/rule-contract.md` §2 |

Say which lane produced the review. A review run in a developer session is not the production lane (`adoption/adoption.md` "Evaluate the mechanism you rely on, not a surrogate").

## Steps

1. **Independence.** If this session wrote or edited the change, or has seen the reasoning that produced it, do not review it: return `insufficient_evidence` with the same-context abstain reason from `templates/agent/SOUL-example.md`. Offer step 4's hand-over instead.
2. **Author and operator.** Identify the author; if it is a bot or agent identity, find its operator the way `controls/gates.md` "Approver independence" says. Whoever that section excludes cannot review this change independently. If the section cannot decide for this author ⇒ `insufficient_evidence`.
3. **Data classes, before any content moves.** Map every changed path to its class from the policy repo, and check that this lane (this model, or the model you would export to) is authorized for each class, as `standards/security.md` "Data classes and model access" defines. An unclassified path ⇒ ask first. Any path the lane may not read ⇒ `insufficient_evidence` with the abstain reason that section names; list the paths and hand over to a person. Never trim the file out and review the rest as if complete.
4. **Inputs.** The reviewer gets the diff and the criteria only: the issue or acceptance criteria, the tier, risk-floor paths touched (`controls/risk-floor-paths.md`), and the relevant standards (`standards/security.md`, `standards/testing.md`, `standards/change-and-deployment.md`). Not the author's chat, plan or self-assessment. Bind the review to the exact commit and diff in the fields `controls/tiers.md` "Per-tier controls" names.
   - **Acting as reviewer** (fresh context, e.g. a reviewer subagent): continue to step 5.
   - **Preparing for another reviewer:** write the inputs to one file (diff, criteria, commit binding, a pointer to the verdict schema), with no secrets, and tell the user where it is. The user chooses the reviewer and sends it; do not call external APIs yourself. Whether another vendor's review counts as cross-vendor: `controls/tiers.md` "Cross-vendor review".
5. **Review.** Check the diff against the criteria. Every finding carries file, line, the claim and its evidence (a quote or a command you ran with its output). On risk-floor paths, also do what `controls/risk-floor-paths.md` "Rule" asks of the review.
6. **Verdict.** Read `ai-engineering/context-and-hats.md` "Typed verdict" and return exactly that schema — field names, allowed values, severities and the rules that combine them — plus the lane and the commit binding from step 4. Cannot run or see what is needed ⇒ `insufficient_evidence`, never a silent approve.

## Rules

- Present the verdict as the class of evidence `controls/rule-contract.md` §2 gives a model review — never as a human approval.
- A new commit after the review makes it stale; re-bind or re-review (`controls/tiers.md` "Per-tier controls").
- One responsible reviewer; no review of a review (`core/constitution.md` "Demand before surface").
- Do not approve, merge or post the verdict anywhere the user did not ask for.
