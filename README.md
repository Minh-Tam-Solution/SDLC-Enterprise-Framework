# SDLC 6.3.2 Universal Framework

**Version**: 6.3.1 | **Status**: ACTIVE | **Date**: April 17, 2026

Built BY AI+Human Teams FOR AI+Human Teams

---

> **IMPORTANT: This is a TOOL-AGNOSTIC methodology framework.**
> It defines *what* teams should do (principles, processes, gates) — not *how* a specific tool implements it.
> Any platform can implement this framework. SDLC Orchestrator is ONE such platform, not the only one.
> See [Framework vs. Platform](#framework-vs-platform) for the architectural boundary.

---

## Overview

SDLC 6.3.2 is a **7-Pillar AI+Human Excellence Framework** with:
- **Pillar 0**: Design Thinking Foundation
- **Pillar 1**: 10 Lifecycle Stages (00-09): Foundation → Govern
- **Pillar 2**: Sprint Planning Governance
- **Pillar 3**: 4-Tier Classification (LITE → ENTERPRISE)
- **Pillar 4**: Quality Gates (Dual-Track: Feature + Sprint)
- **Pillar 5**: SASE Integration (SE 3.0)
- **Pillar 6**: Documentation Permanence
- **Section 7**: Quality Assurance System (Anti-Vibecoding)
- **Section 8**: Unified Specification Standard (+ Spec Converter)
- **Section 9**: Legacy Document Organization Standard

**Key capabilities**: Tool-agnostic AI governance, 4-tier classification (LITE→ENTERPRISE), TDD integration, anti-vibecoding quality gates, evidence-based development.

**Proven in production**: Framework đã được công ty NQH/MTS sử dụng để phát triển các platform trong **NQH Technology Ecosystem** (5-layer architecture, 14 platforms — see [vision doc](https://github.com/Minh-Tam-Solution/Bflow-Platform/blob/main/docs/00-foundation/01-vision/nqh-technology-ecosystem-vision.md))

> For detailed version history, see [CHANGELOG.md](./CHANGELOG.md)

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

## Stage Dependencies (added 5.3.0)

### Explicit Prerequisites

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

See [SDLC-Stage-Lifecycle-Framework.md](./02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md) Part 3 for:
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

> **⚠️ DEPRECATION NOTICE (Jan 2026)**
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

## Quality Assurance System (Section 7, added 5.3.0)

### Vibecoding Index

The **Vibecoding Index** (0-100) measures risk that code lacks proper oversight:

```
vibecoding_index = 100 - (
    intent_clarity × 0.30 +         # Clear purpose for every code change
    code_ownership × 0.25 +         # Developer understands generated code
    context_completeness × 0.20 +   # Sufficient context for AI generation
    ai_attestation_rate × 0.15 +    # AI outputs reviewed and attested
    (100 - rejection_rate) × 0.10   # Historical acceptance quality
)
```

### Progressive Routing

| Score | Category | Routing | Action |
|-------|----------|---------|--------|
| <20 | 🟢 Green | Auto-Approve | No CEO involvement |
| 20-40 | 🟡 Yellow | Tech Lead | Spot-check recommended |
| 40-60 | 🟠 Orange | CEO Optional | CEO should review |
| >=60 | 🔴 Red | CEO Mandatory | CEO must approve |

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

## Unified Specification Standard (Section 8, added 6.0.0)

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

The Context Authority pattern defines 4 zones of AI context with different update authorities:

| Zone | Authority | Trigger | Example |
|------|-----------|---------|----------|
| **Static** | Tech Lead | ADR approval | Architecture, conventions |
| **Semi-Dynamic** | PM/Tech Lead | Sprint planning | Phase, goals, assignments |
| **Dynamic** | System (any platform) | Gate pass/fail | Stage, restrictions, mode |
| **Ephemeral** | AI Assistant | Session start | Task context |

> **Key Insight**: "Static AGENTS.md is guidance. Dynamic AGENTS.md is governance."
> Any platform implementing this framework can automate the Dynamic zone (e.g., SDLC Orchestrator, custom CI/CD, other tools).

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
├── 01-Overview/                  # Executive Summary + Quick Reference
├── 02-Core-Methodology/          # CORE CONTENT (Ring 1 — Lean in 6.3.0)
│   ├── SDLC-Core-Methodology.md           # Hub: 7-Pillar + 10-Stage
│   ├── SDLC-Design-Thinking-Principles.md # Pillar 0 (slim, 364 lines)
│   ├── SDLC-System-Thinking-Foundation.md # Pillar 0 (9 Mental Models — #9 added in 6.3.2 Amendment B)
│   ├── SDLC-Ship-Useful-Principle.md      # Operating Principle [DT] (NEW 6.3.2 Amendment B)
│   ├── SDLC-Crisis-To-Pattern-Methodology.md # Pillar 0 (Mental Model #5)
│   ├── SDLC-Stage-Lifecycle-Framework.md  # CONSOLIDATED 6.3.0 (Dependencies + Exit Criteria + Tier Reqs)
│   ├── SDLC-Context-Authority-Methodology.md # Section 8
│   ├── SDLC-SSOT-Principle.md
│   ├── Documentation-Standards/
│   │   ├── SDLC-Naming-Standards.md
│   │   ├── SDLC-Project-Structure-Standard.md
│   │   ├── SDLC-Sprint-Planning-Guide.md
│   │   └── SDLC-Legacy-Document-Organization.md
│   └── Governance-Compliance/
│       ├── SDLC-Sprint-Governance.md      # Pillar 2
│       ├── SDLC-Quality-Gates-Assurance-Framework.md # CONSOLIDATED 6.3.0 (QA + Gates)
│       ├── gates.yaml
│       └── anti-vibecoding.yaml
├── 03-AI-GOVERNANCE/             # AI GOVERNANCE PRINCIPLES (Ring 1 — timeless)
│   ├── 01 to 09: Core AI Governance Principles
│   ├── 13-AGENTIC-CORE-PRINCIPLES.md    # SASE SE4H/SE4A + 7 principles
│   ├── 14-AGENTIC-MATURITY-MODEL.md     # L0-L3 maturity levels
│   ├── 16-LONG-RUNNING-AGENT-PROTOCOL.md # NEW 6.3.0 (checkpoint/resume/handoff)
│   └── 10/11/12/15: redirect stubs → Ring 2 (expire Sep 2026)
├── 04-AI-TOOLS-LANDSCAPE/        # AI TOOLS TRACKING (Ring 2)
│   ├── tool-profiles/            # Claude Code, Cursor, Copilot profiles
│   ├── best-practices-2026/      # 8 best practice guides
│   ├── integration-guides/       # MCP integration specs
│   ├── capability-matrix.md      # Tool comparison
│   └── trend-watch/              # Monthly tool evolution updates
├── 05-Templates-Tools/           # Templates & Automation (Ring 2)
│   ├── 01-Specification-Standard/  # 5 SPECs + examples + schema
│   │   ├── SPEC-0001 to SPEC-0005
│   │   ├── SDLC-Specification-Standard.md
│   │   └── DESIGN_DECISIONS.md / SPEC_DELTA.md
│   ├── 02-AI-Tools/              # 23 AI prompts by stage (FROZEN)
│   ├── 03-Agent-Templates/       # CLAUDE.md template
│   ├── 04-SASE-Artifacts/        # CRP, MRP, VCR, AGENTS.md, souls/, teams/
│   ├── 05-Checklists/            # Stage transition + compliance
│   ├── 06-Manual-Templates/      # Design Thinking + API templates
│   ├── 07-Scripts/               # Validation scripts
│   └── 08-Project-Templates/     # Planning hierarchy templates
├── 06-Case-Studies/              # BFlow, MTEP, NQH-Bot examples (Ring 2)
├── 07-Implementation-Guides/     # Rollout guides (Ring 3)
├── 08-Training-Materials/        # 11 modules, 39h (Modules 08-11 NEW 6.3.1)
├── 09-Continuous-Improvement/    # RFCs + improvement guide (Ring 3)
├── 10-archive/                   # Centralized legacy archive
│   ├── 00-Legacy/               # Foundation archives (SDLC 1.x-5.0)
│   ├── 01-Legacy/               # Early version scripts
│   ├── 02-Legacy/               # Deprecated guides + code review originals
│   ├── 03-Legacy/               # Sprint 173 orchestrator specs
│   ├── 04-Legacy/               # Sprint 117 POC
│   ├── 05-Legacy/               # Tool guides, OpenSpec, SASE deprecated
│   ├── 06-Legacy/               # Deployment guides v5.1.3
│   └── 09-Legacy/               # Deprecated RFCs, scripts
├── CONTENT-MAP.md                # Topic → file mapping
├── DEPRECATION-POLICY.md         # Redirect rules
└── CHANGELOG.md                  # Version history
```

---

## Quick Start

### Path 1: Understand (30 min)
1. [Executive Summary](./01-Overview/SDLC-Executive-Summary.md) - Overview
2. [Core Methodology](./02-Core-Methodology/SDLC-Core-Methodology.md) - 10 stages
3. [SASE Principles](./03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md) - Agentic workflow

### Path 2: Implement (3 hours)
1. Download [Templates](./05-Templates-Tools/) or [Checklists](./05-Templates-Tools/05-Checklists/)
2. Run 1 feature through 10-stage methodology
3. Setup [Code Review](./07-Implementation-Guides/SDLC-Code-Review-Guide.md)

### Path 3: Full Rollout (2-3 weeks)
1. Week 1: Team training + framework setup
2. Week 2: First Design Thinking sprint
3. Week 3: INTEGRATE, COLLABORATE, GOVERN setup

---

## Key Documents

**Core**:
- [SDLC-Executive-Summary.md](./01-Overview/SDLC-Executive-Summary.md)
- [SDLC-Core-Methodology.md](./02-Core-Methodology/SDLC-Core-Methodology.md)
- [SDLC-Agentic-Core-Principles.md](./03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md)
- [AI Governance Principles](./03-AI-GOVERNANCE/) - 7 timeless principles (5.2.0)

**Stage Governance** (added 5.3.0, current as of 6.1.0):
- [SDLC-Stage-Lifecycle-Framework.md](./02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md) - Stage dependencies + exit criteria + tier requirements (consolidated 6.3.0)
- [SDLC-Sprint-Governance.md](./02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md) - Sprint-stage coordination
- [Stage-Transition-Checklist.md](./05-Templates-Tools/05-Checklists/Stage-Transition-Checklist.md) - Actionable transition checklists

**Quality Assurance** (consolidated in 6.3.0):
- [SDLC-Quality-Gates-Assurance-Framework.md](./02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md) - **Section 7 + Pillar 4: Anti-Vibecoding + Quality Gates**
  - Vibecoding Index (0-100 composite score)
  - Progressive Routing (Auto-approve Green → Senior Review Board Red)
  - Quality Gate requirements (G0-G4, SBOM, SAST, OWASP)
  - Kill Switch Criteria (rejection >80%, latency >500ms, etc.)

**Unified Specification Standard** (added 6.0.2, current as of 6.1.0):
- [SDLC-Specification-Standard.md](./05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md) - **Section 8: Unified Spec Format**
  - YAML frontmatter (spec_id, tier, stage, category)
  - BDD requirements format (GIVEN-WHEN-THEN)
  - Acceptance criteria tables
  - ADR linking requirements
- [DESIGN_DECISIONS.md](./05-Templates-Tools/01-Specification-Standard/DESIGN_DECISIONS.md) - Lightweight ADR alternative
  - Sprint-scoped decisions
  - Options analysis (pros/cons/effort)
  - Escalation rules to full ADR
- [SPEC_DELTA.md](./05-Templates-Tools/01-Specification-Standard/SPEC_DELTA.md) - Version change tracking
  - Breaking change documentation
  - Migration guides
  - CI/CD integration patterns

**AI Tools (Outer Ring)**:
- [AI Tools Landscape](./04-AI-TOOLS-LANDSCAPE/) - Tool-agnostic AI assistant best practices

**Standards**:
- [SDLC-Naming-Standards.md](./02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md) - Naming + Headers
- [SDLC-Team-Collaboration.md](./05-Templates-Tools/05-Checklists/SDLC-Team-Collaboration.md) - Team + Escalation (Ring 2)
- [SDLC-Quality-Gates-Assurance-Framework.md](./02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md) - Pillar 4+5 (consolidated 6.3.0)
- [SDLC-Sprint-Governance.md](./02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md) - Pillar 2

**Templates**:
- [AGENTS.md Template](./05-Templates-Tools/04-SASE-Artifacts/AGENTS-MD-Template.md) - **RECOMMENDED** (replaces MTS/BRS/LPS)
- [SASE Artifacts](./05-Templates-Tools/04-SASE-Artifacts/) - CRP, MRP, VCR, [SOULs](./05-Templates-Tools/04-SASE-Artifacts/souls/), [TEAMs](./05-Templates-Tools/04-SASE-Artifacts/teams/)
- [Checklists](./05-Templates-Tools/05-Checklists/) - Stage transitions, SSOT compliance

**Implementation**:
- [SDLC-Implementation-Guide.md](./07-Implementation-Guides/SDLC-Implementation-Guide.md)
- [SDLC-Code-Review-Guide.md](./07-Implementation-Guides/SDLC-Code-Review-Guide.md) - Unified 3-Tier SSOT

---

## Framework vs. Platform

This Framework is **tool-agnostic policy**. Any platform can implement it:

```
┌───────────────────────────────────────────────────────────┐
│             SDLC 6.1.0 Framework (THIS REPO)             │
│      Methodology • Principles • Gates • Governance        │
│                  (TOOL-AGNOSTIC)                         │
└─────────────┬──────────────────┬─────────────────┬─────────────┘
              │                  │                 │
    ┌─────────┴────┐   ┌───────┴─────┐   ┌─────┴───────┐
    │ SDLC Orchestrator│   │ Custom CI/CD │   │ Other Tools │
    │ (one platform)   │   │ (scripts)    │   │ (future)    │
    └──────────────────┘   └─────────────┘   └────────────┘
```

**Key architectural boundary**:
- **Framework** defines: *what* (principles, stages, gates, evidence requirements)
- **Platform** implements: *how* (APIs, database, UI, CLI that automates Framework rules)
- **Relationship**: 1:N — one Framework, many possible platform implementations
- **Invariant**: Teams can follow this Framework manually without ANY tool. Platforms make enforcement automatic.

> **Rule**: Documents in this repo MUST NOT assume a specific platform.
> When referencing a platform implementation, use "e.g., SDLC Orchestrator" — not as THE implementation.

---

## Version History

For detailed release notes, see [CHANGELOG.md](./CHANGELOG.md).

| Version | Date | Summary |
|---------|------|----------|
| **6.3.1** | **Apr 17, 2026** | **Governance Training Expansion**: 4 new training modules (08-11) — Authority & Decision (2h), Quality Gate Workshop (2h), ADR & Sprint Plan Workflow (2h), Remote Team Governance (1h). Total program: 11 modules, 39h, 80 quiz questions. Modules derived from real governance incidents. |
| 6.3.0 | Mar 29, 2026 | **Methodology Upgrade**: Fix-First Review Protocol (F1), Effort Compression Table (F2), Scope Drift Detection (F3), Three-Tier Testing (F4), Doc Staleness Detection (F5), Terminal Status Taxonomy (F6). SOUL-cso added (18 roles). |
| 6.3.0 | Mar 18, 2026 | Agentic SDLC + Lean Ring 1: 8 Mental Models, Long-Running Agent Protocol, Citizen Developer Guide, ROI Calculator. Ring 1 consolidated (-21%). 42 tool-specific refs sanitized. |
| 6.1.2 | Mar 9, 2026 | SOULs + TEAMs: 18 role templates + 10 team charters (Ring 2) |
| 6.1.1 | Feb 21, 2026 | Post-Cleanup Patch: AI Council→Senior Review Board, 36 frozen templates archived, Conversation-First Governance |
| 6.1.0 | Feb 18, 2026 | Consolidation Release: Ring 1 monolith slim, agentic→AI-GOV move, Multi-Agent Patterns, BRS/MTS/LPS→AGENTS.md |
| 6.0.6 | Feb 16, 2026 | Anthropic Best Practices Integration (Sprint 174): CLAUDE.md Standard, Autonomous Codegen Patterns, MRP Template |
| 6.0.5 | Feb 15, 2026 | RFC-001 Legacy Organization + Anti-Vibecoding alignment + Framework cleanup + Governance Loop |
| 6.0.4 | Feb 8, 2026 | TDD Integration + Sprint 3-Phase Model + Spec Converter |
| 6.0.3 | Feb 2, 2026 | Boris Cherny Consolidation, MCP Integration Guide |
| 6.0.2 | Feb 2, 2026 | E2E API Testing Enhancement |
| 6.0.1 | Feb 1, 2026 | Stage Consistency Validation |
| 6.0.0 | Jan 28, 2026 | Unified Specification Standard (Section 8) |
| 5.3.0 | Jan 28, 2026 | Stage Dependencies + Quality Assurance System |
| 5.2.0 | Jan 22, 2026 | AI Governance Principles + Concentric Circles |
| 5.0.0 | Dec 5, 2025 | 4-Tier Classification |
| 4.8.0 | Nov 7, 2025 | Design Thinking foundation |

---

**Owner**: CPO Office (taidt@mtsolution.com.vn)
**Authority**: CTO Approved
