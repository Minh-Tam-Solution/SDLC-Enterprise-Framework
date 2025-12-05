# GOV-DRIFT-001: Design & Schema Drift Detection Specification

Status: DRAFT (Shadow Planning)
Owner: Governance Engineering
Last Updated: 2025-09-16
Related Pillars: Design Intent Preservation, Predictive Integrity, Continuity Correlation
Upstream References: SDLC 4.4 Core Methodology (Sections 17–21), GOV-CONT-001

---
## 1. Purpose

Phát hiện sớm thay đổi không được phản chiếu (undocumented / unaligned) giữa thiết kế được phê duyệt (design intent) và hiện trạng thực thi (schema, API, process). Mục tiêu: giảm drift noise, kích hoạt cảnh báo trước khi continuity score suy giảm.

## 2. Scope

| Included | Excluded (Phase 1) |
|----------|--------------------|
| API spec (OpenAPI) vs implemented endpoints | Performance benchmark structure |
| Database schema vs migration lineage | Non-governed experimental feature flags |
| Process / workflow definition vs runtime config | Transient prototype branches |
| AI intent linkage vs downstream process usage | Third-party vendor schemas |

## 3. Definitions

| Term | Definition |
|------|------------|
| Drift Event | Bất kỳ sai khác có ý nghĩa giữa nguồn chuẩn (source-of-truth) và trạng thái triển khai |
| Shadow Drift | Drift được ghi nhận nhưng chưa cảnh báo blocking (phase calibration) |
| Critical Drift | Sai khác cấu trúc ảnh hưởng contract / dữ liệu / bảo toàn ý định |
| False Positive (FP) | Signal drift nhưng thực tế là hợp lệ (ví dụ đổi thứ tự field không ảnh hưởng) |
| Alignment Ref | Tham chiếu canonical (intent_id, design_token_id, version hash) |

## 4. Data Inputs

| Input | Source | Format |
|-------|--------|--------|
| OpenAPI canonical specs | `contracts/api-specs/` | YAML / JSON |
| Live endpoint map | Generated via runtime probe (`tools/api/scan_endpoints.py`) | JSON |
| Database canonical schema | Declarative model export | JSON snapshot |
| Migration history | `backend/migrations/` | File list + parsed ops |
| Intent registry | `governance/intent/` | JSON docs |
| Process definitions | `process/` (BPMN / DSL) | XML / YAML |

## 5. Drift Categories

| Category | Description | Severity Basis |
|----------|-------------|----------------|
| API Missing Endpoint | Spec listed nhưng không có runtime | Medium (age escalates) |
| API Undeclared Endpoint | Runtime có nhưng spec thiếu | High (potential contract risk) |
| Schema Extra Column | Column không có trong canonical | Medium |
| Schema Missing Column | Canonical có nhưng runtime thiếu | High (data loss risk) |
| Intent Link Missing | Process không có intent_ref | High |
| Intent Stale Link | intent_ref tồn tại nhưng outdated version | Medium |
| Process Step Divergence | Step name / sequence mismatch | Medium |
| Migration Drift | Migration file không phản chiếu schema snapshot | High |

## 6. Detection Model (Phase 1)

1. Load canonical artifacts (API spec, schema snapshot, intent registry).  
2. Extract runtime state (endpoint scan, DB schema inspection, migration parse).  
3. Normalize representations (sorted arrays, lowercase identifiers).  
4. Compare sets & structures → generate candidate drift events.  
5. Apply suppression rules (benign reorder, naming alias map).  
6. Tag severity + compute FP risk score (heuristic).  
7. Emit drift report JSON (shadow).  
8. (Optional) Correlate with continuity score delta (if available) → add correlation field.

## 7. JSON Report Schema (Draft)

```json
{
  "version": "1",
  "generated_at": "ISO8601",
  "mode": "shadow|enforced",
  "summary": {
    "total_events": 0,
    "critical": 0,
    "medium": 0,
    "low": 0,
    "false_positive_suspect": 0
  },
  "events": [
    {
      "id": "uuid-like",
      "category": "api_missing_endpoint",
      "severity": "medium",
      "artifact_type": "api|schema|intent|process|migration",
      "canonical_ref": "path_or_identifier",
      "runtime_ref": "path_or_identifier",
      "age_cycles": 2,
      "fp_risk": 0.15,
      "correlated_continuity_drop": false,
      "suggested_action": "add_spec_entry",
      "metadata": {}
    }
  ],
  "correlation": {
    "continuity_score_before": 0.0,
    "continuity_score_after": 0.0,
    "delta": 0.0
  },
  "warnings": ["string"],
  "hash": null
}
```

## 8. Thresholds & Gates

| Metric | Shadow Target | Enforce Gate | Action |
|--------|---------------|--------------|--------|
| FP Rate (rolling 3 windows) | <20% | <10% | Promote to advisory → enforce |
| Undeclared Endpoint High Drift | <=2 | 0 sustained 2 cycles | Block (advisory first) |
| Schema Missing Column | 0 | 0 | Immediate critical alert |
| Intent Link Missing | <5 | 0 | Advisory then enforce |
| Stale Intent Ratio | <10% | <5% | Enforce after 3 stable cycles |

## 9. False Positive Reduction Techniques

| Source | Heuristic | Effect |
|--------|-----------|--------|
| API path param order | Normalize pattern tokens | Reduce reorder noise |
| Case variance | Lowercase all identifiers | Eliminate case-only drift |
| Alias columns | Apply alias map (config) | Filter benign schema rename |
| Deprecated endpoints | Exclude flagged endpoints | Avoid legacy churn |
| Spec lag tolerance | Age grace period (cycles<2) | Prevent premature alert |

## 10. Correlation With Continuity

- When continuity score delta (negative) co-occurs with drift burst (>3 events medium+), raise `correlated_continuity_drop=true`.
- Future: compute weighted contribution of drift categories to continuity freshness decay.

## 11. Operational Modes

| Mode | Purpose | Blocking |
|------|---------|----------|
| Shadow | Hiệu chỉnh, thu thập FP | Không block |
| Advisory | Cảnh báo có chọn lọc | Block chỉ critical |
| Enforced | Ổn định | Block theo quy tắc severity |

## 12. Governance & Change Control

- Thay đổi mapping severity cần CTO+CPO review.  
- Thêm alias map: ticket governance + cập nhật hash chain.  
- FP triage log giữ tối thiểu 90 ngày.  

## 13. Future Enhancements

| Enhancement | Description | Priority |
|------------|-------------|----------|
| Drift -> Continuity Weight Model | Statistical attribution engine | High |
| ML-based FP Classifier | Train on triage history | Medium |
| Multi-tenant Drift Segmentation | Per-tenant drift patterns | Medium |
| Visual Timeline Correlation | UI timeline overlay | Low |
| Drift Aging Decay Score | Integrate age-based decay into severity | Medium |

## 14. Acceptance Criteria

- JSON report schema-valid (100 consecutive runs).  
- FP rate <10% (shadow measurement) trước promotion.  
- No critical drift unresolved > 2 cycles.  
- Correlation flag logic validated on synthetic test set.  

---
END OF SPEC
