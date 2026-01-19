# 📦 SASE Artifact Templates
## Streamlined Templates for Human-Agent Collaboration

**Version**: 5.1.4
**Date**: January 2026
**Status**: ACTIVE - PRODUCTION READY
**Pillar**: 5 - SASE Integration
**Framework**: SDLC 5.1.3 + SASE/SE 3.0 Integration
**Reference**: arXiv:2509.06216v2 (Software Agentic Software Engineering)

---

## ⚠️ IMPORTANT: AGENTS.md Migration (ADR-029)

**Effective January 2026**, the following artifacts are **DEPRECATED** in favor of [AGENTS.md](https://agents.md/), the industry standard for AI coding agents:

| Artifact | Status | Migration Path |
|----------|--------|----------------|
| **BriefingScript (BRS)** | 🚫 DEPRECATED | → GitHub Issue template + AGENTS.md |
| **LoopScript (LPS)** | 🚫 DEPRECATED | → AI coders generate own execution plans |
| **MentorScript (MTS)** | 🚫 DEPRECATED | → AGENTS.md "Conventions" section |
| **CRP** | ✅ ACTIVE | Governance artifact (keep) |
| **MRP** | ✅ ACTIVE | Governance artifact (keep) |
| **VCR** | ✅ ACTIVE | Governance artifact (keep) |

### Why AGENTS.md?

- **Industry standard**: 60,000+ projects using AGENTS.md
- **Tool support**: Native support in Cursor, Copilot, Claude Code, OpenCode, RooCode
- **Simplicity**: ≤150 lines Markdown vs 1,400+ lines of YAML/MD
- **Ecosystem**: Founded by Google, OpenAI, Factory, Sourcegraph

### Migration Steps

1. Run `sdlc agents init` to generate AGENTS.md
2. Move coding conventions from MTS → AGENTS.md
3. Convert BRS → GitHub Issue templates
4. Archive LPS (AI coders generate own plans)

**Reference**: [ADR-029: AGENTS.md Integration Strategy](../../../../docs/02-design/01-ADRs/ADR-029-AGENTS-MD-Integration-Strategy.md)

---

## 🎯 Overview

**SASE (Software Agentic Software Engineering)** introduces artifact templates for structured human-agent collaboration. With AGENTS.md adoption, the focus shifts to **3 governance artifacts** (CRP, MRP, VCR) while using the industry standard for AI guidance.

### Current SASE Artifacts (Post-Migration)

| # | Artifact | Created By | Purpose | Status |
|---|----------|------------|---------|--------|
| 01 | **AGENTS.md** | SE4H (Human) | Industry-standard AI guidance | ✅ PRIMARY |
| 02 | **CRP** | SE4A (Agent) | Consultation Request Protocol - when uncertain | ✅ ACTIVE |
| 03 | **MRP** | SE4A (Agent) | Merge-Readiness Pack - 5-point evidence | ✅ ACTIVE |
| 04 | **VCR** | SE4H (Human) | Version Controlled Resolution - approval record | ✅ ACTIVE |

### Deprecated Artifacts (Archive Only)

| # | Artifact | Created By | Purpose | Status |
|---|----------|------------|---------|--------|
| 05 | **BriefingScript (BRS)** | SE4H (Human) | Task specification from human to agent | 🚫 DEPRECATED |
| 06 | **LoopScript (LPS)** | SE4A (Agent) | Execution plan with iterations | 🚫 DEPRECATED |
| 07 | **MentorScript (MTS)** | SE4H (Human) | Coding standards for agent compliance | 🚫 DEPRECATED |

---

## 🔄 Workflow

### Modern SASE Workflow (With AGENTS.md)

```
┌─────────────────────────────────────────────────────────────────────┐
│               AGENTS.md-BASED WORKFLOW (Recommended)                │
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

### Key Differences from Legacy Workflow

| Aspect | Legacy (BRS/MTS/LPS) | Modern (AGENTS.md) |
|--------|---------------------|-------------------|
| **AI Guidance** | MentorScript (550 lines) | AGENTS.md (≤150 lines) |
| **Task Spec** | BriefingScript (307 lines) | GitHub Issue + AGENTS.md |
| **Execution Plan** | LoopScript (558 lines) | AI generates internally |
| **Enforcement** | Manual review | GitHub Checks API |
| **Tool Support** | None | Cursor, Copilot, Claude Code |

### Legacy Workflow (DEPRECATED)

```
Human                          Agent
  │                              │
  │─── BriefingScript (BRS) ────▶│  ⚠️ DEPRECATED
  │                              │
  │─── MentorScript (MTS) ──────▶│  ⚠️ DEPRECATED
  │                              │
  │◀── LoopScript (LPS) ────────│  ⚠️ DEPRECATED
  │                              │
  │─── Approve LPS ─────────────▶│
  │                              │
  │                    [Execute]
  │                              │
  │◀── CRP (if uncertain) ──────│  ✅ KEEP
  │                              │
  │◀── MRP (5-point evidence) ──│  ✅ KEEP
  │                              │
  │─── VCR (Approve/Reject) ────▶│  ✅ KEEP
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
**Last Updated**: December 12, 2025
**Framework Version**: SDLC 5.1.3
