# Principle 7: AI Development Anti-Patterns

**Version**: 6.2.1
**Status**: ACTIVE
**Date**: January 28, 2026

---

## Overview

Learning what NOT to do is as important as knowing best practices.
These anti-patterns come from production failures and expert experience.

---

## The 8 Critical Anti-Patterns

### 1. Blind Acceptance

```
❌ PROBLEM:
   AI generates 500 lines of code
   Developer clicks "Accept All" without reading
   Code ships to production
   Bug causes incident

✅ SOLUTION:
   Review every line before commit
   Understand the code you're shipping
   You own it, you must read it
```

**Rule**: If you can't explain the code, don't ship it.

---

### 2. Context Stuffing

```
❌ PROBLEM:
   Dump entire codebase into context (10K+ lines)
   "AI will figure out what's relevant"
   AI becomes confused, gives poor results

✅ SOLUTION:
   Provide only relevant files (<150 lines total)
   Use progressive disclosure for large projects
   Focus context on the task at hand
```

**Rule**: Less context, more focus = better results.

---

### 3. Mock Proliferation

```
❌ PROBLEM:
   AI creates mocks for unknown dependencies
   "I'll implement the real version later"
   Mocks hide integration issues
   78% production failure rate (AI chatbot project case)

✅ SOLUTION:
   Zero Mock Policy
   Use real implementations or ask
   Docker Compose with real services in dev
```

**Rule**: Mocks hide problems until production.

---

### 4. Planning Avoidance

```
❌ PROBLEM:
   "Just let AI figure it out" for complex changes
   No exploration of existing patterns
   AI drifts from codebase conventions
   Inconsistent architecture

✅ SOLUTION:
   Use Planning Mode for risk-factor changes
   Explore codebase first (agentic grep)
   Extract patterns before generating code
```

**Rule**: Planning prevents architectural drift.

---

### 5. Evidence Skipping

```
❌ PROBLEM:
   "Tests take too long, I'll add them later"
   "SAST is too strict, skip it"
   Code merges without verification
   Bugs and vulnerabilities ship

✅ SOLUTION:
   MRP required for every merge
   Tests, coverage, SAST, lint = mandatory
   No evidence = no merge
```

**Rule**: Evidence is not optional.

---

### 6. Vague Prompts

```
❌ PROBLEM:
   "Make it better"
   "Fix the bug"
   "Add error handling"
   AI guesses at requirements

✅ SOLUTION:
   "Refactor UserService to use dependency injection"
   "Fix null pointer on line 42 of order_service.py"
   "Add error handling for network failures in api_client.py
    following pattern in auth_client.py"
```

**Rule**: Specific prompts get specific results.

---

### 7. Single Model Dependency

```
❌ PROBLEM:
   Only use one AI tool/model
   Get stuck on hard problems
   "AI can't solve this"

✅ SOLUTION:
   Different models for different tasks
   Switch models when stuck
   Fresh perspective often helps
```

**Rule**: Model diversity beats model loyalty.

---

### 8. Verification Bypass

```
❌ PROBLEM:
   Trust AI output without testing
   "AI is smart, it must be correct"
   Skip manual review "to save time"
   Production incident

✅ SOLUTION:
   TDD approach - tests first
   Run tests before accepting code
   Human review always required
```

**Rule**: Trust but verify (always verify).

---

## Anti-Pattern Quick Reference

| # | Anti-Pattern | One-Line Fix |
|---|--------------|--------------|
| 1 | Blind Acceptance | Read every line |
| 2 | Context Stuffing | <150 lines total |
| 3 | Mock Proliferation | Zero Mock Policy |
| 4 | Planning Avoidance | Plan for risk factors |
| 5 | Evidence Skipping | MRP required |
| 6 | Vague Prompts | Be specific |
| 7 | Single Model | Switch when stuck |
| 8 | Verification Bypass | Tests first |

---

## Detection Checklist

Use this in code review to catch anti-patterns:

```yaml
Review Checklist:
  - [ ] Did developer read all AI-generated code? (vs Blind Acceptance)
  - [ ] Is context file <150 lines? (vs Context Stuffing)
  - [ ] Are there any mock implementations? (vs Mock Proliferation)
  - [ ] Was planning done for risk factors? (vs Planning Avoidance)
  - [ ] Is MRP complete and passing? (vs Evidence Skipping)
  - [ ] Were prompts specific in PR description? (vs Vague Prompts)
  - [ ] Was alternative model tried if stuck? (vs Single Model)
  - [ ] Do tests exist and pass? (vs Verification Bypass)
```

---

## These Apply to ALL AI Tools

These anti-patterns are tool-agnostic:
- Blind Acceptance happens with any AI
- Context Stuffing affects any context window
- Mock Proliferation is a practice problem, not tool problem
- etc.

**The fix is in the process, not the tool.**

---

## Related Principles

- [01-AI-Human-Collaboration](01-AI-Human-Collaboration.md) - Correct collaboration model
- [02-Agent-Accountability](02-Agent-Accountability.md) - Human accountability
- [03-Planning-Mode-Principle](03-Planning-Mode-Principle.md) - When to plan
- [04-Verification-Principle](04-Verification-Principle.md) - How to verify
- [05-Context-Management](05-Context-Management.md) - Context best practices
- [06-Tool-Evaluation-Criteria](06-Tool-Evaluation-Criteria.md) - Tool selection

---

**Document Status**: ACTIVE
**Last Updated**: January 22, 2026
