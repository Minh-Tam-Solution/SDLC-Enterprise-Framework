# Risk floor paths

> Who reads this: whoever declares a repo's risk-floor paths, and whoever asks "does this diff need a human?"
> When: at repo setup, and when a diff touches a path listed here.

**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: product repos declaring risk-floor paths; the risk-floor review gate
**Review by**: 2026-12-26

*Shortens:* the argument about whether a small-looking diff needs a human. The path answers it.

## What it is

A fixed list of path patterns that always get the highest verification, whichever person, model
or agent wrote the change. It is a **path classification**, not a score: it computes no index,
and a model's confidence in its own output is not evidence here. It feeds `change_harm` in
[`tiers`](tiers.md): `effective_control = max(service_tier, change_harm)`.

## Paths that are never downgraded

| Path pattern | Why |
|---|---|
| `migrations/` | irreversible schema change; a bad migration can corrupt or lose data |
| `auth/` | authentication; a defect can let anyone in or lock everyone out |
| `tenant/` | tenant isolation; a defect can leak one tenant's data to another |
| `permissions/` | authorization; a defect can grant access that should be denied |
| `billing/` · `payment/` | directly moves or represents money |
| `infra/` | infrastructure and deployment config; a defect can take production down |
| `secrets/` | credentials and keys; a leak is not reversible by a patch |

Also on the floor wherever they appear (not path-bound): IAM configuration, production config,
and destructive SQL (`DROP`, or `DELETE` / `TRUNCATE` without a scoping `WHERE`).

A repo **adds** its own paths in the policy repo's `projects.yaml` ([`adoption`](../adoption/adoption.md)).
It does not remove any of the paths above.

## Rule

A diff touching any path on the floor needs human review by an approver who is not the author
or the author's operator ([`gates`](gates.md)), plus independent re-derivation of any headline
number in it. This floor sits **below** model routing: routing decides who does the work; the
floor decides the minimum verification the work gets.

## Not in scope

- Which model or agent may do which work: that is the tier's lane policy (`tiers.yaml`).
- Scoring the "quality" of AI-written code: v7 keeps no such index.
