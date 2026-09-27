---
name: sdlc-audit
description: Use to audit a product repo or a policy repo against the SDLC Enterprise Framework (SEF) — at adoption, before a release, at a tier's periodic recertification, or when asked "does this repo follow SEF?". Checks tier declaration against evidence, adoption (policy repo, adapters, approvers, agent identity), rule register and gate contract conformance, risk-floor paths, documentation headers and agent context. Reports findings with evidence; it changes nothing.
---

# SEF audit

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents auditing a product or policy repo against SEF; the person who asked for the audit
**Review by**: 2026-12-26

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7. For a single stage gate use `sdlc-gate-check` instead.

Each check says what to look at and which SEF section defines "right". The section is the checklist: read it at the revision you audit against and check every item it lists — do not work from memory or from an earlier audit. Record every result as `found` (with path, command or CI run), `missing`, `violation`, or `not measured` (with why). A result of "nothing found" counts only under `controls/gates.md` "G1–G4".

## Steps

1. **Scope.** Which repo, which ref (pull first), and whether it has a policy repo. Running a repo's gate scripts executes its code: ask before running anything outside SEF's own `scripts/`.
2. **Tier** — `controls/tiers.md` "Derivation". Read the declared tier (policy repo `projects.yaml`), derive the tier from the signals that section lists, and report any violation it defines. Then check the obligations `controls/tiers.md` "Per-tier controls" attaches to the derived tier (recertification included).
3. **Adoption** — `adoption/adoption.md` "Policy repo pattern": every path in its table exists and holds what the table says; every bullet below the table holds. `adoption/adoption.md` "Agent identity": check each mechanism row, using its red case where you can run it.
4. **Rule register** — `controls/rule-contract.md` §1 (row fields and what `cmd` may be), `controls/rule-contract.md` §3 (what an `ADVISORY` row must declare), `controls/rule-contract.md` "Entering at MACHINE directly" (what a row that skipped the ladder must name). Run SEF's runner against the register, e.g. `bash <SEF>/scripts/check-rules.sh --root <policy repo> --table rules.md --run-scope PRODUCT_CI --l3`, and read its result per step 5.
5. **Gate contract** — each gate script against `controls/rule-contract.md` §1 (exit codes, result line, self-test) and `controls/gates.md` "G1–G4"; run each `--selftest`. Each gate's state against `controls/gates.md` "The ladder". Where enforcement sits against `controls/gates.md` "Hooks nudge; CI enforces".
6. **Risk floor** — from which tier a declaration is required: `standards/project-structure.md` "Root files". Compare the declaration row by row with `controls/risk-floor-paths.md` "Paths that are never downgraded"; what a diff on the floor needs: `controls/risk-floor-paths.md` "Rule" — check it on recent merged diffs that touch the floor, with approvers judged by `controls/gates.md` "Approver independence". Data classes: every bullet of `standards/security.md` "Data classes and model access".
7. **Documentation** — `standards/documentation.md` "Header of a living document", `standards/documentation.md` "Header of a source file", `standards/documentation.md` "Front matter", `standards/documentation.md` "File names"; required files per tier: `standards/project-structure.md` "Root files" and `standards/project-structure.md` "Planning files". Counters: `bash <SEF>/scripts/check-doc-ownership.sh --root <repo>` and `bash <SEF>/scripts/rule-no-version-in-names.sh --root <repo>`. Both scan the whole `--root` and exclude only its top-level `archive/` (and `templates/` for ownership), so a product repo's `docs/10-archive/` is counted — read the counts as indicative.
8. **Agent context** — `ai-engineering/context-and-hats.md` "Three tiers": check the repo's always-loaded context file against each bullet there.
9. **Proportion and outcomes** — `core/systems-thinking.md` "Measures get gamed", `practices/lessons-to-rules.md` "Never measure agent output as progress", `core/constitution.md` "Demand before surface". Compare governance work with product work in recent merges; flag governance artifacts with no named consumer; read progress from the outcomes those sections name, not from artifacts added.

## Output

One table, most severe first: `check | result (found / missing / not measured / violation) | evidence (path, command + last line, CI run) | SEF file and section`. Then the tier line with the SEF revision read, and the three findings that most reduce risk if fixed. No compliance percentage: nothing is decided on it (`core/constitution.md` "No template before its first real instance").

## Rules

- Read only. Do not fix during the audit; a fix is a separate PR.
- Every `violation` cites the command output or the file and line. Every `found` on a negative ("no secrets") cites its positive control.
- Do not audit against retired concepts (see `sdlc-framework`, "What SEF no longer has").
