# Principle 1: AI-Human Collaboration

**Version**: 6.2.1
**Status**: ACTIVE
**Date**: January 28, 2026

---

## The Core Model

AI-assisted development follows a clear division of responsibilities:

| Role | Who | Responsibility |
|------|-----|----------------|
| **SE4H** (Human Coach) | Developer/PM | Guide, supervise, DECIDE |
| **SE4A** (Agent Executor) | AI Assistant | Implement, propose, NEVER decide |

---

## The Collaboration Loop

```
┌──────────────────────────────────────────────────────────┐
│  1. HUMAN defines intent (WHAT + WHY)                    │
│     ↓                                                    │
│  2. AGENT proposes approach (HOW)                        │
│     ↓                                                    │
│  3. HUMAN approves/modifies                              │
│     ↓                                                    │
│  4. AGENT executes                                       │
│     ↓                                                    │
│  5. HUMAN verifies result                                │
│     ↓                                                    │
│  6. HUMAN takes accountability                           │
└──────────────────────────────────────────────────────────┘
```

---

## Key Rules

### Human Responsibilities
- Define clear requirements (the WHAT)
- Explain business context (the WHY)
- Review all AI-generated code
- Make architectural decisions
- Approve before merge
- Take accountability for shipped code

### Agent Responsibilities
- Propose implementation approaches
- Generate code following patterns
- Ask clarifying questions (CRP)
- Provide evidence of quality (MRP)
- Never commit without human approval
- Never make architectural decisions alone

---

## Decision Authority

| Decision Type | Authority | Example |
|---------------|-----------|---------|
| Business requirements | Human ONLY | "Users need password reset" |
| Architecture choices | Human ONLY | "Use microservices vs monolith" |
| Implementation details | Agent proposes, Human approves | "Use bcrypt for hashing" |
| Code formatting | Agent (via linters) | "Use 2-space indent" |
| Test approach | Human defines, Agent implements | "Need 80% coverage" |

---

## This Principle is Tool-Agnostic

Works with: Claude, GPT, Gemini, Copilot, Cursor, future tools.

The collaboration model remains the same regardless of which AI assistant you use.

---

## Anti-Pattern: Blind Delegation

```
❌ BAD: "Write the authentication system"
   (No context, no constraints, no review)

✅ GOOD: "Implement JWT authentication following our auth patterns
         in src/auth/. Use bcrypt (cost=12) for password hashing.
         I'll review before merge."
   (Clear context, constraints, human verification)
```

---

## Related Principles

- [02-Agent-Accountability](02-Agent-Accountability.md) - Who owns the code
- [03-Planning-Mode-Principle](03-Planning-Mode-Principle.md) - When to plan first
- [04-Verification-Principle](04-Verification-Principle.md) - How to verify

---

**Document Status**: ACTIVE
**Last Updated**: January 22, 2026
