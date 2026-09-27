# Migration map: AI engineering

> Who reads this: whoever finds an old document in `archive/` and asks "what replaced this?", and whoever brings old knowledge into this part of the live tree.
> When: before rewriting anything from the archive, and after every harvest into this area.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: readers of `archive/` asking where a v6 agent-practice source went; authors harvesting into `ai-engineering/`
**Review by**: 2026-12-26

Harvest rows whose first live successor is in `ai-engineering/`. Rules, outcome vocabulary and the index of all row files: [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

| Source (in `archive/`) | Outcome | Live successor | Retired concepts |
|---|---|---|---|
| `v6/03-AI-GOVERNANCE/03-Planning-Mode-Principle.md` | PARTIALLY_ADOPTED | [`ai-engineering/context-and-hats.md`](../ai-engineering/context-and-hats.md#plan-before-code) | the MANDATORY / RECOMMENDED / OPTIONAL levels and the >50-line, >3-file, <15-line thresholds (size is gameable, as v6 itself said; kept: risk triggers the plan, skip when the diff fits in one sentence); "agentic search beats retrieval" as a rule (a tool choice, unmeasured); per-tool plan commands; kept: explore → plan → a person approves → execute, now required only on the risk floor |
| `v6/04-AI-TOOLS-LANDSCAPE/best-practices-2026/01-planning-mode.md` | PARTIALLY_ADOPTED | [`ai-engineering/context-and-hats.md`](../ai-engineering/context-and-hats.md#plan-before-code) | parallel explorer subagents and the `PlanningContext` schema, similarity percentages, "90% reduction in pattern violations" (no source), the generator validating its own output against the plan (current practice: an independent reviewer checks the diff against the plan); kept: read similar code, the binding decisions and the tests before planning |
