# API DRIFT MEASUREMENT (v0.1)

## Purpose

Track divergence between implemented backend endpoints and declared OpenAPI contracts to enforce Design-First.

## Drift Categories

| Category | Definition | Example | Severity | Auto Action |
|----------|------------|---------|----------|-------------|
| Missing Contract | Endpoint exists in code but not in spec | /v1/ledger/export | High | Fail gate (G4) |
| Missing Implementation | Spec endpoint not implemented | /v1/auth/refresh | High | Warning → fail at G5 if persists |
| Schema Divergence | Field / type mismatch | amount:int vs amount:decimal | Medium | Include in drift ratio |
| Status Code Divergence | Declared 201 but returns 200 | create invoice | Medium | Log & count |
| Deprecation Violation | Deprecated endpoint still active w/o sunset plan | /v1/old-report | Medium | Escalate |
| Documentation Lag | Spec updated but code not deployed (age>14d) | version header mismatch | Low | Reminder |

## Drift Ratio

Drift Ratio = (D_code_only + D_schema + D_status + D_deprecation) / Total_Changed_Endpoints (capped at 1.0)

Target: Drift Ratio ≤ 0.10 (10%)

## Process Flow

1. Collect current OpenAPI spec(s): fastapi generated + stored canonical spec file.
2. Parse code (FastAPI routers, Django DRF views) to enumerate endpoints.
3. Normalize (method, path) keys.
4. Compare contract vs implementation sets.
5. For overlapping endpoints, diff request/response schemas & status codes.
6. Aggregate counts per category.
7. Emit drift_report.json + markdown summary.
8. Gate evaluation: if Missing Contract > 0 → fail.

## Output Schema (drift_report.json)

```json
{
  "generated_at": "ISO-8601",
  "totals": {
    "endpoints_contract": 0,
    "endpoints_implementation": 0,
    "endpoints_overlap": 0
  },
  "counts": {
    "missing_contract": 0,
    "missing_implementation": 0,
    "schema_divergence": 0,
    "status_divergence": 0,
    "deprecation_violation": 0,
    "documentation_lag": 0
  },
  "drift_ratio": 0.0,
  "thresholds": {"max_drift_ratio": 0.10},
  "failures": [],
  "warnings": []
}
```

## Detection Heuristics (Initial)

| Divergence | Heuristic |
|-----------|-----------|
| Schema | Compare json schema shapes (type, required, enum) |
| Status | Collect observed status codes from tests / logs vs spec |
| Deprecation | Spec mark deprecated=true; code still registers route |
| Documentation Lag | Spec commit newer than code commit by > 14 days |

## Integration

| Script | Role | Input | Output |
|--------|------|-------|--------|
| api_drift_check.py | Generate drift metrics | openapi.json, code scan | drift_report.json |
| compliance_report.py | Include drift summary | drift_report.json | compliance_dashboard.md |

## Escalation

- Any High severity category > 0 → block merge (architect override required).
- Two consecutive Medium increases (>20% delta) → architecture review.

## Roadmap

- Endpoint stability score.
- Per-module drift heatmap.
- Historical trending & regression detection.

Last updated: v0.1 scaffold
