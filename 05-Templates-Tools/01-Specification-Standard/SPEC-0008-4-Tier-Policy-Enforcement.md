# SPEC-0008: 4-Tier Policy Enforcement

## Frontmatter

```yaml
spec_id: SPEC-0008
title: 4-Tier Policy Enforcement (ADR-036)
version: 1.0.0
status: approved
tier: ALL
pillar: Section 7 - Quality Assurance System
owner: CTO + Backend Lead
last_updated: 2026-01-30
tags:
  - 4-tier
  - policy-enforcement
  - graduated-governance
  - tier-classification
  - mrp
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
  - SPEC-0004  # Policy Guards
epic: Foundation - 4-Tier Classification
sprint: Sprint 102-104
```

---

## Executive Summary

**Problem**: SDLC Framework 5.2.0+ introduces 4-Tier Classification (LITE/STANDARD/PROFESSIONAL/ENTERPRISE) for graduated governance. Different project sizes need different enforcement levels - startups need advisory guidance while enterprises require zero-tolerance enforcement. A one-size-fits-all policy system would either over-burden small teams or under-protect large teams.

**Solution**: Implement **4-Tier Policy Enforcement** with graduated enforcement modes:
- **LITE** (1-2 people): Advisory only, no blocking
- **STANDARD** (3-10 people): Soft enforcement with warnings
- **PROFESSIONAL** (10-50 people): Hard enforcement with gate blocking
- **ENTERPRISE** (50+ people): Strict zero-tolerance enforcement

**Key Components**:
- **Tier-Based Policy Packs**: Pre-configured policy sets per tier with different enforcement modes
- **MRP 5-Point Validation**: Merge Readiness Protocol checks adapted to tier requirements
- **Dynamic Tier Adjustment**: Projects can upgrade tier as team grows (LITE → STANDARD → PRO → ENT)

**Business Value**:
- **Graduated Onboarding**: Small teams start with LITE tier (no overwhelming governance)
- **Clear Upgrade Path**: Natural progression as team scales (3 people → STANDARD, 10 → PRO, 50 → ENT)
- **Flexible Enforcement**: Same platform serves startups and enterprises with appropriate rigor
- **Compliance Ready**: ENTERPRISE tier meets audit/SOC 2/HIPAA requirements

**Success Criteria**:
- ✅ 4 distinct tier configurations with different enforcement modes
- ✅ MRP validation varies by tier (LITE: basic, ENTERPRISE: comprehensive)
- ✅ Projects can upgrade tier without data migration
- ✅ Policy evaluation <200ms regardless of tier
- ✅ 100% backward compatible with existing projects

---

## 1. Functional Requirements

### FR-001: Tier-Based Policy Pack Configuration

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN a project with assigned tier classification (LITE/STANDARD/PROFESSIONAL/ENTERPRISE)
WHEN the system evaluates policies for that project
THEN the system MUST apply the tier-specific policy pack with:
- Enforcement mode (advisory/soft/hard/strict)
- Required checks list (syntax, security, context, tests, all)
- Block-on-failure behavior (true/false)
- Notification channels (email, Slack, dashboard)
```

**Implementation Details**:
```python
TIER_POLICIES = {
    PolicyTier.LITE: {
        "enforcement_mode": "advisory",
        "block_on_failure": False,
        "required_checks": ["syntax_validation"],
        "notifications": ["dashboard"],
        "max_warnings": None,  # unlimited
    },
    PolicyTier.STANDARD: {
        "enforcement_mode": "soft",
        "block_on_failure": False,
        "required_checks": ["syntax_validation", "basic_security"],
        "notifications": ["dashboard", "email"],
        "max_warnings": 10,
    },
    PolicyTier.PROFESSIONAL: {
        "enforcement_mode": "hard",
        "block_on_failure": True,
        "required_checks": ["syntax_validation", "security_scan", "context_validation", "test_coverage"],
        "notifications": ["dashboard", "email", "slack"],
        "max_warnings": 3,
    },
    PolicyTier.ENTERPRISE: {
        "enforcement_mode": "strict",
        "block_on_failure": True,
        "required_checks": ["all"],  # includes: syntax, security, context, tests, compliance, audit
        "notifications": ["dashboard", "email", "slack", "pagerduty"],
        "max_warnings": 0,  # zero tolerance
        "require_approvals": 2,  # 2-person rule
    },
}
```

**Rationale**: Graduated enforcement ensures small teams aren't overwhelmed while enterprises get required rigor.

---

### FR-002: MRP (Merge Readiness Protocol) 5-Point Validation

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN a merge request awaiting approval
WHEN the system executes MRP validation
THEN the system MUST check 5 readiness points with tier-specific requirements:
1. Evidence Complete: All required evidence artifacts exist
2. Tests Passing: CI/CD tests pass with tier-specific coverage threshold
3. SAST Clean: Security scan passes with tier-specific severity tolerance
4. Context Valid: AGENTS.md context <60 lines and up-to-date
5. VCR Approved: Validated Code Review approval from qualified reviewers
```

**Tier-Specific MRP Matrix**:

| Check | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------|------|----------|--------------|------------|
| **Evidence Complete** | ❌ Optional | ⚠️ Warning if missing | ✅ Required, blocks merge | ✅ Required, blocks merge |
| **Tests Passing** | ❌ Optional | ⚠️ Warning if <60% | ✅ Required, >=80% coverage | ✅ Required, >=90% coverage |
| **SAST Clean** | ❌ Optional | ❌ Optional | ✅ No critical/high CVEs | ✅ No critical/high/medium CVEs |
| **Context <60 lines** | ❌ Optional | ❌ Optional | ⚠️ Warning if >60 lines | ✅ Required, blocks if >60 lines |
| **VCR Approved** | ❌ Optional | ❌ Optional | ⚠️ 1 reviewer required | ✅ 2 reviewers required (2-person rule) |

**Implementation**:
- Service: `MRPValidationService`
- Method: `validate_merge_readiness(merge_request, project_tier)`
- Output: `MRPResult` with 5-point status + tier-specific pass/fail

**Rationale**: MRP adapts to team size - LITE allows fast iteration, ENTERPRISE ensures compliance.

---

### FR-003: Dynamic Tier Upgrade Workflow

**Priority**: P1 (HIGH)

**Requirement**:
```gherkin
GIVEN a project currently on tier T (e.g., LITE)
WHEN the team size or compliance requirements increase
THEN the project owner MUST be able to upgrade to tier T+1 with:
- Pre-upgrade assessment (readiness check against new tier requirements)
- Grace period (30 days to comply with new tier policies)
- Rollback option (revert to previous tier if issues arise)
- Audit trail (document tier change reason + timestamp)
```

**Upgrade Triggers** (Automatic Recommendations):
- **LITE → STANDARD**: Team size >= 3 OR first paying customer
- **STANDARD → PROFESSIONAL**: Team size >= 10 OR enterprise customer
- **PROFESSIONAL → ENTERPRISE**: Team size >= 50 OR compliance requirement (SOC 2, HIPAA)

**Implementation**:
- API: `POST /api/v1/projects/{id}/upgrade-tier`
- Pre-flight checks: Validate current compliance with target tier
- Grace period: 30-day countdown with daily reminder emails
- Rollback: Available within 7 days of upgrade

**Rationale**: Teams naturally grow; tier system grows with them without manual re-configuration.

---

### FR-004: Policy Enforcement Service Architecture

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN a policy evaluation request (e.g., gate check, merge validation)
WHEN the PolicyEnforcementService processes the request
THEN the service MUST:
1. Retrieve project tier from database
2. Load tier-specific policy pack configuration
3. Execute required checks based on tier (syntax, security, context, tests)
4. Aggregate results with tier-specific pass/fail logic
5. Return enforcement action (allow/warn/block) based on tier mode
6. Log evaluation to audit trail (who, what, when, tier, result)
```

**Service Architecture**:
```python
class PolicyEnforcementService:
    def evaluate_policy(self, project_id: str, policy_type: str, context: dict) -> PolicyResult:
        # 1. Retrieve project tier
        project = self.project_repo.get_by_id(project_id)
        tier = project.policy_pack_tier

        # 2. Load tier-specific policy pack
        policy_pack = TIER_POLICIES[tier]

        # 3. Execute required checks
        results = []
        for check in policy_pack["required_checks"]:
            result = self._execute_check(check, context)
            results.append(result)

        # 4. Aggregate with tier-specific logic
        pass_rate = sum(r.passed for r in results) / len(results)
        enforcement_action = self._determine_action(tier, pass_rate, policy_pack)

        # 5. Return enforcement decision
        return PolicyResult(
            tier=tier,
            enforcement_mode=policy_pack["enforcement_mode"],
            action=enforcement_action,
            results=results,
            timestamp=datetime.utcnow(),
        )
```

**Performance**:
- Evaluation latency: <200ms (p95) regardless of tier
- Cache policy pack configs in Redis (1-hour TTL)
- Async execution for non-blocking checks (LITE/STANDARD)

**Rationale**: Centralized service ensures consistent tier-based enforcement across all gates.

---

## 2. Technical Requirements

### TR-001: Database Schema - Project Tier Column

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the projects table in PostgreSQL
WHEN storing project tier classification
THEN the database MUST include:
- Column: policy_pack_tier ENUM('LITE', 'STANDARD', 'PROFESSIONAL', 'ENTERPRISE')
- Default: LITE (new projects start with advisory mode)
- Indexed: Yes (for fast tier-based queries)
- Audit: tier_change_history table (track all tier upgrades/downgrades)
```

**Migration**:
```sql
-- Alembic migration: add_policy_pack_tier_to_projects.py
ALTER TABLE projects
ADD COLUMN policy_pack_tier VARCHAR(20) DEFAULT 'LITE'
CHECK (policy_pack_tier IN ('LITE', 'STANDARD', 'PROFESSIONAL', 'ENTERPRISE'));

CREATE INDEX idx_projects_policy_tier ON projects(policy_pack_tier);

-- Audit trail table
CREATE TABLE tier_change_history (
    id UUID PRIMARY KEY,
    project_id UUID REFERENCES projects(id),
    from_tier VARCHAR(20),
    to_tier VARCHAR(20),
    changed_by UUID REFERENCES users(id),
    changed_at TIMESTAMP DEFAULT NOW(),
    reason TEXT,
    grace_period_end TIMESTAMP
);
```

**Rationale**: Explicit tier column enables fast policy lookups and tier-based filtering.

---

### TR-002: PolicyEnforcementService Implementation

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the backend service layer
WHEN implementing policy enforcement
THEN the system MUST provide PolicyEnforcementService with:
- Method: evaluate_policy(project_id, policy_type, context) → PolicyResult
- Method: get_tier_policy_pack(tier) → PolicyPackConfig
- Method: validate_upgrade_eligibility(project_id, target_tier) → UpgradeResult
- Caching: Redis cache for policy pack configs (1-hour TTL)
- Logging: Structured logs with tier context for all evaluations
```

**Service Location**: `backend/app/services/policy_enforcement_service.py`

**Dependencies**:
- `ProjectRepository` (retrieve project tier)
- `OPAService` (execute policy checks via Open Policy Agent)
- `RedisService` (cache policy pack configs)
- `AuditLogService` (log all enforcement decisions)

**Error Handling**:
- Fallback to LITE tier if project tier is NULL (backward compatibility)
- Retry OPA calls 3 times with exponential backoff
- Return WARN enforcement action on service errors (fail open for LITE/STANDARD, fail closed for PRO/ENT)

**Rationale**: Service abstraction enables consistent enforcement across all policy evaluation points.

---

### TR-003: MRPValidationService 5-Point Check Logic

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN a merge request validation request
WHEN MRPValidationService executes 5-point checks
THEN the service MUST implement tier-specific logic for:
1. Evidence Check: Query evidence_artifacts table, require completion based on tier
2. Test Check: Query CI/CD test results, enforce coverage threshold by tier
3. SAST Check: Query Semgrep scan results, filter by severity based on tier
4. Context Check: Parse AGENTS.md, validate <60 lines for PRO/ENT
5. VCR Check: Query code_reviews table, require N approvals based on tier
```

**Service Location**: `backend/app/services/mrp_validation_service.py`

**Tier-Specific Logic**:
```python
class MRPValidationService:
    def validate_merge_readiness(self, merge_request_id: str, project_tier: PolicyTier) -> MRPResult:
        checks = {
            "evidence_complete": self._check_evidence(merge_request_id, project_tier),
            "tests_passing": self._check_tests(merge_request_id, project_tier),
            "sast_clean": self._check_sast(merge_request_id, project_tier),
            "context_valid": self._check_context(merge_request_id, project_tier),
            "vcr_approved": self._check_vcr(merge_request_id, project_tier),
        }

        # Aggregate with tier-specific pass/fail
        if project_tier == PolicyTier.LITE:
            overall_pass = True  # Advisory only
        elif project_tier == PolicyTier.STANDARD:
            overall_pass = sum(c.status == "pass" for c in checks.values()) >= 2  # At least 2/5
        elif project_tier == PolicyTier.PROFESSIONAL:
            overall_pass = all(c.status in ["pass", "warn"] for c in checks.values())  # All pass/warn
        elif project_tier == PolicyTier.ENTERPRISE:
            overall_pass = all(c.status == "pass" for c in checks.values())  # All pass, no warnings

        return MRPResult(checks=checks, overall_pass=overall_pass, tier=project_tier)
```

**Rationale**: 5-point checks provide comprehensive readiness validation adapted to project risk level.

---

### TR-004: Tier Upgrade API Endpoint

**Priority**: P1 (HIGH)

**Requirement**:
```gherkin
GIVEN the API layer
WHEN a project owner requests tier upgrade
THEN the system MUST provide endpoint:
- Route: POST /api/v1/projects/{id}/upgrade-tier
- Request Body: { "target_tier": "PROFESSIONAL", "reason": "Enterprise customer requirement" }
- Response: { "upgrade_id": "uuid", "from_tier": "STANDARD", "to_tier": "PROFESSIONAL", "grace_period_end": "2026-03-01T00:00:00Z", "pre_flight_checks": [...] }
- Pre-flight Checks: Validate current compliance with target tier requirements
- Authorization: Project owner or admin only
```

**API Specification**:
```yaml
/api/v1/projects/{id}/upgrade-tier:
  post:
    summary: Upgrade project to higher tier
    parameters:
      - name: id
        in: path
        required: true
        schema:
          type: string
          format: uuid
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              target_tier:
                type: string
                enum: [STANDARD, PROFESSIONAL, ENTERPRISE]
              reason:
                type: string
                minLength: 10
                maxLength: 500
    responses:
      200:
        description: Upgrade initiated with grace period
        content:
          application/json:
            schema:
              type: object
              properties:
                upgrade_id:
                  type: string
                  format: uuid
                from_tier:
                  type: string
                to_tier:
                  type: string
                grace_period_end:
                  type: string
                  format: date-time
                pre_flight_checks:
                  type: array
                  items:
                    type: object
                    properties:
                      check_name:
                        type: string
                      status:
                        type: string
                        enum: [pass, warn, fail]
                      message:
                        type: string
      400:
        description: Invalid tier upgrade (e.g., downgrade not allowed)
      403:
        description: User not authorized to upgrade tier
      409:
        description: Upgrade already in progress
```

**Validation Rules**:
- Cannot downgrade tier (PROFESSIONAL → STANDARD not allowed)
- Cannot skip tiers (LITE → ENTERPRISE requires LITE → STANDARD → PROFESSIONAL → ENTERPRISE)
- Grace period: 30 days to comply with new tier requirements

**Rationale**: API-driven tier upgrades enable automated governance scaling as teams grow.

---

## 3. Quality Requirements

### QR-001: Policy Evaluation Performance

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN any policy evaluation request (any tier)
WHEN the PolicyEnforcementService processes the request
THEN the system MUST meet performance targets:
- Latency p95: <200ms (gate evaluation)
- Latency p99: <500ms (complex MRP validation)
- Throughput: 100+ evaluations/second (concurrent projects)
- Cache hit rate: >90% (policy pack configs in Redis)
```

**Benchmarking**:
- Measure with `pytest-benchmark` for all tier configurations
- Load test with 1000 concurrent evaluations (Locust)
- Profile with `py-spy` to identify bottlenecks

**Optimization Strategies**:
- Cache policy pack configs in Redis (1-hour TTL)
- Async execution for non-critical checks (LITE/STANDARD warnings)
- Database query optimization (indexed tier column)

**Rationale**: Fast policy evaluation ensures gates don't slow down developer workflow.

---

### QR-002: Tier Configuration Maintainability

**Priority**: P1 (HIGH)

**Requirement**:
```gherkin
GIVEN the 4 tier policy pack configurations
WHEN maintaining or updating tier requirements
THEN the system MUST ensure:
- Single source of truth: TIER_POLICIES constant in policy_enforcement_service.py
- Type safety: Python type hints for all PolicyPackConfig fields
- Validation: Pydantic schema for policy pack configs (catch errors at startup)
- Versioning: Policy pack version number tracked in database (rollback capability)
```

**Configuration Validation**:
```python
from pydantic import BaseModel, validator

class PolicyPackConfig(BaseModel):
    enforcement_mode: str  # 'advisory', 'soft', 'hard', 'strict'
    block_on_failure: bool
    required_checks: List[str]
    notifications: List[str]
    max_warnings: Optional[int]
    require_approvals: Optional[int]

    @validator('enforcement_mode')
    def validate_enforcement_mode(cls, v):
        allowed = ['advisory', 'soft', 'hard', 'strict']
        if v not in allowed:
            raise ValueError(f"Invalid enforcement_mode: {v}. Must be one of {allowed}")
        return v
```

**Rationale**: Type-safe configurations prevent runtime errors and enable confident policy updates.

---

### QR-003: Audit Trail Completeness

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN any tier-related action (evaluation, upgrade, override)
WHEN the action completes
THEN the system MUST log to audit trail:
- Event type (policy_evaluated, tier_upgraded, enforcement_overridden)
- Project ID + tier at time of action
- User ID (who triggered the action)
- Timestamp (UTC, millisecond precision)
- Context (merge request ID, gate type, policy pack version)
- Result (pass/fail/warn, enforcement action taken)
```

**Audit Log Schema**:
```sql
CREATE TABLE tier_audit_log (
    id UUID PRIMARY KEY,
    event_type VARCHAR(50) NOT NULL,
    project_id UUID REFERENCES projects(id),
    project_tier VARCHAR(20) NOT NULL,
    user_id UUID REFERENCES users(id),
    timestamp TIMESTAMP DEFAULT NOW(),
    context JSONB,
    result JSONB,
    ip_address INET,
    user_agent TEXT
);

CREATE INDEX idx_tier_audit_project ON tier_audit_log(project_id, timestamp DESC);
CREATE INDEX idx_tier_audit_user ON tier_audit_log(user_id, timestamp DESC);
```

**Retention Policy**:
- LITE/STANDARD: 90 days
- PROFESSIONAL: 1 year
- ENTERPRISE: 7 years (compliance requirement)

**Rationale**: Complete audit trails enable compliance reporting and incident investigation.

---

## 4. Tier-Specific Requirements

### TSR-001: LITE Tier - Advisory Mode Behavior

**Applicable Tier**: LITE

**Requirement**:
```gherkin
GIVEN a project on LITE tier
WHEN any policy check fails
THEN the system MUST:
- NOT block merge (advisory only)
- Display warnings in dashboard UI
- Send daily digest email (max 1 per day, no spam)
- Suggest tier upgrade if warnings exceed 10 per week
```

**UI Display**:
- Warning badge on dashboard (yellow color)
- Dismissible notifications (user can close)
- No gate blocking UI (no red "BLOCKED" banner)

**Rationale**: LITE tier enables fast iteration for startups without governance overhead.

---

### TSR-002: STANDARD Tier - Soft Enforcement Warnings

**Applicable Tier**: STANDARD

**Requirement**:
```gherkin
GIVEN a project on STANDARD tier
WHEN policy checks fail
THEN the system MUST:
- Allow merge if <50% checks fail (soft enforcement)
- Block merge if >=50% checks fail (escalation to hard mode)
- Send immediate email notification on failures
- Track warning history (suggest PRO upgrade at 10 warnings/month)
```

**Warning Threshold Logic**:
```python
if failed_checks / total_checks >= 0.5:
    enforcement_action = "block"  # Escalate to hard mode
else:
    enforcement_action = "warn"  # Soft mode
```

**Rationale**: STANDARD tier balances flexibility with quality enforcement for growing teams.

---

### TSR-003: PROFESSIONAL Tier - Hard Enforcement Blocking

**Applicable Tier**: PROFESSIONAL

**Requirement**:
```gherkin
GIVEN a project on PROFESSIONAL tier
WHEN ANY required check fails
THEN the system MUST:
- Block merge immediately (hard enforcement)
- Require manual override from Tech Lead or Senior Engineer
- Send Slack notification to team channel
- Escalate to CTO if >3 overrides per sprint
```

**Override Workflow**:
1. Developer requests override (provide justification)
2. Tech Lead approves/rejects via dashboard
3. If approved, merge allowed with warning flag
4. All overrides tracked in audit log

**Rationale**: PROFESSIONAL tier ensures quality gates are enforced but allows pragmatic overrides.

---

### TSR-004: ENTERPRISE Tier - Zero Tolerance Strict Mode

**Applicable Tier**: ENTERPRISE

**Requirement**:
```gherkin
GIVEN a project on ENTERPRISE tier
WHEN ANY check fails (including warnings)
THEN the system MUST:
- Block merge with NO override option (strict enforcement)
- Require 2-person approval (2-person rule for exceptions)
- Send PagerDuty alert if critical security scan fails
- Log all violations to compliance dashboard
- Enforce 0 warnings policy (warnings = failures in ENTERPRISE)
```

**2-Person Rule**:
- First approver: Tech Lead or Security Lead
- Second approver: CTO or Compliance Officer
- Both must explicitly approve in UI (no auto-approval)

**Compliance Dashboard**:
- Real-time violation count (target: 0)
- Trend chart (violations over time)
- Automated compliance report generation (monthly)

**Rationale**: ENTERPRISE tier provides audit-ready governance for regulated industries (finance, healthcare).

---

## 5. Acceptance Criteria

| ID | Criterion | Test Method | LITE | STD | PRO | ENT |
|----|-----------|-------------|------|-----|-----|-----|
| AC-001 | Policy pack loaded based on project tier | Unit test with 4 tier mocks | ✅ | ✅ | ✅ | ✅ |
| AC-002 | Enforcement mode matches tier configuration | Integration test (LITE=advisory, PRO=hard) | ✅ | ✅ | ✅ | ✅ |
| AC-003 | MRP 5-point validation varies by tier | E2E test with tier-specific requirements | ✅ | ✅ | ✅ | ✅ |
| AC-004 | LITE tier allows merge despite failures | E2E test (fail all checks, merge succeeds) | ✅ | ❌ | ❌ | ❌ |
| AC-005 | STANDARD tier warns but allows merge if <50% fail | Integration test (2/5 checks fail = warn + allow) | ❌ | ✅ | ❌ | ❌ |
| AC-006 | PROFESSIONAL tier blocks merge on any required check failure | E2E test (1 critical check fail = block) | ❌ | ❌ | ✅ | ✅ |
| AC-007 | ENTERPRISE tier enforces 2-person approval rule | E2E test (require 2 approvals for override) | ❌ | ❌ | ❌ | ✅ |
| AC-008 | Tier upgrade API validates eligibility | API test (LITE → ENT = 400 error) | ✅ | ✅ | ✅ | ✅ |
| AC-009 | Grace period allows 30 days to comply with new tier | Integration test (upgrade + 30-day countdown) | ✅ | ✅ | ✅ | ✅ |
| AC-010 | Policy evaluation completes in <200ms (p95) | Load test with 1000 concurrent evaluations | ✅ | ✅ | ✅ | ✅ |
| AC-011 | Audit log captures all tier actions | E2E test (verify log entries for each action) | ✅ | ✅ | ✅ | ✅ |
| AC-012 | Backward compatibility: NULL tier defaults to LITE | Database migration test (existing projects) | ✅ | ❌ | ❌ | ❌ |

**Total**: 12 acceptance criteria (100% coverage across all tiers)

---

## 6. Cross-References

### Related Specifications
- **[SPEC-0001](./SPEC-0001-Anti-Vibecoding.md)**: Anti-Vibecoding quality assurance (4-tier classification)
- **[SPEC-0002](./SPEC-0002-Specification-Standard.md)**: Specification Standard (Framework 6.0.5 format)
- **[SPEC-0004](./SPEC-0004-Policy-Guards-Design.md)**: OPA policy guards (enforcement engine)
- **[SPEC-0009](./SPEC-0009-Codegen-Service-Specification.md)**: Codegen Service Specification
- **[SPEC-0010](./SPEC-0010-IR-Processor-Specification.md)**: IR Processor Specification

### Framework Documents
- **SDLC 5.2.0 - Section 02-GOVERN**: 4-Tier Classification methodology
- **SDLC 5.3.0 - Section 7**: Quality Assurance System with tier-specific requirements

### Implementation Files
- `backend/app/services/policy_enforcement_service.py`: PolicyEnforcementService implementation
- `backend/app/services/mrp_validation_service.py`: MRP 5-point validation service
- `backend/app/models/project.py`: Project model with policy_pack_tier column
- `backend/app/api/routes/projects.py`: Tier upgrade API endpoint
- `backend/alembic/versions/XXX_add_policy_pack_tier.py`: Database migration

---

## 7. Dependencies

### Upstream Dependencies (Must Exist Before Implementation)
- ✅ **SDLC Framework 5.2.0**: 4-Tier Classification methodology defined
- ✅ **OPA Integration**: Policy evaluation engine (SPEC-0004)
- ✅ **Projects Table**: Database schema for project tier storage
- ✅ **RBAC System**: Role-based access control for override approvals

### Downstream Dependencies (Blocked Until This Spec Completes)
- ⏳ **MRP Dashboard UI**: Visual display of 5-point validation per tier
- ⏳ **Tier Upgrade Wizard**: Guided workflow for tier transitions
- ⏳ **Compliance Reporting**: Automated compliance reports for ENTERPRISE tier
- ⏳ **Override Approval UI**: 2-person approval workflow for ENTERPRISE

---

## 8. Related Standards

### Industry Standards
- **SDLC Framework 5.2.0**: 4-Tier Classification (LITE/STANDARD/PROFESSIONAL/ENTERPRISE)
- **OWASP ASVS Level 2**: Security verification standards (PROFESSIONAL/ENTERPRISE tiers)
- **SOC 2 Type II**: Audit compliance requirements (ENTERPRISE tier)
- **HIPAA**: Healthcare data compliance (ENTERPRISE tier with 2-person rule)

### Internal Standards
- **Zero Mock Policy**: All policy pack configs are production-ready (no TODOs)
- **Contract-First API Design**: OpenAPI 3.0 specification for tier upgrade endpoint
- **AGPL Containment**: Network-only access to OPA (no AGPL library imports)
- **Performance Budget**: <200ms p95 latency for all policy evaluations

---

## 9. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-01-30 | Backend Lead + CTO | Initial Framework 6.0.5 migration from ADR-036 |

---

## 10. Approval

| Role | Name | Status | Date | Signature |
|------|------|--------|------|-----------|
| **CTO** | [CTO Name] | ✅ APPROVED | 2026-01-23 | [Digital Signature] |
| **Backend Lead** | [Backend Lead Name] | ✅ APPROVED | 2026-01-23 | [Digital Signature] |
| **Product Manager** | [PM Name] | ✅ REVIEWED | 2026-01-23 | [Digital Signature] |

---

**Document Status**: ✅ APPROVED - Ready for Implementation
**Framework Compliance**: ✅ Framework 6.0.5 (YAML frontmatter, BDD requirements, tier-specific tables)
**Spec Migration**: ✅ Complete (ADR-036 → SPEC-0008)

---

*SPEC-0008 - 4-Tier Policy Enforcement. Graduated governance from startups to enterprises. Zero Mock Policy compliant. Framework-First methodology.*
