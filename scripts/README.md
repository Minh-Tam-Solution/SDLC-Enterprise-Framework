# Scripts

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: gate authors; maintainers of this repo's CI
**Review by**: 2026-12-26

English kebab-case, verb-first names (see [CONTRIBUTING.md](../CONTRIBUTING.md)). The rule
table (which script enforces what, and why) lives in [`controls/rule-contract.md`](../controls/rule-contract.md), not here.
Gate scripts follow the exit-code contract there: `0` pass · `1` cannot measure · `2` violation, last stdout line is the label.

| Script | What it does |
|---|---|
| `check-rules.sh` | Rule-contract runner — reads `controls/rule-contract.md`, runs each row's `cmd`, tallies pass/violation/unmeasurable. |
| `check-advisory-deadline.sh` | Rule C21-4 — every `ADVISORY` row carries a counter (`count=`) and a `deadline=`; overdue with count > 0 is a violation. |
| `check-doc-count.sh` | Rule DOC-1 (ADVISORY) — live docs outside `archive/` and `templates/`: >40 prints a warning; no hard ceiling. |
| `check-doc-ownership.sh` | Rule DOC-2 (MACHINE) — every live doc names an Owner, a Consumer and a Review-by date that has not passed. |
| `check-version-declared.sh` | Rule C21-5 (ADVISORY) — checks whether each doc declares which framework version it was verified against (Convention A). |
| `check-pr-approver.sh` | `PRODUCT_CI` sample — a PR has a valid approval from a login in the base commit's approvers file; used by `product-gates.yml`. |
| `rule-no-swallowed-stderr.sh` | Rule L2 — forbids `2>/dev/null` in `scripts/` unless listed in `.stderr-exemptions` with an expiry. |
| `rule-git-grep-no-word-boundary.sh` | Rule L4 — forbids `\b` in `git grep -E` (it silently matches nothing without `-P`). |
| `rule-no-version-in-names.sh` | Rule NAME-1 (ADVISORY) — counts version numbers in live file and folder names and in Markdown headings (a heading is a link anchor). Skips `archive/` and `CHANGELOG.md`. |
| `rule-no-new-secrets.sh` | Rule SECRET-1 (MACHINE) — no secret-shaped value in lines a change adds; `.secret-allowlist` holds dated debt; `--all` reports the whole tree. |
| `check-migration-class.sh` | Rule MIG-1 (ADVISORY, `PRODUCT_CI`) — classifies migrations expand/contract from their statements; counts expand labels on contract migrations; prints `class=` for the deploy log. |
| `selftest-all.sh` | Runs `--selftest` on every script here that supports it. |

The v6 Python tools (`check_doc_headers.py`, `compliance_*_validator.py`, `quickstart_solo_setup.py`)
are archived in [`archive/v6/scripts/`](../archive/v6/scripts/).
