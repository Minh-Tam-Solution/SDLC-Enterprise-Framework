# SDLC Ship-Useful Principle (Constraint-First / Anti-Theater) [DT]

```yaml
document_id: "SDLC-SHIP-USEFUL"
title: "Ship-Useful Principle — Constraint-First / Anti-Theater"
version: "6.3.2"
amendment: "B"
status: "ACTIVE"
external_adopter_validation: "NOT-YET-VALIDATED — NQH dogfood-first (first-customer principle)"
section: "02-Core-Methodology"
ring: "Core"
pillar: "Operating Principle (cross-cutting)"
audience: ["All Practitioners", "Leadership", "Methodology Authors"]
prerequisites: ["Mental Model #9 (Demand Before Surface)"]
created: "2026-06-03"
last_updated: "2026-06-03"
supersedes: "Implicit defaults that allowed surface accretion without demand validation"
```

> **[DT] External-adopter mark**: This principle is validated **inward** at NQH/MTS via the Amendment B inward-application catalog (see [09-Continuous-Improvement/AmendmentB-NQH-Inward-Application-Catalog.md](../09-Continuous-Improvement/AmendmentB-NQH-Inward-Application-Catalog.md)). **External-adopter value is NOT yet validated** — NQH dogfood-first per first-customer principle. External adopters should evaluate fit against their own surface inventory before applying.

> **Pillar 0 companion**: [System Thinking Foundation](./SDLC-System-Thinking-Foundation.md) (esp. Mental Model #9) → **Ship-Useful Principle** → applied across all 10 stages.

---

## Purpose

This document codifies the operating discipline that the **SDLC Framework itself** — and every project that adopts it — must apply to its own surface area. It exists because frameworks (and the platforms implementing them) accrete templates, gates, tiers, sections, and pillars faster than real adopters need them. Without an explicit anti-theater rule, methodology becomes performance art.

> **One-line rule**: *Every surface must name its daily-user OR be marked **ON-DEMAND** with a dated re-eval trigger.*

---

## The 3-Question Demand Test

Before adopting any new normative surface (pillar, section, gate, template, tier, plugin profile, scorecard, training module, governance ceremony), the proposer MUST answer:

| # | Question | Acceptable answer | Unacceptable answer |
|---|----------|-------------------|---------------------|
| 1 | **Who touches/invokes this ≥1×/day within 30 days?** | Named role + named cadence (`CEO Mon 9am standup`, `pre-commit hook every push`) | `Future adopters`, `enterprise customers`, `auditors during annual review` |
| 2 | **What breaks if this surface disappears tomorrow?** | Concrete job-to-be-done (`CEO loses Mon visibility of pod blockers`) | Compliance abstraction (`§7.3 requires it`, `governance demands it`) |
| 3 | **If #1 or #2 fails, what's the re-eval trigger?** | Dated condition (`re-eval 2026-09-30 if ≥3 pilots request`) | Open-ended (`when we're ready`, `eventually`) |

If all three pass → ship as ACTIVE.  
If #1 or #2 fails but #3 passes → ship as **ON-DEMAND** (frozen surface, re-eval at trigger).  
If #3 also fails → **KILL the proposal**.

---

## Constraint-First Operating Mode

Originating context: CEO Directive 2026-06-02 "Capability Uplift v4 Reframe" — replaced a 12-week transformation program with a Kaizen / constraint-first cadence after a small team.

**Weekly ritual** (the only mandatory governance ceremony at LITE/STANDARD tier):

1. **Identify** — what is the single binding constraint slowing real delivery THIS week? (not the most interesting problem, the binding one)
2. **Fix one** — apply the smallest intervention that relieves it
3. **Measure** — did throughput / lead-time / CEO-visible-quality move?
4. **Next** — re-identify next week's binding constraint (usually different)

**Anti-patterns this replaces**:

- Multi-workstream capability programs against single-digit teams
- Per-quarter roadmap rituals that produce roadmap docs nobody reads
- Maturity-model uplifts where the assessment is the deliverable
- "Body of evidence" rituals that produce evidence for non-existent reviewers

**Compatible with**: standard sprint cadence (sprint plan still required per Pillar 2). Constraint-First operates at the *between-sprint* layer — it picks which problems sprints attack.

---

## Anti-Theater Catalog (rules of thumb)

| Smell | Theater indicator | Anti-theater fix |
|-------|-------------------|------------------|
| **Template-without-author** | Template ships with no one committed to author the first instance | Don't publish the template until the first real instance ships |
| **Gate-without-decider** | Gate exists but no human is on the hook to approve/reject | Either name the decider with cadence OR demote gate to advisory checklist |
| **Tier-without-adopter** | Tier defined but no project sits at it | Collapse to the active tiers; reintroduce when an adopter arrives |
| **ADR-without-decision** | ADR documents a non-decision ("we'll consider X") | Don't write the ADR; write the decision context as a memo |
| **Review-cascade** | n+1 reviewer classes for the same change-class | One responsible reviewer + one accountable approver; everything else = courtesy CC |
| **Lock-refresh ceremony** | Ceremony produces no new evidence; just re-signs | Either change introduces real evidence OR ceremony is dropped |
| **Scorecard-without-action** | Scorecard published; no decision is tied to its movement | Either tie an action to a threshold OR drop the scorecard |
| **Training-without-audience** | Training module ships before there are practitioners doing the daily job | Ship the 1-page cheatsheet; defer full training until real practitioners exist |
| **Principle-without-acceptance-test** | New principle ships without a dated test for whether it changed real decisions; self-cites by its own birth-act count as "evidence" | Require ≥1 **independent** surface cite (different sprint / ADR / product) within 90 days; self-cite and birth-act-cite explicitly DO NOT count; dated demotion if unmet |

---

## ON-DEMAND: How to Mark a Surface

When a surface cannot pass the Demand Test today but is plausibly future-useful, freeze it explicitly:

```yaml
status: ON-DEMAND
reason: "No named daily-user as of {date}; surface preserved for future demand"
re_eval_trigger:
  date: 2026-09-30
  condition: "≥3 pilot adopters explicitly request this surface OR named internal daily-user emerges"
  decision_owners: ["CEO", "CTO", "APM"]
  default: "WAIT — no drift, no soft activation"
```

This pattern:
- Preserves the work already invested (no destructive deletion)
- Prevents the surface from accumulating users-by-default (which would make later removal painful)
- Makes the re-eval calendar explicit (so frozen surfaces don't accumulate indefinitely)
- Forces a joint decision (no single role can quietly thaw a frozen surface)

---

## Application to the Framework Itself (Amendment B Catalog)

The first application of this principle is **inward** at NQH/MTS: see [09-Continuous-Improvement/AmendmentB-NQH-Inward-Application-Catalog.md](../09-Continuous-Improvement/AmendmentB-NQH-Inward-Application-Catalog.md) for the list of existing Framework surfaces that have been re-classified ON-DEMAND under this principle, with each entry's re-eval trigger. That catalog is **NQH-inward only** — it is NOT a normative downgrade for other 6.3.2 adopters. Other tenants apply this principle to their own surface inventory.

**Active surfaces remain unchanged**. Only those that fail all three Demand Test questions are frozen — and the freezing is reversible the moment demand emerges.

## Acceptance Test for This Principle (Self-Application)

This principle applies to itself. By **2026-09-03** (90 days post-introduction), the principle MUST have caused **≥1 independent surface decision** — different sprint, different ADR, different product — to cite MM#9 / Ship-Useful Principle as the driving rationale.

**Self-cite explicitly does NOT count**:

- Citation by the authoring memo (the CPO proposal at `docs/09-govern/decisions/2026-06-03-cpo-proposal-framework-6.3.2-amendment-b.md` in SDLC-Orchestrator) does **not** count.
- Citation by the birth-act review exchange that produced this amendment (CEO/CTO/CPO ratification thread, the Framework PR opening this principle, this doc's own retrospective) does **not** count.
- Citation by a surface that was part of producing this amendment does **not** count.

An **independent cite** must originate from a sprint or ADR or product surface that did not participate in producing Amendment B. If unmet by 2026-09-03: this principle demotes to advisory note (default-WAIT, no drift). Facilitator: dvhiep (APM). Co-deciders: CEO + CTO.

---

## Relationship to Existing Pillars

| Pillar / Section | Effect of Ship-Useful Principle |
|------------------|-------------------------------|
| Pillar 1 (10-Stage Lifecycle) | Unchanged — stages are demand-validated by every active project |
| Pillar 2 (Sprint Governance) | Compatible — sprint plan rule (Rule 1) stays; Constraint-First operates between sprints |
| Pillar 3 (4-Tier Classification) | Amended — only tiers with ≥1 active adopter remain ACTIVE; others → ON-DEMAND |
| Pillar 4 (Quality Gates) | Unchanged for gates with named deciders; advisory-demote for those without |
| Pillar 5 (SASE Integration) | Unchanged — load-bearing for every AI-assisted commit |
| Pillar 6 (Doc Permanence) | Unchanged — invoked daily by AI tools |
| Pillar 7 (Plugin Architecture) | ON-DEMAND on commercial surfaces; internal-use surfaces (mts-sdlc-lite reference plugin) remain ACTIVE |
| Section 7 (Anti-Vibecoding / Vibecoding Index) | ACTIVE — paired with Governance-Spiral anti-pattern; code-side Index + gov-side `gov:code` ratio must both move decisions |
| Section 8 (Unified Spec) | ACTIVE — invoked by every YAML-frontmatter-validated document |

---

## What This Principle Is NOT

- **Not** a budget cut — frozen surfaces keep their docs; their re-eval is calendared
- **Not** anti-rigor — the test for rigor is *daily use*, not *artifact count*
- **Not** anti-planning — sprint plans and ADRs for real decisions remain mandatory
- **Not** a license to skip exit criteria — exit criteria for active stages stay enforced
- **Not** a permission to bypass safety reviews — security/PII/payments still escalate per Mental Model #8

It is, simply, the discipline of refusing to add surface that no one will daily-touch.

---

## References

- [Mental Model #9: Demand Before Surface](./SDLC-System-Thinking-Foundation.md#mental-model-9-demand-before-surface-new-in-632--amendment-b-2026-06-03-dt)
- [CHANGELOG Amendment B — v6.3.2 (2026-06-03)](../CHANGELOG.md#-version-632--amendment-b--june-3-2026-ship-useful--anti-theater-principle-dt)
- [Amendment B — NQH Inward Application Catalog](../09-Continuous-Improvement/AmendmentB-NQH-Inward-Application-Catalog.md) — the inward catalog (NQH-only)
- [SDLC Core Methodology](./SDLC-Core-Methodology.md) — Pillar overview
- CEO Directive 2026-06-02 "Capability Uplift v4 Reframe" (NQH leadership channel) — originating decision
- CTO honest reframe 2026-06-02 "SDLC-Orch internal 2-Role positioning" — first concrete inward application
