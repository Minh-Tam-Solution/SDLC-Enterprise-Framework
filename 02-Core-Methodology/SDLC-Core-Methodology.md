# SDLC 6.3.1 Core Methodology

**Version**: 6.3.1
**Date**: March 18, 2026
**Status**: ACTIVE — Agentic SDLC + Lean Ring 1 (9 Mental Models, Long-Running Agent Protocol, tool-agnostic)
**Authority**: Chairman + CEO + CPO + CTO Approved

---

## Executive Summary

SDLC 6.3.1 is a **7-Pillar + 2-Section AI+Human Excellence Framework** that governs the complete software development lifecycle from strategic discovery to production operations, with **9 Mental Models** (System Thinking), **Long-Running Agent Protocol**, integrated quality assurance (consolidated), and **tool-agnostic methodology** (0 product-specific references in Ring 1).

### Architecture Overview

```
╔════════════════════════════════════════════════════════════════════════════╗
║                    SDLC 6.3.0 - 7 PILLARS + 2 SECTIONS                     ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  ═══════════════════════ CORE PILLARS (Stable) ════════════════════════   ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ PILLAR 0: DESIGN THINKING FOUNDATION                                 │  ║
║  │ "Build the RIGHT thing" - User-centered approach throughout          │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ PILLAR 1: 10-STAGE LIFECYCLE                                         │  ║
║  │ Foundation → Plan → Design → Integrate → Build → Test → Deploy →    │  ║
║  │ Operate → Collaborate → Govern (with Stage Dependency Matrix)        │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ PILLAR 2: SPRINT PLANNING GOVERNANCE (6.0.4 Enhanced)                │  ║
║  │ Planning Hierarchy + G-Sprint Gates + 10 Golden Rules                │  ║
║  │ 3-Phase Sprint: PRE-SPRINT → EXECUTION → POST-SPRINT                 │  ║
║  │ TDD Integration: RED → GREEN → REFACTOR per feature                  │  ║
║  │ "Sprint governance is NOT optional - it's the execution backbone"    │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ PILLAR 3: 4-TIER CLASSIFICATION                                      │  ║
║  │ LITE (1-2) → STANDARD (3-10) → PROFESSIONAL (10-50) → ENTERPRISE    │  ║
║  │ With Tier-Specific Stage Exit Criteria                               │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ PILLAR 4: QUALITY GATES                                              │  ║
║  │ Feature Gates (G0-G4) + Sprint Gates (G-Sprint, G-Sprint-Close)      │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ PILLAR 5: SASE INTEGRATION (SE 3.0)                                  │  ║
║  │ AI+Human Excellence - SE4H + SE4A dual-modality                      │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ PILLAR 6: DOCUMENTATION PERMANENCE                                   │  ║
║  │ AI-parseable, version-free naming, 10-stage /docs structure          │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ═══════════════════ EXTENSION SECTIONS (Additive) ════════════════════   ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ SECTION 7: QUALITY ASSURANCE SYSTEM (5.3.0)                          │  ║
║  │ Anti-Vibecoding: Vibecoding Index + Progressive Routing + Kill Switch│  ║
║  │ "Governance must be the fastest way - or developers will bypass it"  │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
║  ┌──────────────────────────────────────────────────────────────────────┐  ║
║  │ SECTION 8: UNIFIED SPECIFICATION STANDARD (6.0.4) ⭐ ENHANCED        │  ║
║  │ YAML Frontmatter + BDD Requirements + Lightweight ADRs               │  ║
║  │ Spec Converter (SpecIR) + Tier-Aware TDD Coverage (6.0.4)            │  ║
║  │ "Consistent specs enable AI+Human collaboration at scale"            │  ║
║  └──────────────────────────────────────────────────────────────────────┘  ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
```

### Why 7 Pillars + 2 Sections?

**Core Pillars (0-6)** - Stable foundation, rarely changes:

| Pillar | Purpose | Without It |
|--------|---------|------------|
| 0. Design Thinking | Build the RIGHT thing | 70% features unused |
| 1. 10-Stage Lifecycle | Complete coverage | Gaps cause failures |
| 2. Sprint Governance | Execution backbone + TDD | Direction confusion, doc lag |
| 3. 4-Tier Classification | Right-size processes | Over/under engineering |
| 4. Quality Gates | Prevent bad code shipping | Production incidents |
| 5. SASE Integration | AI+Human productivity | 10x vs 50x potential |
| 6. Documentation | Knowledge preservation | Context loss |

**Extension Sections (7-8)** - Additive capabilities, evolves with AI landscape:

| Section | Purpose | Without It |
|---------|---------|------------|
| 7. Quality Assurance | Anti-vibecoding governance | AI-generated tech debt |
| **8. Unified Specs** | **Consistent specification format** | **Integration friction, AI confusion** |

**Heritage**: Built BY AI+Human Teams FOR AI+Human Teams

---

## Pillar 0: Design Thinking Foundation

> **"Build the RIGHT thing, then build the thing RIGHT"**

### The 5 Phases

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DESIGN THINKING 5 PHASES                         │
├─────────────────────────────────────────────────────────────────────┤
│  1. EMPATHIZE   │ Understand users through observation & interviews │
│  2. DEFINE      │ Frame the core problem to solve                   │
│  3. IDEATE      │ Generate 100+ solutions, select top 3             │
│  4. PROTOTYPE   │ Build minimum testable versions                   │
│  5. TEST        │ Validate with real users, iterate                 │
└─────────────────────────────────────────────────────────────────────┘
```

### Design Thinking × SDLC Stage Mapping

| Phase | SDLC Stage | Primary Output |
|-------|------------|----------------|
| EMPATHIZE | Stage 00 | User Interview Summaries, Personas |
| DEFINE | Stage 00 | Problem Statement, Pain Points |
| IDEATE | Stage 01-02 | Solution Concepts, Architecture Options |
| PROTOTYPE | Stage 04 | MVP, Working Features |
| TEST | Stage 05 | User Feedback, Iteration Plan |

### Quality Gates (Design Thinking)

**G0.1: Problem Definition**
- 5+ user interviews conducted
- Pain point ranked (severity 1-10)
- Problem statement validated by stakeholders

**G0.2: Solution Diversity**
- 100+ ideas generated (brainstorm)
- Top 3 concepts selected with rationale
- Validation plan defined

**Reference**: [SDLC-Design-Thinking-Principles.md](./SDLC-Design-Thinking-Principles.md)

**Foundational Thinking Models** (Pillar 0 Trilogy):
- [System Thinking Foundation](./SDLC-System-Thinking-Foundation.md) — Iceberg Model, **9 mental models** for root-cause analysis (6.3.0: +Agent Continuity, +More People Build; 6.3.2: +Demand Before Surface [DT])
- [Crisis-to-Pattern Methodology](./SDLC-Crisis-To-Pattern-Methodology.md) — 5-step pipeline: Diagnose → Policy → Automate → Enforce → Document

---

## Pillar 1: 10-Stage Lifecycle

### Overview

```
┌────────────────────────────────────────────────────────────────────────┐
│                    SDLC 6.3.0 - 10 STAGES                              │
├────────────────────────────────────────────────────────────────────────┤
│  Stage 00: FOUNDATION (WHY?)     → Strategic Discovery & Validation    │
│  Stage 01: PLANNING (WHAT?)      → Requirements & User Stories         │
│  Stage 02: DESIGN (HOW?)         → Architecture & Technical Design     │
│  Stage 03: INTEGRATE             → API Contracts & Third-party Setup   │
│  Stage 04: BUILD                 → Development & Implementation        │
│  Stage 05: TEST                  → Quality Assurance & Validation      │
│  Stage 06: DEPLOY                → Release & Deployment                │
│  Stage 07: OPERATE               → Production Operations & Monitoring  │
│  Stage 08: COLLABORATE           → Team Coordination & Knowledge       │
│  Stage 09: GOVERN                → Compliance & Strategic Oversight    │
└────────────────────────────────────────────────────────────────────────┘
```

### Stage Summary

| Stage | Name | Core Question | Primary Deliverable |
|-------|------|---------------|---------------------|
| 00 | FOUNDATION | WHY are we building this? | Business Case, Problem Statement |
| 01 | PLANNING | WHAT are we building? | Requirements, User Stories, API Specs |
| 02 | DESIGN | HOW will we build it? | Architecture, ADRs, Security Design |
| 03 | INTEGRATE | How does it connect? | API Contracts, Integration Tests |
| 04 | BUILD | Are we building it right? | Working Code, Unit Tests |
| 05 | TEST | Does it work correctly? | Test Reports, UAT Sign-off |
| 06 | DEPLOY | How do we ship safely? | Release Notes, Rollback Procedures |
| 07 | OPERATE | Is it running reliably? | Runbooks, Monitoring Dashboards |
| 08 | COLLABORATE | Is the team effective? | Team Charter, Training Materials |
| 09 | GOVERN | Are we compliant? | Compliance Reports, Audit Docs |

### Stage → Folder Mapping

| Stage | Folder | Notes |
|-------|--------|-------|
| 00 | `docs/00-foundation/` | Strategic documents |
| 01 | `docs/01-planning/` | Requirements, stories |
| 02 | `docs/02-design/` | Architecture, ADRs |
| 03 | `docs/03-integrate/` | API contracts |
| 04 | `docs/04-build/` | **Sprint plans, build logs** |
| 05 | `docs/05-test/` | Test plans, reports |
| 06 | `docs/06-deploy/` | Deployment guides |
| 07 | `docs/07-operate/` | Runbooks, SRE docs |
| 08 | `docs/08-collaborate/` | Team docs, training |
| 09 | `docs/09-govern/` | Compliance, executive reports |
| - | `docs/10-archive/` | Project-level archive (NOT a stage) |

**Important**: Stage mapping applies ONLY to `/docs` folders. Code folders (`backend/`, `frontend/`) are organizational units independent of stages.

### Stage Dependency Matrix (5.3.0)

> **"Working ahead of design = rework. Stage gates prevent this."**

| Stage | Hard Dependencies | Soft Dependencies | Can Start When |
|-------|-------------------|-------------------|----------------|
| 00 Foundation | None | - | Immediately |
| 01 Planning | G0.1 passed | 00 complete | Problem validated |
| 02 Design | G0.2 passed | 01 complete | Solution selected |
| 03 Integrate | 02 partial (API specs) | - | API design approved |
| 04 Build | G2 passed | 03 partial | Architecture approved |
| 05 Test | 04 partial | - | First module complete |
| 06 Deploy | 05 exit | 04 complete | All tests passing |
| 07 Operate | 06 complete | - | Deployed to production |
| 08 Collaborate | None | All stages | Continuous |
| 09 Govern | None | All stages | Continuous |

**Parallel Execution Rules**:
- 03-04: Can run in parallel (API-first development)
- 04-05: Can overlap (continuous testing)
- 07-08-09: Always parallel (operations, collaboration, governance)

**Reference**: [SDLC-Stage-Lifecycle-Framework.md](./SDLC-Stage-Lifecycle-Framework.md)

---

## Pillar 2: Sprint Planning Governance

> **"Sprint governance is NOT optional - it's the execution backbone of every project"**

### Why Sprint Governance is a Core Pillar

**The Incident That Changed Everything** (production platform incident, January 2026):
- 27-day documentation lag
- 4+ documents with inconsistent sprint references
- Sprint started without formal approval
- Team direction confusion requiring CTO intervention

**Root Cause**: SDLC had excellent stage templates but NO sprint governance.

**The Truth**: Every stage (00-09) is executed through SPRINTS. Without sprint governance, even perfect stage documentation doesn't prevent execution chaos.

### Planning Hierarchy

```
╔════════════════════════════════════════════════════════════════════════╗
║                    PLANNING HIERARCHY (4 LEVELS)                       ║
╠════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  Level 1: ROADMAP (12 months)                                         ║
║  └─ Strategic goals, quarterly milestones, OKRs                       ║
║       │                                                                ║
║       ▼                                                                ║
║  Level 2: PHASE (4-8 weeks)                                           ║
║  └─ Phase objectives, feature groupings, release goals                ║
║       │                                                                ║
║       ▼                                                                ║
║  Level 3: SPRINT (5-10 days)                                          ║
║  └─ Sprint goal, committed work, G-Sprint approval                    ║
║       │                                                                ║
║       ▼                                                                ║
║  Level 4: BACKLOG (Tasks)                                             ║
║  └─ User stories, tasks, bugs with assignments                        ║
║                                                                        ║
╚════════════════════════════════════════════════════════════════════════╝
```

### The 10 Golden Rules

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                    10 GOLDEN RULES OF SPRINT GOVERNANCE                   ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   1. Sprint Numbers Are Immutable                                         ║
║      Once assigned, a sprint number cannot be changed or reused.          ║
║      CANCELLED sprints retain their number.                               ║
║                                                                           ║
║   2. Every Sprint Has One Clear Goal                                      ║
║      Single sentence describing the sprint's primary outcome.             ║
║      Not a list of features - a coherent objective.                       ║
║                                                                           ║
║   3. Documentation Within 24 Business Hours                               ║
║      All sprint docs updated within 24h of completion.                    ║
║      Business hours only (weekends/holidays excluded).                    ║
║                                                                           ║
║   4. G-Sprint Gate Before Execution                                       ║
║      No sprint starts without formal planning gate approval.              ║
║      Prevents "ready, fire, aim" development.                             ║
║                                                                           ║
║   5. G-Sprint-Close Gate Before Next Sprint                               ║
║      Current sprint must pass close gate before next sprint starts.       ║
║      Ensures continuity and accountability.                               ║
║                                                                           ║
║   6. Traceability is Mandatory                                            ║
║      Every sprint links to Phase → Roadmap → Strategic Goal.              ║
║      "Why are we doing this sprint?" always answerable.                   ║
║                                                                           ║
║   7. Sprint Goal Must Align with Phase Objective                          ║
║      Verify alignment during G-Sprint gate evaluation.                    ║
║      Misaligned sprints fail the gate.                                    ║
║                                                                           ║
║   8. Strategic Priorities Must Be Explicit                                ║
║      P0/P1/P2 labels required for all work items.                         ║
║      No "options" for P0 items - they are mandates.                       ║
║                                                                           ║
║   9. Failed Gate Blocks Progress                                          ║
║      Cannot proceed to next phase without gate pass or exception.         ║
║      Exceptions require CTO approval with documented rationale.           ║
║                                                                           ║
║  10. Weekly Roadmap Review is Required                                    ║
║      Minimum bi-weekly for STANDARD tier, weekly for PROFESSIONAL+.       ║
║      Prevents roadmap drift and strategic misalignment.                   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### Sprint Governance Gates

**G-Sprint (Sprint Planning Gate)**

| Category | Checklist Item | Required |
|----------|---------------|----------|
| Alignment | Sprint goal aligns with Phase objective | ✅ |
| Alignment | Sprint goal aligns with Roadmap goal | ✅ |
| Alignment | Priorities explicit (P0/P1/P2 labeled) | ✅ |
| Capacity | Team capacity calculated | ✅ |
| Capacity | Story points within velocity (+10% max) | ✅ |
| Dependencies | External dependencies identified | ✅ |
| Risk | Top 3 risks identified | ✅ |
| Documentation | SPRINT-XX.md created | ✅ |

**G-Sprint-Close (Sprint Completion Gate)**

| Category | Checklist Item | Required |
|----------|---------------|----------|
| Work | All items accounted for (done/carryover) | ✅ |
| Work | Carryover documented with reason | ✅ |
| Quality | Definition of Done met | ✅ |
| Retrospective | Sprint retro completed | ✅ |
| Metrics | Velocity calculated | ✅ |
| Documentation | CURRENT-SPRINT.md updated | ✅ |
| Documentation | Documentation within 24 business hours | ✅ |

### Sprint Governance by Tier

| Tier | G-Sprint Approval | G-Sprint-Close | Weekly Review | Documentation |
|------|-------------------|----------------|---------------|---------------|
| LITE | Self (optional) | Self (optional) | Monthly | SPRINT-XX.md only |
| STANDARD | Tech Lead | Tech Lead | Bi-weekly | + CURRENT-SPRINT.md |
| PROFESSIONAL | Tech Lead + PO | Tech Lead | Weekly | + SPRINT-INDEX.md |
| ENTERPRISE | Steering Committee | Tech Lead + PO | Weekly + Monthly | Full audit trail |

### Sprint Governance × 10-Stage Integration

Sprint governance operates ACROSS all stages:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                SPRINT GOVERNANCE ACROSS STAGES                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Stage 00 FOUNDATION ─┐                                                │
│  Stage 01 PLANNING ───┤                                                │
│  Stage 02 DESIGN ─────┤                                                │
│  Stage 03 INTEGRATE ──┼──→ All executed through SPRINTS with:         │
│  Stage 04 BUILD ──────┤    • G-Sprint gate before start               │
│  Stage 05 TEST ───────┤    • Traceability to Phase/Roadmap            │
│  Stage 06 DEPLOY ─────┤    • G-Sprint-Close after completion          │
│  Stage 07 OPERATE ────┤    • 24h documentation requirement            │
│  Stage 08 COLLABORATE ┤                                                │
│  Stage 09 GOVERN ─────┘                                                │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

**Reference**: [SDLC-Sprint-Governance.md](./Governance-Compliance/SDLC-Sprint-Governance.md)

---

## Pillar 3: 4-Tier Classification

### Overview

| Tier | Team Size | Required Stages | Sprint Governance |
|------|-----------|-----------------|-------------------|
| **LITE** | 1-2 | 00, 01, 02, 04 | Optional (recommended) |
| **STANDARD** | 3-10 | 00-02, 04-06 | Required (Tech Lead) |
| **PROFESSIONAL** | 10-50 | All 10 stages | Required (formal gates) |
| **ENTERPRISE** | 50+ | All 10 stages | Mandatory + Audit |

### Documentation Level by Tier

**LITE (1-2 members)**:
```
docs/
├── 00-foundation/
├── 01-planning/
├── 02-design/
└── 04-build/
    └── 02-Sprint-Plans/   ← Sprint governance docs
        └── SPRINT-XX.md
```

**STANDARD (3-10 members)**:
```
docs/
├── 00-foundation/
├── 01-planning/
├── 02-design/
├── 04-build/
│   └── 02-Sprint-Plans/
│       ├── CURRENT-SPRINT.md    ← Required
│       └── SPRINT-XX.md
├── 05-test/
└── 06-deploy/
```

**PROFESSIONAL/ENTERPRISE (10+ members)**:
```
docs/
├── 00-foundation/
├── 01-planning/
│   └── ROADMAP.md               ← Required
├── 02-design/
├── 03-integrate/
├── 04-build/
│   ├── 01-ADRs/
│   └── 02-Sprint-Plans/
│       ├── CURRENT-SPRINT.md
│       ├── SPRINT-INDEX.md      ← Required
│       └── SPRINT-XX.md
├── 05-test/
├── 06-deploy/
├── 07-operate/
├── 08-collaborate/
├── 09-govern/
│   └── ROADMAP-CHANGE-LOG.md    ← Required
└── 10-archive/
```

### Sprint Planning Governance by Tier

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| Planning Hierarchy | Optional | Recommended | Required | Required |
| G-Sprint Gate | Self | Tech Lead | Tech Lead + PO | Steering Committee |
| G-Sprint-Close | Self | Tech Lead | Tech Lead | Tech Lead + PO |
| 24h Documentation | Best effort | Required | Enforced | Enforced + Audit |
| Weekly Review | Monthly | Bi-weekly | Weekly | Weekly + Monthly |
| SSOT Validation | None | CI warning | CI blocking | CI blocking + Alert |
| Roadmap Change | Informal | PO approval | Steering Committee | Change Advisory Board |

---

## Pillar 4: Quality Gates

### Dual-Track Gate System

SDLC 6.3.0 has TWO parallel gate tracks:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DUAL-TRACK QUALITY GATES                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  TRACK 1: FEATURE GATES (G0-G4)                                        │
│  └─ Control feature development lifecycle                              │
│     G0.1 → G0.2 → G1 → G2 → G3 → G4                                   │
│                                                                         │
│  TRACK 2: SPRINT GATES (G-Sprint, G-Sprint-Close)                      │
│  └─ Control sprint execution rhythm                                    │
│     G-Sprint → [Sprint Work] → G-Sprint-Close                          │
│                                                                         │
│  RELATIONSHIP: Feature work is EXECUTED through Sprints               │
│  └─ A feature may span multiple sprints                               │
│  └─ A sprint may contain work from multiple features                  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Track 1: Feature Gates (G0-G4)

| Gate | Stage | Purpose | Key Criteria |
|------|-------|---------|--------------|
| G0.1 | 00 | Problem Validated | 5+ user interviews, pain points ranked |
| G0.2 | 00 | Solution Validated | 100+ ideas, top 3 selected |
| G1 | 01 | Requirements Complete | All stories have acceptance criteria |
| G2 | 02 | Design Approved | Architecture reviewed, ADRs approved |
| G3 | 04-05 | Ship Ready | Tests passing, code reviewed, UAT signed |
| G4 | 06-07 | Production Stable | SLA met, monitoring in place |

### Track 2: Sprint Gates (G-Sprint, G-Sprint-Close)

| Gate | Timing | Purpose | Key Criteria |
|------|--------|---------|--------------|
| G-Sprint | Pre-Sprint | Plan Approved | Goal aligned, capacity validated |
| G-Sprint-Close | Post-Sprint | Sprint Complete | Work accounted, docs updated within 24h |

### Gate Integration Example

```
Feature: User Authentication (G0 → G4)
│
├── Sprint N: Foundation (G-Sprint → G-Sprint-Close)
│   └── Completes G0.1, G0.2
│
├── Sprint N+1: Requirements (G-Sprint → G-Sprint-Close)
│   └── Completes G1
│
├── Sprint N+2: Design (G-Sprint → G-Sprint-Close)
│   └── Completes G2
│
├── Sprint N+3, N+4: Build (G-Sprint → G-Sprint-Close × 2)
│   └── Partial G3
│
├── Sprint N+5: Test (G-Sprint → G-Sprint-Close)
│   └── Completes G3
│
└── Sprint N+6: Deploy (G-Sprint → G-Sprint-Close)
    └── Completes G4
```

**Reference**: [SDLC-Quality-Gates-Assurance-Framework.md](./Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md)

---

## Pillar 5: SASE Integration (SE 3.0)

### SE4H vs SE4A Dual-Modality

| Aspect | SE4H (Agent Coach) | SE4A (Agent Executor) |
|--------|-------------------|----------------------|
| **Role** | Guide & supervise AI agents | Implement human-specified intent |
| **Primary Skills** | Intent specification, validation | Code generation, consistency |
| **Artifacts Created** | AGENTS.md, VCR, policies | CRP, MRP, code |
| **Decision Authority** | FINAL (veto power) | NONE (propose only) |

### Agentic Maturity Levels

| Level | Name | Characteristic | Sprint Governance |
|-------|------|----------------|-------------------|
| **L0** | Tool-Assisted | AI as autocomplete | Manual sprint tracking |
| **L1** | Agent-Assisted | Structured handoff | Agent assists sprint docs |
| **L2** | Structured Agentic | Full SASE workflow | Agent generates sprint reports |
| **L3** | Lifecycle Agentic | Proactive agents | Agent monitors gate compliance |

### 7 Agentic Principles

1. **AGENTS.md First** — Shared context file before any agent work
2. **Evidence-Based MRP** — 5-point evidence for every merge
3. **Human Accountability** — Human responsible for shipped code (VCR)
4. **Consultation Protocol** — CRP when agent uncertain
5. **Mentorship-as-Code** — Standards encoded in AGENTS.md
6. **Dual Workbenches** — ACE for humans, AEE for agents
7. **Gradual Autonomy** — Trust earned from L0→L3

### SASE × SDLC Stage Mapping

| Stage | SASE Discipline | Primary Activity |
|-------|-----------------|------------------|
| 00 Foundation | None | Human-only strategic work |
| 01 Planning | BriefingEng | Create AGENTS.md, define specs |
| 02 Design | ALE + ATIE | Design execution plans, architecture |
| 03 Integrate | ATME + ATIE | CRP generation, API contracts |
| 04 Build | ATLE | Build ACE/AEE, **sprint execution** |
| 05 Test | ALE + ATME | Execute plans, generate MRP |
| 06 Deploy | ATME | Validation, coverage |
| 07 Operate | ATME + AGE | Monitoring, CRP on anomalies |
| 08 Collaborate | ATIE + AGE | Code review, team coordination |
| 09 Govern | AGE | Policy, audit, **sprint governance reports** |

**Reference**: [SDLC-Agentic-Core-Principles.md](../03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md)

---

## Pillar 6: Documentation Permanence

### Core Principles

1. **Version-Free Naming**: `SDLC-Core-Methodology.md` (NOT `SDLC-5.3.0-Core-Methodology.md`)
2. **Feature-Based**: `Authentication-Guide.md` (NOT `Nov-13-Auth.md`)
3. **AI-Parseable**: Markdown, YAML, structured formats
4. **10-Stage Structure**: Documentation organized by lifecycle stage

### Sprint Documentation Standards

| Document | Location | Purpose | Update Frequency |
|----------|----------|---------|------------------|
| ROADMAP.md | `docs/01-planning/` | 12-month strategic plan | Quarterly |
| CURRENT-SPRINT.md | `docs/04-build/` | Active sprint pointer | Every sprint |
| SPRINT-INDEX.md | `docs/04-build/02-Sprint-Plans/` | Sprint history | Every sprint |
| SPRINT-XX.md | `docs/04-build/02-Sprint-Plans/` | Individual sprint plan | Per sprint |
| ROADMAP-CHANGE-LOG.md | `docs/09-govern/` | Strategic changes | As needed |

### SSOT (Single Source of Truth) Validation

```yaml
# CI/CD validation script checks:
SSOT Checks:
  - CURRENT-SPRINT.md matches latest SPRINT-XX.md
  - SPRINT-INDEX.md includes all sprint files
  - Roadmap dates align with phase dates
  - No orphan sprint references in docs
  
Enforcement by Tier:
  LITE: None
  STANDARD: CI warning
  PROFESSIONAL: CI blocking
  ENTERPRISE: CI blocking + Slack alert
```

**Reference**: [SDLC-Naming-Standards.md](./Documentation-Standards/SDLC-Naming-Standards.md)

---

## Section 7: Quality Assurance System (5.3.0)

> **"Governance must be the fastest way - or developers will bypass it"**

### The Problem: Vibecoding

AI tools produce "vibecoded" output - quick but unmaintainable code that:
- Looks functional but lacks architectural coherence
- Has high AI dependency ratio (>80% AI-generated, <10% human review)
- Creates technical debt that compounds rapidly
- Bypasses governance because manual compliance is too slow

### The Solution: Vibecoding Index (0-100)

**5 Weighted Signals** (SPEC-0001):

| Signal | Weight | What It Measures |
|--------|--------|------------------|
| Intent Clarity Score | 30% | How clear is the requirement/ticket? (0-100) |
| Code Ownership Confidence | 25% | Does the AI know who owns this code? (0-100) |
| Context Completeness | 20% | How complete is the context provided to AI? (0-100) |
| AI Attestation Rate | 15% | % of code changes with AI co-authorship declared |
| Historical Rejection Rate | 10% | % of recent PRs rejected in code review |

**Formula**: `Vibecoding Index = 100 - ((Intent × 0.30) + (Ownership × 0.25) + (Context × 0.20) + (Attestation × 0.15) + (100 - Rejection) × 0.10)`

### Progressive Routing

| Score | Category | Action | Review Required |
|-------|----------|--------|-----------------|
| < 20 | 🟢 Green (Low Risk) | Auto-merge | 1+ approvals (automated OK) |
| 20-40 | 🟡 Yellow (Medium Risk) | Human review required | 2+ human code reviews, coverage >= 80% |
| 40-60 | 🟠 Orange (High Risk) | Senior review required | Senior engineer + Security lead sign-off |
| >= 60 | 🔴 Red (Critical Risk) | Block or Senior Review Board | CTO override required, mandatory human rewrite |

### Auto-Generation Layer

**Goal**: Reduce compliance friction from 30 min → <5 min per PR.

| Generator | Trigger | Output | Time Saved |
|-----------|---------|--------|------------|
| Intent Skeleton | Task created | `docs/intents/TASK-{id}-intent.md` | ~15 min |
| Ownership Suggester | File created/modified | `@owner` annotation | ~2 min |
| Context Attachment | PR created | Enriched PR description with ADR/spec links | ~5 min |
| Attestation Pre-Fill | AI code detected | 80% pre-filled attestation form | ~8 min |

### Kill Switch Criteria

Automatic AI code generation disable on quality degradation (ENTERPRISE tier, FULL enforcement):

| Criteria | Threshold | Duration | Action |
|----------|-----------|----------|--------|
| Rejection Rate | >80% | 30 consecutive minutes | Disable AI codegen for 24h |
| Latency P95 | >500ms | 15 consecutive minutes | Fallback to rule-based |
| Security Scan Failures | >5 critical CVEs | Any occurrence | Immediate disable + alert CTO |

**Recovery Conditions**: Manual CTO approval → Root cause analysis → Fix deployed → Gradual re-enable (10% → 50% → 100%)

### Governance Modes

| Mode | Behavior | When to Use |
|------|----------|-------------|
| OFF | No governance | Migration period only |
| WARNING | Log violations, don't block | First 3 days of rollout |
| SOFT | Block critical violations only | Week 1-2 |
| FULL | All rules enforced | Production |

**Reference**: [SDLC-Quality-Gates-Assurance-Framework.md](./Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md)

---

## Industry Standards Integration

SDLC 6.3.0 maps to industry standards:

```yaml
Standards Mapped:
  CMMI v3.0:      Maturity level mapping (LITE=L1-2, ENTERPRISE=L4-5)
  SAFe 6.0:       Planning hierarchy (Portfolio → Program → Team)
  DORA Metrics:   Deployment Frequency, Lead Time, MTTR, CFR
  OWASP ASVS:     Application Security Verification (Levels 1-3)
  NIST SSDF:      Secure Software Development Framework
  ISO/IEC 12207:  Process categories mapping
  Team Topologies: Stream-aligned, Platform, Enabling teams

Sprint Governance Standards:
  Scrum Guide:    Sprint Planning, Sprint Review, Retrospective
  SAFe PI:        Planning Iteration concepts
  PMBOK 7:        Project governance principles

Quality Assurance Standards (5.3.0):
  Code Quality:   SonarQube metrics, cyclomatic complexity
  AI Governance:  Responsible AI frameworks, explainability
  Anti-Patterns:  Martin Fowler's code smell catalog
```

---

## Related Documents

### Core Methodology (Pillar 0 Trilogy)
- [SDLC-Design-Thinking-Principles.md](./SDLC-Design-Thinking-Principles.md) — User-centered approach (Pillar 0 hub)
- [SDLC-System-Thinking-Foundation.md](./SDLC-System-Thinking-Foundation.md) — Iceberg Model, **9 mental models** (6.3.0)
- [SDLC-Crisis-To-Pattern-Methodology.md](./SDLC-Crisis-To-Pattern-Methodology.md) — 5-step crisis-to-pattern pipeline

### AI Governance (Ring 1 — timeless principles)
- [13-AGENTIC-CORE-PRINCIPLES.md](../03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md) — SASE/SE 3.0, 7 Agentic Principles
- [14-AGENTIC-MATURITY-MODEL.md](../03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md) — L0→L3 progression
- [16-LONG-RUNNING-AGENT-PROTOCOL.md](../03-AI-GOVERNANCE/16-LONG-RUNNING-AGENT-PROTOCOL.md) — Checkpoint/resume/handoff (NEW 6.3.0)

### Implementation Patterns (Ring 2 — moved in 6.3.0)
- [MULTI-AGENT-PATTERNS.md](../07-Implementation-Guides/MULTI-AGENT-PATTERNS.md) — 13 collaboration patterns
- [AUTONOMOUS-CODEGEN-PATTERNS.md](../07-Implementation-Guides/AUTONOMOUS-CODEGEN-PATTERNS.md) — Quality pipeline
- [CLAUDE-MD-STANDARD.md](../05-Templates-Tools/03-Agent-Templates/CLAUDE-MD-STANDARD.md) — AI context doc standard

### Section 8 - Unified Specification Standard (6.0.0+)
- [SDLC-Specification-Standard.md](../05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md) - ⭐ **YAML + BDD format**
- [DESIGN_DECISIONS.md](../05-Templates-Tools/01-Specification-Standard/DESIGN_DECISIONS.md) - ⭐ **Lightweight ADRs**
- [SPEC_DELTA.md](../05-Templates-Tools/01-Specification-Standard/SPEC_DELTA.md) - ⭐ **Version tracking**
- [SDLC-Context-Authority-Methodology.md](./SDLC-Context-Authority-Methodology.md) - ⭐ **Dynamic AGENTS.md**

### Consolidated Documents (6.3.0)
- [SDLC-Stage-Lifecycle-Framework.md](./SDLC-Stage-Lifecycle-Framework.md) — Stage dependencies + exit criteria + tier requirements (3→1)
- [SDLC-Quality-Gates-Assurance-Framework.md](./Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md) — Anti-Vibecoding + Quality Gates (2→1)

### Governance & Compliance
- [SDLC-Sprint-Governance.md](./Governance-Compliance/SDLC-Sprint-Governance.md) — Pillar 2 (Sprint + Stage + Change Management)

### Documentation Standards
- [SDLC-Project-Structure-Standard.md](./Documentation-Standards/SDLC-Project-Structure-Standard.md) — Folder structure
- [SDLC-Naming-Standards.md](./Documentation-Standards/SDLC-Naming-Standards.md) — Naming + Header conventions
- [SDLC-Sprint-Planning-Guide.md](./Documentation-Standards/SDLC-Sprint-Planning-Guide.md) — Sprint planning guide

### Ring 3 (Implementation Guides — NEW 6.3.0)
- [Citizen-Developer-Guide.md](../07-Implementation-Guides/Citizen-Developer-Guide.md) — Non-technical user pathway

### Case Studies
- [Sprint Direction Confusion Case Study](../06-Case-Studies/BFlow-Sprint-86-Direction-Confusion-Case-Study.md) - Incident that triggered Pillar 2

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **6.3.2** | **Jun 3, 2026** | **Amendment B (PATCH)** — Mental Model #9 (Demand Before Surface) [DT]; Ship-Useful Principle (Constraint-First / Anti-Theater) [DT]; ON-DEMAND marker pattern; Anti-Theater Catalog (9 smells); NQH Inward Application Catalog (separate file). Self-eval 2026-09-03 (dvhiep APM facilitator; CEO + CTO co-deciders). External-adopter value [DT] — NQH dogfood-first. |
| **6.3.0** | **Mar 18, 2026** | **Agentic SDLC + Lean Ring 1** — 9 Mental Models (+Agent Continuity, +More People Build), Long-Running Agent Protocol (Ring 1), Citizen Developer Guide (Ring 3), ROI Calculator (Ring 2). Ring 1 consolidated: 41→30 files, -21% size. 42 tool-specific refs → 0. 9 docs moved to Ring 2. |
| 6.1.2 | Mar 9, 2026 | SOULs + TEAMs: 18 role templates + 10 team charters (Ring 2) |
| 6.1.0 | Feb 18, 2026 | Consolidation: Ring 1 slim, System Thinking + Crisis-to-Pattern, Multi-Agent Patterns |
| **6.0.6** | **Feb 16, 2026** | **MINOR: Anthropic Best Practices Integration** — CLAUDE.md Standard, Autonomous Codegen Patterns, MRP Template |
| **6.0.5** | **Feb 15, 2026** | **MINOR: RFC-001 Legacy Organization + Anti-Vibecoding SPEC-0001 alignment + 4 new Framework templates** (Go-Live Checklist, Go-Live Assessment, Maturity Assessment, Risk Register) |
| **6.0.4** | **Feb 8, 2026** | **MINOR: TDD Workflow Integration + 3-Phase Sprint Enhancement** - RED-GREEN-REFACTOR cycle, tier-aware coverage (LITE 70% → ENT 95%), Spec Converter (SpecIR) |
| **6.0.3** | **Feb 5, 2026** | **MINOR: Boris Cherny Best Practices Consolidation** - 5 RFCs → Framework structure, MCP Integration Guide, Git Workflow Patterns |
| **6.0.2** | **Feb 3, 2026** | **MINOR: E2E API Testing Enhancement (RFC-SDLC-602)** - 6-phase testing workflow, Stage 03↔05 cross-reference, OWASP API Top 10 |
| **6.0.1** | **Feb 1, 2026** | **MINOR: SPEC-0021 Stage Consistency Validation** - 4-stage consistency model, pre/post-implementation checklists, artifact integrity hashing, CLI validation commands |
| **6.0.0** | **Jan 28, 2026** | **MAJOR: 7-Pillar + 2-Section Architecture, Unified Specification Standard** |
| 5.3.0 | Jan 27, 2026 | Section 7 - Quality Assurance System + Stage Dependencies |
| 5.2.0 | Jan 22, 2026 | Principle-Centric Framework: 7-Pillar + AI Governance Principles |
| 5.1.3 | Jan 18, 2026 | 7-Pillar Architecture: Sprint Planning Governance as Pillar 2 |
| 5.1.2 | Dec 24, 2025 | Documentation vs Code separation, 6-pillar structure |
| 5.1.1 | Dec 12, 2025 | Correct stage numbering, Legacy/Archive folder skip |
| 5.1.0 | Dec 11, 2025 | SASE integration, Stage 03 INTEGRATE repositioned |
| 5.0.0 | Dec 5, 2025 | 4-Tier Classification, Governance standards |
| 4.9.0 | Nov 13, 2025 | 10-Stage lifecycle, complete documentation |
| 4.8.0 | Oct 2025 | Design Thinking foundation |

---

**Last Updated**: March 18, 2026
**Maintained By**: Framework Team
**Authority**: CTO + CPO Approved
**Case Study**: [Sprint Direction Confusion](../06-Case-Studies/BFlow-Sprint-86-Direction-Confusion-Case-Study.md)
**Quality Assurance**: [SDLC-Quality-Gates-Assurance-Framework.md](./SDLC-Quality-Gates-Assurance-Framework.md) - Section 7
**Unified Specs**: [Specification Standard](../05-Templates-Tools/01-Specification-Standard/) - Section 8
**AI Governance**: Aligned with [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) principles
