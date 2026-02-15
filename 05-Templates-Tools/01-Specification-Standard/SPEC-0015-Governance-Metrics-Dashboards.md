# SPEC-0015: Governance Metrics & Dashboards Specification

## Frontmatter

```yaml
spec_id: SPEC-0015
title: Governance Metrics & Dashboards - Observable Quality Governance
version: 2.0.0
status: approved
tier: PROFESSIONAL
pillar: Section 7 - Quality Assurance System
owner: Backend Lead + CTO
last_updated: 2026-01-29
tags:
  - metrics
  - dashboards
  - governance
  - observability
  - dora
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
  - SPEC-0014  # Planning Hierarchy
epic: Governance Observability
sprint: Sprint 70-75
implementation_ref: "SDLC-Orchestrator/docs/02-design/14-Technical-Specs/Governance-Metrics-Dashboards.md"
```

---

## Executive Summary

This specification defines the **governance requirements** for metrics collection, aggregation, and visualization of the quality governance system, enabling data-driven decision-making for threshold tuning, mode transitions, and continuous improvement.

**Key Governance Principles**:
- 12 metrics across 4 categories for comprehensive visibility
- Real-time and aggregated metrics for different use cases
- Role-based dashboards (CEO, CTO, Developer)
- Automated alerting for proactive intervention

**Business Value**:
- Data-driven governance mode transitions (not subjective)
- CEO time savings measurement and tracking
- Quality assurance effectiveness validation
- Developer friction monitoring and mitigation

> **Implementation Reference**: For technical implementation details (database schemas, pipeline architecture, dashboard configuration), see SDLC-Orchestrator documentation.

---

## 1. Metrics Categories

### Overview

The governance system collects **12 key metrics** across **4 categories**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE METRICS FRAMEWORK                     │
├─────────────────────────────────────────────────────────────────────┤
│  CATEGORY 1: DEVELOPER FRICTION (DF)                               │
│  ├─ DF-1: PR Latency Impact                                        │
│  ├─ DF-2: Developer Complaint Rate                                 │
│  └─ DF-3: Override/Break-Glass Usage                               │
├─────────────────────────────────────────────────────────────────────┤
│  CATEGORY 2: QUALITY ASSURANCE (QA)                                │
│  ├─ QA-1: False Positive Rate                                      │
│  ├─ QA-2: False Negative Rate                                      │
│  └─ QA-3: Vibecoding Index Accuracy                                │
├─────────────────────────────────────────────────────────────────────┤
│  CATEGORY 3: TIME SAVINGS (TS)                                     │
│  ├─ TS-1: Auto-Generation Time Saved                               │
│  ├─ TS-2: CEO Time Saved                                           │
│  └─ TS-3: PR Review Cycle Time                                     │
├─────────────────────────────────────────────────────────────────────┤
│  CATEGORY 4: GOVERNANCE MODE (GM)                                  │
│  ├─ GM-1: Mode Stability                                           │
│  ├─ GM-2: Rollback Trigger Distribution                            │
│  └─ GM-3: Break Glass Frequency                                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Functional Requirements

### FR-001: Developer Friction Metrics

**Description**: Track how governance affects developer productivity and experience.

**Requirement**:

```gherkin
GIVEN governance system is operational
WHEN developers work on pull requests
THEN the system SHALL collect developer friction metrics:

DF-1: PR Latency Impact
  - Measure additional time added to PR lifecycle by governance checks
  - Target: <10% increase in PR cycle time
  - Rollback Threshold: >25% increase triggers review

DF-2: Developer Complaint Rate
  - Measure proportion of PRs with developer frustration signals
  - Detection: Sentiment analysis, feedback forms, explicit reports
  - Target: <5% of PRs have complaints
  - Rollback Threshold: >15% triggers rollback

DF-3: Override/Break-Glass Usage
  - Track manual overrides and emergency bypasses
  - Target: <2 overrides per week (team of 10)
  - Alert Threshold: >5 overrides per day triggers review

AND the system SHALL:
  - Aggregate metrics hourly for trend analysis
  - Provide real-time snapshot for dashboards
  - Support breakdown by developer, PR size, time of day
```

---

### FR-002: Quality Assurance Metrics

**Description**: Measure effectiveness of governance quality decisions.

**Requirement**:

```gherkin
GIVEN governance system makes quality decisions
WHEN governance blocks or passes pull requests
THEN the system SHALL collect quality assurance metrics:

QA-1: False Positive Rate
  - Measure proportion of incorrect blocks (should have passed)
  - Detection: Developer reports, CTO review, auto-detection
  - Target: <10% false positive rate
  - Rollback Threshold: >20% triggers rollback

QA-2: False Negative Rate
  - Measure proportion of missed violations (passed but shouldn't have)
  - Detection: Post-merge issues, CEO feedback, security findings
  - Target: <5% false negative rate
  - Alert Threshold: >10% triggers investigation

QA-3: Vibecoding Index Accuracy
  - Measure correlation between index score and actual review time
  - Target: Strong positive correlation (r > 0.7)
  - Alert Threshold: r < 0.5 triggers recalibration
  - Expected Mapping:
    - Index <30 = <5 min review time (Green)
    - Index 30-60 = 5-15 min review time (Yellow)
    - Index 60-80 = 15-30 min review time (Orange)
    - Index >80 = >30 min review time (Red)

AND the system SHALL:
  - Calculate rates hourly with rolling 7-day window
  - Highlight accuracy outliers for investigation
  - Provide drill-down to individual PR examples
```

---

### FR-003: Time Savings Metrics

**Description**: Quantify efficiency gains from governance automation.

**Requirement**:

```gherkin
GIVEN governance system provides auto-generation features
WHEN developers use auto-generation for PRs
THEN the system SHALL collect time savings metrics:

TS-1: Auto-Generation Time Saved
  - Track time saved per PR by auto-generation features
  - Components:
    - Intent generation: ~14 min saved per PR
    - Ownership suggestions: ~1.5 min saved per PR
    - Context attachment: ~5 min saved per PR
    - Attestation fill: ~6 min saved per PR
  - Target: >20 minutes saved per PR

TS-2: CEO/Review Time Saved
  - Track reduction in senior review time
  - Baseline: Establish during WARNING mode
  - Target: 50% reduction in FULL mode
  - Collection: Manual input + automated tracking

TS-3: PR Review Cycle Time
  - Total time from PR open to final approval
  - Target: <24 hours for Green PRs (Index <30)
  - Alert Threshold: >48 hours average triggers review

AND the system SHALL:
  - Display YTD totals for time savings
  - Calculate ROI (time saved * standard rate)
  - Compare baseline vs actual for improvement tracking
```

---

### FR-004: Governance Mode Metrics

**Description**: Track governance mode stability and transitions.

**Requirement**:

```gherkin
GIVEN governance system operates in modes (OFF, WARNING, SOFT, FULL)
WHEN mode transitions occur
THEN the system SHALL collect governance mode metrics:

GM-1: Mode Stability
  - Measure frequency of mode changes (auto-rollback)
  - Target: <1 mode change per day
  - Alert Threshold: >3 changes per day = unstable

GM-2: Rollback Trigger Distribution
  - Categorize which metrics trigger rollbacks most
  - Categories: rejection_rate, latency, false_positive, complaint
  - Target: Balanced distribution (no single metric >50%)

GM-3: Break Glass Frequency
  - Track emergency bypass usage
  - Target: <1 per month in steady state
  - Collection: Incident tracking with resolution time

AND the system SHALL:
  - Log all transitions with reason and initiator
  - Calculate mean time between rollbacks (MTBR)
  - Provide timeline visualization of mode history
```

---

### FR-005: Metrics Pipeline

**Description**: System processes metrics from collection to visualization.

**Requirement**:

```gherkin
GIVEN metrics need to flow from collection to visualization
WHEN events occur in the system
THEN the system SHALL:
  - Ingest events with low latency (<1s p95)
  - Store raw events with configurable retention
  - Aggregate metrics hourly for trend analysis
  - Update snapshots frequently for real-time dashboards
  - Serve dashboard queries efficiently
AND the system SHALL handle:
  - Event deduplication (duplicate handling)
  - Exactly-once processing semantics
  - Backfill capability for missed events
  - High throughput (1000+ events/minute)
```

---

### FR-006: Dashboard Visualization

**Description**: Role-appropriate dashboards for different stakeholders.

**Requirement**:

```gherkin
GIVEN stakeholders need metrics visualization
WHEN accessing dashboards
THEN the system SHALL provide role-based dashboards:

1. Executive Dashboard (CEO/CPO):
   - Time savings overview (weekly trend, YTD total)
   - Review cycle time summary
   - Overall health status indicator
   - Top time-saving items
   - ROI calculation

2. Operational Dashboard (CTO/Tech Lead):
   - Developer friction metrics (DF-1, DF-2, DF-3)
   - Quality assurance metrics (QA-1, QA-2, QA-3)
   - Mode transition timeline
   - Rollback trigger distribution
   - Alert status

3. Team Dashboard (Developers):
   - Individual cycle time performance
   - Personal time savings
   - Quality index distribution
   - Recent feedback items

AND all dashboards SHALL:
  - Support time range selection
  - Provide drill-down capability
  - Support export for reporting
  - Load within acceptable latency (<2s)
```

---

### FR-007: Automated Alerting

**Description**: Proactive notification when metrics exceed thresholds.

**Requirement**:

```gherkin
GIVEN metrics exceed thresholds
WHEN alerting conditions are met
THEN the system SHALL send alerts:

Alert Categories:
1. Critical (P0): Rollback imminent - any threshold at 70%+ of limit
2. Warning (P1): Quality degradation - false positive/negative spikes
3. Advisory (P2): Trend concerns - CEO time not decreasing
4. Operational (P1): Mode instability - frequent transitions
5. Process (P2): Break glass overuse - pattern of bypasses

AND alerts SHALL:
  - Include context and current vs threshold values
  - Suggest remediation actions
  - Route to appropriate recipients by severity
  - Auto-resolve when condition clears
```

---

## 3. Tier-Specific Requirements

| Feature | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---------|------|----------|--------------|------------|
| **Developer Friction** | Not available | Basic (DF-1 only) | All 3 metrics | All + breakdown |
| **Quality Assurance** | Not available | QA-1 only | All 3 metrics | All + analysis |
| **Time Savings** | Not available | TS-3 only | All 3 metrics | All + ROI |
| **Governance Mode** | Not available | Not available | GM-1 only | All 3 metrics |
| **Pipeline** | Not available | Hourly only | Full pipeline | + real-time |
| **Dashboards** | Not available | Team only | All 3 dashboards | + custom |
| **Alerting** | Not available | Not available | Critical only | All 5 rules |
| **Data Retention** | Not available | 7 days | 30 days | 90 days |
| **Export** | Not available | CSV | CSV, PDF | All + API |

**Tier Summary**:
- **LITE**: No metrics (manual governance)
- **STANDARD**: Basic metrics for self-service
- **PROFESSIONAL**: Full metrics for compliance
- **ENTERPRISE**: Advanced analytics and customization

---

## 4. Health Status Calculation

### Definition

Overall governance health combines multiple metrics into a single status indicator.

### Status Levels

| Status | Description | Typical Conditions |
|--------|-------------|-------------------|
| **GREEN** | Healthy | All metrics within targets |
| **YELLOW** | Warning | Some metrics approaching thresholds |
| **RED** | Critical | One or more metrics exceeding thresholds |

### Risk Score Calculation

```
Risk Score (0-100) based on:
- Rejection rate vs 25% threshold
- Latency vs 100ms threshold
- False positive rate vs 20% threshold
- Complaint rate vs 15% threshold

Each metric contributes proportionally to overall score
Any metric at >80% of threshold triggers elevated risk
```

---

## 5. Non-Functional Requirements

### NFR-001: Performance Targets

| Operation | Target | Notes |
|-----------|--------|-------|
| Event ingestion | <1s (p95) | High volume supported |
| Aggregation completion | <5 min per hour | After hour boundary |
| Snapshot update | Every 5 seconds | For live dashboards |
| Dashboard load | <2s (p95) | With caching |
| Alert notification | <30s | From condition to delivery |

### NFR-002: Security Requirements

| Requirement | Description |
|-------------|-------------|
| Authentication | Single sign-on integration |
| Authorization | Role-based dashboard access |
| Data sanitization | No sensitive data in payloads |
| Audit trail | All overrides logged immutably |
| Rate limiting | Prevent abuse of ingestion |

---

## 6. Design Decisions

### Decision 1: Four Metrics Categories

**Rationale**: Comprehensive coverage without overwhelming stakeholders.

**Categories**:
- Developer Friction: Adoption enablement
- Quality Assurance: Effectiveness measurement
- Time Savings: ROI justification
- Governance Mode: Stability tracking

### Decision 2: Role-Based Dashboards

**Rationale**: Different stakeholders need different views.

**Approach**: Three dashboard tiers optimized for:
- Executives: High-level health and ROI
- Operations: Detailed metrics for tuning
- Developers: Personal performance and feedback

### Decision 3: Progressive Alerting

**Rationale**: Alert fatigue reduces effectiveness.

**Approach**: Severity-based routing with auto-resolution:
- P0: Immediate action required
- P1: Review within hours
- P2: Track for trends

### Decision 4: Dual Storage (Snapshot + Aggregate)

**Rationale**: Different access patterns require different optimizations.

**Approach**:
- Snapshots: Frequent updates, short retention, dashboard queries
- Aggregates: Hourly rollup, long retention, trend analysis

---

## 7. Acceptance Criteria

### AC-001: Metric Collection

```gherkin
GIVEN the governance system is operational
WHEN a PR is processed through governance
THEN all applicable metrics are collected
AND metrics appear in dashboards within acceptable latency
```

### AC-002: Health Status Accuracy

```gherkin
GIVEN metrics are being collected
WHEN a metric exceeds its threshold
THEN health status changes appropriately (GREEN → YELLOW → RED)
AND status reflects actual governance health
```

### AC-003: Alert Delivery

```gherkin
GIVEN alerting rules are configured
WHEN a metric exceeds its alert threshold
THEN appropriate recipients receive notification
AND alert includes actionable information
AND alert auto-resolves when condition clears
```

### AC-004: Dashboard Access Control

```gherkin
GIVEN role-based access is configured
WHEN a user accesses dashboards
THEN only authorized dashboards are visible
AND data is appropriate for user's role
```

### AC-005: Time Savings Calculation

```gherkin
GIVEN auto-generation features are used
WHEN time savings are calculated
THEN calculations accurately reflect actual savings
AND ROI is displayed with configurable rate
```

---

## 8. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Metric inaccuracy | Medium | High | Calibration period, manual validation |
| Alert fatigue | Medium | Medium | Severity-based routing, auto-resolution |
| Dashboard performance | Low | Medium | Caching, query optimization |
| Data privacy | Low | High | Anonymization, access controls |

---

## 9. References

### Source Documents
- **SPEC-0001**: Anti-Vibecoding (progressive enforcement)
- **SPEC-0004**: Policy Guards Design
- **ADR-041**: Stage Dependency Matrix

### External Standards
- DORA Metrics: DevOps Research & Assessment
- SPACE Framework: Developer Productivity Metrics

---

## Document Control

| Field | Value |
|-------|-------|
| **Spec ID** | SPEC-0015 |
| **Version** | 2.0.0 |
| **Status** | APPROVED |
| **Author** | Backend Lead |
| **Reviewer** | CTO |
| **Last Updated** | 2026-01-29 |
| **Framework Version** | 6.0.5 |

---

**Pure Methodology Notes**:
- This specification defines WHAT metrics and dashboards governance requires
- For HOW to implement (database schemas, pipeline architecture, dashboard configuration), see SDLC-Orchestrator documentation
- Metric targets are governance goals, implementation may vary by tool
- Dashboard design is conceptual; specific visualizations are implementation details

---

**End of Specification**
