# Scripts

**SDLC Framework Version**: 7.0.0

English kebab-case, verb-first names (see [CONTRIBUTING.md](../CONTRIBUTING.md)). The Rules v7
table (which script enforces what, and why) lives in [`02-Core-Methodology/01-rule-contract.md`](../02-Core-Methodology/01-rule-contract.md), not here.
Gate scripts follow the exit-code contract there: `0` pass · `1` cannot measure · `2` violation, last stdout line is the label.

| Script | What it does |
|---|---|
| `check-rules-v7.sh` | Rules v7 runner — reads `02-Core-Methodology/01-rule-contract.md`, runs each row's `cmd`, tallies pass/violation/unmeasurable. |
| `check-advisory-deadline.sh` | Rule C21-4 — every `ADVISORY` row carries a counter (`count=`) and a `deadline=`; overdue with count > 0 is a violation. |
| `check-doc-count.sh` | Rule DOC-1 — live docs outside `10-Archive/` and `05-Templates-Tools/`: >40 advisory, >60 blocks. |
| `check-version-declared.sh` | Rule C21-5 (ADVISORY) — checks whether each doc declares which framework version it was verified against (Convention A). |
| `check-pr-approver.sh` | `PRODUCT_CI` sample — a PR has a valid approval from a login in the base commit's approvers file; used by `v7-gates-product.yml`. |
| `rule-no-swallowed-stderr.sh` | Rule L2 — forbids `2>/dev/null` in `scripts/` unless listed in `.stderr-exemptions` with an expiry. |
| `rule-git-grep-no-word-boundary.sh` | Rule L4 — forbids `\b` in `git grep -E` (it silently matches nothing without `-P`). |
| `selftest-all.sh` | Runs `--selftest` on every script here that supports it. |

The v6 Python tools (`check_doc_headers.py`, `compliance_*_validator.py`, `quickstart_solo_setup.py`)
are archived in [`10-Archive/v6/scripts/`](../10-Archive/v6/scripts/).

Two deprecated shims remain at the old path until 2026-12-31:
`05-Templates-Tools/07-Scripts/kiem-luat-v7.sh` and `kiem-nghiem-phien-ban.sh`.
