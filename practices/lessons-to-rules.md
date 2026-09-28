# Lessons to rules

> Who reads this: whoever closes an incident, writes a post-mortem, or wants a new rule.
> When: at incident close, when a vendor radar reports, and when a user reports a problem.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
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

- The radar's cadence, its owner and its review records live in the adoption kit, not here.
- Output: a research note → a trial with numbers before/after, named consumer → a policy release → regenerated adapters → one line to the team.
- Its test: the count of "the vendor already ships this and we do not use it" falls between two radars. Do not count docs rewritten.

**Tools that shape the workflow change under you** — the agent CLI, the code host, CI, a review bot, a model gateway.

- **Keeping up with them is the adoption kit's job, not the framework's:** the radar ends in a release of the policy repo, not in a change to this framework. The policy repo and its adapters ([`adoption`](../adoption/adoption.md#policy-repo-pattern)) say how today's tools do a practice; this framework says what the practice must achieve, and changes slowly. The kit treats such a tool like a dependency: a pinned version, moved after reading what the release changed ([Sources](#sources)). v6 kept tool profiles, a capability matrix and a monthly trend watch inside the framework; the archive holds one issue of the trend watch, its next one marked "queued".
- **A tool feature enters the framework only once it is a de-facto standard:** several independent vendors implement it, or an open specification exists — as for the `AGENTS.md` context file ([`context-and-hats`](../ai-engineering/context-and-hats.md#sources)). The harvest row or PR cites that evidence; until then the feature lives in the kit.
- **A claim that depends on tool behaviour names the version it was verified on and how**, as the loading table in [`context-and-hats`](../ai-engineering/context-and-hats.md) does. A version-free claim is about no version in particular. *Burn case:* a team lesson said an environment variable overrides every sub-agent's model setting. It had been true in older versions of the agent CLI, was false in the current one, and was taught as current until someone measured again. In another case a branch was read through one of the code host's two protection mechanisms and reported "unprotected"; the host enforces both side by side.

## User feedback

- One issue label for user feedback. No process beyond that.
- Measure: issues **closed by the person who reported them**. Not PRs merged, not comments.

## How anyone proposes a rule

1. Open an issue with the `rule-proposal` label.
2. Give the burn case, the command that detects it, and the answer to "if it is wrong, what does a false positive cost?".
3. A PR adds the row at `ADVISORY` with a deadline. Nobody adds a row straight at `MACHINE`.

**Exceptions are a contract, not a claim.** A rule may enter at `MACHINE` directly only under the two cases in [`controls/rule-contract.md`](../controls/rule-contract.md#entering-at-machine-directly) — a same-rule replacement for a gate that already blocks, or irreversible harm meeting all six conditions — and the case is named in its `burn_case`. "Our case is special" is not one of them.

## Never measure agent output as progress

Lines written, files created, PRs opened, tokens spent: these measure activity. Count outcomes — lead time to deploy, change-fail rate, rework within 48h, feedback issues closed by the reporter. A framework that rewards agent output grows back to 189 docs.

## Sources

Current practice, each opened on the date shown:

- Semantic Versioning 2.0.0 (a project must declare its public API; a backward-incompatible change to that API increments the major version, so the number says nothing about behaviour outside it) — <https://semver.org/> (accessed 2026-09-28)
- Keep a Changelog 1.1.0 (a curated list of notable changes per version, grouped as added, changed, deprecated, removed, fixed, security) — <https://keepachangelog.com/en/1.1.0/> (accessed 2026-09-28)
- GitHub Docs — About Dependabot version updates (update PRs on a schedule, carrying the changelog and release notes to review before merging; a cooldown after a release) — <https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates> (accessed 2026-09-28)
- Renovate Docs — Dependency Dashboard (one issue with the status of all updates; can require approval before a major update is proposed) — <https://docs.renovatebot.com/key-concepts/dashboard/> (accessed 2026-09-28)
- GitHub Docs — About rulesets (rulesets and branch protection rules work alongside each other and all applicable rules are enforced) — <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets> (accessed 2026-09-28); REST API — Rules for a branch (returns active ruleset rules; the page does not mention branch protection rules) — <https://docs.github.com/en/rest/repos/rules> (accessed 2026-09-28)
- Model Context Protocol — Specification 2025-06-18 (an open protocol with dated specification revisions; an example of a tool feature that became an open specification) — <https://modelcontextprotocol.io/specification/2025-06-18> (accessed 2026-09-28)
