# Migration map: core

> Who reads this: whoever finds an old document in `archive/` and asks "what replaced this?", and whoever brings old knowledge into this part of the live tree.
> When: before rewriting anything from the archive, and after every harvest into this area.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: readers of `archive/` asking where a v6 methodology source went; authors harvesting into `core/`
**Review by**: 2026-12-26

Harvest rows whose first live successor is in `core/` (constitution, lifecycle, systems thinking, design thinking), and retired sources whose idea survives there. Rules, outcome vocabulary and the index of all row files: [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

| Source (in `archive/`) | Outcome | Live successor | Retired concepts |
|---|---|---|---|
| `v6/02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md` | PARTIALLY_ADOPTED | [`core/lifecycle.md`](../core/lifecycle.md) · [`standards/observability.md`](../standards/observability.md) · [`standards/testing.md`](../standards/testing.md) · [`core/design-thinking.md`](../core/design-thinking.md) · [`standards/integration-and-data.md`](../standards/integration-and-data.md) | stage dependency YAML matrix, artifact SHA256 integrity per stage, evidence vault |
| `v6/02-Core-Methodology/SDLC-System-Thinking-Foundation.md` | PARTIALLY_ADOPTED | [`core/systems-thinking.md`](../core/systems-thinking.md) | the nine numbered mental models as a canon, pillar mapping, effort-compression ratios, completeness score X/10, iceberg-per-stage table, company-specific gate numbers |
| `v6/02-Core-Methodology/SDLC-Ship-Useful-Principle.md` | PARTIALLY_ADOPTED | [`core/constitution.md`](../core/constitution.md#demand-before-surface) · [`core/systems-thinking.md`](../core/systems-thinking.md) | ON-DEMAND YAML markers with named decision owners, "used at least daily" frequency rule; its own 90-day acceptance test was never recorded as run — kept as a lesson: a dated test needs a ledger row |
| `v6/02-Core-Methodology/SDLC-Core-Methodology.md` | PARTIALLY_ADOPTED | [`core/systems-thinking.md`](../core/systems-thinking.md) | "tools MUST gate-enforce systems and design thinking evidence at G1/G2" (lenses stay ADVISORY), the company-specific governance ratio threshold |
| `v6/CLAUDE.md` | PARTIALLY_ADOPTED | [`core/systems-thinking.md`](../core/systems-thinking.md) | the rest of the v6 agent guide (v6 machinery) |
| `by-version/v4.4/02-Core-Methodology/SDLC-4.4-Core-Methodology.md` | PARTIALLY_ADOPTED | [`core/systems-thinking.md`](../core/systems-thinking.md) | leverage score, continuity dashboards, escalation timers, "procedural fixes rejected pending structural evaluation" (a veto) |
| `v6/02-Core-Methodology/SDLC-Design-Thinking-Principles.md` | PARTIALLY_ADOPTED | [`core/design-thinking.md`](../core/design-thinking.md) | five-phase ritual with day budgets, gates 0.1–0.5, "50+ ideas" quota, >70% opinion thresholds, mandatory upfront phase, vendor tool rows |
| `v6/06-Case-Studies/SDLC-Design-Thinking-Case-Study-NQH-Bot.md` | PARTIALLY_ADOPTED | [`core/design-thinking.md`](../core/design-thinking.md) | ROI and impact figures; "I would use this" counted as validation |
| `v6/08-Training-Materials/SDLC-Quick-Start-Guide.md` | PARTIALLY_ADOPTED | [`core/design-thinking.md`](../core/design-thinking.md) | "would you use this?" questions and the >70% positive-feedback decision rule |
| `v6/05-Templates-Tools/06-Manual-Templates/Design-Thinking-Prototype-Test-Plan-Template.md` | PARTIALLY_ADOPTED | [`core/design-thinking.md`](../core/design-thinking.md) | the template form (kept: kill assumptions with a success criterion written before the test) |
| `v6/05-Templates-Tools/06-Manual-Templates/Design-Thinking-User-Testing-Script-Template.md` | PARTIALLY_ADOPTED | [`core/design-thinking.md`](../core/design-thinking.md) | the script form (kept: facilitate, do not help, think aloud) |
| `v6/05-Templates-Tools/06-Manual-Templates/Design-Thinking-Problem-Statement-Template.md` | PARTIALLY_ADOPTED | [`core/design-thinking.md`](../core/design-thinking.md) | the template form (kept: anchor the statement in user quotes) |
| `v6/05-Templates-Tools/06-Manual-Templates/Design-Thinking-Feedback-Analysis-Template.md` | PARTIALLY_ADOPTED | [`core/design-thinking.md`](../core/design-thinking.md) | the template form (kept: "cannot do it" outranks "want it different"; one showstopper blocks) |
| `v6/06-Case-Studies/MTEP-PLATFORM-LESSONS-LEARNED.md` | RETIRED | — | "customer reality" as a fourth systems-thinking dimension — the idea survives in design thinking ("is the problem real for these users") |
| `v6/08-Training-Materials/Module-09-Quality-Gate-Workshop.md` | PARTIALLY_ADOPTED | [`core/lifecycle.md`](../core/lifecycle.md#moving-back-is-normal) | one product's walkthrough (web UI, messaging bot, workshop accounts, gate states), the hash-chained audit trail and hashed evidence uploads (retired with the evidence vault, see the stage-lifecycle row), approvers by job title with a joint CEO and CTO sign-off on G4 (contradicted: signing follows the tier), "self-approval is prohibited at every level" (contradicted: at LITE and STANDARD the author records the exit; independence applies where the tier requires a second person, [`gates.md`](../controls/gates.md#approver-independence)), sprint gates and their ten golden rules, escalation after three rejections; kept: reasons a gate is sent back — a claim with nothing to point at, work outside the planned scope, the author's own sign-off where the tier requires someone else's; one question per gate was already there |
