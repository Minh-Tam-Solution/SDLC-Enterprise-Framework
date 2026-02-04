# AI Governance Principles

**Version**: 6.0.4
**Status**: ACTIVE
**Date**: February 8, 2026
**Pillar**: Core AI Governance (Enhanced in 6.0.4 with TDD Integration)

---

## Overview

This section contains **timeless principles** for AI+Human collaboration.
These principles are **tool-agnostic** and apply regardless of which AI coding assistant you use.

> **Philosophy**: "Govern tools, don't document them"
>
> Tools change constantly. Principles endure.

---

## The 7 AI Governance Principles

| # | Principle | Summary | File |
|---|-----------|---------|------|
| 1 | **AI-Human Collaboration** | Human guides, AI executes, Human verifies | [01-AI-Human-Collaboration.md](01-AI-Human-Collaboration.md) |
| 2 | **Agent Accountability** | Human ALWAYS responsible for shipped code | [02-Agent-Accountability.md](02-Agent-Accountability.md) |
| 3 | **Planning Mode** | Risk-based trigger for planning before coding | [03-Planning-Mode-Principle.md](03-Planning-Mode-Principle.md) |
| 4 | **Verification-First** | TDD (RED-GREEN-REFACTOR), evidence, validation | [04-Verification-Principle.md](04-Verification-Principle.md) |
| 5 | **Context Management** | AGENTS.md pattern, keep context <60 lines | [05-Context-Management.md](05-Context-Management.md) |
| 6 | **Tool Evaluation** | Criteria to evaluate ANY new AI tool | [06-Tool-Evaluation-Criteria.md](06-Tool-Evaluation-Criteria.md) |
| 7 | **Anti-Patterns** | What NOT to do with AI assistants | [07-Anti-Patterns.md](07-Anti-Patterns.md) |

---

## Concentric Circles Model

These principles sit in the **Core** ring of the Framework:

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    ┌─────────────────────────────────────────────────┐     │
│    │                                                 │     │
│    │         🎯 CORE (Timeless Principles)          │     │
│    │                                                 │     │
│    │    • Design Thinking                           │     │
│    │    • 10-Stage Lifecycle                        │     │
│    │    • Quality Gates                             │     │
│    │    • AI GOVERNANCE PRINCIPLES ← YOU ARE HERE   │     │
│    │                                                 │     │
│    └─────────────────────────────────────────────────┘     │
│                                                             │
│              📋 GOVERNANCE (Stable Rules)                  │
│              4-Tier, Sprint Planning, Roles                │
│                                                             │
│         🔧 OUTER RING (Tool Guides - Changes Often)        │
│         Claude, Cursor, Copilot specific content           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## When Principles Were Promoted to Core

| Principle | Origin | Promoted | Rationale |
|-----------|--------|----------|-----------|
| AI-Human Collaboration | SE 3.0 SASE | v5.1.0 | Fundamental to all AI work |
| Agent Accountability | BFlow lessons | v5.0.0 | Legal/compliance requirement |
| Planning Mode | 2026 Best Practices | v5.2.0 | Universal pattern, proven effective |
| Verification-First | TDD movement | v5.0.0 → v6.0.4 | Quality foundation + Tier-aware coverage |
| Context Management | AGENTS.md standard | v5.2.0 | 60K+ repos use pattern |
| Tool Evaluation | Framework need | v5.2.0 | Prevent tool-chasing |
| Anti-Patterns | Production failures | v5.2.0 | Learn from mistakes |

---

## Promotion Criteria

A tool feature is promoted to Core when it meets ALL criteria:

| Criteria | Test | Example |
|----------|------|---------|
| **Universal** | Works with ANY AI tool | Planning Mode ✅ |
| **Timeless** | Won't obsolete in 12 months | Context file pattern ✅ |
| **Fundamental** | Changes HOW we work | Human-in-loop ✅ |
| **Proven** | Battle-tested 6+ months | TDD with AI ✅ |

**Counter-examples** (stay in Outer Ring):
- MCP servers (Claude-specific)
- Specific model names (change frequently)
- Slash command syntax (tool-specific)

---

## Related Documents

- [CONTENT-MAP.md](../CONTENT-MAP.md) - Topic → canonical file mapping
- [DEPRECATION-POLICY.md](../DEPRECATION-POLICY.md) - Redirect rules
- [SDLC-Agentic-Core-Principles.md](../02-Core-Methodology/SDLC-Agentic-Core-Principles.md) - SE4H/SE4A model
- [best-practices-2026/](../04-AI-TOOLS-LANDSCAPE/best-practices-2026/) - Tool-specific guides

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: February 8, 2026
**Framework**: SDLC 6.0.4
