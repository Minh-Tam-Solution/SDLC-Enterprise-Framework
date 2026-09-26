# Core methodology

> Who reads this: anyone looking for a rule, a tier, a gate, a stage or a documentation standard.
> When: after the [root README](../README.md). Read in order; each file ≤150 lines.

**SDLC Framework Version**: 7.0.0

| # | File | Read it when |
|---|---|---|
| 00 | [Constitution](00-constitution.md) | before proposing anything |
| 01 | [Rule contract](01-rule-contract.md) | before writing a rule row or a gate script |
| 02 | [Tiers by risk](02-tiers.md) | setting up a repo; asking "does this need a human?" |
| 03 | [Gates](03-gates.md) | adding, switching on or being blocked by a gate |
| 04 | [Context and hats](04-context-and-hats.md) | writing `AGENTS.md`, a PREAMBLE or a hat |
| 05 | [Adoption](05-adoption.md) | bringing v7 to an organisation or repo |
| 06 | [Lessons to rules](06-lessons-to-rules.md) | closing an incident; proposing a rule |
| 07 | [Stage lifecycle](07-stage-lifecycle.md) | starting a project; asking "can this stage exit?" |
| 08 | [Project structure](08-project-structure.md) | creating a repo; deciding where a document or a sprint file goes |
| 09 | [Documentation standards](09-documentation-standards.md) | naming a file; writing a header, a spec, an ADR or a source-file header |
| — | [Risk floor paths](risk-floor-paths.md) | declaring a repo's risk-floor paths; "does this diff need a human?" |

Also: [`05-Templates-Tools/`](../05-Templates-Tools/) (agent and project templates) · [`scripts/`](../scripts/) (gates, each with `--selftest`).

Reading order for a first-time adopter: 00 → 02 → 05. For a gate author: 01 → 03. For a developer starting a repo: 07 → 08 → 09.

This folder is named for what it holds, not for a version: the framework version lives in each file's `SDLC Framework Version` field and in [`CHANGELOG.md`](../CHANGELOG.md), so the path survives the next major version.
