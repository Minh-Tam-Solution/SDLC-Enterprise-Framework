# Tiers by risk

> Who reads this: whoever sets up a repo, and whoever asks "does this change need a human?"
> When: at repo setup, when a repo starts touching new data or users, and at quarterly recertification.

**SDLC Framework Version**: 7.0.0
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

- `service_tier` belongs to the repo. `change_harm` belongs to the diff: which [risk-floor](risk-floor-paths.md) or residency paths it touches.
- A docs-only diff in an ENTERPRISE repo is still ENTERPRISE if it touches the approvers file.
- **Non-compensable harm** (email sent, payment captured, invoice issued): mark `non_compensable: true`. Control goes **before** the side-effect — dry-run, idempotency key, reconciliation. Rollback after the fact does not undo it.

## Per-tier controls

| | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---|---|---|---|---|
| **Mandatory `MACHINE` gates** | repo tests | + generated-file drift · provenance if deployed | + tier floor · deploy-tree harness · provenance probe · deadline ledger | + timed rollback · deploy log · money-path probe (shadow first) |
| **Agent autonomy** | build, merge, deploy | build, merge, deploy; the PR is a record, 0 approvals | merge any diff; auto-deploy when gates are green | as PRO outside the risk floor; a diff touching it merges freely but **deploys only from an approved tag** |
| **"Independent" means** | — | a fresh-context AI review, recorded, not counted | a fresh-context AI review artifact bound to `commit_sha` + `diff_hash`; presence and binding are `MACHINE`, content is `REVIEW` | + a human ≠ author approves the deploy tag on the exact SHA, bound to the artifact digest |
| **Bounded price** | nothing leaves the author's machine; residency paths still apply | ≤1 person-day of rework; with a database, one timed restore before the first deploy | internal numbers wrong ≤1 cycle — only if a probe measures it; no probe ⇒ write "ceiling not measured" | compensable: approved tag + rollback + probe; non-compensable: control before the side-effect |
| **Meter for the price** | — | incident record field `price_paid` (hours, bad records, reached customers?) | same | same, plus one line per incident: price paid vs ceiling |
| **Ritual budget** | none | declared minutes per week; start at one 15-minute review | same | same; over budget ⇒ step a gate down or cut it (G4) |

Details that make the table hold:

- **Cross-vendor review** is self-declared and `ADVISORY` until CI records the provider in the check-run. Otherwise it is theatre.
- **Model reviewer lane:** CI check-run, its own API key, a budget cap. The author cannot edit a check-run. Paths that must not leave your network get `insufficient_evidence` + a human, never a pretend review.
- **PROFESSIONAL and up:** merge freely → a post-merge review issue opens automatically → the next self-merge is locked when the AI review artifact is missing, stale (`diff_hash` mismatch) or empty for >48h. More than 3 break-glass uses per repo in 14 days ⇒ review before the next deploy. This applies to owner accounts too.
- **ENTERPRISE approval** is bound to the head SHA and the artifact digest. A new commit after approval voids it: otherwise you approve diff A and deploy diff B.
- **ENTERPRISE approvers:** a named primary, a backup and an SLA. No backup ⇒ write "accepted single point of failure" in the decision. Flag approvals under 2 minutes with no comment. Estimate the review load from past PRs before switching it on.

## Solo vs small team is a measured state

- `solo` = fewer than 2 distinct accountable committers in the last 14 days. `small team` = 2 or more.
- Identity not clean enough to count ⇒ default `solo`, label `insufficient_evidence`, print it in the digest. Never silent.
- The state changes **who** satisfies independence, never **which** gates fire.
  - Solo: fresh-context AI review + shared QA + machine trace + a post-review with a deadline.
  - Small team: a second person where the table says human.
- Any control that needs ≥2 human approvers must have a solo equivalent, or it is cut.
- Moving from solo to small team is a hand-over of artifacts, not a change of process.
