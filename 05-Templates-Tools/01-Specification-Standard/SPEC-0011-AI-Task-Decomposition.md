# SPEC-0011: AI Task Decomposition Service - CEO-Quality Task Generation

## Frontmatter

```yaml
spec_id: SPEC-0011
title: AI Task Decomposition Service - CEO-Quality Task Generation
version: 1.0.0
status: approved
tier:
  - STANDARD
  - PROFESSIONAL
  - ENTERPRISE
pillar:
  - Pillar 5 - AI Governance
  - Section 7 - Quality Assurance System
owner: CTO + CPO Office
last_updated: 2026-01-31
tags:
  - ai-governance
  - task-decomposition
  - multi-provider
  - quality-scoring
  - ollama
  - sprint-26
  - adr-012
related_specs:
  - SPEC-0001
  - SPEC-0003
  - SPEC-0006
  - SPEC-0009
stage: 02-DESIGN
framework_version: 6.0.5
```

---

**Status**: APPROVED
**Date**: December 3, 2025
**Decision Makers**: CTO, CPO (joint review)
**Stage**: Stage 02 (HOW - Design & Architecture)
**Framework**: SDLC 6.0.5

---

## Overview

### Problem Statement

**Vietnamese Context**: CEO có thể phân tích user story và decompose thành tasks hiệu quả. PM/Tech Lead khác mất nhiều thời gian hơn và thường miss edge cases.

**English Translation**: CEO can analyze user stories and decompose them into tasks effectively. Other PMs/Tech Leads take much more time and often miss edge cases.

**Current State**:
- CEO: 10 phút decompose 1 user story → 8-12 tasks với acceptance criteria
- Average PM: 30-45 phút → 5-8 tasks, thiếu edge cases
- Junior Dev: 60+ phút → incomplete decomposition

**Goal**: AI service decompose user stories with CEO-level quality in <2 minutes.

### Solution Overview

AI Task Decomposition Service that:
1. Accepts user story + project context + SDLC stage
2. Enriches context with project profile, related tasks, team velocity
3. Uses multi-provider AI chain (Ollama qwen2.5:14b primary → Claude fallback)
4. Generates structured task list with estimates, dependencies, acceptance criteria
5. Validates completeness against checklist (happy path, error handling, tests, docs, security)
6. Enables human review workflow (approve/modify/reject)
7. Exports approved tasks to GitHub Issues

**Quality Target**: Match CEO's decomposition quality (measured by task completeness score)

---

## Functional Requirements

### FR-001: AI Task Decomposition Engine

**Requirement ID**: FR-001
**Priority**: P0 (Critical)
**Tier Applicability**: STANDARD, PROFESSIONAL, ENTERPRISE

**Description**:
The system SHALL provide an AI-powered task decomposition engine that transforms user stories into structured task lists with CEO-level quality.

**BDD Requirement**:

```gherkin
Feature: AI Task Decomposition Engine
  As a Product Manager
  I want to decompose user stories using AI
  So that I can generate CEO-quality task breakdowns in <2 minutes

  Background:
    GIVEN I am authenticated as a user with PM role
    AND I have a project with id "proj-123"
    AND the project has tech stack ["Python", "React", "PostgreSQL"]
    AND the project has team size 5 people
    AND the project is in stage "04-BUILD"

  Scenario: Successful user story decomposition
    GIVEN I have a user story:
      """
      Title: Add user authentication to the app
      As a: User
      I want: To login with email and password
      So that: I can access my personal dashboard
      """
    WHEN I call POST /api/v1/projects/proj-123/decompose with the user story
    THEN the response status code SHALL be 200
    AND the response SHALL contain a session_id
    AND the decomposition SHALL complete within 120 seconds (p95)
    AND the generated tasks SHALL have completeness score >= 0.90
    AND the tasks SHALL include:
      | Component         | Required |
      | Happy path impl   | Yes      |
      | Error handling    | Yes      |
      | Input validation  | Yes      |
      | Unit tests        | Yes      |
      | Documentation     | Yes      |

  Scenario: Multi-provider fallback on Ollama timeout
    GIVEN Ollama provider times out after 60 seconds
    WHEN I call POST /api/v1/projects/proj-123/decompose
    THEN the system SHALL automatically fallback to Claude provider
    AND the decomposition SHALL complete within 180 seconds total
    AND the response SHALL indicate provider used was "claude"

  Scenario: Completeness score calculation
    GIVEN a user story has been decomposed into 8 tasks
    AND the tasks include: main feature (2), error handling (1), validation (1), tests (2), docs (1), security (1)
    WHEN I retrieve the decomposition session
    THEN the completeness score SHALL be calculated as:
      """
      Score = (has_main_feature + has_error_handling + has_validation + has_tests + has_docs) / 5
      Where each component is 1.0 if present, 0.0 if absent
      """
    AND the completeness score SHALL be >= 0.80 for STANDARD tier
    AND the completeness score SHALL be >= 0.90 for PROFESSIONAL/ENTERPRISE tiers
```

**Acceptance Criteria**:

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-001 | User story decomposition completes in <2 min (p95) | Performance test: 100 user stories | 95% complete within 120s |
| AC-002 | Generated tasks match CEO quality (90%+ completeness) | Quality comparison: AI vs CEO decomposition | Completeness score >= 0.90 |
| AC-003 | Multi-provider fallback works on timeout | Integration test: Mock Ollama timeout | Claude provider used, decomposition succeeds |
| AC-004 | Completeness score accurately reflects task coverage | Unit test: Score calculation logic | Score = (main + error + validation + tests + docs) / 5 |
| AC-005 | All tasks have required fields (title, type, estimate, complexity) | Schema validation test | 100% tasks pass validation |

**Tier-Specific Requirements**:

| Tier | Min Completeness Score | Max Latency (p95) | Fallback Providers | Human Review Required |
|------|------------------------|-------------------|--------------------|-----------------------|
| **STANDARD** | 0.80 | 120s | Ollama → Claude | Optional |
| **PROFESSIONAL** | 0.90 | 90s | Ollama → Claude → GPT-4o | Recommended |
| **ENTERPRISE** | 0.95 | 60s | Ollama → Claude → GPT-4o → Rule-based | Mandatory |

---

### FR-002: Multi-Provider Fallback Chain

**Requirement ID**: FR-002
**Priority**: P0 (Critical)
**Tier Applicability**: STANDARD, PROFESSIONAL, ENTERPRISE

**Description**:
The system SHALL implement a multi-provider fallback chain for AI task decomposition with automatic failover on timeout, quota exhaustion, or quality degradation.

**BDD Requirement**:

```gherkin
Feature: Multi-Provider Fallback Chain
  As a System Administrator
  I want automatic failover between AI providers
  So that task decomposition never fails due to single provider issues

  Background:
    GIVEN the provider chain is configured as:
      | Priority | Provider | Model | Timeout | Quota |
      | 1 | Ollama | qwen2.5:14b | 60s | Unlimited |
      | 2 | Claude | claude-sonnet-4-5 | 30s | 1000 req/day |
      | 3 | GPT-4o | gpt-4o | 30s | 500 req/day |
      | 4 | Rule-based | deterministic | 5s | Unlimited |

  Scenario: Primary provider success
    GIVEN Ollama provider is healthy and responsive
    WHEN I decompose a user story
    THEN the system SHALL use Ollama provider
    AND the response SHALL indicate provider "ollama"
    AND no fallback providers SHALL be invoked

  Scenario: Primary provider timeout triggers fallback
    GIVEN Ollama provider times out after 60 seconds
    WHEN I decompose a user story
    THEN the system SHALL fallback to Claude provider
    AND the response SHALL indicate provider "claude"
    AND the session metadata SHALL log fallback reason "ollama_timeout"

  Scenario: Quota exhaustion triggers fallback
    GIVEN Claude provider has exhausted daily quota (1000/1000 requests)
    WHEN I decompose a user story using Claude
    THEN the system SHALL fallback to GPT-4o provider
    AND the response SHALL indicate provider "gpt-4o"
    AND the session metadata SHALL log fallback reason "claude_quota_exhausted"

  Scenario: Quality degradation triggers fallback
    GIVEN Ollama generates tasks with completeness score 0.65
    AND the minimum required score is 0.80 for STANDARD tier
    WHEN I validate the decomposition quality
    THEN the system SHALL retry with Claude provider
    AND the new decomposition SHALL achieve score >= 0.80
    AND the session SHALL record quality_retry = true

  Scenario: All providers fail escalates to rule-based
    GIVEN Ollama times out, Claude quota exhausted, GPT-4o unavailable
    WHEN I decompose a user story
    THEN the system SHALL use rule-based deterministic templates
    AND the response SHALL indicate provider "rule-based"
    AND the session SHALL record provider_fallback_count = 3
    AND a warning SHALL be logged for engineering review
```

**Acceptance Criteria**:

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-001 | Fallback chain respects priority order | Integration test: Mock provider failures | Ollama → Claude → GPT-4o → Rule-based |
| AC-002 | Timeout triggers immediate fallback | Performance test: 60s timeout | Fallback initiated within 1s of timeout |
| AC-003 | Quota exhaustion detected and handled | Integration test: Mock 429 response | Next provider invoked, no user-facing error |
| AC-004 | Quality degradation retries with next provider | Quality test: Low score (0.65) | Retry with Claude, achieve >= 0.80 |
| AC-005 | Rule-based fallback never fails | Stress test: All AI providers down | Deterministic templates return valid tasks |

**Tier-Specific Requirements**:

| Tier | Fallback Chain | Max Retry Count | Rule-Based Fallback Allowed |
|------|----------------|-----------------|------------------------------|
| **STANDARD** | Ollama → Claude | 2 | Yes |
| **PROFESSIONAL** | Ollama → Claude → GPT-4o | 3 | Yes (with warning) |
| **ENTERPRISE** | Ollama → Claude → GPT-4o → Rule-based | 4 | Yes (with approval) |

---

### FR-003: Context Enrichment Engine

**Requirement ID**: FR-003
**Priority**: P1 (High)
**Tier Applicability**: PROFESSIONAL, ENTERPRISE

**Description**:
The system SHALL enrich user story context with project profile, existing components, team velocity, similar stories, and SDLC stage requirements before AI decomposition.

**BDD Requirement**:

```gherkin
Feature: Context Enrichment Engine
  As an AI Task Decomposition Service
  I want to enrich user story context with project metadata
  So that generated tasks are contextually relevant and accurate

  Background:
    GIVEN I have a project with id "proj-123"
    AND the project has:
      | Attribute | Value |
      | tech_stack | ["Python", "FastAPI", "React", "PostgreSQL"] |
      | team_size | 5 |
      | current_stage | "04-BUILD" |
      | average_velocity | 32 story points/sprint |

  Scenario: Context enrichment with project profile
    GIVEN I receive a user story for decomposition
    WHEN I build the decomposition context
    THEN the context SHALL include project profile:
      """
      {
        "project": {
          "name": "SDLC Orchestrator",
          "tech_stack": ["Python", "FastAPI", "React", "PostgreSQL"],
          "team_size": 5,
          "current_stage": "04-BUILD"
        }
      }
      """
    AND the context enrichment SHALL complete within 500ms

  Scenario: Context enrichment with existing components
    GIVEN the project has existing components:
      | Component | Type | Status |
      | auth-service | Backend | Active |
      | user-db | Database | Active |
      | dashboard | Frontend | Active |
    WHEN I build the decomposition context
    THEN the context SHALL include existing_components list
    AND each component SHALL have name, type, and status
    AND the AI prompt SHALL reference these components to avoid duplication

  Scenario: Context enrichment with team velocity
    GIVEN the project has historical velocity data:
      | Sprint | Story Points | Completed |
      | 41 | 28 | 26 |
      | 42 | 32 | 30 |
      | 43 | 35 | 34 |
    WHEN I calculate team velocity
    THEN the average velocity SHALL be 30 story points/sprint
    AND the context SHALL include velocity for effort estimation
    AND the AI SHALL use velocity to calibrate task estimates

  Scenario: Context enrichment with similar stories
    GIVEN the project has similar user stories:
      | Story | Similarity | Tasks Generated |
      | "Add OAuth login" | 0.85 | 7 |
      | "Add MFA authentication" | 0.78 | 6 |
    WHEN I find similar stories for "Add JWT authentication"
    THEN the context SHALL include top 3 similar stories (similarity >= 0.70)
    AND each similar story SHALL include task breakdown as reference
    AND the AI prompt SHALL suggest learning from similar decompositions

  Scenario: Context enrichment with SDLC stage requirements
    GIVEN the project is in stage "04-BUILD"
    WHEN I retrieve stage requirements
    THEN the context SHALL include mandatory requirements:
      | Requirement | Source |
      | Unit tests required | Gate G3 |
      | Test coverage >= 90% | Stage 04 policy |
      | Security scan required | Gate G3 |
    AND the AI SHALL generate tasks to satisfy stage requirements
```

**Acceptance Criteria**:

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-001 | Context enrichment completes in <500ms | Performance test: 1000 enrichments | 95% complete within 500ms |
| AC-002 | Project profile includes all required fields | Schema validation test | 100% profiles pass validation |
| AC-003 | Existing components prevent duplication | Integration test: Decompose with auth-service exists | No "Create auth-service" task generated |
| AC-004 | Team velocity calibrates task estimates | Statistical test: Velocity 30 vs 15 | Higher velocity → smaller estimates |
| AC-005 | Similar stories improve decomposition quality | A/B test: With vs without similar stories | +15% completeness score with similar stories |

**Tier-Specific Requirements**:

| Tier | Context Components | Similar Stories Count | SDLC Stage Requirements |
|------|--------------------|-----------------------|-------------------------|
| **STANDARD** | Project profile only | 0 | None |
| **PROFESSIONAL** | Profile + Components + Velocity | 3 | Current stage only |
| **ENTERPRISE** | Full (Profile + Components + Velocity + Similar + SDLC) | 5 | All stages (dependencies) |

---

### FR-004: Quality Scoring & Validation

**Requirement ID**: FR-004
**Priority**: P1 (High)
**Tier Applicability**: STANDARD, PROFESSIONAL, ENTERPRISE

**Description**:
The system SHALL calculate completeness scores for decomposed tasks based on coverage of essential components (happy path, error handling, validation, tests, documentation) and validate against tier-specific thresholds.

**BDD Requirement**:

```gherkin
Feature: Quality Scoring & Validation
  As a Task Decomposition Service
  I want to score task completeness objectively
  So that I can ensure CEO-quality output

  Background:
    GIVEN I have a decomposed task list with 10 tasks

  Scenario: Completeness score calculation
    GIVEN the tasks include:
      | Category | Count | Keywords |
      | Main feature | 3 | "implement", "create", "add", "build" |
      | Error handling | 2 | "error", "exception", "handle", "fallback" |
      | Input validation | 1 | "validate", "validation", "check" |
      | Unit tests | 2 | "test", "unit test" |
      | Documentation | 1 | "document", "readme", "api doc" |
    WHEN I calculate the completeness score
    THEN the score SHALL be computed as:
      """
      checklist = {
        "has_main_feature": 1.0 (3 tasks found),
        "has_error_handling": 1.0 (2 tasks found),
        "has_validation": 1.0 (1 task found),
        "has_tests": 1.0 (2 tasks found),
        "has_documentation": 1.0 (1 task found)
      }
      score = sum(checklist.values()) / len(checklist) = 5.0 / 5 = 1.00
      """
    AND the completeness score SHALL be 1.00 (100%)

  Scenario: Completeness score with missing components
    GIVEN the tasks include:
      | Category | Count |
      | Main feature | 3 |
      | Error handling | 0 (MISSING) |
      | Input validation | 1 |
      | Unit tests | 0 (MISSING) |
      | Documentation | 0 (MISSING) |
    WHEN I calculate the completeness score
    THEN the score SHALL be (1.0 + 0.0 + 1.0 + 0.0 + 0.0) / 5 = 0.40 (40%)
    AND the validation SHALL FAIL for STANDARD tier (requires >= 0.80)

  Scenario: Validation against tier threshold
    GIVEN I have a decomposition with completeness score 0.85
    WHEN I validate for STANDARD tier (threshold 0.80)
    THEN the validation SHALL PASS
    WHEN I validate for PROFESSIONAL tier (threshold 0.90)
    THEN the validation SHALL FAIL
    AND the system SHALL suggest re-generating with higher quality provider

  Scenario: Quality enhancement for failed validation
    GIVEN a decomposition has completeness score 0.70
    AND the tier threshold is 0.80
    WHEN I enhance the task list
    THEN the system SHALL identify missing components:
      | Missing Component | Action |
      | Error handling | Add "Handle authentication timeout" task |
      | Unit tests | Add "Test login success/failure" task |
    AND the enhanced task list SHALL achieve score >= 0.80
```

**Acceptance Criteria**:

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-001 | Completeness score accurately reflects task coverage | Unit test: 20 decompositions with known scores | 100% scores match expected values |
| AC-002 | Keyword detection correctly identifies task categories | Text analysis test: 100 task descriptions | 95%+ accuracy in categorization |
| AC-003 | Tier validation enforces minimum thresholds | Integration test: Score 0.75 vs STANDARD (0.80) | Validation fails, error returned |
| AC-004 | Quality enhancement adds missing tasks | Enhancement test: Score 0.70 → 0.80+ | Missing components added, score improved |
| AC-005 | Validation completes within 100ms | Performance test: 1000 validations | 95% complete within 100ms |

**Tier-Specific Requirements**:

| Tier | Min Completeness Score | Validation Mode | Enhancement Allowed | Quality Retry on Fail |
|------|------------------------|-----------------|---------------------|-----------------------|
| **STANDARD** | 0.80 | Soft (warning) | Yes | Optional |
| **PROFESSIONAL** | 0.90 | Hard (blocking) | Yes | Automatic (1 retry) |
| **ENTERPRISE** | 0.95 | Hard (blocking) | Yes | Automatic (2 retries) |

**Completeness Checklist Components**:

```python
COMPLETENESS_CHECKLIST = {
    "has_main_feature": {
        "keywords": ["implement", "create", "add", "build", "develop"],
        "weight": 1.0,
        "description": "Core functionality implementation tasks"
    },
    "has_error_handling": {
        "keywords": ["error", "exception", "handle", "fallback", "retry"],
        "weight": 1.0,
        "description": "Error handling and edge case tasks"
    },
    "has_validation": {
        "keywords": ["validate", "validation", "check", "verify", "sanitize"],
        "weight": 1.0,
        "description": "Input validation and data integrity tasks"
    },
    "has_tests": {
        "keywords": ["test", "unit test", "integration", "e2e", "pytest"],
        "weight": 1.0,
        "description": "Testing tasks (unit, integration, E2E)"
    },
    "has_documentation": {
        "keywords": ["document", "readme", "api doc", "comment", "docstring"],
        "weight": 1.0,
        "description": "Documentation update tasks"
    }
}
```

---

### FR-005: Human Review Workflow

**Requirement ID**: FR-005
**Priority**: P1 (High)
**Tier Applicability**: PROFESSIONAL, ENTERPRISE

**Description**:
The system SHALL provide a human review workflow where PMs/Tech Leads can approve, modify, or reject AI-generated task decompositions before exporting to GitHub Issues.

**BDD Requirement**:

```gherkin
Feature: Human Review Workflow
  As a Product Manager
  I want to review and refine AI-generated tasks
  So that I can ensure tasks are accurate before creating GitHub Issues

  Background:
    GIVEN I have a decomposition session with id "session-123"
    AND the session has 10 AI-generated tasks
    AND I am authenticated with PM role

  Scenario: Approve all tasks without changes
    GIVEN all 10 tasks are accurate and complete
    WHEN I call POST /api/v1/decomposition/sessions/session-123/approve with:
      """
      {
        "approved_task_ids": ["task-1", "task-2", ..., "task-10"],
        "modified_tasks": [],
        "rejected_task_ids": [],
        "notes": "All tasks approved. Ready for GitHub export."
      }
      """
    THEN the response status code SHALL be 200
    AND all 10 tasks SHALL have review_status = "approved"
    AND the session SHALL have approval_timestamp
    AND the session SHALL be ready for GitHub export

  Scenario: Modify tasks before approval
    GIVEN task "task-3" has incorrect estimate (8h should be 4h)
    WHEN I approve with modified tasks:
      """
      {
        "approved_task_ids": ["task-1", "task-2", "task-4", ..., "task-10"],
        "modified_tasks": [
          {
            "task_id": "task-3",
            "title": "Implement authentication service",
            "estimated_hours": 4,  // Changed from 8
            "complexity": "simple",  // Changed from "medium"
            "modification_reason": "Estimate too high, we have existing auth patterns"
          }
        ],
        "rejected_task_ids": []
      }
      """
    THEN task "task-3" SHALL have review_status = "modified"
    AND the modification SHALL be logged in session history
    AND the system SHALL learn from modifications for future decompositions

  Scenario: Reject tasks
    GIVEN task "task-7" is duplicate of existing work
    AND task "task-9" is out of scope
    WHEN I approve with rejections:
      """
      {
        "approved_task_ids": ["task-1", ..., "task-6", "task-8", "task-10"],
        "modified_tasks": [],
        "rejected_task_ids": ["task-7", "task-9"],
        "rejection_reasons": {
          "task-7": "Duplicate - auth service already implemented",
          "task-9": "Out of scope - belongs to Phase 2"
        }
      }
      """
    THEN tasks "task-7" and "task-9" SHALL have review_status = "rejected"
    AND the rejection reasons SHALL be logged
    AND the approved task count SHALL be 8 (10 - 2 rejected)

  Scenario: Learning from review feedback
    GIVEN I have approved 5 decomposition sessions
    AND I consistently rejected tasks with type "spike" (3 times)
    WHEN the system analyzes review patterns
    THEN future decompositions SHALL reduce "spike" task suggestions
    AND the learning feedback SHALL update decomposition hints
```

**Acceptance Criteria**:

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-001 | Approval workflow completes in <500ms | Performance test: 100 approvals | 95% complete within 500ms |
| AC-002 | Modified tasks are logged with reasons | Integration test: Modify 3 tasks | All modifications recorded in session history |
| AC-003 | Rejected tasks are excluded from GitHub export | E2E test: Reject 2 tasks, export remaining | Only approved tasks appear in GitHub Issues |
| AC-004 | Learning feedback improves future decompositions | Statistical test: 10 sessions with feedback | Rejection rate decreases 20%+ over time |
| AC-005 | Review status transitions are validated | State machine test: Pending → Approved → Exported | Only valid transitions allowed |

**Tier-Specific Requirements**:

| Tier | Human Review Required | Modification Tracking | Learning Feedback | Auto-Export After Approval |
|------|------------------------|----------------------|-------------------|----------------------------|
| **STANDARD** | Optional | No | No | Yes |
| **PROFESSIONAL** | Recommended | Yes (logged) | Yes (monthly analysis) | No (manual export) |
| **ENTERPRISE** | Mandatory | Yes (versioned) | Yes (real-time) | No (approval workflow) |

**Review Workflow State Machine**:

```
Task States:
  pending → approved → exported
         → modified → approved → exported
         → rejected (terminal)

Session States:
  generated → reviewing → approved → exported
           → partially_approved (if some tasks rejected)
```

---

### FR-006: GitHub Issues Export

**Requirement ID**: FR-006
**Priority**: P2 (Medium)
**Tier Applicability**: STANDARD, PROFESSIONAL, ENTERPRISE

**Description**:
The system SHALL export approved decomposed tasks to GitHub Issues with proper formatting, labels, assignees, dependencies, and milestone linking.

**BDD Requirement**:

```gherkin
Feature: GitHub Issues Export
  As a Product Manager
  I want to export approved tasks to GitHub Issues
  So that developers can start working on them immediately

  Background:
    GIVEN I have a decomposition session with id "session-123"
    AND the session has 8 approved tasks
    AND the project is linked to GitHub repo "org/repo"

  Scenario: Export tasks to GitHub Issues
    GIVEN all 8 tasks are approved
    WHEN I call GET /api/v1/decomposition/sessions/session-123/export?project_id=proj-123
    THEN the system SHALL create 8 GitHub Issues
    AND each issue SHALL have:
      | Field | Source |
      | Title | task.title |
      | Body | task.description + acceptance_criteria |
      | Labels | ["ai-generated", task.task_type, task.complexity] |
      | Milestone | sprint.name (if current sprint exists) |
      | Assignee | task.suggested_assignee_role (if team member available) |
    AND the response SHALL return GitHub Issue URLs
    AND the export SHALL complete within 30 seconds (8 tasks)

  Scenario: Export with task dependencies
    GIVEN task "task-2" depends on task "task-1"
    AND task "task-3" depends on task "task-1" and "task-2"
    WHEN I export the tasks to GitHub
    THEN the system SHALL create issues in dependency order:
      """
      1. Create issue for task-1 (no dependencies)
      2. Create issue for task-2, reference task-1 URL in description
      3. Create issue for task-3, reference task-1 and task-2 URLs
      """
    AND each dependent issue SHALL include "Depends on: #<issue-number>" in body
    AND the GitHub issue creation SHALL respect rate limits (5000 req/hour)

  Scenario: Export with formatting
    GIVEN a task has:
      """
      title: "Implement JWT authentication"
      description: "Add JWT token generation and validation"
      acceptance_criteria: [
        {"id": "AC1", "description": "User receives token on login"},
        {"id": "AC2", "description": "Token expires after 15 minutes"}
      ]
      estimated_hours: 4
      complexity: "simple"
      """
    WHEN I export to GitHub
    THEN the GitHub Issue body SHALL be formatted as:
      """
      ## Description
      Add JWT token generation and validation

      ## Acceptance Criteria
      - [ ] **AC1**: User receives token on login
      - [ ] **AC2**: Token expires after 15 minutes

      ## Estimates
      - **Effort**: 4 hours
      - **Complexity**: simple

      ---
      🤖 Generated by SDLC Orchestrator AI Task Decomposition
      Session ID: session-123
      """

  Scenario: Export failure handling
    GIVEN GitHub API returns 403 Forbidden (rate limit exceeded)
    WHEN I attempt to export tasks
    THEN the system SHALL retry with exponential backoff (1s, 2s, 4s)
    AND after 3 failed retries, the system SHALL return error to user:
      """
      {
        "error": "GitHub API rate limit exceeded",
        "retry_after": "2026-01-31T14:30:00Z",
        "exported_count": 0,
        "total_count": 8
      }
      """
    AND the session export_status SHALL be "failed"
```

**Acceptance Criteria**:

| ID | Criteria | Test Method | Expected Result |
|----|----------|-------------|-----------------|
| AC-001 | Export completes within 30s for 10 tasks | Performance test: 10 tasks export | 95% complete within 30s |
| AC-002 | Dependencies are correctly linked in issue descriptions | Integration test: Export 3 tasks with dependencies | "Depends on: #123" in issue body |
| AC-003 | Issue formatting matches template | E2E test: Export and validate GitHub issue body | 100% match expected format |
| AC-004 | Rate limit handling prevents API bans | Stress test: Export 100 tasks in 1 hour | No 403 errors, exponential backoff working |
| AC-005 | Failed exports are logged and retryable | Error simulation test: Mock GitHub 500 error | Error logged, retry mechanism triggered |

**Tier-Specific Requirements**:

| Tier | Max Tasks Per Export | GitHub Labels | Assignee Auto-Link | Milestone Auto-Link | Export Retry Policy |
|------|----------------------|---------------|--------------------|--------------------|---------------------|
| **STANDARD** | 10 | Basic (type, complexity) | No | No | 1 retry |
| **PROFESSIONAL** | 50 | Enhanced (+ ai-generated, sprint) | Yes (if role matches) | Yes (current sprint) | 3 retries |
| **ENTERPRISE** | 200 | Full (+ priority, components) | Yes (intelligent matching) | Yes (phase + sprint) | 5 retries + manual fallback |

**GitHub Issue Template**:

```markdown
## Description
{task.description}

## Acceptance Criteria
{for criterion in task.acceptance_criteria}
- [ ] **{criterion.id}**: {criterion.description}
{endfor}

## Estimates
- **Effort**: {task.estimated_hours} hours
- **Complexity**: {task.complexity}

## Technical Details
- **Type**: {task.task_type}
- **Affected Components**: {task.affected_components | join(", ")}
- **Suggested Role**: {task.suggested_assignee_role}

{if task.depends_on}
## Dependencies
This task depends on:
{for dep_id in task.depends_on}
- Issue #{github_issue_map[dep_id]}
{endfor}
{endif}

---
🤖 Generated by SDLC Orchestrator AI Task Decomposition
Session ID: {session_id}
Generated: {datetime.utcnow().isoformat()}
```

---

## Data Models

### DecomposedTask Table

```sql
CREATE TABLE decomposed_tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_story_id UUID NOT NULL REFERENCES user_stories(id),
    project_id UUID NOT NULL REFERENCES projects(id),

    -- Task details
    title VARCHAR(200) NOT NULL,
    description TEXT,
    task_type VARCHAR(50) NOT NULL,  -- 'feature', 'bug', 'chore', 'spike'
    priority VARCHAR(20) NOT NULL,  -- 'P0', 'P1', 'P2', 'P3'

    -- Estimates
    estimated_hours INTEGER,
    complexity VARCHAR(20),  -- 'trivial', 'simple', 'medium', 'complex', 'unknown'
    confidence_score FLOAT,  -- AI's confidence in estimate (0.0-1.0)

    -- Dependencies
    depends_on UUID[],  -- Array of task IDs this depends on
    blocks UUID[],  -- Array of task IDs blocked by this

    -- Acceptance criteria (JSON)
    acceptance_criteria JSONB,  -- [{"id": "AC1", "description": "...", "testable": true}]

    -- Technical details
    affected_components VARCHAR(100)[],  -- ["auth-service", "user-db"]
    suggested_assignee_role VARCHAR(50),  -- "backend", "frontend", "fullstack"

    -- AI metadata
    ai_provider VARCHAR(50),  -- "ollama", "claude", "gpt-4o", "rule-based"
    ai_model VARCHAR(100),  -- "qwen2.5:14b", "claude-sonnet-4-5"
    decomposition_prompt TEXT,
    raw_ai_response JSONB,

    -- Review status
    review_status VARCHAR(20) DEFAULT 'pending',  -- 'pending', 'approved', 'rejected', 'modified'
    reviewed_by UUID REFERENCES users(id),
    review_notes TEXT,

    -- GitHub export
    github_issue_url VARCHAR(500),
    github_issue_number INTEGER,
    export_status VARCHAR(20),  -- 'pending', 'exported', 'failed'

    -- Audit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT valid_task_type CHECK (task_type IN ('feature', 'bug', 'chore', 'spike')),
    CONSTRAINT valid_priority CHECK (priority IN ('P0', 'P1', 'P2', 'P3')),
    CONSTRAINT valid_complexity CHECK (complexity IN ('trivial', 'simple', 'medium', 'complex', 'unknown')),
    CONSTRAINT valid_review_status CHECK (review_status IN ('pending', 'approved', 'rejected', 'modified'))
);

CREATE INDEX idx_decomposed_tasks_user_story ON decomposed_tasks(user_story_id);
CREATE INDEX idx_decomposed_tasks_project ON decomposed_tasks(project_id);
CREATE INDEX idx_decomposed_tasks_review_status ON decomposed_tasks(review_status);
```

### DecompositionSession Table

```sql
CREATE TABLE decomposition_sessions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_story_id UUID NOT NULL REFERENCES user_stories(id),
    project_id UUID NOT NULL REFERENCES projects(id),

    -- Session metrics
    ai_tasks_generated INTEGER NOT NULL,
    tasks_approved INTEGER DEFAULT 0,
    tasks_modified INTEGER DEFAULT 0,
    tasks_rejected INTEGER DEFAULT 0,

    -- Quality metrics
    completeness_score FLOAT,  -- 0.0-1.0 (% of edge cases covered)
    accuracy_score FLOAT,  -- Estimate accuracy vs actual (updated post-completion)

    -- Timing
    ai_generation_time_ms INTEGER NOT NULL,
    human_review_time_ms INTEGER,

    -- Context snapshot
    context_enrichment JSONB,  -- Project profile, components, velocity, similar stories

    -- Provider chain used
    primary_provider VARCHAR(50),  -- "ollama", "claude", "gpt-4o", "rule-based"
    fallback_count INTEGER DEFAULT 0,
    provider_chain JSONB,  -- [{"provider": "ollama", "result": "timeout"}, {...}]

    -- Review workflow
    review_status VARCHAR(20) DEFAULT 'pending',  -- 'pending', 'approved', 'partially_approved', 'rejected'
    reviewed_by UUID REFERENCES users(id),
    review_notes TEXT,
    approval_timestamp TIMESTAMP,

    -- Export status
    export_status VARCHAR(20) DEFAULT 'pending',  -- 'pending', 'in_progress', 'completed', 'failed'
    github_export_timestamp TIMESTAMP,
    github_issues_created INTEGER DEFAULT 0,

    -- Audit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT valid_session_review_status CHECK (review_status IN ('pending', 'approved', 'partially_approved', 'rejected'))
);

CREATE INDEX idx_decomposition_sessions_user_story ON decomposition_sessions(user_story_id);
CREATE INDEX idx_decomposition_sessions_project ON decomposition_sessions(project_id);
CREATE INDEX idx_decomposition_sessions_review_status ON decomposition_sessions(review_status);
```

---

## API Endpoints

### POST /api/v1/projects/{project_id}/decompose

**Description**: Decompose a user story into tasks using AI

**Request**:
```json
{
  "user_story": {
    "title": "Add user authentication to the app",
    "as_a": "User",
    "i_want": "To login with email and password",
    "so_that": "I can access my personal dashboard",
    "description": "Implement JWT-based authentication..."
  },
  "options": {
    "target_complexity": "medium",
    "include_tests": true,
    "include_documentation": true
  }
}
```

**Response**:
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "tasks": [
    {
      "id": "task-1",
      "title": "Implement JWT token generation",
      "description": "Create service to generate JWT tokens...",
      "task_type": "feature",
      "estimated_hours": 4,
      "complexity": "medium",
      "acceptance_criteria": [
        {"id": "AC1", "description": "Token contains user_id claim", "testable": true},
        {"id": "AC2", "description": "Token expires after 15 minutes", "testable": true}
      ],
      "affected_components": ["auth-service"],
      "suggested_assignee_role": "backend",
      "depends_on": []
    }
  ],
  "completeness_score": 0.92,
  "ai_provider": "ollama",
  "generation_time_ms": 8500
}
```

### GET /api/v1/decomposition/sessions/{session_id}

**Description**: Retrieve decomposition session details

**Response**:
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "user_story_id": "story-123",
  "project_id": "proj-123",
  "tasks_generated": 10,
  "tasks_approved": 8,
  "tasks_rejected": 2,
  "completeness_score": 0.92,
  "review_status": "approved",
  "created_at": "2026-01-31T10:00:00Z"
}
```

### POST /api/v1/decomposition/sessions/{session_id}/approve

**Description**: Approve decomposition session (with optional modifications)

**Request**:
```json
{
  "approved_task_ids": ["task-1", "task-2", "task-3"],
  "modified_tasks": [
    {
      "task_id": "task-3",
      "estimated_hours": 4,
      "complexity": "simple",
      "modification_reason": "Estimate too high"
    }
  ],
  "rejected_task_ids": ["task-7"],
  "rejection_reasons": {
    "task-7": "Duplicate of existing work"
  },
  "notes": "Approved with minor estimate adjustments"
}
```

**Response**:
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "approved_count": 8,
  "modified_count": 1,
  "rejected_count": 2,
  "review_status": "approved",
  "approval_timestamp": "2026-01-31T11:00:00Z"
}
```

### GET /api/v1/decomposition/sessions/{session_id}/export

**Description**: Export approved tasks to GitHub Issues

**Query Parameters**:
- `project_id`: Project ID for GitHub repo link

**Response**:
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "exported_count": 8,
  "github_issues": [
    {
      "task_id": "task-1",
      "github_url": "https://github.com/org/repo/issues/123",
      "issue_number": 123
    }
  ],
  "export_status": "completed",
  "export_timestamp": "2026-01-31T12:00:00Z"
}
```

---

## Performance Requirements

| Metric | Target | Measurement | Tier |
|--------|--------|-------------|------|
| Decomposition latency (p95) | <120s | AI provider response time + validation | STANDARD |
| Decomposition latency (p95) | <90s | AI provider response time + validation | PROFESSIONAL |
| Decomposition latency (p95) | <60s | AI provider response time + validation | ENTERPRISE |
| Context enrichment | <500ms | Database queries + aggregations | ALL |
| Quality scoring | <100ms | Completeness checklist evaluation | ALL |
| Approval workflow | <500ms | Database update + status transition | ALL |
| GitHub export (10 tasks) | <30s | GitHub API calls with rate limiting | ALL |

---

## Security Requirements

| Requirement | Implementation | Validation |
|-------------|----------------|------------|
| User story access control | Row-level security (users see only their team's stories) | Integration test: User A cannot access User B's stories |
| AI prompt injection prevention | Sanitize user inputs before sending to AI provider | Penetration test: Attempt SQL injection, XSS in user story |
| GitHub token security | Store GitHub tokens in Vault with 90-day rotation | Audit: No tokens in logs, code, or database plaintext |
| Decomposition session isolation | Session ID is UUID, not sequential | Security scan: No session ID enumeration possible |
| Audit logging | Log all decomposition requests, approvals, exports | Compliance test: Full audit trail for 100% of sessions |

---

## Dependencies

### Internal Services

| Service | Purpose | API Endpoint |
|---------|---------|--------------|
| AI Gateway Service | Multi-provider AI routing | POST /ai/complete |
| Project Service | Project metadata retrieval | GET /projects/{id} |
| User Story Service | User story CRUD | GET /user-stories/{id} |
| GitHub Integration Service | GitHub Issues creation | POST /github/issues |

### External Services

| Service | Provider | Purpose | Rate Limit |
|---------|----------|---------|------------|
| Ollama API | api.nhatquangholding.com | Primary AI decomposition | Unlimited (self-hosted) |
| Claude API | Anthropic | Fallback AI decomposition | 1000 req/day |
| GPT-4o API | OpenAI | Secondary fallback | 500 req/day |
| GitHub API | GitHub | Issue creation | 5000 req/hour |

---

## Testing Strategy

### Unit Tests (95%+ coverage target)

```python
# Test completeness score calculation
def test_completeness_score_calculation():
    tasks = [
        {"title": "Implement auth", "description": "..."},
        {"title": "Handle errors", "description": "..."},
        {"title": "Validate inputs", "description": "..."},
        {"title": "Write tests", "description": "..."},
        {"title": "Update docs", "description": "..."}
    ]
    score = calculate_completeness(tasks, user_story)
    assert score == 1.0  # All 5 components present

# Test multi-provider fallback
def test_provider_fallback_on_timeout():
    with mock.patch('ollama_api.complete', side_effect=TimeoutError):
        result = decompose_user_story(story, project_id)
        assert result['ai_provider'] == 'claude'
        assert result['fallback_count'] == 1
```

### Integration Tests (90%+ coverage target)

```python
# Test end-to-end decomposition workflow
@pytest.mark.integration
def test_e2e_decomposition_workflow(test_db, test_client):
    # 1. Create user story
    story = create_user_story(test_db, title="Add authentication")

    # 2. Decompose
    response = test_client.post(f"/api/v1/projects/{project_id}/decompose", json={"user_story": story})
    assert response.status_code == 200
    session_id = response.json()['session_id']

    # 3. Approve
    approval = test_client.post(f"/api/v1/decomposition/sessions/{session_id}/approve", json={...})
    assert approval.status_code == 200

    # 4. Export to GitHub
    export = test_client.get(f"/api/v1/decomposition/sessions/{session_id}/export")
    assert export.status_code == 200
    assert export.json()['exported_count'] == 8
```

### Load Tests (100K requests target)

```python
# Locust load test scenario
class TaskDecompositionUser(HttpUser):
    @task
    def decompose_user_story(self):
        story = generate_random_story()
        self.client.post(f"/api/v1/projects/{project_id}/decompose", json={"user_story": story})

# Target: 1000 concurrent users, 95% requests <120s
```

---

## Monitoring & Observability

### Key Metrics

| Metric | Prometheus Query | Alert Threshold |
|--------|------------------|-----------------|
| Decomposition success rate | `rate(decomposition_success_total[5m])` | <95% for 10 minutes |
| Average completeness score | `avg(decomposition_completeness_score)` | <0.80 for STANDARD tier |
| Fallback provider usage | `rate(decomposition_fallback_total[5m])` | >30% (indicates primary provider issues) |
| GitHub export failure rate | `rate(github_export_failed_total[5m])` | >5% for 10 minutes |
| AI latency (p95) | `histogram_quantile(0.95, decomposition_latency_seconds_bucket)` | >120s for STANDARD tier |

### Grafana Dashboard Panels

1. **Decomposition Overview**: Success rate, completeness score, latency (p50, p95, p99)
2. **Provider Health**: Ollama/Claude/GPT-4o usage, fallback count, timeout rate
3. **Quality Metrics**: Completeness score distribution, validation failure rate
4. **Review Workflow**: Approval rate, modification rate, rejection rate
5. **GitHub Export**: Export success rate, issues created, rate limit status

---

## Migration Strategy

### Phase 1: Database Schema (Sprint 26 Day 1-2)

```sql
-- Create tables
\i migrations/001_create_decomposed_tasks.sql
\i migrations/002_create_decomposition_sessions.sql

-- Add foreign key constraints
ALTER TABLE decomposed_tasks ADD CONSTRAINT fk_user_story_id FOREIGN KEY (user_story_id) REFERENCES user_stories(id);
ALTER TABLE decomposition_sessions ADD CONSTRAINT fk_project_id FOREIGN KEY (project_id) REFERENCES projects(id);
```

### Phase 2: AI Service Implementation (Sprint 26 Day 3-4)

```python
# Implement TaskDecompositionService
# - Input parsing: Extract user story components
# - Context enrichment: Load project profile, components, velocity
# - AI decomposition: Multi-provider chain (Ollama → Claude → GPT-4o)
# - Validation: Completeness scoring, tier threshold checks
# - Storage: Save to decomposed_tasks and decomposition_sessions tables
```

### Phase 3: API Endpoints (Sprint 26 Day 5)

```python
# Implement REST API endpoints
# - POST /projects/{id}/decompose
# - GET /decomposition/sessions/{id}
# - POST /decomposition/sessions/{id}/approve
# - GET /decomposition/sessions/{id}/export
```

### Phase 4: Testing & Validation (Sprint 27)

```python
# Unit tests (95%+ coverage)
# Integration tests (E2E workflow)
# Load tests (100K requests simulation)
```

---

## Consequences

### Positive

1. **PM Productivity**: 30-45 min → 2 min decomposition time (93% time savings)
2. **Consistency**: Same quality regardless of PM experience (CEO-level output)
3. **Completeness**: AI checklist catches missing edge cases (90%+ score vs 70% manual)
4. **Learning**: System improves from human feedback (rejection rate decreases over time)
5. **Cost Optimization**: Ollama primary provider = $50/month vs $1000/month Claude-only

### Negative

1. **AI Dependency**: Risk if AI service unavailable (mitigated by multi-provider fallback)
2. **Over-reliance**: PMs may stop thinking critically (mitigated by mandatory review for ENTERPRISE tier)
3. **Context Limitations**: AI may miss domain-specific nuances (mitigated by context enrichment)

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| AI hallucination (suggests non-existent components) | MEDIUM | MEDIUM | Validate against known component list, human review |
| Estimate inaccuracy (AI estimates off by >50%) | MEDIUM | LOW | Calibrate with historical team velocity, confidence scores |
| Provider quota exhaustion (Claude 1000/day limit) | LOW | LOW | Multi-provider fallback, rule-based fallback |
| GitHub rate limit (5000 req/hour) | LOW | MEDIUM | Exponential backoff, batch exports |

---

## Approval

| Role | Name | Decision | Date | Comment |
|------|------|----------|------|---------|
| **CTO** | [CTO Name] | ✅ APPROVED | Dec 3, 2025 | Leverages AI for productivity, multi-provider fallback solid |
| **CPO** | [CPO Name] | ✅ APPROVED | Dec 3, 2025 | Key PM productivity feature, learning feedback loop valuable |

---

## References

- ADR-007: AI Context Engine - Ollama Integration
- ADR-011: AI Governance Layer Architecture
- SPEC-0003: AI Context Engine Multi-Provider Architecture
- SPEC-0006: Multi-Provider Codegen Architecture
- Sprint 26: AI Council Service Implementation

---

**Decision**: **APPROVED** - AI Task Decomposition Service
**Priority**: **HIGH** - Core AI Governance feature
**Timeline**: Sprint 26 (AI Council Service Implementation)
**Framework Version**: SDLC 6.0.5
**Last Updated**: January 31, 2026
