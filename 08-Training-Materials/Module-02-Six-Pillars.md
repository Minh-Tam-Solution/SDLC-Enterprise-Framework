---
document_id: "TRAINING-MODULE-02"
title: "Module 02: Six Universal Pillars"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "6 hours (8 parts)"
audience: "All team members — developers, pod leads, architects, product managers, executives"
prerequisite: "Module 01 (SDLC Overview)"
format: "Lecture + Workshop + Case Study"
---

# Module 02: Six Universal Pillars

> **Core principle**: "Every pillar was born from a real crisis." These are not theoretical ideals — they are battle-tested responses to production failures.

---

## 1. Overview of the Six Pillars (30 minutes)

SDLC 6.3.0 is built on **six universal pillars** — foundational principles proven across three platforms (production platforms).

| Pillar | Name | Crisis Origin | Core Idea |
|--------|------|---------------|-----------|
| 0 | Design Thinking Foundation | 70% of features never used | Validate BEFORE you build |
| 1 | AI-Native Excellence | Manual coding too slow | AI from day one, not as afterthought |
| 2 | Zero Mock Tolerance | 679 mocks in production | 100% real implementations, no exceptions |
| 3 | Quality Governance | Quality inconsistency | System Thinking + 3-tier code review |
| 4 | Documentation Permanence | Lost documentation | Docs are company assets, not byproducts |
| 5 | Continuous Compliance | Compliance failures | Ongoing monitoring, not one-time audits |

Each pillar reinforces the others. Design Thinking (P0) ensures clear intent for AI (P1). AI-Native (P1) enables faster real implementations for Zero Mock (P2). Zero Mock (P2) ensures accurate test results for Quality (P3). Quality (P3) produces reliable documentation (P4). Documentation (P4) provides the audit trail for Compliance (P5).

---

## 2. Pillar 0: Design Thinking Foundation (60 minutes)

### Definition

**Design Thinking** applies Stanford d.school's 5-phase methodology to software development. The goal: validate that you are building the right thing BEFORE writing any code.

### The 5 Phases

| Phase | Purpose | Key Activities | Deliverables |
|-------|---------|---------------|--------------|
| **Empathize** | Understand users deeply | User interviews (5-10), journey mapping, observation | Pain points, user quotes, empathy map |
| **Define** | Frame the right problem | Problem statement, POV statement, HMW questions | Validated problem definition |
| **Ideate** | Generate diverse solutions | Brainstorming (100+ ideas), SCAMPER, dot voting | Top 3 concepts ranked |
| **Prototype** | Build minimum testable version | Paper prototype (4h), digital mockup (1-3d), code (1-2w) | Working prototype |
| **Test** | Validate with real users | User testing (5-8 participants), feedback analysis | Ship / Iterate / Pivot decision |

### Integration with SDLC Stages

```
Design Thinking Phase    SDLC Stage        Deliverable
Empathize             -> Stage 00 (WHY)  -> User Persona, Pain Points
Define                -> Stage 00-01     -> Problem Statement
Ideate                -> Stage 01-02     -> Solution Options
Prototype             -> Stage 03        -> Working Prototype
Test                  -> Stage 05        -> User Feedback
```

### Proven ROI

```
Traditional approach:  6 months, 40-60% rework
Design Thinking:       4 weeks, <10% rework
Time savings:          96%

Platform B Case Study:
  Assumed problem: "Tracking is slow" (functional)
  Actual problem:  "I don't trust the data anymore" (emotional)
  Solution pivot:  Trust restoration instead of speed optimization
  Result:          90% trust restoration
```

---

## 3. Pillar 1: AI-Native Excellence (45 minutes)

### Definition

**AI-Native Excellence** means developing software with AI assistance from day one — not bolting it on later.

### SASE (SE 3.0) Framework

```
SE4H (Human Coach):
  - Creates BRS (BriefingScript) — describes intent
  - Defines MTS (MentorScript) — coding standards
  - Validates with VCR (Validation Certificate Report)
  - Has FINAL decision authority

SE4A (AI Executor):
  - Reads BRS, creates LPS (LoopScript) — execution plan
  - Generates CRP (Consultation Report Protocol) when uncertain
  - Creates MRP (Merge Request Protocol) with evidence
  - Authority: PROPOSE only
```

### AI-Native Development Flow

```
1. Human creates BRS (intent description)
   |
2. AI reads BRS, creates LPS (execution plan)
   |
3. AI executes code, generates MRP
   |
4. If uncertain: AI creates CRP, asks human
   |
5. Human validates with VCR
   |
6. Approved -> Merge
```

### AI Tool Selection

| Task Complexity | Recommended Tool | Rationale |
|----------------|-----------------|-----------|
| Simple (1-2 files) | Ollama (self-hosted) | Zero cost, full privacy |
| Standard features | Continue.dev + Ollama | Local, fast, sufficient |
| Complex (5+ files) | Claude Code | Best multi-file reasoning |
| Architecture review | Claude Code | Full codebase understanding |
| Security-critical | Human only | Too high risk for auto-generation |

---

## 4. Pillar 2: Zero Mock Tolerance (45 minutes)

### Definition

**Zero Mock Tolerance** means NEVER using mock, fake, or dummy data or implementations. No exceptions. No "temporary" mocks.

### The 679 Mock Crisis (September 2025)

```
Discovery: 679 mock instances in Platform B codebase
Impact:    78% production failure rate
Root cause: "Temporary" mocks became permanent
Response:  Emergency 48-hour elimination sprint
Result:    0 mocks, 95% success rate, policy born
```

### What Is Prohibited

```
Absolutely prohibited:
  - Mock data (test_data, fake_users, dummy_products)
  - Mock API responses (hardcoded JSON)
  - Mock databases (in-memory dicts, SQLite in-memory)
  - Mock services (FakeAuthService, mock_payment)
  - Placeholder code (TODO: implement later, pass)
  - Stub functions (return True, raise NotImplementedError)
```

### What Is Required Instead

```
Required replacements:
  - Real database connections (PostgreSQL, Redis)
  - Real API calls to backend services
  - Authentic data patterns (Vietnamese BHXH, VAT, VND)
  - Production-grade implementations from day 1
  - Complete functionality — no placeholders
```

### Enforcement

- **Pre-commit hooks**: Scan for mock_, fake_, dummy_, TODO:, FIXME:
- **CI/CD pipeline gates**: Build fails if mock patterns found
- **Code review checklist**: Zero Mock verification mandatory

---

## 5. Pillar 3: Quality Governance (45 minutes)

### System Thinking (4-Layer Iceberg Model)

```
Level 1 - Events (Visible):
  "What happened?" -> "API returns 500 error"

Level 2 - Patterns (Trends):
  "What trends recur?" -> "Errors increase during peak hours"

Level 3 - Structure (Systems):
  "What systems cause this?" -> "Insufficient connection pooling"

Level 4 - Mental Models (Root):
  "What assumptions drive this?" -> "Assumed traffic stays constant"
```

System Thinking forces the team to look below the surface. Fixing events (Level 1) without addressing structures (Level 3) guarantees recurrence.

### 3-Tier Code Review Framework

| Tier | Reviewer | Time | When | Tools |
|------|----------|------|------|-------|
| **Tier 1** | Developer + AI suggestions | 30-60 min | Small changes, hotfixes | GitHub PR + Copilot |
| **Tier 2** | AI reviewer + human approval | 10-15 min | Standard features | Claude Code |
| **Tier 3** | Automated tools + human oversight | <2 min | Large PRs, frequent changes | CodeRabbit, SonarQube |

### Quality Gates per Stage

Every stage has specific quality gates that must pass before proceeding:

```
Stage 00: Stakeholder sign-off, business case approved
Stage 01: Requirements reviewed, user stories accepted
Stage 02: Architecture approved, security review passed
Stage 03: API contracts finalized, integration tests planned
Stage 04: Code review passed, unit tests >=80%, zero mocks
Stage 05: Integration tests >=70%, E2E tests >=60%
Stage 06: Rollback plan ready, deployment scripts tested
Stage 07: Monitoring active, alerting configured
Stage 08: Documentation updated, retrospective completed
Stage 09: Compliance verified, audit trail complete
```

---

## 6. Pillar 4: Documentation Permanence (30 minutes)

### Definition

**Documentation Permanence** means documentation is a company asset, not a byproduct. Every stage has mandatory documentation, and documents follow a lifecycle.

### 10-Stage Documentation Standard

| Stage | Mandatory Documents | Location |
|-------|-------------------|----------|
| 00 Foundation | Project Charter, Business Case | docs/00-foundation/ |
| 01 Planning | Requirements Spec, Product Backlog | docs/01-planning/ |
| 02 Design | Architecture Docs, Technical Spec | docs/02-design/ |
| 03 Integrate | API Specification, Data Flow Diagram | docs/03-integrate/ |
| 04 Build | Code Documentation, Unit Test Report | docs/04-build/ |
| 05 Test | Test Plan, Test Results, Quality Metrics | docs/05-test/ |
| 06 Deploy | Release Notes, Deployment Guide | docs/06-deploy/ |
| 07 Operate | Runbook, Incident Response Plan | docs/07-operate/ |
| 08 Collaborate | Team Guidelines, Knowledge Base | docs/08-collaborate/ |
| 09 Govern | Governance Report, Compliance Checklist | docs/09-govern/ |

### Naming Standards

```
Documentation files:  kebab-case, no version in filename
  Examples: api-design-guide.md, deployment-guide.md

Documentation folders: kebab-case with stage prefix
  Examples: 00-foundation/, 04-build/, 09-govern/
```

### Document Lifecycle

```
Create -> Review -> Approve -> Publish -> Maintain -> Archive
```

Documents that are superseded move to `10-archive/{NN}-Legacy/` per RFC-001.

---

## 7. Pillar 5: Continuous Compliance (30 minutes)

### Definition

**Continuous Compliance** means ongoing monitoring and adherence to standards — not one-time audits.

### Automated Compliance

```
Pre-commit hooks:    Zero Mock scanning, code style
CI/CD pipeline:      Test coverage, security scanning, quality gates
Production:          Performance metrics, error rates, uptime tracking
```

### Manual Audits

```
Quarterly:  Security review
Annual:     Full compliance audit
As needed:  Architecture review after major changes
```

### Compliance Across 10 Stages

| Stage | Compliance Focus |
|-------|-----------------|
| 00 Foundation | Strategic alignment |
| 01 Planning | Requirements accuracy |
| 02 Design | Architecture standards |
| 03 Integrate | API contract compliance |
| 04 Build | Code quality, zero mock |
| 05 Test | Coverage targets met |
| 06 Deploy | Release standards |
| 07 Operate | SLA compliance |
| 08 Collaborate | Process adherence |
| 09 Govern | Overall compliance |

---

## 8. Workshop: Applying the Six Pillars (75 minutes)

### Exercise 1: Pillar Identification (20 minutes)

For each scenario, identify which pillar(s) are being violated:

**1.** A developer commits code with `fake_users = [...]` to speed up testing.

**2.** The team starts coding a new feature without interviewing any users.

**3.** API documentation was written during Sprint 1 but has not been updated since Sprint 15.

**4.** An AI agent merges a PR without any human reviewing the changes.

**5.** The team passes a security audit once per year but does not run automated security scans in CI/CD.

### Exercise 1 Answers

**1.** Pillar 2 (Zero Mock Tolerance) — fake data is prohibited.
**2.** Pillar 0 (Design Thinking) — must validate with users before building.
**3.** Pillar 4 (Documentation Permanence) — docs must be maintained, not abandoned.
**4.** Pillar 1 (AI-Native Excellence) — SE4H must give final approval via VCR.
**5.** Pillar 5 (Continuous Compliance) — compliance must be ongoing, not annual.

### Exercise 2: Daily Workflow (30 minutes)

Map a typical feature development to all six pillars:

```
1. Design Thinking (P0):  Empathize, define problem, validate
2. AI-Native (P1):        Create BRS, AI generates implementation
3. Zero Mock (P2):        Real database, real API calls from day 1
4. Quality Governance (P3): Code review (Tier 2), tests >=80%
5. Documentation (P4):    Update API docs, stage docs
6. Compliance (P5):       Pre-commit checks, CI/CD gates pass
```

### Exercise 3: Group Discussion (25 minutes)

**Question**: "Which pillar do you think is hardest to maintain consistently, and what would you do to improve adherence?"

Each group presents their answer (3 minutes per group).

---

## Reference Materials

| Document | Location |
|----------|----------|
| Design Thinking Principles | `02-Core-Methodology/SDLC-Design-Thinking-Principles.md` |
| System Thinking Foundation | `02-Core-Methodology/SDLC-System-Thinking-Foundation.md` |
| Quality Gates Framework | `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md` |
| SASE Agentic Principles | `03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` |
| Project Structure Standard | `02-Core-Methodology/Documentation-Standards/SDLC-Project-Structure-Standard.md` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | Overview of the Six Pillars | 30 min |
| 2 | Pillar 0: Design Thinking Foundation | 60 min |
| 3 | Pillar 1: AI-Native Excellence | 45 min |
| 4 | Pillar 2: Zero Mock Tolerance | 45 min |
| 5 | Pillar 3: Quality Governance | 45 min |
| 6 | Pillar 4: Documentation Permanence | 30 min |
| 7 | Pillar 5: Continuous Compliance | 30 min |
| 8 | Workshop: Applying the Six Pillars | 75 min |
| | **Total** | **6h** |

### After completing this module, participants must be able to:

1. Name all six pillars and the crisis that gave birth to each.
2. Apply Design Thinking's 5 phases to a real feature.
3. Explain the SASE framework and the SE4H/SE4A role split.
4. Enforce the Zero Mock Policy and identify violations in code.
5. Use the 3-tier code review framework for the appropriate context.
6. Maintain documentation per the 10-stage standard.

> **Remember**: "Every pillar was born from a real crisis." Ignoring a pillar means repeating the crisis that created it.

---

## Assessment Questions

**Q1.** Which pillar addresses the problem of building features nobody uses?
> **Answer**: Pillar 0 — Design Thinking Foundation. Validate with real users BEFORE building.

**Q2.** How many mock instances triggered the Zero Mock Policy?
> **Answer**: 679 mock instances in the Platform B codebase, causing a 78% production failure rate.

**Q3.** What are the three tiers of code review?
> **Answer**: Tier 1 (Manual + AI Assist, 30-60 min), Tier 2 (AI-Powered + human approval, 10-15 min), Tier 3 (Automated tools + human oversight, <2 min).

**Q4.** What is the Documentation Permanence principle?
> **Answer**: Documentation is a company asset, not a byproduct. Every stage has mandatory documents, and they must be maintained through their full lifecycle.

**Q5.** What distinguishes Continuous Compliance from traditional audits?
> **Answer**: Continuous Compliance uses automated checks (pre-commit, CI/CD, production monitoring) running constantly, rather than relying on periodic manual audits.
