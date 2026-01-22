# SDLC 5.2.0 Universal Framework

**Version**: 5.2.0 | **Status**: ACTIVE | **Date**: January 2026

Built BY AI+Human Teams FOR AI+Human Teams

---

## Overview

SDLC 5.2.0 is a **7-Pillar AI+Human Excellence Framework** with:
- **Pillar 0**: Design Thinking Foundation
- **Pillar 1**: 10 Lifecycle Stages (00-09): Foundation → Govern
- **Pillar 2**: Sprint Planning Governance
- **Pillar 3**: 4-Tier Classification (LITE → ENTERPRISE)
- **Pillar 4**: Quality Gates (Dual-Track: Feature + Sprint)
- **Pillar 5**: SASE Integration (SE 3.0)
- **Pillar 6**: Documentation Permanence

**NEW in 5.2.0**:
- **AI Governance Principles**: 7 timeless principles for AI+Human collaboration
- **Risk-Based Planning**: Planning triggered by risk factors, not LOC count
- **Concentric Circles Model**: Core (timeless) → Governance (stable) → Outer Ring (tools)
- **AI Agent Best Practices 2026**: Complete orchestration guide

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

## Concentric Circles Model (NEW in 5.2.0)

Framework content is organized by stability:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    ┌─────────────────────────────────────────────────────┐     │
│    │         🎯 CORE (Timeless Principles)              │     │
│    │                                                     │     │
│    │    • Design Thinking          • Quality Gates      │     │
│    │    • 10-Stage Lifecycle       • Human Accountability│     │
│    │    • AI Governance Principles (NEW)                │     │
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
│   ├── Documentation-Standards/
│   └── Governance-Compliance/
├── 03-AI-GOVERNANCE/             # AI GOVERNANCE PRINCIPLES (NEW)
│   ├── 01-AI-Human-Collaboration.md
│   ├── 02-Agent-Accountability.md
│   ├── 03-Planning-Mode-Principle.md
│   ├── 04-Verification-Principle.md
│   ├── 05-Context-Management.md
│   ├── 06-Tool-Evaluation-Criteria.md
│   └── 07-Anti-Patterns.md
├── 03-Templates-Tools/           # Templates & Automation
│   ├── SASE-Artifacts/           # CRP, MRP, VCR (MTS/BRS/LPS deprecated)
│   ├── 1-AI-Tools/
│   ├── 2-Agent-Templates/
│   └── 3-Manual-Templates/
├── 04-Case-Studies/              # BFlow, NQH-Bot examples
├── 05-Implementation-Guides/     # Rollout guides
├── 06-Training-Materials/
├── 07-Continuous-Improvement/
├── 08-Version-History/
├── 99-Legacy/                    # Archive
├── CONTENT-MAP.md                # Topic → file mapping (NEW)
└── DEPRECATION-POLICY.md         # Redirect rules (NEW)
```

---

## Quick Start

### Path 1: Understand (30 min)
1. [Executive Summary](./01-Overview/SDLC-Executive-Summary.md) - Overview
2. [Core Methodology](./02-Core-Methodology/SDLC-Core-Methodology.md) - 10 stages
3. [SASE Principles](./02-Core-Methodology/SDLC-Agentic-Core-Principles.md) - Agentic workflow

### Path 2: Implement (3 hours)
1. Download [AI Tools](./03-Templates-Tools/1-AI-Tools/) or [Manual Templates](./03-Templates-Tools/3-Manual-Templates/)
2. Run 1 feature through 10-stage methodology
3. Setup [Code Review Tier](./05-Implementation-Guides/SDLC-Universal-Code-Review-Framework.md)

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
- [AI Governance Principles](./03-AI-GOVERNANCE/) - **NEW in 5.2.0** (7 timeless principles)

**Standards**:
- [SDLC-Document-Naming-Standards.md](./02-Core-Methodology/Documentation-Standards/SDLC-Document-Naming-Standards.md)
- [SDLC-Quality-Gates.md](./02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates.md)
- [SDLC-Security-Gates.md](./02-Core-Methodology/Governance-Compliance/SDLC-Security-Gates.md)
- [SDLC-Sprint-Planning-Governance.md](./02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Planning-Governance.md) ← **NEW in 5.1.3**

**Templates**:
- [AGENTS.md Template](./03-Templates-Tools/SASE-Artifacts/AGENTS-MD-Template.md) - **RECOMMENDED** (replaces MTS/BRS/LPS)
- [SASE Artifacts](./03-Templates-Tools/SASE-Artifacts/) - CRP, MRP, VCR _(MTS/BRS/LPS deprecated)_
- [AI Tools](./03-Templates-Tools/1-AI-Tools/) - AI prompts
- [Agent Templates](./03-Templates-Tools/2-Agent-Templates/) - 17 agents

**Implementation**:
- [SDLC-Implementation-Guide.md](./05-Implementation-Guides/SDLC-Implementation-Guide.md)
- [SDLC-Universal-Code-Review-Framework.md](./05-Implementation-Guides/SDLC-Universal-Code-Review-Framework.md)

---

## Version History

| Version | Date | Key Changes |
|---------|------|-------------|
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
