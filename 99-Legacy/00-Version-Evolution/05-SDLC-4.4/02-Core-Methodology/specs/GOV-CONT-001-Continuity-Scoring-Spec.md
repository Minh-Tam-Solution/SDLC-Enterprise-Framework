# GOV-CONT-001: Continuity Scoring Specification

Status: SHADOW ACTIVE (Calibration Phase)
Owner: Governance Engineering  
Last Updated: 2025-09-16 (Updated with Interim vs Target Weights Calibration)  
Related Pillars: Cryptographic Evidence Continuity, Design Intent Preservation

---
 
## 1. Purpose

Provide a deterministic, explainable composite metric (Continuity Score) that quantifies governance evidence integrity over time: freshness, coverage, orphan minimization, and chain integrity. Enables early detection of silent governance erosion before failures manifest.

## 2. Scope

Applies to governed artifacts across code, design, operational readiness, and intent layers. Initially advisory (shadow) → enforced after stability validation.

Inclusions:

- Design artifacts (architecture tokens, process diagrams, AI intent specs)
- API contracts & schema definitions
- Test evidence (coverage summary + critical suite manifests)
- Operational readiness (observability configs, SLO definitions)
- Governance hash chain indices

Exclusions (Phase 1):

- Performance benchmark raw logs
- Vendor SLA documents
- Transient experiment notebooks

## 3. Definitions

| Term | Definition |
|------|------------|
| Governed Artifact | File or structured record classified as requiring integrity tracking |
| Freshness Window | Maximum acceptable staleness before decay penalty applies |
| Orphan Artifact | Unreferenced or untagged legacy file within governed scope |
| Chain Integrity | Measure of uninterrupted hash linkage across governance checkpoints |
| Shadow Mode | Non-blocking computation used for calibration |

## 4. Data Sources

| Source | Path / Mechanism | Notes |
|--------|------------------|-------|
| Artifact Inventory | `tools/legacy/legacy_scan` (planned) | Emits JSON classified list |
| Hash Chain | `tools/integrity/hash_chain_*` | Provides linkage continuity |
| Documentation Coverage | `tools/docs/coverage_export` | Percentage + critical missing list |
| Test Coverage | `coverage/summary.json` | Line/branch aggregation |
| Intent Registry | `governance/intent/` | Maps AI intent IDs to downstream processes |

## 5. Formula (Weights)

Continuity Score (CS) is a weighted sum of normalized sub-scores.

### 5.0.1 Target Weights (Spec Authority)

CS_target = 0.40·Freshness + 0.30·Coverage + 0.20·(1 − OrphanRatio) + 0.10·ChainIntegrity

### 5.0.2 Interim Implementation Weights (Placeholder Engine)

Current script (`tools/governance/continuity_scan.py`) uses a provisional simplified form:

CS_interim = (0.40·Freshness + 0.35·Coverage + 0.15·IntegrityApprox) · (1 − OrphanPenalty)

Mapping:
- IntegrityApprox ~ ChainIntegrity (no orphan inversion term explicit)
- OrphanPenalty ≈ (OrphanRatio * small_factor) in future; currently minimal pseudo value
- Coverage weight temporarily elevated (+0.05) pending full orphan + chain signal extraction

Rationale: Allows early directional telemetry before full artifact inventory + hash chain APIs are productionized. This delta MUST be retired once inventory & hash continuity adapters are live (tracked in Activation Roadmap §9).

### 5.0.3 Convergence Plan

- Phase A (current): Use CS_interim; record raw freshness & coverage; pseudo orphan penalty.
- Phase B: Introduce real orphan ratio + chain integrity; adjust weights to (0.40/0.30/0.20/0.10) while still supporting backward JSON.
- Phase C: Enforced mode only after 14-day variance stability (< ±0.02 drift window) using target weights.

Constraints (Target Weights):

- Each component ∈ [0,1]
- If any mandatory baseline artifact class coverage < required minimum, cap CS_target at 0.69 (hard floor pre-enforcement)

### 5.1 Freshness Sub-Score

For each governed artifact i:

- age_i = now − last_modified_ts
- Apply decay: d_i = exp(− age_i / τ_class)
- Freshness = (Σ w_i·d_i) / Σ w_i, where w_i derived from artifact criticality tier (HIGH=1.0, MED=0.6, LOW=0.3)

Class τ suggestions:

| Artifact Class | τ (days) |
|----------------|----------|
| AI Intent Spec | 14 |
| Design Token / Diagram | 21 |
| API Contract | 14 |
| Schema Definition | 10 |
| Critical Test Manifest | 7 |
| Observability Config | 14 |

### 5.2 Coverage Sub-Score

Coverage = 0.5·DocCoverageNorm + 0.5·TestCoverageNorm

Normalization:

DocCoverageNorm = min(1, DocCoverageRaw / TargetDoc)  
TestCoverageNorm = min(1, TestCoverageRaw / TargetTest)

Initial Targets: TargetDoc=0.90, TargetTest=0.75 (phase 1); raise after stabilization.

### 5.3 Orphan Ratio Sub-Score

OrphanRatio = orphan_count / total_governed  
If total_governed < threshold_min (e.g., 25), suppress ratio penalty (use neutral 0.5) to avoid early noise.

### 5.4 Chain Integrity Sub-Score

ChainIntegrity = valid_segments / expected_segments within rolling window (e.g., last 14 hash events). Missing or tampered links reduce proportionally. If any cryptographic verification fails (hash mismatch) set ChainIntegrity = 0 until remediation event recorded.

## 6. Output JSON Schema

```json
{
  "version": "1",
  "timestamp": "ISO8601",
  "score": 0.0,
  "components": {
    "freshness": { "value": 0.0, "artifact_sample": ["path1", "path2"], "decay_params": {"tau_map": {"api":14}} },
    "coverage": { "value": 0.0, "doc": 0.0, "test": 0.0, "targets": {"doc":0.9, "test":0.75} },
    "orphans": { "value": 0.0, "count": 0, "total": 0 },
    "chain": { "value": 0.0, "valid_segments": 0, "expected_segments": 0 }
  },
  "caps_applied": ["baseline_coverage_floor"],
  "mode": "shadow|enforced",
  "warnings": ["string"],
  "hash": "sha256(hex)"
}
```

## 7. Operational Modes

| Mode | Purpose | Enforcement |
|------|---------|-------------|
| Shadow | Calibration period | Non-blocking, logs only |
| Advisory | Soft alerts | Blocks only on catastrophic integrity (chain=0) |
| Enforced | Mature stability | Merge/pipeline block below threshold |

## 8. Thresholds & Gates

| Threshold | Value | Action |
|-----------|-------|--------|
| Enforce Promote Gate | ≥0.85 for 14 consecutive days | Enable enforced mode |
| Advisory Warning | <0.80 | Alert governance channel |
| Hard Fail (Enforced) | <0.70 | Block merge / require remediation ticket |
| Chain Tamper Detect | chain=0 | Immediate incident flag |

## 9. Rollout Phases

1. Implement calculator in shadow (export JSON artifact each run).  
2. Track variance (σ of daily score) target <0.05.  
3. Publish weekly trend to executive dashboard (hash-linked).  
4. Promote to Advisory when stability + minimum artifact classification coverage >85%.  
5. Promote to Enforced after Gate criteria met (Section 8).  

## 10. Edge Cases

| Scenario | Handling |
|----------|----------|
| Sudden artifact class surge | Temporarily neutral weight until classification stabilized |
| Extremely low artifact count | Apply neutral Orphan component (0.5) |
| Missing coverage report | Set coverage component=0 and flag warning |
| Negative time skew (clock drift) | Discard sample & emit clock warning |
| Decay τ misconfiguration | Fallback to default τ=14 & warning |

## 11. Governance & Audit

- All parameter changes (weights, τ values, thresholds) require CTO+CPO approval (structural if impacting weight distribution).  
- JSON outputs hashed & appended to governance hash chain.  
- Overrides logged in `governance/continuity_overrides.yaml` (planned).  
- Quarterly retros assess weight relevance; no more than one structural change / quarter unless incident-driven.  

## 12. Future Enhancements

| Enhancement | Description | Priority |
|------------|-------------|----------|
| Adaptive Weight Tuning | Auto-adjust weights based on predictive failure correlation | Medium |
| Per-Domain Sub-Scores | Separate pipeline vs domain service continuity | Medium |
| Intent Freshness Isolation | Independent scoring for AI intent artifacts | High |
| Drift Correlation Layer | Cross-link drift diff anomalies to continuity drops | High |
| Chain Compression | Merkle subtree for large artifact sets | Low |

## 13. Acceptance Criteria (for Enforced Mode)

- CI job produces JSON schema-valid output every run.  
- Variance (σ 14-day window) <0.05.  
- False negative rate (missed stale artifact > 2× τ) <5%.  
- Executive dashboard displays rolling 30-day trajectory.  
- Documentation & test coverage targets met or exceeded for 14 days.  

## 14. Implementation Notes

Initial implementation may use Python script with in-memory classification rules; refactor to modular plugin once >10 artifact classes. Provide dry-run flag and verbose artifact explanation export for troubleshooting.

---
END OF SPEC
