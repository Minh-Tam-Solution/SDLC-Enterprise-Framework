# Scripts

Moved here from `05-Templates-Tools/07-Scripts/` (F4, 2026-09-25) — English kebab-case,
verb-first names (see [CONTRIBUTING.md](../CONTRIBUTING.md) "Script naming"). The Rules v7
table (which script enforces what, and why) lives in `v7/01-rule-contract.md`, not here.

| Script | What it does |
|---|---|
| `check-rules-v7.sh` | Rules v7 Contract gate — reads `v7/01-rule-contract.md`, runs each rule's `cmd`, tallies pass/violation/unmeasurable. |
| `check-version-declared.sh` | Checks whether each doc declares which Framework version it was verified against (Convention A). |
| `rule-no-swallowed-stderr.sh` | Rule L2 — forbids `2>/dev/null` in `scripts/` unless listed in `.mien-nuot-stderr` with an expiry. |
| `rule-git-grep-no-word-boundary.sh` | Rule L4 — forbids `\b` in `git grep -E` (it silently matches nothing without `-P`). |
| `check_doc_headers.py` | Audits a `/docs` tree for Part 5.1 document headers (Version/Date/Status/Authority). |
| `compliance_sdlc_validator.py` | Primary SDLC 6.3.1 validator — 7-Pillar + 2-Section architecture. |
| `compliance_design_thinking_validator.py` | Pillar 0 validator — 5-phase Design Thinking methodology. |
| `compliance_sdlc_scanner.py` | Backward-compatible wrapper around the SDLC validator. |
| `quickstart_solo_setup.py` | Scaffolds a new project for a solo developer (2 days → 10x). |
| `migrate-legacy-to-archive.sh` | RFC-001 migration tool — moves legacy docs into `10-archive/{NN}-Legacy/`. |

Run `./selftest-all.sh` to run `--selftest` on every script here that supports it.

Two deprecated shims remain at the old path until 2026-12-31:
`05-Templates-Tools/07-Scripts/kiem-luat-v7.sh` and `kiem-nghiem-phien-ban.sh`.
