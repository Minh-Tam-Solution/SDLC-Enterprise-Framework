# Git Workflow Patterns for AI Development

**Version**: 6.1.2
**Date**: February 2, 2026
**Status**: ACTIVE
**Framework**: SDLC 6.1.2
**Ring**: 2 (Governance - Best Practices)
**Source**: Consolidated from RFC-SDLC-604 (Boris Cherny Tactic #2)

---

## Overview

Efficient git workflows enable AI-assisted parallel development, achieving **2.5x productivity** improvements through strategic use of git worktrees and contract-first patterns.

### Problem Addressed

**Sequential Development Constraint**:
- Standard workflow: One branch, one AI session
- Components developed sequentially: Backend (Day 1) → Frontend (Day 2) → Tests (Day 3) → Docs (Day 4)
- **Total**: 4 days (20 hours)

**Parallel Development Solution**:
- Multiple git worktrees, multiple AI sessions
- Components developed simultaneously: Backend + Frontend + Tests + Docs (all on Day 1)
- **Total**: 1 day (8 hours) - **2.5x speedup**

---

## Pattern 1: Git Worktrees for Parallel Development

### What is a Git Worktree?

**Git worktrees** enable multiple working directories linked to the same repository:
- Each worktree checks out a different branch
- Shares `.git` directory (saves disk space)
- Changes in one worktree don't affect others
- Perfect for parallel AI development

**Example Structure**:
```bash
# Main repository
/home/user/sdlc-orchestrator (main branch)

# Create worktrees
git worktree add ../sdlc-api feature/api-v2
git worktree add ../sdlc-ui feature/ui-v2
git worktree add ../sdlc-tests feature/tests-v2

# Result:
/home/user/sdlc-orchestrator (main)           # Original
/home/user/sdlc-api (feature/api-v2)          # Worktree 1
/home/user/sdlc-ui (feature/ui-v2)            # Worktree 2
/home/user/sdlc-tests (feature/tests-v2)      # Worktree 3
```

---

### Parallel AI Development Workflow

**Step 1: Feature Breakdown (Human-Driven)**

Decompose feature into **independent components**:

```yaml
Feature: Implement user authentication (500 LOC)

Component Breakdown:
  1. Backend API (200 LOC)
     - POST /api/v1/auth/login
     - POST /api/v1/auth/register
     - JWT token generation
     - Files: backend/app/api/v1/endpoints/auth.py

  2. Frontend UI (150 LOC)
     - Login page component
     - Registration form
     - Auth context provider
     - Files: frontend/src/pages/Login.tsx

  3. Tests (100 LOC)
     - Backend unit tests (pytest)
     - Frontend component tests (Vitest)
     - Files: backend/tests/unit/test_auth.py

  4. Documentation (50 LOC)
     - API reference (OpenAPI)
     - User guide
     - Files: docs/03-integrate/01-api-specifications/

Independence Check:
  ✅ Backend ↔ Frontend: API contract defined (OpenAPI spec)
  ✅ Tests: Can write from specification
  ✅ Docs: Based on specification

Result: ALL 4 COMPONENTS INDEPENDENT → Parallel development enabled
```

**Step 2: Create Worktrees**

```bash
# Navigate to main repository
cd /home/user/sdlc-orchestrator

# Create worktrees manually
git worktree add ../sdlc-auth-backend feature/auth-backend
git worktree add ../sdlc-auth-frontend feature/auth-frontend
git worktree add ../sdlc-auth-tests feature/auth-tests
git worktree add ../sdlc-auth-docs feature/auth-docs

# Verify worktrees
git worktree list
# Output:
# /home/user/sdlc-orchestrator        main
# /home/user/sdlc-auth-backend        feature/auth-backend
# /home/user/sdlc-auth-frontend       feature/auth-frontend
# /home/user/sdlc-auth-tests          feature/auth-tests
# /home/user/sdlc-auth-docs           feature/auth-docs
```

**Step 3: Launch Parallel AI Sessions**

Open separate terminal/IDE instances for each worktree:

```bash
# Terminal 1: Backend AI session
cd ../sdlc-auth-backend
cursor .  # Or Claude Code, or any AI coding assistant
# Prompt: "Implement authentication endpoints per SPEC-042.md"

# Terminal 2: Frontend AI session
cd ../sdlc-auth-frontend
cursor .
# Prompt: "Implement login/register pages per DESIGN-042.md"

# Terminal 3: Tests AI session
cd ../sdlc-auth-tests
cursor .
# Prompt: "Write unit + integration tests per SPEC-042.md"

# Terminal 4: Docs AI session
cd ../sdlc-auth-docs
cursor .
# Prompt: "Update API reference for authentication"
```

**Step 4: Development (AI-Driven, Human-Monitored)**

Each AI session works independently:
- **Backend**: Writes `auth.py` + database models (8 hours)
- **Frontend**: Writes `Login.tsx` + `Register.tsx` (6 hours)
- **Tests**: Writes `test_auth.py` + `auth.test.ts` (4 hours)
- **Docs**: Updates `API-Specification.md` (2 hours)

**Total Duration**: 8 hours (longest session) vs 20 hours (sequential)
**Speedup**: 2.5x

**Step 5: Create PRs**

```bash
# Backend worktree
cd ../sdlc-auth-backend
git add .
git commit -m "feat(auth): Add authentication endpoints"
git push origin feature/auth-backend
gh pr create --title "Backend: Authentication API"

# Frontend worktree
cd ../sdlc-auth-frontend
git add .
git commit -m "feat(auth): Add login/register pages"
git push origin feature/auth-frontend
gh pr create --title "Frontend: Authentication UI"

# Tests worktree (same pattern)
# Docs worktree (same pattern)
```

**Result**: 4 PRs created simultaneously

**Step 6: Code Review & Sequential Merge**

**Merge Order** (dependencies first):
```bash
# 1. Merge backend first (establishes API)
gh pr merge 1234 --squash

# 2. Rebase frontend on updated main (consumes API)
cd ../sdlc-auth-frontend
git fetch origin
git rebase origin/main
git push --force-with-lease
gh pr merge 1235 --squash

# 3. Merge tests (validates both backend + frontend)
gh pr merge 1236 --squash

# 4. Merge docs (references final API)
gh pr merge 1237 --squash
```

**Why Sequential Merge?**
- Prevents merge conflicts
- Ensures dependencies resolved in order
- Allows rebasing on latest main before each merge

**Step 7: Cleanup**

```bash
# Remove worktrees after merge
git worktree remove ../sdlc-auth-backend
git worktree remove ../sdlc-auth-frontend
git worktree remove ../sdlc-auth-tests
git worktree remove ../sdlc-auth-docs

# Verify cleanup
git worktree list
# Should only show main repository
```

---

### When to Use Parallel Development

**Criteria Checklist**:

| Criterion | Threshold | Example |
|-----------|-----------|---------|
| **Feature Size** | >500 LOC | User auth (500 LOC) ✅ |
| **Component Independence** | API contract defined | Backend/Frontend via OpenAPI ✅ |
| **Time Criticality** | Sprint deadline <5 days | Launch in 3 days ✅ |
| **Component Count** | 3-5 components | Backend/Frontend/Tests/Docs (4) ✅ |

**Use Parallel Development When**:
- ✅ Feature >500 LOC with 3-5 independent components
- ✅ API contract predefined (OpenAPI specification)
- ✅ Time-critical deadline (sprint end, launch date)
- ✅ Multiple AI sessions feasible (developer can monitor)

**When NOT to Use**:
- ❌ Small features (<200 LOC) → Sequential faster
- ❌ Tightly coupled components → High merge conflict risk
- ❌ Undefined API contracts → Rework required
- ❌ Single developer, single monitor → Can't supervise 4 sessions
- ❌ Rapid iteration needed → Too much coordination overhead

---

### Coordination Strategy: Contract-First Development

**Problem**: How to prevent AI sessions from conflicting?

**Solution**: **Contract-First Development**

#### 1. Define API Contract (Before Worktrees)

Create OpenAPI specification **before** parallel development:

```yaml
# SPEC-042-Auth-API.yaml (created at Gate G2)

openapi: 3.1.0
info:
  title: Authentication API
  version: 1.0.0

paths:
  /api/v1/auth/login:
    post:
      summary: User login
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                username:
                  type: string
                  example: "user@example.com"
                password:
                  type: string
                  format: password
      responses:
        '200':
          description: Login successful
          content:
            application/json:
              schema:
                type: object
                properties:
                  access_token:
                    type: string
                  refresh_token:
                    type: string
                  expires_in:
                    type: integer
        '401':
          description: Invalid credentials
```

**Freeze Contract**: API spec is **immutable** during parallel development.

#### 2. Assign File Ownership (No Overlap)

Each worktree owns **distinct files**:

```yaml
Worktree 1 (Backend):
  - backend/app/api/v1/endpoints/auth.py
  - backend/app/schemas/auth.py
  - backend/app/services/auth_service.py

Worktree 2 (Frontend):
  - frontend/src/pages/Login.tsx
  - frontend/src/pages/Register.tsx
  - frontend/src/context/AuthContext.tsx

Worktree 3 (Tests):
  - backend/tests/unit/test_auth.py
  - frontend/tests/Login.test.tsx

Worktree 4 (Docs):
  - docs/03-integrate/01-api-specifications/auth.md
```

**No file should appear in multiple worktrees** (prevents conflicts).

#### 3. Staged Merges (Sequential, Not Parallel)

**Merge Order**:
```
Backend (no deps) → Frontend (depends on API) → Tests (validates both) → Docs (references API)
```

**Rebase Protocol**:
```bash
# After backend merged, rebase frontend
cd ../sdlc-auth-frontend
git fetch origin
git rebase origin/main
# Resolve any conflicts (rare if file ownership respected)
git push --force-with-lease
```

#### 4. Communication Channel (Slack/Discord)

Create dedicated channel per feature:
- **Channel**: `#feature-user-auth`
- **Purpose**: Coordinate AI sessions, report issues
- **Updates**: AI agents post progress (optional MCP integration)

---

## Pattern 2: Branch Naming Conventions

### Standard Naming

```bash
# Feature branches
feature/user-auth-backend
feature/user-auth-frontend
feature/user-auth-tests
feature/user-auth-docs

# Bugfix branches
bugfix/login-token-expiry

# Hotfix branches (production)
hotfix/critical-auth-bypass

# Release branches
release/v1.2.0
```

### Component Suffix Pattern

For parallel development, use **component suffixes**:
- `feature/<feature-name>-backend`
- `feature/<feature-name>-frontend`
- `feature/<feature-name>-tests`
- `feature/<feature-name>-docs`

**Example**: User authentication feature
- `feature/auth-backend`
- `feature/auth-frontend`
- `feature/auth-tests`
- `feature/auth-docs`

**Benefit**: Clear component ownership, easy to track in GitHub

---

## Pattern 3: Worktree Management Commands

### Create Worktree

```bash
# Syntax
git worktree add <path> <branch-name>

# Example
git worktree add ../sdlc-auth-backend feature/auth-backend

# Create branch from existing branch
git worktree add -b feature/auth-frontend ../sdlc-auth-frontend origin/main
```

### List Worktrees

```bash
git worktree list

# Output:
# /home/user/sdlc-orchestrator        main
# /home/user/sdlc-auth-backend        feature/auth-backend
# /home/user/sdlc-auth-frontend       feature/auth-frontend
```

### Remove Worktree

```bash
# Remove worktree directory
git worktree remove ../sdlc-auth-backend

# Force remove (if changes present)
git worktree remove --force ../sdlc-auth-backend
```

### Prune Worktrees (Cleanup Stale References)

```bash
# Remove worktree references for deleted directories
git worktree prune
```

---

## Success Metrics

### Productivity Improvements

| Metric | Sequential | Parallel (Worktrees) | Improvement |
|--------|-----------|----------------------|-------------|
| **Development Time** | 20 hours (4 days) | 8 hours (1 day) | **2.5x faster** |
| **Context Switching** | High (4 switches) | None (simultaneous) | **Eliminated** |
| **Merge Conflicts** | Medium (sequential PRs) | Low (file ownership) | **-50%** |
| **Time to Market** | 4 days | 1-2 days (with reviews) | **2x faster** |

### When Productivity Gains Apply

**Best Case** (2.5x speedup):
- 4 independent components
- Clear API contracts
- Minimal dependencies
- Experienced developer monitoring

**Typical Case** (1.8x speedup):
- 3 components
- Some dependencies
- Coordination overhead
- Learning curve

**Not Recommended** (<1.2x speedup):
- <3 components (overhead > benefit)
- Tightly coupled code
- Undefined contracts
- Inexperienced with worktrees

---

## Integration with SDLC Framework

### Stage 04 (Build) Alignment

Parallel development with worktrees fits **Stage 04 (Build)**:
- **Purpose**: Accelerate implementation phase
- **When**: After Gate G2 (Design Ready) with frozen API contracts
- **Who**: Developers with AI coding assistants

### Gate G2 (Design Ready) Prerequisites

Before parallel development:
- ✅ API contracts defined (OpenAPI specification)
- ✅ Component boundaries clear (file ownership matrix)
- ✅ Dependencies mapped (merge order determined)
- ✅ Testing strategy defined (per-component + integration)

### Evidence Vault Tracking

Each worktree PR creates Evidence artifacts:
```json
{
  "artifact_id": "EVD-2026-03-042-backend",
  "type": "parallel_development",
  "worktree": "feature/auth-backend",
  "component": "backend",
  "parent_feature": "user-authentication",
  "pr_url": "https://github.com/org/repo/pull/1234",
  "merge_order": 1,
  "timestamp": "2026-03-05T16:00:00Z"
}
```

---

## Common Pitfalls & Mitigations

### Pitfall 1: Merge Conflicts Across PRs

**Cause**: Overlapping file modifications

**Mitigation**:
- ✅ **File Ownership Matrix**: Assign exclusive files to each worktree
- ✅ **Rebase Before Merge**: Each PR rebases on latest main
- ✅ **Sequential Merge**: Backend → Frontend → Tests → Docs

### Pitfall 2: API Contract Drift

**Cause**: AI sessions deviate from OpenAPI specification

**Mitigation**:
- ✅ **Contract Validation**: CI/CD checks OpenAPI compliance
- ✅ **Frozen Specification**: Lock spec file during parallel development
- ✅ **Automated Tests**: Integration tests validate API contract

### Pitfall 3: Coordination Overhead

**Cause**: Too many worktrees, complex dependencies

**Mitigation**:
- ✅ **Limit Worktrees**: Max 3-5 components
- ✅ **Simple Features First**: Learn pattern on simple features
- ✅ **Communication Channel**: Slack/Discord for coordination

### Pitfall 4: Lost Changes

**Cause**: Worktree deleted without pushing

**Mitigation**:
- ✅ **Check Status**: `git status` before worktree removal
- ✅ **Force Check**: `git worktree remove` warns if uncommitted changes
- ✅ **Backup Strategy**: Push WIP branches frequently

---

## References

### Framework Documents

- [Sub-agent Orchestration](./03-sub-agent-orchestration.md) - Parallel agent patterns
- [Stage 04 (Build)](../../02-Core-Methodology/SDLC-Stage-04-Build.md) - Implementation phase
- [Context Management](../../03-AI-Governance/05-Context-Management.md) - AGENTS.md patterns

### External Resources

- [Git Worktree Documentation](https://git-scm.com/docs/git-worktree) - Official Git documentation
- [Boris Cherny Best Practices](https://example.com/boris-cherny) - Original source (Tactic #2)
- [Contract-First Development](https://swagger.io/resources/articles/adopting-an-api-first-approach/) - OpenAPI patterns

### Related Patterns

- [MCP Integration Guide](../../07-Implementation-Guides/MCP-Integration-Guide.md) - Automated bug triage
- [Continuous Learning Protocol](../../03-AI-Governance/05-Context-Management.md#continuous-learning-protocol) - Learning from mistakes

---

**Document Status**: ACTIVE
**Created**: February 2, 2026
**Framework**: SDLC 6.1.2
**Ring**: 2 (Governance - Best Practices)
**Source**: Consolidated from RFC-SDLC-604 (Boris Cherny Tactic #2)
**Owner**: Engineering + Tech Leads
**Approval**: CTO @nqh ✅
