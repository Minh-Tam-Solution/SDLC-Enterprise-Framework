---
title: "SDLC Quality Gates & Assurance Framework"
version: "6.3.0"
ring: 1
sdlc_version: "6.3.0"
last_updated: "2026-03-18"
status: "ACTIVE"
pillar: "Section 7: Quality Assurance + Pillar 4: Quality Gates"
consolidates:
  - "SDLC-Quality-Gates-Assurance-Framework.md (v6.3.0)"
  - "SDLC-Quality-Gates-Assurance-Framework.md (v6.3.0)"
---

# SDLC Quality Gates & Assurance Framework

> **Ring 1 (Core)** — Unified quality governance: gate definitions + anti-vibecoding + security requirements.
> Consolidates Section 7 (Quality Assurance) and Pillar 4 (Quality Gates) into one reference.

---

# PART 1: Anti-Vibecoding Governance (Section 7)

> Originally: SDLC-Quality-Gates-Assurance-Framework.md (v6.3.0)

## Anti-Vibecoding Governance Framework

**Version**: 1.0.0
**Framework Version**: SDLC 6.3.0
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
- All platforms implementing this framework
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
  how: "sdlc add-ownership --file services/new_service.py"
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

## 6.3 Fix-First Review Protocol (NEW in 6.3.0)

> **Source**: gstack methodology analysis (2026-03-29). Closes the gap between "detect issues" and "resolve issues."
> **Principle**: Every finding gets ACTION, not just a report. No finding is "acknowledged and deferred" without explicit justification.

### The Problem

Traditional review produces a findings list. Then what? Teams triage, argue priorities, defer, and eventually forget. The gap between "issue found" and "issue fixed" is where quality dies.

### The Protocol

Every review finding (code review, gate evaluation, security scan, QA test) is classified into exactly one of two categories:

| Category | Criteria | Action | Examples |
|----------|----------|--------|----------|
| **AUTO-FIX** | Deterministic, mechanical, single correct answer | Fix immediately, no human input needed | Unused imports, missing null checks, formatting violations, typo in variable name, missing type annotation |
| **ASK** | Requires judgment, multiple valid options, or domain knowledge | Batch into single human decision point | Architecture change, business logic question, performance vs readability tradeoff, security approach choice |

### Classification Heuristic

```
For each finding:
  1. Is there exactly ONE correct fix? → AUTO-FIX
  2. Does it require understanding business context? → ASK
  3. Could a junior developer fix it without asking anyone? → AUTO-FIX
  4. Does fixing it change behavior, not just form? → ASK
  5. Is it a style/lint/format issue with a defined standard? → AUTO-FIX
  6. When in doubt → ASK (safer to ask than to auto-fix wrong)
```

### Execution Flow

```
Step 1: CLASSIFY
  Review produces N findings
  Each finding tagged AUTO-FIX or ASK

Step 2: AUTO-FIX (immediate)
  Apply all AUTO-FIX items
  Output per fix: [AUTO-FIXED] [file:line] Problem → What was done
  No human approval needed

Step 3: BATCH-ASK (single decision point)
  Present all ASK items in ONE interaction (not one-by-one)
  Per item: Finding, Options (Fix/Skip/Defer), Recommendation
  Human decides once for entire batch

Step 4: APPLY (approved fixes)
  Apply human-approved fixes
  Output: what was fixed, what was skipped (with reason)

Step 5: VERIFY
  Run tests after all fixes
  If tests fail → retry fix (max 3 attempts per Dev↔QA loop)
  If 3 attempts fail → escalate to human with root cause
```

### Gate Integration

| Gate | Fix-First Application |
|------|----------------------|
| **G-Sprint** | Code review findings → Fix-First before merge |
| **G3** | QA findings + SAST results → Fix-First before ship |
| **G4** | Security scan + dependency audit → Fix-First before deploy |

### Tier-Specific Rules

| Tier | AUTO-FIX Scope | ASK Threshold |
|------|---------------|---------------|
| **LITE** | Style + obvious bugs only | Everything else → ASK |
| **STANDARD** | + Security lint findings | Judgment calls → ASK |
| **PROFESSIONAL** | + Performance improvements | Architecture changes → ASK |
| **ENTERPRISE** | + Compliance fixes | Regulatory items → always ASK |

### Anti-Pattern: "Acknowledged and Deferred"

**Banned**: "Finding acknowledged, will fix in next sprint." This is how v1 accumulated 78 skip/xfail markers.

**Required**: Every finding must result in one of:
- **FIXED** (auto or human-approved)
- **SKIPPED** (human decision with documented reason)
- **DEFERRED** (logged to TODOS.md with deadline — max 1 sprint)

No finding exits the protocol without a disposition.

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

- [ ] Create this document (SDLC-Quality-Gates-Assurance-Framework.md)
- [ ] Update CONTENT-MAP.md with new files
- [ ] Update CHANGELOG.md for Framework 6.3.0
- [ ] Create signal calibration templates

### 10.2 Automation Implementation

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


---

# PART 2: Quality & Security Gate Requirements

> Originally: SDLC-Quality-Gates-Assurance-Framework.md (v6.3.0)

## Purpose

This document defines **quantitative quality and security thresholds** that MUST be met at each gate before proceeding to the next stage. Quality and security are integrated throughout the lifecycle, not bolted on at the end.

**Key Principle**: Quality is not subjective - it's measured.

---

## Part 1: Quality Requirements by Tier

### LITE Tier (1-2 people)

```yaml
Code Quality:
  - Linting: Manual (IDE warnings addressed)
  - Tests: Unit tests for critical paths
  - Coverage: No minimum (but encouraged)
  - Review: Self-review or AI review

CI/CD:
  - Build: Manual or basic CI
  - Deploy: Manual deployment acceptable

Metrics:
  - None required (tracking optional)
```

### STANDARD Tier (3-10 people)

```yaml
Code Quality:
  - Linting: PASS (ESLint, Ruff, etc.)
  - Formatting: Enforced (Prettier, Black)
  - Tests: Unit + basic integration
  - Coverage: ≥60% unit test coverage
  - Review: 1+ reviewer required

CI/CD:
  - Build: Automated (GitHub Actions, GitLab CI)
  - Tests: Run on every PR
  - Deploy: Automated staging deployment

Metrics (DORA - Monthly):
  - Deployment Frequency: Weekly to monthly
  - Lead Time: 1 week to 1 month
  - MTTR: <1 week
  - Change Failure Rate: <30%
```

### PROFESSIONAL Tier (10-50 people)

```yaml
Code Quality:
  - Linting: PASS (zero warnings in CI)
  - Formatting: Auto-enforced (pre-commit hooks)
  - Type Checking: PASS (mypy, TypeScript strict)
  - Tests: Unit + Integration + E2E
  - Coverage:
      Unit: ≥80%
      Integration: ≥70%
      E2E: Critical paths covered
  - Review: 2+ reviewers required
  - ADRs: Required for architectural decisions

CI/CD:
  - Build: Automated with caching
  - Tests: Parallel execution
  - Security: SAST scan ({SAST_tool})
  - Deploy: Blue-green or canary

Metrics (DORA - Weekly):
  - Deployment Frequency: Daily to weekly
  - Lead Time: 1 day to 1 week
  - MTTR: <1 day
  - Change Failure Rate: <20%

Performance:
  - API Latency: <200ms p95
  - Page Load: <3s
  - Database Query: <100ms p95
```

### ENTERPRISE Tier (50+ people)

```yaml
Code Quality:
  - All PROFESSIONAL requirements, PLUS:
  - Coverage:
      Unit: ≥95%
      Integration: ≥90%
      E2E: All critical + edge cases
  - Review: 2+ senior reviewers for core changes
  - Architecture Review: Required for cross-team changes

CI/CD:
  - Build: <5 minutes
  - Tests: <10 minutes total
  - Security: SAST + DAST + dependency scan
  - Deploy: Feature flags, gradual rollout

Metrics (DORA - Daily):
  - Deployment Frequency: Multiple per day
  - Lead Time: <1 hour to <1 day
  - MTTR: <1 hour
  - Change Failure Rate: <15%

Performance:
  - API Latency: <100ms p95
  - Page Load: <1s
  - Database Query: <50ms p95
  - Concurrent Users: Defined capacity tested
```

---

## Part 2: Security Requirements by Tier

### LITE Tier (1-2 people)

```yaml
Minimum Security:
  - Secrets: .env files (NOT committed to git)
  - Dependencies: Basic awareness of major vulnerabilities
  - Authentication: Standard framework auth (NextAuth, Auth.js)

CI/CD Security:
  - None required (manual review acceptable)

Audit:
  - None required
```

### STANDARD Tier (3-10 people)

```yaml
Secrets Management:
  - .env files with .env.example template
  - No secrets in code (pre-commit hook)
  - Basic secret rotation (manual, quarterly)

Dependencies:
  - npm audit / pip-audit on PRs
  - Renovate or Dependabot enabled
  - Critical CVEs addressed within 7 days

Authentication:
  - OAuth 2.0 or standard auth
  - Password policy enforced (12+ chars)
  - Session management (timeouts)

CI/CD Security:
  - Dependency scanning (npm audit, pip-audit)
  - Basic SAST (optional)
```

### PROFESSIONAL Tier (10-50 people)

```yaml
Secrets Management:
  - HashiCorp Vault or AWS Secrets Manager
  - Automatic rotation (90 days)
  - Audit logging for secret access

Software Bill of Materials (SBOM):
  Required: YES
  Tools: Syft, CycloneDX
  Format: SPDX or CycloneDX JSON
  Update: Every release

SAST (Static Application Security Testing):
  Required: YES
  Tools: {SAST_tool} (e.g., Semgrep, SonarQube, CodeQL)
  Rules: OWASP Top 10
  Enforcement: Block on Critical/High

Dependency Scanning:
  Required: YES
  Tools: Grype, Snyk, Dependabot
  Critical: Block PR
  High: Block PR
  Medium: Warning (fix within 14 days)
  Low: Informational

OWASP ASVS Level:
  Required: Level 1 (minimum)
  Categories Covered:
    - V1: Architecture, Design, Threat Modeling
    - V2: Authentication
    - V3: Session Management
    - V4: Access Control
    - V5: Validation, Sanitization, Encoding
    - V6: Stored Cryptography
    - V7: Error Handling, Logging
    - V8: Data Protection
    - V9: Communications
    - V10: Malicious Code
    - V11: Business Logic
    - V12: Files and Resources
    - V13: API and Web Service
    - V14: Configuration

Threat Modeling:
  Required: For new features with user data
  Method: STRIDE or PASTA
  Documentation: ADR format
```

### ENTERPRISE Tier (50+ people)

```yaml
All PROFESSIONAL requirements, PLUS:

OWASP ASVS Level:
  Required: Level 2 (recommended Level 3 for sensitive)

DAST (Dynamic Application Security Testing):
  Required: YES
  Tools: OWASP ZAP, Burp Suite
  Frequency: Weekly automated, monthly manual

Penetration Testing:
  Required: YES (annually minimum)
  Scope: Full application + infrastructure
  Provider: Third-party certified (CREST, OSCP)
  Remediation: Critical within 72h, High within 7 days

Security Champions:
  Required: 1 per team
  Training: Annual security training
  Responsibilities: Code review, threat modeling

Incident Response:
  Plan: Documented and tested
  Contacts: 24/7 security team
  SLA: P0 security <15 minutes response

Compliance:
  Audits: Quarterly internal, annual external
  Certifications: As required (SOC 2, ISO 27001, HIPAA)
  Evidence: Continuous compliance monitoring
```

---

## Part 3: Gate-Specific Requirements

### G0.1 (Problem Definition)

```yaml
Quality Checklist:
  □ Problem Statement documented
  □ User interviews completed (5+ users for PROFESSIONAL+)
  □ Business case validated
  □ Success metrics defined

Security Consideration:
  □ Data sensitivity classification identified
  □ Regulatory requirements noted (GDPR, HIPAA, etc.)
  □ Initial threat landscape assessed

Exit Criteria:
  - Problem validated with real users
  - ROI estimate documented
  - Stakeholder sign-off obtained
```

### G0.2 (Solution Diversity)

```yaml
Quality Checklist:
  □ 100+ ideas generated (PROFESSIONAL+)
  □ Top 3-5 concepts evaluated
  □ Technical feasibility assessed
  □ Risk assessment completed

Security Consideration:
  □ Security implications of each solution evaluated
  □ Third-party components security reviewed
  □ Attack surface compared between options

Exit Criteria:
  - Selected solution documented
  - Alternatives considered (ADR format)
  - Resource estimates provided
```

### G1 (Legal + Market Validation)

```yaml
Quality Checklist:
  □ Legal review completed
  □ License compliance verified
  □ Market research documented
  □ Competitive analysis done

Security Checklist:
  □ License compliance verified (AGPL contamination check)
  □ Data residency requirements identified
  □ Privacy requirements documented
  □ Security budget allocated

Exit Criteria:
  - No blocking legal issues
  - Market opportunity validated
  - Go/No-Go decision documented
```

### G2 (Design Ready)

```yaml
Quality Checklist:
  □ System architecture documented
  □ API contracts defined (OpenAPI)
  □ Database schema designed
  □ ADRs for key decisions

Security Checklist:
  □ Threat model completed (STRIDE/PASTA)
  □ Security architecture documented
  □ Authentication/Authorization design reviewed
  □ Data encryption strategy defined
  □ API security requirements specified
  □ OWASP ASVS checklist started

Exit Criteria:
  - Architecture approved (CTO)
  - API contracts validated
  - Security baseline defined
  - Security Lead sign-off on architecture
  - No unmitigated HIGH/CRITICAL threats
  - SBOM tooling configured
  - Estimated timeline accurate (±20%)
```

### G3 (Ship Ready)

```yaml
Quality Checklist:
  □ All features implemented
  □ Test coverage targets met
  □ Performance budget met
  □ Documentation complete
  □ Runbooks created
  □ Rollback tested

Security Checklist:
  □ SAST scan: PASS (zero Critical/High)
  □ Dependency scan: PASS (zero Critical/High)
  □ SBOM generated and stored
  □ Secrets rotation verified
  □ OWASP ASVS checklist completed (per tier level)
  □ Security documentation complete
  □ Incident response plan tested

Enterprise Additional:
  □ DAST scan completed
  □ Penetration test completed (if applicable)
  □ Compliance evidence collected
  □ Security training verified for all team members

Exit Criteria:
  - Zero P0 bugs
  - Zero critical security issues
  - Performance under load validated
  - UAT sign-off (PROFESSIONAL+)
  - CTO + CPO + Security Lead approval
  - High security issues have mitigation plan
```

---

## Part 4: SBOM (Software Bill of Materials)

### What is SBOM?

A complete inventory of all software components, dependencies, and their versions used in your application.

### SBOM Requirements

```yaml
Required for: PROFESSIONAL+ tiers
Format: SPDX or CycloneDX (JSON)
Generation: Automated in CI/CD
Storage: With each release artifact
Retention: Minimum 3 years

Content Must Include:
  - Package name and version
  - License information
  - Supplier/maintainer
  - Dependency relationships
  - Known vulnerabilities (linked)
```

### SBOM Generation Example

```yaml
# GitHub Actions
- name: Generate SBOM
  uses: anchore/sbom-action@v0
  with:
    format: spdx-json
    output-file: sbom.spdx.json

- name: Scan SBOM for vulnerabilities
  uses: anchore/scan-action@v3
  with:
    sbom: sbom.spdx.json
    fail-build: true
    severity-cutoff: high
```

---

## Part 5: SAST Rules & Configuration

### Semgrep Configuration

```yaml
# .semgrep.yml
rules:
  # OWASP Top 10
  - id: sql-injection
    patterns:
      - pattern: execute($QUERY)
      - pattern-not: execute($QUERY, $PARAMS)
    message: "Potential SQL injection"
    severity: ERROR

  - id: xss-vulnerability
    pattern: innerHTML = $USER_INPUT
    message: "Potential XSS vulnerability"
    severity: ERROR

  - id: hardcoded-secret
    patterns:
      - pattern: password = "..."
      - pattern: api_key = "..."
    message: "Hardcoded secret detected"
    severity: ERROR

  - id: insecure-crypto
    pattern: md5($DATA)
    message: "MD5 is cryptographically weak"
    severity: WARNING
```

### SAST Enforcement

```yaml
CI Pipeline:
  Critical: Block merge
  High: Block merge
  Medium: Warning (must fix before release)
  Low: Informational

Exceptions:
  - Documented false positives (suppression with comment)
  - Reviewed and approved by Security Lead
  - Expiration date for suppression (max 90 days)
```

---

## Part 6: OWASP ASVS Checklist Summary

### Level 1 (PROFESSIONAL tier minimum)

```yaml
V2 - Authentication:
  □ V2.1: Password requirements enforced (12+ chars)
  □ V2.2: Credential recovery secure
  □ V2.5: Account lockout after failures

V3 - Session Management:
  □ V3.2: Session tokens generated securely
  □ V3.3: Session timeout implemented
  □ V3.7: Session invalidation on logout

V4 - Access Control:
  □ V4.1: Access control enforced server-side
  □ V4.2: Principle of least privilege

V5 - Validation:
  □ V5.1: Input validation on all data
  □ V5.3: Output encoding for XSS prevention

V7 - Error Handling:
  □ V7.1: Errors don't leak sensitive info
  □ V7.2: Security events logged

V9 - Communications:
  □ V9.1: TLS for all connections
  □ V9.2: TLS 1.2+ only
```

### Level 2 (ENTERPRISE tier minimum)

```yaml
All Level 1 requirements, PLUS:

V1 - Architecture:
  □ V1.2: Threat model documented
  □ V1.5: Security controls defined

V2 - Authentication:
  □ V2.8: MFA for sensitive operations
  □ V2.9: Cryptographic authentication for APIs

V8 - Data Protection:
  □ V8.1: Sensitive data identified
  □ V8.2: Encryption at rest
  □ V8.3: Data minimization practiced

V13 - API Security:
  □ V13.1: Rate limiting implemented
  □ V13.2: Input validation on API
  □ V13.4: Anti-CSRF tokens
```

---

## Part 7: Threat Modeling

### When Required

```yaml
LITE: Not required
STANDARD: Recommended for user-facing features
PROFESSIONAL: Required for:
  - New features handling user data
  - Authentication/authorization changes
  - Third-party integrations
  - Infrastructure changes

ENTERPRISE: Required for all significant changes
```

### STRIDE Method

```yaml
Threat Categories:
  S - Spoofing: Can attacker pretend to be someone else?
  T - Tampering: Can data be modified maliciously?
  R - Repudiation: Can attacker deny actions?
  I - Information Disclosure: Can data be exposed?
  D - Denial of Service: Can service be disrupted?
  E - Elevation of Privilege: Can attacker gain higher access?

Template:
  | Threat | Category | Asset | Mitigation | Risk Level |
  |--------|----------|-------|------------|------------|
  | [Description] | S/T/R/I/D/E | [What's at risk] | [Control] | H/M/L |
```

---

## Part 8: DORA Metrics Tracking

### Metric Definitions

```yaml
Deployment Frequency (DF):
  Definition: How often code is deployed to production
  Measurement: Count of production deployments per time period
  Target by Tier:
    LITE: Any (tracking optional)
    STANDARD: Weekly to monthly
    PROFESSIONAL: Daily to weekly
    ENTERPRISE: Multiple per day

Lead Time for Changes (LT):
  Definition: Time from code commit to production
  Measurement: Median time (commit timestamp → production deploy)
  Target by Tier:
    LITE: Any
    STANDARD: 1 week to 1 month
    PROFESSIONAL: 1 day to 1 week
    ENTERPRISE: <1 hour to <1 day

Mean Time to Recovery (MTTR):
  Definition: Time to restore service after failure
  Measurement: Median time (incident start → service restored)
  Target by Tier:
    LITE: Any
    STANDARD: <1 week
    PROFESSIONAL: <1 day
    ENTERPRISE: <1 hour

Change Failure Rate (CFR):
  Definition: Percentage of deployments causing failure
  Measurement: (Failed deployments / Total deployments) × 100
  Target by Tier:
    LITE: Any
    STANDARD: <30%
    PROFESSIONAL: <20%
    ENTERPRISE: <15%
```

### Dashboard Template

```yaml
Weekly DORA Dashboard:
  Deployment Frequency: [N] deploys this week (target: [X])
  Lead Time: [N] hours median (target: <[X] hours)
  MTTR: [N] minutes (target: <[X] minutes)
  Change Failure Rate: [N]% (target: <[X]%)

  Trend: [↑/↓/→] vs last week
  Action Items: [If below target, list improvements]
```

---

## Part 9: Incident Response

### Security Incident Classification

```yaml
P0 - Critical:
  - Data breach confirmed
  - System compromise
  - Active exploitation
  Response: <15 minutes
  Escalation: CTO + Security Lead + Legal

P1 - High:
  - Vulnerability actively exploited
  - Significant security gap discovered
  Response: <1 hour
  Escalation: Security Lead + Tech Lead

P2 - Medium:
  - Vulnerability discovered (not exploited)
  - Security misconfiguration
  Response: <4 hours
  Escalation: Security Champion + Team Lead

P3 - Low:
  - Security improvement opportunity
  - Minor policy violation
  Response: Next business day
  Escalation: Team Lead
```

---

## Part 10: Quality Gate Automation

### Pre-commit Hook Example

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: lint
        name: Lint code
        entry: ruff check .
        language: system

      - id: format
        name: Check formatting
        entry: ruff format --check .
        language: system

      - id: typecheck
        name: Type check
        entry: mypy .
        language: system

      - id: test
        name: Run fast tests
        entry: pytest -x --timeout=30
        language: system
```

### CI Pipeline Quality Gates

```yaml
# GitHub Actions example
quality-gates:
  runs-on: ubuntu-latest
  steps:
    - name: Lint
      run: ruff check . --output-format=github

    - name: Format
      run: ruff format --check .

    - name: Type Check
      run: mypy . --strict

    - name: Unit Tests
      run: pytest --cov=src --cov-fail-under=80

    - name: Security Scan
      run: semgrep --config=auto .

    - name: Check Coverage
      run: |
        coverage report --fail-under=80
```

---

## Part 11: Enforcement & Escalation

### Blocking vs Non-Blocking

```yaml
BLOCKING (Fail CI):
  - Lint errors
  - Type errors
  - Test failures
  - Coverage below threshold
  - Security critical/high

NON-BLOCKING (Warning only):
  - Coverage warning (within 5% of threshold)
  - Security medium/low
  - Performance warning (within 10% of target)
```

### Escalation for Quality/Security Failures

```yaml
Quality Issue Escalation:
  Level 1 (Team): Coverage dropped 5%, lint warnings
  Level 2 (Lead): Coverage below threshold, test failures
  Level 3 (CTO): Build broken >24h, P0 bug in production

Security Issue Escalation:
  Level 1 (Team): Security medium findings
  Level 2 (Lead): Security high findings
  Level 3 (CTO): Security critical, active exploitation
```

---

## Part 12: Code Quality Thresholds

### Linting Rules

```yaml
Python (Ruff):
  - All default rules enabled
  - Line length: 120 chars
  - Import sorting: isort compatible
  - Docstrings: Google style

TypeScript (ESLint):
  - @typescript-eslint/recommended
  - No 'any' type (strict mode)
  - Consistent return types

React:
  - react-hooks/rules-of-hooks
  - react-hooks/exhaustive-deps
  - jsx-a11y for accessibility
```

### Test Quality

```yaml
Unit Tests:
  - Arrange-Act-Assert pattern
  - One assertion per test (preferred)
  - No test interdependencies
  - Deterministic (no flaky tests)

Integration Tests:
  - Real services (no mocks for external APIs)
  - Database transactions (rollback after test)
  - Contract validation (OpenAPI)

E2E Tests:
  - User journey focused
  - Stable selectors (data-testid)
  - Retry logic for flakiness
  - Screenshot on failure
```

---


---

## Part 13: Three-Tier Testing Methodology (NEW in 6.3.0)

> **Source**: gstack three-tier testing system (2026-03-29). Addresses AI-specific testing costs (LLM eval runs cost money) and diff-based test selection.

### The Three Tiers

| Tier | What | Cost | When to Run | Gate Requirement |
|------|------|------|-------------|-----------------|
| **Tier 1 — Static** | Lint, type check, format check, schema validation, Zero Mock scan | Free | Every commit, every PR | G-Sprint (mandatory) |
| **Tier 2 — Integration** | Unit tests, integration tests, E2E tests, API contract validation | CI minutes (moderate) | Pre-merge, gated on diff | G3 (mandatory) |
| **Tier 3 — AI Evaluation** | LLM-as-Judge quality eval, security scan (SAST/DAST), performance benchmark | $$$ (LLM API calls) | Pre-release, weekly scheduled | G4 (mandatory for PROFESSIONAL+) |

### Diff-Based Test Selection

Not all tests run on every commit. Each test declares its file dependencies:

```yaml
# Test dependency declaration (conceptual)
test_suites:
  auth_tests:
    triggers: ["backend/app/services/auth*", "backend/app/routes/auth*"]
  gate_tests:
    triggers: ["backend/app/services/gate*", "backend/app/models/gate*"]
  global_tests:
    triggers: ["*"]  # Always run (migrations, config, middleware)
```

**Rule**: Changes to global infrastructure (migrations, config, middleware, CI) trigger ALL tests. Feature-scoped changes trigger only affected suites.

### Cost Management

| Tier | Cost Control | Budget |
|------|-------------|--------|
| Tier 1 | Free — no cost control needed | Unlimited |
| Tier 2 | Diff-based selection reduces CI minutes | Per-project CI budget |
| Tier 3 | Gated by `EVALS=1` flag — never runs accidentally | Max $5/run (LLM eval), monthly cap per project |

### Tier-Specific Gate Requirements

| Gate | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|------|------|----------|--------------|------------|
| **G-Sprint** | Tier 1 | Tier 1 | Tier 1 | Tier 1 |
| **G3** | Tier 1 + basic Tier 2 | Tier 1 + Tier 2 | Tier 1 + Tier 2 | Tier 1 + Tier 2 |
| **G4** | Tier 1 + Tier 2 | Tier 1 + Tier 2 | Tier 1 + Tier 2 + Tier 3 | All three tiers |

### Connection to Existing Standards

- **Zero Skip Policy**: Applies to all tiers — no `skip` or `xfail` markers allowed
- **Coverage targets**: Tier 2 enforces critical-path 95% (PROFESSIONAL+) / overall 80-85%
- **Fix-First Protocol (Section 6.3)**: Tier 1/2 failures → Fix-First classification before merge

---

## Part 14: Documentation Staleness Detection (NEW in 6.3.0)

> **Source**: gstack documentation staleness check (2026-03-29). Enforcement mechanism for Pillar 6 (Documentation Permanence).

### The Problem

Code changes but docs don't. Documentation drift is invisible until someone reads a stale doc and makes a wrong decision. The Framework emphasizes Documentation Permanence (Pillar 6) but lacked a detection mechanism.

### The Protocol

After every code change that passes G-Sprint or G3, cross-reference the diff against `.md` files:

```
For each .md file in /docs:
  1. Does the code diff affect features/components described in this doc?
  2. Was this doc updated in the same branch?
  3. If code changed but doc wasn't → flag as STALE (informational)
```

### Classification

| Result | Meaning | Action |
|--------|---------|--------|
| **FRESH** | Doc was updated alongside code | No action |
| **STALE** | Code changed, related doc not updated | Informational flag — fix before G4 |
| **UNRELATED** | Doc doesn't describe changed code | No action |

### Gate Integration

| Gate | Staleness Check |
|------|----------------|
| G-Sprint | Informational only (non-blocking) |
| G3 | Warning — flag stale docs in review |
| G4 | **BLOCKING for PROFESSIONAL+** — no stale docs in release |

### Tier Rules

| Tier | Enforcement |
|------|-------------|
| LITE | Not required |
| STANDARD | Informational at G3 |
| PROFESSIONAL | Warning at G3, blocking at G4 |
| ENTERPRISE | Warning at G-Sprint, blocking at G3 and G4 |

---

## Further Reading

> The framework above is self-contained. References below are for deeper study.

**External Standards**:
- OWASP Application Security Verification Standard (ASVS) v4.0
- Singapore Model AI Governance Framework — Dimension 3: Technical Controls
- NIST Risk Management Framework (RMF)

**Industry**:
- DORA State of DevOps Report — deployment frequency, lead time, MTTR metrics
- Anthropic: "2026 Agentic Coding Trends Report" — Trend 4: Human oversight scales

**Internal References**:
- [SDLC-Sprint-Governance.md](./SDLC-Sprint-Governance.md) — G-Sprint/G-Sprint-Close gates
- [anti-vibecoding.yaml](./anti-vibecoding.yaml) — Machine-readable scoring rules
- [gates.yaml](./gates.yaml) — Machine-readable gate definitions

---

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-01-28 | Original 2 documents (QA System, Quality-Security-Gates) | CTO (Tai) |
| 2.0 | 2026-03-18 | Consolidated into Quality Gates & Assurance Framework (Framework 6.3.0) | CTO (Tai) |
| 2.1 | 2026-03-29 | Added Fix-First Review Protocol (Section 6.3) — Framework 6.3.0 | PM + CTO |
| 2.2 | 2026-03-29 | Added Three-Tier Testing (Part 13) + Doc Staleness Detection (Part 14) — Framework 6.3.0 | PM + CTO |

