# GOV-CONT-001 – Continuity Scoring Specification
Status: SHADOW ACTIVE (Interim Weights Implemented; Target Weights Pending Enforcement)
Version: 0.9 (Pre-Enforcement)
Last Updated: 2025-09-16
Owner: CPO Governance Office (CTO Technical Steward)

---

## 1. Purpose

Continuity Score quantifies freshness & evidentiary integrity of governance-critical artifacts (design docs, API specs, controls, training matrices) to surface decay before it impacts delivery quality.

## 2. Scope

Applies to all SDLC 4.4 governed repositories. Shadow mode only; no merge blocking until Phase 2 activation.

## 3. Conceptual Model

Continuity aggregates four weighted dimensions producing normalized score [0.00 – 1.00].

| Dimension | Definition | Target Weight | Interim (Implemented) | Metric Source |
|-----------|------------|---------------|-----------------------|---------------|
| Update Freshness | Recency vs expected update interval | 0.40 | 0.45 | Git commit timestamps, doc metadata |
| Coverage Completeness | Required artifact presence & completeness | 0.30 | 0.25 | Scanner index, coverage map |
| Evidence Integrity | Hash chain inclusion & approval lineage | 0.20 | 0.20 | Evidence ledger (planned), approvals |
| Drift Alignment | Absence of unresolved drift findings | 0.10 | 0.10 | drift_scan shadow results |
| TOTAL |  | 1.00 | 1.00 |  |

Rationale for interim variance: overweight freshness early to incentivize rapid normalization of stale docs; underweight coverage to avoid penalizing teams still migrating.

## 4. Score Formula

```text
Continuity = Σ(weight_i * normalized_metric_i)
```

Each metric normalized [0–1]. Missing metric ⇒ 0 (explicit penalty, no silent exclusion).

## 5. Threshold Bands (Shadow Observation)

| Band | Range | Interpretation | Planned Action (Future) |
|------|-------|---------------|--------------------------|
| Excellent | ≥0.85 | Healthy & proactive | Adaptive noise dampening candidate |
| Stable | 0.70–0.84 | Acceptable; watch drift trend | Maintain cadence |
| At Risk | 0.50–0.69 | Emerging decay | Recommend remediation sprint |
| Degrading | 0.30–0.49 | Active integrity loss | Escalate to CPO weekly review |
| Critical | <0.30 | Systemic failure | Block merges (Phase 2) |

## 6. Data Acquisition Pipeline

1. Inventory required artifacts (manifest.json or dynamic walk)  
2. Extract timestamps & compute freshness delta vs policy  
3. Compute coverage ratio (#present / #required)  
4. Query evidence ledger (future) for hash + approval presence  
5. Ingest drift_scan JSON for unresolved drift count  
6. Normalize metrics & apply weights  
7. Emit JSON report: `continuity_report.json`  

## 7. JSON Output (Shadow Prototype)

Example (interim weights):

```json
{
  "version": "0.9-shadow",
  "weights": {"freshness": 0.45, "coverage": 0.25, "evidence": 0.20, "drift": 0.10},
  "metrics": {
    "freshness": {"raw_days_stale_weighted": 14, "normalized": 0.82},
    "coverage": {"required": 42, "present": 39, "normalized": 0.93},
    "evidence": {"ledger_linked": 31, "eligible": 35, "normalized": 0.89},
    "drift": {"unresolved_findings": 2, "normalized": 0.76}
  },
  "continuity_score": 0.846,
  "band": "Stable",
  "generated_at": "2025-09-16T23:12:00Z"
}
```

## 8. Activation Plan

| Phase | Mode | Duration | Exit Criteria |
|-------|------|----------|---------------|
| 0 | Draft | Spec review | CPO sign-off |
| 1 | Shadow (current) | 2 cycles | Metric stability (<5% variance) |
| 2 | Advisory | 1 cycle | ≥80% teams ≥0.70 |
| 3 | Enforced (merge gate) | Ongoing | ≥90% teams ≥0.70; critical <0.30 blocked |
| 4 | Adaptive Weights | Future | Dynamic context weighting PoC |

## 9. Governance & Overrides

- Overrides tracked in override ledger (hash chain) with explicit expiry (≤30 days)  
- Band downgrades cannot be overridden; only temporary merge allowances in Advisory phase.  

## 10. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Metric Gaming | Artificial timestamp updates | Hash chain + min delta enforcement |
| Incomplete Ledger | Understated evidence decay | Penalize missing entries as 0 |
| Drift Engine Delay | Lower composite precision | Maintain interim weighting |
| Coverage Inflation | Low-value placeholder docs | Structural lint & min size rules |

## 11. Future Extensions

- Context-aware weighting (artifact criticality)  
- Trend slope analysis (3-period regression)  
- Predictive continuity forecast (ARIMA/ETS shadow)  
- Evidence quorum scoring (multi-approver graph)  

## 12. Acceptance Checklist

- [x] Dual weight model documented  
- [x] Shadow JSON schema example  
- [ ] Linked from CHANGELOG 4.4 section  
- [ ] Cross-referenced in training objectives  

---
END OF SPEC
