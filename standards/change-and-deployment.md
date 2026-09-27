# Change and deployment

> Who reads this: whoever merges, releases, deploys, migrates a schema or rolls back — person or agent.
> When: before a change that reaches users, and when a deploy goes wrong.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: developers and agents shipping changes; whoever is on duty when a deploy fails
**Review by**: 2026-12-26

*Shortens:* the time from a merged change to users having it, and the time from a bad deploy to users being safe again.

Approval, deploy log, timed rollback, provenance and break-glass are defined in [`controls/tiers.md`](../controls/tiers.md) and [`controls/gates.md`](../controls/gates.md). This standard says how to change safely inside those rules; it does not repeat them.

## Small changes, short branches

| Practice | Why |
|---|---|
| Work in units finishable in hours to a few days; split larger ones | agents produce large diffs cheaply; small ones keep review and rollback cheap |
| Trunk-based: a branch lives hours to a day, merges to the main branch at least daily; no long-lived integration branch; by default no code freezes | parallel agent branches drift fast |
| A diff much larger than its ticket, or one that adds a dependency, is flagged for review | size is the cheapest signal that scope moved |
| Before shipping, compare the diff with the intent that authorised it: clean, extra work, or missing requirements — both can be true at once; each drift item is kept, reverted or deferred | work an agent "helpfully" added is still unreviewed work |
| Parallel sessions on one repo: disjoint files, a frozen shared contract, merge in dependency order, rebase on the latest main before each merge; check for unpushed work before deleting a branch | two agents editing one file silently overwrite each other |

## Change classes

| Class | Means | Process |
|---|---|---|
| Standard | low risk, a recorded procedure, done many times | pre-approved; the gates decide |
| Normal | anything else: features, schema, infrastructure | the tier's gates and, on risk-floor paths, a human ([`risk-floor-paths.md`](../controls/risk-floor-paths.md)) |
| Emergency | ships before the usual checks can finish | break-glass ([`gates.md`](../controls/gates.md)); an incident record and a review within 48 hours; the share of emergency changes is tracked |

**Default: continuous, small-batch delivery without a change approval board, blanket change windows or freezes.** External approval of every change slows delivery without making it safer; peer or AI review, CI, tests and monitoring do that job, and humans review the risk floor. **Exception:** an explicit regulatory or contractual constraint, or an active incident, may impose a window or a freeze — written down, with its end date.

## Before a deploy

- **Declare rollback triggers with thresholds before the deploy** — e.g. error rate, p95 latency, a broken critical function, a security defect, a severe user report. A probe compares the post-deploy numbers with them.
- **Prove recoverability before a state-changing deploy.** A restore has been timed recently enough to trust ([`core/lifecycle.md`](../core/lifecycle.md), stage 06). A contract or unknown migration also needs a restorable checkpoint taken for it and a runbook. No restore record means "cannot measure", not "fine".
- **A change to infrastructure or deploy behaviour updates the deploy guide and runbooks in the same change.**
- **Changes to shared infrastructure run the full test suite** (migrations, configuration, middleware, CI); a feature-scoped change may run only the affected suites.
- **Urgency waives nothing above.** A hotfix, a staging pass or pressure is not an exemption; "document after deploy" is refused.

## Schema and data

- **Expand, migrate, contract.** Never change or drop what the running version uses in the same release that stops using it: add the new structure alongside the old, move the data and the code, remove the old in a later release. Then every deploy's schema also serves the previous code, and a code rollback stays safe.
- **Migrations are scripts in version control**, and the model must match the migration history: regenerating migrations from the model gives an empty diff.
- **The machine classifies each migration** as *expand* (only statements on a known-safe list: new tables, indexes, nullable columns, inserts), *contract* (drops, renames, type changes, enum values, NOT NULL without default, rewrites of existing data) or *unknown* (anything it does not recognise) — [`scripts/check-migration-class.sh`](../scripts/check-migration-class.sh). While MIG-1 is advisory, automatic rollback follows only a deploy with no migration; any migration follows the human runbook ([`gates.md`](../controls/gates.md), deploy log and rollback). A diff under `migrations/` is on the risk floor either way.

## Flags and releases

- **A feature flag separates deploy from release.** Each flag records its intent, its rollback plan and an expiry date; a release flag lives days to weeks, not months. Test the artifact with the flag in both states.
- **A release is immutable.** A version number, once published, never points at different content; a fix is a new version. Moving or force-pushing a release tag is a defect.
- **Version what others depend on.** A public API declares its version and follows semantic versioning; a breaking change carries a record: from/to version, migration steps, rollback procedure, deprecation and removal dates.
- **Deprecate on an announced timeline:** mark deprecated → warn in the response → remove, with the dates published before the first step.
- **The deployed artifact comes from the reviewed commit.** Build in CI, record where and from what it was built, and deploy that artifact — not a local build.

## Rollout and rollback

- **Keep the previous version runnable** until the new one is verified.
- **Each rollout names its rollback method:** redeploy the previous release, switch traffic back, route away from the canary, or turn the flag off.
- **A canary is compared with an unchanged control on a few user-facing signals**, and is big and long enough to be conclusive. With too little traffic it proves nothing: use a flag or a timed watch against the declared triggers, and say "not measured" rather than "passed".
- **Rolling back a code-only deploy needs no approval.** Going forward again does. A deploy with a migration follows the human runbook.
- **After a rollback:** confirm service health, check that no data was lost (a reconciliation query where one exists), open an incident.
- **Hotfix:** the minimal fix now, the permanent fix next, the incident review within 48 hours — each with a row in the deadline ledger.
- Triage asks two questions before choosing a fix: *is data at risk?* and *can we roll back?*

## Measure delivery from the deploy log

Five numbers, all derived from the deploy log line ([`gates.md`](../controls/gates.md)) without extra reporting: change lead time, deployment frequency, change fail rate, failed-deployment recovery time, and **deployment rework rate** — deploys that were unplanned and caused by an incident. Mark each deploy `planned` or `unplanned(<incident>)` to get the last one.

Keep the deploy and change log as long as the risk requires: months for internal tools, years where accounting, contracts or regulators apply.

## Candidate rules

Each enters at `ADVISORY` through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md) once it has a burn case.

| Candidate | Command idea |
|---|---|
| diff size vs declared size; new dependency | `--shortstat` and manifest diff on the PR |
| migration class (MIG-1, now in the register) | `scripts/check-migration-class.sh` |
| model ↔ migration history | regenerate migrations, expect an empty diff |
| release tag never moves | compare each tag's target with the recorded one |
| flag expiry | flag registry with dates, checked like any deadline |
| rework rate | share of `unplanned` deploys in the log |

## Sources

From the archive: the rows for this standard in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

Current practice, each opened on the date shown:

- DORA — Working in small batches — <https://dora.dev/capabilities/working-in-small-batches/> (accessed 2026-09-26)
- DORA — Trunk-based development — <https://dora.dev/capabilities/trunk-based-development/> (accessed 2026-09-26)
- DORA — Streamlining change approval — <https://dora.dev/capabilities/streamlining-change-approval/> (accessed 2026-09-26)
- DORA — Database change management — <https://dora.dev/capabilities/database-change-management/> (accessed 2026-09-26)
- DORA — Software delivery performance metrics — <https://dora.dev/guides/dora-metrics/> (accessed 2026-09-26)
- Martin Fowler — Parallel Change (expand/contract) — <https://martinfowler.com/bliki/ParallelChange.html> (accessed 2026-09-26)
- Pete Hodgson — Feature Toggles — <https://martinfowler.com/articles/feature-toggles.html> (accessed 2026-09-26)
- Google SRE Workbook — Canarying Releases — <https://sre.google/workbook/canarying-releases/> (accessed 2026-09-26)
- Semantic Versioning 2.0.0 — <https://semver.org/> (accessed 2026-09-26)
- The Twelve-Factor App — Build, release, run — <https://12factor.net/build-release-run> (accessed 2026-09-26)
- Reproducible Builds — Definitions — <https://reproducible-builds.org/docs/definition/> (accessed 2026-09-26)
- SLSA v1.0 — Provenance — <https://slsa.dev/spec/v1.0/provenance> (accessed 2026-09-26)
