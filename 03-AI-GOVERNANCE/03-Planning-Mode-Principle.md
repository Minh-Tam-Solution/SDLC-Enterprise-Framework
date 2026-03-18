# Principle 3: Planning Mode (Risk-Based)

**Version**: 6.2.0
**Status**: ACTIVE
**Date**: January 28, 2026

---

## The Rule

> **Planning is triggered by RISK, not just lines of code.**
>
> LOC is a heuristic. Risk factors are the real criteria.

---

## Risk-Based Planning Trigger

### MANDATORY Planning Required

Planning mode is **REQUIRED** when change touches ANY of these:

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

---

## Planning Mode Workflow

```
┌─────────────────────────────────────────────────────────┐
│  1. EXPLORE                                             │
│     • Search for similar implementations (agentic grep) │
│     • Review existing ADRs and conventions              │
│     • Extract patterns from codebase                    │
│                                                         │
│  2. SYNTHESIZE                                          │
│     • Build implementation plan from patterns           │
│     • Identify dependencies and constraints             │
│     • Estimate scope and impact                         │
│                                                         │
│  3. APPROVE                                             │
│     • Present plan to human for validation              │
│     • Gather feedback and modifications                 │
│     • Lock approved approach                            │
│                                                         │
│  4. EXECUTE                                             │
│     • Generate code following approved plan             │
│     • Validate against plan constraints                 │
│     • Create evidence for audit                         │
└─────────────────────────────────────────────────────────┘
```

---

## Key Insight: Agentic Grep > RAG

> "Direct codebase exploration finds real patterns.
> RAG can miss context and produce stale results."

During EXPLORE phase:
- Search actual codebase for similar code
- Read real implementations, not indexed summaries
- Find current patterns, not outdated indexes

---

## Decision Tree

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

## Why Risk-Based > LOC-Based

The old rule ">15 LOC requires planning" was **gameable**:
- Split 100 LOC change into 7 commits of 14 LOC each
- Each commit "passes" but the whole is unplanned

Risk-based triggers are **intent-based**:
- Touching auth? Plan regardless of LOC
- Modifying API? Plan regardless of LOC
- Simple rename across 50 files? Maybe skip planning

---

## Tool-Agnostic Application

This principle works with ANY AI coding tool:
- Claude Code: Use `/plan` or EnterPlanMode
- Cursor: Create spec.md before implementation
- Copilot: Write pseudocode comments first
- Any tool: Document plan before generating code

---

## Related Principles

- [01-AI-Human-Collaboration](01-AI-Human-Collaboration.md) - Human approves plan
- [04-Verification-Principle](04-Verification-Principle.md) - Verify after execute
- [05-Context-Management](05-Context-Management.md) - Context for planning

**Companion**: [Planning Mode Best Practices (2026)](../04-AI-TOOLS-LANDSCAPE/best-practices-2026/01-planning-mode.md) — practical workflows and tool-specific patterns (this doc = doctrine, companion = practice).

---

**Document Status**: ACTIVE
**Last Updated**: February 18, 2026
