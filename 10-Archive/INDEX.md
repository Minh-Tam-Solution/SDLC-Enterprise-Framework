# 10-Archive: Full File Catalog

**Generated**: 2026-04-28 (post-reorganization)
**Total files**: 425 (246 in `by-version/`, 176 in `by-topic/`, plus README + INDEX)

---

## by-version/ — Per-version snapshots

Each subdirectory holds the normative content as it shipped at that Framework version. Use this view when answering "what did v4.5 actually look like?"

| Version | Files | Era | Notes |
|---------|------:|-----|-------|
| `v1.x/` | 2 | June 2025 | Initial Claude Code era; bootstrap scripts only |
| `v2.x/` | 2 | July 2025 | Early iterations; bootstrap scripts only |
| `v3.x/` | 2 | July-Aug 2025 | Enterprise features intro; bootstrap scripts only |
| `v4.0/` | 10 | August 2025 | Design-first era starts; first comprehensive guides |
| `v4.1/` | 7 | August 2025 | Iteration on 4.0 patterns |
| `v4.2/` | 8 | August 2025 | Validation tooling expansion |
| `v4.3/` | 26 | August 2025 | Implementation guides + templates pillar |
| `v4.4/` | 42 | September 2025 | Full multi-folder snapshot (largest pre-Zero-Mock) |
| `v4.5/` | 17 | September 2025 | Universal patterns; pre-emergency |
| `v4.6/` | 23 | September 24, 2025 | **Zero Mock emergency** — the pivot |
| `v4.7/` | 29 | September 27, 2025 | Battle-tested pillars (post-Zero-Mock) |
| `v4.8/` | 26 | November 7, 2025 | Design Thinking enhancement |
| `v4.9/` | 4 | November 13, 2025 | 10-Stage Lifecycle complete |
| `v5.0/` | 4 | December 5, 2025 | Governance + 4-Tier Classification + industry best practices |
| `v5.1.3/` | 15 | December 24, 2025 | Project Structure Standard + 7-Pillar Architecture |
| `v5.2.0/` | 15 | January 22, 2026 | AI Governance Principles + Risk-Based Planning |
| `v5.3.0/` | 6 | January 2026 | Stage Dependencies + Quality Assurance System |
| `v6.2.0/` | 8 | March 2026 | Pre-consolidation snapshot before 6.3.0 cleanup |

**Total in by-version/**: 246 files across 18 version subdirectories.

**Note on coverage gaps**: v6.0.x and v6.1.x are not snapshotted in `by-version/` — those releases were tracked via CHANGELOG.md only, with no normative-content forks. v6.3.0 is the current active version (in `01-Overview/` through `09-Continuous-Improvement/`).

---

## by-topic/ — Per-topic consolidations

Each subdirectory holds a body of work on a specific topic that has been deprecated, superseded, or sunset. Use this view when answering "what was the old approach to X?"

| Topic | Files | What it contains |
|-------|------:|------------------|
| `ai-tools-templates/` | 36 | Sprint 173 AI prompt templates (frozen — superseded by Section 8 Unified Specification Standard) |
| `code-review-consolidation/` | 4 | Sprint 173 code-review framework rollup (Universal + Manual + Subscription-Powered playbooks) |
| `coderabbit-pilot-2025/` | 17 | CodeRabbit Oct 2025 pilot artifacts |
| `deprecated-best-practices/` | 1 | Old AI-tools coordination patterns (now in 04-AI-TOOLS-LANDSCAPE/best-practices-2026/) |
| `deprecated-rfcs/` | 2 | Sunset RFCs |
| `historical-documents/` | 29 | Legacy READMEs, version history, platform-specific historical lessons (BFlow, MTEP), pre-2026-04-28 archive organization metadata |
| `legacy-scripts/` | 29 | Old compliance + governance scripts (pre-Sprint-173 tooling) |
| `openspec-analysis-2026/` | 7 | OpenSpec compatibility analysis (informed v6.0.0 Section 8 Unified Specification Standard) |
| `orchestrator-specs/` | 1 | Sprint 173 SDLC Orchestrator specs (now lives in product repo, not Framework) |
| `proposals/` | 3 | Old proposals + 10-stage validator upgrade plan |
| `sase-deprecated/` | 3 | Deprecated SASE artifacts (superseded by AGENTS.md unification) |
| `sdlc-4.8-approval-docs/` | 28 | 4.8 approval workflow records (historical governance evidence) |
| `sprint-117-poc/` | 1 | Sprint 117 spec-first POC validation report |
| `tool-guides-2026/` | 15 | Per-tool guides (Claude Code, Cursor, Copilot, ChatGPT, Gemini) — superseded by 04-AI-TOOLS-LANDSCAPE/tool-profiles/ |

**Total in by-topic/**: 176 files across 14 topic subdirectories.

---

## How to use this index

- **Looking for a specific version's normative content?** → `by-version/v{N.N}/`
- **Looking for a deprecated approach to a topic?** → `by-topic/{topic-slug}/`
- **Looking for historical context (READMEs, version history)?** → `by-topic/historical-documents/`
- **Looking for old scripts or tooling?** → `by-topic/legacy-scripts/`

If a file you remember isn't where you expect, search the entire archive:

```bash
find 10-Archive -name "FILENAME-PATTERN*"
```

---

## Reorganization context (2026-04-28)

This index was generated as part of a one-shot consolidation of the previous `0[0-9]-Legacy/` numbering scheme (00, 01, 02, 03, 04, 05, 06, 09 — gaps at 07/08, with multiple cleanup batches having layered on top of each other without consolidation). The new two-axis structure (`by-version/` + `by-topic/`) was chosen because:

- The `0[0-9]-Legacy/` scheme had become inconsistent — 7 differently-shaped subdirectories
- File location no longer indicated meaningful semantic — files for the same SDLC version lived in different `0[0-9]-Legacy/` parents depending on which cleanup batch landed them
- Adopters reading the public Framework repo needed a single explainable mental model

See [README.md](README.md) for the full archive policy.
