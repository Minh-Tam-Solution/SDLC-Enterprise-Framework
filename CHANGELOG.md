# MTS SDLC Framework - CHANGELOG

**Framework**: SDLC 7.0.0-alpha Enterprise Framework
**Maintained By**: CEO + CPO + CTO Leadership
**Last Updated**: September 26, 2026 (v6.x and earlier history moved to archive)

Full version history for v6.5.0 and earlier lives in
[`archive/v6/CHANGELOG-v6.md`](archive/v6/CHANGELOG-v6.md), unmodified. This keeps the live
tree small; it does not hide anything — the repository is public, so the archive folder and git
history remain readable.

## Unreleased — 2026-09-26 (layout by kind of document; stages, project structure, documentation standards restored)

| Change | Detail |
|---|---|
| No version and no numbers in top-level paths | `v7/` split by kind of document: `core/` (constitution, lifecycle), `controls/` (rule contract, tiers, gates, risk-floor paths), `standards/` (project structure, documentation), `ai-engineering/` (context and hats), `adoption/`, `practices/` (lessons to rules). File-name numbers dropped; reading order is in the README. `templates/` → `templates/agent/` + `templates/project/`; `10-Archive/` → `archive/`. The version lives in each file's field, git tags and here |
| Restored, shortened | `core/lifecycle.md` (ten stages, stage gates G0.1–G4, exit evidence and signer by tier), `standards/project-structure.md` (`docs/00–09` as the **recommended** layout; root and planning files per tier), `standards/documentation.md` (file names, document header, separate spec and ADR front-matter schemas — issue #17, source-file header — issue #18) |
| Project templates | `templates/project/`: docs tree command, current sprint, sprint index, roadmap, ADR, spec |
| Archive rule | archived files are no longer edited; successors are recorded in `MIGRATION-MAP.md` (outcome per source: adopted, partially adopted, superseded, retired, historical only) |
| Consumers | pinned SHAs keep working; re-pins use the new paths, e.g. `controls/risk-floor-paths.md` (was `v7/risk-floor-paths.md`) |
| Shims removed early | `05-Templates-Tools/07-Scripts/kiem-luat-v7.sh` and `kiem-nghiem-phien-ban.sh` (announced for removal 2026-12-31) are removed: no CI, script or repo calls them; call `scripts/check-rules-v7.sh` and `scripts/check-version-declared.sh`. No file name outside `archive/` is in Vietnamese |

## Version 7.0.0-alpha — 2026-09-25 (third generation: v6.x archived, core rewritten)

| Change | Detail |
|---|---|
| v6.x archived | 189 live files move to `10-Archive/v6/` unmodified, with legacy notes; target ≤30 live docs |
| Core rewritten | `v7/00`–`06` + new root README: four assets, three rule classes, tiers by risk of the artefact (not team size), gate contract (exit 0/1/2 + label + selftest), adoption, lessons-to-rules |
| Doc-count gate | `scripts/check-doc-count.sh` — live docs >40 advisory, >60 blocks |
| Naming | English only; kebab-case files; verb-first scripts (`check-*`, `rule-*`); each doc ≤150 lines ([CONTRIBUTING](CONTRIBUTING.md#naming--size)) |

### Archived first (11 items — v7 archive lot 1, 2026-09-25)

Each item below was tied to a governance engine, index, or config that has since been retired
or gone stale with zero readers.

- `03-AI-GOVERNANCE/08-Governance-Decision-Matrix.md` → `10-Archive/by-topic/ai-governance-v7-retired/` — described a retired governance engine; routed on the now-dropped Vibecoding Index, which conflicted with SPEC-0001's own definition.
- `03-AI-GOVERNANCE/09-Governance-Metrics.md` → same — KPIs on the same retired engine's state machine; none of its ~60 figures ship with a reproducible command.
- `03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md` → same — L0–L3 ladder scores manual artifact creation that mainstream AI CLIs now provide natively, and its L1–L3 labels now collide with v7's own orchestration-tier naming.
- `03-AI-GOVERNANCE/17-AGENTIC-OS-PATTERNS.md` → same — validation record for patterns "verified" by a reference platform that is now retired (0 requests in 33 days).
- `03-AI-GOVERNANCE/18-LLM-MODEL-STRATEGY.md` → same — 2 of 3 listed fallback models don't exist on the current host; cascade is now implemented at the gateway layer, not in this doc.
- `03-AI-GOVERNANCE/19-FEDERATED-PLATFORM-STANDARD.md` → same — 2 of the 4 named platforms are retired and a third closed its SDLC lane.
- `03-AI-GOVERNANCE/20-EVIDENCE-INTEGRATION-STANDARD.md` → same — API contract of a retired product (no running container); v7 evidence is git + CI logs only.
- `02-Core-Methodology/Governance-Compliance/gates.yaml` → same — frozen at 6.2.0 for 7 months, 0 scripts in this repo's `git log` history ever read it.
- `02-Core-Methodology/Governance-Compliance/anti-vibecoding.yaml` → same — same staleness as `gates.yaml`; replaced by `.github/workflows/v7-rules-gate.yml` + `scripts/check-rules-v7.sh`.
- `05-Templates-Tools/07-Scripts/compliance_sdlc_scanner.py` → `10-Archive/scripts/` — fails on every execution path (crash with no arguments; wrong filename with arguments); no CI or script calls it.
- `05-Templates-Tools/07-Scripts/migrate-legacy-to-archive.sh` → same — targets the `{stage}/99-Legacy/` scheme this repo's own `10-Archive/README.md` retired 2026-04-28.

### Added (archive lot 1)

- `03-AI-GOVERNANCE/risk-floor-paths.md` — generic, tool-agnostic risk-floor path list (`migrations/`, `auth/`, `tenant/`, `permissions/`, `billing/`, `payment/`, `infra/`, `secrets/`), extracted from `08-Governance-Decision-Matrix.md`'s Risk Classification table before that file was archived.

### v7 follow-ups (archive lot 2, 2026-09-26)

| Change | Detail |
|---|---|
| Risk floor live again | `risk-floor-paths.md` → `v7/risk-floor-paths.md`, linked from `v7/02` and `v7/05` |
| Archive lot 2 | the four v6.3.1 Python tools (`check_doc_headers.py`, `compliance_sdlc_validator.py`, `compliance_design_thinking_validator.py`, `quickstart_solo_setup.py`) → `10-Archive/v6/scripts/`; no v7 gate or CI ran them, two named internal products |
| Rule C21-5 | `check-version-declared.sh` is a Rules v7 row, `ADVISORY`, `deadline=2026-10-09`; it prints `count=<undeclared>` before its label |
| Approver independence | `check-pr-approver.sh` reads `bot:<login> operated_by=<human>` lines; an approval by the author's operator does not count; a listed bot with no operator ⇒ `1` |
| Website | the v6 site stays at its last deployment; v7 adds no site |

---

