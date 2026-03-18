---
title: "Agentic Core Principles"
version: "6.2.0"
section: "03-AI-GOVERNANCE"
ring: "Core"
type: "Standard"
status: "ACTIVE"
last_updated: "2026-02-18"
author: "SE 3.0 Track 1 — CTO Approved"
origin: "arXiv:2509.06216v2 (SASE Framework)"
---

# AGENTIC CORE PRINCIPLES

> **SDLC 6.1.2** — Software Agentic Software Engineering (SASE) Integration
>
> This document defines the **7 Agentic Principles** and the **SE4H/SE4A framework**
> that govern how humans and AI agents collaborate within the SDLC lifecycle.

---

## 1. INTRODUCTION

### 1.1 The Evolution to Software 3.0

| Era | Model | Who Writes Code | Quality Gate |
|-----|-------|-----------------|--------------|
| **SE 1.0** | Waterfall/Agile | Humans only | Manual review |
| **SE 2.0** | AI-Assisted | Humans + AI autocomplete | Human review + CI |
| **SE 3.0** | Agentic | AI agents execute, humans govern | Evidence-based gates + policy-as-code |

Software 3.0 doesn't replace developers — it redefines their role from **writing code** to **designing feedback loops** that govern AI agents producing code.

### 1.2 SASE Framework Overview

The **Software Agentic Software Engineering (SASE)** framework (arXiv:2509.06216v2) introduces a dual-modality model:

- **SE4H** (Software Engineering for Humans) — the **Agent Coach** role: define intent, review evidence, approve outputs, make architectural decisions.
- **SE4A** (Software Engineering for Agents) — the **Agent Executor** role: implement intent, gather evidence, produce artifacts, request consultation when uncertain.

This separation ensures **human accountability** while enabling **AI productivity**.

### 1.3 Dual-Modality Principle

```
┌─────────────────────────────────────────────────┐
│              DUAL-MODALITY MODEL                 │
│                                                  │
│  SE4H (Agent Coach)    SE4A (Agent Executor)     │
│  ┌───────────────┐    ┌───────────────┐         │
│  │ Define intent  │───>│ Execute tasks │         │
│  │ Review MRP     │<───│ Produce MRP   │         │
│  │ Issue VCR      │    │ Request CRP   │         │
│  │ Set policies   │    │ Follow AGENTS │         │
│  └───────────────┘    └───────────────┘         │
│         │                    │                   │
│         └──── AGENTS.md ─────┘                   │
│              (shared context)                    │
└─────────────────────────────────────────────────┘
```

**Key artifacts** in the SASE workflow:
- **AGENTS.md** — Shared context file (industry standard, 60K+ projects, native IDE support)
- **CRP** — Consultation Request Protocol (agent → human escalation)
- **MRP** — Merge-Readiness Pack (evidence package for code merge)
- **VCR** — Version Controlled Resolution (human decision record)

> **Note on deprecated terms**: Legacy BRS (BriefingScript) and MTS (MentorScript) are superseded by AGENTS.md. CRP, MRP, and VCR remain **ACTIVE**.
> See [AGENTS.md Template](../05-Templates-Tools/04-SASE-Artifacts/AGENTS-MD-Template.md) for the current standard.

---

## 2. SE4H vs SE4A FRAMEWORK

### 2.1 Role Distinction

| Dimension | SE4H (Agent Coach) | SE4A (Agent Executor) |
|-----------|--------------------|-----------------------|
| **Role** | Human — designs, reviews, decides | AI — implements, gathers, produces |
| **Authority** | Full decision-making | Delegated execution only |
| **Accountability** | Legally and ethically responsible | None (tool, not person) |
| **Key Output** | VCR (decisions), policies, reviews | MRP (evidence), CRP (questions), code |
| **Escalation** | Receives CRP, resolves | Sends CRP when uncertain |

### 2.2 SDLC 10-Stage Mapping

| Stage | SE4H (Agent Coach) | SE4A (Agent Executor) | Primary Artifacts |
|-------|--------------------|-----------------------|-------------------|
| 00 Foundation | Define problem & vision | — (human-only) | Problem statement |
| 01 Planning | Write requirements, set criteria | — (human-only) | AGENTS.md, specs |
| 02 Design | Review architecture, approve ADRs | Propose designs via CRP | ADRs, architecture docs |
| 03 Integration | Define contracts, approve APIs | Build adapters, generate code | API specs, integration tests |
| 04 Build | Review MRP, issue VCR | Execute tasks, produce MRP | Code, MRP, VCR |
| 05 Test | Review test coverage, approve | Run tests, collect evidence | Test reports, coverage |
| 06 Deploy | Approve deployment, verify | Execute deployment scripts | Deployment proof |
| 07 Operate | Respond to CRP alerts | Monitor, generate CRP on anomalies | Incident reports, CRP |
| 08 Collaborate | Review explanations, share knowledge | Explain decisions, support reviews | Review comments |
| 09 Govern | Set policies, audit | Enforce policies, report compliance | Audit logs, compliance |

---

## 3. THE 7 AGENTIC PRINCIPLES

### Principle 1: AGENTS.md First

> Every AI-assisted project MUST have an AGENTS.md before any agent work begins.

AGENTS.md is the **single source of truth** for agent context — project architecture, conventions, constraints, and workflow rules. Without it, agents guess, and guessing produces waste.

**Workflow**: Create AGENTS.md → Agent reads context → Agent executes with awareness → Update AGENTS.md on learnings.

**Anti-pattern**: Starting agent work without AGENTS.md. Symptom: high CRP rate, code that ignores team conventions.

> **Dynamic Context Overlay** is the **true moat**: gate-triggered AGENTS.md updates (e.g., G3 pass → "STRICT MODE: bug fixes only") turn static guidance into active governance. See [AGENTS.md Template](../05-Templates-Tools/04-SASE-Artifacts/AGENTS-MD-Template.md).

### Principle 2: Evidence-Based MRP

> Every agent output MUST be accompanied by a Merge-Readiness Pack with verifiable evidence.

MRP is the evidence package that proves code is ready to merge. No evidence = no merge.

**5-point MRP evidence check**:
1. **Tests pass** — unit + integration + E2E (with coverage %)
2. **SAST clean** — Semgrep scan shows no critical/high findings
3. **Context preserved** — code follows AGENTS.md conventions
4. **Requirements traced** — links code to requirement/user story
5. **Performance verified** — benchmarks within budget (<100ms p95)

> See [MRP Template](../05-Templates-Tools/04-SASE-Artifacts/02-MRP-Template.md) for the complete format.

### Principle 3: Human Accountability

> Humans are **always** accountable for agent outputs. AI is a tool, not a person.

Every MRP approval requires a **VCR (Version Controlled Resolution)** — a signed, timestamped record of who reviewed what and what decision was made. "The AI did it" is never an acceptable justification.

**VCR requirements**: reviewer identity, timestamp, scope of review, decision (approve/reject/modify), rationale.

> See [VCR Template](../05-Templates-Tools/04-SASE-Artifacts/03-VCR-Template.md).

### Principle 4: Consultation Protocol (CRP)

> Agents MUST escalate to humans when confidence is low or impact is high.

CRP prevents agents from making consequential decisions autonomously. The escalation threshold is calibrated to project maturity:

| Maturity Level | CRP Threshold | What Triggers CRP |
|----------------|---------------|--------------------|
| L0 Tool-Assisted | N/A | Agent not used |
| L1 Agent-Assisted | Low confidence or any ambiguity | Architecture, security, API contracts, >50 LOC |
| L2 Structured Agentic | Medium confidence only | Cross-service changes, breaking changes |
| L3 Lifecycle Agentic | High-impact only | Security-critical, payment logic, policy changes |

**CRP SLA**: <4 hours response time. Delayed CRP = blocked agent = productivity loss.

> See [CRP Template](../05-Templates-Tools/04-SASE-Artifacts/01-CRP-Template.md).

### Principle 5: Mentorship-as-Code

> Agent behavior is shaped by documented patterns, not ad-hoc instructions.

Instead of telling agents what to do each time, encode team knowledge into AGENTS.md:
- **Code standards** → AGENTS.md conventions section
- **Architecture patterns** → AGENTS.md module zones
- **Common pitfalls** → AGENTS.md debugging section
- **Decision rationale** → AGENTS.md ADR references

The hierarchy: **Project AGENTS.md** (specific) > **Org AGENTS.md** (general) > **Framework defaults** (baseline).

### Principle 6: Dual Workbenches (ACE + AEE)

> Separate the human command environment from the agent execution environment.

| Environment | Purpose | Who Uses | Key Capabilities |
|-------------|---------|----------|------------------|
| **ACE** (Agent Command) | Define intent, review output | Humans | IDE integration, MRP review, VCR signing |
| **AEE** (Agent Execution) | Execute tasks, produce artifacts | Agents | Sandboxed runtime, tool access, evidence collection |

Separation ensures: (1) agents can't modify their own instructions, (2) humans maintain oversight, (3) execution is auditable and reproducible.

### Principle 7: Gradual Autonomy

> Agent autonomy increases as trust is established through evidence.

| Level | Name | Human Oversight | Trust Requirements |
|-------|------|-----------------|--------------------|
| **L0** | Tool-Assisted | 100% (human writes code) | None |
| **L1** | Agent-Assisted | High (review all MRPs) | — |
| **L2** | Structured Agentic | Medium (spot-check MRPs) | 10+ approved MRPs, CRP rate <20%, 3+ months at L1 |
| **L3** | Lifecycle Agentic | Low (exception-based) | 50+ approved MRPs, CRP rate <5%, 6+ months at L2 |

**Key insight**: Trust is **earned** through evidence, not **granted** by declaration. Each level requires measurable proof of reliability before promotion.

---

## 4. SASE DISCIPLINES × SDLC STAGES

The SASE framework defines 6 engineering disciplines. Each maps to primary SDLC stages:

| # | Discipline | Full Name | Primary Stages | Focus |
|---|------------|-----------|----------------|-------|
| 1 | **BriefingEng** | Briefing Engineering | 01 Planning | Effective AGENTS.md + task specs |
| 2 | **ALE** | Agentic Loop Engineering | 02 Design, 04 Build | LoopScript design + execution |
| 3 | **ATME** | Agentic Test & Monitoring | 05 Test, 07 Operate | Validation + observability |
| 4 | **AGE** | Agentic Governance | 09 Govern, 06 Deploy | Policies, compliance, audit |
| 5 | **ATLE** | Agentic Tool & Library | 03 Integration | ACE/AEE infrastructure |
| 6 | **ATIE** | Agentic Trust & Interpretability | 08 Collaborate | Explainability + trust calibration |

**Key metrics per discipline**:
- **BriefingEng**: CRP rate from briefs (lower = clearer), first-pass MRP approval rate
- **ALE**: Step success rate, checkpoint approval rate
- **ATME**: False positive/negative rate, mean time to detect (MTTD)
- **AGE**: Policy violation rate, audit completeness
- **ATLE**: Tool reliability (uptime), execution latency
- **ATIE**: Explanation clarity score, confidence calibration

---

## 5. GETTING STARTED

### Level 0 → Level 1 Checklist

**Week 1 — Foundation**:
- [ ] Identify a small, low-risk pilot project
- [ ] Create AGENTS.md using [template](../05-Templates-Tools/04-SASE-Artifacts/AGENTS-MD-Template.md)
- [ ] Validate AGENTS.md structure

**Week 2 — First Execution**:
- [ ] Agent reads AGENTS.md, produces execution plan
- [ ] Human approves plan
- [ ] Agent executes, produces MRP
- [ ] Human reviews MRP, issues VCR

**Week 3-4 — Iteration**:
- [ ] Repeat for 5-10 tasks, track CRP rate + approval rate
- [ ] Update AGENTS.md with learnings
- [ ] Document challenges and solutions

### Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| No AGENTS.md | High CRP rate, convention-ignoring code | Enforce Principle 1 strictly |
| Insufficient context | Code misses domain patterns | Invest in comprehensive AGENTS.md |
| Ignoring CRPs | Agent blocked, productivity drops | Set CRP SLA (<4 hours) |
| Rubber-stamping MRPs | Quality issues in production | Enforce 5-point evidence review |
| Blame-the-AI culture | Team disengaged | Remember Principle 3: humans are accountable |

---

## 6. GLOSSARY

| Term | Definition |
|------|------------|
| **ACE** | Agent Command Environment — tools for humans to command agents |
| **AEE** | Agent Execution Environment — sandboxed infrastructure for agent execution |
| **AGENTS.md** | Industry-standard AI context file (60K+ projects, native IDE support) |
| **CRP** | Consultation Request Protocol — agent → human escalation |
| **MRP** | Merge-Readiness Pack — evidence package for code merge |
| **SASE** | Software Agentic Software Engineering (arXiv:2509.06216v2) |
| **SE4A** | Software Engineering for Agents (Agent Executor role) |
| **SE4H** | Software Engineering for Humans (Agent Coach role) |
| **VCR** | Version Controlled Resolution — human decision record |
| ~~BRS~~ | ~~BriefingScript~~ — **DEPRECATED**, replaced by AGENTS.md |
| ~~MTS~~ | ~~MentorScript~~ — **DEPRECATED**, replaced by AGENTS.md code standards |

---

## 7. REFERENCES

### Primary Sources
1. **SASE Framework** — arXiv:2509.06216v2 ("Software Engineering for AI-Based Systems")
2. **SDLC 6.1.2 Core Methodology** — [SDLC-Core-Methodology.md](../02-Core-Methodology/SDLC-Core-Methodology.md)
3. **AGENTS.md Standard** — 60,000+ GitHub projects, native support in Cursor/Copilot/Claude Code

### SASE Artifact Templates
- [AGENTS.md Template](../05-Templates-Tools/04-SASE-Artifacts/AGENTS-MD-Template.md)
- [CRP Template](../05-Templates-Tools/04-SASE-Artifacts/01-CRP-Template.md)
- [MRP Template](../05-Templates-Tools/04-SASE-Artifacts/02-MRP-Template.md)
- [VCR Template](../05-Templates-Tools/04-SASE-Artifacts/03-VCR-Template.md)

### Related Documents
- [Planning Mode Principle](./03-Planning-Mode-Principle.md) — when to engage planning mode
- [Agentic Maturity Model](./14-AGENTIC-MATURITY-MODEL.md) — detailed L0-L3 assessment criteria
- [Autonomous Codegen Patterns](./11-AUTONOMOUS-CODEGEN-PATTERNS.md) — quality gates for AI-generated code
- [Multi-Agent Patterns](./12-MULTI-AGENT-PATTERNS.md) — team-based agent collaboration
- [CLAUDE.md Standard](./10-CLAUDE-MD-STANDARD.md) — project context file standard

---

**Document Status:** ACTIVE — PRODUCTION READY
**Version:** 6.2.0 | **Last Updated:** February 18, 2026
**Origin:** SASE Framework (arXiv:2509.06216v2) adapted for SDLC 6.1.2
