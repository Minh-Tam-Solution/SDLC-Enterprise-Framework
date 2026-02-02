# AI Agent Best Practices 2026
## SDLC 6.0.3 - Software Engineering 3.0

**Version:** 6.0.3
**Status:** ACTIVE - PRODUCTION READY
**Date:** February 2, 2026
**Source:** Expert workflow analysis, Claude Code best practices, ADR-034 learnings, Boris Cherny 10 Tactics
**Framework:** SDLC 6.0.3 (7-Pillar + 2-Section Architecture)

---

## Overview

This guide documents the 2026 best practices for AI-assisted software development based on:
- Expert workflow analysis from production AI coding environments
- Battle-tested patterns from BFlow, NQH-Bot, and MTEP platforms
- Claude Code and other AI coding tool best practices
- SDLC Orchestrator governance requirements

---

## Contents

1. [Planning Mode](01-planning-mode.md) - Pre-implementation pattern extraction
2. [Model Selection Matrix](02-model-selection-matrix.md) - Task-appropriate model routing
3. [Sub-agent Orchestration](03-sub-agent-orchestration.md) - Session management patterns
4. [Git Workflow Patterns](04-git-workflow-patterns.md) - Parallel AI development with worktrees ⭐ NEW
5. [Prompting Best Practices](05-prompting-best-practices.md) - Effective AI communication
6. [Memory & Context Management](06-memory-context-management.md) - CLAUDE.md patterns
7. [Permissions & Security](07-permissions-security.md) - Safe AI execution
8. [Developer Role Evolution](08-developer-role-evolution.md) - SE 3.0 responsibilities

---

## Key Principles

### 1. Planning Mode for Significant Changes

**Threshold:** >15 LOC changes require planning mode

```
┌─────────────────────────────────────────────────────────────────┐
│ PLANNING MODE WORKFLOW                                          │
│                                                                 │
│  1. EXPLORE: Pattern extraction via sub-agents                  │
│     - Similar code search (agentic grep)                        │
│     - Architecture/ADR review                                   │
│     - Test pattern extraction                                   │
│                                                                 │
│  2. SYNTHESIZE: Build implementation plan                       │
│     - Merge patterns from exploration                           │
│     - Identify constraints and dependencies                     │
│     - Estimate scope and impact                                 │
│                                                                 │
│  3. APPROVE: Human review and approval                          │
│     - Present plan for validation                               │
│     - Gather feedback and modifications                         │
│     - Lock approved approach                                    │
│                                                                 │
│  4. EXECUTE: Context-aware implementation                       │
│     - Generate code following patterns                          │
│     - Validate against plan                                     │
│     - Create evidence for audit                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Agentic Grep > RAG

**Key insight:** Direct codebase exploration beats indexed retrieval.

> "Agentic grep (AI-powered code search) > RAG for context retrieval. Direct codebase exploration finds real patterns. RAG can miss context and produce stale results."

**Why agentic grep wins:**
- Real-time pattern discovery
- Context-aware search
- No stale index issues
- Finds actual implementation, not summaries

### 3. Model Selection by Task Type

| Task Type | Model Class | Rationale |
|-----------|-------------|-----------|
| Large features (>50 LOC) | Premium reasoning | Complex multi-file refactoring |
| Small fixes (<15 LOC) | Fast balanced | Quick, accurate targeted changes |
| Architecture & debugging | Alternative provider | Different perspective when stuck |
| Design & creativity | Large context | Synthesis and creative solutions |
| Quick answers | Fast compact | Fastest response time |

### 4. Developer Role Evolution

**2026 Developer Responsibilities:**
- Design feedback loops (not write code)
- Monitor AI output quality
- Extract patterns and update context files
- Make high-level architecture decisions
- Configure tools/skills/MCP servers
- Maintain AGENTS.md/CLAUDE.md

### 5. Effective Prompting

```bash
# ✅ GOOD - Specific, actionable, with context
"Implement OAuth2 authentication for our API.
Use the auth patterns from @src/auth/legacy.js"

# ❌ BAD - Vague, no context
"Can you suggest some changes to improve security?"
```

**Core principles:**
- Be explicit with actions ("Change X" > "Can you suggest...")
- Use @ to include context (@src/utils/auth.js)
- Treat AI as pair programmer, not robot
- Provide explicit context, don't rely on chat history

---

## Quick Reference

### When to Use Planning Mode

| Change Size | Planning Mode | Rationale |
|-------------|---------------|-----------|
| <15 LOC | Optional | Low drift risk |
| 15-50 LOC | Recommended | Moderate drift risk |
| >50 LOC | **Mandatory** | High drift risk, multi-file |
| New feature | **Mandatory** | Pattern consistency required |
| Architecture change | **Mandatory** | Must align with existing decisions |

### When to Use Extended Thinking

**Use for:**
- Architectural decisions
- Complex bugs
- Tradeoff evaluation
- Multi-step implementations

**Skip for:**
- Simple CRUD operations
- Standard implementations
- Quick fixes

### When to Use Sub-agents

**Use for:**
- Complex, focused tasks (testing, reviews)
- Tool restrictions needed
- Context isolation (research, analysis)
- Concurrent execution (parallel checks)

**Avoid for:**
- Simple operations
- Main conversation flow
- Nested delegation (not supported)

---

## Integration with SDLC 5.2.0

### Sprint Planning Governance (Pillar 2)

AI agents should be aware of:
- Current sprint context (G-Sprint gate status)
- Planning hierarchy (ROADMAP → PHASE → SPRINT → BACKLOG)
- 24h documentation enforcement
- Dual-track quality gates (Feature + Sprint)

### Dynamic Context Overlay

```yaml
Context updates by gate:
  G0.2 Pass (Solution Approved):
    → "Design approved. Architecture in docs/arch.md"

  G1 Pass (Legal Validated):
    → "Stage: Build. Unit tests required"

  G3 Pass (Feature Ready):
    → "STRICT MODE. Only bug fixes allowed"

  Security Scan Fails:
    → "BLOCKED: CVE-XXX detected. Fix before proceeding"
```

### Evidence Vault Integration

All AI-generated code requires:
- Planning context as evidence artifact
- Link to code generation evidence
- Complete audit trail: plan → approval → generation → validation

---

## Next Steps

1. Review each guide in this folder for detailed patterns
2. Apply Planning Mode for all significant changes
3. Configure CLAUDE.md with project-specific patterns
4. Set up sub-agents for proactive quality checks
5. Integrate with SDLC Orchestrator gates

---

**Document Status:** ACTIVE - PRODUCTION READY
**Last Updated:** February 2, 2026
**Framework:** SDLC 6.0.3
