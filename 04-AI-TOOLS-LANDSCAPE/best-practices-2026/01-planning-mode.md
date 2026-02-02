# Planning Mode Guide
## Pre-Implementation Pattern Extraction for AI Agents

**Version:** 6.0.2
**Status:** ACTIVE
**Date:** January 27, 2026
**Core Principle:** [03-AI-GOVERNANCE/03-Planning-Mode-Principle.md](../../03-AI-GOVERNANCE/03-Planning-Mode-Principle.md)

---

## Overview

Planning Mode is a **RISK-BASED** workflow for AI agents. The key insight: **Planning is triggered by RISK, not just lines of code.**

> "LOC is a heuristic. Risk factors are the real criteria."
> — SDLC 5.3.0 Core Principle

---

## The Problem

When AI agents make risky changes, **architectural drift** becomes a significant risk:

1. **Pattern Inconsistency**: New code doesn't follow existing codebase patterns
2. **Architecture Violation**: Architectural decisions are ignored or contradicted
3. **Convention Drift**: Code style and naming conventions become inconsistent
4. **Test Pattern Mismatch**: Tests don't follow existing test patterns
5. **Security Vulnerabilities**: Risky changes bypass security review

> "Khi không dùng planning mode, codebase dễ bị architectural drift. Planning mode spawns explore sub-agents → extract patterns → build on them. This prevents drift."

**Important (5.3.0 Update)**: The old ">15 LOC" rule was **gameable** (split 100 LOC into 7 commits of 14 LOC each). Risk-based triggers are **intent-based** and cannot be gamed.

---

## Planning Mode Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PLANNING MODE WORKFLOW                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  INPUT: Task description + context                                  │
│                                                                     │
│  PHASE 1: PATTERN EXTRACTION (Parallel Sub-agents)                  │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐  │ │
│  │ │ Similar Code    │ │ Architecture    │ │ Test Pattern    │  │ │
│  │ │ Explorer        │ │ Explorer        │ │ Explorer        │  │ │
│  │ │                 │ │                 │ │                 │  │ │
│  │ │ - Find similar  │ │ - Load relevant │ │ - Find test     │  │ │
│  │ │   implementations│ │   ADRs/docs    │ │   patterns      │  │ │
│  │ │ - Extract code  │ │ - Extract       │ │ - Extract       │  │ │
│  │ │   patterns      │ │   constraints   │ │   conventions   │  │ │
│  │ └────────┬────────┘ └────────┬────────┘ └────────┬────────┘  │ │
│  │          │                    │                    │          │ │
│  │          └────────────────────┼────────────────────┘          │ │
│  └───────────────────────────────┼───────────────────────────────┘ │
│                                  ▼                                  │
│  PHASE 2: PATTERN SYNTHESIS                                         │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Planning Agent: Merge patterns → Implementation plan          │ │
│  │                                                               │ │
│  │ Output: PlanningContext                                       │ │
│  │   - similar_implementations: [code snippets]                  │ │
│  │   - architecture_constraints: [requirements]                  │ │
│  │   - code_patterns: [naming, structure, style]                 │ │
│  │   - test_patterns: [test structure, mocks, assertions]        │ │
│  │   - implementation_plan: [step-by-step approach]              │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                  │                                  │
│                                  ▼                                  │
│  PHASE 3: HUMAN APPROVAL                                            │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Present plan for approval:                                    │ │
│  │   - Show extracted patterns                                   │ │
│  │   - Show architecture constraints                             │ │
│  │   - Show proposed implementation approach                     │ │
│  │   - Request approval before proceeding                        │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                  │                                  │
│                                  ▼                                  │
│  PHASE 4: CONTEXT-AWARE GENERATION                                  │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │ Code Generator (with PlanningContext injected)                │ │
│  │   - Generate code following extracted patterns                │ │
│  │   - Respect architecture constraints                          │ │
│  │   - Match test patterns                                       │ │
│  │   - Validate against plan before output                       │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  OUTPUT: Code that follows existing patterns + Evidence             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## When to Use Planning Mode (Risk-Based Triggers)

### MANDATORY Planning Required

Planning is **REQUIRED** when change touches ANY of these risk factors:

| Risk Factor | Why It's Risky | Example |
|-------------|----------------|---------|
| **Data schema / API contracts** | Breaking changes affect consumers | Adding required field to API |
| **Authentication / Authorization** | Security-critical | Modifying login flow |
| **Cross-service boundaries** | Coordination complexity | Service A calls new Service B |
| **Concurrency / Race conditions** | Hard to test, subtle bugs | Shared state modification |
| **Security-sensitive code** | Vulnerabilities | Input validation, encryption |
| **Public API interfaces** | External consumers affected | REST endpoint changes |
| **Payment / Financial logic** | Money involved | Pricing calculation |

### RECOMMENDED Planning

Planning is **RECOMMENDED** (but not mandatory) when:

| Heuristic | Threshold | Rationale |
|-----------|-----------|-----------|
| Lines of code | >50 LOC | Higher drift risk |
| Files affected | >3 files | Coordination needed |
| Unfamiliar area | Yes | Need context first |
| Complex logic | Yes | Easy to miss edge cases |

### NO Planning Needed

Skip planning for:

| Scenario | Example |
|----------|---------|
| <15 LOC + no risk factors | Fix typo in error message |
| Documentation only | Update README |
| Test additions (no prod code) | Add missing test case |
| Formatting / linting | Run prettier |

### Decision Tree

```
Does change touch a MANDATORY risk factor?
├── YES → Planning REQUIRED
└── NO →
    Is change >50 LOC or >3 files?
    ├── YES → Planning RECOMMENDED
    └── NO →
        Is area unfamiliar?
        ├── YES → Planning RECOMMENDED
        └── NO → Planning OPTIONAL (just code)
```

---

## Phase 1: Pattern Extraction

### Similar Code Explorer

**Purpose:** Find implementations similar to the current task

**Technique: Agentic Grep (NOT RAG)**

> "Agentic grep (AI-powered code search) > RAG for context retrieval. Direct codebase exploration finds real patterns. RAG can miss context and produce stale results."

**Example queries:**
```bash
# Find similar service implementations
glob: **/services/**/*.py
grep: "class.*Service.*:"

# Find similar API endpoints
glob: **/api/**/*.py
grep: "@router\.(get|post|put|delete)"

# Find similar React components
glob: **/components/**/*.tsx
grep: "export (const|function)"
```

**Output:**
- List of similar implementations (file paths, snippets)
- Common patterns identified
- Naming conventions used

### Architecture Explorer

**Purpose:** Extract constraints from architectural decisions

**Sources to check:**
- ADRs (Architecture Decision Records)
- Technical specifications
- System design documents
- CLAUDE.md / AGENTS.md files

**Output:**
- Relevant constraints
- Required integrations
- Forbidden approaches

### Test Pattern Explorer

**Purpose:** Find test patterns matching the implementation

**Example queries:**
```bash
# Find test files for similar components
glob: **/tests/**/test_*.py
grep: "def test_.*service"

# Find test patterns
glob: **/tests/**/*.py
grep: "@pytest.fixture|@patch|mock"
```

**Output:**
- Test file structure
- Fixture patterns
- Mock strategies
- Assertion patterns

---

## Phase 2: Pattern Synthesis

Merge findings from all explorers into a coherent implementation plan:

```yaml
PlanningContext:
  similar_implementations:
    - file: backend/services/user_service.py
      pattern: "Service class with async methods, dependency injection"
    - file: backend/services/auth_service.py
      pattern: "Error handling with custom exceptions"

  architecture_constraints:
    - "Use async/await for all I/O operations"
    - "Follow OWASP ASVS Level 2 for security"
    - "Network-only access to AGPL components"

  code_patterns:
    naming: "snake_case for Python, PascalCase for classes"
    structure: "Service → Repository → Database"
    style: "Google docstrings, type hints required"

  test_patterns:
    framework: "pytest + pytest-asyncio"
    fixtures: "Use conftest.py for shared fixtures"
    mocking: "@patch for external dependencies"

  implementation_plan:
    steps:
      1: "Create service class with dependency injection"
      2: "Implement core methods following async pattern"
      3: "Add error handling with custom exceptions"
      4: "Write unit tests following existing patterns"
      5: "Add integration tests for API endpoints"

    estimated_changes:
      - new: "backend/services/new_service.py (~80 LOC)"
      - modified: "backend/main.py (+5 LOC)"
      - new: "backend/tests/test_new_service.py (~120 LOC)"
```

---

## Phase 3: Human Approval

Present the plan clearly for human review:

```
═══════════════════════════════════════════════════════════════
PLANNING: Add authentication middleware for API routes
═══════════════════════════════════════════════════════════════

PHASE 1: Pattern Extraction
───────────────────────────────────────────────────────────────

Similar Implementations Found:
  1. backend/middleware/cors_middleware.py (87% similar)
  2. backend/middleware/logging_middleware.py (72% similar)
  3. backend/middleware/rate_limit_middleware.py (65% similar)

Architecture Constraints:
  - JWT tokens with 15min expiry (per ADR-002)
  - OAuth 2.0 support required
  - Multi-provider fallback for AI operations

Code Patterns:
  - Middleware class with __call__ method
  - Async/await pattern used
  - Logger injection via dependency
  - Exception handling with HTTPException

Test Patterns:
  - pytest-asyncio for async tests
  - Mock external dependencies
  - Test both success and failure paths

═══════════════════════════════════════════════════════════════
PHASE 2: Implementation Plan
═══════════════════════════════════════════════════════════════

Proposed Steps:
  1. Create AuthMiddleware class in middleware/auth_middleware.py
  2. Implement JWT validation using existing auth_service
  3. Add OAuth token validation fallback
  4. Register middleware in app startup
  5. Create unit tests following existing patterns

Estimated Changes:
  - New: backend/middleware/auth_middleware.py (~80 LOC)
  - Modified: backend/main.py (+5 LOC)
  - New: backend/tests/middleware/test_auth_middleware.py (~120 LOC)

═══════════════════════════════════════════════════════════════

[A]pprove and proceed | [M]odify plan | [C]ancel
```

---

## Phase 4: Context-Aware Generation

With approved plan, generate code that:

1. **Follows extracted patterns** - Use the same structure, naming, style
2. **Respects constraints** - Apply all architecture requirements
3. **Matches test patterns** - Write tests in the same style
4. **Validates against plan** - Check output before completion
5. **Creates evidence** - Document what was done and why

---

## Benefits

1. **Prevents Architectural Drift** - 90% reduction in pattern violations
2. **Enforces Consistency** - Generated code follows existing patterns
3. **Human Oversight** - Approval gate before significant changes
4. **Audit Trail** - Full traceability from plan → code → evidence
5. **Quality Improvement** - Better first-pass code quality
6. **Knowledge Transfer** - Patterns are documented and reused

---

## Common Mistakes

### ❌ Skipping Planning for "Simple" Changes

Even if a change seems simple, >15 LOC can introduce drift.

### ❌ Using RAG Instead of Agentic Grep

RAG indexes can be stale. Direct codebase search finds real, current patterns.

### ❌ Not Getting Human Approval

Always present the plan before implementing. Human oversight prevents costly mistakes.

### ❌ Ignoring Extracted Patterns

The whole point is to follow patterns. Don't generate code that ignores them.

---

## Integration with SDLC Orchestrator

Planning Mode integrates with:

- **Evidence Vault**: Store planning context as evidence artifact
- **Gate Engine**: G-Sprint gate can require planning for large changes
- **Dynamic Context Overlay**: PlanningContext injected into AI prompts

---

**Document Status:** ACTIVE
**Last Updated:** January 22, 2026
