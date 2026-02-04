# SDLC 6.0.4 Universal Framework

**Version**: 6.0.4 | **Status**: ACTIVE | **Date**: February 2026

Built BY AI+Human Teams FOR AI+Human Teams

---

## Overview

SDLC 6.0.4 is a **7-Pillar AI+Human Excellence Framework** with:
- **Pillar 0**: Design Thinking Foundation
- **Pillar 1**: 10 Lifecycle Stages (00-09): Foundation → Govern
- **Pillar 2**: Sprint Planning Governance
- **Pillar 3**: 4-Tier Classification (LITE → ENTERPRISE)
- **Pillar 4**: Quality Gates (Dual-Track: Feature + Sprint)
- **Pillar 5**: SASE Integration (SE 3.0)
- **Pillar 6**: Documentation Permanence
- **Section 7**: Quality Assurance System (Anti-Vibecoding)
- **Section 8**: Unified Specification Standard (+ Spec Converter)

**NEW in 6.0.4 (Minor Release - February 8, 2026)**:
- **TDD Workflow Integration**: Test-Driven Development workflow proven effective through Sprint 154 execution
  - RED-GREEN-REFACTOR cycle documentation
  - 113 tests written FIRST, 100% pass rate achieved
  - Validation of test-first approach for AI-assisted development
- **3-Phase Sprint Lifecycle Model**: Enhanced sprint structure for AI+Human collaboration
  - Phase 1: PRE-SPRINT (Design doc validation, G-Sprint gate)
  - Phase 2: EXECUTION (TDD implementation, daily standups)
  - Phase 3: POST-SPRINT (24h documentation, retrospective)
- **Spec Converter Methodology**: Section 8 enhanced with specification conversion patterns
  - SpecIR (Intermediate Representation) for format-agnostic specifications
  - BDD ↔ OpenSpec bidirectional conversion
  - User Story → BDD → OpenSpec conversion chain
  - Import patterns (Jira, Linear, Text)
- **Tier-Aware TDD Requirements**: TDD compliance levels by tier
  - LITE: 70% test coverage (Basic)
  - STANDARD: 85% test coverage (Standard)
  - PROFESSIONAL: 95% test coverage (Advanced)
  - ENTERPRISE: 95%+ with security tests

**From 6.0.3 (Minor Release - February 2, 2026) - FINALIZED**:
- **Boris Cherny Consolidation**: 5 RFC documents (603-607) consolidated into Framework structure
- **Created (2 new files)**:
  - MCP Integration Guide: 6x faster bug triage via Model Context Protocol automation (Slack/GitHub/Jira)
  - Git Workflow Patterns: 2.5x productivity via parallel AI development with git worktrees
- **Enhanced (3 existing files)**:
  - Memory & Context Management: Continuous Learning Protocol (zero repeated bugs, self-improving AI)
  - Sub-agent Orchestration: Research Delegation Pattern (3.3x faster research phase)
  - Visual Documentation Standards: Explanatory documentation with ASCII diagrams (4x faster onboarding)
- **Consolidation Result**: -3 files (5 deleted - 2 created), 0 methodology content loss
- **Metrics Preserved**: 6x, 2.5x, 3.3x, 4x productivity improvements
- **3-Circle Architecture**: Ring 1 (Core standards), Ring 2 (Best practices), Ring 3 (Implementation guides)
- **Tool-Agnostic**: All patterns work with Claude Code, Cursor, Copilot, GPT-4o, Gemini, Ollama
- **Framework-First**: Track 1 methodology complete, Track 2 implementation deferred to Sprint 144 (Orchestrator automation)

**From 6.0.2 (Minor Release - February 2, 2026)**:
- **RFC-SDLC-602: E2E API Testing Enhancement**: Standardized 6-phase E2E testing workflow
- **Stage Cross-Reference Matrix**: Bidirectional Stage 03 ↔ 05 traceability
- **OWASP API Top 10 Checklist**: Complete API security testing coverage (2023)
- **Testing Artifacts Structure**: SDLC-compliant folder layout for test outputs
- **sdlcctl E2E Commands**: `sdlcctl e2e validate`, `sdlcctl e2e cross-reference`, `sdlcctl e2e generate-report`
- **OPA Policy Integration**: e2e_testing_compliance, stage_cross_reference policies
- **4 New Evidence Types**: e2e_test_report, security_test_report, api_coverage_report, cross_reference_validation

**From 6.0.1 (Minor Release)**:
- **SPEC-0021: Stage Consistency Validation**: Formalized 4-stage consistency validation workflow
- **Pre/Post-Implementation Checklists**: Actionable checklists for stage transitions
- **Artifact Integrity Hashing**: SHA256 checksums for post-approval modification detection
- **CLI Validation Commands**: `sdlcctl validate-consistency` for automated checking
- **Tier-Specific Validation**: LITE (basic), STANDARD (moderate), PROFESSIONAL (deep), ENTERPRISE (comprehensive)

**From 6.0.2 (Major Release)**:
- **Unified Specification Standard**: YAML frontmatter, BDD requirements (GIVEN-WHEN-THEN), tier-aware specs
- **DESIGN_DECISIONS.md Template**: Lightweight ADR alternative for sprint-scoped decisions
- **SPEC_DELTA.md Template**: Version change tracking with breaking change documentation
- **Context Authority Methodology**: Dynamic AGENTS.md patterns with 4 zones (Static → Ephemeral)
- **OpenSpec Alignment**: Industry-standard spec-driven development compatibility
- **20 Priority Spec Migration**: Structured migration plan for existing specifications

**From 5.3.0**:
- Stage Dependency Matrix (ADR-041)
- Stage Exit Criteria per tier
- Sprint-Stage Integration
- Quality Assurance System (Vibecoding Index, Progressive Routing)

**From 5.2.0**:
- AI Governance Principles (7 timeless principles)
- Risk-Based Planning Mode
- Concentric Circles Model
- AI Agent Best Practices 2026

**Proven**: BFlow ($43M, 827:1 ROI), NQH-Bot (₫15B+), MTEP (<30 min PaaS)

---

## The 10-Stage Lifecycle

```
┌─────────────────────────────────────────────────────────────────────┐
│  00 FOUNDATION  (WHY?)      Strategic Discovery & Validation        │
│  01 PLANNING    (WHAT?)     Requirements & User Stories             │
│  02 DESIGN      (HOW?)      Architecture & Technical Design         │
│  03 INTEGRATE               API Contracts & Third-party Setup       │
│  04 BUILD                   Development & Implementation            │
│  05 TEST                    Quality Assurance & Validation          │
│  06 DEPLOY                  Release & Deployment                    │
│  07 OPERATE                 Production Operations & Monitoring      │
│  08 COLLABORATE             Team Coordination & Knowledge           │
│  09 GOVERN                  Compliance & Strategic Oversight        │
└─────────────────────────────────────────────────────────────────────┘
```

### Stage → Folder Mapping

| Stage | Name | Folder | Question |
|-------|------|--------|----------|
| 00 | FOUNDATION | `00-foundation/` | WHY? |
| 01 | PLANNING | `01-planning/` | WHAT? |
| 02 | DESIGN | `02-design/` | HOW? |
| 03 | INTEGRATE | `03-integrate/` | How connect? |
| 04 | BUILD | `04-build/` | Building right? |
| 05 | TEST | `05-test/` | Works correctly? |
| 06 | DEPLOY | `06-deploy/` | Ship safely? |
| 07 | OPERATE | `07-operate/` | Running reliably? |
| 08 | COLLABORATE | `08-collaborate/` | Team effective? |
| 09 | GOVERN | `09-govern/` | Compliant? |

---

## 4-Tier Classification

| Tier | Team Size | Required Stages | Documentation |
|------|-----------|-----------------|---------------|
| **LITE** | 1-2 | 00, 01, 02, 04 | README + .env.example |
| **STANDARD** | 3-10 | 00-02, 04-06 | + CLAUDE.md + /docs |
| **PROFESSIONAL** | 10-50 | All 10 stages | + Full ADRs + Compliance |
| **ENTERPRISE** | 50+ | All 10 stages | + Executive Reports + Audit |

---

## Stage Dependencies (NEW in 5.3.0)

### Explicit Prerequisites (ADR-041)

| Stage | Requires | Prerequisite Gate | Parallel OK |
|-------|----------|-------------------|-------------|
| 00-FOUNDATION | — | — | No |
| 01-PLANNING | 00-FOUNDATION | G0.2 | No |
| 02-DESIGN | 01-PLANNING | G1 | No |
| 03-INTEGRATE | 02-DESIGN | G2 | Yes (with 04) |
| 04-BUILD | 02-DESIGN | G2 | Yes (with 03) |
| 05-TEST | 04-BUILD | G3 | No |
| 06-DEPLOY | 05-TEST | G3 | No |
| 07-OPERATE | 06-DEPLOY | G4 | Yes (continuous) |
| 08-COLLABORATE | 01-PLANNING | — | Yes (throughout) |
| 09-GOVERN | 06-DEPLOY | G4 | Yes (early start) |

### Early Start Triggers

Stage 09 (GOVERN) can start as early as Stage 01 if:
- Regulated industry (healthcare, finance)
- SOC 2 / HIPAA / GDPR compliance required
- AI/ML system (AI Governance Principles 1-6 required)

### Skip Decision Trees

See [SDLC-Tier-Stage-Requirements.md](./02-Core-Methodology/Documentation-Standards/SDLC-Tier-Stage-Requirements.md) for:
- Skip risk levels (LOW → CRITICAL)
- Consequence matrix (time saved vs time cost)
- Decision trees for each optional stage

---

## SASE Integration (SE 3.0)

### SE4H vs SE4A

| Aspect | SE4H (Agent Coach) | SE4A (Agent Executor) |
|--------|-------------------|----------------------|
| **Role** | Guide & supervise | Implement intent |
| **Decision** | FINAL (veto power) | NONE (propose only) |
| **Artifacts** | **AGENTS.md**, VCR | CRP, MRP |

> **⚠️ DEPRECATION NOTICE (ADR-029, Jan 2026)**
>
> **MTS (MentorScript)**, **BRS (BriefingScript)**, and **LPS (LearnedPatternsScript)** are **DEPRECATED**.
>
> **Use `AGENTS.md` instead** - the industry standard for AI coding agents (60K+ projects on GitHub).
>
> Migration path:
> - MTS → `AGENTS.md` (## Conventions, ## DO NOT sections)
> - BRS → `AGENTS.md` (## Quick Start, ## Architecture sections)
> - LPS → PR comments via Context Overlay Service (NOT committed to git)
>
> CLI: `sdlcctl agents init` to generate AGENTS.md from project analysis.

### Agentic Maturity Levels

| Level | Name | Characteristic |
|-------|------|----------------|
| **L0** | Tool-Assisted | AI as autocomplete |
| **L1** | Agent-Assisted | Structured handoff |
| **L2** | Structured Agentic | Full SASE workflow |
| **L3** | Lifecycle Agentic | Proactive agents |

### 7 Agentic Principles

1. **AGENTS.md First** - AGENTS.md committed to repo before agent work _(replaces Brief-First)_
2. **Evidence-Based MRP** - 5-point evidence for every merge
3. **Human Accountability** - Human responsible for shipped code
4. **Consultation Protocol** - CRP when agent uncertain
5. **Conventions-as-Code** - Standards in AGENTS.md _(replaces Mentorship-as-Code)_
6. **Dual Workbenches** - ACE for humans, AEE for agents
7. **Gradual Autonomy** - Trust earned L0→L3

---

## Quality Assurance System (NEW in 5.3.0 - Section 7)

### Vibecoding Index

The **Vibecoding Index** (0-100) measures risk that code lacks proper oversight:

```
vibecoding_index = (
    architectural_smell × 0.25 +    # God class, feature envy, shotgun surgery
    abstraction_complexity × 0.15 + # Deep inheritance, interface proliferation
    ai_dependency_ratio × 0.20 +    # AI lines / total lines
    change_surface_area × 0.20 +    # Files, modules, API contracts touched
    drift_velocity × 0.20           # New patterns, naming violations
)
```

### Progressive Routing

| Score | Category | Routing | Action |
|-------|----------|---------|--------|
| 0-30 | 🟢 Green | Auto-Approve | No CEO involvement |
| 31-60 | 🟡 Yellow | Tech Lead | Spot-check recommended |
| 61-80 | 🟠 Orange | CEO Optional | CEO should review |
| 81-100 | 🔴 Red | CEO Mandatory | CEO must approve |

### Auto-Generation Layer

Reduces compliance friction from 30 min → <5 min per PR:

| Generator | Output | Time Saved |
|-----------|--------|------------|
| Intent | IntentDocument from task description | ~15 min |
| Ownership | OwnershipSuggestion from CODEOWNERS/git blame | ~2 min |
| Context | ADR/spec auto-linkage | ~5 min |
| Attestation | Pre-filled from AI session metadata | ~8 min |

### Governance Modes

| Mode | Behavior | Use Case |
|------|----------|----------|
| OFF | No enforcement | Development/debugging |
| WARNING | Log all, block none | Baseline establishment (Week 1) |
| SOFT | Block critical paths only | Gradual rollout (Week 2) |
| FULL | Block all violations | Production enforcement (Week 3+) |

---

## Unified Specification Standard (NEW in 6.0.0 - Section 8)

### SDLC-Specification-Standard.md

Framework 6.0 introduces a **unified specification standard** inspired by OpenSpec:

```yaml
---
# YAML Frontmatter (Required)
spec_id: SPEC-NNNN
spec_name: "Feature Name"
spec_version: "1.0.0"
status: draft | approved | deprecated | superseded
tier: LITE | STANDARD | PROFESSIONAL | ENTERPRISE | ALL
stage: "00-09"
category: functional | technical | security
owner: "team/person"
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
related_adrs: ["ADR-XXX"]
related_specs: ["SPEC-XXX"]
---
```

### BDD Requirements Format

All requirements must use **Gherkin syntax**:

```gherkin
GIVEN a user with valid credentials
  AND the user is not currently logged in
WHEN the user submits login form
  AND MFA verification succeeds
THEN a session token is issued
  AND the user is redirected to dashboard
```

### Design Decisions (Lightweight ADRs)

For sprint-scoped decisions that don't warrant full ADRs:

| Field | Required | Description |
|-------|----------|-------------|
| `decision_id` | ✅ | DD-NNNN |
| `impact` | ✅ | low / medium / high |
| `reversibility` | ✅ | easy / moderate / difficult |
| `options` | ✅ | At least 2 alternatives considered |

### Spec Delta (Version Tracking)

Track changes between specification versions:

| Delta Type | Version Bump | Breaking |
|------------|--------------|----------|
| **Major** | X.0.0 | Yes |
| **Minor** | 0.X.0 | No |
| **Patch** | 0.0.X | No |

### Context Authority (Dynamic AGENTS.md)

SDLC Orchestrator's TRUE MOAT - dynamic context vs static files:

| Zone | Authority | Trigger | Example |
|------|-----------|---------|---------|
| **Static** | Tech Lead | ADR approval | Architecture, conventions |
| **Semi-Dynamic** | PM/Tech Lead | Sprint planning | Phase, goals, assignments |
| **Dynamic** | System | Gate pass/fail | Stage, restrictions, mode |
| **Ephemeral** | AI Assistant | Session start | Task context |

> **Key Insight**: "Static AGENTS.md is guidance. Dynamic AGENTS.md is governance."

---

## Concentric Circles Model (5.2.0)

Framework content is organized by stability:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ┌─────────────────────────────────────────────────────┐     │
│    │         🎯 CORE (Timeless Principles)              │     │
│    │                                                     │     │
│    │    • Design Thinking          • Quality Gates      │     │
│    │    • 10-Stage Lifecycle       • Human Accountability│     │
│    │    • AI Governance Principles • Quality Assurance  │     │
│    └─────────────────────────────────────────────────────┘     │
│                                                                 │
│              📋 GOVERNANCE (Stable Rules)                      │
│              4-Tier, Sprint Planning, Roles, SASE              │
│                                                                 │
│         🔧 OUTER RING (Tool Guides - Changes Often)            │
│         Claude, Cursor, Copilot specific content               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

> **Philosophy**: "Govern tools, don't document them."
> Framework documents timeless principles. Tool-specific content lives in outer ring.

---

## Framework Structure

```
SDLC-Enterprise-Framework/
├── 01-Overview/                  # Executive Summary
├── 02-Core-Methodology/          # CORE CONTENT
│   ├── SDLC-Core-Methodology.md
│   ├── SDLC-Agentic-Core-Principles.md
│   ├── SDLC-Stage-Dependencies.md       # NEW 5.3.0 (ADR-041)
│   ├── SDLC-Stage-Exit-Criteria.md      # NEW 5.3.0
│   ├── SDLC-Quality-Assurance-System.md # NEW 5.3.0 (Section 7)
│   ├── Documentation-Standards/
│   │   └── SDLC-Tier-Stage-Requirements.md  # NEW 5.3.0
│   └── Governance-Compliance/
│       └── SDLC-Stage-Sprint-Integration.md # NEW 5.3.0
├── 03-AI-GOVERNANCE/             # AI GOVERNANCE PRINCIPLES (5.2.0)
│   ├── 01-AI-Human-Collaboration.md
│   ├── 02-Agent-Accountability.md
│   ├── 03-Planning-Mode-Principle.md
│   ├── 04-Verification-Principle.md
│   ├── 05-Context-Management.md
│   ├── 06-Tool-Evaluation-Criteria.md
│   └── 07-Anti-Patterns.md
├── 04-AI-TOOLS-LANDSCAPE/        # AI TOOLS TRACKING (5.2.0 - Outer Ring)
│   ├── tool-profiles/            # Claude Code, Cursor, Copilot profiles
│   ├── integration-guides/       # MCP integration specs
│   ├── capability-matrix.md      # Tool comparison
│   └── trend-watch/              # Monthly tool evolution updates
├── 05-Templates-Tools/           # Templates & Automation
│   ├── SASE-Artifacts/           # CRP, MRP, VCR, AGENTS.md template
│   ├── Framework: 6.0.3** Unified Spec Standard
│   │   ├── SDLC-Specification-Standard.md
│   │   ├── DESIGN_DECISIONS.md
│   │   ├── SPEC_DELTA.md
│   │   ├── CONTEXT_AUTHORITY_METHODOLOGY.md
│   │   ├── OpenSpec-Analysis.md
│   │   └── MIGRATION-PLAN-20-SPECS.md
│   ├── 1-AI-Tools/               # AI prompts by stage
│   ├── 2-Checklists/
│   │   └── Stage-Transition-Checklist.md # NEW 5.3.0
│   └── 3-Manual-Templates/
├── 06-Case-Studies/              # BFlow, NQH-Bot examples
├── 07-Implementation-Guides/     # Rollout guides
├── 08-Training-Materials/
├── 09-Continuous-Improvement/
├── 99-Legacy/                    # Archive (tool-guides, deployment-guides, etc.)
├── CONTENT-MAP.md                # Topic → file mapping (5.2.0)
└── DEPRECATION-POLICY.md         # Redirect rules (5.2.0)
```

---

## Quick Start

### Path 1: Understand (30 min)
1. [Executive Summary](./01-Overview/SDLC-Executive-Summary.md) - Overview
2. [Core Methodology](./02-Core-Methodology/SDLC-Core-Methodology.md) - 10 stages
3. [SASE Principles](./02-Core-Methodology/SDLC-Agentic-Core-Principles.md) - Agentic workflow

### Path 2: Implement (3 hours)
1. Download [AI Tools](./05-Templates-Tools/1-AI-Tools/) or [Manual Templates](./05-Templates-Tools/3-Manual-Templates/)
2. Run 1 feature through 10-stage methodology
3. Setup [Code Review Tier](./07-Implementation-Guides/SDLC-Universal-Code-Review-Framework.md)

### Path 3: Full Rollout (2-3 weeks)
1. Week 1: Team training + framework setup
2. Week 2: First Design Thinking sprint
3. Week 3: INTEGRATE, COLLABORATE, GOVERN setup

---

## Key Documents

**Core**:
- [SDLC-Executive-Summary.md](./01-Overview/SDLC-Executive-Summary.md)
- [SDLC-Core-Methodology.md](./02-Core-Methodology/SDLC-Core-Methodology.md)
- [SDLC-Agentic-Core-Principles.md](./02-Core-Methodology/SDLC-Agentic-Core-Principles.md)
- [AI Governance Principles](./03-AI-GOVERNANCE/) - 7 timeless principles (5.2.0)

**NEW in 5.3.0 (Stage Governance)**:
- [SDLC-Stage-Dependencies.md](./02-Core-Methodology/SDLC-Stage-Dependencies.md) - ADR-041, explicit stage prerequisites
- [SDLC-Stage-Exit-Criteria.md](./02-Core-Methodology/SDLC-Stage-Exit-Criteria.md) - Documentation, evidence, signoff requirements
- [SDLC-Stage-Sprint-Integration.md](./02-Core-Methodology/Governance-Compliance/SDLC-Stage-Sprint-Integration.md) - Multi-stage sprint handling
- [SDLC-Tier-Stage-Requirements.md](./02-Core-Methodology/Documentation-Standards/SDLC-Tier-Stage-Requirements.md) - LITE/PRO/ENTERPRISE guidance
- [Stage-Transition-Checklist.md](./05-Templates-Tools/2-Checklists/Stage-Transition-Checklist.md) - Actionable transition checklists

**NEW in 5.3.0 (Quality Assurance)**:
- [SDLC-Quality-Assurance-System.md](./02-Core-Methodology/SDLC-Quality-Assurance-System.md) - **Section 7: Anti-Vibecoding**
  - Vibecoding Index (0-100 composite score)
  - Progressive Routing (Auto-approve Green → CEO mandatory Red)
  - Auto-Generation Layer (Intent, Ownership, Context, Attestation)
  - Kill Switch Criteria (rejection >80%, latency >500ms, etc.)

**NEW in 6.0.2 (Unified Specification Standard)**:
- [SDLC-Specification-Standard.md](./05-Templates-Tools/Framework-6.0/SDLC-Specification-Standard.md) - **Section 8: Unified Spec Format**
  - YAML frontmatter (spec_id, tier, stage, category)
  - BDD requirements format (GIVEN-WHEN-THEN)
  - Acceptance criteria tables
  - ADR linking requirements
- [DESIGN_DECISIONS.md](./05-Templates-Tools/Framework-6.0/DESIGN_DECISIONS.md) - Lightweight ADR alternative
  - Sprint-scoped decisions
  - Options analysis (pros/cons/effort)
  - Escalation rules to full ADR
- [SPEC_DELTA.md](./05-Templates-Tools/Framework-6.0/SPEC_DELTA.md) - Version change tracking
  - Breaking change documentation
  - Migration guides
  - CI/CD integration patterns
- [CONTEXT_AUTHORITY_METHODOLOGY.md](./05-Templates-Tools/Framework-6.0/CONTEXT_AUTHORITY_METHODOLOGY.md) - Dynamic AGENTS.md
  - 4 context zones (Static → Ephemeral)
  - Gate-triggered updates
  - Governance mode injection
- [OpenSpec-Analysis.md](./05-Templates-Tools/Framework-6.0/OpenSpec-Analysis.md) - Week 8 Gate recommendation
- [MIGRATION-PLAN-20-SPECS.md](./05-Templates-Tools/Framework-6.0/MIGRATION-PLAN-20-SPECS.md) - 20 priority specs for migration

**AI Tools (Outer Ring)**:
- [AI Tools Landscape](./04-AI-TOOLS-LANDSCAPE/) - Tool tracking for Orchestrator (5.2.0)

**Standards**:
- [SDLC-Naming-Standards.md](./02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md) - Naming + Headers
- [SDLC-Team-Collaboration.md](./02-Core-Methodology/Documentation-Standards/SDLC-Team-Collaboration.md) - Team + Escalation
- [SDLC-Quality-Security-Gates.md](./02-Core-Methodology/Governance-Compliance/SDLC-Quality-Security-Gates.md) - Pillar 4+5
- [SDLC-Sprint-Governance.md](./02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md) - Pillar 2

**Templates**:
- [AGENTS.md Template](./05-Templates-Tools/SASE-Artifacts/AGENTS-MD-Template.md) - **RECOMMENDED** (replaces MTS/BRS/LPS)
- [SASE Artifacts](./05-Templates-Tools/SASE-Artifacts/) - CRP, MRP, VCR _(MTS/BRS/LPS deprecated)_
- [AI Tools](./05-Templates-Tools/1-AI-Tools/) - AI prompts

**Implementation**:
- [SDLC-Implementation-Guide.md](./07-Implementation-Guides/SDLC-Implementation-Guide.md)
- [SDLC-Universal-Code-Review-Framework.md](./07-Implementation-Guides/SDLC-Universal-Code-Review-Framework.md)

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
| **6.0.4** | **Feb 8, 2026** | **MINOR: TDD Integration + Sprint 3-Phase Model + Spec Converter** - TDD Workflow Integration proven through Sprint 154 (113 tests, 100% pass rate, RED-GREEN-REFACTOR validated). 3-Phase Sprint Lifecycle Model (PRE-SPRINT, EXECUTION, POST-SPRINT) with enhanced design doc validation. Spec Converter Methodology adds SpecIR intermediate representation, BDD ↔ OpenSpec bidirectional conversion, User Story → BDD chain, Jira/Linear import patterns. Tier-Aware TDD Requirements (LITE 70%, STANDARD 85%, PROFESSIONAL/ENTERPRISE 95%+). Sprint 154 Track 2 completion. |
| **6.0.3** | **Feb 2, 2026** | **MINOR: Boris Cherny Consolidation (FINALIZED)** - Consolidated 5 RFC documents (603-607) into Framework structure following 3-Circle Architecture. **Created**: MCP Integration Guide (6x faster bug triage), Git Workflow Patterns (2.5x productivity via worktrees). **Enhanced**: Memory & Context Management (Continuous Learning Protocol), Sub-agent Orchestration (Research Delegation 3.3x faster), Visual Documentation Standards (4x faster onboarding). **Result**: -3 files (better organization), 0 methodology content loss, 100% Framework-First compliance. **Metrics preserved**: 6x, 2.5x, 3.3x, 4x productivity improvements. Tool-agnostic patterns work with Claude Code, Cursor, Copilot, GPT-4o, Gemini, Ollama. Sprint 143 Track 1 completion. |
| **6.0.2** | **Feb 2, 2026** | **MINOR: E2E API Testing Enhancement** - RFC-SDLC-602 introduces standardized 6-phase E2E testing workflow, Stage Cross-Reference Matrix (Stage 03 ↔ 05 bidirectional traceability), OWASP API Security Top 10 checklist (2023), Testing Artifacts Structure (SDLC-compliant folders), sdlcctl E2E commands (validate, cross-reference, generate-report), OPA policy integration, 4 new Evidence types (e2e_test_report, security_test_report, api_coverage_report, cross_reference_validation). Addresses API testing gaps and SSOT validation. Sprint 139-141 completion. |
| **6.0.1** | **Feb 1, 2026** | **MINOR: Stage Consistency Validation** - SPEC-0021 formalizes proven 4-stage consistency validation workflow (Stage 01 PLANNING ↔ Stage 02 DESIGN ↔ Stage 03 INTEGRATE ↔ Stage 04 BUILD). Includes pre/post-implementation checklists, artifact integrity hashing (SHA256), CLI validation commands, CI/CD integration patterns, tier-specific validation depths. Addresses "spec drift" where implementation diverges from approved designs. Sprint 134 completion. |
| **6.0.0** | **Jan 28, 2026** | **MAJOR: Unified Specification Standard (Section 8)** - YAML frontmatter requirement, BDD requirements format, DESIGN_DECISIONS.md template (lightweight ADRs), SPEC_DELTA.md template (version tracking), Context Authority Methodology (dynamic AGENTS.md with 4 zones), OpenSpec alignment analysis, 20 priority spec migration plan. Breaking: All new specs must use unified format. |
| 5.3.0 | Jan 28, 2026 | **Stage Dependency Matrix + Quality Assurance System** - Explicit stage dependencies (ADR-041), Stage Exit Criteria, Sprint-Stage Integration, Tier-Specific Requirements, Stage Transition Checklists, Quality Assurance System (Section 7 - Anti-Vibecoding: Vibecoding Index, Progressive Routing, Auto-Generation Layer, Kill Switch) |
| 5.2.0 | Jan 22, 2026 | **Principle-Centric Restructuring** - AI Governance Principles, Risk-Based Planning, Concentric Circles Model, CONTENT-MAP.md, DEPRECATION-POLICY.md |
| 5.1.3 | Jan 18, 2026 | **Sprint Planning Governance** - G-Sprint/G-Sprint-Close gates, Roadmap Change Control, 10 Golden Rules |
| 5.1.2 | Dec 24, 2025 | Quality Gates enhancement, Change Management update |
| 5.1.1 | Dec 12, 2025 | Correct stage numbering, Legacy/Archive folder skip |
| 5.1.0 | Dec 11, 2025 | SASE integration, Stage 03 INTEGRATE repositioned |
| 5.0.0 | Dec 5, 2025 | 4-Tier Classification, Governance standards |
| 4.9.0 | Nov 13, 2025 | 10-Stage lifecycle |
| 4.8.0 | Nov 7, 2025 | Design Thinking foundation |

---

**Owner**: CPO Office (taidt@mtsolution.com.vn)
**Authority**: CTO Approved
