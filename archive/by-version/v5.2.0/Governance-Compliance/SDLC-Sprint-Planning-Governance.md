# SDLC Sprint Planning Governance

**Version**: 5.3.0
**Date**: January 27, 2026
**Stage**: 02 - Core Methodology (Governance & Compliance)
**Pillar**: 2 - Sprint Planning Governance (Core Pillar)
**Status**: ACTIVE - Production Standard
**Authority**: CTO Office
**Industry Standards**: SAFe, Scrum Guide, ITIL 4
**Incident Reference**: BFlow Sprint 86 Direction Confusion (January 2025)

---

## Purpose

Define **governance processes for sprint planning** to prevent direction confusion, ensure documentation consistency, and maintain roadmap alignment. This document addresses gaps in SDLC 5.1.2 identified through the BFlow Platform incident analysis.

**Key Problem Solved**: Sprint templates existed (SPRINT-TEMPLATE.md) but no governance processes to:
- Approve sprint plans before execution
- Enforce post-sprint documentation updates
- Control roadmap changes
- Validate sprint consistency across documents

---

## Scope

This governance framework operates **PARALLEL** to feature lifecycle gates (G0-G3):

| Track | Gates | Purpose |
|-------|-------|---------|
| **Feature Lifecycle** | G0.1, G0.2, G1, G2, G3 | Quality gates for feature development |
| **Sprint Governance** | G-Sprint, G-Sprint-Close | Process gates for sprint management |

Sprint Governance Gates are **NOT** sequential with G0-G3. A sprint may contain work from multiple features at different G-levels.

---

## The 10 Golden Rules

### Rule 1: Sprint Numbers Are Immutable

```yaml
Principle:
  - Once assigned in roadmap, sprint numbers NEVER change
  - Sprint numbers are sequential within a project
  - Cancelled sprints keep their number (marked CANCELLED, not reused)

Exceptions (require CTO approval):
  - Sprint merge: Create new number (e.g., Sprint 86+87 → Sprint 88)
  - Sprint split: Use suffix (e.g., Sprint 86 → Sprint 86A, 86B)
  - Sprint cancel: Mark as CANCELLED, next sprint uses next number

Example:
  ❌ Wrong: Sprint 87-90 renamed to Sprint 83-86
  ✅ Correct: Sprint 83-86 completed, Sprint 87-90 is next
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

See: SDLC-Change-Management-Standard.md → Roadmap Change section
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

See: Section 8 for implementation details
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
      └── Sprint 87 Goal: "Implement F&B vertical"
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
  ❌ "Sprint 86 Options: Mobile OR Analytics OR CGF Prep"
  ✅ "Sprint 86: CGF V2.2 Preparation (P0), Analytics (P2 if capacity)"

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

## Sprint Governance Gates

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

---

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

## Roadmap Change Request Process

### When to Use

Use Roadmap Change Request for:
- Sprint renumbering
- Phase objective changes
- Roadmap goal additions/removals
- Strategic priority changes
- Timeline shifts >1 week

### Template

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

### Approval Matrix

| Change Type | Lead Time | Approver |
|-------------|-----------|----------|
| Sprint Renumbering | 24-48h | CTO or PM |
| Phase Changes | 48-72h | CPO or CTO |
| Roadmap Goal Changes | 1 week | CEO or CPO |
| Strategic Priority | 24-48h | CEO |

---

## Sprint Numbering Conventions

### Standard Numbering

```yaml
Format: Sprint [N]
  - N = Sequential integer starting from 1
  - N increments by 1 for each new sprint
  - N never repeats within a project

Examples:
  Sprint 1, Sprint 2, ..., Sprint 86, Sprint 87

Multi-Sprint Features:
  - Use range: "Sprint 87-90" means Sprints 87, 88, 89, 90
  - Each sprint in range is still individual
```

### Exception Handling

```yaml
Sprint Cancellation:
  - Mark as CANCELLED (do not reuse number)
  - Document reason in sprint file
  - Next sprint uses next sequential number
  
  Example:
    Sprint 86: CANCELLED (team restructure)
    Sprint 87: Next active sprint

Sprint Merge:
  - Requires CTO approval
  - Create new sprint number for merged work
  - Original sprints marked MERGED
  
  Example:
    Sprint 86: MERGED into Sprint 88
    Sprint 87: MERGED into Sprint 88
    Sprint 88: Combined scope

Sprint Split:
  - Use letter suffix
  - Document reason
  
  Example:
    Sprint 86A: Frontend work
    Sprint 86B: Backend work
    Sprint 87: Next full sprint
```

### Naming Conventions

```yaml
Sprint Name Format: "Sprint [N]: [Goal Summary]"

Examples:
  Sprint 86: CGF V2.2 Preparation
  Sprint 87-90: CGF V2.2 Multi-Industry Implementation
  Sprint 91: Performance Optimization

File Naming:
  - SPRINT-86-CGF-PREP.md
  - SPRINT-87-90-CGF-V2-MULTI-INDUSTRY.md
  - SPRINT-91-PERFORMANCE-OPT.md
```

---

## SSOT Validation Implementation

### Validation Script

```bash
#!/bin/bash
# tools/validate-sprint-consistency.sh
# SDLC 5.1.3 - Sprint Consistency Validator

set -e

echo "🔍 SDLC 5.1.3 Sprint Consistency Validator"
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

# Check for duplicate sprint numbers with different content
# (This is a simplified check - production would be more thorough)

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

## Tier Requirements Matrix

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

## Metrics & Monitoring

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

## Implementation Checklist

### For New Projects

```yaml
Setup (One-time):
  □ Create ROADMAP-TEMPLATE.md from framework
  □ Create SPRINT-TEMPLATE.md from framework
  □ Setup CURRENT-SPRINT.md
  □ Configure CI/CD for SSOT validation
  □ Schedule weekly roadmap review (PROFESSIONAL+)
  □ Define sprint approval authority

Per Sprint:
  □ Pass G-Sprint before kickoff
  □ Daily standup updates
  □ Pass G-Sprint-Close within 24h of completion
  □ Update all documentation
```

### For Existing Projects (Migration)

```yaml
Assessment:
  □ Identify current sprint number
  □ Check documentation freshness
  □ Assess roadmap consistency

Migration:
  □ Update CURRENT-SPRINT.md to latest format
  □ Run SSOT validation (fix any issues)
  □ Establish weekly review cadence
  □ Conduct first G-Sprint for next sprint

Validation:
  □ One successful sprint cycle with governance
  □ Team trained on process
  □ Metrics baseline established
```

---

## References

- [SDLC-Quality-Gates.md](./SDLC-Quality-Gates.md) - Feature lifecycle gates
- [SDLC-Change-Management-Standard.md](./SDLC-Change-Management-Standard.md) - Change control
- [SPRINT-TEMPLATE.md](../../05-Templates-Tools/5-Project-Templates/PLANNING-HIERARCHY-TEMPLATE/SPRINT-TEMPLATE.md) - Sprint documentation template
- [ROADMAP-TEMPLATE.md](../../05-Templates-Tools/5-Project-Templates/PLANNING-HIERARCHY-TEMPLATE/ROADMAP-TEMPLATE.md) - Roadmap template
- BFlow Gap Analysis (January 18, 2026) - Incident that drove this governance

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 5.1.3 | Jan 18, 2026 | Initial release - Sprint Planning Governance |

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for PROFESSIONAL+ tiers
**Last Updated**: January 18, 2026
**Owner**: CTO Office
**Approved By**: CTO
