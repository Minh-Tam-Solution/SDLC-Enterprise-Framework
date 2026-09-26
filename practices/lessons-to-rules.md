# Lessons to rules

> Who reads this: whoever closes an incident, writes a post-mortem, or wants a new rule.
> When: at incident close, at the monthly vendor radar, and when a user reports a problem.

**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: whoever closes an incident or proposes a rule
**Review by**: 2026-12-26

*Shortens:* the second time the same incident happens. A lesson that does not reach a rule is paid for twice.

## The path

```text
burn case → rule row (burn_case mandatory) → ADVISORY, counter + deadline → REVIEW → MACHINE
```

| Step | Exit condition |
|---|---|
| **Burn case** | a real incident with a price paid: hours, bad records, who was affected |
| **Rule row** | `id`, class, command, `burn_case` filled in ([`rule-contract`](../controls/rule-contract.md)); no burn case ⇒ no row |
| **ADVISORY** | the command prints `count=`, the row carries `deadline=`; thresholds published |
| **REVIEW** | violation rate < 20% (upper Wilson bound, [`gates`](../controls/gates.md)) |
| **MACHINE** | < 5% for 2 consecutive weeks |

Each "fail" leaves a trace: burn case → `burn_case` → the red case in `--selftest`. That is how "fix" does not repeat.

## Incident record: one field

Every closed incident or lesson carries:

```text
rule_ref: <rule id> | reference | none(<reason>)
```

- Measured by grep over closed records: records missing the field are counted in the weekly digest (`ADVISORY`, with a positive control — one record planted without it).
- Also report the share of `<rule id>` among all records. Otherwise everyone writes `none` and the count looks clean.

## Vendor radar

Vendors change how context loads, how hooks behave and which models exist — monthly.

- The radar is a **recurring dated row in the deadline ledger**, one owner, monthly. Missing it turns the ledger red; no separate tracker.
- Output: a research note → a trial with numbers before/after, named consumer → a policy release → regenerated adapters → one line to the team.
- Its test: the count of "the vendor already ships this and we do not use it" falls between two radars. Do not count docs rewritten.

## User feedback

- One issue label for user feedback. No process beyond that.
- Measure: issues **closed by the person who reported them**. Not PRs merged, not comments.

## How anyone proposes a rule

1. Open an issue with the `rule-proposal` label.
2. Give the burn case, the command that detects it, and the answer to "if it is wrong, what does a false positive cost?".
3. A PR adds the row at `ADVISORY` with a deadline. Nobody adds a row straight at `MACHINE`.

**Two exceptions, each recorded in the row.** A gate may enter at `MACHINE` when its count is 0 on the day it lands, the decision is named in its `burn_case`, and either (a) it *replaces* a gate that already blocks — starting lower would open a gap where nothing blocks — or (b) the harm it prevents cannot be undone, and its scope is narrow enough to stay quiet. The ladder exists so a gate is not switched on while violations are common; with none, it only delays protection. Uses: DOC-2 replacing the doc-count ceiling (a); SECRET-1, secrets in added lines (b) — both 2026-09-26.

## Never measure agent output as progress

Lines written, files created, PRs opened, tokens spent: these measure activity. Count outcomes — lead time to deploy, change-fail rate, rework within 48h, feedback issues closed by the reporter. A framework that rewards agent output grows back to 189 docs.
