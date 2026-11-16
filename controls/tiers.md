# Tiers by risk

> Who reads this: whoever sets up a repo, and whoever asks "does this change need a human?"
> When: at repo setup, when a repo starts touching new data or users, and at quarterly recertification.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: repo owners setting a tier; reviewers deciding whether a change needs a human
**Review by**: 2026-12-26

*Shortens:* ritual on low-risk work, and arguments about who must approve what.

## Definitions

| Tier | Any one of these | Example |
|---|---|---|
| **LITE** | no production deploy · the only user is the author · no real data | sandbox, proof of concept |
| **STANDARD** | real internal users · `git revert` restores state · no money, customer or personnel data | internal docs site, internal tool |
| **PROFESSIONAL** | others make decisions on its numbers or commands · schema migrations on live data · users outside the team | reporting service, policy repo |
| **ENTERPRISE** | money path · customer or personnel PII · accounting or contracts · irreversible side-effects | payments, payroll, customer chat |

The old criterion — team size — is gone. One person building ENTERPRISE gets ENTERPRISE gates.

## Derivation: evidence, not declaration

`tier = max(repo evidence, declared service metadata, deploy evidence)`

| Source | Signals |
|---|---|
| Repo evidence (`PRODUCT_CI`) | `migrations/` ⇒ ≥PRO · a path in `risk_floor_paths` ⇒ ≥PRO · money, payroll, pricing, personnel or PII path segments ⇒ ENT |
| Declared metadata | data kinds · who decides on the output · reversible or not |
| Deploy evidence | production target · cron · service unit |

- Match path **segments**, not substrings: `hr/` must not match `chrome/`.
- Declared < derived ⇒ exit `2`. Lowering a tier needs a recorded decision id in the commit.
- A path heuristic alone is gamed by moving code. That is why there are three sources.
- The metadata file declares `tier_scheme: v7-risk`, so old data is never read with the new meaning.
- PROFESSIONAL and ENTERPRISE **recertify quarterly** — a recurring row in the deadline ledger ([`gates`](gates.md)).

## Two axes

`effective_control = max(service_tier, change_harm)`

- `service_tier` belongs to the repo. `change_harm` belongs to the diff: which [risk-floor](risk-floor-paths.md) paths and [data classes](../standards/security.md#data-classes-and-model-access) it touches.
- A docs-only diff in an ENTERPRISE repo is still ENTERPRISE if it touches the approvers file.
- **Non-compensable harm** (email sent, payment captured, invoice issued): mark `non_compensable: true`. Control goes **before** the side-effect — dry-run, idempotency key, reconciliation. Rollback after the fact does not undo it.

## Per-tier controls

| | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---|---|---|---|---|
| **Mandatory `MACHINE` gates** | repo tests | + generated-file drift · provenance if deployed | + tier floor · deploy-tree harness · provenance probe · deadline ledger | + timed rollback · deploy log · money-path probe (shadow first) |
| **Agent autonomy** | build, merge, deploy | build, merge, deploy; the PR is a record, 0 approvals | merge any diff; auto-deploy when gates are green | as PRO outside the risk floor; a diff touching it merges with the approvals of its change level (a human code owner) and **deploys only from an approved tag** ([two control points](#merge-and-production-authorization)) |
| **"Independent" means** | — | a fresh-context AI review, recorded, not counted | a fresh-context AI review artifact bound to `commit_sha` + `diff_hash`; presence and binding are `MACHINE`, content is `REVIEW` | + a human ≠ author approves the deploy tag on the exact SHA, bound to the artifact digest |
| **Bounded price** | nothing leaves the author's machine; data classes still apply | ≤1 person-day of rework; with a database, one timed restore before the first deploy | internal numbers wrong ≤1 cycle — only if a probe measures it; no probe ⇒ write "ceiling not measured" | compensable: approved tag + rollback + probe; non-compensable: control before the side-effect |
| **Meter for the price** | — | incident record field `price_paid` (hours, bad records, reached customers?) | same | same, plus one line per incident: price paid vs ceiling |
| **Ritual budget** | none | declared minutes per week; start at one 15-minute review | same | same; over budget ⇒ step a gate down or cut it (G4) |

Details that make the table hold:

- **Cross-vendor review** is self-declared and `ADVISORY` until CI records the provider in the check-run. Otherwise it is theatre. Its class, what it blocks and when it may replace a human approval are stated once, in the [engineering authorization contract](review-and-ci-evidence.md#engineering-authorization-contract).
- **Model reviewer lane:** CI check-run, its own API key, a budget cap. The author cannot edit a check-run. Paths that must not leave your network get `insufficient_evidence` + a human, never a pretend review.
- **PROFESSIONAL and up:** merge with the approvals the change level requires ([engineering authorization contract](review-and-ci-evidence.md#engineering-authorization-contract)), no more → a post-merge review issue opens automatically → the next self-merge is locked when the AI review artifact is missing, stale (`diff_hash` mismatch) or empty for >48h. More than 3 break-glass uses per repo in 14 days ⇒ review before the next deploy. This applies to owner accounts too.
- **ENTERPRISE approval** is bound to the head SHA and the artifact digest. A new commit after approval voids it: otherwise you approve diff A and deploy diff B.
- **ENTERPRISE approvers:** a named primary, a backup and an SLA. No backup ⇒ write "accepted single point of failure" in the decision. Flag approvals under 2 minutes with no comment. Estimate the review load from past PRs before switching it on.

## Merge and production authorization

Two control points, each granting one right. This section is the one contract; other pages and adopting repos point here instead of restating it.

| Control point | Grants | Checks | Approvals |
|---|---|---|---|
| **Merge authorization** | the change may land on the main branch | code quality, risk floor and `change_harm`, author ≠ reviewer ≠ the author's operator ([`gates.md`](gates.md#approver-independence)), CI evidence on the head SHA | by change level ([`review-and-ci-evidence.md`](review-and-ci-evidence.md#human-approvals-by-change-level)), under the [engineering authorization contract](review-and-ci-evidence.md#engineering-authorization-contract); never below the tier row above |
| **Production authorization** | this artifact may run in this production environment | artifact provenance (built in CI from the merged SHA, digest recorded), target environment, migration class, blast radius, recovery proved ([`standards/change-and-deployment.md`](../standards/change-and-deployment.md#before-a-deploy)) | by tier: the approved tag above for ENTERPRISE; the deploy gate's green checks below it |
| **Irreversible business action** (`non_compensable`, [two axes](#two-axes)) | one side-effect may happen once | authorization immediately before the action, an idempotency key, reconciliation afterwards | per action, not per deploy |

- **MUST NOT** treat a merge approval as production authorization. A merged change has no right to run in production until its own control point passes.
  *Why:* the merge reviewer judges a diff; production risk depends on the artifact, the target and the data, which the merge review does not see.
- **MAY** grant production authorization through a recorded policy that names a class of deploy (for example: no migration or additive only, no risk-floor path, a pinned deploy script) and uses the merge approval as one piece of its evidence. The right then comes from that policy, checked by the deploy gate, not from the approval alone.
- **MUST NOT** ask the same human to approve the same SHA for the same scope twice. A second approval is asked only when the scope differs: another control point, another artifact digest, another target.
  *Why:* a repeated approval of the same thing adds wait time and no evidence ([`core/constitution.md`](../core/constitution.md), a review of a review is removed).

## Solo vs small team is a measured state

- `solo` = fewer than 2 distinct accountable committers in the last 14 days. `small team` = 2 or more.
- Identity not clean enough to count ⇒ default `solo`, label `insufficient_evidence`, print it in the digest. Never silent.
- The state changes **who** satisfies independence, never **which** gates fire.
  - Solo: fresh-context AI review + shared QA + machine trace + a post-review with a deadline.
  - Small team: a second person where the table says human.
- Any control that needs ≥2 human approvers must have a solo equivalent, or it is cut.
- Moving from solo to small team is a hand-over of artifacts, not a change of process.
