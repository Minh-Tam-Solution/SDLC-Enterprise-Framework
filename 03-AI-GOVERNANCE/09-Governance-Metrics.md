# Governance Metrics & KPIs

**Version**: 6.0.6
**Status**: ACTIVE
**Date**: February 15, 2026
**Pillar**: Core AI Governance
**Purpose**: Measurable KPIs for governance effectiveness across all tiers

---

## Overview

Governance without measurement is governance theater. This document defines the key performance indicators (KPIs) that the Orchestrator tracks to measure whether AI governance is actually working — reducing risk, improving quality, and maintaining velocity.

---

## Metric Categories

### 1. Vibecoding Index (Quality Signal)

The Vibecoding Index (0-100) measures AI contribution quality. Lower is better.

| Signal | Weight | Measurement | Target |
|--------|--------|-------------|--------|
| AI LOC ratio | 25% | `ai_generated_lines / total_lines` per PR | <60% |
| Test coverage delta | 25% | Coverage after AI commit − before | ≥0% (no regression) |
| Review depth | 20% | `human_review_comments / ai_generated_LOC` | >0.02 (1 comment per 50 LOC) |
| Planning artifact | 15% | Boolean: was planning mode used for HIGH+ risk? | 100% for HIGH/CRITICAL |
| Context freshness | 15% | Hours since last AGENTS.md update | <24h |

**Aggregate scoring**:
```
vibecoding_index = (
    ai_loc_ratio * 25 +
    (1 - test_coverage_delta_normalized) * 25 +
    (1 - review_depth_normalized) * 20 +
    (0 if planning_used else 1) * 15 +
    context_staleness_normalized * 15
)
```

**Zone routing**:

| Zone | Index Range | Color | Routing |
|------|-------------|-------|---------|
| GREEN | 0-30 | Green | Auto-approve, log only |
| YELLOW | 31-60 | Yellow | Tech Lead review required |
| ORANGE | 61-80 | Orange | Senior Engineer + CEO review |
| RED | 81-100 | Red | CTO + CEO must review |

**Dashboard metric**: Average Vibecoding Index per team per sprint (trend line).

---

### 2. Gate Pass Rate (Process Health)

Measures how often gates pass on first attempt vs requiring rework.

| Metric | Formula | Target | Warning |
|--------|---------|--------|---------|
| First-pass rate | `gates_passed_first_attempt / total_gate_evaluations` | >70% | <50% |
| Rejection rate | `gates_rejected / total_gate_submissions` | <20% | >35% |
| Re-evaluation count | `avg(evaluations_per_gate)` | <2.0 | >3.0 |
| Time to pass | `avg(gate_approved_at - gate_created_at)` | <48h | >96h |
| Stale evaluation rate | `EVALUATED_STALE_count / EVALUATED_count` | <15% | >30% |

**Interpretation**:
- High first-pass rate → teams understand exit criteria
- High rejection rate → either criteria too strict OR teams skipping planning
- High re-evaluation → evidence quality issues (teams submitting incomplete work)
- High stale rate → evidence uploaded after evaluation (process ordering problem)

---

### 3. Evidence Coverage (Audit Completeness)

Measures whether gates have sufficient evidence before approval.

| Metric | Formula | Target | Warning |
|--------|---------|--------|---------|
| Evidence completeness | `gates_with_all_evidence / gates_approved` | 100% | <95% |
| Evidence integrity | `sha256_server_matches / total_uploads` | 100% | <100% |
| Evidence freshness | `avg(evidence_uploaded_at - gate_created_at)` | <24h | >72h |
| Missing evidence overrides | `approved_with_missing_evidence / total_approved` | 0% | >0% |
| Evidence per gate | `avg(evidence_count per gate)` | ≥2 | <1 |

**Critical alert**: If `approved_with_missing_evidence > 0`, governance mode may be bypassed. Investigate immediately.

---

### 4. Governance Mode Distribution (Adoption)

Tracks which governance mode projects are using.

| Metric | Formula | Target | Warning |
|--------|---------|--------|---------|
| FULL mode adoption | `projects_full_mode / active_projects` | >50% | <30% |
| OFF mode projects | `projects_off_mode / active_projects` | <10% | >20% |
| Mode escalation rate | `mode_upgrades / total_mode_changes` | >60% | <40% |
| Override frequency | `CTO_overrides_per_sprint` | <3 | >5 |

**Healthy progression**: OFF → SOFT → WARNING → FULL as teams mature.

---

### 5. Principle Adherence (Behavioral)

Measures whether teams follow the 7 AI Governance Principles.

| Principle | Metric | Target |
|-----------|--------|--------|
| P1: AI-Human Collaboration | % of AI PRs with human review | 100% |
| P2: Agent Accountability | % of AI commits with attribution tag | >95% |
| P3: Planning Mode | % of HIGH+ risk changes with planning artifact | 100% |
| P4: Verification-First | % of HIGH+ risk changes with TDD evidence | >90% |
| P5: Context Management | AGENTS.md freshness (% projects <24h) | >80% |
| P6: Tool Evaluation | New tools with evaluation scorecard | 100% |
| P7: Anti-Patterns | Anti-pattern violations per sprint | <3 |

---

## Tier-Specific Targets

Not all tiers need the same rigor. Targets scale with tier:

| Metric | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|--------|------|----------|--------------|------------|
| Vibecoding Index target | <60 | <45 | <35 | <25 |
| Gate first-pass rate | >50% | >60% | >70% | >80% |
| Evidence completeness | >80% | >90% | >95% | 100% |
| Governance mode | SOFT+ | WARNING+ | FULL | FULL |
| Planning artifact required | CRITICAL only | HIGH+ | MEDIUM+ | ALL |
| Review depth target | >0.01 | >0.02 | >0.03 | >0.05 |

---

## Dashboard Views

### Sprint Summary (Weekly)

```
Sprint N — Governance Summary
═══════════════════════════════

  Vibecoding Index (avg):  34  ██████████░░░░░░░░░░  YELLOW
  Gate First-Pass Rate:    72% ██████████████░░░░░░  ✅ On target
  Evidence Completeness:   98% ███████████████████░  ✅ On target
  Rejection Rate:          12% ██░░░░░░░░░░░░░░░░░░  ✅ Healthy
  Active Mode:             FULL (3 projects), WARNING (1), SOFT (1)

  Top Issues:
    ⚠ 2 gates had EVALUATED_STALE (evidence after evaluation)
    ⚠ 1 project AGENTS.md >48h stale
    ✅ 0 integrity failures
    ✅ 0 missing evidence overrides
```

### Team Comparison (Monthly)

| Team | VI (avg) | First-Pass | Evidence | Mode | Trend |
|------|----------|------------|----------|------|-------|
| Backend | 28 | 78% | 100% | FULL | ↑ Improving |
| Frontend | 42 | 65% | 95% | WARNING | → Stable |
| DevOps | 18 | 85% | 100% | FULL | ↑ Improving |
| Mobile | 55 | 52% | 88% | SOFT | ↓ Needs attention |

---

## Alerting Thresholds

| Severity | Condition | Action |
|----------|-----------|--------|
| **P0 (Critical)** | Evidence integrity failure (`sha256` mismatch) | Block gate, notify CTO |
| **P0 (Critical)** | Gate approved with missing evidence | Audit, notify CTO |
| **P1 (High)** | Vibecoding Index RED zone (>80) for 2+ sprints | CTO review meeting |
| **P1 (High)** | Gate first-pass rate <50% for 2+ sprints | Process review |
| **P2 (Medium)** | AGENTS.md stale >72h | Warn team lead |
| **P2 (Medium)** | Rejection rate >35% | Review exit criteria |
| **P3 (Low)** | Governance mode OFF for >30 days | Recommend escalation |

---

## Implementation in Orchestrator

These metrics are computed by the Orchestrator backend and exposed via:

| Endpoint | Purpose |
|----------|---------|
| `GET /api/v1/governance/metrics/summary` | Sprint-level summary |
| `GET /api/v1/governance/metrics/vibecoding-index` | Per-PR vibecoding index |
| `GET /api/v1/governance/metrics/gate-pass-rate` | Gate pass/fail trends |
| `GET /api/v1/governance/metrics/evidence-coverage` | Evidence completeness |
| `GET /api/v1/governance/metrics/team-comparison` | Cross-team comparison |

Data sources:
- Gate state machine transitions → `gate_status_history` table
- Evidence uploads → `evidence` table (`sha256_client`, `sha256_server`, `criteria_snapshot_id`)
- PR metadata → GitHub webhook integration
- AGENTS.md freshness → Context Authority service

---

## Related Documents

- [08-Governance-Decision-Matrix.md](08-Governance-Decision-Matrix.md) — Principle → enforcement mapping
- [01-AI-Human-Collaboration.md](01-AI-Human-Collaboration.md) — Principle 1
- [07-Anti-Patterns.md](07-Anti-Patterns.md) — What NOT to do
- [../../02-Core-Methodology/SDLC-Quality-Assurance-System.md](../02-Core-Methodology/SDLC-Quality-Assurance-System.md) — Vibecoding Index definition

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: February 15, 2026
**Framework**: SDLC 6.0.6
