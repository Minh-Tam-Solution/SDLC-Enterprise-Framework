# Principle 2: Agent Accountability

**Version**: 6.3.0
**Status**: ACTIVE
**Date**: January 28, 2026

---

## The Rule

> **Human ALWAYS owns the code that ships.**
>
> AI is a tool. Humans are accountable.

---

## Accountability Chain

```
Code Generated → Human Reviews → Human Approves → Human Ships → Human Accountable
      ↑                                                              ↑
   AI does this                                              Human owns this
```

---

## What This Means in Practice

### Human is Accountable For:

| Area | Accountability |
|------|---------------|
| **Correctness** | Code does what it should |
| **Security** | No vulnerabilities introduced |
| **Performance** | Meets latency/resource targets |
| **Compliance** | Follows legal/regulatory requirements |
| **Architecture** | Fits system design |
| **Maintenance** | Code is maintainable |

### AI is NOT Accountable For:

- Production incidents caused by AI-generated code
- Security breaches from AI-suggested patterns
- Performance issues from AI implementations
- Legal issues from AI code suggestions

**Why?** AI cannot be held legally or professionally responsible. Only humans can.

---

## The Review Mandate

Before any AI-generated code ships:

```yaml
MANDATORY:
  - [ ] Human has READ every line
  - [ ] Human UNDERSTANDS the code
  - [ ] Human can EXPLAIN the code
  - [ ] Human can MAINTAIN the code
  - [ ] Human APPROVES the merge

OPTIONAL (but recommended):
  - [ ] Peer review by second human
  - [ ] Automated tests pass
  - [ ] Security scan clean
```

---

## Evidence Requirements (MRP)

Every merge of AI-generated code requires a Merge-Readiness Pack:

| Evidence | Description |
|----------|-------------|
| Tests | Unit + integration tests pass |
| Coverage | Meets coverage threshold |
| Security | SAST scan clean |
| Lint | No lint errors |
| Human Approval | PR approved by human |

---

## Anti-Pattern: Blind Acceptance

```
❌ DANGEROUS:
   AI generates 500 lines of code
   Developer clicks "Accept All"
   Code ships to production
   Bug causes incident
   "But the AI wrote it!" ← NOT A DEFENSE

✅ CORRECT:
   AI generates 500 lines of code
   Developer reads every line
   Developer modifies 3 functions
   Developer adds tests
   Developer approves merge
   Developer owns the result
```

---

## Legal & Compliance Note

In regulated industries (healthcare, finance, etc.):
- AI-generated code must be reviewed same as human code
- Audit trails must show human approval
- "AI wrote it" is never a compliance defense

---

## Related Principles

- [01-AI-Human-Collaboration](01-AI-Human-Collaboration.md) - The collaboration model
- [04-Verification-Principle](04-Verification-Principle.md) - How to verify
- [07-Anti-Patterns](07-Anti-Patterns.md) - Common mistakes

---

**Document Status**: ACTIVE
**Last Updated**: January 22, 2026
