# SDLC Enterprise Framework

**Version**: 7.0.0-alpha | **Status**: ALPHA | **Date**: 2026-09-25 | **License**: MIT

> Who reads this: anyone deciding whether to adopt the framework, or opening this repo for the first time.
> When: before anything else. It takes ten minutes; the core is in [`02-Core-Methodology/`](02-Core-Methodology/README.md).

## What v7 is

1. A methodology for building software with AI agents and a few people — often one.
2. You own four assets. Vendors supply the rest: agents, models, runtimes, in-session orchestration.
3. Rules sit in three classes. Only deterministic checks block.
4. Controls scale with the risk of the thing being built, not with team size.
5. A rule names a runnable command and the real incident (burn case) that justifies it.
6. A rule without a command is reference material, not a rule.
7. Gates start ADVISORY with a counter and a deadline. They move up only on measured rates.
8. Incidents flow back into rules through one path ([`02-Core-Methodology/06`](02-Core-Methodology/06-lessons-to-rules.md)).
9. The framework gates itself in CI: doc count, rule tables, version declarations.
10. Promise: fewer rules, more of them enforced. Every section says what it shortens.

## The four assets you own

| Asset | What it is | Where it lives |
|---|---|---|
| **Policy** | tiers, rules, hats (role files), approvers | one policy repo ([`02-Core-Methodology/05`](02-Core-Methodology/05-adoption.md)) |
| **Repo knowledge** | domain context an agent needs: `AGENTS.md`, pointers to sources | each product repo |
| **Runnable gates** | scripts with exit codes 0/1/2 and a `--selftest` | `scripts/` here; the policy repo |
| **Eval set** | fixed cases with a published taxonomy, to compare agents and configs | the policy repo |

Everything else is rented: agent CLIs, subagents, skills, hooks, models, CI runners.
Adapters to them are generated and disposable. The policy is not.
*Shortens:* you build and maintain nothing a vendor already ships.

## Tier by risk of the artefact, not headcount

| Tier | Any one of these, derived from evidence | Skip risk if under-tiered |
|---|---|---|
| **LITE** | no production deploy · the only user is the author · no real data | low — a sandbox breaks |
| **STANDARD** | real internal users · `git revert` restores state · no money, customer or personnel data | colleagues blocked for hours |
| **PROFESSIONAL** | others decide on its numbers or commands · schema migrations on live data · users outside the team | wrong numbers drive decisions for a cycle; code rollback cannot undo a migration |
| **ENTERPRISE** | money path · customer or personnel PII · accounting or contracts · irreversible side-effects | money lost, data leaked, invoices issued — not undoable |

- Tier = max(repo evidence, declared service metadata, deploy evidence). Declare up only; below evidence is a violation.
- One person building ENTERPRISE gets ENTERPRISE gates. Three people building a sandbox get no ritual.
- Detail: [`02-Core-Methodology/02-tiers.md`](02-Core-Methodology/02-tiers.md).

## Three classes

| Class | Definition | On failure |
|---|---|---|
| `MACHINE` | deterministic; same input, same result; no judgement | blocks (fail-closed) |
| `REVIEW` | a named reviewer judges defined evidence | flags, does not block |
| `ADVISORY` | a lens; no pass/fail criterion | counted, with a deadline |

A probabilistic model is **never** `MACHINE`, however accurate. It adds a differently-blind check. It never replaces a deterministic one.

## Gate contract

Every gate is a script you own. Exit `0` = pass. Exit `1` = cannot measure — the default code of anything that crashes lands here, so a crash is never reported as a violation. Exit `2` = violation, and the script must return it on purpose. `≥3` is reserved. No `exit $?` that passes another tool's code through. The last stdout line is a label: `result=pass|insufficient_evidence|violation gate=<id> reason=<slug> [fix=…]`. Every gate ships `--selftest` with at least one red case that must fail and one green case that must pass. A gate nobody has made red is unmeasured, not green. Full contract and rule table: [`02-Core-Methodology/01-rule-contract.md`](02-Core-Methodology/01-rule-contract.md).

## Adopt in a repo

1. **Policy repo.** One repo holds tiers, rules, hats, approvers, gates. Product repos pin a release tag; generated files record the resolved SHA.
2. **Generated adapters.** `adapters/gen.sh` writes the vendor files (for example Claude Code and Qwen Code settings) from the policy. A hand edit is drift; CI catches it.
3. **Reusable workflow.** Product CI calls the policy repo's workflow at the pinned ref. The tier comes from the policy, never from an input the product sets.

Day one for a developer: clone, open the agent CLI. Nothing to remember. Detail: [`02-Core-Methodology/05-adoption.md`](02-Core-Methodology/05-adoption.md).

## Layout of this repo

| Path | Holds |
|---|---|
| `02-Core-Methodology/` | the core: principles and gates (00–06), stage lifecycle, project structure and documentation standards (07–09), the risk-floor path list — start at [`02-Core-Methodology/README.md`](02-Core-Methodology/README.md) |
| `05-Templates-Tools/` | copy-and-edit templates: agent context (PREAMBLE, SOUL) and project files (sprint, roadmap, ADR, spec) |
| `scripts/` | gate scripts, each with `--selftest` |
| `.github/workflows/` | CI that gates this repo, and a reusable workflow for product repos |
| `10-Archive/` | v6.x and earlier, read-only |

Website: the v6 site remains at its last deployment; v7 has no site (no new components).

## Lineage

v7 is the **third generation** of one methodology, not a new framework. The goals never changed: know what each member (human or AI) is doing, know what they have done, coordinate them.

| Generation | How it tried | What happened |
|---|---|---|
| 1 (v1–v5) | documents and stages describe the process | people had to remember it |
| 2 (v6.x) | platforms routed work through custom software (orchestrator, agent gateway) | vendors shipped execution; the control plane left was friction, and usage went to zero |
| 3 (v7) | read the traces work already leaves (PRs, CI, deploy logs); build only policy, gates, eval, repo knowledge | this repo |

- **What generation 1 got right stays.** The ten stages, the `docs/00–09` project layout and the documentation standards are kept, shortened, in `02-Core-Methodology/07`–`09`. Generation 3 adds gates that check them instead of relying on memory.
- v6.x archived 2026-09-25: 189 live files → target ≤30. The history stays in [`CHANGELOG.md`](CHANGELOG.md).
- **Legacy note rule.** Archive, never delete. An archived file keeps its content unmodified and gets one legacy note naming its successor. A file that changes meaning without a legacy note breaks the past silently — no later gate catches that.
- **Size rule.** Live docs >40 is flagged, >60 blocks ([`scripts/check-doc-count.sh`](scripts/check-doc-count.sh)). Each doc ≤150 lines. See [`CONTRIBUTING.md`](CONTRIBUTING.md).
