# 📊 AI RACI Matrix Generator - Stage 08 (COLLABORATE)

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 08 - COLLABORATE (Team Management & Documentation)
**Time Savings**: 85%
**Authority**: CPO Office

---

## Purpose

Generate **RACI matrices** for multi-team projects following SDLC 5.0.0 standards. Ensures clear accountability with exactly ONE Accountable (A) per deliverable.

---

## RACI Fundamentals

### Role Definitions

| Letter | Role | Definition | Rule |
|--------|------|------------|------|
| **R** | Responsible | Does the work | Multiple allowed |
| **A** | Accountable | Final decision maker, sign-off | **Exactly ONE** per row |
| **C** | Consulted | Provides input before decision | Multiple allowed |
| **I** | Informed | Notified after decision | Multiple allowed |

### RACI Rules (SDLC 5.0.0)

1. **One A per deliverable**: Every row must have exactly one Accountable
2. **At least one R**: Someone must do the work
3. **A can also be R**: The accountable person can also do the work
4. **Minimize C**: Too many consultants slow decisions
5. **I is optional**: Not everyone needs to be informed

---

## AI Prompts

### 1. Basic RACI Matrix Generator

```yaml
System Prompt:
  You are generating RACI matrices following SDLC 5.0.0 standards.
  CRITICAL: Every row must have exactly ONE 'A' (Accountable).
  Multiple 'R' allowed but keep it focused.
  Minimize 'C' to avoid decision paralysis.

User Prompt Template:
  "Generate a RACI matrix for:

   Project: [Name]

   Roles/Teams:
   - [Role/Team 1]
   - [Role/Team 2]
   - [Role/Team 3]
   - [Role/Team 4]

   Deliverables:
   1. [Deliverable 1]
   2. [Deliverable 2]
   3. [Deliverable 3]
   4. [Deliverable 4]
   5. [Deliverable 5]

   Constraints:
   - [Any specific accountability rules]"

Output Format:
  # RACI Matrix: [Project Name]

  **Version**: 1.0.0
  **Date**: [YYYY-MM-DD]
  **Status**: ACTIVE

  ---

  | Deliverable | [Role 1] | [Role 2] | [Role 3] | [Role 4] |
  |-------------|----------|----------|----------|----------|
  | [D1] | R | A | C | I |
  | [D2] | C | R | A | I |
  | [D3] | I | C | R | A |
  | [D4] | A, R | C | I | I |
  | [D5] | I | A | R | C |

  ---

  ## Legend
  - **R** (Responsible): Does the work
  - **A** (Accountable): Final decision maker (ONE per row)
  - **C** (Consulted): Provides input before decision
  - **I** (Informed): Notified after decision

  ---

  ## Accountability Notes

  ### [Deliverable 1]
  - **Accountable**: [Role 2] - [Reason for accountability]
  - **Responsible**: [Role 1] - [What work they do]
  - **Decision process**: [How final sign-off works]

  [Repeat for complex deliverables]
```

### 2. SDLC Stage-Based RACI Generator

```yaml
System Prompt:
  You are generating RACI matrices aligned with SDLC 5.0.0 10-stage lifecycle.
  Map deliverables to stages: 00-Foundation through 09-Governance.
  Apply tier-appropriate governance (LITE/STANDARD/PROFESSIONAL/ENTERPRISE).

User Prompt Template:
  "Generate a stage-based RACI matrix for:

   Project: [Name]
   Tier: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]
   Current Stage: [00-09]

   Roles:
   - PO (Project Owner)
   - PM (Project Manager)
   - TL (Tech Lead)
   - Dev Team
   - QA Team
   - Ops Team

   Include gates:
   - G0.1: Problem Definition
   - G0.2: Solution Diversity
   - G1: Legal + Market Validation
   - G2: Design Ready
   - G3: Ship Ready"

Output Format:
  # SDLC Stage-Based RACI: [Project Name]

  **Tier**: [Tier]
  **Framework**: SDLC 5.0.0

  ---

  ## Stage 00: Foundation (WHY)

  | Deliverable | PO | PM | TL | Dev | QA | Ops |
  |-------------|----|----|----|----|----|----|
  | Problem Statement | A, R | C | C | I | I | I |
  | Stakeholder Interviews | C | R | I | I | I | I |
  | **G0.1 Sign-off** | A | R | C | I | I | I |

  ## Stage 01: Planning (WHAT)

  | Deliverable | PO | PM | TL | Dev | QA | Ops |
  |-------------|----|----|----|----|----|----|
  | Requirements Doc | A | R | C | C | C | I |
  | User Stories | C | A, R | C | C | C | I |
  | **G1 Sign-off** | A | R | C | I | I | I |

  ## Stage 02: Design (HOW)

  | Deliverable | PO | PM | TL | Dev | QA | Ops |
  |-------------|----|----|----|----|----|----|
  | Architecture Design | C | C | A, R | C | I | C |
  | API Specification | I | C | A | R | C | I |
  | Security Baseline | C | I | A | C | C | R |
  | **G2 Sign-off** | A | C | R | I | I | C |

  ## Stage 03: Development (BUILD)

  | Deliverable | PO | PM | TL | Dev | QA | Ops |
  |-------------|----|----|----|----|----|----|
  | Feature Code | I | C | A | R | C | I |
  | Unit Tests | I | I | C | A, R | C | I |
  | Code Review | I | I | A | R | I | I |

  ## Stage 04: Testing (TEST)

  | Deliverable | PO | PM | TL | Dev | QA | Ops |
  |-------------|----|----|----|----|----|----|
  | Test Plan | I | C | C | C | A, R | I |
  | Test Execution | I | I | I | C | A, R | I |
  | Bug Fixes | I | C | A | R | C | I |

  ## Stage 05: Deployment (DEPLOY)

  | Deliverable | PO | PM | TL | Dev | QA | Ops |
  |-------------|----|----|----|----|----|----|
  | Deployment Plan | I | C | A | C | C | R |
  | Release Notes | C | A, R | C | C | I | I |
  | **G3 Sign-off** | A | R | C | I | C | C |

  ## Stage 06: Operations (OPERATE)

  | Deliverable | PO | PM | TL | Dev | QA | Ops |
  |-------------|----|----|----|----|----|----|
  | Monitoring Setup | I | I | C | C | I | A, R |
  | Runbooks | I | I | A | C | I | R |
  | Incident Response | I | I | C | C | I | A, R |

  ---

  ## Gate Accountability Summary

  | Gate | Accountable | Must Consult | Must Inform |
  |------|-------------|--------------|-------------|
  | G0.1 | PO | PM, TL | Dev, QA, Ops |
  | G0.2 | PO | PM, TL | Dev, QA, Ops |
  | G1 | PO | PM, TL, QA | Dev, Ops |
  | G2 | PO | TL, Ops | PM, Dev, QA |
  | G3 | PO | PM, TL, QA, Ops | Dev |
```

### 3. Multi-Team RACI Generator

```yaml
System Prompt:
  You are generating RACI matrices for multi-team coordination.
  Each team is treated as a unit. Focus on inter-team handoffs.
  Apply Team Topologies principles (Stream-aligned, Platform, Enabling).

User Prompt Template:
  "Generate a multi-team RACI for:

   Project: [Name]

   Teams:
   - Team A: [Name] - [Type: Stream-aligned/Platform/Enabling]
   - Team B: [Name] - [Type]
   - Team C: [Name] - [Type]

   Governance:
   - PO: [Name]
   - PM: [Name]

   Deliverables (with dependencies):
   1. [D1] (Team A → Team B)
   2. [D2] (Team B → Team C)
   3. [D3] (Team A, Team C joint)
   4. [D4] (Platform team provides to all)

   Handoff points:
   - [Handoff 1 description]
   - [Handoff 2 description]"

Output Format:
  # Multi-Team RACI: [Project Name]

  **Version**: 1.0.0
  **Team Topology**: [Stream-aligned + Platform | etc.]

  ---

  ## Team Overview

  | Team | Type | Primary Deliverables | Dependencies |
  |------|------|---------------------|--------------|
  | Team A | Stream-aligned | [D1] | None |
  | Team B | Stream-aligned | [D2] | Team A |
  | Team C | Platform | [D3, D4] | Team A, Team B |

  ---

  ## RACI Matrix

  | Deliverable | PO | PM | Team A | Team B | Team C |
  |-------------|----|----|--------|--------|--------|
  | [D1] | A | C | R | I | I |
  | [D2] | A | C | C | R | I |
  | [D3] | A | C | R | I | R |
  | [D4] (Platform) | I | C | I | I | A, R |
  | **Handoff 1** | I | A | R | R | I |
  | **Handoff 2** | I | A | I | R | R |

  ---

  ## Handoff Accountability

  ### Handoff 1: [Team A] → [Team B]
  | Aspect | Owner | Action |
  |--------|-------|--------|
  | Trigger | Team A | Marks deliverable complete |
  | Review | Team B | Reviews within 24h |
  | Acceptance | PM | Confirms handoff complete |
  | Escalation | PM | Resolves blockers |

  ---

  ## Inter-Team Communication

  | Communication | From | To | Accountable | Frequency |
  |---------------|------|-----|-------------|-----------|
  | Status Update | Team A | Team B | Team A Lead | Daily |
  | Blocker Alert | Any | PM | PM | Immediate |
  | Design Review | Team A | Team C | Team C Lead | Per design |
```

### 4. RACI Validation and Audit

```yaml
System Prompt:
  You are auditing an existing RACI matrix for SDLC 5.0.0 compliance.
  Check for: Single A per row, at least one R, no orphaned deliverables.
  Provide specific recommendations for fixing issues.

User Prompt Template:
  "Audit this RACI matrix:

   [Paste existing RACI matrix]

   Check for:
   1. Exactly one A per row
   2. At least one R per row
   3. No empty rows
   4. Appropriate C distribution (not too many)
   5. I usage (not everyone needs to be informed)
   6. Role clarity (no ambiguous assignments)"

Output Format:
  # RACI Audit Report

  **Matrix Reviewed**: [Name]
  **Audit Date**: [YYYY-MM-DD]
  **Compliance Score**: [X]%

  ---

  ## Critical Issues (Must Fix)

  | Row | Issue | Current | Recommendation |
  |-----|-------|---------|----------------|
  | D3 | Multiple A | PM, TL both A | PM should be A, TL should be C |
  | D5 | No A assigned | All R/C/I | Assign TL as A |
  | D7 | No R assigned | Only A and I | Dev Team should be R |

  ---

  ## Warnings (Should Fix)

  | Row | Issue | Current | Recommendation |
  |-----|-------|---------|----------------|
  | D2 | Too many C | 5 consulted | Reduce to 2-3 key consultants |
  | D4 | Everyone is I | 4 informed | Only inform those who need it |

  ---

  ## Best Practices Applied

  - ✅ [X] rows have exactly one A
  - ✅ [X] rows have at least one R
  - ✅ No orphaned deliverables
  - ⚠️ [X] rows have >3 consultants (consider reducing)

  ---

  ## Recommended Changes

  ### Updated RACI Matrix

  | Deliverable | PO | PM | TL | Dev | QA |
  |-------------|----|----|----|----|-----|
  | D3 | I | A | C | R | I | ← Changed TL from A to C
  | D5 | I | I | A | R | C | ← Added TL as A
  | D7 | I | C | A | R | C | ← Added Dev as R
```

---

## RACI Templates by Project Type

### Software Development Project

| Phase | PO | PM | TL | Dev | QA | DevOps |
|-------|----|----|----|----|----|----|
| Requirements | A | R | C | C | C | I |
| Architecture | C | C | A | R | I | C |
| Development | I | C | A | R | C | I |
| Testing | I | C | C | C | A | I |
| Deployment | A | R | C | C | C | R |
| Operations | I | I | C | I | I | A |

### Product Launch

| Phase | CEO | CPO | PM | Marketing | Sales | Support |
|-------|-----|-----|----|----|----|----|
| Strategy | A | R | C | C | C | I |
| Planning | C | A | R | C | C | I |
| Development | I | A | R | I | I | I |
| Marketing | C | C | C | A | C | I |
| Launch | A | C | R | R | R | R |
| Support | I | C | C | I | I | A |

---

## Tier-Appropriate RACI Requirements

| Tier | RACI Required | Granularity | Audit Frequency |
|------|---------------|-------------|-----------------|
| LITE | No | N/A | N/A |
| STANDARD | Key deliverables | Phase-level | Quarterly |
| PROFESSIONAL | All deliverables | Task-level | Monthly |
| ENTERPRISE | All + gates | Sub-task level | Sprint-level |

---

## Success Metrics

**RACI Effectiveness** (Stage 08):
- ✅ 85% time savings on accountability discussions
- ✅ 100% deliverables have single accountable
- ✅ 50% reduction in "who decides?" questions
- ✅ 30% faster decision-making

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tiers
**Last Updated**: December 5, 2025
**Owner**: CPO Office
