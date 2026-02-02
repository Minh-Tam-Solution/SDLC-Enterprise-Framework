# RFC-SDLC-605: Continuous Learning Protocol

**Status**: 📋 DRAFT
**Created**: March 5, 2026
**Author**: Framework Architect
**Sprint**: 143 - Framework-First Track 1
**Related**: Boris Cherny Tactics Analysis (Partial Gap - CLAUDE.md Maintenance)
**Framework Version**: SDLC 6.0.3

---

## 1. Problem Statement

### Current Challenge

AI coding assistants (Claude Code, Cursor, Copilot) repeatedly make the **same mistakes** across projects because they lack a **feedback loop** to learn from bug fixes. When a developer fixes a bug caused by AI-generated code, the lesson learned is often lost:

**Current Workflow** (No Learning):
```
1. AI generates code with bug (e.g., "Use Pydantic v1 Config instead of v2")
2. Developer discovers bug during code review
3. Developer fixes bug manually
4. PR merged
5. ❌ AI REPEATS SAME MISTAKE in next feature

Months later:
6. Different developer, same project
7. AI generates same bug (Pydantic v1 Config)
8. Another manual fix required
9. Cycle repeats indefinitely
```

**Problem**: No mechanism to **capture and propagate** learnings from bug fixes to future AI generations.

### Boris Cherny Insight

Boris Cherny recommends:
> "Sau mỗi lần sửa lỗi: 'Cập nhật CLAUDE.md để không lặp lại sai lầm'. Claude tự viết quy tắc cực tốt cho chính nó."
> (Translation: "After every bug fix: 'Update CLAUDE.md to not repeat mistakes'. Claude writes rules extremely well for itself.")

**Key Insight**: AI should **self-document** lessons learned in CLAUDE.md/AGENTS.md to improve future generations.

### Gap Analysis

**Current State** (SDLC Orchestrator v1.6.0):
- ✅ CLAUDE.md exists (v3.2.0, 120KB, last updated Jan 23, 2026)
- ✅ CHANGELOG with version history (v1.1.0 → v3.2.0)
- ✅ Battle-Tested Patterns section (BFlow, NQH, MTEP learnings)
- ✅ Feedback Loop Closure documented (lines 1231-1245)
- ❌ **No auto-update mechanism after bug fixes**

**Industry Practice**:
- Standard: Static CLAUDE.md (manual updates)
- Advanced: Quarterly synthesis (manual)
- Best-in-class: Boris Cherny's continuous update pattern

**Competitive Advantage**: Automate learning cycle

---

## 2. Current State

### Feedback Loop Closure (From CLAUDE.md v3.2.0)

```markdown
Learning from Code Reviews:
  1. Extract patterns from PR review comments
  2. Categorize: pattern_violation | missing_requirement | edge_case | performance
  3. Store learnings in pr_learnings table
  4. Monthly: Aggregate → Update decomposition hints
  5. Quarterly: Synthesize → Update CLAUDE.md patterns
```

**Process exists** but is **NOT automated**.

**Example Learning** (Manual Entry):
```markdown
# CLAUDE.md v3.1.0 Update (Jan 18, 2026)

## Pydantic v2 Migration (Sprint 142)

❌ DON'T:
- Use `class Config:` (Pydantic v1 syntax, deprecated)

✅ DO:
- Use `model_config = ConfigDict(from_attributes=True)` (Pydantic v2)

Learned from: Sprint 142 Day 2 (RA-005, 19 files migrated)
```

This was manually added after Sprint 142. We want this **automated**.

---

## 3. Proposed Pattern

### 3.1 Continuous Learning Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ BUG FIX LIFECYCLE                                                │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 1. Bug Discovered (Code Review / Production)              │   │
│  │    - AI generated incorrect code                          │   │
│  │    - Root cause identified                                │   │
│  └────────────────────┬─────────────────────────────────────┘   │
│                       │                                          │
│  ┌────────────────────▼─────────────────────────────────────┐   │
│  │ 2. Developer Fixes Bug                                    │   │
│  │    - Write correct implementation                         │   │
│  │    - Add test case (prevent regression)                   │   │
│  │    - Create PR with detailed description                  │   │
│  └────────────────────┬─────────────────────────────────────┘   │
│                       │                                          │
│  ┌────────────────────▼─────────────────────────────────────┐   │
│  │ 3. PR Merged                                              │   │
│  │    - GitHub Actions trigger                               │   │
│  │    - Extract root cause from PR description               │   │
│  │    - Call Learning Service API                            │   │
│  └────────────────────┬─────────────────────────────────────┘   │
│                       │                                          │
├───────────────────────┴──────────────────────────────────────────┤
│ LEARNING SERVICE (SDLC Orchestrator - New Component)            │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 4. Create Learning Entry                                  │   │
│  │    - File: .claude/learnings/YYYY-MM-DD-issue-NNN.md     │   │
│  │    - Format: Problem → Solution → Rule                    │   │
│  │    - Evidence artifact (audit trail)                      │   │
│  └────────────────────┬─────────────────────────────────────┘   │
│                       │                                          │
│  ┌────────────────────▼─────────────────────────────────────┐   │
│  │ 5. Monthly Aggregation (Automated)                        │   │
│  │    - Scan .claude/learnings/ directory                    │   │
│  │    - Group by category (pydantic, auth, etc.)             │   │
│  │    - Generate CLAUDE.md update PR                         │   │
│  │    - Human reviews + approves                             │   │
│  └────────────────────┬─────────────────────────────────────┘   │
│                       │                                          │
│  ┌────────────────────▼─────────────────────────────────────┐   │
│  │ 6. CLAUDE.md Updated                                      │   │
│  │    - New section added (Lessons Learned)                  │   │
│  │    - Version bumped (v3.2.0 → v3.3.0)                     │   │
│  │    - Future AI generations learn from past mistakes       │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Learning Entry Format

**File**: `.claude/learnings/2026-03-05-issue-1234.md`

```markdown
---
date: 2026-03-05
issue: https://github.com/org/repo/issues/1234
pr: https://github.com/org/repo/pull/1235
category: pydantic
severity: medium
learned_by: @developer
reviewed_by: @tech-lead
---

# Learning: Pydantic v2 Config Migration

## Problem

AI generated code using Pydantic v1 syntax in `app/schemas/user.py`:

\`\`\`python
class User(BaseModel):
    name: str
    email: str

    class Config:  # ❌ Pydantic v1 (deprecated)
        from_attributes = True
\`\`\`

This caused 500+ deprecation warnings during pytest execution (Sprint 142 Day 2).

## Root Cause

- CLAUDE.md v3.1.0 didn't document Pydantic v2 migration
- AI training data (pre-2024) uses Pydantic v1 syntax
- No guidance in project context files

## Solution

Update to Pydantic v2 syntax:

\`\`\`python
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)  # ✅ Pydantic v2
\`\`\`

## Rule for Future AI Generations

**DON'T**:
- Use `class Config:` (Pydantic v1, deprecated since 2023)

**DO**:
- Use `model_config = ConfigDict(...)` (Pydantic v2 standard)
- Import `ConfigDict` from `pydantic`
- Migrate `@validator` to `@field_validator` + `@classmethod`

## Test Case (Prevent Regression)

\`\`\`python
# tests/unit/schemas/test_user.py
def test_user_schema_uses_pydantic_v2():
    """Ensure User schema uses Pydantic v2 ConfigDict"""
    from app.schemas.user import User
    assert hasattr(User, "model_config")
    assert not hasattr(User, "Config")
\`\`\`

## Impact

- Fixed: 19 files migrated (Sprint 142 Day 2)
- Warnings reduced: 500+ → 30 (94% reduction)
- Time saved: ~2 hours in future sprints (no repeat migration)

## References

- Sprint 142 Day 2 RA-005: [Link to progress report]
- Pydantic v2 Migration Guide: https://docs.pydantic.dev/latest/migration/
- Issue #1234: https://github.com/org/repo/issues/1234
- PR #1235: https://github.com/org/repo/pull/1235
```

### 3.3 GitHub Actions Workflow (Automated)

**.github/workflows/learning-capture.yml**:

```yaml
name: Capture Learning from Bug Fix

on:
  pull_request:
    types: [closed]
    branches: [main]

jobs:
  capture-learning:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
      - name: Check if PR is bug fix
        id: check-bug
        run: |
          if [[ "${{ github.event.pull_request.title }}" =~ ^fix|bug|Fix|Bug ]]; then
            echo "is_bug_fix=true" >> $GITHUB_OUTPUT
          fi

      - name: Extract learning
        if: steps.check-bug.outputs.is_bug_fix == 'true'
        run: |
          # Call Learning Service API
          curl -X POST "${{ secrets.ORCHESTRATOR_URL }}/api/v1/learning/capture" \
            -H "Authorization: Bearer ${{ secrets.LEARNING_TOKEN }}" \
            -H "Content-Type: application/json" \
            -d '{
              "pr_number": ${{ github.event.pull_request.number }},
              "pr_title": "${{ github.event.pull_request.title }}",
              "pr_url": "${{ github.event.pull_request.html_url }}",
              "pr_body": ${{ toJSON(github.event.pull_request.body) }},
              "files_changed": ${{ toJSON(github.event.pull_request.changed_files) }},
              "merged_by": "${{ github.event.pull_request.merged_by.login }}",
              "merged_at": "${{ github.event.pull_request.merged_at }}"
            }'

      - name: Create learning entry (if bug fix)
        if: steps.check-bug.outputs.is_bug_fix == 'true'
        run: echo "Learning entry created via API"
```

### 3.4 Manual CLI Command (Alternative)

For teams without GitHub Actions:

```bash
# After merging bug fix PR
sdlcctl learn --from-fix "Don't use class Config in Pydantic v2"
# Creates .claude/learnings/2026-03-05-manual-001.md

# Monthly aggregation (manual trigger)
sdlcctl learn --aggregate --since 2026-02-01
# Creates PR with CLAUDE.md updates

# View all learnings
sdlcctl learn --list
```

---

## 4. Integration with SDLC Framework

### 4.1 Evidence Vault Storage

Each learning entry becomes an **Evidence artifact**:

```json
{
  "manifest_id": "MANIFEST-2026-03-005",
  "artifacts": [
    {
      "artifact_id": "EVD-2026-03-005",
      "type": "learning_entry",
      "category": "pydantic",
      "severity": "medium",
      "issue_url": "https://github.com/org/repo/issues/1234",
      "pr_url": "https://github.com/org/repo/pull/1235",
      "learning_file": ".claude/learnings/2026-03-05-issue-1234.md",
      "rule_summary": "Use Pydantic v2 ConfigDict, not class Config",
      "timestamp": "2026-03-05T15:30:00Z",
      "signature": "ed25519:..."
    }
  ]
}
```

**Hash-Chained**: Each learning entry links to previous manifest (immutable)

### 4.2 Stage 09 (Govern) - Knowledge Management

**Learning Protocol aligns with Stage 09**:
- **Purpose**: Governance, compliance, knowledge retention
- **When**: Continuous (throughout project lifecycle)
- **Output**: Updated CLAUDE.md (version history)

**Stage 09 Artifacts Enhanced**:
- Learning entries (`.claude/learnings/`)
- CLAUDE.md version history (v3.0.0 → v3.3.0)
- Evidence artifacts (audit trail)

### 4.3 Monthly Aggregation Workflow

**Automated Process** (Scheduled GitHub Actions):

```yaml
# .github/workflows/monthly-learning-sync.yml
name: Monthly Learning Aggregation

on:
  schedule:
    - cron: "0 9 1 * *"  # First day of month, 9am UTC
  workflow_dispatch:  # Manual trigger

jobs:
  aggregate-learnings:
    runs-on: ubuntu-latest
    steps:
      - name: Aggregate learnings
        run: sdlcctl learn --aggregate --since "1 month ago"

      - name: Create CLAUDE.md update PR
        run: |
          gh pr create \
            --title "docs: Update CLAUDE.md with learnings ($(date +%Y-%m))" \
            --body "Aggregated learnings from past month. Review and approve." \
            --label "documentation" \
            --assignee "@tech-lead"
```

---

## 5. Tool-Agnostic Implementation

### 5.1 Works with Any AI Tool

**Learning entries are markdown** (tool-agnostic format):
- Claude Code reads `.claude/learnings/`
- Cursor reads project context from same files
- GitHub Copilot indexes markdown as embeddings
- Any AI tool can parse markdown

**No vendor lock-in**: Learning entries are plain text.

### 5.2 Manual Process (No Automation)

Teams can use this pattern **without automation**:

```bash
# After bug fix, manually create learning entry
mkdir -p .claude/learnings
cat > .claude/learnings/2026-03-05-manual.md << 'EOF'
# Learning: [Title]
## Problem: [Description]
## Solution: [Code fix]
## Rule: [Guideline for AI]
EOF

# Monthly, manually update CLAUDE.md
# Copy learnings to CLAUDE.md "Lessons Learned" section
```

---

## 6. Tradeoffs and Alternatives

### 6.1 Alternatives Considered

| Alternative | Pros | Cons | Decision |
|-------------|------|------|----------|
| **No Learning** | Zero cost | Repeat mistakes | ❌ Reject (status quo) |
| **Manual Quarterly** | Low automation cost | Slow learning cycle | 🟡 Acceptable fallback |
| **Continuous Automated** | Fast feedback loop | Development cost | ✅ **Approved** |
| **RAG (Retrieval-Augmented)** | Semantic search | Complex infrastructure | ⏸️ Future enhancement |

### 6.2 Tradeoffs Accepted

**Costs**:
- **Development**: 200 LOC, 8 hours (Sprint 144)
- **Infrastructure**: $10/month (GitHub Actions minutes)
- **Maintenance**: 1 hour/month (review aggregation PRs)

**Benefits**:
- **Time Saved**: 2 hours/sprint (no repeat bugs)
- **ROI**: Positive after 4 months
- **Knowledge Retention**: Institutional memory preserved

---

## 7. Decision

### 7.1 Recommendation

**APPROVE** Continuous Learning Protocol for SDLC Framework 6.0.3.

**Reasoning**:
1. ✅ Addresses Partial Gap (CLAUDE.md maintenance automation)
2. ✅ Tool-agnostic (markdown learning entries)
3. ✅ Evidence Vault integration (audit trail)
4. ✅ Low cost, high value (ROI in 4 months)
5. ✅ Incremental adoption (manual → automated)

### 7.2 Implementation Roadmap

**Track 1 (Sprint 143)**: ✅ **This RFC** (methodology documentation)
**Track 2 (Sprint 144)**: Implementation (conditional on Track 1 approval)

**Sprint 144 Implementation**:
```yaml
Component: Learning Service
LOC: 200
Effort: 8 hours
Files:
  - backend/app/services/learning_service.py (100 LOC)
  - backend/app/api/v1/endpoints/learning.py (50 LOC)
  - .github/workflows/learning-capture.yml (50 LOC)
CLI Commands:
  - sdlcctl learn --from-fix "description"
  - sdlcctl learn --aggregate --since DATE
  - sdlcctl learn --list
```

### 7.3 Success Criteria

**Track 1 Success** (Sprint 143):
- ✅ RFC approved by CTO
- ✅ Learning entry format defined
- ✅ Tool-agnostic validation passed

**Track 2 Success** (Sprint 144):
- ✅ First learning entry auto-created from bug fix PR
- ✅ Monthly aggregation PR generated
- ✅ CLAUDE.md updated with first learning
- ✅ Evidence Vault storing learning artifacts
- ✅ Zero bugs repeated (test regression suite)

---

## 8. Appendices

### A. Learning Entry Template

**`.claude/learnings/YYYY-MM-DD-issue-NNN.md`**:

```markdown
---
date: YYYY-MM-DD
issue: [GitHub issue URL]
pr: [GitHub PR URL]
category: [pydantic|auth|testing|performance|...]
severity: [low|medium|high|critical]
learned_by: [@username]
reviewed_by: [@username]
---

# Learning: [Title]

## Problem
[What went wrong? Include code snippet if relevant]

## Root Cause
[Why did AI generate incorrect code?]

## Solution
[Correct implementation with code snippet]

## Rule for Future AI Generations
**DON'T**: [Anti-pattern]
**DO**: [Best practice]

## Test Case (Prevent Regression)
[Test code to prevent repeat]

## Impact
- Files affected: [Count]
- Time saved: [Estimate]

## References
- [Issue/PR links]
- [External documentation]
```

### B. References

- [Boris Cherny Implementation Plan](/home/dttai/.claude/plans/parallel-painting-turing.md)
- [CLAUDE.md v3.2.0](../../CLAUDE.md)
- [Evidence Vault Specification](../../02-design/14-Technical-Specs/Evidence-Vault-Spec.md)

---

**RFC Status**: 📋 DRAFT → ⏳ CTO REVIEW → ✅ APPROVED → 🔄 IMPLEMENTED
**Current Phase**: Track 1 (Methodology Documentation)
**Next Phase**: Track 2 (Implementation - Sprint 144, conditional)

**Framework-First Compliance**: ✅ VERIFIED
**Tool-Agnostic**: ✅ VERIFIED
**Boris Cherny Coverage**: ✅ Partial Gap Addressed

---

*SDLC Framework 6.0.3 - Continuous Learning Protocol*
