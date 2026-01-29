# SPEC-0007: AGENTS.md Technical Design

## Frontmatter

```yaml
spec_id: SPEC-0007
title: AGENTS.md Technical Design - Static Generator + Dynamic Overlay
version: 1.0.0
status: approved
tier: PROFESSIONAL
pillar: Pillar 4 - Build & Implementation
owner: Backend Lead + CTO
last_updated: 2026-01-29
tags:
  - agents-md
  - ai-context
  - static-generator
  - dynamic-overlay
  - ep-07
related_specs:
  - SPEC-0003  # AI Context Engine
  - SPEC-0004  # Policy Guards
  - SPEC-0009  # Codegen Service
  - SPEC-0016  # AGENTS.md Integration
  - SPEC-0018  # AGENTS.md Technical Implementation
epic: EP-07 AGENTS.md Framework
sprint: Sprint 80
```

---

## 1. Overview

### 1.1 Purpose

This specification defines the technical design for implementing AGENTS.md integration in SDLC Orchestrator, based on CTO-approved ADR-029. The implementation follows a **two-layer architecture**:

1. **Static AGENTS.md**: Committed to repository, read by AI coding tools (Cursor, Claude Code, Copilot)
2. **Dynamic Overlay**: Runtime context delivered via PR comments, CLI, API (NOT committed to git)

### 1.2 Strategic Context

**Problem**: AI coding tools (Cursor, Claude Code, Copilot) lack project-specific context, leading to:
- Generic code generation that violates project conventions
- Security issues (AGPL contamination, hardcoded secrets)
- Violations of Zero Mock Policy
- Unaware of current SDLC stage and constraints

**Solution**: Two-layer AGENTS.md system that provides:
- **Static layer**: Project-wide conventions, architecture, security rules (committed to repo)
- **Dynamic layer**: Current SDLC stage, sprint context, active constraints (delivered at runtime)

**Expert Feedback Integration**:
- ✅ Dynamic via commits = git pollution → **Overlay via PR comments, NOT commits**
- ✅ 150-line limit for AI context windows → **Enforced in generator**
- ✅ No secrets in AGENTS.md → **Validator with secret patterns**
- ✅ Static + Dynamic separation → **Two-layer architecture**

### 1.3 Scope

**In Scope**:
- AGENTS.md Generator Service (analyze project → generate compliant AGENTS.md)
- AGENTS.md Validator/Linter (detect secrets, enforce line limits, check structure)
- Context Overlay Service (generate dynamic context from SDLC state)
- CLI commands (`sdlcctl agents init/validate/lint`)
- API endpoints (4 new endpoints for generation, validation, overlay retrieval)
- PR comment integration (inject overlay into PR conversations)
- Database schema (2 new tables: `agents_md_files`, `context_overlays`)

**Out of Scope** (Sprint 81+):
- VS Code Extension integration
- GitHub Check Run overlay injection
- Multi-repo AGENTS.md management
- AGENTS.md version history UI

---

## 2. Functional Requirements

### FR-001: AGENTS.md Generation from Project Analysis

**GIVEN** a project with codebase configuration files (docker-compose.yml, package.json, requirements.txt, tsconfig.json)
**WHEN** user runs `sdlcctl agents init` or calls `POST /api/v1/projects/{id}/agents-md/generate`
**THEN** the system MUST:
1. Analyze project structure using FileAnalyzer
2. Generate AGENTS.md with sections: Quick Start, Architecture, Current Stage, Conventions, Security, Git Workflow, DO NOT
3. Enforce line limit (≤150 lines recommended, ≤200 lines max)
4. Validate generated content for secrets/credentials
5. Return AgentsMdFile with content, hash, line count, validation status
6. Save generation history to `agents_md_files` table for audit

**Tier-Specific Requirements**:
| Tier | Max Lines | Sections | Secret Detection | Audit Trail |
|------|-----------|----------|------------------|-------------|
| LITE | 200 | Basic (Quick Start, Conventions, DO NOT) | ❌ | ❌ |
| STANDARD | 150 | Standard (+ Architecture, Security) | ✅ | ⚠️ (90 days) |
| PROFESSIONAL | 150 | Full (+ Git Workflow, Current Stage) | ✅ | ✅ (1 year) |
| ENTERPRISE | 150 | Full + AGPL rules | ✅ | ✅ (Permanent) |

**Acceptance Criteria**:
| Criteria | Pass Condition |
|----------|----------------|
| **Generation Speed** | <2s for p95 (API response time) |
| **Line Count** | 100-150 lines for typical project |
| **Section Coverage** | All enabled sections present |
| **Secret Detection** | 100% catch rate for known API key patterns |
| **Audit Trail** | All generations logged with project_id, user_id, timestamp |

---

### FR-002: AGENTS.md Validation and Secret Detection

**GIVEN** an AGENTS.md file content (from file or user input)
**WHEN** user runs `sdlcctl agents validate` or calls `POST /api/v1/agents-md/validate`
**THEN** the system MUST:
1. Check line limits (error if >200 lines, warning if >150 lines)
2. Detect secrets using 15+ regex patterns (API keys, tokens, passwords, private keys, connection strings)
3. Validate markdown structure (must start with title, include "AGENTS" in title)
4. Check for recommended sections (Quick Start, Architecture, Conventions, Security, DO NOT)
5. Return ValidationResult with valid flag, errors, warnings, line count, sections found

**Tier-Specific Requirements**:
| Tier | Line Limit | Secret Patterns | Structure Check | Section Check |
|------|------------|-----------------|-----------------|---------------|
| LITE | 200 (max) | ❌ | Basic (title only) | ❌ |
| STANDARD | 150 (warn), 200 (max) | ✅ (10 patterns) | ✅ (title + markdown) | ⚠️ (recommended) |
| PROFESSIONAL | 150 (warn), 200 (max) | ✅ (15 patterns) | ✅ (full structure) | ✅ (required) |
| ENTERPRISE | 150 (max, strict) | ✅ (20+ patterns + custom) | ✅ (full structure) | ✅ (required) |

**Secret Detection Patterns** (15+ patterns):
- OpenAI: `sk-[a-zA-Z0-9]{20,}`
- GitHub PAT: `ghp_[a-zA-Z0-9]{36}`
- AWS Access Key: `AKIA[A-Z0-9]{16}`
- Stripe Live Key: `sk_live_[a-zA-Z0-9]{24,}`
- Anthropic API Key: `sk-ant-api[a-zA-Z0-9-]{20,}`
- JWT Token: `eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.`
- Private Keys: `-----BEGIN.*PRIVATE KEY-----`
- Connection Strings: `://[^:]+:[^@]{8,}@` (user:password@host)

**Acceptance Criteria**:
| Criteria | Pass Condition |
|----------|----------------|
| **Validation Speed** | <500ms for p95 (API response time) |
| **False Positive Rate** | <5% (secrets in comments/examples allowed) |
| **Coverage** | 100% of OpenAI, GitHub, AWS, Stripe, Anthropic keys detected |
| **Structure Accuracy** | 100% detection of missing title or AGENTS keyword |
| **Section Detection** | 95%+ accuracy for finding ## headings |

---

### FR-003: Context Overlay Generation and Delivery

**GIVEN** a project with current SDLC stage, active sprint, and constraints
**WHEN** PR is created/updated, CLI requests context, or API calls `GET /api/v1/projects/{id}/context-overlay`
**THEN** the system MUST:
1. Retrieve current SDLC stage and gate status from GateService
2. Retrieve active sprint context (number, goal, velocity, days remaining) from SprintService
3. Identify active constraints:
   - Strict mode (post-G3: only bug fixes allowed)
   - Security issues (active CVEs, vulnerabilities)
   - AGPL containment (if project uses MinIO/Grafana)
   - Active incidents (P0/P1 production issues)
4. Build ContextOverlay object with all data
5. Format for delivery channel (PR comment, CLI output, Check Run, JSON API)
6. Save overlay to `context_overlays` table for audit
7. Deliver via specified channel (PR comment, CLI print, API response)

**Tier-Specific Requirements**:
| Tier | Stage/Gate | Sprint Context | Constraints | Strict Mode | Audit Trail |
|------|------------|----------------|-------------|-------------|-------------|
| LITE | ❌ | ❌ | Basic (AGPL only) | ❌ | ❌ |
| STANDARD | ✅ (stage only) | ⚠️ (number + goal) | ✅ (AGPL + security) | ❌ | ⚠️ (90 days) |
| PROFESSIONAL | ✅ (stage + gate) | ✅ (full context) | ✅ (all constraints) | ✅ | ✅ (1 year) |
| ENTERPRISE | ✅ (stage + gate) | ✅ (full context) | ✅ (all + custom) | ✅ | ✅ (Permanent) |

**Acceptance Criteria**:
| Criteria | Pass Condition |
|----------|----------------|
| **Overlay Generation Speed** | <500ms for p95 (API response time) |
| **PR Comment Latency** | <3s from PR open to comment posted |
| **Data Freshness** | Stage/sprint data <5min old (cached) |
| **Constraint Accuracy** | 100% detection of G3 pass, active CVEs, AGPL deps |
| **Delivery Success Rate** | >99.5% (PR comments posted successfully) |

---

### FR-004: CLI Commands for AGENTS.md Management

**GIVEN** user has sdlcctl CLI installed
**WHEN** user runs CLI commands `sdlcctl agents init/validate/lint`
**THEN** the system MUST provide:

**`sdlcctl agents init`**:
- Analyze project at specified path
- Display project analysis summary (Rich Table)
- Generate AGENTS.md with configurable options (--max-lines, --force, --dry-run)
- Validate for secrets before writing
- Write AGENTS.md to project root or specified output path
- Display success message with file path and line count

**`sdlcctl agents validate`**:
- Read AGENTS.md from specified path
- Run full validation (secrets, structure, line limits, sections)
- Display results with color-coded output (errors in red, warnings in yellow)
- Exit with code 1 if errors found (or warnings in --strict mode)
- Exit with code 0 if validation passes

**`sdlcctl agents lint`**:
- Read AGENTS.md from specified path
- Detect linting issues (trailing whitespace, multiple blank lines, missing newline at end)
- Display issues found
- Apply fixes if --fix flag provided
- Write fixed content back to file
- Display count of fixes applied

**Tier-Specific Requirements**:
| Tier | Commands | Rich Output | Secret Detection | Auto-Fix | Project Analysis |
|------|----------|-------------|------------------|----------|------------------|
| LITE | init, validate | ❌ (plain text) | ❌ | ❌ | Basic |
| STANDARD | init, validate, lint | ✅ (Rich tables) | ✅ | ⚠️ (whitespace only) | Standard |
| PROFESSIONAL | init, validate, lint | ✅ (Rich + panels) | ✅ | ✅ (all fixes) | Full |
| ENTERPRISE | init, validate, lint | ✅ (Rich + progress) | ✅ | ✅ (all + custom) | Full + custom rules |

**Acceptance Criteria**:
| Criteria | Pass Condition |
|----------|----------------|
| **CLI Speed** | `init` <3s, `validate` <1s, `lint` <1s (end-to-end) |
| **Rich Output** | Tables, panels, colors render correctly in terminal |
| **Help Text** | `--help` displays usage, options, examples for all commands |
| **Error Handling** | Graceful errors with exit codes (1 for errors, 0 for success) |
| **Cross-Platform** | Works on Linux, macOS, Windows (PowerShell + CMD) |

---

### FR-005: GitHub PR Webhook Integration for Overlay Injection

**GIVEN** GitHub repository with webhook configured
**WHEN** PR is opened or updated
**THEN** the system MUST:
1. Receive webhook at `POST /api/v1/webhooks/github`
2. Extract project_id, pr_number, repo_owner, repo_name from payload
3. Generate context overlay for project
4. Format overlay as PR comment (markdown with HTML comment markers)
5. Post comment to PR using GitHub API
6. Update `context_overlays` table with pr_comment_id for tracking
7. Handle PR updates by editing existing comment (not creating new comment)

**Tier-Specific Requirements**:
| Tier | PR Comment | Auto-Update | Constraint Detail | Strict Mode Banner | Audit Trail |
|------|------------|-------------|-------------------|--------------------|-------------|
| LITE | ❌ | ❌ | ❌ | ❌ | ❌ |
| STANDARD | ✅ (basic) | ❌ | ⚠️ (type + message only) | ❌ | ⚠️ (90 days) |
| PROFESSIONAL | ✅ (full) | ✅ | ✅ (type + message + files) | ✅ | ✅ (1 year) |
| ENTERPRISE | ✅ (full + custom) | ✅ | ✅ (full + custom rules) | ✅ | ✅ (Permanent) |

**PR Comment Format** (markdown):
```markdown
<!-- SDLC-CONTEXT-START -->
## 🎯 SDLC Context (Feb 03, 2026 10:00 UTC)

> 🔒 **STRICT MODE ACTIVE**: Only bug fixes allowed.

| Stage | Gate | Sprint |
|-------|------|--------|
| Stage 04 (BUILD) | G3 PASSED | Sprint 80 - AGENTS.md Generator (8 days left) |

### Active Constraints
- ⚠️ **Strict Mode**: Post-G3: Only bug fixes allowed.
- 🔴 **Security Review**: CVE-2026-1234 detected in auth_service.py
  - `backend/app/services/auth_service.py`
- ℹ️ **AGPL**: MinIO/Grafana network-only access (no SDK imports)

---
*Generated by [SDLC Orchestrator](https://sdlc.dev) • [View Dashboard](#)*
<!-- SDLC-CONTEXT-END -->
```

**Acceptance Criteria**:
| Criteria | Pass Condition |
|----------|----------------|
| **Webhook Latency** | <3s from PR open to comment posted |
| **Comment Update** | Existing comment edited, not new comment created |
| **Error Handling** | Graceful degradation if GitHub API fails (logged, not blocking) |
| **Rate Limiting** | Respects GitHub API rate limits (5000 req/hour) |
| **HTML Marker Parsing** | AI tools can parse `<!-- SDLC-CONTEXT-START -->` markers |

---

## 3. Database Schema

### 3.1 New Tables

**Table: `agents_md_files`** - Stores generated AGENTS.md history per project

```sql
CREATE TABLE agents_md_files (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,

    -- Content
    content TEXT NOT NULL,
    content_hash VARCHAR(64) NOT NULL,  -- SHA256
    line_count INTEGER NOT NULL,
    sections JSONB NOT NULL,  -- ["Quick Start", "Architecture", ...]

    -- Generation metadata
    generated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    generated_by UUID REFERENCES users(id),
    generator_version VARCHAR(20) NOT NULL,  -- "1.0.0"
    source_analysis JSONB,  -- Files analyzed, configs found

    -- Validation
    validation_status VARCHAR(20) NOT NULL DEFAULT 'pending',
    validation_errors JSONB,
    validation_warnings JSONB,

    -- Audit
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Constraints
    CONSTRAINT chk_line_count CHECK (line_count > 0 AND line_count <= 200),
    CONSTRAINT chk_validation_status CHECK (validation_status IN ('pending', 'valid', 'invalid'))
);

CREATE INDEX idx_agents_md_files_project_id ON agents_md_files(project_id);
CREATE INDEX idx_agents_md_files_generated_at ON agents_md_files(generated_at DESC);
CREATE INDEX idx_agents_md_files_content_hash ON agents_md_files(content_hash);

-- Latest file per project view
CREATE VIEW v_latest_agents_md AS
SELECT DISTINCT ON (project_id)
    id, project_id, content, content_hash, line_count, sections,
    generated_at, generator_version, validation_status
FROM agents_md_files
ORDER BY project_id, generated_at DESC;
```

**Table: `context_overlays`** - Stores generated context overlays for audit

```sql
CREATE TABLE context_overlays (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,

    -- Context data
    stage_name VARCHAR(50),
    gate_status VARCHAR(50),
    sprint_id UUID REFERENCES sprints(id),
    sprint_number INTEGER,
    sprint_goal TEXT,

    -- Constraints (stored as JSONB array)
    constraints JSONB NOT NULL DEFAULT '[]',
    -- Example: [{"type": "strict_mode", "severity": "warning", "message": "..."}]

    -- Flags
    strict_mode BOOLEAN NOT NULL DEFAULT FALSE,

    -- Delivery tracking
    generated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    trigger_type VARCHAR(30) NOT NULL,  -- pr_webhook, cli, api, scheduled
    trigger_ref VARCHAR(255),  -- PR number, CLI session, etc

    -- Delivery channels used
    delivered_to_pr BOOLEAN DEFAULT FALSE,
    delivered_to_check_run BOOLEAN DEFAULT FALSE,
    pr_comment_id BIGINT,  -- GitHub comment ID if delivered
    check_run_id BIGINT,   -- GitHub check run ID if delivered

    -- Audit
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    -- Constraints
    CONSTRAINT chk_trigger_type CHECK (trigger_type IN ('pr_webhook', 'cli', 'api', 'scheduled', 'manual'))
);

CREATE INDEX idx_context_overlays_project_id ON context_overlays(project_id);
CREATE INDEX idx_context_overlays_generated_at ON context_overlays(generated_at DESC);
CREATE INDEX idx_context_overlays_trigger ON context_overlays(trigger_type, trigger_ref);
CREATE INDEX idx_context_overlays_pr ON context_overlays(pr_comment_id) WHERE pr_comment_id IS NOT NULL;
```

### 3.2 Entity Relationship

```
projects (1) ──┬── (N) agents_md_files
               │
               └── (N) context_overlays
                        │
                        └── (N) sprints (FK: sprint_id)
```

---

## 4. API Endpoints

### 4.1 Endpoint Specifications

**POST /api/v1/projects/{project_id}/agents-md/generate**
- **Summary**: Generate AGENTS.md from project configuration
- **Tags**: [AGENTS.md]
- **Request Body**: `AgentsMdConfig` (optional)
  ```json
  {
    "include_quick_start": true,
    "include_architecture": true,
    "include_conventions": true,
    "include_security": true,
    "include_git_workflow": true,
    "include_do_not": true,
    "max_lines": 150
  }
  ```
- **Response 200**: `AgentsMdFile`
  ```json
  {
    "id": "uuid",
    "content": "# AGENTS.md - Project Name\n...",
    "content_hash": "sha256",
    "line_count": 142,
    "sections": ["Quick Start", "Architecture", ...],
    "generated_at": "2026-02-03T10:00:00Z",
    "validation_status": "valid"
  }
  ```
- **Errors**: 400 (Invalid config), 404 (Project not found)

**POST /api/v1/agents-md/validate**
- **Summary**: Validate AGENTS.md content
- **Tags**: [AGENTS.md]
- **Request Body**:
  ```json
  {
    "content": "# AGENTS.md\n..."
  }
  ```
- **Response 200**: `ValidationResult`
  ```json
  {
    "valid": false,
    "errors": [{"severity": "error", "message": "Secret detected", "line_number": 4}],
    "warnings": [{"severity": "warning", "message": "Missing section: Security"}],
    "line_count": 45,
    "sections_found": ["Quick Start"]
  }
  ```

**GET /api/v1/projects/{project_id}/context-overlay**
- **Summary**: Get current context overlay for project
- **Tags**: [Context]
- **Response 200**: `ContextOverlay`
  ```json
  {
    "project_id": "uuid",
    "generated_at": "2026-02-03T10:00:00Z",
    "stage_name": "Stage 04 (BUILD)",
    "gate_status": "G3 PASSED",
    "sprint": {
      "id": "uuid",
      "number": 80,
      "goal": "AGENTS.md Generator",
      "velocity": 32,
      "days_remaining": 8
    },
    "constraints": [
      {"type": "strict_mode", "severity": "warning", "message": "Post-G3: Only bug fixes"},
      {"type": "agpl", "severity": "info", "message": "MinIO/Grafana network-only"}
    ],
    "strict_mode": true
  }
  ```

**GET /api/v1/projects/{project_id}/context-overlay/pr-comment**
- **Summary**: Get context overlay formatted as PR comment
- **Tags**: [Context]
- **Response 200**:
  ```json
  {
    "comment": "<!-- SDLC-CONTEXT-START -->..."
  }
  ```

---

## 5. Architecture Design

### 5.1 Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                       SDLC Orchestrator                             │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │                     API Layer                              │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐     │   │
│  │  │ /agents-md│  │ /context │  │ CLI: sdlc agents    │     │   │
│  │  │ generate  │  │ overlay  │  │ init|validate|lint  │     │   │
│  │  └─────┬────┘  └─────┬────┘  └──────────┬──────────┘     │   │
│  └────────│──────────────│───────────────────│────────────────┘   │
│           │              │                   │                    │
│  ┌────────▼──────────────▼───────────────────▼────────────────┐   │
│  │                  Service Layer                             │   │
│  │  ┌────────────────┐  ┌────────────────┐  ┌──────────────┐  │   │
│  │  │ AgentsMdService│  │ ContextOverlay │  │ AgentsMd     │  │   │
│  │  │                │  │ Service        │  │ Validator    │  │   │
│  │  │ • generate()   │  │ • get_overlay()│  │ • validate() │  │   │
│  │  │ • _sections()  │  │ • format_*()   │  │ • lint()     │  │   │
│  │  └────────┬───────┘  └────────┬───────┘  └──────┬───────┘  │   │
│  └───────────│──────────────────│──────────────────│──────────┘   │
│              │                  │                  │              │
│  ┌───────────▼──────────────────▼──────────────────▼──────────┐   │
│  │                  Data Access Layer                         │   │
│  │  ┌────────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐  │   │
│  │  │FileAnalyzer│  │GateService│  │Sprint   │  │Security │  │   │
│  │  └────────────┘  └──────────┘  └──────────┘  └─────────┘  │   │
│  │  ┌────────────┐  ┌──────────────────────────────────────┐  │   │
│  │  │AgentsMdRepo│  │ContextOverlayRepo                    │  │   │
│  │  │(PostgreSQL)│  │(PostgreSQL)                          │  │   │
│  │  └────────────┘  └──────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘

External Integrations:
┌──────────┐   ┌──────────┐   ┌──────────────┐
│GitHub API│   │Project   │   │AI Coding     │
│(PR       │   │Repo      │   │Tools         │
│comments) │   │(file read│   │(consume      │
└──────────┘   └──────────┘   └──────────────┘
```

### 5.2 Data Flow

**AGENTS.md Generation Flow**:
```
1. User: sdlc agents init
        ↓
2. CLI → POST /api/v1/projects/{id}/agents-md/generate
        ↓
3. AgentsMdService.generate():
        ├── FileAnalyzer.analyze_project_structure()
        │     ├── Check docker-compose.yml
        │     ├── Check package.json/requirements.txt
        │     ├── Check tsconfig.json/pyproject.toml
        │     └── Check .github/workflows/
        ├── Generate sections (Quick Start, Architecture, Conventions, Security, Git Workflow, DO NOT)
        ├── Combine sections (enforce ≤150 lines)
        └── AgentsMdValidator.validate() → Check structure/secrets
        ↓
4. Return AgentsMdFile → CLI writes AGENTS.md
        ↓
5. User commits: git add AGENTS.md && git commit
```

**Context Overlay Flow**:
```
1. PR created/updated → Webhook → POST /api/v1/webhooks/github
        ↓
2. ContextOverlayService.get_overlay(project_id):
        ├── GateService.get_current_stage() → SDLC stage
        ├── GateService.get_latest_gate_status() → G0.1, G3, etc
        ├── SprintService.get_active_sprint() → Sprint context
        ├── SecurityService.get_active_issues() → Constraints
        └── Build ContextOverlay object
        ↓
3. ContextOverlayService.format_pr_comment(overlay)
        ↓
4. GitHubService.post_pr_comment(pr_number, comment)
        ↓
5. AI tools (Cursor, Copilot) see comment in PR context
```

---

## 6. Performance Targets

| Operation | Target (p95) | Measurement |
|-----------|--------------|-------------|
| **Generate AGENTS.md** | <2s | API response time |
| **Validate AGENTS.md** | <500ms | API response time |
| **Get Context Overlay** | <500ms | API response time |
| **PR Comment Latency** | <3s | Webhook → comment posted |
| **CLI `init`** | <3s | End-to-end (analysis → file write) |
| **CLI `validate`** | <1s | End-to-end (file read → validation) |
| **CLI `lint`** | <1s | End-to-end (file read → fixes → write) |

**Optimization Strategies**:
1. **Caching**: Cache project analysis for 5 minutes
2. **Parallel section generation**: Generate sections concurrently
3. **Lazy loading**: Only load sections enabled in config
4. **Database indexes**: Optimized for project_id lookups

---

## 7. Security Considerations

### 7.1 Secret Detection

The validator includes patterns for detecting common secrets:

| Pattern Type | Examples | Regex |
|-------------|----------|-------|
| **API Keys** | `api_key = "sk-..."`, `API_KEY: "..."` | `(?i)api[_-]?key\s*[=:]\s*["\'][^"\']{8,}["\']` |
| **OpenAI** | `sk-abc123...` | `sk-[a-zA-Z0-9]{20,}` |
| **GitHub PAT** | `ghp_...`, `gho_...` | `gh[po]_[a-zA-Z0-9]{36}` |
| **AWS** | `AKIA...`, `aws_secret_access_key` | `AKIA[A-Z0-9]{16}` |
| **Stripe** | `sk_live_...` | `sk_live_[a-zA-Z0-9]{24,}` |
| **Anthropic** | `sk-ant-api...` | `sk-ant-api[a-zA-Z0-9-]{20,}` |
| **Private Keys** | `-----BEGIN PRIVATE KEY-----` | `-----BEGIN.*PRIVATE KEY-----` |
| **Connection Strings** | `://user:password@host` | `(?i)://[^:]+:[^@]{8,}@` |
| **JWT Tokens** | `eyJ...` | `eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.` |

### 7.2 Input Validation

- **project_id**: Must be valid UUID
- **content**: Max 500KB to prevent abuse
- **max_lines**: Range 50-200
- **config options**: Boolean only

### 7.3 AGPL Containment

System ensures AGPL containment is included in DO NOT section when MinIO/Grafana detected:
- `- Import AGPL libraries (MinIO SDK, Grafana SDK)`
- `- AGPL: MinIO/Grafana network-only (NO SDK imports)`

---

## 8. Testing Requirements

### 8.1 Unit Tests (95%+ coverage)

**Test Coverage**:
- AgentsMdService: Generation, section creation, line limit enforcement
- AgentsMdValidator: Secret detection (15+ patterns), structure validation, line limits
- ContextOverlayService: Overlay generation, formatting (PR comment, CLI, JSON)
- FileAnalyzer: Project structure detection (docker-compose, package.json, etc)

### 8.2 Integration Tests (90%+ coverage)

**Test Scenarios**:
- API: Generate AGENTS.md → Validate → Success
- API: Validate with secrets → Errors returned
- API: Get context overlay → Sprint + constraints included
- CLI: `init` → File created with correct content
- CLI: `validate` → Errors/warnings displayed
- CLI: `lint --fix` → Whitespace/structure fixed

### 8.3 E2E Tests (critical user journeys)

**Test Flows**:
- Full workflow: `sdlc agents init` → File created → `sdlc agents validate` → PASS
- PR flow: PR opened → Webhook received → Context overlay comment posted → AI tools see comment
- Strict mode: G3 passed → Overlay shows strict mode banner → Feature PR blocked

---

## 9. Deployment & Rollout

### 9.1 Feature Flags

```python
AGENTS_MD_ENABLED = os.getenv("AGENTS_MD_ENABLED", "true") == "true"
CONTEXT_OVERLAY_ENABLED = os.getenv("CONTEXT_OVERLAY_ENABLED", "true") == "true"
AUTO_PR_COMMENT_ENABLED = os.getenv("AUTO_PR_COMMENT_ENABLED", "false") == "true"
```

### 9.2 Rollout Plan

| Phase | Scope | Duration |
|-------|-------|----------|
| **Phase 1** | Internal testing (BFlow, NQH) | 1 week |
| **Phase 2** | CLI only (no auto-comments) | 1 week |
| **Phase 3** | Full rollout (with PR comments) | Sprint 81 |

### 9.3 Monitoring

```yaml
Metrics:
  - agents_md_generations_total (counter)
  - agents_md_validations_total (counter)
  - agents_md_validation_errors_total (counter)
  - context_overlay_requests_total (counter)
  - agents_md_generation_duration_seconds (histogram)

Alerts:
  - agents_md_validation_error_rate > 10%
  - agents_md_generation_duration_p95 > 5s
```

---

## 10. Dependencies

### 10.1 Sprint 79 Dependencies (RESOLVED)

| Dependency | Status | Notes |
|------------|--------|-------|
| Evidence Ed25519 signing | ✅ Complete | `evidence_manifest_service.py` |
| GitHub Check Run service | ✅ Complete | `github_checks_service.py` |
| Over-claims fixes | ✅ Complete | Expert docs updated |

### 10.2 External Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| pydantic | 2.0+ | Data validation |
| typer | 0.9+ | CLI framework |
| rich | 13.0+ | CLI rich output |
| httpx | 0.25+ | GitHub API calls |

---

## 11. References

### 11.1 ADR References

- **ADR-029**: AGENTS.md Integration - Static + Dynamic Layers (approved)
- **ADR-007**: AI Context Engine - Ollama Integration
- **ADR-014**: SDLC Structure Validator CLI

### 11.2 Related Specifications

- **SPEC-0003**: AI Context Engine (ADR-007) - Provides AI model for context generation
- **SPEC-0004**: Policy Guards Design - Provides constraint data for overlays
- **SPEC-0009**: FileAnalyzer Service - Provides project structure analysis

### 11.3 Expert Feedback Documents

- Expert feedback on AGENTS.md 150-line limit (Jan 2026)
- Expert feedback on Static + Dynamic separation (Jan 2026)
- Expert feedback on Secret detection patterns (Jan 2026)

---

## 12. Example Artifacts

### 12.1 Example Generated AGENTS.md

```markdown
# AGENTS.md - SDLC Orchestrator

## Quick Start
- Full stack: `docker compose up -d`
- Backend only: `cd backend && pytest`
- Frontend only: `cd frontend/web && npm run dev`

## Architecture
- Infrastructure: Docker Compose
- Backend: Python (FastAPI)
- Frontend: React (TypeScript)
- Database: PostgreSQL
See `/docs/02-design/` for detailed architecture documentation.

## Current Stage
Check project dashboard for current SDLC stage and gate status.
Dynamic context is delivered via PR comments (not in this file).

## Conventions
- Python: ruff + mypy strict mode
- TypeScript: strict mode enabled
- Files: snake_case (Python ≤50 chars), camelCase/PascalCase (TypeScript)
- Tests: 95%+ coverage required

## Security
- OWASP ASVS L2 compliance required
- No hardcoded secrets (use environment variables)
- Input validation on all API endpoints
- SQL injection prevention via ORM
- AGPL: MinIO/Grafana network-only (NO SDK imports)

## Git Workflow
- Branch: `feature/{ticket}-{description}`
- Commit: `feat|fix|chore(scope): message`
- PR: Must pass quality gates before merge

## DO NOT
- Add mocks or placeholders (Zero Mock Policy)
- Skip tests for 'quick fixes'
- Hardcode secrets or credentials
- Use `// TODO` without ticket reference
- Import AGPL libraries (MinIO SDK, Grafana SDK)
```

### 12.2 Example Context Overlay PR Comment

```markdown
<!-- SDLC-CONTEXT-START -->
## 🎯 SDLC Context (Feb 03, 2026 10:00 UTC)

> 🔒 **STRICT MODE ACTIVE**: Only bug fixes allowed.

| Stage | Gate | Sprint |
|-------|------|--------|
| Stage 04 (BUILD) | G3 PASSED | Sprint 80 - AGENTS.md Generator (8 days left) |

### Active Constraints
- ⚠️ **Strict Mode**: Post-G3: Only bug fixes allowed.
- 🔴 **Security Review**: CVE-2026-1234 detected in auth_service.py
  - `backend/app/services/auth_service.py`
- ℹ️ **AGPL**: MinIO/Grafana network-only access (no SDK imports)

---
*Generated by [SDLC Orchestrator](https://sdlc.dev) • [View Dashboard](#)*
<!-- SDLC-CONTEXT-END -->
```

---

## 13. Approvals

| Role | Name | Status | Date |
|------|------|--------|------|
| **Author** | Backend Lead | ✅ Complete | Jan 19, 2026 |
| **Tech Lead** | Tech Lead | ✅ Approved | Jan 20, 2026 |
| **CTO** | CTO | ✅ Approved | Jan 21, 2026 |

---

**SDLC 6.0.0 Framework | Sprint 80 | Stage 02 (DESIGN)**

*Specification ID: SPEC-0007 | Version 1.0.0*
*Framework Version: 6.0.0 (In Development)*
