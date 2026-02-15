# SPEC-0021: Stage Consistency Validation Service

**Version**: 1.0.0
**Status**: DRAFT
**Created**: February 1, 2026
**Framework Version**: SDLC 6.0.5
**Type**: Service Specification
**Owner**: CTO Office + QA Team (BFlow)
**Approval**: Pending

---

## Executive Summary

### Purpose

This specification defines the **Stage Consistency Validation Service** - a systematic process to ensure consistency between Stage 01 (Specifications), Stage 02 (Design), Stage 03 (Integration), and Stage 04 (Implementation) throughout the software development lifecycle.

**Problem Statement**: Teams often maintain specifications, design documents, API contracts, and code in separate silos, leading to **drift** where code no longer matches design, or design no longer reflects specifications. This drift causes:
- Rework (discovered during testing)
- Communication gaps (team members working from different sources of truth)
- Technical debt (undocumented changes)
- Failed audits (evidence doesn't match reality)

**Solution**: Automated stage consistency validation with pre-implementation and post-implementation checklists, enforced through CI/CD gates.

### Key Features

1. **4-Stage Consistency Model**: Validates consistency across planning → design → integration → implementation
2. **Pre/Post Implementation Checklists**: Systematic validation before and after code changes
3. **Artifact Integrity Hashing**: SHA256 checksums to detect post-approval modifications
4. **SSOT Validation**: Single Source of Truth validation mechanism
5. **Tier-Specific Requirements**: Different validation depths for LITE/STANDARD/PROFESSIONAL/ENTERPRISE

### Success Metrics

| Metric | Baseline (Sprint 134) | Target (Sprint 135+) | Measurement |
|--------|----------------------|---------------------|-------------|
| Stage consistency violations | 182 violations | <10 violations | Evidence validator output |
| Documentation lag | Variable | 0 sprints >24h | Sprint Governance Rule 2 |
| Stage rollback rate | Unknown | <5% | Sprint governance metrics |
| Cross-stage conflicts | Manual detection | Automated CI/CD blocking | SSOT validator |

---

## 1. The 4-Stage Consistency Model

### 1.1 Stage Definitions

```yaml
Stage 01 (PLANNING):
  Purpose: WHAT - Define requirements and specifications
  Outputs:
    - Requirements documents
    - API specifications (OpenAPI 3.0)
    - User stories
  Gate: G1 (Legal + Market Validation)

Stage 02 (DESIGN):
  Purpose: HOW - Define architecture and design
  Outputs:
    - ADRs (Architecture Decision Records)
    - System architecture diagrams
    - Database schema designs
  Gate: G2 (Design Ready)

Stage 03 (INTEGRATE):
  Purpose: CONTRACTS - Define integration points
  Outputs:
    - API contracts (OpenAPI validated)
    - Integration strategy documents
    - Third-party integration agreements
  Gate: G2 (parallel with Stage 02)

Stage 04 (BUILD):
  Purpose: CODE - Implement the design
  Outputs:
    - Source code
    - Unit tests
    - Code reviews
  Gate: G3 (Ship Ready)
```

### 1.2 Consistency Dependencies

```
Stage 01 ←→ Stage 02 ←→ Stage 03 ←→ Stage 04
   ↓           ↓           ↓           ↓
  WHAT  →    HOW    →  CONTRACTS →   CODE
```

**Consistency Rules**:
1. **Stage 02 MUST reference Stage 01**: Every ADR must cite requirements from Stage 01
2. **Stage 03 MUST align with Stage 02**: API contracts must match architecture design
3. **Stage 04 MUST implement Stage 02/03**: Code must follow design and respect API contracts
4. **Backward updates required**: If Stage 04 requires design changes, Stage 02 ADRs MUST be updated

---

## 2. Pre-Implementation Checklist

**When to Use**: Before starting any code implementation (Stage 04)

### 2.1 Stage 01 Verification

```yaml
Checklist:
  - [ ] Stage 01 specification exists in docs/01-planning/
  - [ ] Requirements approved (G1 gate passed)
  - [ ] API specification defined (OpenAPI 3.0)
  - [ ] User stories prioritized
  - [ ] No pending requirement changes
  - [ ] Specification version recorded

Validation Command:
  sdlcctl validate-stage --stage 01 --gate G1

Expected Output:
  ✅ Stage 01 COMPLETE
  ✅ G1 Gate PASSED
  ✅ API Specification: docs/01-planning/05-API-Design/API-Specification.md
  ✅ Checksum: sha256:abc123...
```

### 2.2 Stage 02 Verification

```yaml
Checklist:
  - [ ] Stage 02 design exists in docs/02-design/
  - [ ] ADRs reference Stage 01 specifications
  - [ ] Architecture diagrams created
  - [ ] Design review completed
  - [ ] G2 gate passed (Design Ready)
  - [ ] No conflicts with Stage 01 identified

Validation Command:
  sdlcctl validate-stage --stage 02 --gate G2 \
    --check-references-to-stage 01

Expected Output:
  ✅ Stage 02 COMPLETE
  ✅ G2 Gate PASSED
  ✅ ADR count: 5 (minimum 3 for PROFESSIONAL)
  ✅ All ADRs reference Stage 01: YES
  ✅ Conflicts detected: 0
```

### 2.3 Stage 03 Verification (if applicable)

```yaml
Checklist:
  - [ ] API contracts validated (OpenAPI)
  - [ ] Integration strategy documented
  - [ ] Third-party dependencies identified
  - [ ] API contracts match Stage 02 architecture
  - [ ] No breaking changes introduced

Validation Command:
  sdlcctl validate-stage --stage 03 --gate G2 \
    --check-api-contracts \
    --compare-with-stage 02

Expected Output:
  ✅ Stage 03 COMPLETE
  ✅ API Contracts validated: docs/03-integrate/01-api-contracts/
  ✅ OpenAPI 3.0 valid: YES
  ✅ Breaking changes: 0
  ✅ Matches Stage 02 architecture: YES
```

### 2.4 Prerequisites Summary

```yaml
BEFORE implementing code (Stage 04):
  ✅ All prerequisite stages complete
  ✅ All prerequisite gates passed
  ✅ No conflicts between stages
  ✅ All artifacts integrity-checked (SHA256)

BLOCKING if not met:
  ❌ G3 gate evaluation will FAIL
  ❌ Sprint cannot proceed to testing (Stage 05)
  ❌ Documentation freeze activated
```

---

## 3. Post-Implementation Checklist

**When to Use**: After completing code implementation (Stage 04)

### 3.1 Code Implements Design Correctly

```yaml
Checklist:
  - [ ] Code follows Stage 02 architecture patterns
  - [ ] All ADR decisions implemented correctly
  - [ ] No deviations from design without new ADR
  - [ ] Code review passed (2+ reviewers for PROFESSIONAL)
  - [ ] Unit tests cover implementation

Validation Command:
  sdlcctl validate-implementation \
    --code backend/app/ \
    --design docs/02-design/01-ADRs/ \
    --check-adherence

Expected Output:
  ✅ Implementation matches design: YES
  ✅ ADR adherence: 100%
  ✅ Deviations detected: 0
  ⚠️  New patterns introduced: 2 (require new ADRs)
```

### 3.2 API Contracts Remain Valid

```yaml
Checklist:
  - [ ] API endpoints match Stage 03 contracts
  - [ ] Request/response schemas unchanged
  - [ ] No breaking changes introduced
  - [ ] OpenAPI spec regenerated (if changed)
  - [ ] API contract checksums updated

Validation Command:
  sdlcctl validate-api-contracts \
    --spec docs/03-integrate/01-api-contracts/openapi.yaml \
    --implementation backend/app/api/routes/ \
    --check-breaking-changes

Expected Output:
  ✅ API endpoints match spec: 64/64
  ✅ Breaking changes: 0
  ✅ Response schemas valid: YES
  ⚠️  New endpoints: 3 (update OpenAPI spec required)
```

### 3.3 Specifications Still Accurate

```yaml
Checklist:
  - [ ] Stage 01 requirements still met
  - [ ] No behavioral changes undocumented
  - [ ] User stories completed as specified
  - [ ] Acceptance criteria met
  - [ ] If requirements changed, updated in Stage 01

Validation Command:
  sdlcctl validate-requirements \
    --requirements docs/01-planning/03-Functional-Requirements/ \
    --implementation backend/app/ \
    --check-behavioral-changes

Expected Output:
  ✅ Requirements met: 45/45
  ✅ Behavioral changes detected: 2
  ⚠️  Requires documentation update: YES
      - docs/01-planning/03-Functional-Requirements/FR-012-Authentication.md
      - docs/01-planning/05-API-Design/API-Specification.md
```

### 3.4 Cross-Stage Consistency

```yaml
Checklist:
  - [ ] All 4 stages are consistent
  - [ ] Evidence files updated
  - [ ] Artifact checksums recorded
  - [ ] SSOT validation passed
  - [ ] No pending documentation updates

Validation Command:
  sdlcctl validate-consistency \
    --stage 01 docs/01-planning/ \
    --stage 02 docs/02-design/ \
    --stage 03 docs/03-integrate/ \
    --stage 04 backend/app/ \
    --output consistency-report.json

Expected Output:
  ✅ Stage 01 ←→ Stage 02: CONSISTENT
  ✅ Stage 02 ←→ Stage 03: CONSISTENT
  ✅ Stage 03 ←→ Stage 04: CONSISTENT
  ✅ Stage 01 ←→ Stage 04: CONSISTENT
  ✅ Overall consistency: 100%
  ✅ Violations detected: 0
```

---

## 4. Validation Tools & Implementation

### 4.1 CLI Commands

```bash
# Install SDLC CLI (if not already installed)
pip install sdlcctl

# Validate single stage
sdlcctl validate-stage --stage 01 --gate G1

# Validate cross-stage consistency
sdlcctl validate-consistency \
  --stage 01 docs/01-planning/ \
  --stage 02 docs/02-design/ \
  --stage 03 docs/03-integrate/ \
  --stage 04 backend/app/ \
  --output consistency-report.json

# Generate consistency report
sdlcctl report-consistency \
  --input consistency-report.json \
  --format html \
  --output docs/reports/consistency-report.html

# Update artifact checksums
sdlcctl update-checksums \
  --stage 01 \
  --stage 02 \
  --stage 03 \
  --output docs/artifact-checksums.json
```

### 4.2 CI/CD Integration

```yaml
# .github/workflows/validate-consistency.yml
name: Stage Consistency Validation

on:
  pull_request:
    paths:
      - 'backend/**'
      - 'docs/**'

jobs:
  validate-consistency:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install SDLC CLI
        run: pip install sdlcctl

      - name: Validate Stage Consistency
        run: |
          sdlcctl validate-consistency \
            --stage 01 docs/01-planning/ \
            --stage 02 docs/02-design/ \
            --stage 03 docs/03-integrate/ \
            --stage 04 backend/app/ \
            --output consistency-report.json

      - name: Check for Violations
        run: |
          VIOLATIONS=$(jq '.violations | length' consistency-report.json)
          if [ "$VIOLATIONS" -gt 0 ]; then
            echo "❌ Stage consistency violations detected: $VIOLATIONS"
            jq '.violations' consistency-report.json
            exit 1
          else
            echo "✅ Stage consistency validation PASSED (0 violations)"
          fi

      - name: Upload Consistency Report
        uses: actions/upload-artifact@v3
        with:
          name: consistency-report
          path: consistency-report.json
```

### 4.3 Pre-commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: stage-consistency
        name: Validate Stage Consistency
        entry: sdlcctl validate-consistency
        args:
          - --stage 01 docs/01-planning/
          - --stage 02 docs/02-design/
          - --stage 03 docs/03-integrate/
          - --stage 04 backend/app/
          - --output consistency-report.json
        language: system
        files: '\.(md|py|ts|tsx)$'
        pass_filenames: false
```

---

## 5. Artifact Integrity Hashing

### 5.1 Purpose

**Problem**: Documents can be modified after approval, creating "approved" documents that don't match what was actually approved.

**Solution**: SHA256 checksums recorded at gate approval time, verified before next stage.

### 5.2 Checksum Recording

```yaml
Checksum Recording Points:
  - G1 Pass: Record Stage 01 artifact checksums
  - G2 Pass: Record Stage 02 and Stage 03 artifact checksums
  - G3 Pass: Record Stage 04 artifact checksums

Artifacts to Hash:
  Stage 01:
    - Requirements documents
    - API specifications
    - User stories

  Stage 02:
    - ADRs (all)
    - Architecture diagrams (SVG/PNG)
    - Database schema files

  Stage 03:
    - API contracts (OpenAPI YAML/JSON)
    - Integration strategy documents

  Stage 04:
    - Git commit hash (for code)
    - Test coverage reports
    - Build artifacts
```

### 5.3 Checksum Storage

```json
{
  "$schema": "./artifact-checksums-schema.json",
  "project_id": "sdlc-orchestrator",
  "framework_version": "6.0.5",
  "recorded_at": "2026-02-01T10:00:00Z",
  "checksums": {
    "stage_01": {
      "gate": "G1",
      "passed_at": "2026-01-15T14:30:00Z",
      "artifacts": [
        {
          "path": "docs/01-planning/03-Functional-Requirements/FR-001-Authentication.md",
          "sha256": "abc123def456...",
          "size_bytes": 12345
        },
        {
          "path": "docs/01-planning/05-API-Design/API-Specification.md",
          "sha256": "def456ghi789...",
          "size_bytes": 34567
        }
      ]
    },
    "stage_02": {
      "gate": "G2",
      "passed_at": "2026-01-20T16:00:00Z",
      "artifacts": [
        {
          "path": "docs/02-design/01-ADRs/ADR-001-Multi-Tenant-Architecture.md",
          "sha256": "ghi789jkl012...",
          "size_bytes": 8901
        }
      ]
    },
    "stage_03": {
      "gate": "G2",
      "passed_at": "2026-01-20T16:00:00Z",
      "artifacts": [
        {
          "path": "docs/03-integrate/01-api-contracts/openapi.yaml",
          "sha256": "jkl012mno345...",
          "size_bytes": 15678
        }
      ]
    },
    "stage_04": {
      "gate": "G3",
      "passed_at": "2026-01-25T18:00:00Z",
      "artifacts": [
        {
          "path": "backend/app/",
          "git_commit_hash": "a1b2c3d4e5f6...",
          "note": "Code artifacts use Git commit hash instead of file checksums"
        }
      ]
    }
  }
}
```

### 5.4 Checksum Verification

```bash
# Verify artifact integrity before Stage 04 implementation
sdlcctl verify-integrity \
  --checksums docs/artifact-checksums.json \
  --stage 01 \
  --stage 02 \
  --stage 03

# Expected output if NO modifications:
✅ Stage 01 artifacts: 12/12 VALID
✅ Stage 02 artifacts: 8/8 VALID
✅ Stage 03 artifacts: 3/3 VALID
✅ Overall integrity: VERIFIED

# Expected output if modifications detected:
❌ Stage 02 artifacts: 7/8 VALID
⚠️  Modified after approval:
    - docs/02-design/01-ADRs/ADR-005-API-Gateway.md
    Expected: ghi789jkl012...
    Actual:   xyz987uvw654...
    Modified: 2026-01-22T10:30:00Z (2 days after G2 approval)

❌ Overall integrity: FAILED
⚠️  Recommendation: Re-approve modified documents before proceeding
```

---

## 6. Common Inconsistency Patterns

### 6.1 Anti-Pattern: Code-First Development

**Description**: Developers write code without consulting design documents.

**Detection**:
```bash
sdlcctl detect-code-first \
  --code backend/app/ \
  --design docs/02-design/01-ADRs/ \
  --threshold 0.3

Output:
  ⚠️  Code-first development detected
  ⚠️  New patterns introduced: 5
  ⚠️  Matching ADRs: 0
  ⚠️  Recommendation: Create ADRs for new patterns before G3 gate
```

**Fix**:
1. Document new patterns in ADRs
2. Get design review approval
3. Re-run consistency validation

### 6.2 Anti-Pattern: Stale Specifications

**Description**: Stage 01 specifications not updated when requirements change.

**Detection**:
```bash
sdlcctl detect-stale-specs \
  --requirements docs/01-planning/03-Functional-Requirements/ \
  --code backend/app/ \
  --check-behavioral-changes

Output:
  ⚠️  Stale specifications detected
  ⚠️  Behavioral changes: 3
  ⚠️  Updated in Stage 01: 0
  ⚠️  Recommendation: Update requirements before G3 gate
```

**Fix**:
1. Update Stage 01 requirements documents
2. Record artifact checksums
3. Re-approve G1 gate (if major changes)

### 6.3 Anti-Pattern: API Drift

**Description**: Code API endpoints don't match Stage 03 contracts.

**Detection**:
```bash
sdlcctl detect-api-drift \
  --spec docs/03-integrate/01-api-contracts/openapi.yaml \
  --implementation backend/app/api/routes/

Output:
  ❌ API drift detected
  ❌ Mismatched endpoints: 3
      - GET /users/{id} (spec) vs GET /api/v1/users/{id} (code)
      - POST /projects (spec) vs POST /api/v1/workspaces (code)
  ❌ Missing endpoints: 2
      - DELETE /users/{id} (in spec, not in code)
  ❌ Recommendation: Update API contracts or fix implementation
```

**Fix**:
1. Update OpenAPI spec to match implementation
2. OR fix implementation to match spec
3. Get API contract review approval
4. Re-run G2 gate validation

---

## 7. Tier-Specific Requirements

### 7.1 LITE Tier (1-2 developers)

```yaml
Pre-Implementation Checklist:
  - Stage 01: Optional (can skip for prototypes)
  - Stage 02: Recommended (at least 1 ADR)
  - Stage 03: Skip if no third-party APIs
  - Stage 04: Required

Post-Implementation Checklist:
  - Consistency validation: Optional
  - Artifact checksums: Optional
  - SSOT validation: Not required

Enforcement:
  - CI/CD gates: Not blocking (warnings only)
  - Documentation freeze: Not enforced
```

### 7.2 STANDARD Tier (3-10 developers)

```yaml
Pre-Implementation Checklist:
  - Stage 01: Recommended
  - Stage 02: Required (3+ ADRs)
  - Stage 03: Required if APIs exist
  - Stage 04: Required

Post-Implementation Checklist:
  - Consistency validation: Recommended
  - Artifact checksums: Recommended
  - SSOT validation: Enforced in CI/CD (warnings)

Enforcement:
  - CI/CD gates: Warnings for violations
  - Documentation freeze: Recommended
```

### 7.3 PROFESSIONAL Tier (10-50 developers)

```yaml
Pre-Implementation Checklist:
  - Stage 01: MANDATORY
  - Stage 02: MANDATORY (5+ ADRs)
  - Stage 03: MANDATORY if APIs exist
  - Stage 04: MANDATORY

Post-Implementation Checklist:
  - Consistency validation: MANDATORY
  - Artifact checksums: MANDATORY
  - SSOT validation: Enforced in CI/CD (blocking)

Enforcement:
  - CI/CD gates: Blocking for >10 violations
  - Documentation freeze: MANDATORY (24-hour rule)
  - Stage rollback: Automatic if exit criteria not met
```

### 7.4 ENTERPRISE Tier (50+ developers)

```yaml
Pre-Implementation Checklist:
  - All stages: MANDATORY
  - ADR count: 10+ for major features
  - Architecture review board approval required

Post-Implementation Checklist:
  - Consistency validation: MANDATORY + audit trail
  - Artifact checksums: MANDATORY + 7-year retention
  - SSOT validation: Enforced in CI/CD (blocking)

Enforcement:
  - CI/CD gates: Blocking for >5 violations
  - Documentation freeze: MANDATORY (24-hour rule)
  - Stage rollback: Automatic if exit criteria not met
  - Compliance audit: Quarterly review of consistency violations
```

---

## 8. Integration with Existing Gates

### 8.1 Gate-Stage Mapping

```yaml
G0.1 (Problem Definition):
  → Stage 00 entry validation

G0.2 (Solution Diversity):
  → Stage 00 → Stage 01 transition

G1 (Legal + Market Validation):
  → Stage 01 exit criteria
  → Record Stage 01 artifact checksums

G2 (Design Ready):
  → Stage 02 + Stage 03 exit criteria
  → Record Stage 02 + Stage 03 artifact checksums
  → Validate Stage 01 ←→ Stage 02 consistency

G3 (Ship Ready):
  → Stage 04 exit criteria
  → Record Stage 04 artifact checksums
  → Validate Stage 01 ←→ Stage 02 ←→ Stage 03 ←→ Stage 04 consistency
  → **CRITICAL**: Full consistency validation before ship

G4 (Deployed):
  → Stage 06 exit criteria
  → Final evidence vault commit
```

### 8.2 Enhanced G3 Gate Checklist

```yaml
G3 Checklist (PROFESSIONAL+ tier):

Code Quality:
  - [ ] All features implemented
  - [ ] Test coverage ≥80%
  - [ ] Performance budget met
  - [ ] Zero P0 bugs

**NEW - Stage Consistency Validation**:
  - [ ] Pre-implementation checklist completed (before coding)
  - [ ] Post-implementation checklist completed (after coding)
  - [ ] Stage 01 ←→ Stage 02 consistency: PASS
  - [ ] Stage 02 ←→ Stage 03 consistency: PASS
  - [ ] Stage 03 ←→ Stage 04 consistency: PASS
  - [ ] Stage 01 ←→ Stage 04 consistency: PASS
  - [ ] Overall consistency violations: <10 (PROFESSIONAL), <5 (ENTERPRISE)
  - [ ] Artifact checksums verified (no post-approval modifications)
  - [ ] SSOT validation: PASS

Exit Criteria Enhancement:
  ✅ All existing G3 criteria met
  ✅ Stage consistency validation PASSED
  ✅ Consistency report generated and reviewed
  ✅ CTO + CPO + Security Lead approval
```

---

## 9. Troubleshooting Guide

### 9.1 "Consistency validation failed: 25 violations"

**Symptom**: CI/CD blocks PR merge due to high violation count

**Root Causes**:
1. Documentation not updated after code changes
2. New patterns introduced without ADRs
3. API contracts outdated

**Fix**:
```bash
# 1. Generate detailed violation report
sdlcctl report-consistency \
  --input consistency-report.json \
  --format detailed

# 2. Group violations by type
sdlcctl analyze-violations \
  --input consistency-report.json \
  --group-by type

# 3. Fix most common violations first
#    Example: "Missing ADRs for new patterns"
sdlcctl generate-adr \
  --pattern new_authentication_flow \
  --output docs/02-design/01-ADRs/ADR-NEW-Auth-Flow.md

# 4. Re-run validation
sdlcctl validate-consistency \
  --stage 01 docs/01-planning/ \
  --stage 02 docs/02-design/ \
  --stage 03 docs/03-integrate/ \
  --stage 04 backend/app/ \
  --output consistency-report.json

# 5. Verify violations reduced
jq '.violations | length' consistency-report.json
```

### 9.2 "Artifact integrity check failed"

**Symptom**: Stage 02 ADR modified after G2 approval

**Root Cause**: Document edited after gate approval without re-approval

**Fix**:
```bash
# 1. Identify modified artifacts
sdlcctl verify-integrity \
  --checksums docs/artifact-checksums.json \
  --stage 02 \
  --verbose

# 2. Review changes
git diff <approval_commit> docs/02-design/01-ADRs/ADR-005.md

# 3. If changes are valid:
#    a. Get re-approval from design review board
#    b. Update checksums
sdlcctl update-checksums \
  --stage 02 \
  --output docs/artifact-checksums.json

# 4. If changes are accidental:
#    a. Revert to approved version
git checkout <approval_commit> -- docs/02-design/01-ADRs/ADR-005.md

# 5. Re-run integrity check
sdlcctl verify-integrity \
  --checksums docs/artifact-checksums.json \
  --stage 02
```

### 9.3 "SSOT validation failed: conflicting sprint numbers"

**Symptom**: Different documents reference different sprint numbers

**Root Cause**: Sprint numbering updated in some documents but not all

**Fix**:
```bash
# 1. Run SSOT validation (from Sprint Governance Rule 6)
tools/validate-sprint-consistency.sh docs/

# 2. Review conflicts
#    Example output:
#    ❌ CURRENT-SPRINT.md: Sprint 135
#    ❌ ROADMAP.md: Sprint 134
#    ❌ PROJECT-PLAN.md: Sprint 136

# 3. Determine correct sprint number
#    (usually CURRENT-SPRINT.md is source of truth)

# 4. Update all conflicting documents
#    Use search-and-replace
rg "Sprint 134" docs/ --files-with-matches | xargs sed -i 's/Sprint 134/Sprint 135/g'

# 5. Re-run SSOT validation
tools/validate-sprint-consistency.sh docs/

# Expected output:
# ✅ Sprint Consistency Validation PASSED
```

---

## 10. API Specification

### 10.1 Validation Endpoints

```yaml
POST /api/v1/stage-consistency/validate
  Description: Validate consistency across multiple stages
  Request:
    {
      "project_id": "sdlc-orchestrator",
      "stages": ["01", "02", "03", "04"],
      "paths": {
        "01": "docs/01-planning/",
        "02": "docs/02-design/",
        "03": "docs/03-integrate/",
        "04": "backend/app/"
      }
    }
  Response:
    {
      "overall_consistency": 95.2,
      "violations": [
        {
          "type": "missing_adr",
          "severity": "medium",
          "message": "New pattern 'async_background_jobs' requires ADR",
          "location": "backend/app/jobs/background_processor.py",
          "recommendation": "Create ADR documenting pattern choice"
        }
      ],
      "stage_transitions": [
        {"from": "01", "to": "02", "consistency": 100.0},
        {"from": "02", "to": "03", "consistency": 98.5},
        {"from": "03", "to": "04", "consistency": 92.3}
      ]
    }

POST /api/v1/stage-consistency/checksums/record
  Description: Record artifact checksums at gate approval
  Request:
    {
      "project_id": "sdlc-orchestrator",
      "stage": "02",
      "gate": "G2",
      "artifacts": [
        {
          "path": "docs/02-design/01-ADRs/ADR-001.md",
          "content": "<file content for hashing>"
        }
      ]
    }
  Response:
    {
      "recorded_at": "2026-02-01T10:00:00Z",
      "checksums": [
        {
          "path": "docs/02-design/01-ADRs/ADR-001.md",
          "sha256": "abc123def456...",
          "size_bytes": 12345
        }
      ]
    }

POST /api/v1/stage-consistency/checksums/verify
  Description: Verify artifact integrity against recorded checksums
  Request:
    {
      "project_id": "sdlc-orchestrator",
      "stage": "02",
      "artifacts": [
        {
          "path": "docs/02-design/01-ADRs/ADR-001.md",
          "content": "<file content for hashing>"
        }
      ]
    }
  Response:
    {
      "overall_status": "FAILED",
      "verified": 7,
      "failed": 1,
      "failures": [
        {
          "path": "docs/02-design/01-ADRs/ADR-005.md",
          "expected_sha256": "ghi789jkl012...",
          "actual_sha256": "xyz987uvw654...",
          "modified_at": "2026-01-22T10:30:00Z",
          "days_after_approval": 2
        }
      ]
    }

GET /api/v1/stage-consistency/report/{project_id}
  Description: Generate consistency report
  Response:
    {
      "project_id": "sdlc-orchestrator",
      "generated_at": "2026-02-01T10:00:00Z",
      "overall_consistency": 95.2,
      "violations_count": 12,
      "violations_by_type": {
        "missing_adr": 5,
        "api_drift": 3,
        "stale_spec": 2,
        "code_first": 2
      },
      "stage_consistency": {
        "01_02": 100.0,
        "02_03": 98.5,
        "03_04": 92.3,
        "01_04": 95.2
      },
      "artifact_integrity": {
        "stage_01": "VERIFIED",
        "stage_02": "FAILED",
        "stage_03": "VERIFIED",
        "stage_04": "VERIFIED"
      }
    }
```

---

## 11. Success Metrics & KPIs

### 11.1 Primary Metrics

| Metric | Target | Measurement | Owner |
|--------|--------|-------------|-------|
| **Consistency Score** | ≥95% | Automated validator | QA Team |
| **Violation Count** | <10 (PRO), <5 (ENT) | CI/CD reporting | Tech Lead |
| **Documentation Lag** | 0 sprints >24h | Sprint Governance Rule 2 | PM |
| **Stage Rollback Rate** | <5% | Sprint governance metrics | CTO |

### 11.2 Secondary Metrics

| Metric | Target | Measurement | Owner |
|--------|--------|-------------|-------|
| **Artifact Integrity Failures** | 0 per sprint | Checksum verification | Security Team |
| **API Drift Incidents** | <2 per quarter | API contract validation | API Team |
| **ADR Coverage** | 100% of patterns | Pattern detector | Architect |
| **SSOT Validation Failures** | 0 per sprint | CI/CD gates | DevOps |

### 11.3 Lagging Indicators

| Metric | Target | Measurement | Review Cadence |
|--------|--------|-------------|----------------|
| **Rework Due to Inconsistency** | <5% of sprint capacity | Sprint retro analysis | Monthly |
| **Failed Audits (Consistency)** | 0 per year | Compliance audit | Quarterly |
| **Technical Debt (Documentation)** | <10% of codebase | Code vs docs delta | Quarterly |

---

## 12. Rollout Plan

### Phase 1: Framework Update (Week 1)

```yaml
Tasks:
  - [ ] Create SPEC-0021 (this document)
  - [ ] Update CONTENT-MAP.md
  - [ ] Update Framework version to 6.0.5
  - [ ] Create Stage Consistency Validation Guide
  - [ ] Get CTO + QA Team approval
```

### Phase 2: CLI Implementation (Week 2-3)

```yaml
Tasks:
  - [ ] Implement sdlcctl validate-stage command
  - [ ] Implement sdlcctl validate-consistency command
  - [ ] Implement sdlcctl verify-integrity command
  - [ ] Implement sdlcctl update-checksums command
  - [ ] Write unit tests (95%+ coverage)
  - [ ] Write integration tests
```

### Phase 3: CI/CD Integration (Week 4)

```yaml
Tasks:
  - [ ] Create GitHub Actions workflow
  - [ ] Create pre-commit hook template
  - [ ] Test on SDLC Orchestrator project (Sprint 135)
  - [ ] Document CI/CD setup guide
  - [ ] Train development team
```

### Phase 4: Production Rollout (Week 5+)

```yaml
Tasks:
  - [ ] Enable in WARNING mode (Week 5)
  - [ ] Monitor for false positives
  - [ ] Enable in SOFT mode (Week 6, PROFESSIONAL tier)
  - [ ] Enable in FULL mode (Week 7, PROFESSIONAL tier)
  - [ ] Quarterly review and refinement
```

---

## Related Documents

**Framework:**
- [SDLC-Stage-Exit-Criteria.md](../../02-Core-Methodology/SDLC-Stage-Exit-Criteria.md) - Stage exit criteria definitions
- [SDLC-Stage-Dependencies.md](../../02-Core-Methodology/SDLC-Stage-Dependencies.md) - ADR-041 Stage Dependency Matrix
- [SDLC-Sprint-Governance.md](../../02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md) - 24-hour documentation rule
- [SDLC-Quality-Security-Gates.md](../../02-Core-Methodology/Governance-Compliance/SDLC-Quality-Security-Gates.md) - G0-G4 gate requirements

**Specifications:**
- [SPEC-0002-Specification-Standard.md](./SPEC-0002-Specification-Standard.md) - YAML frontmatter + BDD format
- [SPEC-0012-Validation-Pipeline-Interface.md](./SPEC-0012-Validation-Pipeline-Interface.md) - Test-fix validation pipeline
- [SPEC-0019-Conformance-Testing-Specification.md](./SPEC-0019-Conformance-Testing-Specification.md) - Framework conformance testing

**Implementation Guides:**
- [SDLC-Implementation-Guide.md](../../07-Implementation-Guides/SDLC-Implementation-Guide.md) - Framework implementation guide

---

## Approval

**QA Team (BFlow)**: ✅ APPROVED (February 1, 2026)
**CTO Office**: Pending
**Framework Release**: SDLC 6.0.5 (Pending)

---

**Document Status**: DRAFT
**Version**: 1.0.0
**Last Updated**: February 1, 2026
**Owner**: CTO Office + QA Team (BFlow)
