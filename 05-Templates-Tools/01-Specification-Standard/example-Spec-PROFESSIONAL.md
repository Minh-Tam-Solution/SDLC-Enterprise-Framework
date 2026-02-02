# Example Specification: PROFESSIONAL Tier

This example demonstrates the comprehensive specification format for regulated industries and mission-critical systems.

---

```markdown
---
# Core Metadata
spec_id: SPEC-0201
spec_name: "Anti-Vibecoding Governance Engine"
spec_version: "2.0.0"
status: implemented
tier: PROFESSIONAL
stage: "03"
category: technical

# Ownership
owner: "governance-team"
reviewers: ["backend-lead", "security-lead", "cto"]
approver: "CEO"

# Timestamps
created: 2025-11-01
last_updated: 2026-01-28
approved_date: 2026-01-20

# Relationships
related_adrs: ["ADR-007", "ADR-011", "ADR-022", "ADR-035"]
related_specs: ["SPEC-0042", "SPEC-0108", "SPEC-0155", "SPEC-0178"]
parent_spec: "SPEC-0150"
supersedes: "SPEC-0098"

# Tags
tags: ["governance", "anti-vibecoding", "quality-gates", "ai-governance"]
priority: P0
effort: XL
---

## 1. Overview

Anti-Vibecoding Governance Engine provides automated quality assessment for AI-generated code through Vibecoding Index calculation, progressive PR routing, and enforcement modes (WARNING → SOFT → FULL).

**Key Objectives**:
- Calculate Vibecoding Index (0-100) for all PRs
- Route PRs to appropriate reviewers based on index
- Enforce quality gates with configurable modes
- Reduce CEO review time by 75% (40h → 10h/week)

**Scope**:
- **In Scope**: Index calculation, routing logic, enforcement modes, auto-generation, kill switch
- **Out of Scope**: Code generation, test execution, deployment automation

## 2. Context

### 2.1 Problem Statement

Without governance, AI-generated code ("vibecoding") leads to:
- 40+ hours/week CEO time on PR reviews
- Inconsistent code quality
- Missing documentation and tests
- Technical debt accumulation

The governance engine automates quality assessment to reduce human bottlenecks while maintaining quality standards.

### 2.2 Background

This specification builds on:
- Sprint 111-113: Governance UI implementation (7,884 LOC)
- ADR-035: Progressive Routing System
- SDLC 6.0.2 Section 7: Quality Assurance System

### 2.3 Stakeholders

| Stakeholder | Role | Interest |
|-------------|------|----------|
| CEO | Decision Maker | Reduce review time |
| CTO | Approver | Technical quality |
| Developers | Users | Minimal friction |
| QA Team | Validators | Test coverage |
| Compliance | Auditors | Audit trail |

### 2.4 Assumptions

- GitHub integration configured
- OPA policy engine available
- AI providers accessible (Ollama/Claude)
- Developers have IDE extensions installed

### 2.5 Constraints

- Latency: <100ms for index calculation
- False positive rate: <5%
- Kill switch must activate within 60 seconds
- AGPL containment for MinIO/Grafana

## 3. Requirements

### 3.1 Functional Requirements

#### FR-001: Vibecoding Index Calculation
**Priority**: P0
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN a PR submitted to the repository
  AND the PR contains code changes
WHEN the governance engine evaluates the PR
THEN a Vibecoding Index (0-100) is calculated
  AND the index is based on 5 weighted signals:
    | Signal | Weight |
    | Intent clarity | 25% |
    | Spec linkage | 20% |
    | Test coverage | 20% |
    | ADR reference | 15% |
    | Context freshness | 20% |
  AND the index is stored in Evidence Vault
```

#### FR-002: Progressive Routing
**Priority**: P0
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN a calculated Vibecoding Index
WHEN the system determines the routing
THEN the PR is routed based on index range:
  | Index Range | Color | Action |
  | 0-30 | Green | Auto-approve (Tech Lead optional) |
  | 31-60 | Yellow | Tech Lead required |
  | 61-80 | Orange | Senior Dev + Tech Lead required |
  | 81-100 | Red | CEO review required |
  AND the routing decision is logged
```

#### FR-003: Enforcement Modes
**Priority**: P0
**Tier**: PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN the governance mode is configured
WHEN evaluating PR merge eligibility
THEN the system enforces based on mode:
  | Mode | Green | Yellow | Orange | Red |
  | WARNING | Pass | Warn | Warn | Warn |
  | SOFT | Pass | Pass+Log | Pass+Log | Block |
  | FULL | Auto | Approve | Block | Block |
  AND mode changes are logged in audit trail
```

#### FR-004: Auto-Generation Layer
**Priority**: P1
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN a PR with missing governance metadata
WHEN the developer requests auto-generation
THEN the system generates:
  - Intent document (from PR title/description)
  - Ownership header (from git blame)
  - Context summary (from AGENTS.md)
  - Attestation template (compliance checkboxes)
  AND generation uses multi-provider fallback (Ollama → Claude)
  AND generation completes within 30 seconds
```

#### FR-005: Kill Switch Mechanism
**Priority**: P0
**Tier**: PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN the governance system is in SOFT or FULL mode
WHEN any kill switch criteria is met:
  | Criteria | Threshold |
  | Rejection rate | >80% in 1 hour |
  | False positives | >10% reported |
  | API latency | >500ms p95 |
  | System errors | >5% error rate |
THEN the system automatically rolls back to WARNING mode
  AND notifications are sent to CTO and CEO
  AND incident is logged for review
```

#### FR-006: Override Workflow
**Priority**: P1
**Tier**: PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN a blocked PR with valid business justification
WHEN a CTO-level user requests override
THEN the override request is logged
  AND the PR is allowed to merge
  AND the override is tracked for audit
  AND override quota is checked (max 5 per week)
```

### 3.2 Non-Functional Requirements

#### NFR-001: Performance
| Metric | Target | Measurement |
|--------|--------|-------------|
| Index calculation | <100ms p95 | Prometheus |
| Auto-generation | <30s p95 | Prometheus |
| Dashboard load | <1s | Lighthouse |
| Concurrent PRs | 100 | Load test |

#### NFR-002: Security
| Requirement | Standard | Verification |
|-------------|----------|--------------|
| Authentication | OAuth 2.0 + JWT | Integration test |
| Authorization | RBAC (13 roles) | Unit test |
| Audit logging | Immutable | DB constraint |
| Data encryption | TLS 1.3 + AES-256 | Config audit |

#### NFR-003: Reliability
| Metric | Target | Measurement |
|--------|--------|-------------|
| Uptime | 99.9% | Prometheus |
| Data durability | 99.99% | MinIO config |
| Recovery time | <15 minutes | DR drill |

#### NFR-004: Compliance
| Requirement | Standard | Verification |
|-------------|----------|--------------|
| Audit trail | SOC 2 Type II | External audit |
| Data retention | 7 years (ENTERPRISE) | Policy check |
| Access logs | GDPR compliant | DPO review |

### 3.3 Tier-Specific Requirements

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| Vibecoding Index | Basic (3 signals) | Standard (5 signals) | Full (5 signals) | Custom weights |
| Enforcement modes | WARNING only | WARNING, SOFT | All modes | All + custom |
| Kill switch | Manual | Automatic | Auto + custom | Custom criteria |
| Override workflow | N/A | Tech Lead | CTO | Custom hierarchy |
| Audit retention | 30 days | 1 year | 3 years | 7+ years |
| SLA | None | 99% | 99.9% | 99.99% |

## 4. Design Decisions

### 4.1 Related ADRs

| ADR | Title | Status | Impact on This Spec |
|-----|-------|--------|---------------------|
| ADR-007 | Ollama AI Integration | Accepted | Primary AI provider |
| ADR-011 | AI Governance Layer | Accepted | Architecture foundation |
| ADR-022 | IR-Based Codegen | Accepted | Code generation flow |
| ADR-035 | Progressive Routing | Accepted | Routing logic |

### 4.2 Key Decisions

#### Decision 1: 5 Weighted Signals for Index
- **Status**: Decided
- **ADR Reference**: ADR-035
- **Summary**: 5 signals with configurable weights provide balanced assessment
- **Impact**: Tunable quality gates, transparent scoring

#### Decision 2: Kill Switch Automatic Rollback
- **Status**: Decided
- **Summary**: Automatic rollback prevents extended disruption
- **Impact**: Safety net for aggressive enforcement

#### Decision 3: Multi-Provider AI Fallback
- **Status**: Decided
- **ADR Reference**: ADR-007
- **Summary**: Ollama → Claude → Rule-based fallback ensures availability
- **Impact**: 95% cost savings, graceful degradation

### 4.3 Open Questions

- [x] ~~Signal weights finalized~~ (Decided: 25/20/20/15/20)
- [x] ~~Kill switch thresholds~~ (Decided: 80%/10%/500ms/5%)
- [ ] Custom signal support for ENTERPRISE tier

## 5. Technical Specification

### 5.1 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Anti-Vibecoding Governance Engine                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│  │   GitHub    │───▶│   Webhook   │───▶│   Index     │───▶│   Router    │ │
│  │   Events    │    │   Handler   │    │   Calculator│    │   Service   │ │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘ │
│                           │                  │                  │          │
│                           ▼                  ▼                  ▼          │
│                     ┌─────────────┐    ┌─────────────┐    ┌─────────────┐ │
│                     │   Signal    │    │   Evidence  │    │   Override  │ │
│                     │   Engine    │    │   Vault     │    │   Queue     │ │
│                     └─────────────┘    └─────────────┘    └─────────────┘ │
│                           │                                     │          │
│                           ▼                                     ▼          │
│                     ┌─────────────┐                       ┌─────────────┐ │
│                     │   AI        │                       │   Audit     │ │
│                     │   Providers │                       │   Log       │ │
│                     │ (Ollama/    │                       │   (Append-  │ │
│                     │  Claude)    │                       │    only)    │ │
│                     └─────────────┘                       └─────────────┘ │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                         Kill Switch Monitor                         │  │
│  │  [Rejection Rate] [False Positives] [Latency] [Errors] → Auto-OFF   │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Data Model

```yaml
Entity: VibecondingIndex
  Fields:
    - id: UUID (PK)
    - pr_id: VARCHAR(100) NOT NULL
    - project_id: UUID (FK) NOT NULL
    - index_value: INTEGER (0-100) NOT NULL
    - signal_intent: INTEGER (0-100)
    - signal_spec_linkage: INTEGER (0-100)
    - signal_test_coverage: INTEGER (0-100)
    - signal_adr_reference: INTEGER (0-100)
    - signal_context_freshness: INTEGER (0-100)
    - routing_color: ENUM('green', 'yellow', 'orange', 'red')
    - calculated_at: TIMESTAMP DEFAULT NOW()
    - calculated_by: VARCHAR(50) # provider used
  Indexes:
    - pr_id (UNIQUE)
    - project_id, calculated_at
    - routing_color

Entity: GovernanceDecision
  Fields:
    - id: UUID (PK)
    - index_id: UUID (FK) NOT NULL
    - mode: ENUM('WARNING', 'SOFT', 'FULL')
    - action: ENUM('AUTO_APPROVE', 'REQUIRE_REVIEW', 'BLOCK')
    - override_by: UUID (FK) NULL
    - override_reason: TEXT NULL
    - decided_at: TIMESTAMP DEFAULT NOW()
  Indexes:
    - index_id
    - decided_at

Entity: KillSwitchEvent
  Fields:
    - id: UUID (PK)
    - trigger_reason: VARCHAR(100) NOT NULL
    - trigger_value: DECIMAL NOT NULL
    - threshold: DECIMAL NOT NULL
    - previous_mode: ENUM('SOFT', 'FULL')
    - triggered_at: TIMESTAMP DEFAULT NOW()
    - acknowledged_by: UUID (FK) NULL
    - acknowledged_at: TIMESTAMP NULL
  Indexes:
    - triggered_at
```

### 5.3 API Contracts

```yaml
Endpoint: POST /api/v1/governance/evaluate
  Description: Evaluate PR and calculate Vibecoding Index
  Authentication: Service token (internal) or Bearer token (webhook)
  Request:
    Content-Type: application/json
    Body:
      pr_number: integer (required)
      repository: string (required)
      commit_sha: string (required)
  Response:
    200:
      index:
        value: integer
        color: string
        signals:
          intent: integer
          spec_linkage: integer
          test_coverage: integer
          adr_reference: integer
          context_freshness: integer
      decision:
        action: string
        mode: string
        requires_review: boolean
        reviewers: array
    400:
      error: "Invalid PR data"
    503:
      error: "Governance temporarily disabled (kill switch)"

Endpoint: POST /api/v1/governance/override
  Description: Request override for blocked PR
  Authentication: Bearer token (CTO role required)
  Request:
    Content-Type: application/json
    Body:
      pr_number: integer (required)
      reason: string (required, min 50 chars)
  Response:
    200:
      override_id: UUID
      approved: boolean
      quota_remaining: integer
    400:
      error: "Reason too short"
    403:
      error: "Override quota exceeded"
    404:
      error: "PR not found or not blocked"
```

### 5.4 Integration Points

| System | Protocol | Direction | Data Format |
|--------|----------|-----------|-------------|
| GitHub | Webhook + REST | Bidirectional | JSON |
| OPA | REST | Outbound | JSON |
| MinIO | S3 API | Outbound | Binary + JSON |
| Ollama | REST | Outbound | JSON |
| Claude | REST | Outbound | JSON |
| PostgreSQL | SQL | Bidirectional | SQL |
| Redis | Protocol | Bidirectional | Binary |

### 5.5 Security Considerations

- **Authentication**: Service tokens for internal, OAuth for webhooks
- **Authorization**: RBAC with role-based override permissions
- **Data Protection**: Index data encrypted at-rest
- **Audit**: All decisions and overrides logged immutably
- **Kill Switch**: Automatic rollback prevents abuse

## 6. Acceptance Criteria

### 6.1 Functional Acceptance

| ID | Criterion | Test Type | Priority |
|----|-----------|-----------|----------|
| AC-001 | Index calculated for PR within 100ms | Performance | P0 |
| AC-002 | Green PRs auto-approved in FULL mode | Integration | P0 |
| AC-003 | Red PRs blocked in SOFT/FULL mode | Integration | P0 |
| AC-004 | Kill switch triggers at 80% rejection | Integration | P0 |
| AC-005 | Override workflow completes successfully | E2E | P1 |
| AC-006 | Auto-generation produces valid documents | Integration | P1 |
| AC-007 | Dashboard shows real-time index data | E2E | P1 |

### 6.2 Performance Acceptance

| Metric | Threshold | Test Method | Blocker |
|--------|-----------|-------------|---------|
| Index calculation | <100ms p95 | pytest-benchmark | Yes |
| Auto-generation | <30s p95 | Integration test | Yes |
| Concurrent PRs | 100 simultaneous | Locust | No |
| Dashboard load | <1s | Lighthouse | Yes |

### 6.3 Security Acceptance

| Criterion | Standard | Verification | Blocker |
|-----------|----------|--------------|---------|
| Audit trail immutable | Append-only DB | Schema review | Yes |
| Override requires CTO | RBAC test | Integration | Yes |
| Tokens rotated | 90-day policy | Config audit | No |

### 6.4 Definition of Done

- [ ] All P0 acceptance criteria pass
- [ ] Code review approved (CTO + 2 reviewers)
- [ ] Security review passed (Security Lead)
- [ ] Performance benchmarks met
- [ ] Documentation updated (API, runbook)
- [ ] Kill switch tested in staging
- [ ] CEO sign-off on enforcement mode

## 7. Spec Delta

### 7.1 Current Version Changes (v1.5.0 → v2.0.0)

**Summary**: Major upgrade with FULL enforcement mode and kill switch

**Impact**: breaking (new enforcement mode affects all PRs)

#### Added
- FR-003: FULL enforcement mode
- FR-005: Kill Switch Mechanism (automatic rollback)
- FR-006: Override Workflow (CTO approval)
- NFR-004: Compliance requirements

#### Modified

| Original | New | Rationale |
|----------|-----|-----------|
| 3 signals | 5 signals | Better accuracy |
| Manual kill switch | Automatic | Faster response |
| 30-day audit | 7-year (ENTERPRISE) | Compliance |

#### Breaking Changes

⚠️ **Warning**: The following changes require updates:

1. **API Response Format**: Index response includes new `signals` object
   - Fix: Update clients to handle new response structure

2. **Enforcement Mode**: FULL mode now blocks Orange/Red PRs
   - Fix: Ensure teams understand new workflow

### 7.2 Migration Guide

1. Update API clients to handle new response format
2. Configure enforcement mode (start with WARNING)
3. Set up kill switch monitoring alerts
4. Train team on override workflow
5. Test in staging before production

## 8. Dependencies

### 8.1 Upstream Dependencies

| Dependency | Type | Version | Status | Risk |
|------------|------|---------|--------|------|
| SPEC-0042 | Auth | 1.0.0 | Stable | Low |
| SPEC-0108 | Evidence | 1.2.0 | Stable | Low |
| SPEC-0155 | GitHub | 1.0.0 | Stable | Low |
| OPA | Engine | 0.58.0 | Stable | Low |
| Ollama | AI | qwen3:32b | Stable | Medium |

### 8.2 Downstream Dependencies

| Dependent | Type | Impact if Changed |
|-----------|------|-------------------|
| CEO Dashboard | UI | Requires update |
| Developer Extension | IDE | Requires update |
| Audit Reports | Feature | Schema change |

## 9. Appendix

### 9.1 Glossary

| Term | Definition |
|------|------------|
| Vibecoding | AI-generated code without proper specification |
| Vibecoding Index | Quality score (0-100) for AI-generated PRs |
| Kill Switch | Emergency mechanism to disable enforcement |
| Override | Manual approval for blocked PRs |

### 9.2 Signal Calculation Details

```python
def calculate_vibecoding_index(pr_data: dict) -> int:
    """Calculate Vibecoding Index from 5 signals."""
    weights = {
        "intent_clarity": 0.25,
        "spec_linkage": 0.20,
        "test_coverage": 0.20,
        "adr_reference": 0.15,
        "context_freshness": 0.20,
    }

    signals = {
        "intent_clarity": analyze_intent(pr_data),
        "spec_linkage": check_spec_links(pr_data),
        "test_coverage": get_test_coverage(pr_data),
        "adr_reference": check_adr_links(pr_data),
        "context_freshness": check_agents_md(pr_data),
    }

    index = sum(
        signal_value * weights[signal_name]
        for signal_name, signal_value in signals.items()
    )

    return int(100 - index)  # Lower is better
```

### 9.3 Kill Switch Threshold Configuration

```yaml
kill_switch:
  enabled: true
  check_interval_seconds: 60
  thresholds:
    rejection_rate:
      value: 0.80
      window_minutes: 60
    false_positive_rate:
      value: 0.10
      window_minutes: 60
    api_latency_p95_ms:
      value: 500
    error_rate:
      value: 0.05
      window_minutes: 15
  rollback_to: WARNING
  notification:
    channels: ["slack", "email"]
    recipients: ["cto", "ceo", "oncall"]
```

### 9.4 Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-11-01 | Backend Team | Initial spec |
| 1.5.0 | 2025-12-15 | Backend Team | Added SOFT mode |
| 2.0.0 | 2026-01-28 | Governance Team | FULL mode, kill switch |
```

---

## Notes

This PROFESSIONAL tier example demonstrates:

1. **Complete specification** - All sections filled
2. **Complex requirements** - Multiple scenarios, edge cases
3. **Tier differentiation** - Clear requirements per tier
4. **Detailed technical spec** - Architecture, data model, API
5. **Comprehensive audit** - Change tracking, compliance
6. **Production-ready** - Kill switch, override workflow

PROFESSIONAL tier specifications are appropriate for:
- Regulated industries (finance, healthcare)
- Mission-critical systems
- Multi-team enterprise projects
- High compliance requirements
