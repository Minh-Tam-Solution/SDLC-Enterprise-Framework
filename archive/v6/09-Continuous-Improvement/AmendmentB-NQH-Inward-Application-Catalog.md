# Amendment B — NQH Inward Application Catalog (Framework 6.3.2)

```yaml
document_id: "AMENDMENT-B-NQH-INWARD-CATALOG"
title: "Amendment B — NQH Inward Application Catalog"
version: "6.3.2"
amendment: "B"
status: "ACTIVE — NQH-INWARD ONLY"
scope: "NQH/MTS internal Framework surfaces — NOT a normative downgrade for external adopters"
section: "09-Continuous-Improvement"
created: "2026-06-03"
last_updated: "2026-06-03"
related:
  - "02-Core-Methodology/SDLC-Ship-Useful-Principle.md"
  - "02-Core-Methodology/SDLC-System-Thinking-Foundation.md#mental-model-9-demand-before-surface-new-in-632--amendment-b-2026-06-03-dt"
  - "CHANGELOG.md (Amendment B v6.3.2 entry)"
```

---

## Scope Disclaimer (READ FIRST)

> **This catalog is NQH/MTS's own inward application of Mental Model #9 (Demand Before Surface) to its own product surfaces.** It is **NOT a normative downgrade** of Framework 6.3.2 for other adopters.
>
> Other tenants of Framework 6.3.2 apply Mental Model #9 to **their own** surface inventory — their daily-users, their daily-jobs, their own re-eval triggers. A surface frozen at NQH may be load-bearing at another adopter; the reverse also holds.
>
> The catalog lives in `09-Continuous-Improvement/` (not in Core or CHANGELOG) precisely because it is operational hygiene for one tenant, not a methodology change.

---

## Why this file exists separately

The first draft of Amendment B inlined this catalog inside `CHANGELOG.md`. CEO §7 review (2026-06-03) caught the framing risk: an inward NQH catalog appearing inside the Framework's CHANGELOG could read to external adopters as a normative downgrade ("Framework 6.3.2 deprecates the ENTERPRISE tier; freezes 12 SOULs; …").

The fix is structural: split the catalog out of the normative Core/CHANGELOG and place it in 09-Continuous-Improvement (operating ground, not methodology authority), with this explicit scope disclaimer at the top.

This split-out is part of CEO §7 ratification minor-change item P0-1.

---

## Inward Reclassification Catalog

Per Ship-Useful Principle, frozen surfaces preserve all existing docs and re-eval at dated triggers (default-WAIT, no drift):

| Surface | Old status | New status (NQH-inward) | Reason (NQH-specific) | Re-eval trigger |
|---------|-----------|--------------------------|------------------------|-----------------|
| Pillar 3 — Tiers ENTERPRISE / OPTIONAL (18 SOULs available) | ACTIVE | **ON-DEMAND** | No NQH adopter sits at ENTERPRISE tier as of 2026-06-03; OPTIONAL SOULs lack a daily-author internally | ≥1 named NQH adopter at the tier OR ≥3 internal pilots requesting it; otherwise re-eval **2026-09-30** |
| Section 7 — Vibecoding Index (5 signals, progressive routing) | ACTIVE (Anti-Vibecoding) | **PENDING-EFFICACY-AUDIT** | Internal diagnosis: no recorded case at NQH where Index movement changed a decision; signal-without-action pattern observed | Audit Sprint 71-72 for any decision-change evidence at NQH; if none → demote to advisory checklist internally; re-eval **2026-08-31** |
| Pillar 7 — Plugin Architecture commercial surfaces (marketplace UI, semver+rollback policy, 3-layer scorecard telemetry, mts-sdlc-lite OSS public demo) | ACTIVE (Sprints 69-73 planned) | **ON-DEMAND** (per ADR-024 Tier-Scope decision 2026-05-29 — confirmed under MM#9) | No external commercial adopter daily-uses these surfaces yet; internal NQH use covered by reference plugin only | Joint CEO+CTO+APM GO/WAIT/KILL at **2026-07-15** (S52 pilot data), **2026-08-31** (PDPL clarity), **2026-09-30** (marketplace go/no-go) |
| 18 SOUL templates (full set beyond the ~6 daily-invoked in active NQH projects) | ACTIVE library | **ON-DEMAND** (12 of 18 frozen at NQH) | 6 SOULs daily-invoked at NQH (@pm, @architect, @coder, @reviewer, @tester, @cpo); the other 12 lack a daily caller in NQH projects | Each frozen SOUL un-freezes individually when first real NQH instance ships; portfolio re-eval **2026-12-31** |
| 10 TEAM charters | ACTIVE library | **ON-DEMAND** | No NQH team charter has been instantiated against a real team operating to its charter day-to-day | First real NQH adoption un-freezes the relevant charter; library re-eval **2026-12-31** |
| Training modules ahead of practitioner demand (e.g., Module 14 full Plugin Architecture training) | PLANNED for Sprint 70 | **COMPRESSED to 1-page cheatsheet** at NQH | No NQH dev has authored a Governed-profile plugin yet → no real audience for full training internally | Cheatsheet ships in S070; full training defers until ≥3 internal NQH plugin authors exist; re-eval per sprint |

---

## NQH Surfaces Explicitly REAFFIRMED as ACTIVE

(Passed all 3 Demand Test questions inward at NQH; included here for completeness so the catalog is auditable as a full inventory, not a selective freeze list.)

- All 10 SDLC stages (every active NQH project invokes them)
- Pillar 1, 2 (sprint governance + Rule 1 CI gate), 4 (G0-G4 with named NQH deciders), 5 (SASE invoked per AI-assisted commit), 6 (doc permanence invoked by every AI tool read), Section 8 (YAML frontmatter validated continuously)
- Mental Models #1-#8 (all daily-load-bearing at NQH)
- 6 daily-invoked SOULs and the ~6 corresponding TEAM patterns
- Long-Running Agent Protocol (S119 substrate)
- Multi-Agent Patterns guide (referenced by every multi-agent design)
- CLAUDE.md Standard (consumed by AI tools every session)
- MRP Template (required at every NQH merge)
- Sprint Plan Workflow Rules 1-7 (CI-enforced at NQH)

---

## Operating Notes

- **Frozen ≠ deleted**: every frozen surface keeps its canonical doc location and content; ON-DEMAND is a status field, not a removal action.
- **Default-WAIT, no drift**: frozen surfaces do not accumulate users-by-default; thaw requires a joint CEO+CTO+APM decision at the named re-eval trigger.
- **External-adopter independence**: an external adopter of Framework 6.3.2 may legitimately mark this same Pillar 3 / Section 7 / Pillar 7 surface as ACTIVE for their own context — that is correct usage of MM#9, not a deviation from this catalog.
- **Self-eval 2026-09-03**: this entire catalog (and the principle that produced it) is itself subject to the acceptance test in [Ship-Useful Principle](../02-Core-Methodology/SDLC-Ship-Useful-Principle.md#acceptance-test-for-this-principle-self-application).

---

## References

- [Ship-Useful Principle](../02-Core-Methodology/SDLC-Ship-Useful-Principle.md)
- [Mental Model #9 — Demand Before Surface](../02-Core-Methodology/SDLC-System-Thinking-Foundation.md#mental-model-9-demand-before-surface-new-in-632--amendment-b-2026-06-03-dt)
- [CHANGELOG — Amendment B v6.3.2](../CHANGELOG.md)
- CEO Directive 2026-06-02 "Capability Uplift v4 Reframe" — originating decision
- CTO honest reframe 2026-06-02 — first concrete inward application
- ADR-024 Tier-Scope Decision (SDLC-Orchestrator, 2026-05-29) — Plugin commercial-surface tier framing
