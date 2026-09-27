# Migration map: controls and policies

> Who reads this: whoever finds an old document in `archive/` and asks "what replaced this?", and whoever brings old knowledge into this part of the live tree.
> When: before rewriting anything from the archive, and after every harvest into this area.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: readers of `archive/` asking where a v6 rule, gate or artifact policy went; authors of controls and policies
**Review by**: 2026-12-26

Harvest rows whose first live successor is in `controls/` or `policies/`, retired sources that contradict a control (the rule they break is named in the row), and the v6 changelog kept as record. Rules, outcome vocabulary and the index of all row files: [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

| Source (in `archive/`) | Outcome | Live successor | Retired concepts |
|---|---|---|---|
| `by-topic/ai-governance-v7-retired/08-Governance-Decision-Matrix.md` (risk classification table) | PARTIALLY_ADOPTED | [`controls/risk-floor-paths.md`](../controls/risk-floor-paths.md) · [`standards/testing.md`](../standards/testing.md) | the rest of the decision matrix |
| `by-topic/historical-documents/DEPRECATION-POLICY.md` (v6.3, live until 2026-09-26) | PARTIALLY_ADOPTED | [`policies/artifact-lifecycle.md`](../policies/artifact-lifecycle.md) | redirect stubs at old paths (replaced by the path map), 6-month stub grace period, `CONTENT-MAP.md`, `{NN}-Legacy/` archive layout, `99-Legacy` linter; kept: archive never delete, delete only harmful content, agents do not read the archive, broken links block (now a candidate rule) |
| `v6/03-AI-GOVERNANCE/21-V7-RULE-CONTRACT.md` | SUPERSEDED | [`controls/rule-contract.md`](../controls/rule-contract.md) | — |
| `v6/CHANGELOG-v6.md` | HISTORICAL_ONLY | [`CHANGELOG.md`](../CHANGELOG.md) (from 7.0.0) | — |
| `v6/05-Templates-Tools/04-SASE-Artifacts/02-MRP-Template.md` | RETIRED | — | merge-readiness package ritual; its "downgrade -1" migration rollback contradicts the migration rule in `controls/gates.md` |
| `v6/05-Templates-Tools/01-Specification-Standard/SPEC-0003-Policy-Guards-Design.md` | RETIRED | — | fail-open on a broken check (contradicts G2), secret policy exempting a PR with any test file (contradicts G3), policy-engine service |
| `v6/09-Continuous-Improvement/SDLC-Continuous-Improvement-Guide.md` | PARTIALLY_ADOPTED | [`policies/artifact-lifecycle.md`](../policies/artifact-lifecycle.md#releases) · [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md) | "enhancement over replacement" and "preserve all content, zero breaking changes" (contradicted: kept by harvesting claims; v7 archived every v6 document); two-week upgrade phases with sign-offs by job title; monthly, quarterly and annual review rituals; major-version criteria by platform count; ROI and productivity figures; version, date and authority in every document header (git holds them); version-numbered archive folders; kept: every release says what is preserved, what changed and what a consumer must do; only proven additions (burn case) |
| `v6/06-Case-Studies/SDLC-5.0-Framework-Upgrade-Case-Study.md` | PARTIALLY_ADOPTED | [`policies/artifact-lifecycle.md`](../policies/artifact-lifecycle.md#releases) | approval scores, onboarding-time and ROI figures, tiers by team size, team-collaboration templates; kept only the burn case: "Breaking changes: none" declared in the release that renamed three top-level folders |
| `v6/06-Case-Studies/README.md` | RETIRED | — | an index and a version timeline of the case studies (the history is the v6 changelog, kept as record above); headline figures — productivity multipliers 10x / 20x / 30x, "827:1 ROI", "$500K+ risk avoided", "99.1 % SDLC compliance" — with no measurement; tiers by team size (contradicts [`controls/tiers.md`](../controls/tiers.md#definitions)); "measure and report success metrics" as the way to contribute a case study; contradictions inside the file: two of its links point to files that are in `archive/by-topic/historical-documents/`, not in this folder, the 4.4 → 4.5 entry is summarised as "framework stability" though that study is about a count of mocks, header and footer name different framework versions (6.4.0 and 6.3.0); ideas that survive elsewhere without this source: a lesson with a price paid enters as a burn case ([`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md)) |
