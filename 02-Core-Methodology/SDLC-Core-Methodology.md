# SDLC 5.1.1 Core Methodology

**Version**: 5.1.1
**Date**: December 12, 2025
**Status**: ACTIVE
**Authority**: Chairman + CEO + CPO + CTO Approved

---

## Executive Summary

SDLC 5.1.1 is a **10-Stage AI+Human Excellence Framework** integrating:
- **10 Lifecycle Stages** (00-09): Foundation → Govern
- **4-Tier Classification**: LITE → ENTERPRISE (team size-based)
- **SASE Integration** (SE 3.0): Software Agentic Software Engineering
- **Design Thinking Foundation**: 5-phase user-centered approach

**Heritage**: Built BY AI+Human Teams FOR AI+Human Teams

---

## The 10-Stage Lifecycle

```
┌────────────────────────────────────────────────────────────────────────┐
│                    SDLC 5.1.1 - 10 STAGES                              │
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

### Stage → Folder Mapping

| Stage | Name | Folder | Core Question |
|-------|------|--------|---------------|
| 00 | FOUNDATION | `00-foundation/` | WHY are we building this? |
| 01 | PLANNING | `01-planning/` | WHAT are we building? |
| 02 | DESIGN | `02-design/` | HOW will we build it? |
| 03 | INTEGRATE | `03-integrate/` | How does it connect? |
| 04 | BUILD | `04-build/` | Are we building it right? |
| 05 | TEST | `05-test/` | Does it work correctly? |
| 06 | DEPLOY | `06-deploy/` | How do we ship safely? |
| 07 | OPERATE | `07-operate/` | Is it running reliably? |
| 08 | COLLABORATE | `08-collaborate/` | Is the team effective? |
| 09 | GOVERN | `09-govern/` | Are we compliant & accountable? |

---

## 4-Tier Classification System

| Tier | Team Size | Required Stages | Documentation Level |
|------|-----------|-----------------|---------------------|
| **LITE** | 1-2 | 00, 01, 02, 04 | README + .env.example |
| **STANDARD** | 3-10 | 00-02, 04-06 | + CLAUDE.md + /docs |
| **PROFESSIONAL** | 10-50 | All 10 stages | + Full ADRs + Compliance |
| **ENTERPRISE** | 50+ | All 10 stages | + Executive Reports + Audit |

### Folder Structure by Tier

**LITE (1-2 members)**:
```
docs/
├── 00-foundation/
├── 01-planning/
├── 02-design/
└── 04-build/
```

**STANDARD (3-10 members)**:
```
docs/
├── 00-foundation/
├── 01-planning/
├── 02-design/
├── 04-build/
├── 05-test/
└── 06-deploy/
```

**PROFESSIONAL/ENTERPRISE (10+ members)**:
```
docs/
├── 00-foundation/
│   └── 99-legacy/     # Stage-level legacy
├── 01-planning/
│   └── 99-legacy/
├── 02-design/
│   └── 99-legacy/
├── 03-integrate/
│   └── 99-legacy/
├── 04-build/
│   └── 99-legacy/
├── 05-test/
│   └── 99-legacy/
├── 06-deploy/
│   └── 99-legacy/
├── 07-operate/
│   └── 99-legacy/
├── 08-collaborate/
│   └── 99-legacy/
├── 09-govern/
│   └── 99-legacy/
└── 10-archive/        # Project-level archive (NOT a stage)

backend/
└── 99-legacy/         # Legacy in backend

frontend/
└── 99-legacy/         # Legacy in frontend

tools/
└── 99-legacy/         # Legacy in tools
```

**Legacy/Archive Rules**:
- **10-archive**: ONLY at docs root (not a stage, holds unsorted legacy docs)
- **99-legacy**: within EACH stage (00-09) AND in backend, frontend, tools
- Content in legacy/archive folders is never validated or upgraded

---

## SASE Integration (SE 3.0)

### SE4H vs SE4A Distinction

| Aspect | SE4H (Agent Coach) | SE4A (Agent Executor) |
|--------|-------------------|----------------------|
| **Role** | Guide & supervise AI agents | Implement human-specified intent |
| **Primary Skills** | Intent specification, quality validation | Code generation, pattern consistency |
| **Artifacts Created** | BRS, MTS, VCR | LPS, CRP, MRP |
| **Decision Authority** | FINAL (veto power) | NONE (propose only) |

### Agentic Maturity Levels

| Level | Name | Characteristic | Artifacts |
|-------|------|----------------|-----------|
| **L0** | Tool-Assisted | AI as autocomplete | None |
| **L1** | Agent-Assisted | Structured handoff | BRS, MRP, VCR |
| **L2** | Structured Agentic | Full SASE workflow | All 6 + ACE/AEE |
| **L3** | Lifecycle Agentic | Proactive agents | Full + Memory |

### 7 Agentic Principles

1. **Brief-First** - BriefingScript before any agent work
2. **Evidence-Based MRP** - 5-point evidence for every merge
3. **Human Accountability** - Human responsible for shipped code
4. **Consultation Protocol** - CRP when agent uncertain
5. **Mentorship-as-Code** - Standards in MentorScript
6. **Dual Workbenches** - ACE for humans, AEE for agents
7. **Gradual Autonomy** - Trust earned from L0→L3

### SASE × SDLC Stage Mapping

| Stage | SASE Discipline | Primary Activity |
|-------|-----------------|------------------|
| 00 Foundation | None | Human-only strategic work |
| 01 Planning | BriefingEng | Create BRS for features |
| 02 Design | ALE + ATIE | Design LPS, MTS |
| 03 Integrate | ATME + ATIE | CRP generation, API contracts |
| 04 Build | ATLE | Build ACE/AEE |
| 05 Test | ALE + ATME | Execute LPS, generate MRP |
| 06 Deploy | ATME | Validation, coverage |
| 07 Operate | ATME + AGE | Monitoring, verification |
| 08 Collaborate | ATIE + AGE | Code review, team coordination |
| 09 Govern | AGE | Policy, audit |

**See**: [SDLC-Agentic-Core-Principles.md](./SDLC-Agentic-Core-Principles.md)

---

## Stage Details

### Stage 00: FOUNDATION (WHY?)

**Purpose**: Validate the problem is worth solving before any development begins.

**Key Activities**:
- Stakeholder interviews (CEO, CTO, users)
- Design Thinking: EMPATHIZE + DEFINE phases
- Market analysis and competitive research
- Business case development (ROI projection)
- Risk assessment

**Quality Gate G0**: Problem validated, business case approved

**Deliverables**:
- Problem Statement
- Business Case Document
- User Interview Summary
- Risk Register

---

### Stage 01: PLANNING (WHAT?)

**Purpose**: Define what to build with sufficient detail for estimation and design.

**Key Activities**:
- Functional Requirements (FR1-FRn)
- Non-Functional Requirements (NFR1-NFRn)
- User Stories (Epics → Stories → Tasks)
- Data Model design (ERD, Schema)
- API Specification (OpenAPI 3.0)

**Quality Gate G1**: Requirements complete, stakeholders approved

**Deliverables**:
- Functional Requirements Document
- Non-Functional Requirements
- User Stories with Acceptance Criteria
- Data Model ERD
- API Specification

---

### Stage 02: DESIGN (HOW?)

**Purpose**: Design the technical architecture and system components.

**Key Activities**:
- System Architecture (4-layer design)
- Database Schema (with migrations)
- API Design (REST/GraphQL)
- Security Architecture (RBAC, encryption)
- ADRs (Architecture Decision Records)

**Quality Gate G2**: Design approved by CTO/Tech Lead

**Deliverables**:
- System Architecture Document
- Technical Design Document
- Security Baseline
- ADRs

---

### Stage 03: INTEGRATE

**Purpose**: Define and setup all integration points before main development.

**Key Activities**:
- API contract definition (OpenAPI, Protobuf)
- Third-party integration setup (OAuth, payment, etc.)
- Event-driven architecture (Kafka, queues)
- Data integration patterns (ETL, CDC)
- Integration testing strategy

**Quality Gate**: API contracts validated, integration tests defined

**Deliverables**:
- API Contracts
- Integration Architecture
- Third-party Setup Guides
- Integration Test Plan

---

### Stage 04: BUILD

**Purpose**: Implement the designed solution with quality.

**Key Activities**:
- Sprint-based development
- Code review (PR process)
- Unit testing (80%+ coverage)
- CI/CD pipeline setup
- Feature documentation

**Quality Gate G3**: Feature complete, tests passing, code reviewed

**Deliverables**:
- Working code
- Unit tests
- Sprint logs
- Technical documentation

---

### Stage 05: TEST

**Purpose**: Comprehensive testing before production.

**Key Activities**:
- Integration testing
- End-to-end testing
- Performance testing (load, stress)
- Security testing (OWASP, penetration)
- User Acceptance Testing (UAT)

**Quality Gate**: All tests pass, UAT approved, zero P0 bugs

**Deliverables**:
- Test Reports
- Performance Benchmarks
- Security Audit Report
- UAT Sign-off

---

### Stage 06: DEPLOY

**Purpose**: Safe production deployment with rollback capability.

**Key Activities**:
- Pre-deployment checklist
- Blue-green / Canary deployment
- Rollback procedure validation
- War room activation
- Graduated rollout (10% → 50% → 100%)

**Quality Gate**: Successful deployment, rollback tested

**Deliverables**:
- Deployment Guide
- Release Notes
- Rollback Procedure
- Post-deployment Report

---

### Stage 07: OPERATE

**Purpose**: Production excellence and reliability.

**Key Activities**:
- Monitoring & alerting (Prometheus, Grafana)
- Incident response (P0 <15min, P1 <1h)
- SLA management (99.9%+ uptime)
- Maintenance (proactive, reactive)
- Continuous improvement

**Quality Gate**: SLA met, monitoring coverage >95%

**Deliverables**:
- Runbooks
- Monitoring Dashboards
- Incident Reports
- SLA Reports

---

### Stage 08: COLLABORATE

**Purpose**: Effective team coordination and knowledge sharing.

**Key Activities**:
- Team structure (RACI matrix)
- Communication protocols
- Knowledge management
- Training & onboarding
- Retrospectives

**Quality Gate**: Team velocity stable, satisfaction >8/10

**Deliverables**:
- Team Charter
- Communication Protocol
- Training Materials
- Retrospective Reports

---

### Stage 09: GOVERN

**Purpose**: Strategic oversight, compliance, and accountability.

**Key Activities**:
- Executive reporting (weekly/monthly/quarterly)
- Risk management
- Compliance monitoring
- Budget tracking
- Audit preparation

**Quality Gate**: Zero violations, budget ±10%

**Deliverables**:
- Executive Reports
- Risk Register Updates
- Compliance Reports
- Audit Documentation

---

## Design Thinking Integration

### 5 Phases → SDLC Stages

| Design Thinking | SDLC Stage | Output |
|----------------|------------|--------|
| **EMPATHIZE** | Stage 00 | User Interview Summaries |
| **DEFINE** | Stage 00 | Problem Statement |
| **IDEATE** | Stage 01-02 | Solution Concepts, Architecture |
| **PROTOTYPE** | Stage 04 | MVP, Working Code |
| **TEST** | Stage 05 | User Feedback, Iteration Plan |

### Quality Gates (Design Thinking)

**G0.1: Problem Definition**
- 5+ user interviews
- Pain point ranked (1-10)
- Problem statement validated

**G0.2: Solution Diversity**
- 100+ ideas generated
- Top 3 concepts selected
- Validation plan defined

---

## Governance & Compliance

### Quality Gates Summary

| Gate | Stage | Key Criteria |
|------|-------|--------------|
| G0.1 | 00 | Problem validated |
| G0.2 | 00 | Solution concepts validated |
| G1 | 01 | Requirements complete |
| G2 | 02 | Design approved |
| G3 | 04-05 | Ship ready |
| G4 | 06-07 | Production stable |

### DORA Metrics (PROFESSIONAL+ Tiers)

- **Deployment Frequency**: How often code deploys to production
- **Lead Time**: Commit to production time
- **MTTR**: Mean time to recovery
- **Change Failure Rate**: % deployments causing issues

### Security Requirements by Tier

| Tier | Security Level |
|------|---------------|
| LITE | Basic (.env protection) |
| STANDARD | Dependency scanning |
| PROFESSIONAL | OWASP ASVS Level 1 |
| ENTERPRISE | OWASP ASVS Level 2+ |

---

## Industry Standards Integration

```yaml
Standards Mapped:
  CMMI v3.0:      Maturity level mapping (LITE=L1-2, ENTERPRISE=L4-5)
  SAFe 6.0:       Lean Governance for gate approval
  DORA Metrics:   Deployment Frequency, Lead Time, MTTR, CFR
  OWASP ASVS:     Application Security Verification (Levels 1-3)
  NIST SSDF:      Secure Software Development Framework
  ISO/IEC 12207:  Process categories mapping
  Team Topologies: Stream-aligned, Platform, Enabling teams
```

---

## Related Documents

**Core Methodology**:
- [SDLC-Agentic-Core-Principles.md](./SDLC-Agentic-Core-Principles.md) - SASE principles
- [SDLC-Agentic-Maturity-Model.md](./SDLC-Agentic-Maturity-Model.md) - L0→L3 progression

**Governance & Compliance**:
- [SDLC-Quality-Gates.md](./Governance-Compliance/SDLC-Quality-Gates.md)
- [SDLC-Security-Gates.md](./Governance-Compliance/SDLC-Security-Gates.md)
- [SDLC-Observability-Checklist.md](./Governance-Compliance/SDLC-Observability-Checklist.md)

**Documentation Standards**:
- [SDLC-Document-Naming-Standards.md](./Documentation-Standards/SDLC-Document-Naming-Standards.md)
- [SDLC-Team-Communication-Protocol.md](./Documentation-Standards/Team-Collaboration/SDLC-Team-Communication-Protocol.md)

**Templates**:
- [SASE Artifact Templates](../03-Templates-Tools/SASE-Artifacts/)
- [Stage Templates](../03-Templates-Tools/2-Agent-Templates/)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 5.1.1 | Dec 12, 2025 | Correct stage numbering, Legacy/Archive folder skip |
| 5.1.0 | Dec 11, 2025 | SASE integration, Stage 03 INTEGRATE repositioned |
| 5.0.0 | Dec 5, 2025 | 4-Tier Classification, Governance standards |
| 4.9.0 | Nov 13, 2025 | 10-Stage lifecycle, complete documentation |
| 4.8.0 | Oct 2025 | Design Thinking foundation |

---

**Last Updated**: December 12, 2025
**Maintained By**: Framework Team
**Authority**: CTO Approved
