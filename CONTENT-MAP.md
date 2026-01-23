# SDLC Framework 5.2.0 Content Map

**Version**: 5.2.0
**Status**: ACTIVE
**Date**: January 22, 2026
**Purpose**: Single source of truth for topic → canonical file mapping

---

## Overview

This document prevents content duplication and guides redirects during Framework restructuring.
Before creating any new document, check if a canonical file already exists for the topic.

---

## Topic → Canonical File Mapping

### Core Principles (03-AI-GOVERNANCE/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AI-Human Collaboration | `03-AI-GOVERNANCE/01-AI-Human-Collaboration.md` | — | ACTIVE |
| Agent Accountability | `03-AI-GOVERNANCE/02-Agent-Accountability.md` | — | ACTIVE |
| Planning Mode Principle | `03-AI-GOVERNANCE/03-Planning-Mode-Principle.md` | `1-AI-Tools/ai-agent-best-practices-2026/01-planning-mode.md` | ACTIVE |
| Verification Principle | `03-AI-GOVERNANCE/04-Verification-Principle.md` | — | ACTIVE |
| Context Management | `03-AI-GOVERNANCE/05-Context-Management.md` | `1-AI-Tools/ai-agent-best-practices-2026/05-memory-context-management.md` | ACTIVE |
| Tool Evaluation Criteria | `03-AI-GOVERNANCE/06-Tool-Evaluation-Criteria.md` | — | ACTIVE |
| AI Anti-Patterns | `03-AI-GOVERNANCE/07-Anti-Patterns.md` | — | ACTIVE |

### Core Methodology (02-Core-Methodology/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| 10-Stage Lifecycle | `02-Core-Methodology/SDLC-Core-Methodology.md` | Legacy versions in 99-Legacy/ | ACTIVE |
| Design Thinking | `02-Core-Methodology/SDLC-Design-Thinking-Principles.md` | Multiple legacy versions | ACTIVE |
| Agentic Principles | `02-Core-Methodology/SDLC-Agentic-Core-Principles.md` | — | ACTIVE |
| Quality Gates | `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates.md` | — | ACTIVE |
| Security Gates | `02-Core-Methodology/Governance-Compliance/SDLC-Security-Gates.md` | — | ACTIVE |
| Sprint Planning Governance | `02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Planning-Governance.md` | — | ACTIVE |

### Templates (05-Templates-Tools/SASE-Artifacts/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AGENTS.md Template | `05-Templates-Tools/SASE-Artifacts/AGENTS-MD-Template.md` | — | ACTIVE |
| CRP (Consultation Request) | `05-Templates-Tools/SASE-Artifacts/04-CRP-Template.md` | — | ACTIVE |
| MRP (Merge-Readiness Pack) | `05-Templates-Tools/SASE-Artifacts/05-MRP-Template.md` | — | ACTIVE |
| VCR (Version Controlled Resolution) | `05-Templates-Tools/SASE-Artifacts/06-VCR-Template.md` | — | ACTIVE |
| BriefingScript (BRS) | — | `05-Templates-Tools/SASE-Artifacts/01-BriefingScript-Template.yaml` | DEPRECATED |
| LoopScript (LPS) | — | `05-Templates-Tools/SASE-Artifacts/02-LoopScript-Template.yaml` | DEPRECATED |
| MentorScript (MTS) | — | `05-Templates-Tools/SASE-Artifacts/03-MentorScript-Template.md` | DEPRECATED |

### AI Tools Best Practices (05-Templates-Tools/1-AI-Tools/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AI Best Practices Index | `05-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/README.md` | — | ACTIVE |
| Planning Mode (Tool Guide) | `05-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/01-planning-mode.md` | — | ACTIVE |
| Model Selection | `05-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/02-model-selection-matrix.md` | — | ACTIVE |
| Sub-agent Orchestration | `05-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/03-sub-agent-orchestration.md` | — | ACTIVE |
| Prompting Best Practices | `05-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/04-prompting-best-practices.md` | — | ACTIVE |
| Memory & Context | `05-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/05-memory-context-management.md` | — | ACTIVE |
| Permissions & Security | `05-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/06-permissions-security.md` | — | ACTIVE |
| Developer Role Evolution | `05-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/07-developer-role-evolution.md` | — | ACTIVE |

### Implementation Guides (07-Implementation-Guides/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| Code Review Framework | `07-Implementation-Guides/SDLC-Universal-Code-Review-Framework.md` | `1-AI-Tools/code-review/` (partial) | ACTIVE |
| Implementation Guide | `07-Implementation-Guides/SDLC-Implementation-Guide.md` | — | ACTIVE |

### AI Tools Landscape (04-AI-TOOLS-LANDSCAPE/) - NEW

| Topic | Canonical File | Purpose | Status |
|-------|---------------|---------|--------|
| AI Tools Overview | `04-AI-TOOLS-LANDSCAPE/README.md` | Tool landscape for Orchestrator | ACTIVE |
| Claude Code Profile | `04-AI-TOOLS-LANDSCAPE/tool-profiles/claude-code-2026.md` | Primary tool integration | ACTIVE |
| Cursor Profile | `04-AI-TOOLS-LANDSCAPE/tool-profiles/cursor-2026.md` | Secondary tool (IDE-native) | ACTIVE |
| Copilot Profile | `04-AI-TOOLS-LANDSCAPE/tool-profiles/copilot-2026.md` | Limited-use assistant | ACTIVE |
| Capability Matrix | `04-AI-TOOLS-LANDSCAPE/capability-matrix.md` | Tool comparison | ACTIVE |
| MCP Integration Guide | `04-AI-TOOLS-LANDSCAPE/integration-guides/mcp-integration.md` | Protocol onboarding steps | ACTIVE |
| Trend Watch | `04-AI-TOOLS-LANDSCAPE/trend-watch/` | Monthly updates (starting with 2026-01-trends.md) | ACTIVE |

> **Note**: This is OUTER RING content but STRATEGIC for Orchestrator.
> Tool-specific knowledge enables Orchestrator to enforce Core principles.

### Tool-Specific Content (99-Legacy/tool-guides-2026/)

| Topic | Archive Location | Original Location | Status |
|-------|-----------------|-------------------|--------|
| Claude Code Templates | `99-Legacy/tool-guides-2026/claude-code/` | `2-Agent-Templates/claude-code/` | ARCHIVED |
| Cursor Templates | `99-Legacy/tool-guides-2026/cursor/` | `2-Agent-Templates/cursor/` | ARCHIVED |
| Copilot Templates | `99-Legacy/tool-guides-2026/copilot/` | `2-Agent-Templates/copilot/` | ARCHIVED |
| ChatGPT Templates | `99-Legacy/tool-guides-2026/chatgpt/` | `2-Agent-Templates/chatgpt/` | ARCHIVED |
| Gemini Templates | `99-Legacy/tool-guides-2026/gemini/` | `2-Agent-Templates/gemini/` | ARCHIVED |

### Deployment Guides (99-Legacy/deployment-guides-5.1.3/)

| Topic | Archive Location | Purpose | Status |
|-------|-----------------|---------|--------|
| Team Compliance Docs | `99-Legacy/deployment-guides-5.1.3/08-Team-Management/` | BFlow 5.1.3 deployment | ARCHIVED |
| AI Platform Deployment | `99-Legacy/deployment-guides-5.1.3/AI-Platform/` | AI Platform 5.1.3 config | ARCHIVED |

> **Note**: These deployment guides were specific to SDLC 5.1.3 projects.
> For 5.2.0 deployments, adapt the governance docs from 02-Core-Methodology/.

---

## Active Redirect Stubs

| Original Location | Archive Location | Created | Expires |
|-------------------|------------------|---------|---------|
| `2-Agent-Templates/claude-code/` | `99-Legacy/tool-guides-2026/claude-code/` | Jan 2026 | Jul 2026 |
| `2-Agent-Templates/cursor/` | `99-Legacy/tool-guides-2026/cursor/` | Jan 2026 | Jul 2026 |
| `2-Agent-Templates/copilot/` | `99-Legacy/tool-guides-2026/copilot/` | Jan 2026 | Jul 2026 |
| `2-Agent-Templates/chatgpt/` | `99-Legacy/tool-guides-2026/chatgpt/` | Jan 2026 | Jul 2026 |
| `2-Agent-Templates/gemini/` | `99-Legacy/tool-guides-2026/gemini/` | Jan 2026 | Jul 2026 |

---

## Deprecated Artifacts Status

| Artifact | Status | Replacement | Removal Date |
|----------|--------|-------------|--------------|
| BRS (BriefingScript) | DEPRECATED | AGENTS.md "## Task Brief" | July 2026 |
| MTS (MentorScript) | DEPRECATED | AGENTS.md "## Conventions" | July 2026 |
| LPS (LoopScript) | DEPRECATED | AI generates own plans | July 2026 |

---

## Redirect Policy

See [DEPRECATION-POLICY.md](DEPRECATION-POLICY.md) for:
- Redirect stub templates
- Stub retention period (6 months)
- Archive naming conventions

---

## Usage Instructions

### Before Creating New Content

1. Search this document for existing canonical file
2. If found → Link to it, don't duplicate
3. If not found → Add entry here BEFORE creating file
4. Mark status as NEW until file is created

### When Moving Files

1. Update this map with new location
2. Create redirect stub at old location
3. Update all internal links
4. Run CI link checker

### When Archiving

1. Move file to 99-Legacy/ with dated subfolder
2. Create redirect stub at original location
3. Update status to ARCHIVED in this map
4. Stub expires after 6 months

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: January 23, 2026
