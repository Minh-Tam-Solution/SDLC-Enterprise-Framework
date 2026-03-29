# SASE Artifact Templates
## Streamlined Templates for Human-Agent Collaboration

**Version**: 6.2.1
**Date**: March 18, 2026
**Status**: ACTIVE - PRODUCTION READY
**Pillar**: 5 - SASE Integration
**Framework**: SDLC 6.2.1 + SASE/SE 3.0 Integration
**Reference**: arXiv:2509.06216v2 (Software Agentic Software Engineering)

---

## Overview

**SASE (Software Agentic Software Engineering)** defines artifact templates for structured human-agent collaboration. As of SDLC 6.2.0, we use:

- **AGENTS.md** - Industry standard for AI context (replaces BRS/MTS)
- **3 Governance Artifacts** - CRP, MRP, VCR for oversight and audit

---

## Current SASE Artifacts

| # | Artifact | Created By | Purpose | Template |
|---|----------|------------|---------|----------|
| - | **AGENTS.md** | SE4H (Human) | Industry-standard AI guidance | [AGENTS-MD-Template.md](AGENTS-MD-Template.md) |
| 01 | **CRP** | SE4A (Agent) | Consultation Request Protocol | [01-CRP-Template.md](01-CRP-Template.md) |
| 02 | **MRP** | SE4A (Agent) | Merge-Readiness Pack (5-point evidence) | [02-MRP-Template.md](02-MRP-Template.md) |
| 03 | **VCR** | SE4H (Human) | Version Controlled Resolution | [03-VCR-Template.md](03-VCR-Template.md) |

### Why This Set?

- **AGENTS.md**: Industry standard with 60,000+ projects using it. Native support in Cursor, Copilot, Claude Code, OpenCode, RooCode.
- **CRP**: Enables agents to escalate uncertainty to humans
- **MRP**: Provides structured evidence for code review
- **VCR**: Creates audit trail for approvals

---

## Workflow

### AGENTS.md-Based Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│               SASE WORKFLOW (SDLC 6.2.0)                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Human                          Agent                               │
│    │                              │                                 │
│    │─── AGENTS.md (repo) ────────▶│  (AI reads conventions)        │
│    │                              │                                 │
│    │─── GitHub Issue/Task ───────▶│  (Task specification)          │
│    │                              │                                 │
│    │◀── Dynamic Overlay ─────────│  (Context via PR comment)       │
│    │                              │                                 │
│    │                    [Execute Task]                              │
│    │                              │                                 │
│    │◀── CRP (if uncertain) ──────│  (Escalate to human)           │
│    │                              │                                 │
│    │─── Answer CRP ──────────────▶│                                │
│    │                              │                                 │
│    │                    [Complete]                                  │
│    │                              │                                 │
│    │◀── MRP (5-point evidence) ──│  (Merge readiness)             │
│    │                              │                                 │
│    │─── VCR (Approve/Reject) ────▶│  (Human decision)              │
│    │                              │                                 │
│    ├── GitHub Check ─────────────▶│  (Enforcement)                 │
│    │                              │                                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Template Summaries

### AGENTS.md Template

**Created by**: SE4H (Human - Agent Coach)
**Purpose**: Industry-standard AI guidance file

```markdown
# AGENTS.md

## Project Context
- What we're building
- Why it matters

## Architecture
- Tech stack
- Key patterns

## Code Standards
- Style guide
- Best practices

## Current Tasks
- Sprint goals
- Acceptance criteria
```

---

### 01-CRP-Template.md (Consultation Request Protocol)

**Created by**: SE4A (Agent - Agent Executor)
**Purpose**: Escalate uncertainty to human

```markdown
# Consultation Request

## Question
What needs human decision?

## Context
Background information

## Options Considered
1. Option A (pros/cons)
2. Option B (pros/cons)

## Recommendation
Agent's suggested approach

## Impact
Consequences of each choice
```

---

### 02-MRP-Template.md (Merge-Readiness Pack)

**Created by**: SE4A (Agent - Agent Executor)
**Purpose**: 5-point evidence for code review

```markdown
# Merge-Readiness Pack

## 1. What Changed
Summary of code changes

## 2. Why Changed
Alignment with requirements

## 3. How Tested
Test results and coverage

## 4. Risk Assessment
Potential issues identified

## 5. Rollback Plan
How to revert if needed
```

---

### 03-VCR-Template.md (Version Controlled Resolution)

**Created by**: SE4H (Human - Agent Coach)
**Purpose**: Approval record with audit trail

```markdown
# Version Controlled Resolution

## Decision
APPROVED | REJECTED | NEEDS_CHANGES

## MRP Review
Summary of review findings

## Conditions
Any conditions for approval

## Approver
Name and signature

## Timestamp
Date and time of decision
```

---

### SOUL Role Templates (NEW 6.1.2)

17 SASE role-specific personas for AI agents:
- 8 SE4A executors: coder, tester, architect, pm, pjm, devops, fullstack, reviewer
- 3 SE4H advisors: ceo, cto, cpo
- 1 Router: assistant
- 1 SE4A support: researcher
- 4 Optional (non-SDLC): writer, sales, cs, itadmin

See [souls/README.md](souls/README.md) for full index and tier availability matrix.

### TEAM Charters (NEW 6.1.2)

10 team composition templates:
- 7 SDLC function teams: dev, qa, design, executive, fullstack, ops, planning
- 3 Organizational teams: advisory, business, engineering

See [teams/](teams/) directory.

---

## Agentic Maturity Levels (Updated for 5.2.0)

| Level | Name | Artifacts Used |
|-------|------|----------------|
| **L0** | Tool-Assisted | None (ad-hoc prompts) |
| **L1** | Agent-Assisted | AGENTS.md + MRP + VCR |
| **L2** | Structured Agentic | AGENTS.md + CRP + MRP + VCR |
| **L3** | Lifecycle Agentic | All + Planning Mode + Dynamic Context |

### Getting Started

**For Level 1** (Start Here):
1. Create `AGENTS.md` with project context
2. Agent produces work with MRP evidence
3. Human approves with VCR

**For Level 2** (Full Workflow):
1. Configure AGENTS.md with full standards
2. Agent uses CRP when uncertain
3. Continue with MRP → VCR flow

**For Level 3** (Advanced):
1. Enable Planning Mode for >15 LOC changes
2. Use Dynamic Context Overlay for gates
3. Integrate with SDLC Orchestrator

---

## Related Documents

- [SDLC-Agentic-Core-Principles](../../03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md)
- [SDLC-Agentic-Maturity-Model](../../03-AI-GOVERNANCE/14-AGENTIC-MATURITY-MODEL.md)
- [AI Agent Best Practices 2026](../../04-AI-TOOLS-LANDSCAPE/best-practices-2026/README.md)

---

**Document Status**: ACTIVE - PRODUCTION READY
**Last Updated**: February 14, 2026
**Framework Version**: 6.2.0
