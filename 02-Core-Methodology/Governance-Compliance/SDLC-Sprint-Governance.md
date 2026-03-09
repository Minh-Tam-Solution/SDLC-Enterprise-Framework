# SDLC Sprint Governance

**Version**: 6.1.2
**Date**: January 28, 2026
**Stage**: 02 - Core Methodology (Governance & Compliance)
**Pillar**: 2 - Sprint Planning Governance (Core Pillar)
**Status**: ACTIVE - Production Standard
**Authority**: CTO Office
**Industry Standards**: SAFe, Scrum Guide, ITIL 4
**Related**: [SDLC-Quality-Security-Gates.md](./SDLC-Quality-Security-Gates.md), [SDLC-Stage-Exit-Criteria.md](../SDLC-Stage-Exit-Criteria.md)

---

## Purpose

This document defines comprehensive **sprint governance** including:
- **10 Golden Rules** for sprint planning governance
- **Sprint Governance Gates** (G-Sprint, G-Sprint-Close)
- **Stage × Sprint Integration** for multi-stage sprints
- **Change Management** processes for roadmap changes

**Key Problem Solved**: Sprint templates existed but no governance processes for approval, documentation enforcement, roadmap changes, or stage integration.

---

## Part 1: The 10 Golden Rules

### Rule 1: Sprint Numbers Are Immutable

```yaml
Principle:
  - Once assigned in roadmap, sprint numbers NEVER change
  - Sprint numbers are sequential within a project
  - Cancelled sprints keep their number (marked CANCELLED, not reused)

Exceptions (require CTO approval):
  - Sprint merge: Create new number (e.g., Sprint N+N+1 → Sprint N+2)
  - Sprint split: Use suffix (e.g., Sprint N → Sprint NA, NB)
  - Sprint cancel: Mark as CANCELLED, next sprint uses next number

Example:
  ❌ Wrong: Later sprints renamed to fill gaps in numbering
  ✅ Correct: Completed sprints keep their numbers, next sprint uses next sequential number
```

### Rule 2: Post-Sprint Documentation Within 24 Business Hours

```yaml
Requirement:
  - Sprint completion triggers MANDATORY documentation updates
  - Deadline: 24 business hours (excludes weekends, holidays)
  - Blocking: New sprint CANNOT start until documentation complete

Documents to Update:
  1. CURRENT-SPRINT.md (status: COMPLETED)
  2. SPRINT-INDEX.md (add entry)
  3. Roadmap files (if sprint numbering affected)
  4. CHANGELOG.md (version bump if applicable)

Enforcement:
  - LITE: Optional (recommended)
  - STANDARD: Recommended (tracked)
  - PROFESSIONAL: Mandatory (blocks next sprint)
  - ENTERPRISE: Mandatory (audited)

Grace Period:
  - Sprint ends Friday 5pm → Deadline Monday 5pm
  - Sprint ends mid-week → 24h from completion
```

### Rule 3: Sprint Planning Requires Approval

```yaml
Approval Matrix by Tier:

LITE (1-2 people):
  - Self-approval
  - No formal process required

STANDARD (3-10 people):
  - Tech Lead approval
  - Approval via PR comment or Slack ack

PROFESSIONAL (10-50 people):
  - CTO or PM approval required
  - Sprint plan document must exist
  - G-Sprint gate must pass

ENTERPRISE (50+ people):
  - CPO + CTO approval required
  - Formal sprint planning meeting
  - G-Sprint gate must pass
  - Capacity signed off by all leads
```

### Rule 4: Weekly Roadmap Review (PROFESSIONAL+)

```yaml
Schedule:
  Day: Monday
  Time: 10:00 AM (local time)
  Duration: 15-30 minutes

Attendees:
  Required: CTO, PM, Tech Lead(s)
  Optional: CPO (for strategic decisions)

Agenda:
  1. Sprint progress vs plan (5 min)
  2. Roadmap alignment check (5 min)
  3. Next sprint preview (5 min)
  4. Blockers & decisions (5-15 min)

Output:
  - Meeting notes in shared doc
  - Action items assigned
  - Roadmap updates (if any)

Tier Requirements:
  - LITE: Not required
  - STANDARD: Monthly (recommended)
  - PROFESSIONAL: Weekly (mandatory)
  - ENTERPRISE: Weekly + daily standups
```

### Rule 5: Roadmap Changes Use Change Management

```yaml
Roadmap Change Types:

Sprint Renumbering:
  - Definition: Changing sprint numbers in roadmap
  - Approval: CTO or PM
  - Lead Time: 24-48 hours
  - Process: Normal Change

Phase Changes:
  - Definition: Modifying phase objectives or dates
  - Approval: CPO or CTO
  - Lead Time: 48-72 hours
  - Process: Normal Change

Roadmap Goal Changes:
  - Definition: Adding/removing/changing strategic goals
  - Approval: CEO or CPO
  - Lead Time: 1 week
  - Process: Normal Change with executive review

Strategic Priority Changes:
  - Definition: Changing P0/P1/P2 priorities
  - Approval: CEO
  - Lead Time: 24-48 hours
  - Process: Emergency or Normal Change

See: Part 6 - Change Management for full details
```

### Rule 6: Single Source of Truth (SSOT) Validation

```yaml
Principle:
  - All roadmap documents must have consistent sprint references
  - CI/CD validates consistency before merge
  - Inconsistency blocks deployment

Documents Requiring Consistency:
  - CURRENT-SPRINT.md
  - ROADMAP-*.md files
  - PROJECT-IMPLEMENTATION-PLAN.md
  - SPRINT-*-PLAN.md files

Validation Script:
  - Location: tools/validate-sprint-consistency.sh
  - Trigger: Pre-commit hook, CI pipeline
  - Output: Pass/Fail with specific conflicts

See: Part 5 for implementation details
```

### Rule 7: Sprint Goal Must Align with Roadmap Phase

```yaml
Traceability Chain:
  Roadmap Goal → Phase Objective → Sprint Goal → Backlog Items

Validation:
  - Every sprint goal traces to a Phase objective
  - Every Phase objective traces to a Roadmap goal
  - Traceability validated before sprint starts (G-Sprint)

Example:
  Roadmap Goal: "Launch CGF V2.2 by March 2026"
  └── Phase 4 Objective: "Complete Multi-Industry Support"
      └── Sprint N Goal: "Implement F&B vertical"
          └── Backlog: User stories, tasks, bugs

Validation Question:
  "How does this sprint goal contribute to roadmap goals?"
  If unclear → Sprint goal needs refinement
```

### Rule 8: Strategic Priorities Explicit (Not "Options")

```yaml
Priority Definitions:

P0 (CORE / Must Have):
  - Must be in every sprint plan
  - Cannot be deferred without CEO approval
  - Example: CGF V2.2 Multi-Industry

P1 (Important / Should Have):
  - Should be in sprint if capacity allows
  - Can be deferred with CTO approval
  - Example: Performance optimization

P2 (Nice-to-Have / Could Have):
  - Only if P0/P1 complete
  - Can be deferred freely
  - Example: UI polish, analytics

Anti-Pattern:
  ❌ "Sprint N Options: Mobile OR Analytics OR Feature Prep"
  ✅ "Sprint N: Feature Preparation (P0), Analytics (P2 if capacity)"

Enforcement:
  - Sprint plan must list priorities explicitly
  - P0 items cannot be listed as "options"
  - G-Sprint validates priority clarity
```

### Rule 9: Documentation Freeze = Sprint Freeze

```yaml
Principle:
  - If documentation is not up-to-date, new sprint cannot start
  - Forces disciplined sprint closure
  - Prevents documentation debt accumulation

Freeze Conditions:
  - CURRENT-SPRINT.md shows stale sprint (>24h post-completion)
  - Roadmap has inconsistent sprint references
  - Previous sprint retro not documented

Unfreeze Process:
  1. Complete all pending documentation
  2. Pass G-Sprint-Close for previous sprint
  3. CTO or PM confirms documentation complete
  4. New sprint can begin

Exceptions:
  - P0 emergency (CEO approval required)
  - Must document within 48h post-emergency
```

### Rule 10: Quarterly Roadmap Re-Approval

```yaml
Cadence: Every quarter (Q1, Q2, Q3, Q4)
Timing: First week of quarter

Re-Approval Required If:
  - >20% change from previous quarter's plan
  - New P0 priorities added
  - Major timeline shifts (>1 month)
  - Budget changes >10%

Re-Approval Authority:
  - LITE/STANDARD: CTO
  - PROFESSIONAL: CPO + CTO
  - ENTERPRISE: CEO + CPO + CTO

Process:
  1. PM prepares quarterly roadmap review
  2. Compare actual vs planned
  3. Present variance analysis
  4. Get explicit approval for next quarter
  5. Document in ROADMAP-QUARTERLY-REVIEW.md
```

---

## Part 2: Sprint Governance Gates

Sprint governance gates operate **PARALLEL** to feature lifecycle gates (G0-G3):

| Track | Gates | Purpose |
|-------|-------|---------|
| **Feature Lifecycle** | G0.1, G0.2, G1, G2, G3 | Quality gates for feature development |
| **Sprint Governance** | G-Sprint, G-Sprint-Close | Process gates for sprint management |

Sprint Governance Gates are **NOT** sequential with G0-G3. A sprint may contain work from multiple features at different G-levels.

### G-Sprint (Sprint Planning Gate)

**Purpose**: Validate sprint plan before execution begins.

**Trigger**: Before sprint kickoff meeting.

**Entry Criteria**:
```yaml
Required Before G-Sprint:
  □ Previous sprint documented (G-Sprint-Close passed)
  □ Roadmap up-to-date (SSOT validation passed)
  □ Sprint plan document created (SPRINT-XX.md)
  □ Sprint goal defined (single sentence)
  □ Backlog items prioritized (P0/P1/P2)
  □ Dependencies identified
```

**Evaluation Checklist**:
```yaml
G-Sprint Checklist:

Alignment:
  □ Sprint goal aligns with Phase objective
  □ Sprint goal aligns with Roadmap goal
  □ Priorities explicit (P0/P1/P2 labeled)
  □ No "options" for P0 items

Capacity:
  □ Team capacity calculated
  □ Story points within velocity
  □ Key personnel availability confirmed
  □ PTO/holidays accounted for

Dependencies:
  □ External dependencies identified
  □ Blocker mitigation planned
  □ Cross-team coordination scheduled

Risk:
  □ Top 3 risks identified
  □ Mitigation strategies defined
  □ Escalation path clear

Documentation:
  □ SPRINT-XX.md created
  □ Definition of Done agreed
  □ Sprint events scheduled
```

**Exit Criteria**:
```yaml
G-Sprint Passed When:
  □ All checklist items verified
  □ Approved by authority (tier-dependent)
  □ Sprint plan committed to repo
  □ Team kickoff scheduled
  □ Sprint status set to ACTIVE
```

**Approval Authority**:
| Tier | Approver | Method |
|------|----------|--------|
| LITE | Self | Git commit |
| STANDARD | Tech Lead | PR approval |
| PROFESSIONAL | CTO or PM | Meeting + document sign-off |
| ENTERPRISE | CPO + CTO | Formal meeting + audit trail |

### G-Sprint-Close (Sprint Completion Gate)

**Purpose**: Ensure proper sprint closure before next sprint begins.

**Trigger**: Sprint end date reached OR all committed work complete.

**Entry Criteria**:
```yaml
Required Before G-Sprint-Close:
  □ Sprint end date reached or work complete
  □ Sprint retro conducted
  □ Metrics captured
```

**Evaluation Checklist**:
```yaml
G-Sprint-Close Checklist:

Work:
  □ All committed work done OR explicitly carried over
  □ Carryover items documented with reason
  □ No silent drops (all items accounted for)

Quality:
  □ Definition of Done met for completed items
  □ No P0 bugs shipped
  □ Test coverage maintained

Retrospective:
  □ Sprint retro completed
  □ Action items assigned
  □ Improvements documented

Metrics:
  □ Velocity calculated
  □ Completion rate recorded
  □ Bug escape rate recorded

Documentation:
  □ CURRENT-SPRINT.md updated (within 24h)
  □ SPRINT-INDEX.md updated
  □ Roadmap reviewed (update if needed)
  □ CHANGELOG.md updated (if release)
```

**Exit Criteria**:
```yaml
G-Sprint-Close Passed When:
  □ All checklist items verified
  □ Documentation updated within 24 business hours
  □ Approved by authority (tier-dependent)
  □ Sprint status set to COMPLETED
  □ Next sprint can begin
```

**Time Limit**: 24 business hours after sprint end date.

**Failure Consequence**:
- New sprint BLOCKED until G-Sprint-Close passes
- Escalation to CTO if >48h delay
- Pattern of failure triggers process review

---

## Part 3: Stage × Sprint Integration

### Multi-Stage Sprint Scenarios

**Scenario 1: Sprint Spans Multiple Stages**

Example: Multi-Stage Sprint (App Builder Integration)
- **Stages Affected**: 02-DESIGN, 03-INTEGRATE, 04-BUILD
- **Duration**: 4 days (Day 0-3)
- **Challenge**: Must track stage transitions within sprint

**Example Timeline**:

| Day | Stage | Deliverable | Gate |
|-----|-------|-------------|------|
| **Day 0** | 02-DESIGN | Architecture decisions | G2 (Architecture) |
| **Day 1** | 03-INTEGRATE | TemplateBlueprint schema | G2 (Integration) |
| **Day 1-2** | 04-BUILD | 5 templates (4,811 LOC) | G3 (Code) |
| **Day 2** | 04-BUILD | AppBuilderProvider, tests (1,088 LOC) | G3 (Code) |
| **Day 3** | 04-BUILD | Intent Router, E2E tests (552 LOC) | G3 (Code) |

**Documentation Requirements**:

```yaml
SPRINT-NNN.md:
  metadata:
    stages_affected: [02-DESIGN, 03-INTEGRATE, 04-BUILD]
    primary_stage: 04-BUILD
    stage_transitions:
      - from: 02-DESIGN
        to: 03-INTEGRATE
        gate: G2
        date: 2026-01-27
        exit_criteria_met: true
      - from: 03-INTEGRATE
        to: 04-BUILD
        gate: G2
        date: 2026-01-27
        exit_criteria_met: true
```

**G-Sprint Gates for Multi-Stage Sprint**:

**G-Sprint-Start** (Before sprint begins):
- ✅ Verify all prerequisite stages complete
- ✅ Verify current stage entry criteria met
- ✅ Identify stage transition points in sprint plan
- ✅ Document expected stage transitions

**G-Sprint-Close** (After sprint ends):
- ✅ Verify each stage exit criteria met
- ✅ Update all affected stage folders
- ✅ Document stage transitions in CURRENT-SPRINT.md
- ✅ Commit evidence artifacts to Evidence Vault

**Scenario 2: Sprint Entirely Within One Stage**

Example: Single-Stage Sprint (Quality Pipeline Enhancement)
- **Stage**: 04-BUILD (entire sprint)
- **Challenge**: None (simple scenario)

```yaml
SPRINT-NNN.md:
  metadata:
    stages_affected: [04-BUILD]
    primary_stage: 04-BUILD
    stage_transitions: []  # No transitions
```

**Scenario 3: Sprint Starts Mid-Stage**

Example: Continuation Sprint (Quality Gates Integration)
- **Stage**: 04-BUILD (already in progress)
- **Previous Sprint**: Previous sprint completed Stage 04 partially
- **Challenge**: Track stage continuation, not stage entry

```yaml
SPRINT-NNN.md:
  metadata:
    stages_affected: [04-BUILD]
    primary_stage: 04-BUILD
    stage_status: IN_PROGRESS
    previous_sprint: SPRINT-{N-1}

  stage_continuation:
    stage_04:
      entry_date: {date of previous sprint}
      continuation_date: {date of current sprint}
      progress: 60%
      remaining: Quality Gates integration
```

### Stage-Specific Sprint Responsibilities

| Stage | Sprint Work | Documentation Location | Typical Sprints |
|-------|-------------|------------------------|-----------------|
| **00-FOUNDATION** | Design Thinking workshops, user research | `docs/00-foundation/` | 1-2 |
| **01-PLANNING** | Requirements, API design, user stories | `docs/01-planning/` | 1-2 |
| **02-DESIGN** | Architecture, ADRs, design reviews | `docs/02-design/` | 1-2 |
| **03-INTEGRATE** | API contracts, integration design | `docs/03-integrate/` | 0-1 |
| **04-BUILD** | Feature development, unit testing | `docs/04-build/02-Sprint-Plans/` | 2-10 |
| **05-TEST** | Integration/E2E testing, bug fixing | `docs/05-test/` | 1-2 |
| **06-DEPLOY** | Deployment automation, rollout | `docs/06-deploy/` | 0.5-1 |
| **07-OPERATE** | Monitoring, incident response | `docs/07-operate/` | 1 + ongoing |
| **08-COLLABORATE** | Code reviews, knowledge sharing | `docs/08-collaborate/` | Ongoing |
| **09-GOVERN** | Audits, compliance reviews | `docs/09-govern/` | 1-2 + ongoing |

### Rollback Procedure (Stage Exit Criteria Not Met)

**Step 1: Identify Failed Criteria**
```yaml
sprint: 107
status: PARTIAL COMPLETE
stage: 04-BUILD
failed_criteria:
  - "Code coverage < 60% (actual: 45%)"
  - "Missing code review approval"
```

**Step 2: Mark Sprint as Partial**
```yaml
# CURRENT-SPRINT.md
status: PARTIAL COMPLETE (80% done)
next_sprint: SPRINT-107.1 (cleanup sprint)
blocked_stages: [05-TEST]
```

**Step 3: Create Follow-Up Sprint**
```yaml
# SPRINT-107.1.md
type: CLEANUP_SPRINT
duration: 1-2 days
goal: Complete Stage 04 exit criteria
tasks:
  - Increase code coverage to 60%
  - Get code review approval
  - Re-run G-Sprint-Close
```

**Step 4: Re-Run G-Sprint-Close**
- After follow-up sprint completes
- Verify all exit criteria now met
- Mark sprint as COMPLETE
- Unblock next stage

---

## Part 4: Tier Requirements Matrix

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| G-Sprint Gate | Optional | Recommended | **Mandatory** | **Mandatory** |
| G-Sprint-Close Gate | Optional | Recommended | **Mandatory** | **Mandatory** |
| 24h Documentation | Optional | Recommended | **Mandatory** | **Mandatory** |
| Weekly Roadmap Review | Not required | Monthly | **Weekly** | **Weekly** |
| Roadmap Change Request | Git commit | PR | **Formal RCR** | **Formal RCR** |
| SSOT Validation | Optional | CI warning | **CI blocking** | **CI blocking** |
| Sprint Approval | Self | Tech Lead | **CTO/PM** | **CPO+CTO** |
| Quarterly Re-Approval | Not required | CTO | **CPO+CTO** | **CEO+CPO+CTO** |

---

## Part 5: SSOT Validation Implementation

### Validation Script

```bash
#!/bin/bash
# tools/validate-sprint-consistency.sh
# SDLC 6.1.2 - Sprint Consistency Validator

set -e

echo "🔍 SDLC 6.1.2 Sprint Consistency Validator"
echo "==========================================="

# Configuration
DOCS_DIR="${1:-docs}"
ERRORS=0

# Extract sprint references from key documents
extract_sprints() {
    local file="$1"
    if [ -f "$file" ]; then
        grep -oP "Sprint \K[0-9]+(-[0-9]+)?" "$file" 2>/dev/null | sort -u
    fi
}

# Check for CURRENT-SPRINT.md
if [ -f "$DOCS_DIR/CURRENT-SPRINT.md" ]; then
    CURRENT_SPRINT=$(grep -oP "Sprint Number:\s*\K[0-9]+" "$DOCS_DIR/CURRENT-SPRINT.md" 2>/dev/null || echo "")
    echo "📋 Current Sprint: $CURRENT_SPRINT"
else
    echo "⚠️  CURRENT-SPRINT.md not found"
fi

# Find all roadmap files
echo ""
echo "📊 Checking roadmap files..."
ROADMAP_FILES=$(find "$DOCS_DIR" -name "*ROADMAP*.md" -o -name "*roadmap*.md" 2>/dev/null)

for file in $ROADMAP_FILES; do
    sprints=$(extract_sprints "$file")
    if [ -n "$sprints" ]; then
        echo "  📄 $file: $sprints"
    fi
done

# Find all sprint plan files
echo ""
echo "📝 Checking sprint plan files..."
SPRINT_FILES=$(find "$DOCS_DIR" -name "SPRINT-*.md" -o -name "Sprint-*.md" 2>/dev/null)

for file in $SPRINT_FILES; do
    sprint_num=$(basename "$file" | grep -oP "[0-9]+(-[0-9]+)?" | head -1)
    if [ -n "$sprint_num" ]; then
        echo "  📄 $file: Sprint $sprint_num"
    fi
done

# Validate no conflicts
echo ""
echo "🔎 Validating consistency..."

# Check CURRENT-SPRINT matches a sprint plan
if [ -n "$CURRENT_SPRINT" ]; then
    if ! find "$DOCS_DIR" -name "*SPRINT*$CURRENT_SPRINT*" | grep -q .; then
        echo "❌ ERROR: Current sprint $CURRENT_SPRINT has no matching plan file"
        ERRORS=$((ERRORS + 1))
    fi
fi

# Final result
echo ""
if [ $ERRORS -eq 0 ]; then
    echo "✅ Sprint Consistency Validation PASSED"
    exit 0
else
    echo "❌ Sprint Consistency Validation FAILED ($ERRORS errors)"
    exit 1
fi
```

### CI/CD Integration

```yaml
# .github/workflows/validate-docs.yml
name: Validate Documentation

on:
  pull_request:
    paths:
      - 'docs/**'
      - '*.md'

jobs:
  sprint-consistency:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Validate Sprint Consistency
        run: |
          chmod +x tools/validate-sprint-consistency.sh
          ./tools/validate-sprint-consistency.sh docs/

  doc-links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check Markdown Links
        uses: gaurav-nelson/github-action-markdown-link-check@v1
        with:
          folder-path: 'docs/'
```

### Pre-commit Hook

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: sprint-consistency
        name: Validate Sprint Consistency
        entry: tools/validate-sprint-consistency.sh
        language: script
        files: '\.(md)$'
        pass_filenames: false
```

---

## Part 6: Change Management

### Change Types

#### Standard Change (Pre-Approved)

```yaml
Definition:
  - Low risk, well-understood changes
  - Follow documented procedure
  - Pre-approved by change authority

Examples:
  - Security patches (critical/high)
  - Dependency updates (minor versions)
  - Configuration changes (documented)
  - Scheduled maintenance

Approval: None required (pre-approved template)
Lead Time: Immediate to 24 hours
Documentation: Change log entry
```

#### Normal Change (Requires Approval)

```yaml
Definition:
  - Medium risk changes
  - Require assessment and approval
  - Follow standard change process

Examples:
  - New feature deployments
  - Major dependency updates
  - Infrastructure changes
  - Database schema changes

Approval: CAB or delegated authority
Lead Time: 24-72 hours
Documentation: Change request + review
```

#### Emergency Change (Expedited)

```yaml
Definition:
  - Urgent fix for production incident
  - Cannot wait for normal process
  - Higher risk accepted for speed

Examples:
  - P0 bug hotfix
  - Security vulnerability patch
  - Data corruption fix
  - Service outage recovery

Approval: Post-hoc CAB review (within 48h)
Lead Time: Immediate
Documentation: Incident + change record
```

#### Roadmap Change (Strategic Planning)

```yaml
Definition:
  - Changes to strategic planning documents
  - Requires impact assessment
  - Different approval authority than code changes

Examples:
  - Sprint renumbering
  - Phase objective change
  - Roadmap goal addition/removal
  - Strategic priority reordering

Approval Authority:
  - Sprint renumbering: CTO or PM
  - Phase changes: CPO or CTO
  - Roadmap goal changes: CEO or CPO
  - Strategic priority: CEO

Lead Time:
  - Sprint renumbering: 24-48 hours
  - Phase changes: 48-72 hours
  - Roadmap goal changes: 1 week
  - Emergency strategic: Immediate (CEO ratify within 24h)

Documentation: Roadmap Change Request (RCR)
```

### Roadmap Change Request Process

#### When to Use

Use Roadmap Change Request for:
- Sprint renumbering
- Phase objective changes
- Roadmap goal additions/removals
- Strategic priority changes
- Timeline shifts >1 week

#### RCR Template

```markdown
# Roadmap Change Request: [RCR-YYYY-NNN]

## Summary
| Field | Value |
|-------|-------|
| Change Type | Sprint Renumbering / Phase Change / Goal Change / Priority Change |
| Requested By | [Name] |
| Date | [YYYY-MM-DD] |
| Target Date | [YYYY-MM-DD] |
| Urgency | Normal / Urgent |

## Current State
**Affected Roadmap Section**:
[Describe current state]

**Issue/Reason for Change**:
[Why is this change needed?]

## Proposed Change
**New State**:
[Describe proposed state]

**Rationale**:
[Business/technical justification]

## Impact Assessment

### Affected Documents
| Document | Change Required |
|----------|-----------------|
| CURRENT-SPRINT.md | [Yes/No - describe] |
| ROADMAP-*.md | [Yes/No - describe] |
| PROJECT-IMPLEMENTATION-PLAN.md | [Yes/No - describe] |
| SPRINT-*-PLAN.md | [Yes/No - describe] |

### Affected Teams
| Team | Impact | Notification |
|------|--------|--------------|
| [Team name] | [Description] | [Yes/No] |

### Risk Level
- [ ] Low - Documentation only
- [ ] Medium - Timeline/scope change
- [ ] High - Strategic direction change

## Approval

| Role | Name | Decision | Date | Signature |
|------|------|----------|------|-----------|
| Requester | | Request | | |
| CTO | | Approve/Reject | | |
| CPO | | Approve/Reject (if required) | | |
| CEO | | Approve/Reject (if required) | | |

## Implementation Plan
1. [ ] Update document A
2. [ ] Update document B
3. [ ] Notify team X
4. [ ] Run SSOT validation
5. [ ] Commit changes

## Post-Change Validation
- [ ] SSOT validation passed
- [ ] All teams notified
- [ ] No consistency errors
```

### Risk Scoring Matrix

```yaml
Impact (1-5):
  1: No user impact
  2: Minor inconvenience, workaround exists
  3: Moderate impact, degraded service
  4: Major impact, feature unavailable
  5: Critical, service down

Likelihood (1-5):
  1: Very unlikely (<5%)
  2: Unlikely (5-20%)
  3: Possible (20-50%)
  4: Likely (50-80%)
  5: Very likely (>80%)

Risk Score = Impact × Likelihood

Risk Level:
  1-5: Low (Green) - Standard process
  6-12: Medium (Yellow) - Enhanced review
  13-25: High (Red) - CAB required
```

### Rollback Requirements

```yaml
When to Rollback:
  - Error rate increases >5% after deploy
  - Latency p95 increases >50%
  - Critical functionality broken
  - Security vulnerability introduced
  - Customer-reported P0 issues

Rollback Decision Authority:
  - On-call engineer: Can rollback immediately
  - No approval needed for automated rollback triggers

Before Deployment (PROFESSIONAL+):
  □ Rollback procedure documented
  □ Rollback tested in staging
  □ Database rollback tested (if applicable)
  □ Rollback time verified
```

---

## Part 7: Metrics & Monitoring

### Sprint Governance Metrics

```yaml
Track Weekly (PROFESSIONAL+):
  Sprint Planning:
    - G-Sprint pass rate (target: 100%)
    - Sprint planning time (target: <2h)
    - Approval turnaround (target: <24h)

  Sprint Closure:
    - G-Sprint-Close pass rate (target: 100%)
    - Documentation lag (target: <24h)
    - Carryover rate (target: <20%)

  Roadmap Alignment:
    - Sprint goal alignment rate (target: 100%)
    - Roadmap change frequency (track only)
    - SSOT validation failures (target: 0)

Track Monthly:
  - Sprint velocity trend
  - Predictability (planned vs actual)
  - Direction confusion incidents (target: 0)
```

### Escalation Triggers

```yaml
Immediate Escalation to CTO:
  - G-Sprint-Close >48h overdue
  - SSOT validation failing for >24h
  - Sprint started without G-Sprint approval
  - P0 priority changed without CEO approval

Weekly Escalation (in roadmap review):
  - Sprint goal misalignment detected
  - Carryover rate >30%
  - Documentation lag pattern (>2 sprints)
```

---

## Part 8: Sprint Planning Template

```markdown
# Sprint XXX: [Sprint Name]

**Status**: ACTIVE | COMPLETE | PARTIAL COMPLETE
**Duration**: X days
**Stages Affected**: [XX-STAGE, XX-STAGE]
**Primary Stage**: XX-STAGE

## Stage Tracking

### Stages Affected
- **XX-STAGE**: [Entry criteria met? | In progress | Complete]
- **XX-STAGE**: [Entry criteria met? | In progress | Complete]

### Stage Transitions (if multi-stage)
| From | To | Gate | Expected Date | Actual Date | Exit Criteria Met? |
|------|----|----|---------------|-------------|--------------------|
| XX | XX | GX | YYYY-MM-DD | YYYY-MM-DD | ✅ Yes / ❌ No |

## Work Breakdown by Stage

### Stage XX: [STAGE NAME]
**Work**:
- Task 1
- Task 2

**Deliverables**:
- Artifact 1 (location: docs/XX-stage/...)
- Artifact 2

**Exit Criteria Checklist**:
- [ ] Documentation complete
- [ ] Stakeholder signoff received
- [ ] Gate passed

## G-Sprint Gates

### G-Sprint-Start Checklist
- [ ] Prerequisite stages verified
- [ ] Entry criteria met for current stage(s)
- [ ] Stage transitions documented

### G-Sprint-Close Checklist
- [ ] All stage exit criteria met
- [ ] Documentation updated
- [ ] Evidence artifacts committed
- [ ] Sprint retrospective complete
```

---

## Related Documents

- [SDLC-Quality-Security-Gates.md](./SDLC-Quality-Security-Gates.md) - Feature gates (G0-G3)
- [SDLC-Stage-Exit-Criteria.md](../SDLC-Stage-Exit-Criteria.md) - Stage completion criteria
- [SDLC-Tier-Stage-Requirements.md](../Documentation-Standards/SDLC-Tier-Stage-Requirements.md) - Tier-specific guidance
- [SDLC-Observability-Checklist.md](./SDLC-Observability-Checklist.md) - Monitoring requirements
- [SPRINT-TEMPLATE.md](../../05-Templates-Tools/5-Project-Templates/PLANNING-HIERARCHY-TEMPLATE/SPRINT-TEMPLATE.md) - Sprint template

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 6.0.0 | Jan 28, 2026 | Folder flattening (remove layer 3), version upgrade |
| 5.3.0 | Jan 28, 2026 | Consolidated Sprint Planning + Stage-Sprint Integration + Change Management |
| 5.2.0 | Jan 22, 2026 | AI Governance integration |
| 5.1.3 | Jan 18, 2026 | Initial Sprint Planning Governance |

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for PROFESSIONAL+ tiers
**Version**: 6.1.2
**Last Updated**: January 28, 2026
**Owner**: CTO Office
