# SDLC Enterprise Framework — CHANGELOG

**Framework**: SDLC Enterprise Framework 7.0.0-alpha
**Last Updated**: September 26, 2026 (v6.x and earlier history moved to archive)
**Owner**: @dttai71
**Consumer**: adopters choosing or pinning a release; maintainers writing release notes
**Review by**: 2026-12-26

Full version history for v6.5.0 and earlier lives in
[`archive/v6/CHANGELOG-v6.md`](archive/v6/CHANGELOG-v6.md), unmodified. This keeps the live
tree small; it does not hide anything — the repository is public, so the archive folder and git
history remain readable.

## Unreleased

| Change | Detail |
|---|---|
| Script | `scripts/check-rules-v7.sh` → `scripts/check-rules.sh`; label `gate=check-rules` |
| Workflows | `v7-gate.yml` → `version-declared.yml` · `v7-rules-gate.yml` → `rules.yml` · `v7-gates-product.yml` → `product-gates.yml` (reusable; callers pinned to a SHA keep working, re-pins use the new file name) |
| Rule-table heading | `## Rules v7` → `## Rule register`. The old heading, and the older Vietnamese one, are still read with a deprecation notice until 2026-12-31. Not `## Rules`: the deadline gate scans every `.md`, and `MIGRATION-MAP.md` already has a `## Rules` section |
| Policy-repo file | `rules-v7.md` → `rules.md` (old name read until 2026-12-31) |
| Titles | old file numbers and "v7" removed from H1 titles and from three headings (headings are link anchors) |
| New rule NAME-1 (ADVISORY) | `scripts/rule-no-version-in-names.sh` counts version numbers in live file and folder names and in Markdown headings; first count 3, all in `DEPRECATION-POLICY.md` |
| New rule DOC-2 (MACHINE) | `scripts/check-doc-ownership.sh`: every live doc names an **Owner**, a **Consumer** and a **Review by** date that has not passed. All 19 live docs filled in; count 0 on landing. Entered at MACHINE by a recorded exception (CEO, 2026-09-26): it replaces a gate that already blocked, so there is no gap; the exception is written into `practices/lessons-to-rules.md` |
| Doc count no longer blocks | DOC-1 keeps the >40 warning; the >60 hard ceiling is removed. `count=` now reports docs over the threshold (was the total, which the deadline gate would have read as 19 violations on 2026-10-25) |
| New `policies/` | `policies/artifact-lifecycle.md` replaces `DEPRECATION-POLICY.md` (v6.3, still marked ACTIVE; now archived): status decided by validity and a successor, not by age or version; statuses, transitions, deletion only for harmful content, archive payload never edited |
| Archive navigation | `archive/README.md` and `archive/INDEX.md` are living navigation and were corrected (`10-Archive`, `v7/`, "≤30 docs", removed shims); every other file in `archive/` stays byte-identical |
| Lifecycle | a product covers the ten questions in proportion to risk; a change revisits only the questions it affects; evidence (README, issue, ADR, PR, CI run, deploy record) rather than a document per stage; one line states a "no" |
| Contradiction removed | "archived documents gain a header" (standards) contradicted "archive is not edited"; archived files are now never edited, successors live in `MIGRATION-MAP.md` |
| CONTRIBUTING | 7-pillar review criteria, `CONTENT-MAP.md` and pillar scopes replaced by the folder-per-kind taxonomy; DCO stated as it is (external contributors; not checked by CI) |
| SECURITY | supported versions 7.x; release tags stated as annotated, not GPG-signed (the earlier "signed" claim was not true); normative folders updated |
| CHANGELOG header | company name and role titles removed (vendor-neutral public repo) |

## Layout change — 2026-09-26 (in tag `v7.0.0-alpha`): layout by kind of document; stages, project structure, documentation standards restored

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

