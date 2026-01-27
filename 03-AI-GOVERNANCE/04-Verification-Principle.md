# Principle 4: Verification-First

**Version**: 5.3.0
**Status**: ACTIVE
**Date**: January 27, 2026

---

## The Rule

> **Prove it works BEFORE it merges.**
>
> Evidence-based development is not optional.

---

## TDD with AI

Test-Driven Development amplifies AI effectiveness:

```
┌─────────────────────────────────────────────────────────┐
│  1. WRITE TESTS from expected input/output              │
│     ↓                                                   │
│  2. CONFIRM tests fail (no implementation yet)          │
│     ↓                                                   │
│  3. COMMIT test suite                                   │
│     ↓                                                   │
│  4. IMPLEMENT code to pass tests                        │
│     ↓                                                   │
│  5. COMMIT completed implementation                     │
└─────────────────────────────────────────────────────────┘
```

> "AI performs best when it has a clear target to iterate against."
> — Anthropic Best Practices

---

## Why TDD Works Better with AI

| Without TDD | With TDD |
|-------------|----------|
| AI guesses requirements | AI has concrete test cases |
| Vague "make it work" | Specific pass/fail criteria |
| Drift from intent | Constrained to test suite |
| Manual verification needed | Automated verification |
| "It looks right" | "It passes tests" |

---

## Verification Checklist (MRP)

Before ANY merge of AI-generated code:

| Check | Tool | Required? |
|-------|------|-----------|
| Unit tests pass | pytest, vitest | MANDATORY |
| Integration tests pass | pytest, playwright | MANDATORY |
| Coverage threshold met | coverage.py, c8 | MANDATORY (80%+) |
| SAST scan clean | Semgrep | MANDATORY |
| Lint errors zero | ruff, eslint | MANDATORY |
| Type check pass | mypy, tsc | MANDATORY |
| Human approval | PR review | MANDATORY |

---

## Evidence Artifact (MRP)

Every merge requires Merge-Readiness Pack:

```yaml
MRP:
  tests:
    unit: PASS (127/127)
    integration: PASS (45/45)
    coverage: 87% (threshold: 80%)

  security:
    sast: CLEAN (0 findings)
    dependencies: CLEAN (0 CVEs)

  quality:
    lint: PASS (0 errors)
    types: PASS (0 errors)

  approval:
    reviewer: @developer-name
    date: 2026-01-22
    comment: "Code reviewed, tested locally"
```

---

## Multi-Agent Verification

For critical code, use parallel verification:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   Agent 1 (Writer)         Agent 2 (Reviewer)          │
│   ┌─────────────┐          ┌─────────────┐             │
│   │ Generates   │          │ Reviews for │             │
│   │ code        │ ───────► │ issues      │             │
│   └─────────────┘          └─────────────┘             │
│                                   │                     │
│                                   ▼                     │
│                            Findings to                  │
│                            Human for                    │
│                            final decision               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

> "One agent writes code while another reviews...
> often yields better results than single agent handling everything."

---

## Anti-Pattern: Verification Skipping

```
❌ BAD:
   AI generates code
   "Tests take too long, I'll add them later"
   Code ships without tests
   Bug discovered in production

✅ CORRECT:
   AI generates tests first
   Tests fail (no implementation)
   AI generates implementation
   Tests pass
   Human reviews
   Code ships WITH evidence
```

---

## Zero Mock Policy

From NQH-Bot lessons (679 mocks → 78% production failure):

| Policy | Rationale |
|--------|-----------|
| No `// TODO: implement` | Real code or nothing |
| No `return mock_data` | Real implementations only |
| No `pass # placeholder` | Complete or don't commit |
| Real services in dev | Docker Compose with actual DB, Redis, etc. |

---

## Tool-Agnostic Application

This principle applies to ALL AI tools:
- Always write tests before implementation
- Always verify before merge
- Always create evidence artifacts
- Never skip verification "to save time"

---

## Related Principles

- [02-Agent-Accountability](02-Agent-Accountability.md) - Human owns verified code
- [03-Planning-Mode-Principle](03-Planning-Mode-Principle.md) - Plan includes verification
- [07-Anti-Patterns](07-Anti-Patterns.md) - Verification anti-patterns

---

**Document Status**: ACTIVE
**Last Updated**: January 22, 2026
