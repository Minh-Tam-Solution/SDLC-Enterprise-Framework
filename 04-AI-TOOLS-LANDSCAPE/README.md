# AI Tools Landscape

**Version**: 5.3.0
**Status**: ACTIVE - OUTER RING (STRATEGIC)
**Date**: January 2026
**Purpose**: Track AI coding tools for Orchestrator governance

---

## Overview

This section tracks the **AI coding tools landscape** - a **strategic component** of SDLC Orchestrator.

> **Position in Concentric Circles**: OUTER RING
>
> - Content changes frequently as tools evolve
> - For timeless principles → [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/)
> - But this IS essential for Orchestrator to govern effectively

### Why This Is Strategic (Not Just Reference)

**SDLC Orchestrator's mission**: Govern AI-assisted development.

To govern effectively, Orchestrator MUST:

| Need | This Section Provides |
|------|----------------------|
| **Know the landscape** | Tool categories, vendors, capabilities |
| **Evaluate new tools** | Governance criteria, capability matrix |
| **Integrate tools** | MCP configs, API patterns, integration guides |
| **Anticipate trends** | Emerging patterns, what to promote to Core |
| **Guide teams** | Which tools fit which use cases |

### Dual Purpose

| For Manual SDLC Users | For Orchestrator System |
|----------------------|-------------------------|
| Reference for tool selection | Input for governance rules |
| Best practices by tool | Integration specifications |
| Capability comparison | Feature detection logic |

**This is the "eyes and ears" of SDLC Orchestrator in the AI tools ecosystem.**

### What This Section Contains

| Content | Purpose | Update Frequency |
|---------|---------|------------------|
| [Tool Categories](#tool-categories-january-2026) | Classification of AI coding tools | Quarterly |
| Tool Profiles ([Claude Code](tool-profiles/claude-code-2026.md) · [Cursor](tool-profiles/cursor-2026.md) · [Copilot](tool-profiles/copilot-2026.md)) | Individual tool capabilities | As needed |
| [Capability Matrix](capability-matrix.md) | Feature comparison & readiness score | Quarterly |
| [Best Practices 2026](best-practices-2026/) | AI agent workflows, planning mode, model selection | As needed |
| [Integration Notes](integration-guides/mcp-integration.md) | MCP onboarding playbook | As needed |
| Trend Watch ([Jan 2026](trend-watch/2026-01-trends.md)) | Emerging patterns and features | Monthly |

---

## Tool Categories (January 2026)

### 1. AI Code Assistants (IDE-Integrated)

| Tool | Vendor | Primary Use | Integration |
|------|--------|-------------|-------------|
| **Claude Code** | Anthropic | CLI + IDE | Native MCP |
| **Cursor** | Cursor Inc | Full IDE | Native |
| **GitHub Copilot** | Microsoft/OpenAI | IDE Extension | VS Code, JetBrains |
| **Codeium** | Codeium | IDE Extension | Multi-IDE |
| **Amazon Q** | AWS | IDE + CLI | VS Code, JetBrains |

### 2. Chat-Based AI (Code Generation)

| Tool | Vendor | Primary Use | API Access |
|------|--------|-------------|------------|
| **ChatGPT** | OpenAI | Conversational | Yes |
| **Claude** | Anthropic | Conversational | Yes |
| **Gemini** | Google | Conversational | Yes |
| **DeepSeek** | DeepSeek | Code-focused | Yes |

### 3. Specialized Code Tools

| Tool | Vendor | Specialty | Integration |
|------|--------|-----------|-------------|
| **Devin** | Cognition | Autonomous agent | API |
| **Sweep** | Sweep AI | PR automation | GitHub |
| **Codex** | OpenAI | Code completion | API |
| **Tabnine** | Tabnine | Enterprise completion | Multi-IDE |

---

## Capability Matrix (January 2026)

Full matrix with expanded criteria: [capability-matrix.md](capability-matrix.md)

| Capability | Claude Code | Cursor | Copilot | Codeium |
|------------|-------------|--------|---------|---------|
| Context file (AGENTS.md) | ✅ CLAUDE.md | ✅ .cursorrules | ⚠️ Limited | ⚠️ Limited |
| Multi-file editing | ✅ | ✅ | ⚠️ | ⚠️ |
| Human approval workflow | ✅ | ✅ | ❌ | ❌ |
| Sub-agents/parallel | ✅ | ⚠️ | ❌ | ❌ |
| MCP integration | ✅ Native | ❌ | ❌ | ❌ |
| Extended thinking | ✅ | ⚠️ | ❌ | ❌ |
| Custom commands | ✅ | ✅ | ❌ | ❌ |
| Headless/CI mode | ✅ | ❌ | ✅ | ⚠️ |
| Audit trail | ✅ | ⚠️ | ⚠️ | ⚠️ |

**Legend**: ✅ Full support | ⚠️ Partial/Limited | ❌ Not supported

---

## Governance Evaluation Criteria

When evaluating ANY tool for use with SDLC Orchestrator:

| Criterion | Required? | Description |
|-----------|-----------|-------------|
| Context file support | ✅ MUST | Can read AGENTS.md or equivalent |
| Human approval | ✅ MUST | Requires approval before code changes |
| Quality gate integration | ✅ MUST | Can block on test/lint failure |
| Audit trail | ✅ MUST | Logs actions for compliance |
| Session isolation | ✅ MUST | Changes don't persist unexpectedly |
| API access | NICE | Enables Orchestrator integration |
| MCP/plugin support | NICE | Extensibility for governance tools |

**Full criteria**: See [06-Tool-Evaluation-Criteria.md](../03-AI-GOVERNANCE/06-Tool-Evaluation-Criteria.md)

---

## Orchestrator Integration Status

| Tool | Integration Level | Notes |
|------|-------------------|-------|
| **Claude Code** | FULL | Native MCP, context overlay |
| **Cursor** | PARTIAL | Context file, manual gates |
| **Copilot** | MINIMAL | PR-based governance only |
| **ChatGPT** | MINIMAL | Manual workflow |

---

## Best Practices 2026

**NEW in 5.2.0**: AI agent best practices consolidated here (moved from 05-Templates-Tools).

Full guide: [best-practices-2026/README.md](best-practices-2026/README.md)

| Topic | Summary | File |
|-------|---------|------|
| **Planning Mode** | >15 LOC changes require planning first | [01-planning-mode.md](best-practices-2026/01-planning-mode.md) |
| **Model Selection** | Task-appropriate model routing | [02-model-selection-matrix.md](best-practices-2026/02-model-selection-matrix.md) |
| **Sub-agents** | Session management patterns | [03-sub-agent-orchestration.md](best-practices-2026/03-sub-agent-orchestration.md) |
| **Prompting** | Effective AI communication | [04-prompting-best-practices.md](best-practices-2026/04-prompting-best-practices.md) |
| **Context Management** | CLAUDE.md patterns (<60 lines) | [05-memory-context-management.md](best-practices-2026/05-memory-context-management.md) |
| **Security** | Safe AI execution | [06-permissions-security.md](best-practices-2026/06-permissions-security.md) |
| **Developer Role** | SE 3.0 responsibilities | [07-developer-role-evolution.md](best-practices-2026/07-developer-role-evolution.md) |

### Why Best Practices Are Here (Not in 05-Templates-Tools)

> **Concentric Circles Separation**:
> - `04-AI-TOOLS-LANDSCAPE/` = WHAT tools exist + HOW to use them effectively (strategic intel)
> - `05-Templates-Tools/` = Reusable prompts BY STAGE and agent configurations BY ROLE (operational templates)

Best practices are **tool-specific strategic knowledge** (planning mode works with Claude Code, model selection varies by vendor). They belong with tool profiles, not with stage-aligned prompts.

---

## Trend Watch (January 2026)

Detailed monthly briefing: [trend-watch/2026-01-trends.md](trend-watch/2026-01-trends.md)

### Emerging Patterns

1. **MCP (Model Context Protocol)** - Anthropic's standard for tool integration
2. **Agentic workflows** - Multi-step autonomous execution
3. **Context windows expanding** - 200K+ tokens becoming standard
4. **Reasoning models** - o1, DeepSeek R1 with thinking traces
5. **Local models** - Ollama, LM Studio for privacy-sensitive work

### Patterns Promoted to Core (v5.2.0)

These patterns proved universal and were promoted to [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/):

| Pattern | Source | Promoted As |
|---------|--------|-------------|
| Context file (<60 lines) | CLAUDE.md, .cursorrules | 05-Context-Management.md |
| Risk-based planning | Claude Code best practices | 03-Planning-Mode-Principle.md |
| TDD with AI | Multiple tools | 04-Verification-Principle.md |
| Human-in-loop | Universal | 01-AI-Human-Collaboration.md |

---

## Directory Structure

```
04-AI-TOOLS-LANDSCAPE/
├── README.md                    # This file (overview)
├── tool-profiles/               # Individual tool docs (WHAT tools can do)
│   ├── claude-code-2026.md
│   ├── cursor-2026.md
│   └── copilot-2026.md
├── best-practices-2026/         # ⭐ AI agent workflows (HOW to use effectively)
│   ├── README.md                # Overview of 2026 best practices
│   ├── 01-planning-mode.md      # Pre-implementation pattern extraction
│   ├── 02-model-selection-matrix.md  # Task-appropriate model routing
│   ├── 03-sub-agent-orchestration.md # Session management patterns
│   ├── 04-prompting-best-practices.md # Effective AI communication
│   ├── 05-memory-context-management.md # CLAUDE.md patterns
│   ├── 06-permissions-security.md # Safe AI execution
│   └── 07-developer-role-evolution.md # SE 3.0 responsibilities
├── capability-matrix.md         # Detailed comparison
├── integration-guides/          # Orchestrator integration
│   └── mcp-integration.md
└── trend-watch/                 # Monthly updates
    └── 2026-01-trends.md
```

---

## Update Policy

| Content | Update Trigger | Owner |
|---------|----------------|-------|
| Tool profiles | Major version release | PM |
| Best practices | Expert workflow changes, new patterns | Tech Lead |
| Capability matrix | Quarterly review | Tech Lead |
| Trend watch | Monthly | CTO Office |
| Integration guides | As implemented | DevOps |

---

## Relationship to Core & Orchestrator

```
┌─────────────────────────────────────────────────────────────┐
│  SDLC ORCHESTRATOR (Automation Platform)                    │
│  • Implements governance rules                              │
│  • Integrates with tools via MCP/API                       │
│  • Uses this section for tool-specific logic               │
└─────────────────────────────────────────────────────────────┘
         │                              │
         │ Implements                   │ Reads tool capabilities
         ↓                              ↓
┌─────────────────────────────────────────────────────────────┐
│  03-AI-GOVERNANCE/ (CORE - Timeless Principles)            │
│  • Apply to ALL tools                                       │
│  • Rarely changes                                           │
│  • Prescriptive rules                                       │
└─────────────────────────────────────────────────────────────┘
         ↑
         │ Patterns promoted when proven universal
         │
┌─────────────────────────────────────────────────────────────┐
│  04-AI-TOOLS-LANDSCAPE/ (OUTER RING - Strategic Intel)     │
│  • Tracks specific tools & capabilities                    │
│  • Changes frequently (tool evolution)                     │
│  • Descriptive (what tools CAN do)                         │
│  • Input for Orchestrator integration decisions            │
└─────────────────────────────────────────────────────────────┘
```

### Key Insight

> **Framework principles are universal. But Orchestrator needs tool-specific knowledge to ENFORCE those principles.**
>
> Example: Principle says "require human approval". But HOW to enforce differs:
> - Claude Code: Check session approval flag via MCP
> - Cursor: Verify .cursorrules loaded
> - Copilot: PR review gate only
>
> This section provides the tool-specific knowledge Orchestrator needs.

---

## Related Documents

- [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) - Timeless principles (Core)
- [06-Tool-Evaluation-Criteria.md](../03-AI-GOVERNANCE/06-Tool-Evaluation-Criteria.md) - How to evaluate
- [CONTENT-MAP.md](../CONTENT-MAP.md) - Topic → file mapping
- [99-ARCHIVE/tool-guides-2026/](../99-ARCHIVE/tool-guides-2026/) - Archived tool templates

---

**Document Status**: ACTIVE - OUTER RING
**Owner**: CTO Office
**Last Updated**: January 2026
