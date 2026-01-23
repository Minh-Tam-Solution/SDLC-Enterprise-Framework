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

### Templates (03-Templates-Tools/SASE-Artifacts/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AGENTS.md Template | `03-Templates-Tools/SASE-Artifacts/AGENTS-MD-Template.md` | — | ACTIVE |
| CRP (Consultation Request) | `03-Templates-Tools/SASE-Artifacts/04-CRP-Template.md` | — | ACTIVE |
| MRP (Merge-Readiness Pack) | `03-Templates-Tools/SASE-Artifacts/05-MRP-Template.md` | — | ACTIVE |
| VCR (Version Controlled Resolution) | `03-Templates-Tools/SASE-Artifacts/06-VCR-Template.md` | — | ACTIVE |
| BriefingScript (BRS) | — | `03-Templates-Tools/SASE-Artifacts/01-BriefingScript-Template.yaml` | DEPRECATED |
| LoopScript (LPS) | — | `03-Templates-Tools/SASE-Artifacts/02-LoopScript-Template.yaml` | DEPRECATED |
| MentorScript (MTS) | — | `03-Templates-Tools/SASE-Artifacts/03-MentorScript-Template.md` | DEPRECATED |

### AI Tools Best Practices (03-Templates-Tools/1-AI-Tools/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AI Best Practices Index | `03-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/README.md` | — | ACTIVE |
| Planning Mode (Tool Guide) | `03-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/01-planning-mode.md` | — | ACTIVE |
| Model Selection | `03-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/02-model-selection-matrix.md` | — | ACTIVE |
| Sub-agent Orchestration | `03-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/03-sub-agent-orchestration.md` | — | ACTIVE |
| Prompting Best Practices | `03-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/04-prompting-best-practices.md` | — | ACTIVE |
| Memory & Context | `03-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/05-memory-context-management.md` | — | ACTIVE |
| Permissions & Security | `03-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/06-permissions-security.md` | — | ACTIVE |
| Developer Role Evolution | `03-Templates-Tools/1-AI-Tools/ai-agent-best-practices-2026/07-developer-role-evolution.md` | — | ACTIVE |

### Implementation Guides (05-Implementation-Guides/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| Code Review Framework | `05-Implementation-Guides/SDLC-Universal-Code-Review-Framework.md` | `1-AI-Tools/code-review/` (partial) | ACTIVE |
| Implementation Guide | `05-Implementation-Guides/SDLC-Implementation-Guide.md` | — | ACTIVE |

### Tool-Specific Content (99-ARCHIVE/tool-guides-2026/)

| Topic | Archive Location | Original Location | Status |
|-------|-----------------|-------------------|--------|
| Claude Code Templates | `99-ARCHIVE/tool-guides-2026/claude-code/` | `2-Agent-Templates/claude-code/` | ARCHIVED |
| Cursor Templates | `99-ARCHIVE/tool-guides-2026/cursor/` | `2-Agent-Templates/cursor/` | ARCHIVED |
| Copilot Templates | `99-ARCHIVE/tool-guides-2026/copilot/` | `2-Agent-Templates/copilot/` | ARCHIVED |
| ChatGPT Templates | `99-ARCHIVE/tool-guides-2026/chatgpt/` | `2-Agent-Templates/chatgpt/` | ARCHIVED |
| Gemini Templates | `99-ARCHIVE/tool-guides-2026/gemini/` | `2-Agent-Templates/gemini/` | ARCHIVED |

---

## Active Redirect Stubs

| Original Location | Archive Location | Created | Expires |
|-------------------|------------------|---------|---------|
| `2-Agent-Templates/claude-code/` | `99-ARCHIVE/tool-guides-2026/claude-code/` | Jan 2026 | Jul 2026 |
| `2-Agent-Templates/cursor/` | `99-ARCHIVE/tool-guides-2026/cursor/` | Jan 2026 | Jul 2026 |
| `2-Agent-Templates/copilot/` | `99-ARCHIVE/tool-guides-2026/copilot/` | Jan 2026 | Jul 2026 |
| `2-Agent-Templates/chatgpt/` | `99-ARCHIVE/tool-guides-2026/chatgpt/` | Jan 2026 | Jul 2026 |
| `2-Agent-Templates/gemini/` | `99-ARCHIVE/tool-guides-2026/gemini/` | Jan 2026 | Jul 2026 |

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

1. Move file to 99-ARCHIVE/ with dated subfolder
2. Create redirect stub at original location
3. Update status to ARCHIVED in this map
4. Stub expires after 6 months

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: January 22, 2026
