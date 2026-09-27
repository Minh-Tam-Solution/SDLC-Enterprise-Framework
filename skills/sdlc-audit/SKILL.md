---
name: sdlc-audit
description: Use to audit a product repo or a policy repo against the SDLC Enterprise Framework (SEF) — at adoption, before a release, at the quarterly recertification of a PROFESSIONAL or ENTERPRISE repo, or when asked "does this repo follow SEF?". Checks tier declaration against evidence, adoption (policy repo, adapters, approvers, agent identity), rule register and gate contract conformance, risk-floor paths, documentation headers and agent context. Reports findings with evidence; it changes nothing.
---

# SEF audit

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7. For a single stage gate use `sdlc-gate-check` instead.

Each check below says what to look at and which SEF file defines "right". Record every result as `found` (with path, command or CI run), `missing`, or `not measured` (with why). A check that found nothing needs a positive control before it counts as clean (`controls/gates.md` G1).

## Steps

1. **Scope.** Which repo, which ref (pull first), and whether it has a policy repo. Running a repo's gate scripts executes its code: ask before running anything outside SEF's own `scripts/`.
2. **Tier** — `controls/tiers.md`.
   - Declared tier (policy repo `projects.yaml`, `tier_scheme: v7-risk`) vs derived: max(repo evidence, declared metadata, deploy evidence). Path signals are matched by segment (`hr/` must not match `chrome/`).
   - Declared below derived is a violation; lowering a tier needs a recorded decision id.
   - PROFESSIONAL and ENTERPRISE: a quarterly recertification row in the deadline ledger.
3. **Adoption** — `adoption/adoption.md`.
   - Policy repo holds every file in the "Policy repo pattern" table; the rule table's heading is `## Rule register`.
   - Product pins a release tag; generated files record the resolved SHA; CI regenerates adapters and expects an empty diff; the reusable workflow takes no tier input from the product.
   - Agent identity: agents act as a least-privilege bot; the owner credential is not on the agent's machine; `.approvers` maps every agent identity `bot:<login> operated_by=<human>`; authority comes from the authenticated actor, never commit trailers.
4. **Rule register** — `controls/rule-contract.md`.
   - One table, columns `id | class | cmd | burn_case | run_scope`; every row has a burn case; `cmd` is the repo's own script, no shell operators; ADVISORY rows carry `deadline=` and their `cmd` prints `count=`.
   - Run SEF's runner against it, e.g. `bash <SEF>/scripts/check-rules.sh --root <policy repo> --table rules.md --run-scope PRODUCT_CI --l3`, and read the result per step 5.
   - A row that entered at `MACHINE` names case (a) or (b) of "Entering at MACHINE directly" in its burn case.
5. **Gate contract** — `controls/rule-contract.md` §1, `controls/gates.md`.
   - Each gate script: exit `0/1/2` on purpose, no `exit $?`, last stdout line `result=… gate=… reason=…` matching the exit code, `--selftest` with a red and a green case that pass, no `2>/dev/null` on commands whose result is evidence.
   - Gates are on the ladder (ADVISORY → REVIEW → MACHINE) with thresholds published before step 1; known debt sits in a skip file with owner and expiry.
   - Enforcement is in CI required checks, protected environments or deploy tags — not only agent hooks.
6. **Risk floor** — `controls/risk-floor-paths.md`, `controls/tiers.md`.
   - Declared from PROFESSIONAL up (`standards/project-structure.md` "Root files"); contains every path and item the SEF file lists as never downgraded — compare against that table, do not work from memory; a repo adds paths, never removes them.
   - Merged diffs touching the floor had a human approver who is neither the author nor the author's operator (`controls/gates.md` "Approver independence").
   - Data classes are declared by path in the policy repo, unlisted paths have a declared default, and restricted/no-ai paths are enforced at the OS boundary (`standards/security.md` "Data classes and model access").
7. **Documentation** — `standards/documentation.md`, `standards/project-structure.md`.
   - Living docs carry `SDLC Framework Version`, `Status`, `Owner`, `Consumer`, `Review by` (not passed). `bash <SEF>/scripts/check-doc-ownership.sh --root <repo>` gives a count; it scans `--root` (the repo root) and excludes only `archive/` and `templates/`, so a product repo's `docs/10-archive/` is counted — read it as indicative.
   - Source files from STANDARD up start with `Purpose:` and `Design:` (or `Covers:` in tests); `Design:` paths exist or say `none`; generated files, migrations and files under 20 lines are exempt (`standards/documentation.md` "Header of a source file").
   - Specs and ADRs use their own front-matter schemas; no version numbers, status words or person names in living file names or headings (`scripts/rule-no-version-in-names.sh --root <repo>` counts them, with the same archive caveat).
   - Required root and planning files for the tier exist; `current-sprint.md` moved with the last gate, ADR or release.
8. **Agent context** — `ai-engineering/context-and-hats.md`.
   - `AGENTS.md` (STANDARD up) points to sources instead of copying tables, counts or trees; the shared part stays small; blocking rules live in hooks/CI, not in context text.
9. **Proportion and outcomes** — `core/systems-thinking.md` "Measures get gamed", `practices/lessons-to-rules.md` "Never measure agent output as progress", `core/constitution.md` "Demand before surface".
   - Compare governance work with product work in recent merges; flag governance artifacts with no named consumer.
   - Progress is read from outcomes (lead time, change-fail rate, rework, feedback closed by the reporter), not from docs, checks or PRs added.

## Output

One table, most severe first: `check | result (found / missing / not measured / violation) | evidence (path, command + last line, CI run) | SEF file`. Then the tier line, and the three findings that most reduce risk if fixed. No compliance percentage: a score no decision moves on is dropped (`core/constitution.md`).

## Rules

- Read only. Do not fix during the audit; a fix is a separate PR.
- Every `violation` cites the command output or the file and line. Every `found` on a negative ("no secrets") cites its positive control.
- Do not audit against retired concepts (see `sdlc-framework`, "What SEF no longer has").
