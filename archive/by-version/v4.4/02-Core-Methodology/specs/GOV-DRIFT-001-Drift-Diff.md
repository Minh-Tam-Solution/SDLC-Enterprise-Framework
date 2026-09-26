# GOV-DRIFT-001 – Drift Diff & Predictive Alignment Specification (Shadow Draft)

> Status: SHADOW DRAFT (Not Enforced)  
> Version: 0.1  
> Linked Specs: GOV-CONT-001 (Continuity Scoring), GOV-LEGACY-ADAPTIVE-MODEL (Classification)  
> Owner: Governance Engineering (CPO Stewardship, CTO Technical Oversight)

---

## 1. Purpose
Establish a standardized method for detecting, quantifying, and projecting SDLC governance drift across documentation, implementation artifacts, and execution telemetry before material integrity loss occurs. The Drift Diff engine supplies early-stage variance signals feeding continuity scoring, readiness grading, and executive dashboards.

## 2. Problem Statement
Manual or periodic review of divergence between intended governance state (design docs, specs, controls checklists) and actual system or process implementation leads to:

- Latent integrity decay (stale documents reused as authoritative)
- Delayed identification of control regression
- Elevated remediation cost due to compounding misalignment
- Over-reliance on human spot checks without quantitative baselines

## 3. Scope
 
In-Scope:

- Structured comparison of declared governance artifacts vs implemented state (APIs, controls, training modules, role matrices)
- Detection of deletions, insertions, semantic modifications, and missing required sections
- Weighted drift scoring by artifact criticality (e.g., API contract > optional procedural note)
- Shadow-mode operation integrated with continuity & readiness composites
- JSON diff payload export for downstream analytics & ledger anchoring

Out-of-Scope (Initial Wave):

- Real-time continuous streaming diff (batch cycle only)
- Auto-remediation actions (manual governance review required)
- Full semantic LLM hallucination risk scoring (future enhancement)

## 4. Definitions

| Term | Definition |
|------|------------|
| Baseline Artifact | Canonical declarative governance file (e.g., spec, checklist, contract) |
| Observed State | Extracted current implementation snapshot (e.g., live OpenAPI, role mapping) |
| Drift Event | Classified variance unit (add/remove/modify/missing) with severity & weight |
| Drift Window | Batch evaluation interval (e.g., daily shadow run) |
| Residual Drift Index (RDI) | Weighted sum of unresolved drift events normalized 0–1 |

## 5. Inputs

| Input | Source | Format | Notes |
|-------|--------|--------|-------|
| Baseline Spec Set | Version-controlled repo | File paths list | Filter by governance file registry |
| Live API Snapshot | OpenAPI extractor | JSON | Hash compared per endpoint+method |
| Controls Checklist State | Controls tracker | JSON/CSV | Mapped to control IDs |
| Training Module Index | Training registry script | JSON | Title + version + hash |
| Role Execution Matrix | Role telemetry | JSON | Active vs required roles |
| Continuity Snapshot | Continuity engine | JSON | Provides freshness weighting |

## 6. Outputs
 
Primary Output Document (per run): `governance_drift_report_<timestamp>.json`

Schema (Draft Simplified):

```json
{
  "run_id": "uuid",
  "ts": "2025-09-17T01:35:00Z",
  "mode": "shadow",
  "baseline_commit": "<git-sha>",
  "summary": {
    "total_events": 42,
    "critical": 3,
    "high": 7,
    "medium": 19,
    "low": 13,
    "residual_drift_index": 0.27
  },
  "by_domain": {
    "api_contracts": {"events": 8, "rdi_component": 0.11},
    "controls": {"events": 5, "rdi_component": 0.05},
    "training": {"events": 6, "rdi_component": 0.03},
    "roles": {"events": 4, "rdi_component": 0.02},
    "documents": {"events": 19, "rdi_component": 0.06}
  },
  "events": [
    {
      "id": "DRV-API-0001",
      "domain": "api_contracts",
      "artifact": "openapi/public.yaml#GET /tenants/{id}",
      "type": "missing_endpoint",
      "severity": "critical",
      "weight": 5,
      "expected_hash": "sha256:...",
      "observed_hash": null,
      "notes": "Endpoint removed without governance approval"
    }
  ],
  "metrics": {
    "resolved_events_prev_window": 12,
    "new_events": 7,
    "rolling_rdi_7d": 0.23
  },
  "linkage": {
    "continuity_snapshot_id": "CONT-2025-09-17-01",
    "integrity_ledger_anchor": null
  }
}
```

## 7. Drift Event Classification

| Type | Description | Severity Guidance |
|------|-------------|-------------------|
| missing_endpoint | Baseline API spec endpoint absent in live spec | Critical/High |
| added_endpoint | Live endpoint not declared in baseline | High |
| schema_divergence | Field/shape mismatch | High/Medium |
| control_missing | Required control not implemented | Critical |
| control_stale | Control implemented but outdated revision | Medium |
| training_gap | Required module missing or outdated | Medium |
| role_gap | Required role unassigned/inactive | High |
| doc_section_missing | Required section absent | Medium/Low |
| doc_section_stale | Section present but hash unchanged past freshness threshold | Medium |

## 8. Weights & Index Computation (Draft)
 
```text
severity_weight: { critical:5, high:3, medium:2, low:1 }
RDI = ( Σ(event_weight) / Σ(max_domain_weight) ) normalized to 0–1
Domain caps & normalization factors defined in implementation appendix (future).
```

Interplay with Continuity: High freshness reduces effective weight of doc_section_stale events (decay multiplier).

## 9. Shadow Mode Plan

| Phase | Duration | Goal | Exit Criteria |
|-------|----------|------|---------------|
| Calibration | 2 weeks | Validate volume & false positives | RDI variance stable (<±10% drift) |
| Tuning | 2 weeks | Adjust weights & suppression rules | False positive rate <5% |
| Executive Preview | 1 cycle | CPO/CTO dashboard review | Sign-off on enforcement gating |
| Pre-Enforcement | 1 cycle | Dry-run threshold alerts | ≥90% critical/high addressed |

## 10. Future Enhancements
 
- Predictive drift forecasting (time-series anomaly detection)
- Semantic delta clustering (grouping related changes)
- Integrity ledger anchoring per run (hash of full drift report)
- Auto-suppression rule learning (pattern-based noise reduction)

## 11. Open Questions
 
| Area | Question |
|------|----------|
| Weight Calibration | Fixed table vs adaptive scaling per domain volume? |
| Suppression Strategy | Manual curation vs rule learning threshold? |
| Ledger Anchoring | Anchor every run or weekly aggregate only? |

## 12. Acceptance Checklist
 
- [ ] Skeleton spec created with all required sections
- [ ] Linked in CHANGELOG (pending update)
- [ ] Cross-links added to training/overview materials
- [ ] Weight table validated against continuity interplay model

---

> On approval: proceed to implement `scripts/governance/drift_diff.py` (shadow) + add CHANGELOG entry + training cross-links.
