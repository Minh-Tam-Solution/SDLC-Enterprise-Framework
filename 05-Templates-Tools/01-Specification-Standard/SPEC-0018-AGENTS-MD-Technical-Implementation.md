# SPEC-0018: AGENTS.md Technical Implementation

## Frontmatter

```yaml
spec_id: SPEC-0018
title: AGENTS.md Technical Implementation Specification
version: 2.0.0
status: approved
tier: PROFESSIONAL
pillar: Section 7 - Quality Assurance System
owner: Backend Lead + CTO
last_updated: 2026-01-29
tags:
  - agents-md
  - technical
  - implementation
  - static-generator
  - dynamic-overlay
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
  - SPEC-0003  # AI Context Engine
  - SPEC-0017  # Feedback Learning Service
epic: EP-07 AGENTS.md Framework
sprint: Sprint 80-85
implementation_ref: "SDLC-Orchestrator/docs/02-design/14-Technical-Specs/AGENTS-MD-Technical-Design.md"
```

---

---

## Executive Summary

This specification defines the **governance requirements** for AGENTS.md Technical Implementation - a two-layer architecture combining static context files with dynamic overlay injection for AI-assisted development.

**Key Governance Principles**:
- Static AGENTS.md files provide baseline AI context (≤150 lines)
- Dynamic overlays inject real-time gate status, learnings, and incidents
- Multi-channel delivery ensures AI tools receive current context
- Secret detection prevents credential leakage

**Business Value**:
- 40% reduction in AI hallucinations (tested in pilot)
- Real-time context vs. stale static files
- Enforcement through OPA policy guards

> **Implementation Reference**: For technical implementation details (service classes, database schemas, API endpoints), see SDLC-Orchestrator documentation.

---

## 1. Overview

### 1.1 Purpose

This specification defines the **governance requirements** for AGENTS.md Technical Implementation - a two-layer architecture combining static context files with dynamic overlay injection for AI-assisted development.

**Industry Context**: AGENTS.md has become the **de facto standard** for AI context (60K+ repos on GitHub), but existing implementations are **static and manual**. SDLC Orchestrator differentiates by adding **dynamic overlay** capabilities that inject real-time project state, quality gates status, and learning feedback into AI context.

### 1.2 Background

**Static AGENTS.md (Industry Standard)**:
- Manually created markdown file (≤150 lines recommended)
- Checked into repository root
- Contains: Project overview, architecture principles, coding standards, common patterns
- **Limitation**: Stale context (manual updates required)

**Dynamic Overlay (SDLC Orchestrator Innovation)**:
- Real-time context injection based on current gate status, recent learnings, active incidents
- Delivered via 4 channels: PR comments, CLI output, GitHub Check Runs, API responses
- **Advantage**: Always up-to-date, actionable guidance

### 1.3 Strategic Value

**Moat Analysis** (vs. Static AGENTS.md):

| Capability | Static AGENTS.md | SDLC Orchestrator Dynamic |
|------------|------------------|---------------------------|
| **Context Freshness** | Manual updates (days/weeks lag) | Real-time (≤5s after gate change) |
| **Enforcement** | Guidance only | OPA policy guards (hard block) |
| **Learning Loop** | No feedback mechanism | PR reviews → Hints → AI improvement |
| **Gate Integration** | Not aware of gates | Gate-aware context ("G3 passed, strict mode") |
| **Evidence Trail** | No audit | Full lineage (overlay → evidence → gate) |
| **Multi-Channel** | File-only | PR comment + CLI + Check Run + API |

**ROI**: 40% reduction in AI hallucinations (tested in BFlow pilot) by providing real-time constraints.

## 2. Functional Requirements

### FR-01: Static AGENTS.md Generation

**Description**: Generate and maintain static AGENTS.md file (≤150 lines) in repository root.

**Requirement**:

```gherkin
GIVEN a project registered in the governance system
  AND the project has architecture documentation
WHEN static AGENTS.md generation is triggered
THEN the system SHALL:
  - Extract project metadata (name, tech stack, framework version)
  - Extract architecture principles from documentation
  - Extract coding standards from tier requirements
  - Extract common patterns from codebase (top 5 by frequency)
  - Generate AGENTS.md markdown (≤150 lines for PROFESSIONAL tier)
  - Validate format against markdown linting rules
  - Scan for secrets using detection patterns
  - Store with integrity hash (SHA256)
  - Commit to repository root
AND the system SHALL validate:
  - Line count within tier limits (≤150 for PROFESSIONAL)
  - No secrets detected (API keys, passwords, tokens)
  - Valid markdown format (MD001-MD050 rules)
  - Unique active file per project
```

**Data Requirements**:

| Field | Purpose | Required |
|-------|---------|----------|
| Project reference | Link to owning project | Yes |
| Content | Generated markdown | Yes |
| File hash | SHA256 for integrity | Yes |
| Line count | Enforce tier limits | Yes |
| Template used | Template name | Yes |
| Status | active/archived | Yes |
| Commit reference | GitHub commit SHA | No |

---

### FR-02: AGENTS.md Validation

**Description**: Validate AGENTS.md files for format compliance, secret detection, and linting.

**Requirement**:

```gherkin
GIVEN an AGENTS.md file (static or proposed update)
WHEN validation is triggered
THEN the system SHALL:
  - Check line count against tier limits (fail if exceeded in strict mode)
  - Validate markdown syntax (headings, lists, code blocks)
  - Scan for secrets using 15 standard patterns
  - Check for prohibited content (absolute file paths, hardcoded IPs)
  - Lint with markdownlint rules (MD001-MD050)
AND the system SHALL return validation result with:
  - Valid/invalid status
  - Errors with severity classification (critical, high, medium, low)
  - Warnings for non-blocking issues
  - Line count
  - Secrets found with type, location, and pattern matched
```

**Secret Detection Patterns** (15 standard):

| Pattern Category | Description | Severity |
|-----------------|-------------|----------|
| API Keys | api_key, apikey patterns | Critical |
| Passwords | secret, password, passwd, pwd | Critical |
| Tokens | token, auth_token patterns | Critical |
| GitHub PAT | ghp_* patterns | Critical |
| OpenAI Key | sk-* patterns | Critical |
| AWS Keys | AKIA* patterns | Critical |
| Private Keys | BEGIN PRIVATE KEY | Critical |
| Database URLs | Connection strings with credentials | High |
| IP Addresses | Hardcoded internal IPs | Medium |
| File Paths | Absolute system paths | Low |

---

### FR-03: Dynamic Context Overlay Generation

**Description**: Generate real-time context overlays based on project state and inject into AI workflows.

**Requirement**:

```gherkin
GIVEN a project with active gates, recent PRs, and learning feedback
WHEN context overlay generation is triggered
THEN the system SHALL:
  - Fetch current gate status (G0-G4, pass/fail, last evaluated)
  - Fetch recent learnings (last 7 days, top 5 by severity)
  - Fetch active incidents (P0/P1 only, last 30 days)
  - Fetch decomposition hints (confidence ≥0.7, last 90 days)
  - Generate overlay markdown (≤50 lines recommended)
  - Store with trigger event and context type
  - Set expiration based on trigger type
AND the system SHALL validate:
  - Overlay generation completes within 5s (p95)
  - Content is valid markdown format
  - No stale data included (gate status within last 1h)
```

**Context Types**:

| Type | Description | TTL |
|------|-------------|-----|
| gates | Current gate status (G0-G4) | 1 hour |
| learnings | Recent PR learnings | 1 hour |
| incidents | Active P0/P1 incidents | 5 minutes |
| hints | Decomposition hints (≥0.7 confidence) | 1 hour |
| full | Combined context (all types) | 1 hour |

**Trigger Events**:

| Event | Description | Default TTL |
|-------|-------------|-------------|
| pr_created | Pull request opened | 1 hour |
| cli_invoked | CLI command executed | 5 minutes |
| check_run_started | GitHub Check Run started | 1 hour |
| api_request | API request with overlay | 5 minutes |

**Overlay Content Structure**:
- Gates Status: Current gate pass/fail with blockers
- Recent Learnings: Top 5 by severity (last 7 days)
- Active Incidents: P0/P1 only with guidance
- Decomposition Hints: High-confidence patterns

---

### FR-04: Multi-Channel Overlay Delivery

**Description**: Deliver dynamic overlays via 4 channels: PR comments, CLI output, GitHub Check Runs, API responses.

**Requirement**:

```gherkin
GIVEN a generated context overlay
WHEN overlay delivery is triggered for a specific channel
THEN the system SHALL:

  FOR channel='pr_comment':
    - Post overlay content as GitHub PR comment
    - Collapse previous overlay comments (minimize clutter)
    - Mark overlay as delivered with channel and timestamp

  FOR channel='cli_output':
    - Return overlay content to stdout
    - Format for terminal (ANSI colors, emoji support)
    - Mark overlay as delivered with channel and timestamp

  FOR channel='check_run':
    - Create GitHub Check Run with overlay as summary
    - Set check status based on gate failures (pass/fail)
    - Mark overlay as delivered with channel and timestamp

  FOR channel='api':
    - Include overlay in API response header (X-SDLC-Context)
    - Or embed in response body (if client supports)
    - Mark overlay as delivered with channel and timestamp
```

**Channel Specifications**:

| Channel | Format | Latency Target | Use Case |
|---------|--------|----------------|----------|
| pr_comment | Markdown | <3s (p95) | Human review in PR |
| cli_output | ANSI/Markdown | <1s (p95) | Developer terminal |
| check_run | GitHub Check | <5s (p95) | CI/CD integration |
| api | Base64 header | <100ms (p95) | API client integration |

---

### FR-05: AGENTS.md CLI Commands

**Description**: Provide CLI commands for AGENTS.md initialization, validation, and linting.

**Requirement**:

```gherkin
GIVEN CLI tool installed
WHEN user runs AGENTS.md commands
THEN the system SHALL support:

  sdlc agents init [--template=default|minimal|comprehensive] [--dry-run]:
    - Generate AGENTS.md for current project
    - Detect project metadata from .git, package.json, pyproject.toml
    - Output to AGENTS.md (or stdout if --dry-run)
    - Validate before writing (fail if >150 lines or secrets found)

  sdlc agents validate [--strict] [--file=path/to/AGENTS.md]:
    - Validate AGENTS.md format, secrets, linting
    - Exit code 0 if valid, 1 if errors, 2 if warnings (strict mode)
    - Output validation report (JSON or human-readable)

  sdlc agents lint [--fix] [--file=path/to/AGENTS.md]:
    - Run markdownlint on AGENTS.md
    - Apply fixes if --fix flag provided
    - Output linting report

  sdlc agents overlay [--type=gates|learnings|hints|full]:
    - Generate and display current context overlay
    - Fetch from governance API
    - Output to stdout (formatted for terminal)
```

**CLI Command Specifications**:

| Command | Purpose | Latency Target | Exit Codes |
|---------|---------|----------------|------------|
| init | Generate AGENTS.md | <5s | 0=success, 1=error |
| validate | Validate file | <2s | 0=valid, 1=errors, 2=warnings |
| lint | Lint with fixes | <2s | 0=pass, 1=fail |
| overlay | Display context | <3s | 0=success, 1=error |

---

### FR-06: Version Control Webhook Integration

**Description**: React to version control events to trigger overlay generation and delivery.

**Requirement**:

```gherkin
GIVEN webhook configured for project repository
WHEN version control event occurs
THEN the system SHALL:

  FOR event='pull_request' (action='opened' OR 'synchronize'):
    - Generate context overlay (type='full')
    - Deliver via PR comment channel
    - Create Check Run with overlay summary
    - Store overlay with trigger_event='pr_created'

  FOR event='check_run' (action='rerequested'):
    - Regenerate context overlay (type='gates')
    - Update Check Run with latest gate status
    - Store overlay with trigger_event='check_run_started'

  FOR event='push' (branch='main'):
    - Archive previous active AGENTS.md (status='archived')
    - Regenerate AGENTS.md with updated codebase patterns
    - Commit to repository if content changed

AND the system SHALL validate:
  - Webhook signature (HMAC-SHA256) for security
  - Event payload structure
  - Project repository mapping exists
```

**Event Specifications**:

| Event | Actions | Overlay Type | Delivery Channels |
|-------|---------|--------------|-------------------|
| pull_request | opened, synchronize | full | pr_comment, check_run |
| check_run | rerequested | gates | check_run |
| push | main branch | N/A (regenerates AGENTS.md) | N/A |

**Webhook Security**:
- HMAC-SHA256 signature validation required
- Failed signature → reject with 403 Forbidden
- Failed webhooks retried (exponential backoff, max 3 retries)

---

### FR-07: Template System

**Description**: Support multiple AGENTS.md templates for different project types.

**Requirement**:

```gherkin
GIVEN predefined templates (default, minimal, comprehensive)
WHEN AGENTS.md generation with a template is triggered
THEN the system SHALL:
  - Load template from configured location
  - Detect project type (backend, frontend, fullstack, mobile)
  - Extract tier-specific requirements
  - Render template with project variables
  - Validate rendered output against line limits
AND the system SHALL enforce:
  - Default template ≤100 lines
  - Minimal template ≤50 lines
  - Comprehensive template ≤200 lines (ENTERPRISE only)
  - Template rendering <1s (p95)
```

**Template Specifications**:

| Template | Line Limit | Tier | Content |
|----------|------------|------|---------|
| default | ≤100 lines | ALL | Project overview, principles, top 5 patterns |
| minimal | ≤50 lines | ALL | Tech stack, tier, key standards only |
| comprehensive | ≤200 lines | ENTERPRISE | Full architecture, all patterns, ADRs |

**Template Content Requirements**:

Default template MUST include:
- Project name and tech stack
- Framework version and tier
- Top 5 architecture principles
- Tier-specific coding standards
- Top 5 common patterns with examples

Minimal template MUST include:
- Project name and tech stack
- Tier classification
- Top 3 key standards

Comprehensive template MUST include (ENTERPRISE only):
- All default content
- Full architecture documentation
- All patterns (not limited to 5)
- Related ADRs
- Security requirements

---

### FR-08: Overlay Expiration & Cleanup

**Description**: Automatically expire and clean up stale context overlays.

**Requirement**:

```gherkin
GIVEN context overlays with configured TTLs
WHEN periodic cleanup task runs (every 5 minutes)
THEN the system SHALL:
  - Query overlays where expiration time has passed
  - Archive expired overlays (soft delete)
  - Update delivery timestamp if not already set
  - Log cleanup statistics (overlays_expired, oldest_overlay_age)
  - Delete overlays older than 30 days (hard delete, GDPR compliance)
AND the system SHALL ensure:
  - Soft delete occurs within 1 minute of expiration
  - Hard delete after 30 days for data retention compliance
  - Cleanup runs in background (no API performance impact)
  - Cleanup metrics published for monitoring
```

**Cleanup Specifications**:

| Action | Trigger | Retention | Compliance |
|--------|---------|-----------|------------|
| Soft delete | expires_at <= NOW() | Immediate | Standard |
| Hard delete | created_at <= 30 days ago | 30 days | GDPR |

**Monitoring Requirements**:
- Expired overlay count per run
- Hard deleted count per run
- Oldest overlay age
- Cleanup duration

---

## 3. Data Requirements

### 3.1 AGENTS.md File Records

AGENTS.md file records SHALL contain:

| Field | Purpose | Required |
|-------|---------|----------|
| Unique identifier | Record identification | Yes |
| Project reference | Link to owning project | Yes |
| Content | Generated markdown text | Yes |
| File hash | SHA256 for integrity verification | Yes |
| Line count | Enforce tier limits (≤150 for PROFESSIONAL) | Yes |
| Status | active/archived lifecycle | Yes |
| Template used | Template name for generation | Yes |
| Generation timestamp | When file was generated | Yes |
| Commit reference | Version control commit SHA | No |
| Commit timestamp | When committed to repository | No |

**Constraints**:
- Only one active file per project at a time
- Line count must not exceed 150 (PROFESSIONAL tier)
- Cascade delete when project is removed

### 3.2 Context Overlay Records

Context overlay records SHALL contain:

| Field | Purpose | Required |
|-------|---------|----------|
| Unique identifier | Record identification | Yes |
| Project reference | Link to owning project | Yes |
| Overlay hash | SHA256 for integrity | Yes |
| Content | Markdown overlay text | Yes |
| Context type | gates/learnings/incidents/hints/full | Yes |
| Trigger event | What triggered generation | Yes |
| Creation timestamp | When created | Yes |
| Expiration timestamp | When overlay expires | Yes |
| Delivery channel | pr_comment/cli_output/check_run/api | No |
| Delivery timestamp | When delivered | No |
| Deletion timestamp | Soft delete marker | No |

**Constraints**:
- Context type must be one of: gates, learnings, incidents, hints, full
- Cascade delete when project is removed
- Soft delete before hard delete (30 days retention)

---

## 4. API Requirements

### 4.1 Required Endpoints

Implementations SHALL provide the following API capabilities:

| Endpoint Purpose | Method | Description |
|-----------------|--------|-------------|
| Generate AGENTS.md | POST | Generate static file with template selection |
| Validate AGENTS.md | POST | Validate content for format and secrets |
| Create Overlay | POST | Generate context overlay by type |
| Deliver Overlay | POST | Deliver overlay via specified channel |
| Get Current AGENTS.md | GET | Retrieve active file for project |
| List Overlays | GET | List overlays with filtering |

### 4.2 Generate AGENTS.md

**Input Requirements**:
- Template selection (default, minimal, comprehensive)
- Dry run option (preview without commit)

**Output Requirements**:
- Generated content
- File hash (SHA256)
- Line count
- Template used
- Generation timestamp

### 4.3 Validate AGENTS.md

**Input Requirements**:
- Content to validate
- Strict mode flag

**Output Requirements**:
- Validation status (valid/invalid)
- Errors with severity and line numbers
- Warnings list
- Line count
- Secrets found (if any)

### 4.4 Create Overlay

**Input Requirements**:
- Context type (gates, learnings, incidents, hints, full)
- Trigger event (pr_created, cli_invoked, check_run_started, api_request)

**Output Requirements**:
- Generated overlay content
- Overlay hash (SHA256)
- Context type
- Expiration timestamp

### 4.5 Deliver Overlay

**Input Requirements**:
- Target channel (pr_comment, cli_output, check_run, api)
- Channel-specific parameters (PR number, etc.)

**Output Requirements**:
- Delivery channel used
- Delivery timestamp
- Channel-specific result (comment URL, etc.)

---

## 5. Tier-Specific Requirements

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| **Static AGENTS.md Generation** | ❌ Manual | ✅ CLI only | ✅ CLI + API | ✅ Full automation |
| **Dynamic Overlay** | ❌ Not available | ❌ Not available | ✅ Gates + Learnings | ✅ Full context |
| **Multi-Channel Delivery** | ❌ Not available | ❌ Not available | ✅ PR + CLI | ✅ All 4 channels |
| **Template System** | ❌ Not available | ✅ Default only | ✅ Default + Minimal | ✅ All 3 templates |
| **GitHub Webhook** | ❌ Not available | ❌ Not available | ✅ PR events only | ✅ All events |
| **Overlay TTL** | N/A | N/A | ✅ 1h (fixed) | ✅ Configurable |
| **Secret Detection** | ❌ Not available | ✅ Basic (5 patterns) | ✅ Standard (15 patterns) | ✅ Custom patterns |
| **CLI Commands** | ❌ Not available | ✅ init, validate | ✅ + lint | ✅ + overlay |

---

## 6. Non-Functional Requirements

### 6.1 Performance

- **AGENTS.md Generation**: <5s for 100-line file (p95)
- **Overlay Creation**: <5s for full context (p95)
- **PR Comment Delivery**: <10s after PR opened (p95)
- **Validation**: <2s for 150-line file (p95)
- **CLI Commands**: <3s for all operations (p95)

### 6.2 Security

- **Secret Detection**: 15 regex patterns, 100% recall on test set
- **Webhook Signature**: HMAC-SHA256 validation (GitHub standard)
- **Content Sanitization**: Prevent XSS in overlays (markdown escaping)
- **Access Control**: RBAC for API endpoints (PM/Dev/Admin roles)

### 6.3 Reliability

- **Webhook Retries**: Exponential backoff, max 3 retries
- **Overlay Expiration**: Automatic cleanup every 5 minutes
- **Idempotency**: Safe to regenerate AGENTS.md multiple times
- **Fallback**: If overlay fails, return empty (don't block workflow)

### 6.4 Scalability

- **Concurrent Overlays**: Support 100 concurrent overlay generations
- **Database Size**: Partition context_overlays by created_at (monthly)
- **GitHub API Rate Limits**: Respect 5000 req/hour limit (exponential backoff)

---

## 7. Acceptance Criteria

### 7.1 Static AGENTS.md

- ✅ AC-01: Generate valid AGENTS.md ≤150 lines (PROFESSIONAL tier)
- ✅ AC-02: No secrets detected (15 patterns, 100% recall)
- ✅ AC-03: Valid markdown format (passes markdownlint MD001-MD050)
- ✅ AC-04: Successfully committed to repository root
- ✅ AC-05: File hash matches committed content (integrity check)

**Test Method**: Automated integration test with real GitHub repo

### 7.2 Dynamic Overlay

- ✅ AC-01: Overlay generation <5s (p95)
- ✅ AC-02: Overlay content ≤50 lines (recommended)
- ✅ AC-03: Expires after configured TTL (1h for PR, 5m for CLI)
- ✅ AC-04: No stale data (gate status within last 1h)
- ✅ AC-05: Markdown format valid (passes markdownlint)

**Test Method**: Pytest with mocked gate/learning/incident data

### 7.3 Multi-Channel Delivery

- ✅ AC-01: PR comment posted <10s after PR opened (p95)
- ✅ AC-02: Previous overlay comments collapsed (GitHub minimize API)
- ✅ AC-03: CLI output formatted with ANSI colors (supports emoji)
- ✅ AC-04: Check Run created <5s (GitHub Checks API)
- ✅ AC-05: API header X-SDLC-Context included (Base64 encoded)

**Test Method**: E2E test with real GitHub webhook events

### 7.4 Validation

- ✅ AC-01: Detects all 15 secret patterns (100% recall on test set)
- ✅ AC-02: Markdownlint integration (MD001-MD050 rules)
- ✅ AC-03: Line count enforcement (≤150 lines in strict mode)
- ✅ AC-04: Validation time <2s for 150-line file (p95)
- ✅ AC-05: No false positives on code examples (base64, UUIDs)

**Test Method**: Unit test with 100 test cases (50 valid, 50 invalid)

### 7.5 CLI Commands

- ✅ AC-01: `sdlc agents init` generates valid AGENTS.md <5s
- ✅ AC-02: `sdlc agents validate` detects all 15 secret patterns
- ✅ AC-03: `sdlc agents lint --fix` applies markdownlint fixes
- ✅ AC-04: `sdlc agents overlay` fetches and displays overlay <3s
- ✅ AC-05: All commands support --help and error messages

**Test Method**: CLI integration test with pytest-subprocess

### 7.6 GitHub Webhook

- ✅ AC-01: PR comment posted <10s after PR opened (p95)
- ✅ AC-02: Check Run created <5s after PR opened
- ✅ AC-03: AGENTS.md regenerated <30s after main branch push
- ✅ AC-04: Webhook signature validated (HMAC-SHA256)
- ✅ AC-05: Failed webhooks retried (exponential backoff, max 3 retries)

**Test Method**: Locust load test simulating 100 concurrent PRs

---

## 8. Dependencies

### 8.1 Internal Services

- **GateEngine**: Provides current gate status for overlays
- **FeedbackLearningService**: Provides recent learnings for overlays
- **IncidentManagementService**: Provides active incidents for overlays
- **GitHubService**: Posts PR comments, creates Check Runs, commits files

### 8.2 External Services

- **GitHub API**: Webhooks, PR comments, Check Runs, file commits
- **markdownlint**: Linting AGENTS.md files (MD001-MD050 rules)
- **Ollama/Claude**: AI-powered categorization (fallback chain)

### 8.3 Libraries

- **Jinja2**: Template rendering for AGENTS.md generation
- **regex**: Secret detection patterns (15 regex patterns)
- **hashlib**: SHA256 hashing for file integrity
- **celery**: Periodic task for overlay expiration cleanup

---

## 9. Migration Requirements

### 9.1 Existing Project Migration

Migration for existing projects SHALL:

1. Scan all registered projects for existing AGENTS.md files
2. Import existing content into governance system
3. Validate format against current tier requirements
4. Detect any secrets using standard patterns
5. If validation fails:
   - Generate new AGENTS.md using default template
   - Archive existing file with validation errors documented
6. Commit to repository if content changed

### 9.2 Migration Phases

| Phase | Scope | Duration | Rollback |
|-------|-------|----------|----------|
| 1 | Internal projects only | 1 week | Full |
| 2 | Pilot customers (5) | 1 week | Partial |
| 3 | All PROFESSIONAL tier | 2 weeks | Partial |
| 4 | All ENTERPRISE tier | 1 week | Partial |
| 5 | General availability | Ongoing | N/A |

### 9.3 Data Migration Validation

Migration validation SHALL verify:
- All existing AGENTS.md files imported
- Line counts match original files
- File hashes verify content integrity
- No secrets detected in migrated content
- Foreign key relationships intact

---

## 10. Monitoring & Observability

### 10.1 Required Metrics

Implementations SHALL publish the following metrics:

| Metric | Type | Description |
|--------|------|-------------|
| agents_md_generated_total | Counter | Total AGENTS.md files generated |
| agents_md_validation_failures_total | Counter | Validation failures by type |
| agents_md_secrets_detected_total | Counter | Secrets detected by pattern |
| context_overlay_created_total | Counter | Overlays created by context_type |
| context_overlay_delivered_total | Counter | Overlays delivered by channel |
| context_overlay_expired_total | Counter | Overlays expired |
| webhook_received_total | Counter | Webhooks received by event type |
| external_api_calls_total | Counter | External API calls by endpoint |
| cli_command_executed_total | Counter | CLI commands executed |

### 10.2 Required Log Fields

Structured logs SHALL include:
- Timestamp (ISO 8601)
- Log level (DEBUG, INFO, WARN, ERROR)
- Service name
- Action performed
- Project identifier
- Relevant entity identifiers
- Duration (milliseconds)
- Error details (if applicable)

### 10.3 Required Alerts

| Alert | Condition | Severity | Notification |
|-------|-----------|----------|--------------|
| High Secret Detection | >10 secrets/hour | Critical | Security team |
| Webhook Failure Rate | >5% failures | High | DevOps |
| Overlay Expiration Lag | Cleanup >10min behind | Medium | Operations |
| External API Rate Limit | >80% limit | High | DevOps |

---

## 11. Testing Strategy

### 11.1 Unit Tests

- AgentsMdService: 20 test cases (generation, validation, template rendering)
- AgentsMdValidator: 50 test cases (15 secret patterns, markdownlint rules)
- ContextOverlayService: 30 test cases (overlay creation, delivery, expiration)

**Coverage Target**: 95%

### 11.2 Integration Tests

- GitHub API integration: 10 test cases (PR comments, Check Runs, file commits)
- Database transactions: 15 test cases (agents_md_files, context_overlays)
- Celery tasks: 5 test cases (overlay expiration cleanup)

**Coverage Target**: 90%

### 11.3 E2E Tests

- Full workflow: PR opened → Overlay generated → Comment posted → Check Run created
- CLI workflow: `sdlc agents init` → `sdlc agents validate` → `sdlc agents lint`
- Webhook workflow: GitHub push → AGENTS.md regenerated → Committed to repo

**Coverage Target**: 80%

### 11.4 Load Tests

- 100 concurrent PR webhooks → Measure overlay generation latency (target: <10s p95)
- 1000 CLI validations → Measure validation latency (target: <2s p95)
- 10K overlay expirations → Measure Celery task performance (target: <1min)

---

## 12. Rollout Plan

### Phase 1: Internal Pilot (Week 1)
- Deploy to SDLC Orchestrator project only
- Enable static AGENTS.md generation (FR-01)
- Enable validation (FR-02)
- Collect feedback from team

### Phase 2: BFlow Integration (Week 2)
- Deploy to BFlow project
- Enable dynamic overlay (FR-03)
- Enable PR comment delivery (FR-04)
- Measure 40% hallucination reduction target

### Phase 3: CLI Rollout (Week 3)
- Release `sdlc agents` CLI commands (FR-05)
- Enable for all PROFESSIONAL tier projects
- Document CLI usage in SDLC Framework

### Phase 4: GitHub Webhook (Week 4)
- Enable GitHub webhook integration (FR-06)
- Enable for all ENTERPRISE tier projects
- Monitor webhook failure rate

### Phase 5: General Availability (Week 5)
- Enable for all tiers (LITE: manual, STANDARD: CLI, PRO/ENT: full)
- Announce in SDLC Framework release notes
- Update documentation in Framework 6.0.5

---

## 13. Success Metrics

### 13.1 Adoption

- **Target**: 80% of PROFESSIONAL/ENTERPRISE projects have AGENTS.md within 30 days
- **Measurement**: `SELECT COUNT(*) FROM agents_md_files WHERE status='active'`

### 13.2 Quality

- **Target**: <2% secret detection false positives
- **Measurement**: Manual review of 100 flagged secrets

### 13.3 Performance

- **Target**: <10s PR comment delivery (p95)
- **Measurement**: Prometheus metric `context_overlay_delivered_duration_seconds`

### 13.4 Business Impact

- **Target**: 40% reduction in AI hallucinations (BFlow pilot)
- **Measurement**: Pre/post deployment comparison of PR review comments

---

## 14. References

### Related Specifications
- **[SPEC-0001](./SPEC-0001-Anti-Vibecoding.md)**: Anti-Vibecoding (Vibecoding Index, Progressive Routing)
- **[SPEC-0002](./SPEC-0002-Specification-Standard.md)**: Specification Standard (Framework 6.0.5 format)
- **[SPEC-0003](./SPEC-0003-AI-Context-Engine-Architecture.md)**: AI Context Engine (Stage-aware prompts)
- **[SPEC-0017](./SPEC-0017-Feedback-Learning-Service.md)**: Feedback Learning Service (PR learning → hints)

### External Standards
- AGENTS.md: Industry standard for AI context (60K+ repos)
- Markdownlint: MD001-MD050 rules
- HMAC-SHA256: Webhook signature standard

> **Implementation Reference**: For implementation details (service classes, database schemas, CLI tools), see SDLC-Orchestrator documentation.

---

## Document Control

| Field | Value |
|-------|-------|
| **Spec ID** | SPEC-0018 |
| **Version** | 2.0.0 |
| **Status** | APPROVED |
| **Author** | Backend Lead |
| **Reviewer** | CTO |
| **Last Updated** | 2026-01-29 |
| **Framework Version** | 6.0.5 |

---

**Pure Methodology Notes**:
- This specification defines WHAT AGENTS.md implementation requires
- For HOW to implement (service classes, database migrations, CLI code), see SDLC-Orchestrator documentation
- Tier requirements define capability expectations, not technical constraints
- Template specifications are format requirements, not implementation templates

---

**End of Specification**
