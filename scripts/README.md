# Scripts

**SDLC Framework Version**: 7.0.0

English kebab-case, verb-first names (see [CONTRIBUTING.md](../CONTRIBUTING.md)). The Rules v7
table (which script enforces what, and why) lives in [`v7/01-rule-contract.md`](../v7/01-rule-contract.md), not here.
Gate scripts follow the exit-code contract there: `0` pass · `1` cannot measure · `2` violation, last stdout line is the label.

| Script | What it does |
|---|---|
| `check-rules-v7.sh` | Rules v7 runner — reads `v7/01-rule-contract.md`, runs each row's `cmd`, tallies pass/violation/unmeasurable. |
| `check-advisory-deadline.sh` | Rule C21-4 — every `ADVISORY` row carries a counter (`count=`) and a `deadline=`; overdue with count > 0 is a violation. |
| `check-doc-count.sh` | Rule DOC-1 — live docs outside `10-Archive/` and `templates/`: >40 advisory, >60 blocks. |
| `check-version-declared.sh` | Pending C21-5 — checks whether each doc declares which framework version it was verified against (Convention A). |
| `check-pr-approver.sh` | `PRODUCT_CI` sample — a PR has a valid approval from a login in the base commit's approvers file; used by `v7-gates-product.yml`. |
| `rule-no-swallowed-stderr.sh` | Rule L2 — forbids `2>/dev/null` in `scripts/` unless listed in `.stderr-exemptions` with an expiry. |
| `rule-git-grep-no-word-boundary.sh` | Rule L4 — forbids `\b` in `git grep -E` (it silently matches nothing without `-P`). |
| `selftest-all.sh` | Runs `--selftest` on every script here that supports it. |
| `check_doc_headers.py` | v6 tool: audits a `/docs` tree for document headers (Version/Date/Status/Authority). |
| `compliance_sdlc_validator.py` | v6 tool: 7-Pillar + 2-Section validator (SDLC 6.3.1). |
| `compliance_design_thinking_validator.py` | v6 tool: Pillar 0 validator — 5-phase Design Thinking. |
| `quickstart_solo_setup.py` | v6 tool: scaffolds a new project for a solo developer. |

Two deprecated shims remain at the old path until 2026-12-31:
`05-Templates-Tools/07-Scripts/kiem-luat-v7.sh` and `kiem-nghiem-phien-ban.sh`.
