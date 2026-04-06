# AI Governance Principles

**Version**: 6.2.1
**Status**: ACTIVE
**Date**: March 18, 2026
**Pillar**: Core AI Governance (6.2.0: Lean Ring 1 — implementation patterns moved to Ring 2)

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

### Practical Enforcement Documents

| # | Document | Purpose |
|---|----------|---------|
| 8 | [Governance Decision Matrix](08-Governance-Decision-Matrix.md) | Flowchart: requirement → principle → enforcement action |
| 9 | [Governance Metrics & KPIs](09-Governance-Metrics.md) | Measurable KPIs: vibecoding index, gate pass rate, evidence coverage |

### SASE & Agentic Governance (Ring 1 — timeless principles)

| # | Document | Purpose |
|---|----------|---------|
| 13 | [Agentic Core Principles](13-AGENTIC-CORE-PRINCIPLES.md) | SE4H/SE4A model, 7 SASE principles, 6 disciplines. **Section 8 (NEW 6.2.1)**: Agent Task Terminal Status Taxonomy (DONE/DONE_WITH_CONCERNS/BLOCKED/NEEDS_CONTEXT) |
| 14 | [Agentic Maturity Model](14-AGENTIC-MATURITY-MODEL.md) | L0-L3 maturity levels, AGENTS.md standard |
| 16 | [Long-Running Agent Protocol](16-LONG-RUNNING-AGENT-PROTOCOL.md) | **NEW 6.2.0** — Checkpoint, memory, handoff, human checkpoints |

### New Pillars (6.3.0 Draft — validated by SDLC Orchestrator v2)

| # | Document | Purpose |
|---|----------|---------|
| 17 | [Agentic OS Patterns](17-AGENTIC-OS-PATTERNS.md) | 12/18 production-verified patterns from 513K LOC Claude Code |
| 18 | [LLM Model Strategy](18-LLM-MODEL-STRATEGY.md) | 3-tier cascade standard (Claude Code → OpenAI → Ollama) |
| 19 | [Federated Platform Standard](19-FEDERATED-PLATFORM-STANDARD.md) | BRAIN/VOICE/HANDS/ADVISOR boundaries + V2 Independence |
| 20 | [Evidence Integration Standard](20-EVIDENCE-INTEGRATION-STANDARD.md) | Multi-source ingestion, no source preference |

### Moved to Ring 2 (6.2.0 — implementation patterns, not timeless principles)

| # | Old Location | New Location | Reason |
|---|-------------|-------------|--------|
| 10 | ~~10-CLAUDE-MD-STANDARD.md~~ | `05-Templates-Tools/03-Agent-Templates/CLAUDE-MD-STANDARD.md` | Tool-specific (Claude) |
| 11 | ~~11-AUTONOMOUS-CODEGEN-PATTERNS.md~~ | `07-Implementation-Guides/AUTONOMOUS-CODEGEN-PATTERNS.md` | Implementation pattern |
| 12 | ~~12-MULTI-AGENT-PATTERNS.md~~ | `07-Implementation-Guides/MULTI-AGENT-PATTERNS.md` | Implementation pattern |
| 15 | ~~15-CONVERSATION-FIRST-GOVERNANCE.md~~ | `07-Implementation-Guides/CONVERSATION-FIRST-GOVERNANCE.md` | Interface-specific |

> Redirect stubs remain at old locations until September 2026.

---

## Relationship to Automation Tools

These principles are **methodology** (Framework layer). Automation tools MAY enforce them:

```
Framework (this section)          Automation Tool (any implementation)
═══════════════════════           ═══════════════════════════════════
Principle 1: Collaboration   →   Human review gates
Principle 2: Accountability  →   Immutable audit trail
Principle 3: Planning Mode   →   Risk classifier + planning artifact check
Principle 4: Verification    →   TDD evidence + test coverage delta
Principle 5: Context Mgmt    →   Context file management (AGENTS.md)
Principle 6: Tool Evaluation →   Tool evaluation scorecard
Principle 7: Anti-Patterns   →   Policy-as-code detection rules
Decision Matrix (doc 08)     →   Gate action computation
Metrics (doc 09)             →   Governance metrics dashboard
```

**Key invariant**: Teams can follow these principles **manually** without any automation tool. Automation makes enforcement automatic and auditable — but the principles stand on their own.

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
| Agent Accountability | Production platform lessons | v5.0.0 | Legal/compliance requirement |
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
- [SDLC-Agentic-Core-Principles.md](./13-AGENTIC-CORE-PRINCIPLES.md) - SE4H/SE4A model
- [best-practices-2026/](../04-AI-TOOLS-LANDSCAPE/best-practices-2026/) - Tool-specific guides

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: February 16, 2026
**Framework**: SDLC 6.2.1
