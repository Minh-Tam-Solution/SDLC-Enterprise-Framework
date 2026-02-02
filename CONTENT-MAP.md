# SDLC Framework 6.0.2 Content Map

**Version**: 6.0.2
**Status**: ACTIVE
**Date**: February 2, 2026
**Purpose**: Single source of truth for topic → canonical file mapping

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
│  99-Legacy/ - Archived and deprecated content                     │
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
| Context Management | `03-AI-GOVERNANCE/05-Context-Management.md` | `02-AI-Tools/ai-agent-best-practices-2026/05-memory-context-management.md` | ACTIVE |
| Tool Evaluation Criteria | `03-AI-GOVERNANCE/06-Tool-Evaluation-Criteria.md` | — | ACTIVE |
| AI Anti-Patterns | `03-AI-GOVERNANCE/07-Anti-Patterns.md` | — | ACTIVE |

### Core Methodology (02-Core-Methodology/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| 10-Stage Lifecycle | `02-Core-Methodology/SDLC-Core-Methodology.md` | Legacy versions in 99-Legacy/ | ACTIVE |
| Design Thinking | `02-Core-Methodology/SDLC-Design-Thinking-Principles.md` | Multiple legacy versions | ACTIVE |
| Agentic Principles | `02-Core-Methodology/SDLC-Agentic-Core-Principles.md` | — | ACTIVE |
| Sprint Governance | `02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md` | Consolidated from Sprint-Planning + Stage-Integration + Change-Management | ACTIVE |
| Quality + Security Gates | `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Security-Gates.md` | Consolidated from Quality-Gates + Security-Gates | ACTIVE |
| Observability Checklist | `02-Core-Methodology/Governance-Compliance/SDLC-Observability-Checklist.md` | — | ACTIVE |
| Naming Standards | `02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md` | Consolidated from Code-File-Naming + Document-Naming + Header-Templates | ACTIVE |
| Team Collaboration | `02-Core-Methodology/Documentation-Standards/SDLC-Team-Collaboration.md` | Consolidated from Team-Collaboration/* folder | ACTIVE |
| **Stage Dependencies** | `02-Core-Methodology/SDLC-Stage-Dependencies.md` | Renamed from ADR-041 | **NEW 5.3.0** |
| **Quality Assurance System** | `02-Core-Methodology/SDLC-Quality-Assurance-System.md` | — | **NEW 5.3.0** |
| **Context Authority** | `02-Core-Methodology/SDLC-Context-Authority-Methodology.md` | Moved from 05-Templates-Tools/01-Specification-Standard/ | **NEW 6.0.2** |

### Templates (05-Templates-Tools/04-SASE-Artifacts/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AGENTS.md Template | `05-Templates-Tools/04-SASE-Artifacts/AGENTS-MD-Template.md` | — | ACTIVE |
| CRP (Consultation Request) | `05-Templates-Tools/04-SASE-Artifacts/01-CRP-Template.md` | Renamed from 04-CRP | ACTIVE |
| MRP (Merge-Readiness Pack) | `05-Templates-Tools/04-SASE-Artifacts/02-MRP-Template.md` | Renamed from 05-MRP | ACTIVE |
| VCR (Version Controlled Resolution) | `05-Templates-Tools/04-SASE-Artifacts/03-VCR-Template.md` | Renamed from 06-VCR | ACTIVE |
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
| **Stage Consistency Validation** | `05-Templates-Tools/01-Specification-Standard/SPEC-0021-Stage-Consistency-Validation.md` | 4-stage consistency validation service | **NEW 6.0.1** |

### E2E API Testing Templates (05-Templates-Tools/02-AI-Tools/) - NEW in 6.0.2

| Topic | Canonical File | Purpose | Status |
|-------|---------------|---------|--------|
| **E2E API Testing Workflow** | `05-Templates-Tools/02-AI-Tools/testing_e2e-api-testing-workflow.md` | 6-phase standardized E2E testing workflow | **NEW 6.0.2** |
| **Security Testing Checklist** | `05-Templates-Tools/02-AI-Tools/testing_security-testing-checklist.md` | OWASP API Top 10 (2023) checklist | **NEW 6.0.2** |
| **Stage Cross-Reference Matrix** | `02-Core-Methodology/SDLC-Stage-Cross-Reference.md` | Bidirectional Stage 03 ↔ 05 traceability | **NEW 6.0.2** |
| **Testing Artifacts Structure** | `02-Core-Methodology/Documentation-Standards/SDLC-Testing-Artifacts-Structure.md` | SDLC-compliant test folder layout | **NEW 6.0.2** |

> **Note**: RFC-SDLC-602 introduces standardized E2E API testing with OWASP security integration and cross-stage traceability.

| OpenSpec Analysis | `99-Legacy/OpenSpec-Analysis-2026/OpenSpec-Analysis.md` | Week 8 Gate decision (EXTEND approved) | ARCHIVED |
| Migration Plan (20 Specs) | `99-Legacy/OpenSpec-Analysis-2026/MIGRATION-PLAN-20-SPECS.md` | Priority specs for conversion | ARCHIVED |
| Conversion Layer Spec | `99-Legacy/OpenSpec-Analysis-2026/CONVERSION-LAYER-SPECIFICATION.md` | `sdlcctl spec convert` command | ARCHIVED |
| Week 8 Gate Decision Brief | `99-Legacy/OpenSpec-Analysis-2026/WEEK-8-GATE-CTO-DECISION-BRIEF.md` | CEO APPROVED (Jan 28) | ARCHIVED |
| Week 8 Gate Comparison Matrix | `99-Legacy/OpenSpec-Analysis-2026/WEEK-8-GATE-COMPARISON-MATRIX.md` | Executive summary | ARCHIVED |

> **Note**: Framework 6.0.2 introduces BREAKING CHANGES - new specs MUST use YAML frontmatter and BDD format.

### AI Agent Best Practices (04-AI-TOOLS-LANDSCAPE/best-practices-2026/) - MOVED

> **MOVED in 5.2.0**: Best practices moved from `05-Templates-Tools/02-AI-Tools/` to `04-AI-TOOLS-LANDSCAPE/`
> **Reason**: Concentric Circles separation - best practices are strategic intel, not templates

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| AI Best Practices Index | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/README.md` | `05-Templates-Tools/02-AI-Tools/ai-agent-best-practices-2026/` | ACTIVE |
| Planning Mode (Tool Guide) | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/01-planning-mode.md` | — | ACTIVE |
| Model Selection | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/02-model-selection-matrix.md` | — | ACTIVE |
| Sub-agent Orchestration | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/03-sub-agent-orchestration.md` | — | ACTIVE |
| Prompting Best Practices | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/04-prompting-best-practices.md` | — | ACTIVE |
| Memory & Context | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/05-memory-context-management.md` | — | ACTIVE |
| Permissions & Security | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/06-permissions-security.md` | — | ACTIVE |
| Developer Role Evolution | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/07-developer-role-evolution.md` | — | ACTIVE |

### Implementation Guides (07-Implementation-Guides/)

| Topic | Canonical File | Redirects From | Status |
|-------|---------------|----------------|--------|
| Code Review Framework | `07-Implementation-Guides/SDLC-Universal-Code-Review-Framework.md` | `02-AI-Tools/code-review/` (partial) | ACTIVE |
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
| Claude Code Templates | `99-Legacy/tool-guides-2026/claude-code/` | `03-Agent-Templates/claude-code/` | ARCHIVED |
| Cursor Templates | `99-Legacy/tool-guides-2026/cursor/` | `03-Agent-Templates/cursor/` | ARCHIVED |
| Copilot Templates | `99-Legacy/tool-guides-2026/copilot/` | `03-Agent-Templates/copilot/` | ARCHIVED |
| ChatGPT Templates | `99-Legacy/tool-guides-2026/chatgpt/` | `03-Agent-Templates/chatgpt/` | ARCHIVED |
| Gemini Templates | `99-Legacy/tool-guides-2026/gemini/` | `03-Agent-Templates/gemini/` | ARCHIVED |

### Deployment Guides (99-Legacy/deployment-guides-5.1.3/)

| Topic | Archive Location | Purpose | Status |
|-------|-----------------|---------|--------|
| Team Compliance Docs | `99-Legacy/deployment-guides-5.1.3/08-Team-Management/` | BFlow 5.1.3 deployment | ARCHIVED |
| AI Platform Deployment | `99-Legacy/deployment-guides-5.1.3/AI-Platform/` | AI Platform 5.1.3 config | ARCHIVED |

> **Note**: These deployment guides were specific to SDLC 5.1.3 projects.
> For 6.0.0 deployments, adapt the governance docs from 02-Core-Methodology/.

### Sprint 117 POC Documents (99-Legacy/Sprint-117-POC/)

| Topic | Archive Location | Purpose | Status |
|-------|-----------------|---------|--------|
| Spec-First POC Validation | `99-Legacy/Sprint-117-POC/SPEC-FIRST-POC-VALIDATION.md` | POC validation report (working doc) | ARCHIVED |

> **Note**: Working documents and drafts are archived here after sprint completion.

---

## Active Redirect Stubs

| Original Location | New/Archive Location | Created | Expires |
|-------------------|----------------------|---------|---------|
| `spec/controls/anti-vibecoding.yaml` | `02-Core-Methodology/Governance-Compliance/anti-vibecoding.yaml` | Jan 29, 2026 | Jul 2026 |
| `spec/gates/gates.yaml` | `02-Core-Methodology/Governance-Compliance/gates.yaml` | Jan 29, 2026 | Jul 2026 |
| `spec/evidence/spec-frontmatter-schema.json` | `05-Templates-Tools/01-Specification-Standard/spec-frontmatter-schema.json` | Jan 29, 2026 | Jul 2026 |
| `spec/VERSIONING.md` | `02-Core-Methodology/SDLC-Schema-Versioning.md` | Jan 29, 2026 | Jul 2026 |
| `docs/SPEC-FIRST-POC-VALIDATION.md` | `99-Legacy/Sprint-117-POC/` | Jan 29, 2026 | Jul 2026 |
| `docs/02-design/01-ADRs/SPEC-0011-*.md` | `05-Templates-Tools/01-Specification-Standard/SPEC-0011-*.md` | Jan 29, 2026 | Jul 2026 |
| `05-Templates-Tools/02-AI-Tools/ai-agent-best-practices-2026/` | `04-AI-TOOLS-LANDSCAPE/best-practices-2026/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/claude-code/` | `99-Legacy/tool-guides-2026/claude-code/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/cursor/` | `99-Legacy/tool-guides-2026/cursor/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/copilot/` | `99-Legacy/tool-guides-2026/copilot/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/chatgpt/` | `99-Legacy/tool-guides-2026/chatgpt/` | Jan 2026 | Jul 2026 |
| `03-Agent-Templates/gemini/` | `99-Legacy/tool-guides-2026/gemini/` | Jan 2026 | Jul 2026 |

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
**Last Updated**: February 1, 2026
