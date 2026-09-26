---
document_id: "TRAINING-MODULE-01"
title: "Module 01: SDLC 6.3.0 Overview — Complete 10-Stage Lifecycle"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "4 hours (6 parts)"
audience: "All team members — developers, pod leads, architects, product managers, executives"
prerequisite: "None (this is the foundation module)"
format: "Lecture + Discussion + Quiz"
---

# Module 01: SDLC 6.3.0 Overview — Complete 10-Stage Lifecycle

> **Core principle**: "Ask WHY before asking HOW." Every great product begins with understanding the purpose, not the technology.

---

## 1. What Is SDLC 6.3.0? (30 minutes)

### Definition

**SDLC 6.3.0** is a battle-tested Software Development Lifecycle framework featuring a **complete 10-stage lifecycle** (WHY to GOVERN), **7-Pillar Architecture**, **SASE Integration** (SE 3.0), and an **AI+Human orchestration model**.

### Key Characteristics

| Characteristic | Description |
|---------------|-------------|
| **10-Stage Lifecycle** | Foundation (WHY) through Govern (strategic oversight) |
| **Integration-First** | Stage 03 (Integrate) comes BEFORE Stage 04 (Build) |
| **SASE Integration** | Software Agentic Software Engineering (SE 3.0) |
| **AI+Human Orchestration** | SE4H (Human Coach) + SE4A (AI Executor) |
| **4-Tier Classification** | LITE / STANDARD / PROFESSIONAL / ENTERPRISE |
| **Production-Proven** | Battle-tested across multiple production platforms in NQH Technology Ecosystem |

### Why SDLC 6.3.0?

```
Industry Reality (Standish Group, 2020):
  70% of features rarely or never used
  64% of features NOT essential (waste)
  45% of features built are never used at all

Root Cause: Building solutions before understanding problems

SDLC 6.3.0 Solution:
  Design Thinking validation BEFORE coding
  Integration-First approach (API contracts before code)
  SASE framework for AI-human collaboration
  Evidence-based quality gates at every stage
```

---

## 2. The 10-Stage Complete Lifecycle (45 minutes)

Every stage answers a fundamental question. Together they form a complete journey from purpose to governance.

| Stage | Name | Question | Key Outputs |
|-------|------|----------|-------------|
| 00 | **Foundation** | WHY are we building this? | Project charter, business case, vision |
| 01 | **Planning** | WHAT will we build? | Requirements, user stories, backlog |
| 02 | **Design** | HOW will we build it? | Architecture diagrams, technical specs |
| 03 | **Integrate** | How do systems CONNECT? | API contracts, data flows, integration architecture |
| 04 | **Build** | Let us BUILD it! | Source code, unit tests, technical docs |
| 05 | **Test** | Does it WORK? | Test reports, quality metrics, bug reports |
| 06 | **Deploy** | How do we RELEASE it? | Release notes, deployment scripts, rollback plan |
| 07 | **Operate** | How do we RUN it? | Operational metrics, incident reports, runbooks |
| 08 | **Collaborate** | How do we WORK TOGETHER? | Review reports, knowledge base, retrospectives |
| 09 | **Govern** | Does it ALIGN with strategy? | Governance reports, audit results, compliance |

### The Integration-First Shift

This is the single most important change in SDLC 5.1.0+ compared to traditional approaches:

```
Traditional SDLC:
  Design -> Build -> Test -> ... -> Integrate (last)
  Problem: Integration issues discovered late
  Cost: High rework, delayed delivery

SDLC 6.3.0:
  Design -> INTEGRATE -> Build -> Test -> ...
  Benefit: API contracts defined before code
  Result: Fewer surprises, parallel development possible
```

**Why it matters**:
- API contracts are the "common language" between teams
- Defining contracts first eliminates miscommunication
- Early integration surfaces issues before code is written
- Contract-first development enables parallel workstreams

### Documentation Mapping

Stage mapping applies ONLY to `/docs` folders. Code folders (`backend/`, `frontend/`) are organizational units, NOT stage-mapped.

```
docs/00-foundation/   -> Stage 00: Foundation
docs/01-planning/     -> Stage 01: Planning
docs/02-design/       -> Stage 02: Design
docs/03-integrate/    -> Stage 03: Integration
docs/04-build/        -> Stage 04: Build
docs/05-test/         -> Stage 05: Test
docs/06-deploy/       -> Stage 06: Deploy
docs/07-operate/      -> Stage 07: Operations
docs/08-collaborate/  -> Stage 08: Collaboration
docs/09-govern/       -> Stage 09: Governance
```

---

## 3. SASE Integration Overview (30 minutes)

### What Is SASE?

**SASE (SE 3.0)** = Software Agentic Software Engineering. It defines how humans and AI agents collaborate with clear roles and structured artifacts.

```
SE 1.0 (Traditional):  Human writes all code
SE 2.0 (AI-Assisted):  AI suggests, human accepts/rejects
SE 3.0 (SASE):         AI executes tasks, human guides and validates
```

### SE4H vs SE4A

| Aspect | SE4H (Human Coach) | SE4A (AI Executor) |
|--------|--------------------|--------------------|
| Role | Guide and supervise | Execute and implement |
| Key skill | Intent specification | Code generation |
| Artifacts created | BRS, MTS, VCR | LPS, CRP, MRP |
| Decision authority | **FINAL** (veto power) | **NONE** (propose only) |

### Stage-by-Stage AI Integration

| Stage | SE4H % | SE4A % | AI Activities |
|-------|--------|--------|---------------|
| 00 Foundation | 100% | 0% | None (human-only strategic decisions) |
| 01 Planning | 80% | 20% | Requirements analysis assistance |
| 02 Design | 60% | 40% | Design pattern suggestions |
| 03 Integrate | 40% | 60% | API contract generation |
| 04 Build | 30% | 70% | Code implementation |
| 05 Test | 30% | 70% | Test generation and execution |
| 06 Deploy | 40% | 60% | Deployment script generation |
| 07 Operate | 50% | 50% | Monitoring setup |
| 08 Collaborate | 40% | 60% | Code review automation |
| 09 Govern | 90% | 10% | Compliance report generation |

---

## 4. 4-Tier Classification System (30 minutes)

Teams select a tier based on team size. The tier determines which stages are mandatory and how much documentation is required.

| Tier | Team Size | Mandatory Stages | Documentation Level |
|------|-----------|-----------------|---------------------|
| **LITE** | 1-2 | 00, 01, 02, 04 | README + .env.example |
| **STANDARD** | 3-10 | 00-02, 04-06 | + CLAUDE.md + /docs |
| **PROFESSIONAL** | 10-50 | All 10 stages | + Full ADRs + Compliance |
| **ENTERPRISE** | 50+ | All 10 stages + Audit | + Executive Reports + Audit Trail |

### Tier-Specific Requirements

```
LITE (1-2 members):
  Tests: Basic unit tests
  SASE Level: L0-L1
  Docs: Minimal

STANDARD (3-10 members):
  Tests: Unit + Integration
  SASE Level: L1-L2
  Docs: CLAUDE.md + stage folders

PROFESSIONAL (10-50 members):
  Tests: Unit + Integration + E2E
  SASE Level: L2
  Docs: Full ADRs, compliance docs

ENTERPRISE (50+ members):
  Tests: Full suite + Performance
  SASE Level: L2-L3
  Docs: Executive reports, audit trails
```

---

## 5. Quality Standards and Proven Results (30 minutes)

### Quality Targets

| Metric | Minimum | Target |
|--------|---------|--------|
| Unit Test Coverage | 80% | 90% |
| Integration Test Coverage | 70% | 85% |
| E2E Test Coverage | 60% | 75% |
| API Response (p50) | <50ms | <30ms |
| API Response (p95) | <100ms | <50ms |
| Uptime | 99.9% | 99.95% |
| Mock Instances | 0 | 0 |

### Production Validation

Framework đã được áp dụng để phát triển các platform trong NQH Technology Ecosystem.
Quantified ROI metrics deferred to post-go-live measurement (BFlow GA pending).

| Platform | Duration | Status |
|----------|----------|--------|
| Platform A | 52 days | In production |
| Platform B | 4 weeks | In production |
| Platform C | 6 weeks | In production |

### Productivity Gains

```
Design Thinking:   Significant time savings vs traditional waterfall
Code Review:       Fast turnaround with AI assistance (Tier 3)
Crisis Resolution: 24-48 hours (proven multiple times)
Test Coverage:     90%+ with real services only
```

---

## 6. Hands-on Discussion and Quiz (75 minutes)

### Discussion Questions (30 minutes)

**1.** Why does SDLC 6.3.0 place Integration (Stage 03) before Build (Stage 04)?

**2.** What is the difference between SE4H and SE4A? Who has final decision authority?

**3.** Your team has 8 members. Which tier applies? Which stages are mandatory?

**4.** A developer wants to skip Stage 00 (Foundation) because "we already know what to build." Is this acceptable? Why or why not?

**5.** Name three benefits of the Zero Mock Policy.

### Quiz (45 minutes, 20 questions, 80% pass rate required)

**Sample Questions**:

**Q1.** How many stages does the SDLC 6.3.0 lifecycle contain?
- a) 6
- b) 8
- c) **10** (correct)
- d) 12

**Q2.** Which stage comes BEFORE Build in SDLC 6.3.0?
- a) Test
- b) Deploy
- c) **Integrate** (correct)
- d) Operate

**Q3.** Who has final decision authority in the SASE framework?
- a) AI Agent
- b) **Human (SE4H)** (correct)
- c) Both equally
- d) Depends on the stage

**Q4.** What is the minimum unit test coverage required?
- a) 60%
- b) 70%
- c) **80%** (correct)
- d) 90%

**Q5.** In a team of 15 people, which tier applies?
- a) LITE
- b) STANDARD
- c) **PROFESSIONAL** (correct)
- d) ENTERPRISE

---

## Reference Materials

| Document | Location |
|----------|----------|
| SDLC 6.3.0 Framework | `SDLC-Enterprise-Framework/README.md` |
| Core Methodology | `02-Core-Methodology/SDLC-Core-Methodology.md` |
| Stage Lifecycle Framework | `02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md` |
| System Thinking Foundation | `02-Core-Methodology/SDLC-System-Thinking-Foundation.md` |
| Executive Summary | `01-Overview/SDLC-Executive-Summary.md` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | What Is SDLC 6.3.0 — definition, characteristics, rationale | 30 min |
| 2 | The 10-Stage Complete Lifecycle — each stage explained | 45 min |
| 3 | SASE Integration Overview — SE4H vs SE4A, stage mapping | 30 min |
| 4 | 4-Tier Classification System — LITE to ENTERPRISE | 30 min |
| 5 | Quality Standards and Proven Results — metrics, ROI | 30 min |
| 6 | Discussion and Quiz — 5 questions + 20-item quiz | 75 min |
| | **Total** | **4h** |

### After completing this module, participants must be able to:

1. Explain the 10-stage lifecycle and the question each stage answers.
2. Describe why Integration (Stage 03) comes before Build (Stage 04).
3. Distinguish between SE4H (Human Coach) and SE4A (AI Executor).
4. Select the correct tier for a given team size.
5. State the minimum quality targets (test coverage, API response time, zero mocks).

> **Remember**: "Ask WHY before asking HOW." Understanding the purpose prevents building the wrong thing.

---

## Assessment Questions

**Q1.** What is the core innovation of the Integration-First approach?
> **Answer**: API contracts are defined BEFORE code is written (Stage 03 before Stage 04), eliminating late-stage integration surprises.

**Q2.** Can an AI agent approve a merge request without human validation?
> **Answer**: No. SE4A (AI) can only propose. SE4H (Human) always has final decision authority via the VCR (Validation Certificate Report).

**Q3.** A solo developer building a small internal tool — which tier and which stages?
> **Answer**: LITE tier (1-2 members). Mandatory stages: 00 (Foundation), 01 (Planning), 02 (Design), 04 (Build).

**Q4.** What is the Zero Mock Policy?
> **Answer**: NEVER use mock, fake, or dummy data or implementations. All code must use real databases, real API calls, and real data patterns. No exceptions.

**Q5.** Where has the SDLC Framework been validated in production?
> **Answer**: Across multiple platforms in the NQH Technology Ecosystem (BFlow ERP, NQH-Bot WFM, MTEP PaaS, plus tech products SDLC Orchestrator and MTClaw). Quantified ROI metrics deferred to post-go-live measurement.
