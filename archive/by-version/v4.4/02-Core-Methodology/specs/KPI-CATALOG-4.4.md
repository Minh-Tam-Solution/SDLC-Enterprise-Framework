# KPI CATALOG 4.4 (Adaptive & Predictive Governance)

Status: DRAFT (Iteration 1)
Owner: Governance / Data Reliability
Last Updated: 2025-09-16
Scope: Phase 1–2 metrics supporting continuity, drift, readiness, executive transparency.

---

## 1. Structure & Naming

Each KPI entry includes: Purpose, Definition, Formula / Method, Data Sources, Frequency, Tier, Alert Rules, Anti-Gaming Notes.

Tier Legend: CORE / ADAPTIVE / PREDICTIVE / ADVANCED

---

## 2. KPI Index

| Code | Name | Tier | Primary Pillar |
|------|------|------|----------------|
| KPI-FRESH | Evidence Freshness % | ADAPTIVE | Continuity |
| KPI-CSCORE | Continuity Score | ADAPTIVE→PREDICTIVE | Continuity |
| KPI-DRIFT-CRIT | Critical Drift Events | PREDICTIVE | Design Intent |
| KPI-DRIFT-FP | Drift False Positive Rate | PREDICTIVE | Predictive Integrity |
| KPI-DOC | Documentation Coverage % | CORE | Documentation Integrity |
| KPI-TEST | Test Coverage % | CORE | Quality Execution |
| KPI-TENANT-COV | Tenant Coverage % | ADAPTIVE | Isolation Assurance |
| KPI-TENANT-RAW | Tenant Raw Emit Count | ADAPTIVE | Isolation Assurance |
| KPI-MTTC | Median Time To Containment | ADAPTIVE | Time-to-Containment |
| KPI-HALT | Halt Events / Quarter | ADAPTIVE | Stability & Control |
| KPI-ANOM-PREC | Anomaly Forecast Precision | ADVANCED | Predictive Guardrails |
| KPI-ANOM-FP | Anomaly Forecast False Positive % | ADVANCED | Predictive Guardrails |
| KPI-P95-LAT | p95 Latency Delta % | CORE→ADAPTIVE | Performance Early Warning |
| KPI-ALERT-NOISE | Alert Noise Reduction % | ADAPTIVE | Signal Hygiene |
| KPI-INTENT-LINK | Intent Link Coverage % | ADAPTIVE→PREDICTIVE | Design Intent |
| KPI-INTENT-STALE | Stale Intent Ratio % | PREDICTIVE | Design Intent |

---

## 3. KPI Definitions

### KPI-FRESH – Evidence Freshness %

- Purpose: Đảm bảo artifact quan trọng không bị staleness kéo dài.
- Definition: governed_artifacts_updated_<24h / total_governed * 100
- Data Sources: Artifact inventory (legacy scan), file mtimes.
- Frequency: Daily (CI pipeline + nightly batch).
- Tier: ADAPTIVE
- Alert Rules: <95% advisory, <90% warning, <85% escalate.
- Anti-Gaming: Random spot hash to ensure “touch without change” không hợp lệ (future).

### KPI-CSCORE – Continuity Score

- Purpose: Composite sức khoẻ chuỗi bằng chứng (xem GOV-CONT-001).
- Definition: 0.40 Freshness + 0.30 Coverage + 0.20 (1 − Orphan) + 0.10 ChainIntegrity.
- Data Sources: continuity_score.json.
- Frequency: Per pipeline run.
- Tier: ADAPTIVE→PREDICTIVE.
- Alert Rules: <0.80 advisory; <0.70 block (enforced mode).
- Anti-Gaming: Coverage floor cap + chain integrity zeroing.

### KPI-DRIFT-CRIT – Critical Drift Events

- Purpose: Theo dõi số lượng sai khác ảnh hưởng contract / data / intent.
- Definition: Count of drift events severity=critical (current window).
- Data Sources: drift_report.json.
- Frequency: Per drift scan run.
- Tier: PREDICTIVE.
- Alert Rules: >0 triggers immediate review; 2 consecutive cycles → escalation.
- Anti-Gaming: Triage log immutable, hash-chained.

### KPI-DRIFT-FP – Drift False Positive Rate

- Purpose: Đo chất lượng bộ lọc drift.
- Definition: confirmed_fp / total_drift_events (rolling 3 windows).
- Data Sources: triage log + drift report.
- Frequency: Rolling window compute.
- Tier: PREDICTIVE.
- Alert Rules: >20% blocks promotion; target <10% for enforcement.
- Anti-Gaming: Manual override entries require reason + reviewer id.

### KPI-DOC – Documentation Coverage %

- Purpose: Bảo đảm baseline doc.
- Definition: documented_entities / total_entities.
- Data Sources: docs coverage export.
- Frequency: CI pipeline.
- Tier: CORE.
- Alert Rules: <90% hold adaptive progression; <85% block release.
- Anti-Gaming: Cross-check with design tokens list.

### KPI-TEST – Test Coverage %

- Purpose: Bảo đảm chất lượng thực thi.
- Definition: line_coverage% (tool-provided).
- Data Sources: coverage/summary.json.
- Frequency: CI pipeline.
- Tier: CORE.
- Alert Rules: <60% cannot enable predictive modules; <50% escalate.
- Anti-Gaming: Mutation score (future) to validate depth.

### KPI-TENANT-COV – Tenant Coverage %

- Purpose: Đo tỷ lệ tenant có emit với nhãn đúng.
- Definition: (1 - unlabeled/total) * 100.
- Data Sources: readiness script shadow.
- Frequency: Daily.
- Tier: ADAPTIVE.
- Alert Rules: <97% advisory, <95% escalation.
- Anti-Gaming: Random sampling of raw events.

### KPI-TENANT-RAW – Tenant Raw Emit Count

- Purpose: Bổ trợ context coverage (slope tracking).
- Definition: Count raw labeled events.
- Data Sources: readiness script.
- Frequency: Daily.
- Tier: ADAPTIVE.
- Alert Rules: Sudden ±30% delta triggers review.
- Anti-Gaming: Smoothing (3-run EWMA).

### KPI-MTTC – Median Time To Containment

- Purpose: Rút ngắn detection→containment.
- Definition: median(incident_containment_time_minutes).
- Data Sources: incident log.
- Frequency: Per incident + weekly aggregation.
- Tier: ADAPTIVE.
- Alert Rules: >15 min median = yellow; >25 red.
- Anti-Gaming: Require external timestamp source.

### KPI-HALT – Halt Events / Quarter

- Purpose: Đo ổn định & chất lượng kiểm soát.
- Definition: Count enforced halt events severity≥HIGH / quarter.
- Data Sources: governance halt log.
- Frequency: Quarterly roll-up.
- Tier: ADAPTIVE.
- Alert Rules: Upward trend 2 quarters → root cause review.
- Anti-Gaming: Require cause classification.

### KPI-ANOM-PREC – Anomaly Forecast Precision

- Purpose: Đánh giá giá trị predictive.
- Definition: true_positive / (true_positive + false_positive).
- Data Sources: forecast evaluation set.
- Frequency: Weekly.
- Tier: ADVANCED.
- Alert Rules: <70% block gating.
- Anti-Gaming: Balanced validation dataset.

### KPI-ANOM-FP – Anomaly Forecast False Positive %

- Purpose: Giảm noise.
- Definition: false_positive / total_alerts * 100.
- Data Sources: forecast evaluation log.
- Frequency: Weekly.
- Tier: ADVANCED.
- Alert Rules: >25% revert to advisory.
- Anti-Gaming: Require manual classification record.

### KPI-P95-LAT – p95 Latency Delta %

- Purpose: Early performance regression signal.
- Definition: (current_p95 - baseline_p95) / baseline_p95 * 100.
- Data Sources: perf telemetry.
- Frequency: Each deploy + hourly.
- Tier: CORE→ADAPTIVE.
- Alert Rules: ±10% watch; ±20% red.
- Anti-Gaming: Baseline auto-rotation (28d median).

### KPI-ALERT-NOISE – Alert Noise Reduction %

- Purpose: Đo hiệu quả adaptive thresholding.
- Definition: (baseline_volume - current_volume)/baseline_volume * 100.
- Data Sources: alert aggregation.
- Frequency: Weekly.
- Tier: ADAPTIVE.
- Alert Rules: <15% improvement after enablement → tuning review.
- Anti-Gaming: Baseline locked snapshot.

### KPI-INTENT-LINK – Intent Link Coverage %

- Purpose: Bảo toàn WHY trong thực thi.
- Definition: processes_with_intent / total_processes * 100.
- Data Sources: intent registry + process model index.
- Frequency: Daily.
- Tier: ADAPTIVE→PREDICTIVE.
- Alert Rules: <95% advisory; <90% block predictive modules.
- Anti-Gaming: Random process sampling cross-check.

### KPI-INTENT-STALE – Stale Intent Ratio %

- Purpose: Phát hiện intent lỗi thời so với downstream.
- Definition: stale_intent_links / total_intent_links * 100.
- Data Sources: intent freshness join.
- Frequency: Daily.
- Tier: PREDICTIVE.
- Alert Rules: >10% advisory; >15% block drift enforcement.
- Anti-Gaming: Require diff justification notes.

---

## 4. Aggregation & SLO Layer

- All KPI raw values hashed & chained (immutable provenance).
- Executive snapshot weekly: pick last stable value (no active incidents).
- Rolling window smoothing: EWMA(α=0.3) for noisy metrics (ANOM-FP, ALERT-NOISE).

## 5. Governance

| Change Type | Approval |
|-------------|----------|
| Add new KPI | CPO + CTO |
| Modify formula | CTO + Governance Engineering |
| Adjust alert thresholds | Governance Engineering + CPO (notify CEO if structural) |
| Deprecate KPI | CTO + CPO + written rationale |

## 6. Future Extensions

| Idea | Description | Priority |
|------|-------------|----------|
| Predictive KPI Weight Index | Composite governance health radar | Medium |
| Auto Tier Recommendation | Maturity model inference | High |
| KPI Drift Detection | Detect silent KPI definition creep | Medium |
| Cost-to-Control Ratio | Map operational cost vs KPI gains | Low |

---
END OF KPI CATALOG
