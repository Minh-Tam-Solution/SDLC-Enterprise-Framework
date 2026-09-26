# 10-Archive: Centralized Legacy Content

**Status**: AI-NEVER-READ
**Last reorganized**: 2026-04-28
**Standard**: RFC-001 Legacy Document Organization

---

## v6.x — archived 2026-09-25 (legacy)

`v6/` holds the whole v6.x tree (Framework 6.5.0 and its amendments) exactly as it stood on
2026-09-25: moved with `git mv`, content unchanged. Its live replacement is [`../v7/`](../v7/README.md).

**Why it was archived, not revised:**
- v6 tiered projects by **team size**; v7 tiers them by **the risk of what is being built**.
- v6 reached **189 live docs** (502 with this archive). Nobody could say which were still true, and
  most "rules" had no runnable command behind them.
- v7 replaces it with a core of **≤30 live docs**, each rule backed by a script with a selftest
  (`scripts/check-doc-count.sh` keeps the count honest).

**Rules for this folder:** [`DEPRECATION-POLICY.md`](../DEPRECATION-POLICY.md) applies. Nothing in
`v7/`, `templates/`, `scripts/` or the root docs links into `10-Archive/`; to reuse a v6 idea, copy
the excerpt forward into a v7 doc and give it a command or mark it reference.

| Path in `v6/` | Files | What it was |
|---|---:|---|
| `01-Overview/` | 2 | executive summary, quick reference |
| `02-Core-Methodology/` | 18 | 7 pillars, 10 stages, tiers by team size, quality gates, spec standard |
| `03-AI-GOVERNANCE/` | 12 | AI governance principles; `21-V7-RULE-CONTRACT.md` (superseded by `v7/01`) |
| `04-AI-TOOLS-LANDSCAPE/` | 15 | per-tool guides |
| `05-Templates-Tools/` | 82 | spec templates, SASE artifacts, checklists, project templates (the two script shims in `07-Scripts/` stay live until 2026-12-31) |
| `06-Case-Studies/` | 12 | case studies |
| `07-Implementation-Guides/` | 19 | rollout guides |
| `08-Training-Materials/` | 13 | training material |
| `09-Continuous-Improvement/` | 4 | amendment catalogs, improvement guide |
| `site/` | 9 | the v6 website (static page; its deploy workflow is archived at `.github/workflows/pages.yml`) |
| `CONTENT-MAP.md`, `CLAUDE.md`, `.claude/`, `.coverage` | 4 | v6 content map, v6 agent guide and settings, a stray coverage file |

177 Markdown files in `v6/`.

---

## AI-NEVER-READ Directive

```yaml
directive: AI-NEVER-READ
reason: Contains archived, deprecated, and historical content
exception: User explicitly requests historical information
```

**AI assistants MUST NOT read content from this folder unless specifically requested by the user.**

---

## Structure (post-2026-04-28 reorganization)

Two top-level axes — **by version** for time-bound snapshots, **by topic** for topic-bound consolidations. The previous `0[0-9]-Legacy/` numbering scheme was retired because it had become inconsistent (multiple cleanup batches landed without consolidation, producing 7 differently-shaped subdirectories).

```
10-Archive/
├── README.md            # This file
├── INDEX.md             # Full file catalog
│
├── v6/                  # v6.x tree as of 2026-09-25 (see the section above)
│
├── by-version/          # Per-version snapshots (chronological)
│   ├── v1.x/            # June 2025 — initial Claude Code era
│   ├── v2.x/            # July 2025 — early iterations
│   ├── v3.x/            # July-Aug 2025 — enterprise features
│   ├── v4.0/            # August 2025 — design-first era
│   ├── v4.1/, v4.2/, v4.3/
│   ├── v4.4/            # Sept 2025 — emergency patches
│   ├── v4.5/            # Sept 2025 — universal patterns
│   ├── v4.6/            # Sept 24, 2025 — Zero Mock emergency
│   ├── v4.7/, v4.8/, v4.9/
│   ├── v5.0/            # Dec 2025 — governance + 4-tier
│   ├── v5.1.3/          # Deployment guides + 7-Pillar
│   ├── v5.2.0/          # AI Governance + Risk-Based Planning
│   ├── v5.3.0/          # Stage Dependencies + QA System
│   └── v6.2.0/          # Pre-consolidation snapshot
│
└── by-topic/            # Per-topic consolidations (atemporal)
    ├── ai-governance-v7-retired/   # v7 (Sep 2026): retired AI-governance docs + dead gates.yaml/anti-vibecoding.yaml
    ├── ai-tools-templates/         # Sprint 173 AI prompt templates (frozen)
    ├── code-review-consolidation/  # Sprint 173 code-review framework rollup
    ├── coderabbit-pilot-2025/      # CodeRabbit Oct 2025 pilot artifacts
    ├── deprecated-best-practices/  # Old AI-tools coordination patterns
    ├── deprecated-rfcs/            # Sunset RFCs
    ├── historical-documents/       # Legacy READMEs, version history, platform lessons
    ├── legacy-scripts/             # Old compliance + governance scripts
    ├── openspec-analysis-2026/     # OpenSpec compatibility analysis
    ├── orchestrator-specs/         # Sprint 173 Orchestrator specs
    ├── proposals/                  # Old proposals + upgrade plans
    ├── sase-deprecated/            # Deprecated SASE artifacts
    ├── sdlc-4.8-approval-docs/     # 4.8 approval workflow records
    ├── sprint-117-poc/             # Sprint 117 spec-first POC
    └── tool-guides-2026/           # Per-tool guides (Claude Code, Cursor, Copilot, ChatGPT, Gemini)
```

A third top-level location, **`scripts/`** (flat, not axis-organized), holds individually
retired automation scripts that don't belong to a version snapshot or a topic body of work —
see `scripts/` for the v7 (Sep 2026) additions.

See [INDEX.md](INDEX.md) for the full file catalog.

---

## Archive Policy

- **Move, don't delete** — Documents are archived, never deleted
- **Two-axis organization** — Choose `by-version/` for "this is what v4.5 shipped" and `by-topic/` for "this is the now-deprecated approach to X"
- **No active references** — Active docs (root docs, `v7/`, `templates/`, `scripts/`) do not link to archived content; if a citation is needed, copy the relevant excerpt forward and explain the historical context
- **Periodic review** — Quarterly cleanup cadence; at each major version, the prior version's normative content snapshots into `by-version/v{N.N}/`

---

## When to Add to Archive

| Situation | Destination |
|-----------|-------------|
| Major version cut → freeze old normative content | `by-version/v{N.N}/` |
| A topic-specific approach is deprecated → preserve the body of work | `by-topic/{topic-slug}/` |
| A pilot or POC ends → preserve evidence | `by-topic/{name-of-pilot}/` |
| A README or meta-doc is now historical | `by-topic/historical-documents/` |

---

## What NOT to Add

- Sprint plans, retros, or governance audit reports — those belong in active stage folders (`08-collaborate/retrospectives/`, `09-govern/audits/`, etc.) and follow their own retention policy
- Vendor-specific platform deployment configs — those belong in the implementing platform's own repo
- Personal notes, scratchpads, draft content — those belong on individual maintainer machines, not in the Framework repo

---

**Owner**: CTO Office
