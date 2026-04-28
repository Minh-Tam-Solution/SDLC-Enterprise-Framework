# SDLC Quality Assurance System (Section 7)
## Anti-Vibecoding Governance Framework

**Version**: 1.0.0
**Framework Version**: SDLC 5.3.0
**Status**: APPROVED
**Date**: January 27, 2026
**Authority**: CTO + CPO + CEO Approved
**Related**: SDLC-Core-Methodology.md, Governance-Compliance/

---

## 1. Overview

### 1.1 Purpose

The SDLC Quality Assurance System provides **anti-vibecoding governance** to ensure code quality remains high even as AI coding assistants become primary code generators. It addresses the growing concern that AI-generated code ("vibecoding") lacks the architectural rigor, contextual understanding, and ownership accountability of human-reviewed code.

**Core Principle:**
> "Governance must be the FASTEST way to ship quality code, not a bureaucratic obstacle."

### 1.2 Scope

This document applies to:
- All SDLC Orchestrator implementations
- Teams using AI coding assistants (Claude, Cursor, Copilot, etc.)
- Projects with STANDARD tier or above (LITE tier: simplified rules)
- Any codebase where AI-generated code exceeds 20% of changes

### 1.3 Problem Statement

**The "Vibecoding" Crisis:**

| Metric | Before AI | With AI (No Governance) | With AI + Governance |
|--------|-----------|--------------------------|----------------------|
| Code velocity | 100 LOC/day | 500 LOC/day | 400 LOC/day |
| Bug rate | 2% | 8% | 2.5% |
| Architectural debt | Low | HIGH | Low |
| CEO review time | 20h/week | 40h/week | 10h/week |
| Developer understanding | 90% | 45% | 85% |

**Key Insight:**
> AI increases code velocity but creates quality and ownership problems. Governance restores quality while preserving velocity gains.

---

## 2. Vibecoding Index

### 2.1 Definition

The **Vibecoding Index** is a composite score (0-100) measuring the risk that code lacks proper human oversight, architectural rigor, or contextual understanding.

**Score Interpretation:**

| Range | Category | Color | Routing |
|-------|----------|-------|---------|
| 0-30 | Green | 🟢 | Auto-approve (no CEO involvement) |
| 31-60 | Yellow | 🟡 | Tech Lead review required |
| 61-80 | Orange | 🟠 | CEO should review (recommended) |
| 81-100 | Red | 🔴 | CEO must review (mandatory) |

### 2.2 Five Signals

The Vibecoding Index is calculated from five weighted signals:

```yaml
vibecoding_index = (
    architectural_smell × 0.25 +
    abstraction_complexity × 0.15 +
    ai_dependency_ratio × 0.20 +
    change_surface_area × 0.20 +
    drift_velocity × 0.20
)
```

#### Signal 1: Architectural Smell (25%)

**Definition**: Detects anti-patterns that violate SOLID principles.

**Patterns Detected:**
- **God Class**: Class >500 lines OR >30 methods
- **Feature Envy**: Method calls external classes >2x more than own
- **Shotgun Surgery**: Single change touches >10 files
- **Parallel Inheritance**: Two class hierarchies with matching names
- **Data Clumps**: Same 3+ parameters repeated across 3+ methods

**CEO Rationale:**
> "God classes and shotgun surgery = rework later. This is the #1 signal from 3 years of NQH code reviews."

#### Signal 2: Abstraction Complexity (15%)

**Definition**: Measures over-engineering through excessive abstraction.

**Patterns Detected:**
- **Deep Inheritance**: Inheritance depth >3 levels
- **Interface Proliferation**: >5 interfaces for single implementation
- **Generic Type Depth**: Nested generics >3 levels (T<U<V<W>>>)
- **Factory Pattern Abuse**: Factory for single implementation
- **Premature Abstraction**: Abstract class with 1 concrete implementation

**CEO Rationale:**
> "Over-engineering slows development more than under-engineering."

#### Signal 3: AI Dependency Ratio (20%)

**Definition**: Measures AI-generated code percentage and human modification ratio.

**Red Flag Condition:**
```
AI Dependency Ratio > 80% AND Human Modification < 10%
→ "Copy-paste without understanding"
```

**Scoring:**
| AI Ratio | Human Modification | Score | Interpretation |
|----------|-------------------|-------|----------------|
| <40% | Any | 0-20 | Mostly human |
| 40-60% | Any | 30 | Balanced |
| 60-80% | >10% | 50 | Moderate AI, reviewed |
| >80% | >10% | 70 | High AI, reviewed |
| >80% | <10% | 100 | RED FLAG: Copy-paste |

**CEO Rationale:**
> "AI code without human review = liability. Developer must understand every line they ship."

#### Signal 4: Change Surface Area (20%)

**Definition**: Measures coordination risk by counting touched files, modules, and contracts.

**Factors:**
| Factor | Weight | Scoring |
|--------|--------|---------|
| Files Changed | 30% | min(100, file_count × 5) |
| Modules Touched | 25% | min(100, module_count × 10) |
| API Contracts Affected | 25% | min(100, api_count × 20) |
| Database Schema Touched | 15% | 100 if touched, 0 otherwise |
| Security-Sensitive Files | 5% | 100 if touched, 0 otherwise |

**CEO Rationale:**
> "Touching too many files = coordination risk. Keep PRs focused."

#### Signal 5: Drift Velocity (20%)

**Definition**: Measures codebase divergence rate over 7 days.

**Metrics:**
- New patterns introduced: 10 points per new pattern
- Deprecated patterns used: 20 points per deprecated usage
- Inconsistent naming: 5 points per inconsistency
- Style violations: 1 point per violation

**Formula:**
```
drift_velocity_score = min(100, total_severity / 7.0)
```

**CEO Rationale:**
> "Codebase diverging = technical debt accumulating. Consistency matters."

### 2.3 MAX CRITICALITY OVERRIDE

**Principle:**
> "One-line change to auth.py can score 0 by algorithm but is still HIGH RISK."

**Critical Paths (Auto-Boost to Red):**

```yaml
critical_paths:
  security:
    - "auth/**"
    - "security/**"
    - "**/authentication*"
    - "**/authorization*"
    - "**/jwt*"
    - "**/oauth*"

  payment:
    - "payment/**"
    - "billing/**"
    - "**/stripe*"
    - "**/payment_service*"

  database_schema:
    - "prisma/schema.prisma"
    - "migrations/**"
    - "alembic/**"
    - "**/models/*.py"

  infrastructure:
    - "docker-compose*.yml"
    - "Dockerfile"
    - "k8s/**"
    - ".github/workflows/**"

  secrets:
    - "**/.env*"
    - "**/secrets*"
    - "**/credentials*"
```

**Override Behavior:**
```python
if file_matches_critical_path(submission):
    index = max(calculated_index, 80)  # Force Red
    routing = "ceo_must_review"
```

---

## 3. CEO Time Optimization

### 3.1 Problem

**Baseline (No Governance):**
- CEO reviews 100% of PRs manually
- CEO spends 40h/sprint on governance activities
- 80% of PRs are "safe" (Index <30) but CEO reviews anyway
- CEO is the bottleneck for every merge

### 3.2 Solution: Progressive Routing

**Routing Logic:**

```python
def route_submission(vibecoding_index, critical_override):
    if critical_override:
        return "ceo_must_review"  # Red - Critical path

    if vibecoding_index >= 81:
        return "ceo_must_review"  # Red
    elif vibecoding_index >= 61:
        return "ceo_should_review"  # Orange
    elif vibecoding_index >= 31:
        return "tech_lead_review"  # Yellow
    else:
        return "auto_approve"  # Green
```

**CEO Time Savings Projection:**

| Week | CEO Hours | Reduction | Green Auto-Approve Rate |
|------|-----------|-----------|-------------------------|
| Baseline | 40h | - | 0% |
| Week 2 | 30h | -25% | 60% |
| Week 4 | 20h | -50% | 70% |
| Week 8 | 10h | -75% | 85% |

### 3.3 CEO Contract

**CEO Commits To:**
1. NOT reviewing Green PRs (Index <30)
2. Tracking time weekly for measurement
3. Providing override feedback for calibration
4. Weekly dashboard review

**System Commits To:**
1. Never auto-approving critical path changes
2. Explainable scores (every score >30 justified)
3. Weekly calibration based on CEO overrides
4. Kill switch if CEO time increases

---

## 4. Developer Experience

### 4.1 Friction Target

**Baseline:** 30 minutes per PR (manual compliance)
**Target:** <5 minutes per PR (auto-generation + quick confirmation)

**Friction Reduction:** 83%

### 4.2 Auto-Generation Layer

**Four Components:**

| Component | Latency Target | Fallback | Developer Action |
|-----------|----------------|----------|------------------|
| Intent Statement | <10s (LLM) | Template | Confirm/Edit |
| Ownership Annotation | <2s (deterministic) | Directory pattern | Confirm |
| Context Attachment | <5s (ADR search) | Heuristic | Confirm |
| AI Code Attestation | <3s (session pre-fill) | Empty form | Fill required fields |

### 4.3 Fallback Chain (2-Minute Guarantee)

**Principle:**
> "Developer can ALWAYS submit within 2 minutes, even if all systems fail."

**Fallback Chain:**
```
LEVEL 1: LLM Generation (Ollama qwen3:32b)
         ↓ timeout (10s) or low quality (<0.7)
LEVEL 2: Template Generation (< 150ms)
         ↓ template not found
LEVEL 3: Minimal Placeholder (< 50ms)
         ↓ all systems fail
LEVEL 4: Manual Entry (< 2 min developer time)
         → NEVER BLOCKED
```

### 4.4 Actionable Feedback

**Every rejection includes:**
1. **What failed**: Specific policy violation
2. **Why it matters**: Business impact explanation
3. **How to fix**: CLI command to resolve
4. **Documentation**: Link to detailed guidance

**Example:**
```yaml
rejection:
  what: "Missing ownership annotation"
  why: "Every file must have an owner for accountability"
  how: "sdlc add-ownership --file backend/app/services/new_service.py"
  docs: "https://docs.sdlc.dev/ownership-requirements"
```

---

## 5. Governance Modes

### 5.1 Progressive Enforcement

**Four Modes:**

| Mode | Behavior | Use Case |
|------|----------|----------|
| **OFF** | No governance | Emergency/Debugging |
| **WARNING** | Log violations, don't block | Initial rollout, calibration |
| **SOFT** | Block critical paths only | Building trust |
| **FULL** | Block all violations | Production governance |

### 5.2 Rollout Timeline

```yaml
Week 1: WARNING mode
  - All governance violations logged
  - No PRs blocked
  - CEO reviews all Red/Orange
  - Calibrate signal weights

Week 2: SOFT mode (if Week 1 successful)
  - Critical path changes blocked
  - Other violations logged with warnings
  - Tech Lead reviews Yellow
  - CEO reviews Red/Orange only

Week 3-4: FULL mode (if Week 2 successful)
  - All policy violations blocked
  - Green PRs auto-approved
  - Tech Lead reviews Yellow
  - CEO reviews Red/Orange only

Week 5+: Maintain FULL mode
  - Weekly calibration
  - Continuous improvement
```

### 5.3 Kill Switch

**Auto-Rollback Triggers:**

| Criterion | Threshold | Duration | Action |
|-----------|-----------|----------|--------|
| Rejection Rate | >80% | 1 hour | Rollback to WARNING |
| Latency P95 | >500ms | 5 min | Rollback to WARNING |
| False Positive Rate | >20% | 30 min | Rollback to WARNING |
| Developer Complaints | >5/day | 1 day | Rollback to WARNING |

**Kill Switch Behavior:**
```python
if any_trigger_exceeded():
    governance_mode = "WARNING"
    notify(["CEO", "CTO", "Tech Leads"])
    schedule_emergency_review(hours=2)
    log_audit_event("kill_switch_triggered")
```

---

## 6. Quality Gates Integration

### 6.1 Gate-Governance Mapping

| Gate | Governance Integration |
|------|------------------------|
| **G0.1** | Problem Validated | N/A |
| **G0.2** | Solutions Explored | N/A |
| **G1** | Legal + Market | Intent validation begins |
| **G2** | Architecture | ADR linkage required |
| **G3** | Code + Tests | Full Vibecoding Index evaluation |
| **G4** | Deployed | Post-deployment governance audits |

### 6.2 PR Governance Checklist

**Before PR can merge:**

```yaml
governance_checklist:
  mandatory:
    - intent_statement_present: true
    - ownership_declared: true
    - vibecoding_index_calculated: true
    - routing_decision_made: true

  if_index_above_30:
    - explainability_generated: true
    - suggested_focus_provided: true
    - baseline_comparison_included: true

  if_index_above_60:
    - tech_lead_review_complete: true

  if_index_above_80:
    - ceo_review_complete: true

  if_critical_path:
    - ceo_review_complete: true
    - security_scan_pass: true
```

---

## 7. Metrics & Monitoring

### 7.1 Primary Metrics (CEO Dashboard)

| Metric | Baseline | Week 4 Target | Week 8 Target |
|--------|----------|---------------|---------------|
| CEO Time/Sprint | 40h | 20h (-50%) | 10h (-75%) |
| PRs Auto-Approved | 0% | 70% | 85% |
| Governance Autonomy | 0% | 70% | 85% |

### 7.2 Secondary Metrics (Tech Dashboard)

| Metric | Target |
|--------|--------|
| Developer Friction | <5 min per PR |
| First Pass Rate | >85% by Week 8 |
| Auto-Generation Usage | >80% |
| Developer NPS | >50 |

### 7.3 Tertiary Metrics (Ops Dashboard)

| Metric | Target |
|--------|--------|
| Vibecoding Index Avg | <30 |
| Bypass Incidents | 0 |
| False Positive Rate | <10% |
| System Uptime | >99% |
| Latency P95 | <500ms |

---

## 8. Calibration Process

### 8.1 Weekly Calibration

**Data Collection:**
- CEO overrides (approved Red → reject, or rejected Green → approve)
- False positives (CEO disagrees with Red/Orange)
- False negatives (CEO escalates Yellow/Green)

**Weight Adjustment Algorithm:**
```python
for signal in signals:
    if signal contributed to false_positive:
        signal.weight *= 0.90  # Decrease 10%
    if signal missed true_positive:
        signal.weight *= 1.10  # Increase 10%

# Renormalize to sum = 1.0
total = sum(signal.weight for signal in signals)
for signal in signals:
    signal.weight /= total
```

### 8.2 Calibration Session Format

**Duration:** 2 hours (CEO + Tech Lead)

**Agenda:**
1. Review week's overrides (30 min)
2. Analyze false positives/negatives (45 min)
3. Adjust signal weights (30 min)
4. Test new weights on sample PRs (15 min)

**Output:**
- Updated `governance_signals.yaml`
- Calibration notes for next session

---

## 9. Tier-Specific Rules

### 9.1 LITE Tier

**Simplified Rules:**
- Vibecoding Index: Calculated but not blocking
- Mandatory signals: AI Dependency Ratio only
- CEO involvement: Only for Index >80
- Documentation: Intent statement optional

### 9.2 STANDARD Tier

**Full Rules:**
- Vibecoding Index: All 5 signals
- Blocking: Index >60 requires approval
- CEO involvement: Index >60
- Documentation: All 4 artifacts required

### 9.3 PROFESSIONAL Tier

**Enhanced Rules:**
- Vibecoding Index: 5 signals + custom signals
- Blocking: Index >50 requires approval
- CEO involvement: Index >50 or critical path
- Documentation: All artifacts + ADR linkage mandatory

### 9.4 ENTERPRISE Tier

**Maximum Governance:**
- Vibecoding Index: All signals + regulatory compliance
- Blocking: Index >40 requires approval
- CEO involvement: All Orange/Red + audit committee
- Documentation: Full audit trail, 7-year retention

---

## 10. Implementation Checklist

### 10.1 Framework Implementation

- [ ] Create this document (SDLC-Quality-Assurance-System.md)
- [ ] Update CONTENT-MAP.md with new files
- [ ] Update CHANGELOG.md for Framework 5.3.0
- [ ] Create signal calibration templates

### 10.2 Orchestrator Implementation

- [ ] Implement 5-signal Vibecoding Index
- [ ] Create auto-generation layer (4 generators)
- [ ] Build CEO/Tech/Ops dashboards
- [ ] Implement kill switch automation
- [ ] Deploy 14-table governance database

### 10.3 Rollout Implementation

- [ ] Week 1: WARNING mode (calibration)
- [ ] Week 2: SOFT mode (critical paths)
- [ ] Week 3-4: FULL mode (all policies)
- [ ] Week 5+: Maintenance + optimization

---

## Related Documents

**Framework:**
- [SDLC-Core-Methodology.md](./SDLC-Core-Methodology.md) - 10-Stage lifecycle
- [SDLC-Stage-Dependencies.md](./SDLC-Stage-Dependencies.md) - Stage transition rules
- [SDLC-Agentic-Core-Principles.md](./SDLC-Agentic-Core-Principles.md) - AI Governance Principles

**Orchestrator Implementation:**
- `/docs/governance-v1/` - Governance System v1.0 implementation docs
- `/docs/phase-0/` - Phase 0 technical deliverables
- `/backend/app/services/governance/` - Service implementations

**Policies:**
- CEO-WORKFLOW-CONTRACT.md - CEO time commitments
- AUTO-GENERATION-FAIL-SAFE-POLICY.md - 2-minute fallback guarantee
- VIBECODING-INDEX-EXPLAINABILITY-SPEC.md - Explainability requirements

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2026-01-27 | Initial version - Anti-Vibecoding Governance | CTO (Tai) |

---

## Approval

**CTO Review**: ✅ APPROVED
**CPO Review**: ✅ APPROVED
**CEO Review**: ✅ APPROVED (CEO Time Optimization focus)

**Framework Release**: SDLC 5.3.0 (January 27, 2026)
