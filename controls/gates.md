# Gates

> Who reads this: whoever writes, runs or switches on a gate — in this repo, in product CI, or on a server.
> When: before adding a gate, before moving one up a step, and when a gate blocks you.

**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: gate authors; this repo's CI; product CI
**Review by**: 2026-12-26

*Shortens:* the time between a bad change and someone noticing. And the gates people learn to ignore.

## Contract

Exit codes, the label line, `--selftest` and the rule table live in [`rule-contract.md`](rule-contract.md). In short: `0` pass · `1` cannot measure · `2` violation (deliberate) · last line `result=… gate=… reason=… [fix=…]`. This file does not repeat it.

## Three run scopes

A rule row declares where its command can run. The runner filters rows **before** running them; a command run in the wrong place is a false red.

| Scope | Runs in | Example |
|---|---|---|
| `FRAMEWORK_REPO` | CI of this repo | doc count, rule table check |
| `PRODUCT_CI` | CI of a product repo that adopts v7 | tier floor, adapter drift, approver check |
| `RUNTIME_PROBE` | the machine running the service | provenance, deploy-tree harness |

## The ladder — switch gates on by trajectory, not as a wall

A gate switched on while violations are common turns CI red on day one. It gets disabled within a day, and you lose the gate and the safe path with it.

| Step | State | Move up when |
|---|---|---|
| 1 | `ADVISORY` + counter, printed weekly, with a deadline | violation rate < 20% |
| 2 | `REVIEW` — flags, does not block | violation rate < 5% for 2 consecutive weeks |
| 3 | `MACHINE` — blocks | — |

- **Publish thresholds before step 1.** Setting them after seeing the numbers is grading yourself.
- **Rates use the upper Wilson 95% bound, not the point estimate.** With small n the bound stays high: 0 violations in 10 runs gives ≈28%, which fails "< 20%". Reaching "< 5%" with 0 violations needs ≥73 runs. A gate with few runs therefore **stays `ADVISORY` — by design, not by neglect.**
- A rate is a measurement, not a target. Adding rows whose command does not test what the rule says raises the rate and enforces nothing. Every command needs a red case that proves it catches the forbidden thing.

## G1–G4 — four rules about gates, including gates people run

| # | Rule | Burn case |
|---|---|---|
| **G1** | A negative result ("0", "clean", "not found") needs a positive control that shows the tool can see what it looks for. No control ⇒ write "not measured", not `0`. | a secret scan redacted its output, then a grep for the redaction marker returned 0; the real count was 49 |
| **G2** | A gate needs an output reserved for "cannot measure", separate from "measured and failed". Without it, it fails open — always towards clean. With it but mislabelled, people fix the wrong thing. | an error redirect swallowed a missing-library error; the gate blamed a config mismatch and two people fixed the wrong file |
| **G3** | Write a gate from the **definition**, not from an example. Every gate has a case that deliberately turns it red. Never red ⇒ green means unmeasured. | a duplicate-doc gate compared file names; real duplicates never share a name, so it was always green |
| **G4** | An `ADVISORY` gate has a counter and a deadline. At the deadline, if the count is still > 0: move to `REVIEW` or delete the rule. There is no third option. | an advisory finding sat in a green gate for weeks; people had learned not to read it |

## Catalog

One line each. Scripts are in [`scripts/`](../scripts/); a "pattern" row describes a gate products build against their own stack.

| Gate | Scope | Checks | Where |
|---|---|---|---|
| rule table | FRAMEWORK_REPO | every rule row runs; with `--l3`, every command has a passing `--selftest` and no `exit $?` | `scripts/check-rules.sh` |
| version declared | FRAMEWORK_REPO | which framework version each doc was checked against; counts, does not block | `scripts/check-version-declared.sh` |
| advisory deadline | FRAMEWORK_REPO | every `ADVISORY` row has `deadline=` and a `count=`; past deadline with count > 0 ⇒ 2 | `scripts/check-advisory-deadline.sh` |
| no swallowed stderr | FRAMEWORK_REPO | no error redirect to null in gate scripts without a dated exemption | `scripts/rule-no-swallowed-stderr.sh` |
| no version in names | FRAMEWORK_REPO | no version number in a live file or folder name, or in a Markdown heading (anchor); counts, does not block | `scripts/rule-no-version-in-names.sh` |
| doc ownership | FRAMEWORK_REPO | every live doc names an Owner, a Consumer and a Review-by date that has not passed; blocks | `scripts/check-doc-ownership.sh` |
| doc count | FRAMEWORK_REPO | live docs outside `archive/` and `templates/`: >40 advisory; no hard ceiling (a count is a smell, ownership is the gate) | `scripts/check-doc-count.sh` |
| PR approver | PRODUCT_CI | approver login ≠ author and ≠ the author's operator, listed in `.approvers`, approval on the current head SHA | `scripts/check-pr-approver.sh` |
| adapter drift | PRODUCT_CI | regenerating adapters at the pinned policy ref gives an empty diff | pattern |
| tier floor | PRODUCT_CI | declared tier ≥ tier derived from evidence ([`tiers`](tiers.md)) | pattern |
| provenance probe | RUNTIME_PROBE | the running code resolves to a deploy tree built from a merged SHA; no symlink, interpreter, cron entry, service unit, env var or config path points into a working tree; state dirs have the right owner and mode | pattern |
| deploy-tree harness | RUNTIME_PROBE | fast smoke checks (boot, import, config, DB, health) run **on the deploy tree** and block; the broad suite runs but does not block | pattern |
| deadline ledger | governance | every self-declared deadline closes as `done`, `dropped`, `superseded` or `extended→YYYY-MM-DD`, with a pointer to evidence that exists and is merged/closed/green; `extended` at most twice | pattern |

Known debt goes into a skip file with `expiry` and `owner`. The gate blocks **new** failures; known ones turn red at expiry. Break-glass is not for old debt.

## Approver independence

An approval counts only if the reviewer is neither the PR author nor the person who operates the author. Agents open PRs under bot identities, so `reviewer ≠ author` alone lets a person approve their own agent's work. The approvers file maps each agent identity to its operator (`bot:<bot-login> operated_by=<human-login>`); a listed bot with no operator is `1` (cannot measure), never a pass. The four identity layers apply ([`adoption`](../adoption/adoption.md)): authority comes from the authenticated actor the code host reports, and the operator mapping lives in the protected approvers file, read from the PR's base commit — never from commit trailers or from the PR under review.

## Break-glass

- A blocked deploy must be loud: a message to the team channel and an issue. A silent block becomes a deploy that silently never happened.
- **A terminal prompt is only the UI to ask for an override. It is not authorization** — an agent with a shell can type "yes".
- Authorization = an authenticated human from the approvers list, using a credential that does not exist on the agent's machine (e.g. a code-host approval with 2FA).
- One override covers **one SHA, one artifact digest, one deploy**. It has an expiry, opens an issue and requires a post-review.
- Rate-limited: >3 per repo per 14 days ⇒ review before the next deploy ([`tiers`](tiers.md)).

## Hooks nudge; CI enforces

Agent hooks are UX: they stop an agent early and cheaply. They are never the guarantee — they run on the machine the agent controls, and some modes bypass them. The enforcement points are CI required checks, protected environments and deploy tags. Do not read an agent's text to learn whether a gate blocked; read exit codes and denial records.

## Deploy log and rollback

Every deploy writes one line:

```text
{sha_before, sha_after, artifact_digest, migration, actor, approval_ref, result}
```

- It feeds the delivery numbers — lead time, deployment frequency, change fail rate, recovery time and rework rate ([`standards/change-and-deployment.md`](../standards/change-and-deployment.md)) — without anyone reporting anything. Add `planned` or `unplanned(<incident>)` to get the rework rate.
- Health red after restart ⇒ **automatic rollback only when `migration=false`**. Rolling code back onto a migrated schema breaks more than it fixes.
- "Health" here is the new release's own liveness and readiness, not the health of shared dependencies. A health check that calls the database would roll good code back during a database blip ([`standards/observability.md`](../standards/observability.md)).
- `migration=true` and health red ⇒ stop, alert loudly, follow the human runbook.
