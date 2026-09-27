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
| `v6/03-AI-GOVERNANCE/05-Context-Management.md` | PARTIALLY_ADOPTED | [`ai-engineering/context-and-hats.md`](../ai-engineering/context-and-hats.md#three-tiers) | "AGENTS.md works everywhere" and `.claude/rules/` + imports as progressive disclosure (tools load context differently; see the table at the top of the successor); the 5-hop import limit; dynamic context posted as PR comments, a CLI overlay or an IDE extension (a retired product's channel; session state goes in the hand-over file); the effectiveness-by-line-count table credited to research (the article cited recommends under 300 lines and shows its own file of under sixty as an example); the adoption count; kept: a small file, project-specific lines only, no linter's job, pointers instead of copies |
| `v6/04-AI-TOOLS-LANDSCAPE/best-practices-2026/06-memory-context-management.md` | PARTIALLY_ADOPTED | [`ai-engineering/context-and-hats.md`](../ai-engineering/context-and-hats.md#three-tiers) | one vendor's load order, paths, import syntax, memory shortcuts and managed-settings JSON (the tool's own docs own them); a context file rewritten by a machine at each gate (a second home for state the sprint file holds); dated lesson files per bug folded into the context file monthly (grows the file the rule gets lost in; now: prune, then move the rule to a hook or check through lessons-to-rules); kept: specific over general, one instruction per bullet, grouped by topic |
| `v6/04-AI-TOOLS-LANDSCAPE/best-practices-2026/05-prompting-best-practices.md` | PARTIALLY_ADOPTED | [`ai-engineering/context-and-hats.md`](../ai-engineering/context-and-hats.md#briefing-an-agent) | tool-specific reference syntax and thinking-trigger phrases; model-version quirks ("may skip summaries", "do not stop early for token budget"); gate-aware and evidence-aware prompting (gate state is read from the sprint file; evidence comes from CI, not from a prompt); per-task prompt forms; kept: scope the task, point to an existing pattern, name the thing instead of leaning on chat history; added from current practice: the brief ends in a check the agent can run |
