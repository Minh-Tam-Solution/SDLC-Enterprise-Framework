# 10-Archive: Centralized Legacy Content

**Status**: AI-NEVER-READ
**Last reorganized**: 2026-04-28
**Standard**: RFC-001 Legacy Document Organization

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

See [INDEX.md](INDEX.md) for the full file catalog.

---

## Archive Policy

- **Move, don't delete** — Documents are archived, never deleted
- **Two-axis organization** — Choose `by-version/` for "this is what v4.5 shipped" and `by-topic/` for "this is the now-deprecated approach to X"
- **No active references** — Active docs (in `01-Overview/` through `09-Continuous-Improvement/`) should not link to archived content; if a citation is needed, copy the relevant excerpt forward and explain the historical context
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
