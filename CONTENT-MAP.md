# SDLC Framework 6.2.0 Content Map

**Version**: 6.2.0
**Status**: ACTIVE
**Date**: March 18, 2026
**Purpose**: Single source of truth for topic → canonical file mapping (RFC-001: Legacy Document Organization)

---

## Overview

This document prevents content duplication and guides redirects during Framework restructuring.
Before creating any new document, check if a canonical file already exists for the topic.

---

## 3-Ring Architecture (Concentric Circles)

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│  RING 1: CORE (01-03) - Timeless Methodology                     │
│  ├── 01-Overview/ - Framework introduction                        │
│  ├── 02-Core-Methodology/ - 10-Stage lifecycle, governance       │
│  │   └── Governance-Compliance/*.yaml - Machine-readable specs   │
│  └── 03-AI-GOVERNANCE/ - 7 AI principles                         │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  RING 2: GOVERNANCE (04-05) - Stable Rules & Templates           │
│  ├── 04-AI-TOOLS-LANDSCAPE/ - Tool profiles, best practices      │
│  └── 05-Templates-Tools/ - Specifications, SASE artifacts        │
│      └── 01-Specification-Standard/*.json - JSON Schema          │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  RING 3: OUTER (06-09) - Implementation & Training               │
│  ├── 06-Case-Studies/ - Real-world examples                      │
│  ├── 07-Implementation-Guides/ - How-to guides                   │
│  ├── 08-Training-Materials/ - Onboarding, workshops              │
│  └── 09-Continuous-Improvement/ - Feedback, iteration            │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ARCHIVE LAYER (10) - Centralized Legacy (RFC-001)               │
│  └── 10-archive/{NN}-Legacy/ - Stage-aligned archive              │
│      (00-Legacy through 09-Legacy for production migration       │
│       04-Historical-Documents, OpenCode-Evaluation, etc.)        │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## Topic → Canonical File Mapping

### Machine-Readable Governance (Ring 1 + Ring 2)

| Topic | Canonical File | Purpose | Status |
|-------|---------------|---------|--------|
| **Schema Versioning** | `02-Core-Methodology/SDLC-Schema-Versioning.md` | Schema versioning strategy | **ACTIVE** |
| **Anti-Vibecoding Controls** | `02-Core-Methodology/Governance-Compliance/anti-vibecoding.yaml` | Quality control definitions | **ACTIVE** |
| **Quality Gates YAML** | `02-Core-Methodology/Governance-Compliance/gates.yaml` | G0-G4 gate requirements | **ACTIVE** |
| **Spec Frontmatter Schema** | `05-Templates-Tools/01-Specification-Standard/spec-frontmatter-schema.json` | YAML frontmatter validation | **ACTIVE** |

> **Note**: Machine-readable specs are distributed across rings based on their purpose:
> - Ring 1: Core governance rules (controls, gates, versioning)
> - Ring 2: Template validation schemas

### Core Principles (03-AI-GOVERNANCE/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AI-Human Collaboration | `03-AI-GOVERNANCE/01-AI-Human-Collaboration.md` | — | ACTIVE |
| Agent Accountability | `03-AI-GOVERNANCE/02-Agent-Accountability.md` | — | ACTIVE |
| Planning Mode Principle | `03-AI-GOVERNANCE/03-Planning-Mode-Principle.md` | `02-AI-Tools/ai-agent-best-practices-2026/01-planning-mode.md` | ACTIVE |
| Verification Principle | `03-AI-GOVERNANCE/04-Verification-Principle.md` | — | ACTIVE |
| Context Management | `03-AI-GOVERNANCE/05-Context-Management.md` | `02-AI-Tools/ai-agent-best-practices-2026/06-memory-context-management.md` | ACTIVE |
| Tool Evaluation Criteria | `03-AI-GOVERNANCE/06-Tool-Evaluation-Criteria.md` | — | ACTIVE |
| AI Anti-Patterns | `03-AI-GOVERNANCE/07-Anti-Patterns.md` | — | ACTIVE |
| **CLAUDE.md Standard (3-Tier)** | `05-Templates-Tools/03-Agent-Templates/CLAUDE-MD-STANDARD.md` (moved to Ring 2 in 6.2.0) | — | **NEW 6.0.6** |
| **Autonomous Codegen Patterns** | `07-Implementation-Guides/AUTONOMOUS-CODEGEN-PATTERNS.md` (moved to Ring 2 in 6.2.0) | — | **NEW 6.0.6** |
| **Multi-Agent Patterns** | `07-Implementation-Guides/MULTI-AGENT-PATTERNS.md` (moved to Ring 2 in 6.2.0) | — | **NEW 6.1.0** |
| **Agentic Core Principles** | `03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` | Moved from `02-Core-Methodology/SDLC-Agentic-Core-Principles.md` | **MOVED 6.1.0** |
| **Agentic Maturity Model** | `03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md` | Moved from `02-Core-Methodology/SDLC-Agentic-Maturity-Model.md` | **MOVED 6.1.0** |
| **Conversation-First Governance** | `07-Implementation-Guides/CONVERSATION-FIRST-GOVERNANCE.md` (moved to Ring 2 in 6.2.0) | Governance-via-conversation patterns (OTT/CLI primary) | **NEW 6.1.2** |

### Core Methodology (02-Core-Methodology/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| 10-Stage Lifecycle | `02-Core-Methodology/SDLC-Core-Methodology.md` | Legacy versions in 10-archive/02-Legacy/ | ACTIVE |
| Design Thinking | `02-Core-Methodology/SDLC-Design-Thinking-Principles.md` | Multiple legacy versions in 10-archive/02-Legacy/ | ACTIVE |
| Agentic Principles | `03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` | Moved from `02-Core-Methodology/` in 6.1.0 | ACTIVE |
| Sprint Governance | `02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md` | Consolidated from Sprint-Planning + Stage-Integration + Change-Management | ACTIVE |
| Quality + Security Gates | `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md` | Consolidated from Quality-Gates + Security-Gates | ACTIVE |
| Observability Checklist | `02-Core-Methodology/Governance-Compliance/SDLC-Observability-Checklist.md` | — | ACTIVE |
| Naming Standards | `02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md` | Consolidated from Code-File-Naming + Document-Naming + Header-Templates | ACTIVE |
| Team Collaboration | `02-Core-Methodology/Documentation-Standards/SDLC-Team-Collaboration.md` | Consolidated from Team-Collaboration/* folder | ACTIVE |
| **Visual Documentation Standards** | `02-Core-Methodology/Documentation-Standards/SDLC-Visual-Documentation-Standards.md` | RFC-SDLC-607 | **NEW 6.0.3** |
| **Stage Dependencies** | `02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md` | Stage prerequisite matrix | **NEW 5.3.0** |
| **Quality Assurance System** | `02-Core-Methodology/SDLC-Quality-Gates-Assurance-Framework.md` | — | **NEW 5.3.0** |
| **Context Authority** | `02-Core-Methodology/SDLC-Context-Authority-Methodology.md` | Moved from 05-Templates-Tools/01-Specification-Standard/ | **NEW 6.0.2** |
| **System Thinking Foundation** | `02-Core-Methodology/SDLC-System-Thinking-Foundation.md` | — | **NEW 6.1.0** |
| **Crisis-to-Pattern Methodology** | `02-Core-Methodology/SDLC-Crisis-To-Pattern-Methodology.md` | Extracted from Design Thinking Principles | **NEW 6.1.0** |
| **Design Thinking Templates** | `02-Core-Methodology/Documentation-Standards/SDLC-Design-Thinking-Templates.md` | Extracted from Design Thinking Principles | **NEW 6.1.0** |
| **MRP Template** | `05-Templates-Tools/06-Manual-Templates/SDLC-MRP-Template.md` | Moved from `02-Core-Methodology/` in 6.1.0 | **NEW 6.0.6** |

### Templates (05-Templates-Tools/04-SASE-Artifacts/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AGENTS.md Template | `05-Templates-Tools/04-SASE-Artifacts/AGENTS-MD-Template.md` | — | ACTIVE |
| CRP (Consultation Request) | `05-Templates-Tools/04-SASE-Artifacts/01-CRP-Template.md` | Renamed from 04-CRP | ACTIVE |
| MRP (Merge-Readiness Pack) | `05-Templates-Tools/04-SASE-Artifacts/02-MRP-Template.md` | Renamed from 05-MRP | ACTIVE |
| VCR (Version Controlled Resolution) | `05-Templates-Tools/04-SASE-Artifacts/03-VCR-Template.md` | Renamed from 06-VCR | ACTIVE |
| **SOULs Index** | `05-Templates-Tools/04-SASE-Artifacts/souls/README.md` | — | **NEW 6.1.2** |
| SOUL-assistant (Router) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-assistant.md` | — | **NEW 6.1.2** |
| SOUL-coder (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-coder.md` | — | **NEW 6.1.2** |
| SOUL-tester (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-tester.md` | — | **NEW 6.1.2** |
| SOUL-architect (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-architect.md` | — | **NEW 6.1.2** |
| SOUL-pm (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-pm.md` | — | **NEW 6.1.2** |
| SOUL-pjm (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-pjm.md` | — | **NEW 6.1.2** |
| SOUL-devops (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-devops.md` | — | **NEW 6.1.2** |
| SOUL-fullstack (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-fullstack.md` | — | **NEW 6.1.2** |
| SOUL-reviewer (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-reviewer.md` | — | **NEW 6.1.2** |
| SOUL-researcher (SE4A) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-researcher.md` | — | **NEW 6.1.2** |
| SOUL-ceo (SE4H) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-ceo.md` | — | **NEW 6.1.2** |
| SOUL-cto (SE4H) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-cto.md` | — | **NEW 6.1.2** |
| SOUL-cpo (SE4H) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-cpo.md` | — | **NEW 6.1.2** |
| SOUL-writer (Optional) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-writer.md` | — | **NEW 6.1.2** |
| SOUL-sales (Optional) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-sales.md` | — | **NEW 6.1.2** |
| SOUL-cs (Optional) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-cs.md` | — | **NEW 6.1.2** |
| SOUL-itadmin (Optional) | `05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-itadmin.md` | — | **NEW 6.1.2** |
| TEAM-dev | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-dev.md` | — | **NEW 6.1.2** |
| TEAM-qa | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-qa.md` | — | **NEW 6.1.2** |
| TEAM-design | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-design.md` | — | **NEW 6.1.2** |
| TEAM-executive | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-executive.md` | — | **NEW 6.1.2** |
| TEAM-fullstack | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-fullstack.md` | — | **NEW 6.1.2** |
| TEAM-ops | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-ops.md` | — | **NEW 6.1.2** |
| TEAM-planning | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-planning.md` | — | **NEW 6.1.2** |
| TEAM-advisory | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-advisory.md` | — | **NEW 6.1.2** |
| TEAM-business | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-business.md` | — | **NEW 6.1.2** |
| TEAM-engineering | `05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-engineering.md` | — | **NEW 6.1.2** |
| BriefingScript (BRS) | — | `05-Templates-Tools/04-SASE-Artifacts/01-BriefingScript-Template.yaml` | DEPRECATED |
| LoopScript (LPS) | — | `05-Templates-Tools/04-SASE-Artifacts/02-LoopScript-Template.yaml` | DEPRECATED |
| MentorScript (MTS) | — | `05-Templates-Tools/04-SASE-Artifacts/03-MentorScript-Template.md` | DEPRECATED |

### Framework 6.0.2 Templates (05-Templates-Tools/01-Specification-Standard/) - NEW in 6.0.0

| Topic | Canonical File | Purpose | Status |
|-------|---------------|---------|--------|
| **Unified Specification Standard** | `05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md` | YAML frontmatter + BDD format | **NEW 6.0.2** |
| **Design Decisions Template** | `05-Templates-Tools/01-Specification-Standard/DESIGN_DECISIONS.md` | Lightweight ADR for sprint decisions | **NEW 6.0.2** |
| **Spec Delta Template** | `05-Templates-Tools/01-Specification-Standard/SPEC_DELTA.md` | Version change tracking | **NEW 6.0.2** |
| **Context Authority Methodology** | `05-Templates-Tools/01-Specification-Standard/CONTEXT_AUTHORITY_METHODOLOGY.md` | Dynamic AGENTS.md (4 zones) | **NEW 6.0.2** |
| **Stage Consistency Validation** | `07-Implementation-Guides/SDLC-Stage-Consistency-Validation-Guide.md` | 4-stage consistency validation (SPEC-0021 moved to Orchestrator) | **NEW 6.0.1** |

### E2E API Testing Templates — ARCHIVED in 6.1.2

> **ARCHIVED (6.1.2)**: 36 AI prompt templates from `05-Templates-Tools/02-AI-Tools/` moved to `10-archive/05-Legacy/ai-tools-templates-sprint173/`. FROZEN since Sprint 173, not integrated. See redirect stub at `05-Templates-Tools/02-AI-Tools/README.md`.

| Topic | Canonical File | Purpose | Status |
|-------|---------------|---------|--------|
| **E2E API Testing Workflow** | `10-archive/05-Legacy/ai-tools-templates-sprint173/testing_e2e-api-testing-workflow.md` | 6-phase standardized E2E testing workflow | **ARCHIVED 6.1.2** |
| **E2E Testing Quickstart** | `07-Implementation-Guides/E2E-TESTING-QUICKSTART.md` | Moved from `05-Templates-Tools/02-AI-Tools/` in 6.1.0 | **MOVED 6.1.0** |
| **E2E API Testing Methodology** | `07-Implementation-Guides/SDLC-E2E-API-Testing-Methodology.md` | Moved from `05-Templates-Tools/02-AI-Tools/` in 6.1.0 | **MOVED 6.1.0** |
| **Security Testing Checklist** | `10-archive/05-Legacy/ai-tools-templates-sprint173/testing_security-testing-checklist.md` | OWASP API Top 10 (2023) checklist | **ARCHIVED 6.1.2** |
| **Stage Cross-Reference Matrix** | `02-Core-Methodology/SDLC-Stage-Cross-Reference.md` | Bidirectional Stage 03 ↔ 05 traceability | **NEW 6.0.2** |
| **Testing Artifacts Structure** | `02-Core-Methodology/Documentation-Standards/SDLC-Testing-Artifacts-Structure.md` | SDLC-compliant test folder layout | **NEW 6.0.2** |

> **Note**: RFC-SDLC-602 templates archived in 6.1.2 (Sprint 173 freeze). Active testing guidance remains in `07-Implementation-Guides/`.

| OpenSpec Analysis | `10-archive/05-Legacy/OpenSpec-Analysis-2026/OpenSpec-Analysis.md` | Week 8 Gate decision (EXTEND approved) | ARCHIVED |
| Migration Plan (20 Specs) | `10-archive/05-Legacy/OpenSpec-Analysis-2026/MIGRATION-PLAN-20-SPECS.md` | Priority specs for conversion | ARCHIVED |
| Conversion Layer Spec | `10-archive/05-Legacy/OpenSpec-Analysis-2026/CONVERSION-LAYER-SPECIFICATION.md` | `sdlcctl spec convert` command | ARCHIVED |
| Week 8 Gate Decision Brief | `10-archive/05-Legacy/OpenSpec-Analysis-2026/WEEK-8-GATE-CTO-DECISION-BRIEF.md` | CEO APPROVED (Jan 28) | ARCHIVED |
| Week 8 Gate Comparison Matrix | `10-archive/05-Legacy/OpenSpec-Analysis-2026/WEEK-8-GATE-COMPARISON-MATRIX.md` | Executive summary | ARCHIVED |

> **Note**: Framework 6.0.0+ introduces BREAKING CHANGES - new specs MUST use YAML frontmatter and BDD format.

### AI Agent Best Practices (04-AI-TOOLS-LANDSCAPE/best-practices-2026/) - MOVED

> **MOVED in 5.2.0**: Best practices moved from `05-Templates-Tools/02-AI-Tools/` to `04-AI-TOOLS-LANDSCAPE/`
> **Reason**: Concentric Circles separation - best practices are strategic intel, not templates

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AI Best Practices Index | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/README.md` | `05-Templates-Tools/02-AI-Tools/ai-agent-best-practices-2026/` | ACTIVE |
| Planning Mode (Tool Guide) | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/01-planning-mode.md` | — | ACTIVE |
| Model Selection | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/02-model-selection-matrix.md` | — | ACTIVE |
| Sub-agent Orchestration | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/03-sub-agent-orchestration.md` | — | ACTIVE (Enhanced 6.0.3) |
| Prompting Best Practices | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/04-prompting-best-practices.md` | — | ACTIVE |
| Memory & Context | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/06-memory-context-management.md` | — | ACTIVE (Enhanced 6.0.3) |
| Permissions & Security | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/07-permissions-security.md` | — | ACTIVE |
| Developer Role Evolution | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/08-developer-role-evolution.md` | — | ACTIVE |
| **Git Workflow Patterns** | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/04-git-workflow-patterns.md` | RFC-SDLC-604 | **NEW 6.0.3** |

### Implementation Guides (07-Implementation-Guides/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| Code Review Guide (SSOT) | `07-Implementation-Guides/SDLC-Code-Review-Guide.md` | Consolidated from 3 guides (Sprint 173) | ACTIVE |
| Implementation Guide | `07-Implementation-Guides/SDLC-Implementation-Guide.md` | — | ACTIVE |
| **MCP Integration Guide** | `07-Implementation-Guides/MCP-Integration-Guide.md` | RFC-SDLC-603 | **NEW 6.0.3** |

### AI Tools Landscape (04-AI-TOOLS-LANDSCAPE/) - NEW

| Topic | Canonical File | Purpose | Status |
|-------|---------------|---------|--------|
| AI Tools Overview | `04-AI-TOOLS-LANDSCAPE/README.md` | Tool landscape for Orchestrator | ACTIVE |
| Claude Code Profile | `04-AI-TOOLS-LANDSCAPE/tool-profiles/claude-code-2026.md` | Reference profile (CLI-based) | ACTIVE |
| Cursor Profile | `04-AI-TOOLS-LANDSCAPE/tool-profiles/cursor-2026.md` | Reference profile (IDE-native) | ACTIVE |
| Copilot Profile | `04-AI-TOOLS-LANDSCAPE/tool-profiles/copilot-2026.md` | Reference profile (inline assist) | ACTIVE |
| Capability Matrix | `04-AI-TOOLS-LANDSCAPE/capability-matrix.md` | Tool comparison | ACTIVE |
| MCP Integration Guide | `04-AI-TOOLS-LANDSCAPE/integration-guides/mcp-integration.md` | Protocol onboarding steps | ACTIVE |
| Trend Watch | `04-AI-TOOLS-LANDSCAPE/trend-watch/` | Monthly updates (starting with 2026-01-trends.md) | ACTIVE |

> **Note**: This is OUTER RING content but STRATEGIC for Orchestrator.
> Tool-specific knowledge enables Orchestrator to enforce Core principles.

### AI Prompt Templates (10-archive/05-Legacy/ai-tools-templates-sprint173/) — ARCHIVED 6.1.2

| Topic | Archive Location | Original Location | Status |
|-------|-----------------|-------------------|--------|
| 36 AI Prompt Templates | `10-archive/05-Legacy/ai-tools-templates-sprint173/` | `05-Templates-Tools/02-AI-Tools/` | **ARCHIVED 6.1.2** |

> **Reason**: FROZEN since Sprint 173 (Feb 2026). Not integrated with Orchestrator. 36 files, ~320 KB. Reactivation requires CPO approval.

### Tool-Specific Content (10-archive/05-Legacy/tool-guides-2026/)

| Topic | Archive Location | Original Location | Status |
|-------|-----------------|-------------------|--------|
| Claude Code Templates | `10-archive/05-Legacy/tool-guides-2026/claude-code/` | `03-Agent-Templates/claude-code/` | ARCHIVED |
| Cursor Templates | `10-archive/05-Legacy/tool-guides-2026/cursor/` | `03-Agent-Templates/cursor/` | ARCHIVED |
| Copilot Templates | `10-archive/05-Legacy/tool-guides-2026/copilot/` | `03-Agent-Templates/copilot/` | ARCHIVED |
| ChatGPT Templates | `10-archive/05-Legacy/tool-guides-2026/chatgpt/` | `03-Agent-Templates/chatgpt/` | ARCHIVED |
| Gemini Templates | `10-archive/05-Legacy/tool-guides-2026/gemini/` | `03-Agent-Templates/gemini/` | ARCHIVED |

### Deployment Guides (10-archive/06-Legacy/deployment-guides-5.1.3/)

| Topic | Archive Location | Purpose | Status |
|-------|-----------------|---------|--------|
| Team Compliance Docs | `10-archive/06-Legacy/deployment-guides-5.1.3/08-collaborate/` | BFlow 5.1.3 deployment | ARCHIVED |
| AI Platform Deployment | `10-archive/06-Legacy/deployment-guides-5.1.3/AI-Platform/` | AI Platform 5.1.3 config | ARCHIVED |

> **Note**: These deployment guides were specific to SDLC 5.1.3 projects.
> For 6.1.0 deployments, adapt the governance docs from 02-Core-Methodology/.

### Sprint 117 POC Documents (10-archive/04-Legacy/Sprint-117-POC/)

| Topic | Archive Location | Purpose | Status |
|-------|-----------------|---------|--------|
| Spec-First POC Validation | `10-archive/04-Legacy/Sprint-117-POC/SPEC-FIRST-POC-VALIDATION.md` | POC validation report (working doc) | ARCHIVED |

> **Note**: Working documents and drafts are archived here after sprint completion.

---

## Active Redirect Stubs

| Original Location | New/Archive Location | Created | Expires |
|-------------------|----------------------|---------|---------|
| `spec/controls/anti-vibecoding.yaml` | `02-Core-Methodology/Governance-Compliance/anti-vibecoding.yaml` | Jan 29, 2026 | Jul 2026 |
| `spec/gates/gates.yaml` | `02-Core-Methodology/Governance-Compliance/gates.yaml` | Jan 29, 2026 | Jul 2026 |
| `spec/evidence/spec-frontmatter-schema.json` | `05-Templates-Tools/01-Specification-Standard/spec-frontmatter-schema.json` | Jan 29, 2026 | Jul 2026 |
| `spec/VERSIONING.md` | `02-Core-Methodology/SDLC-Schema-Versioning.md` | Jan 29, 2026 | Jul 2026 |
| `docs/SPEC-FIRST-POC-VALIDATION.md` | `10-archive/04-Legacy/Sprint-117-POC/` | Jan 29, 2026 | Jul 2026 |
| `docs/02-design/01-ADRs/SPEC-0011-*.md` | `05-Templates-Tools/01-Specification-Standard/SPEC-0011-*.md` | Jan 29, 2026 | Jul 2026 |
| `05-Templates-Tools/02-AI-Tools/ai-agent-best-practices-2026/` | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/` | Jan 2026 | Jul 2026 |
| `07-Implementation-Guides/SDLC-Universal-Code-Review-Framework.md` | `07-Implementation-Guides/SDLC-Code-Review-Guide.md` | Feb 2026 | Aug 2026 |
| `07-Implementation-Guides/SDLC-Manual-Code-Review-Playbook.md` | `07-Implementation-Guides/SDLC-Code-Review-Guide.md` | Feb 2026 | Aug 2026 |
| `07-Implementation-Guides/SDLC-Subscription-Powered-Code-Review-Guide.md` | `07-Implementation-Guides/SDLC-Code-Review-Guide.md` | Feb 2026 | Aug 2026 |
| `02-Core-Methodology/SDLC-Agentic-Core-Principles.md` | `03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` | Feb 2026 | Aug 2026 |
| `02-Core-Methodology/SDLC-Agentic-Maturity-Model.md` | `03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md` | Feb 2026 | Aug 2026 |
| `02-Core-Methodology/SDLC-MRP-Template.md` | `05-Templates-Tools/06-Manual-Templates/SDLC-MRP-Template.md` | Feb 2026 | Aug 2026 |
| `05-Templates-Tools/02-AI-Tools/E2E-TESTING-QUICKSTART.md` | `07-Implementation-Guides/E2E-TESTING-QUICKSTART.md` | Feb 2026 | Aug 2026 |
| `05-Templates-Tools/02-AI-Tools/SDLC-E2E-API-Testing-Methodology.md` | `07-Implementation-Guides/SDLC-E2E-API-Testing-Methodology.md` | Feb 2026 | Aug 2026 |
| `05-Templates-Tools/02-AI-Tools/*.md` (36 templates) | `10-archive/05-Legacy/ai-tools-templates-sprint173/` | Feb 2026 | Aug 2026 |
| `03-Agent-Templates/claude-code/` | `10-archive/05-Legacy/tool-guides-2026/claude-code/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/cursor/` | `10-archive/05-Legacy/tool-guides-2026/cursor/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/copilot/` | `10-archive/05-Legacy/tool-guides-2026/copilot/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/chatgpt/` | `10-archive/05-Legacy/tool-guides-2026/chatgpt/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/gemini/` | `10-archive/05-Legacy/tool-guides-2026/gemini/` | Jan 2026 | Jul 2026 |

---

## Deprecated Artifacts Status

| Artifact | Status | Replacement | Removal Date |
|----------|--------|-------------|--------------|
| BRS (BriefingScript) | DEPRECATED | AGENTS.md "## Task Brief" | July 2026 |
| MTS (MentorScript) | DEPRECATED | AGENTS.md "## Conventions" | July 2026 |
| LPS (LoopScript) | DEPRECATED | AI generates own plans | July 2026 |

### 6.1.0 Consolidation (February 18, 2026)

| Action | Source | Target | Net Effect |
|--------|--------|--------|------------|
| **Slim + Extract** | `SDLC-Design-Thinking-Principles.md` (2,018 lines) | Hub (364 lines) + Templates (572 lines) + Crisis-to-Pattern (280 lines) | −802 lines, 3 focused docs |
| **Slim + Move** | `SDLC-Agentic-Core-Principles.md` (1,313 lines) | `03-AI-GOVERNANCE/13-...` (293 lines) | −1,020 lines, correct ring |
| **Rewrite** | `SDLC-Agentic-Maturity-Model.md` | `03-AI-GOVERNANCE/14-...` (817 lines) | BRS/MTS/LPS → AGENTS.md |
| **Create** | — | `SDLC-System-Thinking-Foundation.md` (230 lines) | New foundational doc |
| **Create** | — | `12-MULTI-AGENT-PATTERNS.md` (450 lines) | Multi-agent collaboration patterns |
| **Move** | `02-Core-Methodology/SDLC-MRP-Template.md` | `05-Templates-Tools/06-Manual-Templates/` | Correct ring |
| **Move** | `05-Templates-Tools/02-AI-Tools/E2E-*` | `07-Implementation-Guides/` | Correct ring |
| **Terminology** | BRS/MTS/LPS refs across SASE templates, Maturity Model | AGENTS.md terminology | 0 stale refs |
| **Version** | 636 stale `6.0.6` references | Updated to `6.1.0` | Consistent versioning |

**Net result**: −1,822 lines from Ring 1 monoliths, +960 lines in focused docs, 0 BRS/MTS/LPS stale refs.

### Boris Cherny Consolidation (6.0.3 - Feb 2, 2026)

| RFC File | Consolidated Into | Content Preserved | Status |
|----------|-------------------|-------------------|--------|
| **RFC-SDLC-603** | `07-Implementation-Guides/MCP-Integration-Guide.md` | ✅ 100% methodology | DELETED |
| **RFC-SDLC-604** | `04-AI-Tools-Landscape/best-practices-2026/04-git-workflow-patterns.md` | ✅ 100% complete | DELETED |
| **RFC-SDLC-605** | `04-AI-Tools-Landscape/best-practices-2026/06-memory-context-management.md` (enhanced) | ✅ 100% methodology | DELETED |
| **RFC-SDLC-606** | `04-AI-Tools-Landscape/best-practices-2026/03-sub-agent-orchestration.md` (enhanced) | ✅ 100% methodology | DELETED |
| **RFC-SDLC-607** | `02-Core-Methodology/Documentation-Standards/SDLC-Visual-Documentation-Standards.md` | ✅ 100% methodology | DELETED |

**Consolidation Metrics**:
- Source: 2,307 lines (5 RFCs)
- Target: ~1,530 lines (2 new + 3 enhanced files)
- Net change: -3 files (5 deleted - 2 created)
- Content loss: 0 methodology lines (Track 2 implementation details omitted per Framework-First principle)

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

### When Archiving (RFC-001, SDLC 6.2.0)

1. Move file to `10-archive/{NN}-Legacy/` with date/context subfolder ({NN} = original stage number)
2. Create redirect stub at original location
3. Update status to ARCHIVED in this map
4. Stub expires after 6 months
5. Example: Design doc from `02-Design/` → `10-archive/02-Legacy/deprecation-2026/`

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: February 18, 2026
