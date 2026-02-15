# SPEC-0019: Conformance Testing Specification

## Frontmatter

```yaml
spec_id: SPEC-0019
title: Conformance Testing & Plan Approval Specification
version: 2.0.0
status: approved
tier: PROFESSIONAL
pillar: Section 7 - Quality Assurance System
owner: Backend Lead + CTO
last_updated: 2026-01-29
tags:
  - conformance
  - testing
  - pattern-validation
  - plan-approval
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
epic: Pattern Conformance Automation
sprint: Sprint 92-95
implementation_ref: "SDLC-Orchestrator/docs/02-design/14-Technical-Specs/Conformance-Testing-Design.md"
```

---

## 1. Overview

### 1.1 Purpose

This specification defines the **Conformance Testing & Plan Approval** system - pattern-based validation of proposed changes (PRs) and human review workflows for AI-generated implementation plans in SDLC Orchestrator.

**Industry Context**: Most AI coding tools generate code without conformance checks, leading to **architectural drift** (estimated 30% of AI-generated code violates established patterns). SDLC Orchestrator prevents drift by comparing proposed changes against **extracted codebase patterns** before merge.

### 1.2 Background

**Traditional Approach** (Manual Code Review):
- Reviewers manually check for pattern violations
- Inconsistent enforcement (depends on reviewer knowledge)
- Slow feedback loop (24-48h for review)
- **Result**: Architectural drift accumulates over time

**SDLC Orchestrator Approach** (Automated Conformance):
- Extract patterns from existing codebase (PatternExtractionService)
- Compare PR diffs against patterns automatically (ConformanceCheckService)
- Score conformance 0-100 (95%+ = excellent, <50% = high risk)
- **Result**: Prevent drift before merge, <5min feedback

### 1.3 Strategic Value

**Moat Analysis** (vs. Manual Reviews):

| Capability | Manual Reviews | SDLC Orchestrator Conformance |
|------------|----------------|-------------------------------|
| **Pattern Detection** | Human knowledge (inconsistent) | Automated extraction (consistent) |
| **Feedback Time** | 24-48h (PR review wait) | <5min (CI/CD check) |
| **Accuracy** | Varies (reviewer-dependent) | 95%+ (pattern-based scoring) |
| **Coverage** | Partial (reviewer fatigue) | 100% (all PRs scanned) |
| **Cost** | High (senior eng time) | Low (automated + occasional human approval) |
| **Learning Loop** | No feedback mechanism | Patterns → Plans → Learnings → Hints |

**ROI**: 60% reduction in architectural drift (BFlow pilot: 18 → 7 pattern violations per month).

## 2. Functional Requirements

### FR-01: Pattern Conformance Checking

**Requirement**: Automatically check PR diffs against established codebase patterns to prevent architectural drift.

```gherkin
GIVEN a GitHub pull request with code changes
  AND the project has extracted patterns (from PatternExtractionService)
WHEN ConformanceCheckService.check_pr_diff(pr_url, patterns) is called
THEN the system MUST:
  1. Fetch PR diff from GitHub API
  2. Parse diff into changed files + lines
  3. Analyze changes against patterns:
     - Pattern coverage: Does change follow existing patterns?
     - ADR alignment: Does change reference relevant ADRs?
     - Convention following: Does change follow code conventions?
     - Risk assessment: Is this a high-risk change (auth, DB schema)?
  4. Calculate conformance score (0-100):
     - Base score: 100
     - Deduct 15 points per major pattern violation
     - Deduct 5 points per minor pattern violation
     - Deduct 10 points per missing ADR reference
     - Deduct 5 points per high-risk change
  5. Classify conformance level:
     - Excellent: 95-100 (no action needed)
     - Good: 70-94 (minor improvements suggested)
     - Needs Improvement: 50-69 (review recommended)
     - Poor: 0-49 (blocking merge)
  6. Return ConformanceResult with:
     - score: int (0-100)
     - level: str (excellent, good, needs_improvement, poor)
     - deviations: list[ConformanceDeviation]
     - recommendations: list[str]
     - passed: bool (score >= threshold, default 50)
```

**Scoring Criteria**:

| Category | Max Points | Description |
|----------|------------|-------------|
| **Pattern Coverage** | 40 | Do changes follow existing patterns? |
| **ADR Alignment** | 20 | Are ADRs referenced for arch changes? |
| **Convention Following** | 20 | Code style, naming, structure |
| **Risk Assessment** | 20 | Auth, DB, external integrations |

**Violation Deductions**:

| Violation Type | Deduction | Description |
|----------------|-----------|-------------|
| Major violation | -15 points | New pattern without ADR |
| Minor violation | -5 points | Code style inconsistency |
| Missing ADR reference | -10 points | Arch change without doc |
| High-risk change | -5 points each | Auth, schema, API changes |

**Conformance Result Structure**:

| Field | Type | Description |
|-------|------|-------------|
| score | 0-100 | Conformance score |
| level | enum | excellent, good, needs_improvement, poor |
| deviations | list | Pattern violations detected |
| recommendations | list | Actionable fix suggestions |
| passed | boolean | True if score >= threshold |
| threshold | integer | Threshold used for pass/fail |
| coverage_score | 0-40 | Pattern coverage score |
| adr_score | 0-20 | ADR alignment score |
| convention_score | 0-20 | Convention following score |
| risk_score | 0-20 | Risk assessment score |

> **Implementation Reference**: For service classes and Pydantic schemas, see SDLC-Orchestrator documentation.

**Acceptance Criteria**:
- ✅ AC-01: Conformance check completes <5s (p95) for 500 LOC diff
- ✅ AC-02: Scoring accuracy ≥95% (validated against manual reviews)
- ✅ AC-03: Detects all 4 deviation types (major, minor, missing ADR, high-risk)
- ✅ AC-04: Recommendations are actionable (specific file + line + fix suggestion)
- ✅ AC-05: False positive rate <5% (no incorrect pattern violations)

---

### FR-02: Planning API Routes

**Requirement**: Provide REST API endpoints for planning operations (start, approve, check conformance).

```gherkin
GIVEN API routes for planning operations
WHEN clients make HTTP requests
THEN the system MUST support:

POST /api/v1/planning/subagent/plan
  - Start new planning session
  - Extract patterns from codebase
  - Generate implementation plan
  - Return session_id + patterns + plan + conformance

GET /api/v1/planning/subagent/{session_id}
  - Retrieve planning session details
  - Return patterns, plan, conformance, status

POST /api/v1/planning/subagent/{session_id}/approve
  - Approve or reject plan
  - Store approval decision
  - Return updated session status

POST /api/v1/planning/subagent/conformance
  - Check PR conformance (for CI/CD)
  - Return conformance result
  - Store conformance history

GET /api/v1/planning/subagent/sessions
  - List active planning sessions
  - Filter by status (awaiting_approval, approved, rejected)
  - Paginate results (default 20 per page)
```

**API Endpoints Specification**:

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| POST | `/api/v1/planning/subagent/plan` | Start planning session | Bearer token |
| GET | `/api/v1/planning/subagent/{id}` | Get planning result | Bearer token |
| POST | `/api/v1/planning/subagent/{id}/approve` | Approve/reject plan | Bearer token |
| POST | `/api/v1/planning/subagent/conformance` | Check PR conformance | API key OR Bearer |
| GET | `/api/v1/planning/subagent/sessions` | List active sessions | Bearer token |

**Request/Response Requirements**:

| Endpoint | Request Fields | Response Fields |
|----------|----------------|-----------------|
| POST /plan | task, project_path, depth, include_tests, include_adrs, auto_approve | id, task, status, patterns, plan, conformance |
| POST /{id}/approve | approved (boolean), notes (optional) | id, status, approved_by, approved_at, notes |
| POST /conformance | pr_url, threshold | score, level, deviations, passed, threshold |

> **Implementation Reference**: For detailed JSON schemas and examples, see SDLC-Orchestrator API documentation.

**Acceptance Criteria**:
- ✅ AC-01: All 5 endpoints respond <200ms (p95)
- ✅ AC-02: OpenAPI 3.0 documentation auto-generated (FastAPI /docs)
- ✅ AC-03: JWT authentication working for Bearer token endpoints
- ✅ AC-04: API key authentication working for /conformance endpoint (CI/CD)
- ✅ AC-05: Error responses follow RFC 7807 (Problem Details)

---

### FR-03: Plan Approval Dashboard UI

**Requirement**: Provide web dashboard UI for human review and approval of AI-generated implementation plans.

```gherkin
GIVEN a user with PM or Tech Lead role
  AND there are planning sessions awaiting approval
WHEN user navigates to /app/planning/plan-review
THEN the system MUST display:
  1. List of active planning sessions (status: awaiting_approval)
  2. For each session:
     - Task summary
     - Conformance score gauge (0-100, color-coded)
     - Status badge (awaiting approval, approved, rejected)
     - Created timestamp (relative time, e.g., "2m ago")
  3. Click session → Navigate to /app/planning/plan-review/{session_id}
  4. Session detail page shows:
     - Task summary section
     - Conformance score gauge (large, animated)
     - Extracted patterns list (expandable)
     - Implementation plan steps (timeline view)
     - Deviations & recommendations (if any)
     - Action buttons: [Reject with Notes] [Request Changes] [Approve Plan]
```

**UI Components**:

```
┌─────────────────────────────────────────────────────────────────┐
│                   PLAN REVIEW DASHBOARD                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────┐  ┌──────────────────────────┐  │
│  │ TASK SUMMARY                │  │ CONFORMANCE SCORE        │  │
│  │ "Add OAuth2 auth..."        │  │      ┌────────┐          │  │
│  │                             │  │      │  85%   │          │  │
│  │ Status: Awaiting Approval   │  │      │  GOOD  │          │  │
│  │ Created: 2m ago             │  │      └────────┘          │  │
│  └─────────────────────────────┘  └──────────────────────────┘  │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ EXTRACTED PATTERNS (15 found)                             │  │
│  │ ┌──────────────────────────────────────────────────────┐  │  │
│  │ │ ✅ FastAPI Router Pattern (auth_service.py)          │  │  │
│  │ │ ✅ Error Handling (try/except with logging)          │  │  │
│  │ │ ✅ Pydantic Schema Validation                        │  │  │
│  │ │ ⚠️ New Pattern: OAuth2 Provider (may need ADR)       │  │  │
│  │ └──────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ IMPLEMENTATION PLAN (5 steps)                             │  │
│  │                                                           │  │
│  │ Step 1: Analyze requirements ─────────────────── 0.5h    │  │
│  │ Step 2: Create OAuth2 service ─────────────────── 2.0h   │  │
│  │ Step 3: Integrate with existing auth ──────────── 1.0h   │  │
│  │ Step 4: Write tests ──────────────────────────── 1.5h    │  │
│  │ Step 5: Update documentation ─────────────────── 0.5h    │  │
│  │                                                           │  │
│  │ Total: 230 LOC | 5.5 hours                               │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ DEVIATIONS & RECOMMENDATIONS                              │  │
│  │                                                           │  │
│  │ ⚠️ New OAuth2 pattern may need ADR documentation         │  │
│  │ ℹ️ Consider referencing ADR-001 (Authentication)         │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ [Reject with Notes]  [Request Changes]  [✅ Approve Plan] │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

**Frontend Integration Requirements**:

| Hook | Purpose | Behavior |
|------|---------|----------|
| Session Query | Fetch single planning session | Refresh every 5s if status is pending |
| Sessions List Query | Fetch all planning sessions | Filter by status parameter |
| Approve Mutation | Approve or reject plan | Invalidate sessions cache on success |

> **Implementation Reference**: For React hooks and components, see SDLC-Orchestrator frontend documentation.

**Acceptance Criteria**:
- ✅ AC-01: Dashboard loads <1s (p95)
- ✅ AC-02: Conformance gauge animates smoothly (60fps)
- ✅ AC-03: All components render correctly (Playwright E2E test)
- ✅ AC-04: Approve/reject actions complete <2s
- ✅ AC-05: Responsive design (desktop + tablet, min 768px)

---

### FR-04: GitHub Check Integration

**Requirement**: Create GitHub Check Run on PRs to display conformance score and block merge if score <threshold.

```gherkin
GIVEN a GitHub repository with SDLC Orchestrator integration
  AND GitHub webhook configured for pull_request events
WHEN a PR is opened, synchronized, or reopened
THEN the system MUST:
  1. Trigger GitHub Action workflow (.github/workflows/pattern-conformance.yml)
  2. Workflow runs `sdlcctl plan check --pr-url {pr_url} --threshold 70`
  3. CLI fetches PR diff from GitHub API
  4. CLI runs conformance check (ConformanceCheckService.check_pr_diff)
  5. CLI outputs result as JSON
  6. Workflow creates GitHub Check Run with:
     - name: "Pattern Conformance"
     - status: "completed"
     - conclusion: "success" (score ≥70) OR "neutral" (50-69) OR "failure" (<50)
     - output.title: "✅ Conformance: 85/100 (good)"
     - output.summary: Markdown table with score, level, deviations
  7. Workflow posts PR comment with conformance report
  8. If conclusion = "failure", PR cannot merge (branch protection)
```

**CI/CD Integration Requirements**:

The GitHub integration SHALL support:

| Workflow Step | Requirement |
|---------------|-------------|
| Trigger | On PR events: opened, synchronize, reopened |
| Permissions | contents:read, pull-requests:write, checks:write |
| Check Run | Create with name "Pattern Conformance" |
| Conclusion | success (≥70), neutral (50-69), failure (<50) |
| PR Comment | Post conformance report with score and level |

**CLI Command Requirements**:

| Command | Options | Description |
|---------|---------|-------------|
| `sdlcctl plan check` | --pr-url, --threshold, --format | Check PR conformance |

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| --pr-url | string | required | GitHub PR URL |
| --threshold | int | 70 | Minimum score to pass |
| --format | enum | cli | Output format: cli, json |

> **Implementation Reference**: For GitHub Action workflows and CLI implementation, see SDLC-Orchestrator documentation.

**Acceptance Criteria**:
- ✅ AC-01: GitHub Check Run created <30s after PR opened
- ✅ AC-02: Check conclusion matches score (success ≥70, neutral 50-69, failure <50)
- ✅ AC-03: PR comment posted with conformance report
- ✅ AC-04: Workflow respects GitHub API rate limits (5000 req/hour)
- ✅ AC-05: Failed workflows retry (exponential backoff, max 3 retries)

---

### FR-05: E2E Test Suite

**Requirement**: Comprehensive E2E tests for planning workflow using Playwright.

```gherkin
GIVEN Playwright E2E test suite
WHEN tests run in CI/CD
THEN the system MUST validate:

Test 1: Plan generation flow
  - Navigate to /app/planning/plan-review
  - Start new planning session via API
  - Wait for session to complete
  - Verify session appears in list

Test 2: Pattern extraction accuracy
  - Create test project with known patterns
  - Trigger pattern extraction
  - Verify extracted patterns match expected categories (architecture, error_handling, testing)

Test 3: Conformance scoring
  - Create test PR with known pattern violations
  - Run conformance check
  - Verify score calculation matches expected (e.g., 2 major violations = -30 points)

Test 4: Approval workflow
  - Open session detail page
  - Click "Approve Plan" button
  - Verify session status changes to "approved"
  - Verify approval timestamp recorded

Test 5: Plan review UI
  - Verify task summary renders
  - Verify conformance gauge renders with correct score
  - Verify patterns list renders
  - Verify implementation plan steps render
  - Verify action buttons clickable

Test 6: Session management
  - List sessions API returns correct data
  - Filter by status works (awaiting_approval, approved, rejected)
  - Pagination works (page size, page number)

Test 7: Error handling
  - Test invalid PR URL → Displays error message
  - Test invalid session ID → Shows 404 page
  - Test network timeout → Retries with exponential backoff

Test 8: GitHub Check integration
  - Trigger PR webhook (mocked)
  - Verify GitHub Check Run created
  - Verify PR comment posted
  - Verify check conclusion matches score
```

**E2E Test Requirements**:

| Test Case | Steps | Expected Result |
|-----------|-------|-----------------|
| Plan generation flow | Navigate, create session, wait for completion | Session appears in list with conformance score |
| Conformance scoring accuracy | Create PR with 2 major violations | Score = 70 (100 - 15*2), level = good |
| Approval workflow | Open session, click approve, submit | Status changes to approved |

> **Implementation Reference**: For Playwright test implementation, see SDLC-Orchestrator frontend tests.

**Acceptance Criteria**:
- ✅ AC-01: All 8 E2E tests pass in CI/CD
- ✅ AC-02: Test execution time <3min total
- ✅ AC-03: Tests run in parallel (4 workers)
- ✅ AC-04: Tests generate HTML report with screenshots on failure
- ✅ AC-05: Test coverage ≥80% for frontend planning components

---

## 3. Database Schema

### 3.1 Planning Sessions Data Requirements

**Note**: MVP uses in-memory sessions. Persistence can be added later.

**Planning Session Record Structure**:

| Field | Type | Description |
|-------|------|-------------|
| id | UUID | Primary key |
| project_id | UUID | Reference to project |
| task | text | Task description |
| status | enum | pending, awaiting_approval, approved, rejected |
| patterns_json | JSON | Extracted patterns |
| plan_json | JSON | Generated implementation plan |
| conformance_json | JSON | Conformance check result |
| approved_by | UUID | User who approved (optional) |
| approved_at | timestamp | Approval timestamp (optional) |
| rejection_reason | text | Rejection notes (optional) |
| created_at | timestamp | Creation timestamp |
| updated_at | timestamp | Last update timestamp |

**Required Indexes**:
- Project reference (filter by project)
- Status (filter by status)
- Created timestamp (sort by recency)

> **Implementation Reference**: For SQL schema and migrations, see SDLC-Orchestrator backend documentation.

---

## 4. API Requirements Summary

| Endpoint | Method | Purpose | Auth |
|----------|--------|---------|------|
| /api/v1/planning/subagent/plan | POST | Start new planning session | Bearer token |
| /api/v1/planning/subagent/{id} | GET | Get planning result | Bearer token |
| /api/v1/planning/subagent/{id}/approve | POST | Approve/reject plan | Bearer token |
| /api/v1/planning/subagent/conformance | POST | Check PR conformance | API key OR Bearer |
| /api/v1/planning/subagent/sessions | GET | List active sessions | Bearer token |

> **Implementation Reference**: For detailed API schemas, request/response examples, and error codes, see SDLC-Orchestrator API documentation.

---

## 5. Tier-Specific Requirements

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| **Conformance Checking** | ❌ Not available | ❌ Not available | ✅ Manual (CLI only) | ✅ Automated (CI/CD) |
| **Plan Approval UI** | ❌ Not available | ❌ Not available | ✅ Web dashboard | ✅ Web dashboard |
| **GitHub Check Integration** | ❌ Not available | ❌ Not available | ❌ Not available | ✅ Automated check runs |
| **Pattern Extraction Depth** | N/A | N/A | ✅ 3 levels | ✅ 5 levels |
| **Conformance Threshold** | N/A | N/A | ✅ 50 (default) | ✅ Configurable |
| **Deviation Recommendations** | N/A | N/A | ✅ Basic | ✅ AI-powered (GPT-4o) |
| **E2E Test Coverage** | N/A | N/A | ✅ 80%+ | ✅ 95%+ |

---

## 6. Non-Functional Requirements

### 6.1 Performance

- **Conformance Check**: <5s for 500 LOC diff (p95)
- **API Response Time**: <200ms for all endpoints (p95)
- **Dashboard Load Time**: <1s (p95)
- **GitHub Check Creation**: <30s after PR opened (p95)

### 6.2 Security

- **API Authentication**: JWT tokens for web, API keys for CI/CD
- **Rate Limiting**: 100 req/min per API key (CI/CD), 1000 req/hour per user
- **Input Validation**: Sanitize PR URLs, session IDs, notes
- **RBAC**: Only PM/Tech Lead/Admin can approve plans

### 6.3 Reliability

- **GitHub API Retries**: Exponential backoff, max 3 retries
- **Workflow Failures**: Notify on-call team if >5% workflows fail
- **Data Persistence**: Planning sessions expire after 7 days (GDPR compliance)

### 6.4 Scalability

- **Concurrent Checks**: Support 100 concurrent conformance checks
- **Session Storage**: In-memory for MVP (Redis for scale)
- **GitHub Webhook Queue**: Celery queue for async processing

---

## 7. Acceptance Criteria

### 7.1 Conformance Checking

- ✅ AC-01: Conformance check completes <5s (p95) for 500 LOC diff
- ✅ AC-02: Scoring accuracy ≥95% (validated against manual reviews)
- ✅ AC-03: Detects all 4 deviation types (major, minor, missing ADR, high-risk)
- ✅ AC-04: Recommendations are actionable (specific file + line + fix)
- ✅ AC-05: False positive rate <5%

**Test Method**: Automated integration test with 50 known PRs

### 7.2 API Endpoints

- ✅ AC-01: All 5 endpoints respond <200ms (p95)
- ✅ AC-02: OpenAPI 3.0 documentation auto-generated
- ✅ AC-03: JWT authentication working for Bearer token endpoints
- ✅ AC-04: API key authentication working for /conformance endpoint
- ✅ AC-05: Error responses follow RFC 7807

**Test Method**: Pytest integration tests + Postman collection

### 7.3 Dashboard UI

- ✅ AC-01: Dashboard loads <1s (p95)
- ✅ AC-02: Conformance gauge animates smoothly (60fps)
- ✅ AC-03: All components render correctly (Playwright E2E)
- ✅ AC-04: Approve/reject actions complete <2s
- ✅ AC-05: Responsive design (desktop + tablet, min 768px)

**Test Method**: Playwright E2E tests + Lighthouse performance audit

### 7.4 GitHub Check Integration

- ✅ AC-01: GitHub Check Run created <30s after PR opened
- ✅ AC-02: Check conclusion matches score (success ≥70, neutral 50-69, failure <50)
- ✅ AC-03: PR comment posted with conformance report
- ✅ AC-04: Workflow respects GitHub API rate limits
- ✅ AC-05: Failed workflows retry (exponential backoff, max 3 retries)

**Test Method**: E2E test with real GitHub webhook + mocked PR

### 7.5 E2E Test Suite

- ✅ AC-01: All 8 E2E tests pass in CI/CD
- ✅ AC-02: Test execution time <3min total
- ✅ AC-03: Tests run in parallel (4 workers)
- ✅ AC-04: Tests generate HTML report with screenshots on failure
- ✅ AC-05: Test coverage ≥80% for frontend planning components

**Test Method**: CI/CD pipeline execution

---

## 8. Dependencies

### 8.1 Internal Services

- **PatternExtractionService**: Provides extracted patterns for conformance checks
- **PlanningOrchestratorService**: Generates implementation plans
- **ADRScannerService**: Scans ADRs for architecture decision references

### 8.2 External Services

- **GitHub API**: Fetch PR diffs, create Check Runs, post comments
- **Playwright**: E2E testing framework

### 8.3 Libraries

- **pygithub**: GitHub API client (Python)
- **difflib**: Diff parsing (Python standard library)
- **@playwright/test**: E2E testing (TypeScript)

---

## 9. Migration Plan

### 9.1 Rollout Schedule

- **Week 1**: ConformanceCheckService backend implementation
- **Week 2**: Planning API routes + CLI `sdlcctl plan check`
- **Week 3**: Plan Approval UI components
- **Week 4**: GitHub Check integration + E2E tests
- **Week 5**: Production deployment + BFlow pilot

### 9.2 Pilot Criteria

**BFlow Project Pilot**:
- Enable conformance checks on BFlow repository
- Target: Reduce architectural drift by 50% (18 → 9 violations/month)
- Measure: Track pattern violations before/after for 30 days

---

## 10. Monitoring & Observability

### 10.1 Metrics (Prometheus)

- `conformance_checks_total` (counter): Total conformance checks run
- `conformance_score_distribution` (histogram): Distribution of scores (0-100)
- `conformance_deviations_total` (counter): Total deviations detected by type
- `plan_approvals_total` (counter): Total plan approvals (approved/rejected)
- `github_check_created_total` (counter): GitHub Check Runs created
- `github_api_calls_total` (counter): GitHub API calls by endpoint

### 10.2 Logs (Structured)

**Required Log Fields**:

| Field | Description |
|-------|-------------|
| timestamp | ISO 8601 timestamp |
| level | Log level (INFO, WARN, ERROR) |
| service | Service name (conformance_check) |
| action | Operation (check_pr_diff) |
| pr_url | GitHub PR URL |
| score | Conformance score (0-100) |
| deviations | Number of deviations detected |
| duration_ms | Operation duration in milliseconds |

### 10.3 Alerts

- **High Deviation Rate**: >50% of checks with score <70 → Alert Tech Lead
- **GitHub API Rate Limit**: >80% of 5000 req/hour limit → Alert DevOps
- **Workflow Failure Rate**: >5% workflow failures → Alert DevOps

---

## 11. Testing Strategy

### 11.1 Unit Tests

- ConformanceCheckService: 30 test cases (scoring, deviation detection, recommendations)
- Planning API routes: 20 test cases (endpoints, auth, error handling)

**Coverage Target**: 95%

### 11.2 Integration Tests

- GitHub API integration: 10 test cases (PR diff fetch, Check Run creation, comments)
- Database integration (future): 5 test cases (session CRUD operations)

**Coverage Target**: 90%

### 11.3 E2E Tests

- 8 comprehensive E2E tests (plan generation, approval, conformance, GitHub integration)

**Coverage Target**: 80%

### 11.4 Load Tests

- 100 concurrent conformance checks → Measure latency (target: <5s p95)
- 1000 GitHub webhook events → Measure queue processing (target: <30s p95)

---

## 12. Success Metrics

### 12.1 Adoption

- **Target**: 80% of PROFESSIONAL/ENTERPRISE projects enable conformance checks within 60 days
- **Measurement**: `SELECT COUNT(*) FROM projects WHERE conformance_enabled=true`

### 12.2 Quality

- **Target**: 60% reduction in architectural drift (18 → 7 violations/month)
- **Measurement**: Manual review of monthly pattern violations

### 12.3 Performance

- **Target**: <5s conformance check time (p95)
- **Measurement**: Prometheus metric `conformance_check_duration_seconds`

### 12.4 Business Impact

- **Target**: 50% reduction in code review time (BFlow pilot)
- **Measurement**: Pre/post deployment comparison of PR review durations

---

## 13. Related Specifications

- [SPEC-0001: Anti-Vibecoding Specification](./SPEC-0001-Anti-Vibecoding.md) - Quality assurance context
- [SPEC-0002: Specification Standard](./SPEC-0002-Specification-Standard.md) - Specification format
- [SPEC-0003: AI Context Engine Architecture](./SPEC-0003-AI-Context-Engine-Architecture.md) - Pattern extraction integration
- [SPEC-0011: AI Task Decomposition Service](./SPEC-0011-AI-Task-Decomposition.md) - Planning orchestration
- [SPEC-0018: AGENTS.md Technical Implementation](./SPEC-0018-AGENTS-MD-Technical-Implementation.md) - Context integration

---

## Document Control

| Field | Value |
|-------|-------|
| **Spec ID** | SPEC-0019 |
| **Version** | 2.0.0 |
| **Status** | APPROVED |
| **Author** | Backend Lead |
| **Reviewer** | CTO |
| **Last Updated** | 2026-01-29 |
| **Framework Version** | 6.0.5 |

---

**Pure Methodology Notes**:
- This specification defines WHAT conformance testing requires
- For HOW to implement (service classes, database schemas, API endpoints), see SDLC-Orchestrator documentation
- Scoring criteria and deviation types are governance standards; implementation tools may vary
- Tier requirements define capability expectations, not technical constraints

---

**End of Specification**
