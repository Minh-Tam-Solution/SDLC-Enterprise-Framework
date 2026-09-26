# Migration map

> Who reads this: whoever finds an old document in `archive/` and asks "what replaced this?", and whoever brings old knowledge back into the live tree.
> When: before rewriting anything from the archive, and after every change that moves content between the archive and the live tree.

**SDLC Framework Version**: 7.0.0

*Shortens:* the search for where an old rule went, and the temptation to rewrite an old document instead of harvesting what is still true in it.

## Rules

- `archive/` is not edited. What happened to an archived document is recorded here, one row per source.
- Knowledge is harvested, not files: take the claims that are still true, merge them into the live document that owns the topic, record the row.
- Outcome is one of: `ADOPTED` (the substance lives on) · `PARTIALLY_ADOPTED` (some claims live on; the rest is listed as retired) · `SUPERSEDED` (a different live document answers the same question) · `RETIRED` (no longer true or no longer needed) · `HISTORICAL_ONLY` (kept as record, never in force again).
- A source with no row has not been reviewed yet. That is the default for most of `archive/v6/`.

## Map

| Source (in `archive/`) | Outcome | Live successor | Retired concepts |
|---|---|---|---|
| `v6/02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md` | PARTIALLY_ADOPTED | [`core/lifecycle.md`](core/lifecycle.md) | stage dependency YAML matrix, artifact SHA256 integrity per stage, evidence vault |
| `v6/02-Core-Methodology/Documentation-Standards/SDLC-Project-Structure-Standard.md` | PARTIALLY_ADOPTED | [`standards/project-structure.md`](standards/project-structure.md) | legacy folder-name aliases (`docs/why/` …), mandatory `docs/00–09` (now recommended) |
| `v6/02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md` | PARTIALLY_ADOPTED | [`standards/documentation.md`](standards/documentation.md) | per-language naming tables, migration-document header |
| `v6/05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md` | PARTIALLY_ADOPTED | [`standards/documentation.md`](standards/documentation.md) · [`templates/project/SPEC-template.md`](templates/project/SPEC-template.md) | reviewers/approver/effort/priority as mandatory front matter; single schema for specs and ADRs |
| `by-version/v4.5/09-Documentation-Standards/FILE-HEADER-STANDARDS-SDLC-4.5.md` | PARTIALLY_ADOPTED | [`standards/documentation.md`](standards/documentation.md#header-of-a-source-file) | framework version, approval, "authenticity" and business-value lines in code headers |
| `v6/05-Templates-Tools/08-Project-Templates/Planning-Hierarchy-*.md` | PARTIALLY_ADOPTED | [`templates/project/`](templates/project/README.md) | separate phase and backlog templates (phase = roadmap section; backlog = issue tracker) |
| `by-topic/ai-governance-v7-retired/08-Governance-Decision-Matrix.md` (risk classification table) | PARTIALLY_ADOPTED | [`controls/risk-floor-paths.md`](controls/risk-floor-paths.md) | the rest of the decision matrix |
| `v6/03-AI-GOVERNANCE/21-V7-RULE-CONTRACT.md` | SUPERSEDED | [`controls/rule-contract.md`](controls/rule-contract.md) | — |
| `v6/CHANGELOG-v6.md` | HISTORICAL_ONLY | [`CHANGELOG.md`](CHANGELOG.md) (from 7.0.0) | — |

## Next to harvest

Engineering and organisation standards first, AI-specific content after — tools change faster than engineering practice. Candidates named in review: systems thinking, design thinking, ship-useful, SSOT, security gates, testing artifacts and definition of done, observability, change management, team collaboration and hand-over, crisis-to-pattern (merges into [`practices/lessons-to-rules.md`](practices/lessons-to-rules.md)).
