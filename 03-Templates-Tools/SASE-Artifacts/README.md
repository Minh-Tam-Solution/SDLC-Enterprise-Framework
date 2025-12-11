# 📦 SASE Artifact Templates
## 6 Core Templates for Structured Human-Agent Collaboration

**Version**: 5.1.0
**Date**: December 11, 2025
**Status**: ACTIVE - PRODUCTION READY
**Framework**: SDLC 5.1.0 + SASE/SE 3.0 Integration
**Reference**: arXiv:2509.06216v2 (Software Agentic Software Engineering)

---

## 🎯 Overview

**SASE (Software Agentic Software Engineering)** introduces **6 artifact templates** for structured human-agent collaboration. These templates enable teams to transition from ad-hoc AI usage (Level 0) to structured agentic workflows (Level 2+).

### The 6 SASE Artifacts

| # | Artifact | Created By | Purpose |
|---|----------|------------|---------|
| 01 | **BriefingScript (BRS)** | SE4H (Human) | Task specification from human to agent |
| 02 | **LoopScript (LPS)** | SE4A (Agent) | Execution plan with iterations |
| 03 | **MentorScript (MTS)** | SE4H (Human) | Coding standards for agent compliance |
| 04 | **CRP** | SE4A (Agent) | Consultation Request Protocol - when uncertain |
| 05 | **MRP** | SE4A (Agent) | Merge-Readiness Pack - 5-point evidence |
| 06 | **VCR** | SE4H (Human) | Version Controlled Resolution - approval record |

---

## 🔄 Workflow

### Minimum Viable SASE (Level 1)

```
Human                          Agent
  │                              │
  │─── BriefingScript (BRS) ────▶│
  │                              │
  │                    [Execute Task]
  │                              │
  │◀── Merge-Readiness Pack ────│
  │        (MRP)                 │
  │                              │
  │─── VCR (Approve/Reject) ────▶│
  │                              │
```

### Full SASE Workflow (Level 2)

```
Human                          Agent
  │                              │
  │─── BriefingScript (BRS) ────▶│
  │                              │
  │─── MentorScript (MTS) ──────▶│
  │                              │
  │                    [Create LPS]
  │                              │
  │◀── LoopScript (LPS) ────────│
  │                              │
  │─── Approve LPS ─────────────▶│
  │                              │
  │                    [Execute]
  │                              │
  │◀── CRP (if uncertain) ──────│
  │                              │
  │─── Answer CRP ──────────────▶│
  │                              │
  │                    [Complete]
  │                              │
  │◀── MRP (5-point evidence) ──│
  │                              │
  │─── VCR (Approve/Reject) ────▶│
  │                              │
```

---

## 📋 Template Files

### 01-BriefingScript-Template.yaml
**Created by**: SE4H (Human - Agent Coach)
**Purpose**: Specify task for agent execution

```yaml
# Key sections:
task_specification:
  objective: "Clear statement of what needs to be done"
  acceptance_criteria: [...]
  constraints: [...]

context:
  project: "Project name"
  stage: "SDLC stage (00-09)"
  files_involved: [...]

expectations:
  quality_requirements: [...]
  timeline: "Expected completion"
```

---

### 02-LoopScript-Template.yaml
**Created by**: SE4A (Agent - Agent Executor)
**Purpose**: Execution plan with iterations

```yaml
# Key sections:
execution_plan:
  phases: [...]
  iterations: [...]
  checkpoints: [...]

deliverables:
  code_changes: [...]
  tests: [...]
  documentation: [...]
```

---

### 03-MentorScript-Template.md
**Created by**: SE4H (Human - Agent Coach)
**Purpose**: Coding standards for agent compliance

```markdown
# Key sections:
- Code Style Guidelines
- Architecture Patterns
- Naming Conventions
- Testing Requirements
- Documentation Standards
```

---

### 04-CRP-Template.md (Consultation Request Protocol)
**Created by**: SE4A (Agent - Agent Executor)
**Purpose**: Escalate uncertainty to human

```markdown
# Key sections:
- Question/Uncertainty
- Context
- Options Considered
- Recommendation
- Impact of Decision
```

---

### 05-MRP-Template.md (Merge-Readiness Pack)
**Created by**: SE4A (Agent - Agent Executor)
**Purpose**: 5-point evidence for review

```markdown
# The 5-Point Evidence:
1. What Changed (diff summary)
2. Why Changed (BRS alignment)
3. How Tested (test results)
4. Risk Assessment (potential issues)
5. Rollback Plan (if needed)
```

---

### 06-VCR-Template.md (Version Controlled Resolution)
**Created by**: SE4H (Human - Agent Coach)
**Purpose**: Approval record with audit trail

```markdown
# Key sections:
- Decision: APPROVED / REJECTED / NEEDS_CHANGES
- MRP Review Summary
- Conditions (if any)
- Approver Signature
- Timestamp
```

---

## 🎯 Agentic Maturity Levels

| Level | Name | Artifacts Used |
|-------|------|----------------|
| **L0** | Tool-Assisted | None (ad-hoc prompts) |
| **L1** | Agent-Assisted | BRS, MRP, VCR (minimum) |
| **L2** | Structured Agentic | All 6 artifacts |
| **L3** | Lifecycle Agentic | All + Memory + Proactive |

### Getting Started

**For Level 1** (Start Here):
1. Use `01-BriefingScript-Template.yaml` to specify tasks
2. Agent produces work with `05-MRP-Template.md` evidence
3. Human approves with `06-VCR-Template.md`

**For Level 2** (Full Workflow):
1. Add `03-MentorScript-Template.md` for standards
2. Agent creates `02-LoopScript-Template.yaml` execution plan
3. Agent uses `04-CRP-Template.md` when uncertain
4. Continue with MRP → VCR flow

---

## 📚 Related Documents

- [SDLC-Agentic-Core-Principles](../../02-Core-Methodology/SDLC-Agentic-Core-Principles.md)
- [SDLC-Agentic-Maturity-Model](../../02-Core-Methodology/SDLC-Agentic-Maturity-Model.md)
- [ACE-AEE-Reference-Architecture](../../05-Implementation-Guides/ACE-AEE-Reference-Architecture.md)

---

**Document Status**: ACTIVE - PRODUCTION READY
**Last Updated**: December 11, 2025
**Framework Version**: SDLC 5.1.0
