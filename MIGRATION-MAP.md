# Migration map

> Who reads this: whoever finds an old document in `archive/` and asks "what replaced this?", and whoever brings old knowledge back into the live tree.
> When: before rewriting anything from the archive, and after every change that moves content between the archive and the live tree.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: readers of `archive/`; consuming repos fixing links to moved files
**Review by**: 2026-12-26

*Shortens:* the search for where an old rule went, and the temptation to rewrite an old document instead of harvesting what is still true in it.

## Rules

- `archive/` is not edited. What happened to an archived document is recorded in this map, one row per source, in the row file listed under [Map](#map).
- Knowledge is harvested, not files: take the claims that are still true, merge them into the live document that owns the topic, record the row.
- Outcome is one of: `ADOPTED` (the substance lives on) · `PARTIALLY_ADOPTED` (some claims live on; the rest is listed as retired) · `SUPERSEDED` (a different live document answers the same question) · `RETIRED` (no longer true or no longer needed) · `HISTORICAL_ONLY` (kept as record, never in force again).
- A source with no row has not been reviewed yet. That is the default for most of `archive/v6/`.

## Path map

Where each live file of the 7.0.0 layout (`d363387`) went: the layout change of 2026-09-26 (#35) and the version-neutral control names after `v7.0.0-alpha`. Links in consuming repos are fixed with this table. A reference pinned to a commit SHA keeps working; the next re-pin uses the new path.

**Folder rule:** `10-Archive/<path>` → `archive/<path>`, every file, byte-identical.

| Old path | New path | Note |
|---|---|---|
| `v7/00-constitution.md` | `core/constitution.md` | |
| `v7/01-rule-contract.md` | `controls/rule-contract.md` | |
| `v7/02-tiers.md` | `controls/tiers.md` | |
| `v7/03-gates.md` | `controls/gates.md` | |
| `v7/04-context-and-hats.md` | `ai-engineering/context-and-hats.md` | |
| `v7/05-adoption.md` | `adoption/adoption.md` | |
| `v7/06-lessons-to-rules.md` | `practices/lessons-to-rules.md` | |
| `v7/risk-floor-paths.md` | `controls/risk-floor-paths.md` | |
| `v7/README.md` | `README.md` | removed; its index is the README section "Layout of this repo" |
| `templates/PREAMBLE-example.md` | `templates/agent/PREAMBLE-example.md` | |
| `templates/SOUL-example.md` | `templates/agent/SOUL-example.md` | |
| `05-Templates-Tools/07-Scripts/README.md` | `scripts/README.md` | removed; it only pointed to `scripts/` |
| `05-Templates-Tools/07-Scripts/kiem-luat-v7.sh` | `scripts/check-rules.sh` | deprecated shim removed; call the successor |
| `05-Templates-Tools/07-Scripts/kiem-nghiem-phien-ban.sh` | `scripts/check-version-declared.sh` | deprecated shim removed; call the successor |
| `scripts/check-rules-v7.sh` | `scripts/check-rules.sh` | renamed after 7.0.0-alpha; the table heading is now `## Rule register` (`## Rules v7` read until 2026-12-31) |
| `.github/workflows/v7-gate.yml` | `.github/workflows/version-declared.yml` | renamed after 7.0.0-alpha |
| `.github/workflows/v7-rules-gate.yml` | `.github/workflows/rules.yml` | renamed after 7.0.0-alpha |
| `DEPRECATION-POLICY.md` | `policies/artifact-lifecycle.md` | archived to `archive/by-topic/historical-documents/DEPRECATION-POLICY.md` |
| `.github/workflows/v7-gates-product.yml` | `.github/workflows/product-gates.yml` | renamed after 7.0.0-alpha; callers pinned to a SHA keep working, re-pins use the new file |

Check — every file of the old layout that is gone is mapped (expected output: `0`):

```bash
BASE=d363387; git fetch -q origin
comm -23 <(git ls-tree -r --name-only "$BASE" | sort) <(git ls-tree -r --name-only HEAD | sort) |
  while IFS= read -r f; do
    case "$f" in 10-Archive/*) [ -e "archive/${f#10-Archive/}" ] && continue ;; esac
    grep -qF "| \`$f\` |" MIGRATION-MAP.md || echo "UNMAPPED $f"
  done | tee /dev/stderr | wc -l
```

## Map

One row per source, in the file for the live area the source feeds. A row goes in the file of the folder of its **first** live successor; a row with no successor (`RETIRED`) goes where the rule it contradicts, or the topic it would have fed, now lives. Columns in every file: source (in `archive/`) · outcome · live successor · retired concepts.

| Rows for sources that feed | File |
|---|---|
| `core/` — constitution, lifecycle, systems and design thinking | [`migration-map/core.md`](migration-map/core.md) |
| `controls/` and `policies/` — rules, gates, artifact lifecycle; the v6 changelog | [`migration-map/controls-and-policies.md`](migration-map/controls-and-policies.md) |
| `standards/` — every engineering standard | [`migration-map/standards.md`](migration-map/standards.md) |
| `ai-engineering/` — working with agents | [`migration-map/ai-engineering.md`](migration-map/ai-engineering.md) |
| `templates/` | [`migration-map/templates.md`](migration-map/templates.md) |

A live document can be a later successor in a row filed elsewhere; all rows that name it: `grep -n 'standards/testing.md' migration-map/*.md` (any live path).

A live area with no file yet (`adoption/`, `practices/`) gets one with its first row whose first successor is there; until then no source feeds it first.

Check — v6 sources that have no row yet (not reviewed):

```bash
git ls-files archive/v6/ | sed 's|^archive/||' | while IFS= read -r f; do
  grep -qF "| \`$f\`" migration-map/*.md || echo "$f"
done
```

A row that names its sources with a glob (`Planning-Hierarchy-*.md`) covers files the check still lists; read the output before trusting it.

## Next to harvest

Done 2026-09-26: security, testing, change and deployment, observability (four standards); systems thinking and design thinking (`core/`), ship-useful folded into the constitution. Batch 3: one home per fact (in `standards/documentation.md`), `standards/integration-and-data.md`, `standards/collaboration.md`, data classes in `standards/security.md`. Batch 4 (2026-09-27): plan before code (`ai-engineering/context-and-hats.md`), who answers for an agent's work (`standards/collaboration.md`), tools built by people who do not write code (`standards/security.md`), diagrams (`standards/documentation.md`). Batch 5 (2026-09-27): what earns a line in the always-loaded context file and where a repeatedly broken rule goes, briefing an agent (`ai-engineering/context-and-hats.md`), releases and what counts as breaking (`policies/artifact-lifecycle.md`). Batch 8 (2026-09-28): what earns an ADR (`standards/collaboration.md`); rows for `Module-01`, `Module-02`, `Module-07`, `Module-10`, `SDLC-Training-Materials.md`, the `BFlow-4.4-to-4.5` and `BFlow-52-Day-Journey` case studies and the case-study `README.md`. Next: `v6/03-AI-GOVERNANCE/01-AI-Human-Collaboration.md` and that folder's `README.md` (topic already owned by `standards/collaboration.md`; rows only), the specification sources (`SPEC-0001`, `SPEC-0002`, `SPEC-0004`, `SPEC-0005`, the three example specs), the sprint-planning guide, the remaining case studies and training modules.
