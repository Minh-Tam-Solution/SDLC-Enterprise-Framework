# SDLC Stage Consistency Validation - Implementation Guide

**Version**: 1.0.0
**Date**: February 1, 2026
**Status**: ACTIVE - PRODUCTION READY
**Framework**: SDLC 6.3.0
**Specification**: SPEC-0021 Stage Consistency Validation (moved to Orchestrator `docs/05-test/`)
**Target**: Developers, Tech Leads, QA Engineers implementing 4-stage consistency validation

---

## 🎯 30-Second Overview

**What is Stage Consistency Validation?**
- Prevents "spec drift" where implementation diverges from approved designs
- Validates consistency across 4 stages: Planning → Design → Integration → Build
- Enforces pre/post-implementation checklists for stage transitions
- Uses artifact integrity hashing (SHA256) to detect silent modifications

**Why use it?**
- **Problem Prevented**: Sprint 128-129 context drift (backend 100% complete, frontend 0%)
- **Cost Savings**: Automated validation reduces manual review time by ~60%
- **Risk Mitigation**: Early detection prevents costly rework
- **Developer Experience**: Clear checklists reduce cognitive load

**How to start?** (Pick your tier)
1. **LITE/STANDARD**: Manual checklists (start immediately)
2. **PROFESSIONAL**: Recommended checklists + checksums (2-day setup)
3. **ENTERPRISE**: Automated CI/CD validation (1-week setup)

---

## 🛤️ Pick Your Implementation Path

| Your Situation | Path | Time | Start Here |
|----------------|------|------|------------|
| **New project** (Greenfield) | Implement from Day 1 | 1 hour | [Quick Start - Greenfield](#-quick-start-greenfield-new-projects) |
| **Existing project** (Brownfield) | Incremental adoption | 1-2 days | [Quick Start - Brownfield](#-quick-start-brownfield-existing-projects) |
| **CI/CD Integration** | Automated validation | 1 week | [CI/CD Setup](#-cicd-integration-automated-validation) |

---

## 📊 Tier Selection Matrix

| Tier | Stage Validation Depth | Enforcement | Tooling | Time to Implement |
|------|------------------------|-------------|---------|-------------------|
| **LITE** | Manual checklists | Recommended | None | 1 hour |
| **STANDARD** | Manual checklists | Recommended | None | 1 hour |
| **PROFESSIONAL** | Checklists + Checksums | Mandatory | CLI (future) | 2 days |
| **ENTERPRISE** | Full automation | Mandatory + CI/CD blocking | CLI + CI/CD | 1 week |

**Recommended starting point**: PROFESSIONAL tier (best balance of effort vs. value)

---

## 🚀 Quick Start - Greenfield (New Projects)

**Time**: 1 hour | **Tier**: Any

### Step 1: Create Checklist Files (10 minutes)

Create `.sdlc/checklists/` directory in your project:

```bash
mkdir -p .sdlc/checklists
```

**Pre-Implementation Checklist** (`.sdlc/checklists/pre-implementation.md`):

```markdown
# Pre-Implementation Checklist

**Purpose**: Verify stage alignment BEFORE writing code (Stage 04)

## Stage 01 Verification (Specifications)
- [ ] Specification exists and is approved (G1 passed)
- [ ] Requirements are testable and measurable
- [ ] API specification is complete (OpenAPI 3.0 if applicable)
- [ ] User stories are prioritized and estimated
- [ ] Acceptance criteria defined

## Stage 02 Verification (Design Documents)
- [ ] ADR(s) exist and reference Stage 01 specs
- [ ] Architecture diagrams are current
- [ ] Design review is completed and approved
- [ ] Technical decisions are documented
- [ ] Design patterns identified

## Stage 03 Verification (Integration Contracts)
- [ ] API contracts validated (if applicable)
- [ ] Integration strategy documented
- [ ] Partner agreements signed (if applicable)
- [ ] OpenAPI/GraphQL schemas validated

## Stage Transition Verification
- [ ] No conflicts between stages identified
- [ ] All prerequisite gates passed (G0.1, G0.2, G1, G2)
- [ ] Team alignment confirmed (kick-off meeting held)
- [ ] Development environment ready

**Validation Date**: _____________
**Validated By**: _____________
**Issues Found**: _____________
```

**Post-Implementation Checklist** (`.sdlc/checklists/post-implementation.md`):

```markdown
# Post-Implementation Checklist

**Purpose**: Verify stages remain consistent AFTER writing code (Stage 04)

## Stage 04 Verification (Code Implementation)
- [ ] Code implements Stage 02 design correctly
- [ ] API contracts (Stage 03) remain valid
- [ ] Specifications (Stage 01) still accurate
- [ ] All 4 stages are consistent
- [ ] No orphaned code (all code has design reference)
- [ ] No orphaned specs (all specs have implementation)

## Evidence Verification
- [ ] Evidence files updated with implementation artifacts
- [ ] Test results attached (if Stage 05 entered)
- [ ] Code coverage report generated (if required by tier)
- [ ] Screenshots/demos captured (if UI changes)

## Documentation Verification
- [ ] README.md updated (if applicable)
- [ ] API documentation current (auto-generated from OpenAPI)
- [ ] ADRs updated (if design changed during implementation)
- [ ] CHANGELOG.md updated (if versioned release)

## Quality Gates
- [ ] G3 (Ship Ready) criteria met (if preparing for release)
- [ ] Code review completed (2+ approvers for PROFESSIONAL+)
- [ ] Security scan passed (Semgrep/SonarQube)
- [ ] Performance benchmarks met (if applicable)

**Validation Date**: _____________
**Validated By**: _____________
**Issues Found**: _____________
**Corrective Actions**: _____________
```

### Step 2: Integrate into Development Workflow (20 minutes)

**Add to Pull Request Template** (`.github/pull_request_template.md`):

```markdown
## Stage Consistency Validation

### Pre-Implementation Checklist
- [ ] Completed pre-implementation checklist (`.sdlc/checklists/pre-implementation.md`)
- [ ] All stages (01-04) aligned before coding

### Post-Implementation Checklist
- [ ] Completed post-implementation checklist (`.sdlc/checklists/post-implementation.md`)
- [ ] Verified stages remain consistent after changes

### Evidence Artifacts
- [ ] Attached checklist files to PR description
- [ ] Documented any stage conflicts found and resolved
```

### Step 3: Team Onboarding (30 minutes)

**Conduct 30-minute workshop**:

1. **Explain "Spec Drift" Problem** (5 min)
   - Show Sprint 128-129 example (backend 100%, frontend 0%)
   - Explain cost of late-stage inconsistency discovery

2. **Demonstrate Checklists** (10 min)
   - Walk through pre-implementation checklist
   - Walk through post-implementation checklist
   - Show how to fill them out

3. **Practice with Example** (10 min)
   - Use real project requirement
   - Team fills out pre-implementation checklist together
   - Identify any gaps

4. **Q&A** (5 min)
   - Clarify tier-specific requirements
   - Address concerns

### Step 4: First Validation (10 minutes)

**Run first validation on current work**:

```bash
# Manual validation (LITE/STANDARD)
1. Open `.sdlc/checklists/pre-implementation.md`
2. For current feature, check each box
3. If any box unchecked, address gap before coding
4. Save completed checklist in PR
```

**Success Criteria**:
- ✅ Checklists created and committed
- ✅ PR template updated
- ✅ Team trained (30-min workshop complete)
- ✅ First validation completed successfully

---

## 🚀 Quick Start - Brownfield (Existing Projects)

**Time**: 1-2 days | **Tier**: PROFESSIONAL+

### Phase 1: Baseline Assessment (Day 1 Morning)

**Step 1: Inventory Current Stages**

Run manual scan of your project structure:

```bash
# Stage 01: Planning artifacts
find . -path "*/01-planning/*" -o -path "*/planning/*" -o -path "*/requirements/*" -o -name "*.requirements.*" 2>/dev/null

# Stage 02: Design artifacts
find . -path "*/02-design/*" -o -path "*/design/*" -o -path "*/architecture/*" -o -name "ADR-*.md" 2>/dev/null

# Stage 03: Integration artifacts
find . -path "*/03-integrate/*" -o -path "*/integration/*" -o -name "openapi.yaml" -o -name "*.contract.*" 2>/dev/null

# Stage 04: Build artifacts
find . -name "*.py" -o -name "*.ts" -o -name "*.tsx" -o -name "*.js" 2>/dev/null | head -20
```

**Step 2: Create Gap Analysis Report**

Document findings in `.sdlc/stage-consistency-baseline.md`:

```markdown
# Stage Consistency Baseline Analysis

**Date**: February 1, 2026
**Project**: [Your Project Name]
**Assessed By**: [Your Name]

## Current State

| Stage | Artifacts Found | Location | Status |
|-------|-----------------|----------|--------|
| 01 Planning | 15 requirement files | `docs/requirements/` | ✅ Exists |
| 02 Design | 8 ADRs | `docs/adr/` | ⚠️ Incomplete (missing 3 features) |
| 03 Integration | 2 OpenAPI specs | `api/specs/` | ⚠️ Outdated (doesn't match code) |
| 04 Build | 247 source files | `src/` | ✅ Exists |

## Gaps Identified

1. **Missing Design Documents**:
   - Feature A (implemented but no ADR)
   - Feature B (implemented but no ADR)
   - Feature C (implemented but no ADR)

2. **Outdated Integration Contracts**:
   - `openapi.yaml` last updated 3 months ago
   - Code has 12 new endpoints not in spec

3. **Orphaned Requirements**:
   - Requirement REQ-042: Not implemented
   - Requirement REQ-053: Partially implemented

## Remediation Plan

**Priority 1** (This sprint):
- [ ] Create ADRs for Features A, B, C
- [ ] Update OpenAPI spec with current endpoints

**Priority 2** (Next sprint):
- [ ] Implement REQ-042 or mark as DEFERRED
- [ ] Complete REQ-053 implementation

**Priority 3** (Ongoing):
- [ ] Establish pre/post-implementation checklists
- [ ] Train team on stage consistency validation
```

### Phase 2: Incremental Remediation (Day 1 Afternoon)

**Don't stop development!** Remediate incrementally:

```yaml
week_1_strategy:
  focus: "Document existing work (retroactive ADRs)"
  approach: "1 feature per day"
  team_impact: "30 min/day"

  day_1:
    task: "Write ADR for Feature A"
    time: "30 minutes"

  day_2:
    task: "Write ADR for Feature B"
    time: "30 minutes"

  day_3:
    task: "Write ADR for Feature C"
    time: "30 minutes"

  day_4:
    task: "Update OpenAPI spec"
    time: "1 hour"

  day_5:
    task: "Validate all 4 stages aligned"
    time: "30 minutes"
```

### Phase 3: Process Integration (Day 2)

**Step 1: Update Development Process**

Add to your team's workflow documentation:

```markdown
## New Feature Development Process (Updated Feb 1, 2026)

### Before Coding (Stage 01-03)
1. Write requirement in `docs/requirements/{feature-id}.md`
2. Write ADR in `docs/adr/ADR-{number}-{feature}.md`
3. Update OpenAPI spec if API changes
4. Complete `.sdlc/checklists/pre-implementation.md`
5. Get Tech Lead approval

### During Coding (Stage 04)
6. Implement feature
7. Write tests
8. Keep OpenAPI spec synchronized

### After Coding (Stage 04 → 05)
9. Complete `.sdlc/checklists/post-implementation.md`
10. Verify all 4 stages consistent
11. Submit PR with checklists attached
```

**Step 2: First PR with New Process**

Create a sample PR demonstrating the new process:

```markdown
## PR: Implement User Profile API

### Stage Consistency Validation

**Pre-Implementation Checklist**: ✅ Attached (`.sdlc/checklists/pre-impl-PR-123.md`)
**Post-Implementation Checklist**: ✅ Attached (`.sdlc/checklists/post-impl-PR-123.md`)

### Stage Alignment

| Stage | Artifact | Status |
|-------|----------|--------|
| 01 Planning | `docs/requirements/REQ-089-user-profile.md` | ✅ Created |
| 02 Design | `docs/adr/ADR-043-user-profile-api.md` | ✅ Created |
| 03 Integration | `api/specs/openapi.yaml` (lines 234-267) | ✅ Updated |
| 04 Build | `src/api/users.py`, `src/api/profile.py` | ✅ Implemented |

### Validation Results

- [x] All 4 stages aligned
- [x] No conflicts detected
- [x] Evidence files updated
```

**Success Criteria**:
- ✅ Baseline assessment completed
- ✅ Gap analysis documented
- ✅ Remediation started (at least 1 feature documented)
- ✅ Process updated and communicated
- ✅ First PR with new process merged

---

## 🔧 Manual Validation Workflow (LITE/STANDARD)

**When to Use**: Every feature, before and after coding

### Pre-Implementation Validation

**Trigger**: Before writing any code for a feature

**Process**:

```bash
# 1. Open pre-implementation checklist
vim .sdlc/checklists/pre-implementation.md

# 2. For current feature, validate each stage:

# Stage 01 (Planning): Does specification exist?
ls docs/01-planning/04-functional-requirements/ | grep -i "feature-name"
# ✅ If yes: Check box
# ❌ If no: Create requirement document first

# Stage 02 (Design): Does ADR exist?
ls docs/02-design/01-ADRs/ | grep -i "feature-name"
# ✅ If yes: Check box
# ❌ If no: Create ADR first

# Stage 03 (Integration): Does API contract exist (if applicable)?
grep -i "feature-name" docs/03-integrate/01-api-contracts/*.yaml
# ✅ If yes: Check box
# ⚠️ If not applicable: Mark N/A
# ❌ If applicable but missing: Create contract first

# 3. Verify no conflicts
grep -r "conflicting-requirement" docs/
# ✅ If no conflicts: Proceed to coding
# ❌ If conflicts found: Resolve before coding

# 4. Save completed checklist
git add .sdlc/checklists/pre-implementation.md
git commit -m "chore: Pre-implementation validation for Feature X"
```

### Post-Implementation Validation

**Trigger**: After completing code implementation

**Process**:

```bash
# 1. Open post-implementation checklist
vim .sdlc/checklists/post-implementation.md

# 2. Verify code matches design
diff <(grep "function" docs/02-design/01-ADRs/ADR-043.md) <(grep "def " src/feature.py)
# ✅ If matches: Check box
# ❌ If diverges: Update ADR or fix code

# 3. Verify API contracts still valid
# Compare OpenAPI spec with actual routes
diff api/specs/openapi.yaml <(your-api-extract-tool src/)
# ✅ If matches: Check box
# ❌ If diverges: Update spec or fix routes

# 4. Verify all stages consistent
# Run cross-reference check (manual)
# - Every function has ADR reference?
# - Every API endpoint in spec?
# - Every requirement has test?

# 5. Save completed checklist
git add .sdlc/checklists/post-implementation.md
git commit -m "chore: Post-implementation validation for Feature X"
```

---

## 🔐 Artifact Integrity Hashing (PROFESSIONAL+)

**When to Use**: After gate approvals (G1, G2, G3) to detect silent modifications

### Setup Checksumming (One-Time)

```bash
# 1. Create checksums directory
mkdir -p .sdlc/checksums

# 2. Create checksum script
cat > .sdlc/scripts/record-checksums.sh <<'EOF'
#!/bin/bash
# Record SHA256 checksums for stage artifacts

STAGE=$1  # 01, 02, 03, or 04
OUTPUT_FILE=".sdlc/checksums/stage-${STAGE}.sha256"

case $STAGE in
  01)
    # Stage 01: Planning artifacts
    find docs/01-planning -type f -name "*.md" -exec sha256sum {} \; > "$OUTPUT_FILE"
    ;;
  02)
    # Stage 02: Design artifacts (ADRs)
    find docs/02-design/01-ADRs -type f -name "ADR-*.md" -exec sha256sum {} \; > "$OUTPUT_FILE"
    ;;
  03)
    # Stage 03: Integration artifacts (API specs)
    find docs/03-integrate -type f \( -name "*.yaml" -o -name "*.json" \) -exec sha256sum {} \; > "$OUTPUT_FILE"
    ;;
  04)
    # Stage 04: Build artifacts (source code)
    find src -type f \( -name "*.py" -o -name "*.ts" -o -name "*.tsx" \) -exec sha256sum {} \; > "$OUTPUT_FILE"
    ;;
  *)
    echo "Usage: $0 <stage: 01|02|03|04>"
    exit 1
    ;;
esac

echo "Checksums recorded for Stage $STAGE → $OUTPUT_FILE"
EOF

chmod +x .sdlc/scripts/record-checksums.sh
```

### Recording Checksums (After Gate Approval)

```bash
# After G1 approval (Planning complete)
.sdlc/scripts/record-checksums.sh 01

# After G2 approval (Design complete)
.sdlc/scripts/record-checksums.sh 02

# After API contracts validated (Integration complete)
.sdlc/scripts/record-checksums.sh 03

# After G3 approval (Build complete)
.sdlc/scripts/record-checksums.sh 04
```

### Validating Checksums (Detect Silent Modifications)

```bash
# Create validation script
cat > .sdlc/scripts/validate-checksums.sh <<'EOF'
#!/bin/bash
# Validate checksums to detect post-approval modifications

STAGE=$1
CHECKSUM_FILE=".sdlc/checksums/stage-${STAGE}.sha256"

if [ ! -f "$CHECKSUM_FILE" ]; then
  echo "❌ No checksums recorded for Stage $STAGE"
  echo "Run: .sdlc/scripts/record-checksums.sh $STAGE"
  exit 1
fi

echo "Validating checksums for Stage $STAGE..."
sha256sum -c "$CHECKSUM_FILE" 2>&1 | tee /tmp/checksum-validation.log

FAILED_COUNT=$(grep "FAILED" /tmp/checksum-validation.log | wc -l)

if [ "$FAILED_COUNT" -gt 0 ]; then
  echo ""
  echo "⚠️  WARNING: $FAILED_COUNT file(s) modified after approval!"
  echo ""
  echo "Modified files:"
  grep "FAILED" /tmp/checksum-validation.log | awk '{print "  - " $1}'
  echo ""
  echo "Action required:"
  echo "  1. Review changes to understand why artifacts were modified"
  echo "  2. If intentional: Re-approve with Tech Lead + update checksums"
  echo "  3. If unintentional: Revert to approved version"
  exit 1
else
  echo "✅ All checksums valid - no post-approval modifications detected"
  exit 0
fi
EOF

chmod +x .sdlc/scripts/validate-checksums.sh

# Run validation
.sdlc/scripts/validate-checksums.sh 01  # Validate Stage 01
.sdlc/scripts/validate-checksums.sh 02  # Validate Stage 02
# etc.
```

### Integration with Evidence Vault (SPEC-0016)

**For SDLC Orchestrator users** (future CLI):

```bash
# Record checksum in Evidence Vault
sdlcctl evidence attach \
  --spec-id SPEC-0043 \
  --stage 02-DESIGN \
  --artifact-type checksum \
  --file .sdlc/checksums/stage-02.sha256

# Validate against Evidence Vault
sdlcctl evidence validate \
  --spec-id SPEC-0043 \
  --stage 02-DESIGN \
  --artifact-type checksum
```

---

## 🤖 CI/CD Integration (Automated Validation)

**Tier**: ENTERPRISE | **Time**: 1 week setup

### GitHub Actions Workflow

**File**: `.github/workflows/stage-consistency.yml`

```yaml
name: Stage Consistency Validation

on:
  pull_request:
    branches: [main, develop]
    types: [opened, synchronize, reopened]
  push:
    branches: [main]

jobs:
  validate-stage-consistency:
    runs-on: ubuntu-latest
    timeout-minutes: 10

    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0  # Full history for cross-stage analysis

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y jq yq

      - name: Validate Stage 01 → 02 Alignment
        id: validate-01-02
        run: |
          echo "Validating Planning → Design alignment..."

          # Check that every ADR references at least one requirement
          ADRS=$(find docs/02-design/01-ADRs -name "ADR-*.md" 2>/dev/null || echo "")

          if [ -z "$ADRS" ]; then
            echo "::warning::No ADRs found - skipping validation"
            exit 0
          fi

          VIOLATIONS=0
          for adr in $ADRS; do
            # Look for requirement references (REQ-XXX or docs/01-planning links)
            if ! grep -qiE "(REQ-[0-9]+|docs/01-planning)" "$adr"; then
              echo "::error::$adr does not reference any requirements"
              VIOLATIONS=$((VIOLATIONS + 1))
            fi
          done

          if [ $VIOLATIONS -gt 0 ]; then
            echo "::error::Found $VIOLATIONS ADR(s) with no requirement references"
            exit 1
          fi

          echo "✅ All ADRs reference requirements"

      - name: Validate Stage 02 → 03 Alignment
        id: validate-02-03
        run: |
          echo "Validating Design → Integration alignment..."

          # Check that OpenAPI specs match ADR decisions
          OPENAPI_SPEC="docs/03-integrate/01-api-contracts/openapi.yaml"

          if [ ! -f "$OPENAPI_SPEC" ]; then
            echo "::warning::No OpenAPI spec found - skipping validation"
            exit 0
          fi

          # Extract API paths from OpenAPI
          API_PATHS=$(yq eval '.paths | keys | .[]' "$OPENAPI_SPEC" 2>/dev/null || echo "")

          # For each API path, check if there's an ADR mentioning it
          VIOLATIONS=0
          for path in $API_PATHS; do
            if ! grep -qr "$path" docs/02-design/01-ADRs/; then
              echo "::warning::API path $path not documented in any ADR"
              VIOLATIONS=$((VIOLATIONS + 1))
            fi
          done

          if [ $VIOLATIONS -gt 0 ]; then
            echo "::notice::$VIOLATIONS API path(s) missing ADR documentation"
          else
            echo "✅ All API paths documented in ADRs"
          fi

      - name: Validate Stage 03 → 04 Alignment
        id: validate-03-04
        run: |
          echo "Validating Integration → Build alignment..."

          OPENAPI_SPEC="docs/03-integrate/01-api-contracts/openapi.yaml"

          if [ ! -f "$OPENAPI_SPEC" ]; then
            echo "::warning::No OpenAPI spec - skipping validation"
            exit 0
          fi

          # Extract API paths
          API_PATHS=$(yq eval '.paths | keys | .[]' "$OPENAPI_SPEC" 2>/dev/null || echo "")

          # Check if each path has implementation (simplified check)
          VIOLATIONS=0
          for path in $API_PATHS; do
            # Convert /users/{id} → /users/
            search_path=$(echo "$path" | sed 's/{[^}]*}//g' | sed 's/\/\//\//g')

            # Search for route definition in source code
            if ! grep -qr "route.*$search_path" src/ 2>/dev/null; then
              echo "::error::API path $path defined in spec but not implemented in code"
              VIOLATIONS=$((VIOLATIONS + 1))
            fi
          done

          if [ $VIOLATIONS -gt 0 ]; then
            echo "::error::Found $VIOLATIONS API path(s) with no implementation"
            exit 1
          fi

          echo "✅ All API paths have implementations"

      - name: Validate Artifact Integrity (if checksums exist)
        id: validate-checksums
        run: |
          if [ -d ".sdlc/checksums" ]; then
            echo "Validating artifact integrity..."

            for checksum_file in .sdlc/checksums/*.sha256; do
              if [ -f "$checksum_file" ]; then
                echo "Checking $checksum_file..."
                if sha256sum -c "$checksum_file" --status; then
                  echo "✅ $(basename $checksum_file) - no modifications"
                else
                  echo "::warning::$(basename $checksum_file) - files modified after approval"
                  sha256sum -c "$checksum_file" 2>&1 | grep FAILED || true
                fi
              fi
            done
          else
            echo "::notice::No checksums found - skipping integrity validation"
          fi

      - name: Generate Validation Report
        if: always()
        run: |
          cat > /tmp/stage-consistency-report.md <<EOF
          # Stage Consistency Validation Report

          **PR**: #${{ github.event.pull_request.number }}
          **Commit**: ${{ github.sha }}
          **Date**: $(date -u +"%Y-%m-%d %H:%M:%S UTC")

          ## Validation Results

          | Stage Transition | Status | Details |
          |------------------|--------|---------|
          | Stage 01 → 02 (Planning → Design) | ${{ steps.validate-01-02.outcome }} | ADR-requirement alignment |
          | Stage 02 → 03 (Design → Integration) | ${{ steps.validate-02-03.outcome }} | API spec-ADR alignment |
          | Stage 03 → 04 (Integration → Build) | ${{ steps.validate-03-04.outcome }} | API implementation check |
          | Artifact Integrity | ${{ steps.validate-checksums.outcome }} | SHA256 checksum validation |

          ## Next Steps

          - Review any warnings above
          - Ensure all stages are aligned before merge
          - Update checksums after approval if artifacts changed
          EOF

          cat /tmp/stage-consistency-report.md

      - name: Comment on PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('/tmp/stage-consistency-report.md', 'utf8');

            // Check if validation failed
            const validate0102 = '${{ steps.validate-01-02.outcome }}';
            const validate0304 = '${{ steps.validate-03-04.outcome }}';

            let emoji = '✅';
            let title = 'Stage Consistency Validation Passed';

            if (validate0102 === 'failure' || validate0304 === 'failure') {
              emoji = '❌';
              title = 'Stage Consistency Validation Failed';
            }

            const comment = `${emoji} **${title}**\n\n${report}`;

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

### GitLab CI/CD Example

**File**: `.gitlab-ci.yml`

```yaml
stage-consistency-validation:
  stage: test
  image: ubuntu:22.04

  before_script:
    - apt-get update && apt-get install -y jq yq git

  script:
    - echo "Validating stage consistency..."

    # Stage 01 → 02
    - |
      ADRS=$(find docs/02-design/01-ADRs -name "ADR-*.md" 2>/dev/null || echo "")
      if [ -n "$ADRS" ]; then
        for adr in $ADRS; do
          if ! grep -qiE "(REQ-[0-9]+|docs/01-planning)" "$adr"; then
            echo "ERROR: $adr does not reference requirements"
            exit 1
          fi
        done
      fi

    # Stage 03 → 04
    - |
      OPENAPI_SPEC="docs/03-integrate/01-api-contracts/openapi.yaml"
      if [ -f "$OPENAPI_SPEC" ]; then
        API_PATHS=$(yq eval '.paths | keys | .[]' "$OPENAPI_SPEC" 2>/dev/null || echo "")
        for path in $API_PATHS; do
          search_path=$(echo "$path" | sed 's/{[^}]*}//g')
          if ! grep -qr "route.*$search_path" src/ 2>/dev/null; then
            echo "ERROR: API path $path not implemented"
            exit 1
          fi
        done
      fi

    - echo "✅ Stage consistency validation passed"

  only:
    - merge_requests
    - main
```

---

## 📋 Common Validation Patterns

### Pattern 1: Orphaned Code Detection

**Problem**: Code exists with no design document reference

**Solution**:

```bash
# Find source files
find src -name "*.py" -o -name "*.ts" | while read -r file; do
  # Extract file purpose from docstring/comments
  purpose=$(head -20 "$file" | grep -oP "(?<=Purpose: ).*" || echo "Unknown")

  # Search for ADR mentioning this file or purpose
  if ! grep -qr "$(basename $file)" docs/02-design/01-ADRs/; then
    if ! grep -qr "$purpose" docs/02-design/01-ADRs/ 2>/dev/null; then
      echo "⚠️  Orphaned code: $file (no ADR reference)"
    fi
  fi
done
```

### Pattern 2: Orphaned Spec Detection

**Problem**: Specification exists but not implemented

**Solution**:

```bash
# Find all requirements
find docs/01-planning -name "REQ-*.md" | while read -r req; do
  REQ_ID=$(basename "$req" .md)

  # Search for implementation
  if ! grep -qr "$REQ_ID" src/; then
    # Check if marked as DEFERRED in spec
    if ! grep -q "Status.*DEFERRED" "$req"; then
      echo "⚠️  Orphaned spec: $REQ_ID (not implemented or deferred)"
    fi
  fi
done
```

### Pattern 3: API Drift Detection

**Problem**: OpenAPI spec doesn't match actual routes

**Solution** (Python FastAPI example):

```python
# generate-api-spec.py
import json
import yaml
from fastapi import FastAPI
from app.main import app  # Your FastAPI app

# Extract routes from FastAPI
spec = app.openapi()
actual_paths = set(spec['paths'].keys())

# Load documented OpenAPI spec
with open('docs/03-integrate/01-api-contracts/openapi.yaml') as f:
    documented_spec = yaml.safe_load(f)
    documented_paths = set(documented_spec['paths'].keys())

# Find drift
missing_docs = actual_paths - documented_paths
extra_docs = documented_paths - actual_paths

if missing_docs:
    print(f"⚠️  {len(missing_docs)} route(s) missing from docs:")
    for path in missing_docs:
        print(f"  - {path}")

if extra_docs:
    print(f"⚠️  {len(extra_docs)} route(s) documented but not implemented:")
    for path in extra_docs:
        print(f"  - {path}")

if not (missing_docs or extra_docs):
    print("✅ OpenAPI spec and routes are synchronized")
    exit(0)
else:
    exit(1)
```

### Pattern 4: Cross-Stage Reference Validation

**Problem**: Design doesn't reference requirements properly

**Solution**:

```bash
# validate-cross-references.sh
#!/bin/bash

echo "Validating cross-stage references..."

# Check ADRs reference requirements
VIOLATIONS=0
for adr in docs/02-design/01-ADRs/ADR-*.md; do
  # Extract referenced requirements
  REFS=$(grep -oP "REQ-[0-9]+" "$adr" || echo "")

  if [ -z "$REFS" ]; then
    echo "❌ $adr: No requirement references"
    VIOLATIONS=$((VIOLATIONS + 1))
    continue
  fi

  # Verify each referenced requirement exists
  for req_id in $REFS; do
    if ! find docs/01-planning -name "${req_id}.md" | grep -q .; then
      echo "❌ $adr: References non-existent $req_id"
      VIOLATIONS=$((VIOLATIONS + 1))
    fi
  done
done

if [ $VIOLATIONS -gt 0 ]; then
  echo "Total violations: $VIOLATIONS"
  exit 1
else
  echo "✅ All cross-references valid"
  exit 0
fi
```

---

## 🔍 Troubleshooting Guide

### Issue 1: "Too many false positives in CI/CD validation"

**Symptoms**:
- CI/CD fails frequently with warnings
- Developers frustrated by "noisy" validation

**Root Cause**:
- Validation rules too strict for project's actual workflow
- Project doesn't follow standard directory structure

**Solution**:

```yaml
# Customize validation in .sdlc/validation-config.yaml
stage_validation:
  stage_01_to_02:
    enabled: true
    strict_mode: false  # Allow warnings instead of errors
    custom_paths:
      planning: "docs/requirements"  # Non-standard path
      design: "docs/architecture"

  stage_03_to_04:
    enabled: true
    exclude_paths:
      - "src/legacy/*"  # Don't validate legacy code

  artifact_integrity:
    enabled: true
    stages: [02, 03]  # Only checksum design and integration
```

### Issue 2: "Checklists not being filled out"

**Symptoms**:
- PRs merged without completed checklists
- Team not using validation process

**Root Cause**:
- Process not enforced
- Checklists too long/complex
- No accountability

**Solution**:

1. **Enforce in PR Template** (required sections):
```markdown
### Stage Consistency (REQUIRED)

**Pre-Implementation Checklist**:
- [ ] Attached as file: `.sdlc/checklists/pre-impl-PR-{number}.md`

**Post-Implementation Checklist**:
- [ ] Attached as file: `.sdlc/checklists/post-impl-PR-{number}.md`

**Note**: PR cannot be merged without both checklists. Tech Lead will verify.
```

2. **Simplify Checklists** (tier-specific):
```markdown
# LITE Tier Pre-Implementation Checklist (Simplified)

- [ ] Requirement exists (any format)
- [ ] Design notes exist (can be PR description)
- [ ] No obvious conflicts

That's it! Keep it simple for LITE tier.
```

3. **Add Accountability**:
- Tech Lead reviews checklists in code review
- PROFESSIONAL+ tier: Use CODEOWNERS to enforce
```
# .github/CODEOWNERS
.sdlc/checklists/  @tech-lead @senior-devs
```

### Issue 3: "Checksums constantly failing"

**Symptoms**:
- Checksum validation always fails
- Files legitimately need updates after approval

**Root Cause**:
- Artifacts change frequently (normal iteration)
- Checksums recorded too early (before G-Sprint-Close)

**Solution**:

1. **Record checksums at correct gate**:
```bash
# DON'T record during development
# DO record only after gate approval

# After G1 (Planning APPROVED)
.sdlc/scripts/record-checksums.sh 01

# After G2 (Design APPROVED)
.sdlc/scripts/record-checksums.sh 02

# NOT after G-Sprint-Close (too early - implementation may iterate)
```

2. **Update checksums when needed**:
```bash
# If artifacts legitimately changed (e.g., bug fix in ADR)
# 1. Get Tech Lead approval for change
# 2. Update checksums
.sdlc/scripts/record-checksums.sh 02

# 3. Document reason
git commit -m "chore: Update Stage 02 checksums after ADR-043 correction (Tech Lead approved)"
```

### Issue 4: "Can't find stage artifacts in non-standard project"

**Symptoms**:
- Project doesn't use `docs/01-planning/`, `docs/02-design/`, etc.
- Validation scripts fail

**Root Cause**:
- Project uses different directory structure
- Legacy project structure

**Solution**:

Create project-specific validation config (`.sdlc/project-structure.yaml`):

```yaml
# Custom directory mappings
stage_directories:
  01_planning: "requirements"      # Instead of docs/01-planning
  02_design: "architecture/adr"    # Instead of docs/02-design
  03_integrate: "api/contracts"    # Instead of docs/03-integrate
  04_build: "app/src"              # Instead of src

# Custom file patterns
artifact_patterns:
  planning: ["*.req.md", "*.spec.md"]
  design: ["arch-*.md", "decision-*.md"]
  integration: ["*.openapi.yml", "*.graphql"]
  build: ["**/*.ts", "**/*.tsx"]
```

Then update validation scripts to read this config.

---

## 📊 Success Metrics

### Leading Indicators (Track Weekly)

| Metric | Target | Measurement |
|--------|--------|-------------|
| Checklist completion rate | >90% | PRs with both checklists / Total PRs |
| Average time to complete checklist | <10 min | Developer self-report or time tracking |
| Stage alignment violations detected | Decreasing trend | CI/CD validation failures |
| Orphaned code detected | 0 | Automated scan results |

### Lagging Indicators (Track Monthly)

| Metric | Baseline (Sprint 128-129) | Target (Sprint 135+) |
|--------|---------------------------|----------------------|
| "Spec drift" incidents | 1 per sprint (major) | 0 per sprint |
| Rework due to misalignment | 20% of sprint time | <5% of sprint time |
| Late-stage requirement changes | 3-5 per sprint | <1 per sprint |
| Developer satisfaction | Baseline survey | +20% improvement |

### ROI Calculation

**Time Investment**:
- Setup: 1 hour (LITE/STANDARD) to 1 week (ENTERPRISE)
- Per PR overhead: 10-20 minutes (checklists)

**Time Savings**:
- Prevented rework: 4-8 hours per incident (Sprint 128-129 = 16 hours wasted)
- Faster code review: 30% reduction (clearer context from checklists)
- Reduced late-stage changes: 2-4 hours per sprint

**Break-Even**: 1-2 sprints (after setup costs recovered)

---

## 🎓 Best Practices

### 1. Start Small, Scale Gradually

**Anti-Pattern**: ❌ Implement all validation automation on Day 1
**Best Practice**: ✅ Phase 1 → Manual checklists, Phase 2 → CLI, Phase 3 → CI/CD

### 2. Customize for Your Context

**Anti-Pattern**: ❌ Force SDLC directory structure on legacy project
**Best Practice**: ✅ Map your existing structure to SDLC stages

### 3. Make Checklists Actionable

**Anti-Pattern**: ❌ "Verify design is good" (vague)
**Best Practice**: ✅ "ADR-043 exists in docs/02-design/01-ADRs/ and references REQ-089" (specific)

### 4. Integrate with Existing Workflow

**Anti-Pattern**: ❌ Add separate "validation day" to sprint
**Best Practice**: ✅ Embed validation into PR process (already happens)

### 5. Use Tier-Appropriate Enforcement

**Anti-Pattern**: ❌ ENTERPRISE-level automation for 2-person LITE team
**Best Practice**: ✅ LITE → Manual, PROFESSIONAL → Recommended, ENTERPRISE → Automated

---

## 🔗 Related Resources

### Framework Documentation
- SPEC-0021: Stage Consistency Validation - Full specification (moved to Orchestrator `docs/05-test/`)
- [Stage Dependency Matrix](../02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md) - Stage prerequisites
- [SDLC-Stage-Lifecycle-Framework.md](../02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md) - Exit criteria per stage
- [SDLC-Sprint-Governance.md](../02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md) - 24-hour documentation rule

### Related Specifications
- [SPEC-0005: Validation Pipeline Interface](../05-Templates-Tools/01-Specification-Standard/SPEC-0005-Validation-Pipeline-Interface.md) - Retry logic, timeouts

### Implementation Examples
- [SPRINT-134-COMPLETION-SUMMARY.md](/docs/04-build/02-Sprint-Plans/SPRINT-134-COMPLETION-SUMMARY.md) - Real-world usage Sprint 128-129
- [test-fixing skill](/home/nqh/shared/skills/test-fixing/SKILL.md) - Stage consistency in test-fix workflow

---

## 📞 Support & Feedback

### Getting Help

**Documentation Issues**:
- File issue: [SDLC Framework GitHub Issues](https://github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework/issues)
- Tag: `stage-consistency`, `implementation-guide`

**Implementation Questions**:
- Slack: #sdlc-framework (internal teams)
- Email: sdlc-support@mtsolution.com.vn

**Feature Requests**:
- Submit to CTO Office via `SPEC_DELTA.md` template
- Include use case and tier requirements

### Contribution

Found a better validation pattern? Share it!

1. Document your pattern in [09-Continuous-Improvement/](../09-Continuous-Improvement/)
2. Submit PR with example implementation
3. CTO Office will review for Framework inclusion

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: February 1, 2026
**Framework Version**: SDLC 6.3.1
**Specification**: SPEC-0021 v1.0.0

---

*Stage Consistency Validation prevents "spec drift" where implementation diverges from approved designs. This guide provides tier-specific implementation paths from manual checklists (LITE) to automated CI/CD validation (ENTERPRISE).*
