# SPEC-0014: Planning Hierarchy Specification

## Frontmatter

```yaml
spec_id: SPEC-0014
title: Planning Hierarchy Specification - Strategic-to-Tactical Traceability
version: 2.0.0
status: approved
tier: PROFESSIONAL
pillar: Pillar 2 - Sprint Planning Governance
owner: Backend Lead + CTO
last_updated: 2026-01-29
tags:
  - planning
  - hierarchy
  - roadmap
  - phase
  - sprint
  - backlog
  - traceability
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
  - SPEC-0013  # Teams Data Model
epic: AI Governance Layer
sprint: Sprint 28
implementation_ref: "SDLC-Orchestrator/docs/02-design/14-Technical-Specs/Planning-Hierarchy-Specification.md"
```

---

## Executive Summary

This specification defines the **governance requirements** for a 4-level planning hierarchy system that provides strategic-to-tactical traceability from vision statements down to individual backlog items.

**Key Governance Principles**:
- 4-level hierarchy: Roadmap → Phase → Sprint → Backlog
- Vision-to-task traceability with alignment scoring
- Tier-appropriate planning depth (LITE to ENTERPRISE)
- Evidence-based planning with audit trail

**Business Value**:
- Strategic alignment visibility (vision → daily tasks)
- Progress tracking across planning levels
- Compliance evidence for quality gates
- Resource allocation and velocity tracking

> **Implementation Reference**: For technical implementation details (database schemas, ORM models, API endpoints), see SDLC-Orchestrator documentation.

---

## 1. Planning Hierarchy Model

### 1.1 Four-Level Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│  LEVEL 1: ROADMAP (Strategic Vision - 1-3 Years)                   │
│  "Why are we building this? What's the end goal?"                  │
│  Owner: Product Owner / CEO                                         │
├─────────────────────────────────────────────────────────────────────┤
│  LEVEL 2: PHASE (Quarterly Objectives - 3 Months)                  │
│  "What must we achieve this quarter?"                               │
│  Owner: Product Manager                                             │
├─────────────────────────────────────────────────────────────────────┤
│  LEVEL 3: SPRINT (Iteration Planning - 1-2 Weeks)                  │
│  "What can we deliver this iteration?"                              │
│  Owner: Scrum Master / Tech Lead                                    │
├─────────────────────────────────────────────────────────────────────┤
│  LEVEL 4: BACKLOG (Task Execution - Daily)                         │
│  "What specific task am I working on today?"                        │
│  Owner: Developer / Team Member                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Traceability Chain

Every backlog item SHOULD be traceable up to the strategic vision:

```
Backlog Item → Sprint Goal → Phase Objective → Roadmap Vision
```

---

## 2. Functional Requirements

### FR-001: Roadmap Entity (Level 1)

**Description**: Roadmaps capture the strategic vision and long-term direction for a project.

**Requirement**:

```gherkin
GIVEN a project needs strategic planning
WHEN a product owner creates a roadmap
THEN the system SHALL:
  - Store unique identifier and project association
  - Capture vision statement (strategic direction)
  - Define timeframe (1-3 years)
  - Track strategic themes (3-10 focus areas)
  - Store success metrics (OKR format)
  - Maintain status lifecycle (draft → active → archived)
  - Record audit information (created, approved, timestamps)
AND the system SHALL enforce:
  - Only one active roadmap per project
  - Vision statement required for active status
  - Valid timeframe (end after start)
  - Approval required before activation
```

**Entity Attributes** (Semantic):

| Attribute | Description | Constraints |
|-----------|-------------|-------------|
| Identifier | Unique roadmap ID | Globally unique |
| Project | Parent project | Required, referential |
| Version | Semantic version | Format: X.Y.Z |
| Status | Lifecycle state | draft, active, archived |
| Vision | Strategic direction | 1-5000 characters |
| Timeframe | Duration | Start/end dates, 1-3 years |
| Themes | Strategic focus areas | 3-10 items |
| Metrics | Success measurement | OKR format |
| Audit | Created/approved by | User + timestamp |

---

### FR-002: Phase Entity (Level 2)

**Description**: Phases represent quarterly objectives within a roadmap.

**Requirement**:

```gherkin
GIVEN a roadmap exists
WHEN a product manager creates a quarterly phase
THEN the system SHALL:
  - Store unique identifier and roadmap association
  - Capture phase name and quarter identifier
  - Define objectives (SMART format, 3-7 items)
  - List key deliverables
  - Track resource allocation (team + budget)
  - Include risk assessment with mitigations
  - Map to target quality gates
  - Identify SDLC stages to complete
  - Maintain status lifecycle (planned → active → completed)
AND the system SHALL enforce:
  - Phase dates within roadmap timeframe
  - Sequential phase numbering
  - One-way status transitions (no backward)
```

**Entity Attributes** (Semantic):

| Attribute | Description | Constraints |
|-----------|-------------|-------------|
| Identifier | Unique phase ID | Globally unique |
| Roadmap | Parent roadmap | Required, referential |
| Number | Sequential order | 1, 2, 3, 4... |
| Name | Display name | 1-100 characters |
| Quarter | Time period | Format: Q1-2026 |
| Status | Lifecycle state | planned, active, completed |
| Objectives | SMART goals | 3-7 items |
| Deliverables | Expected outputs | List |
| Resources | Team + budget | Allocation object |
| Risks | Risk items | With mitigations |
| Gates | Target gates | G0-G4 references |
| Stages | SDLC stages | Stage numbers |
| Velocity | Planned vs actual | Story points |

---

### FR-003: Sprint Entity (Level 3)

**Description**: Sprints represent time-boxed iterations for delivering incremental value.

**Requirement**:

```gherkin
GIVEN a phase exists (or standalone for STANDARD tier)
WHEN a scrum master creates a sprint
THEN the system SHALL:
  - Store unique identifier and optional phase association
  - Capture sprint name and number
  - Define timeframe (typically 1-2 weeks)
  - Store sprint goals (3-5 specific goals)
  - Include definition of done (checklist)
  - Track story points (planned vs completed)
  - Record burndown data (daily progress)
  - Maintain status lifecycle (planned → active → completed)
AND the system SHALL enforce:
  - Sprint duration 5-14 days
  - Sprint dates within phase timeframe (if linked)
  - Sequential sprint numbering within project
  - One-way status transitions
```

**Entity Attributes** (Semantic):

| Attribute | Description | Constraints |
|-----------|-------------|-------------|
| Identifier | Unique sprint ID | Globally unique |
| Phase | Parent phase (optional) | Referential |
| Project | Parent project | Required |
| Number | Sequential order | Within project |
| Name | Sprint theme | 1-100 characters |
| Status | Lifecycle state | planned, active, completed |
| Goals | Sprint objectives | 3-5 items |
| Definition of Done | Completion criteria | Checklist |
| Story Points | Capacity | Planned vs completed |
| Burndown | Daily progress | Progress tracking |

---

### FR-004: Backlog Item Entity (Level 4)

**Description**: Backlog items represent individual units of work to be completed.

**Requirement**:

```gherkin
GIVEN a project exists
WHEN a team member creates a backlog item
THEN the system SHALL:
  - Store unique identifier and project association
  - Capture title and description
  - Classify item type (user_story, task, bug, tech_debt, spike)
  - Assign priority (P0, P1, P2, P3)
  - Track status through lifecycle
  - Support external tool integration (issue tracker reference)
  - Store estimation (story points, hours)
  - Record actual time spent
  - Include acceptance criteria (BDD format)
  - Enable traceability links (parent story, decomposition session)
AND the system SHALL enforce:
  - Status lifecycle: backlog → todo → in_progress → review → done
  - Story points from Fibonacci sequence (1, 2, 3, 5, 8, 13, 21)
  - Acceptance criteria required before work begins
  - External sync maintains consistency (no duplicates)
```

**Entity Attributes** (Semantic):

| Attribute | Description | Constraints |
|-----------|-------------|-------------|
| Identifier | Unique item ID | Globally unique |
| Sprint | Parent sprint (optional) | Referential |
| Project | Parent project | Required |
| External Reference | Issue tracker link | ID + URL |
| Title | Brief description | 1-200 characters |
| Description | Detailed context | 1-10000 characters |
| Type | Item classification | Enumerated |
| Priority | Importance level | P0-P3 |
| Status | Workflow state | Lifecycle states |
| Labels | Tags for filtering | List |
| Estimation | Planned effort | Points + hours |
| Actuals | Recorded effort | Hours |
| Assignee | Responsible person | User reference |
| Acceptance Criteria | BDD scenarios | GIVEN-WHEN-THEN |
| Traceability | Parent links | Story + session |

---

### FR-005: Hierarchy Retrieval

**Description**: System provides complete planning hierarchy for a project.

**Requirement**:

```gherkin
GIVEN a project with planning data exists
WHEN a user requests the planning hierarchy
THEN the system SHALL:
  - Retrieve active roadmap (if exists)
  - Load all phases within roadmap (if exists)
  - Load all sprints within each phase (if exists)
  - Optionally load backlog items within sprints
  - Return nested hierarchy structure
AND the system SHALL support:
  - Filtering by status (active only, all)
  - Tier-appropriate depth (STANDARD: Sprint+Backlog only)
  - Performance optimization (no redundant queries)
  - Pagination for large item lists
```

---

### FR-006: Traceability Chain Calculation

**Description**: System calculates alignment from backlog item to strategic vision.

**Requirement**:

```gherkin
GIVEN a backlog item exists
WHEN a user requests traceability for that item
THEN the system SHALL:
  - Navigate from item to sprint to phase to roadmap
  - Calculate alignment score (0.0 to 1.0)
  - Return complete lineage with contributing factors
AND the alignment score SHALL consider:
  - Keyword matching between item and phase objectives (weight: 40%)
  - Sprint goal alignment (weight: 30%)
  - Acceptance criteria quality (weight: 20%)
  - Gate contribution (weight: 10%)
AND the system SHALL:
  - Cache scores for performance
  - Invalidate cache on hierarchy changes
  - Return 0.0 for unlinked items
```

---

### FR-007: External Tool Synchronization

**Description**: System synchronizes with external issue tracking tools.

**Requirement**:

```gherkin
GIVEN a sprint exists with external tool integration configured
WHEN synchronization is triggered
THEN the system SHALL:
  - Query external tool for items matching sprint criteria
  - Update existing backlog items with external changes
  - Create new backlog items for untracked external items
  - Track synchronization metadata (timestamp, counts)
AND the system SHALL enforce:
  - Read-only bridge pattern (no write-back to external tool)
  - Status mapping between systems
  - Rate limiting to prevent overload
  - Graceful error handling (partial sync on failures)
```

---

## 3. Tier-Specific Requirements

| Feature | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---------|------|----------|--------------|------------|
| **Roadmap** | Not available | Not available | Required | Required |
| **Phase** | Not available | Not available | Required | Required |
| **Sprint** | Not available | Required | Required | Required |
| **Backlog** | Required | Required | Required | Required |
| **Traceability** | Not available | Sprint → Backlog | Full chain | Full + trends |
| **Alignment Score** | Not available | Not available | Calculated | + anomaly detection |
| **External Sync** | Manual import | Basic sync | Advanced sync | Bi-directional (future) |
| **Export Formats** | None | Markdown | Markdown, JSON | All + PDF |
| **Velocity Tracking** | Not tracked | Sprint-level | Phase + Sprint | + predictive |
| **Resource Allocation** | Not available | Not available | Phase-level | Phase + Sprint |
| **Risk Assessment** | Not available | Not available | Phase-level | + mitigation tracking |
| **Gate Mapping** | Not available | Not available | Phase → Gates | + Evidence links |

**Tier Summary**:
- **LITE**: Backlog only for small teams
- **STANDARD**: Sprint + Backlog for agile teams
- **PROFESSIONAL**: Full 4-level hierarchy
- **ENTERPRISE**: All features + advanced analytics

---

## 4. Status Lifecycles

### Roadmap Lifecycle
```
draft → active → archived
```
- **draft**: Initial creation, editing allowed
- **active**: Current strategic direction, approval required
- **archived**: Historical reference, read-only

### Phase Lifecycle
```
planned → active → completed
```
- **planned**: Future quarter, can modify
- **active**: Current work, limited changes
- **completed**: Retrospective available, read-only

### Sprint Lifecycle
```
planned → active → completed
```
- **planned**: Backlog refinement stage
- **active**: In-progress work
- **completed**: Done, retrospective required

### Backlog Item Lifecycle
```
backlog → todo → in_progress → review → done
```
- **backlog**: Unscheduled, needs refinement
- **todo**: Scheduled in sprint, ready to start
- **in_progress**: Active development
- **review**: Code review / QA
- **done**: Meets definition of done

---

## 5. Alignment Score Algorithm

### Purpose
Measure how well a backlog item aligns with strategic vision.

### Calculation

```
Score = (Keyword × 0.4) + (SprintGoal × 0.3) + (Criteria × 0.2) + (Gate × 0.1)

Where:
- Keyword: Item labels ∩ Phase objectives (0-1)
- SprintGoal: Item in sprint goal keywords (0-1)
- Criteria: Item has ≥3 acceptance criteria (0-1)
- Gate: Item contributes to phase target_gates (0-1)

Final: min(1.0, weighted sum)
```

### Interpretation

| Score Range | Meaning | Action |
|-------------|---------|--------|
| 0.8 - 1.0 | Highly aligned | Excellent traceability |
| 0.6 - 0.8 | Well aligned | Good strategic fit |
| 0.4 - 0.6 | Moderately aligned | Review objectives |
| 0.2 - 0.4 | Weakly aligned | Consider re-linking |
| 0.0 - 0.2 | Not aligned | May be orphan work |

---

## 6. Non-Functional Requirements

### NFR-001: Performance Targets

| Operation | Target Latency (p95) | Notes |
|-----------|---------------------|-------|
| Hierarchy retrieval (100 items) | <200ms | Optimized queries |
| Traceability calculation (cached) | <100ms | With cache |
| External sync (50 items) | <5s | Rate limited |
| Export (markdown) | <1s | Async for large |

### NFR-002: Security Requirements

| Requirement | Description |
|-------------|-------------|
| Authentication | Token-based with expiry |
| Authorization | Role-based access (PM, Dev, QA) |
| Data validation | Input sanitization |
| Rate limiting | Sync operations limited |
| Audit trail | All updates logged |

---

## 7. Design Decisions

### Decision 1: Four-Level Hierarchy

**Rationale**: Industry standard structure with clear separation of concerns.

**Levels**:
- Roadmap (1-3 years) → Executive-level vision
- Phase (3 months) → Quarterly objectives
- Sprint (1-2 weeks) → Iteration planning
- Backlog (daily) → Task execution

**Alternative Rejected**: 3-level (no Phase) - Teams need quarterly planning for enterprise projects.

### Decision 2: Flexible Data Storage

**Rationale**: Planning structures vary by team and evolve over time.

**Approach**: Use flexible storage for varying data (objectives, metrics) while maintaining typed fields for critical data (dates, status).

**Trade-offs**:
- Pro: Schema evolution without migrations
- Con: Application-level validation required

### Decision 3: Read-Only External Bridge

**Rationale**: SDLC Orchestrator governs, not replaces. External tools remain source of truth for issue tracking.

**Approach**: Read from external tools, never write back.

**Future**: Bi-directional sync deferred to ENTERPRISE tier.

### Decision 4: Weighted Alignment Score

**Rationale**: Multiple factors contribute to strategic alignment.

**Weights** (calibrated from pilot feedback):
- Keyword matching: 40% (primary indicator)
- Sprint goal alignment: 30% (tactical focus)
- Acceptance criteria: 20% (definition clarity)
- Gate contribution: 10% (quality milestone)

---

## 8. Acceptance Criteria

### AC-001: Roadmap Creation

```gherkin
GIVEN a project exists
WHEN a product owner creates a roadmap with valid vision and timeframe
THEN the roadmap is persisted in draft status
AND only one active roadmap can exist per project
AND approval is required to activate
```

### AC-002: Phase Boundary Validation

```gherkin
GIVEN a roadmap with timeframe Jan 2026 - Dec 2026
WHEN a phase is created with dates outside this range
THEN the system rejects the phase with validation error
AND the error message indicates the boundary constraint
```

### AC-003: Traceability Chain

```gherkin
GIVEN a backlog item linked to sprint → phase → roadmap
WHEN traceability is requested
THEN the full chain is returned with alignment score
AND contributing factors breakdown is included
```

### AC-004: External Sync Idempotency

```gherkin
GIVEN an external item was previously synced
WHEN sync is triggered again
THEN the existing backlog item is updated (not duplicated)
AND sync statistics reflect update count
```

### AC-005: Tier-Appropriate Depth

```gherkin
GIVEN a STANDARD tier project
WHEN hierarchy is requested
THEN only Sprint and Backlog levels are returned
AND Roadmap and Phase are not included
```

---

## 9. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Planning overhead | Medium | Medium | Start with STANDARD tier (Sprint+Backlog only) |
| Stale alignment scores | Low | Medium | Auto-invalidate on hierarchy changes |
| External sync failures | Medium | Low | Partial sync + retry mechanism |
| Over-complicated hierarchy | Low | High | Tier-appropriate features |

---

## 10. References

### Source Documents
- **ADR-013**: Planning Hierarchy Architecture Decision
- **SDLC 5.3.0**: Pillar 2 - Sprint Planning Governance
- **SPEC-0001**: Anti-Vibecoding (quality gates integration)

### External Standards
- Agile Alliance: Sprint Planning Best Practices
- SAFe Framework: Program Increment Planning
- Scrum Guide: Sprint Backlog Management

---

## Document Control

| Field | Value |
|-------|-------|
| **Spec ID** | SPEC-0014 |
| **Version** | 2.0.0 |
| **Status** | APPROVED |
| **Author** | Backend Lead |
| **Reviewer** | CTO |
| **Last Updated** | 2026-01-29 |
| **Framework Version** | 6.0.5 |

---

**Pure Methodology Notes**:
- This specification defines WHAT planning hierarchy governance requires
- For HOW to implement (database schemas, API endpoints, ORM models), see SDLC-Orchestrator technical documentation
- Tier requirements are governance rules, implementation enforces via appropriate mechanism
- Alignment score algorithm is conceptual; implementation may optimize

---

**End of Specification**
