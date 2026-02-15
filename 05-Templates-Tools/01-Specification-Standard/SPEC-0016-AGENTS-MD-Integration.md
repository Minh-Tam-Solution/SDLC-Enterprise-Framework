# SPEC-0016: AGENTS.md Integration Specification

## Frontmatter

```yaml
spec_id: SPEC-0016
title: AGENTS.md Integration - Static + Dynamic AI Context Governance
version: 2.0.0
status: approved
tier: PROFESSIONAL
pillar: Pillar 4 - Build & Implementation
owner: Backend Lead + CTO
last_updated: 2026-01-29
tags:
  - agents-md
  - integration
  - ai-context
  - governance
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
  - SPEC-0007  # AGENTS.md Technical Design
epic: EP-07 AGENTS.md Framework
sprint: Sprint 80
implementation_ref: "SDLC-Orchestrator/docs/02-design/14-Technical-Specs/AGENTS-MD-Integration-Specification.md"
```

---

## Executive Summary

This specification defines the **governance requirements** for integrating the industry-standard AGENTS.md format with dynamic runtime overlays to guide AI coding assistants while maintaining clean git history.

**Key Governance Principles**:
- Static AGENTS.md file committed to repository (stable, rarely updated)
- Dynamic overlay delivered at runtime (context-aware, frequently updated)
- SASE artifact migration path (deprecate MTS/BRS/LPS, keep CRP/MRP/VCR)
- Security validation to prevent sensitive information exposure

**Business Value**:
- Industry standard alignment (60K+ projects using AGENTS.md)
- Zero noise commits from dynamic context updates
- AI tool compatibility (works with all major AI coding assistants)
- Governance context without polluting repository history

> **Implementation Reference**: For technical implementation details (services, APIs, CLI commands), see SDLC-Orchestrator documentation.

---

## 1. Static AGENTS.md Structure

### Overview

The static AGENTS.md file provides foundational context that changes rarely and is committed to the repository root.

### Required Sections

| Section | Purpose | Content Type |
|---------|---------|--------------|
| **Quick Start** | Setup commands for developers | Environment setup, dependencies |
| **Architecture** | System overview for AI context | Layer diagram, key patterns |
| **Conventions** | Coding standards | Naming, style, test patterns |
| **Security** | Security requirements | Authentication, authorization, boundaries |
| **Git Workflow** | Repository practices | Branch naming, commit format, PR rules |
| **DO NOT** | Forbidden patterns | Anti-patterns, security violations |

### File Constraints

| Constraint | Value | Rationale |
|------------|-------|-----------|
| Location | Repository root | Industry standard, tool discovery |
| Maximum length | 150 lines | Brevity for AI token efficiency |
| Maximum size | 50KB | Prevent abuse, ensure fast parsing |
| Update frequency | Rarely | Only for architecture changes, new conventions |
| Format | Markdown only | No executable code blocks |

---

## 2. Functional Requirements

### FR-001: Generator Service

**Description**: System generates AGENTS.md from project analysis.

**Requirement**:

```gherkin
GIVEN a project needs AI code governance
WHEN the generator service is invoked
THEN the system SHALL:
  - Analyze project configuration files (package manifests, docker configs)
  - Extract setup commands for "Quick Start" section
  - Summarize design documentation for "Architecture" section
  - Parse linting/editor configs for "Conventions" section
  - Load security baseline for "Security" section
  - Generate forbidden patterns for "DO NOT" section
  - Output file meeting length constraints
AND the system SHALL validate:
  - File length within limits (truncate with warning if exceeded)
  - No secrets in generated content (block if found)
  - No internal URLs (redact automatically)
```

---

### FR-002: Static File Management

**Description**: System manages committed AGENTS.md file.

**Requirement**:

```gherkin
GIVEN a project has generated AGENTS.md
WHEN the file is committed to the repository
THEN the system SHALL enforce:
  - Location: Repository root directory
  - Content: Markdown only (no executable code)
  - Validation: Secrets detection, size limits
  - Tracking: Last updated timestamp, update reason
AND the system SHALL validate commits:
  - Check file size within limits
  - Scan for secrets (block if detected)
  - Scan for internal URLs (warn developer)
  - Require signed commit (ENTERPRISE tier only)
```

---

### FR-003: Dynamic Overlay - Version Control Integration

**Description**: Dynamic context delivered through version control check mechanisms.

**Requirement**:

```gherkin
GIVEN a code change is submitted for review
WHEN governance checks run
THEN the system SHALL post dynamic overlay containing:
  - Current SDLC Stage + Gate Status
  - Sprint Context (goal, velocity, remaining capacity)
  - Active Constraints (strict mode, security review, risky files)
  - Incident Constraints (detected issues requiring fixes)
  - Auto-Generation Status (from Anti-Vibecoding)
AND the overlay SHALL:
  - Update on every code change
  - Include Vibecoding Index score with routing recommendation
  - Link to relevant documentation
  - Show time since last gate pass
  - Auto-expire constraints after resolution
```

---

### FR-004: Dynamic Overlay - Code Review Comments

**Description**: Structured comments provide context during code review.

**Requirement**:

```gherkin
GIVEN a code change request is created or updated
WHEN constraints change (gate pass, incident detected)
THEN the system SHALL post structured comment:
  - Machine-readable markers for tool parsing
  - Current stage and gate status
  - Active constraints with severity
  - Sprint context with progress
  - Timestamp for staleness detection
AND the system SHALL:
  - Update existing comment (not create new comments)
  - Support collapse/expand for long constraint lists
  - Link to detailed explanations
  - Handle user deletion (recreate with warning)
```

---

### FR-005: Dynamic Overlay - Developer Tooling

**Description**: Local developer tools receive governance context.

**Requirement**:

```gherkin
GIVEN a developer works locally
WHEN developer requests context
THEN the system SHALL:
  - Fetch current project context from governance platform
  - Display formatted context in terminal/IDE
  - Save context locally (ignored by version control)
  - Support filtering by stage, sprint, or constraints
AND the context SHALL include:
  - Stage and sprint information
  - Gate status with pass/fail indicator
  - Vibecoding Index score
  - Active constraints with severity
  - Sprint velocity metrics
```

---

### FR-006: Dynamic Overlay - IDE Extension

**Description**: IDE extensions provide real-time governance context.

**Requirement**:

```gherkin
GIVEN a developer uses IDE with governance extension
WHEN developer opens a project
THEN the extension SHALL:
  - Fetch context from governance platform
  - Display context in sidebar panel
  - Inject context into AI chat (invisible to user)
  - Update context periodically (real-time)
  - Show notification on constraint changes
AND the extension SHALL:
  - Cache context locally (reduce API calls)
  - Work offline (show last known context)
  - Support multi-project workspaces
```

---

### FR-007: SASE Artifact Migration

**Description**: Migration path from legacy SASE artifacts to AGENTS.md.

**Requirement**:

```gherkin
GIVEN SASE artifacts (MTS/BRS/LPS) are deprecated
WHEN migrating projects to AGENTS.md
THEN the system SHALL:

Deprecation plan:
  - MentorScript (MTS) → AGENTS.md "Conventions" section
  - BriefingScript (BRS) → Issue templates + AGENTS.md "Architecture"
  - LoopScript (LPS) → Removed (AI tools plan own work)

Retention:
  - CRP (Consultation Request Protocol) → KEEP
  - MRP (Merge Readiness Protocol) → KEEP
  - VCR (Verification Report) → KEEP

AND the system SHALL:
  - Detect legacy artifacts (scan for deprecated files)
  - Warn users to migrate (dashboard notification)
  - Provide migration tooling
  - Archive old files (preserve history)
  - Support hybrid mode (AGENTS.md + CRP/MRP/VCR coexist)
```

---

### FR-008: Security Validation

**Description**: Security policies protect sensitive information.

**Requirement**:

```gherkin
GIVEN AGENTS.md may contain sensitive information
WHEN AGENTS.md is generated or committed
THEN the system SHALL enforce:

1. Secrets Detection:
   - Scan for API keys, passwords, credentials
   - Scan for internal URLs and infrastructure details
   - Block commit if secrets detected
   - Notify security team (ENTERPRISE tier)

2. Content Validation:
   - File size within limits
   - No executable code blocks
   - No private infrastructure details
   - Auto-redact sensitive data if found

3. Source Validation (ENTERPRISE):
   - Load from default branch only
   - Require signed commits
   - Verify CI status before merge
```

---

## 3. Tier-Specific Requirements

| Feature | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---------|------|----------|--------------|------------|
| **AGENTS.md Generator** | Manual creation | Basic generator | Full generator | Full + custom templates |
| **Dynamic Overlay - VCS Check** | Not available | Basic context | Full context | Full + historical trends |
| **Dynamic Overlay - Comments** | Not available | Manual only | Automated | Automated + rich formatting |
| **Dynamic Overlay - CLI** | Not available | Basic output | Full + export | Full + filtering + export |
| **Dynamic Overlay - IDE** | Not available | Not available | Read-only panel | Full panel + chat injection |
| **SASE Migration** | Not available | Automated | Automated + validation | Automated + custom rules |
| **Security Validation** | Not available | Basic secrets | Full validation | Full + signed commits |
| **Update Frequency** | Manual | Per commit | Per commit | Real-time refresh |

---

## 4. Architecture Design

### Static + Dynamic Overlay Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                    STATIC + DYNAMIC OVERLAY MODEL                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LAYER A: STATIC AGENTS.md (Committed to repository)                │
│  ─────────────────────────────────────────────────                  │
│  Location: Repository root                                          │
│  Update: Rarely (architecture changes, new conventions)             │
│  Contents:                                                          │
│    • Quick Start (environment setup)                                │
│    • Architecture (system overview, key patterns)                   │
│    • Conventions (coding standards, naming, tests)                  │
│    • Security (authentication, authorization, boundaries)           │
│    • Git Workflow (branch naming, commit format)                    │
│    • DO NOT (forbidden patterns, anti-patterns)                     │
│  Compatibility: All major AI coding assistants                      │
│                                                                     │
│  LAYER B: DYNAMIC OVERLAY (Runtime - NOT committed)                 │
│  ──────────────────────────────────────────────────                 │
│  Update: Per gate pass, per incident, per code change               │
│  Contents:                                                          │
│    • Current SDLC stage + gate status                               │
│    • Sprint context (goal, velocity, blockers)                      │
│    • Active constraints (strict mode, security review)              │
│    • Incident constraints (detected issues)                         │
│    • Known risky files (under review)                               │
│                                                                     │
│  Delivery Channels:                                                 │
│    ├─ Version Control Check (universal, all tools)                  │
│    ├─ Code Review Comment (visible in review tools)                 │
│    ├─ Developer CLI (local context file, ignored by VCS)            │
│    └─ IDE Extension (sidebar panel, chat injection)                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Generator Service Concept

```
Input Sources                 Generator Service              Output
─────────────                 ─────────────────              ──────
Package manifests      ──→    Quick Start Analyzer     ──→   Quick Start section
Docker/container config

Design documentation   ──→    Architecture Summarizer  ──→   Architecture section
System diagrams

Linting/editor config  ──→    Convention Extractor     ──→   Conventions section
Style guides

Security baseline      ──→    Security Rules Gen       ──→   Security section
OWASP/compliance

VCS workflow config    ──→    Workflow Analyzer        ──→   Git Workflow section

Security policies      ──→    Anti-Pattern Generator   ──→   DO NOT section
Known anti-patterns

                              ↓
                         Validation Pipeline
                         (length, secrets, URLs)
                              ↓
                         AGENTS.md output
```

---

## 5. Non-Functional Requirements

### NFR-001: Performance Targets

| Operation | Target | Notes |
|-----------|--------|-------|
| Generator execution | <10s | File analysis and generation |
| VCS check posting | <5s | Real-time context delivery |
| Comment posting | <10s | Code review context |
| CLI context fetch | <2s | Local developer experience |
| IDE refresh | <3s | Real-time updates |
| Secrets detection | <1s | Per-file analysis |

### NFR-002: Security Requirements

| Requirement | Description |
|-------------|-------------|
| Secrets detection | Block commits with credentials |
| Size limits | Enforce maximum file size |
| Signed commits | Require signatures (ENTERPRISE) |
| Source validation | Load from default branch only |
| Audit trail | Log all updates |

---

## 6. Design Decisions

### Decision 1: Static + Dynamic Separation

**Rationale**: Avoid polluting git history with frequent context updates.

**Approach**:
- Static file committed once, updated rarely
- Dynamic overlay delivered at runtime through multiple channels
- Clean separation of stable vs volatile context

### Decision 2: Industry Standard Adoption

**Rationale**: 60K+ projects use AGENTS.md, native tool support.

**Approach**:
- Adopt AGENTS.md format as-is for static file
- Add dynamic overlay as differentiator
- Maintain compatibility with Cursor, Copilot, Claude Code

### Decision 3: SASE Artifact Deprecation

**Rationale**: Proprietary artifacts have zero industry adoption.

**Approach**:
- Deprecate MTS/BRS/LPS (migrate to AGENTS.md + issue templates)
- Keep CRP/MRP/VCR (governance artifacts with audit value)
- Provide migration tooling and hybrid mode support

### Decision 4: Multi-Channel Delivery

**Rationale**: Different tools consume context differently.

**Approach**:
- VCS checks for universal visibility
- Comments for code review context
- CLI for local development
- IDE extension for real-time integration

---

## 7. Acceptance Criteria

### AC-001: Generator Produces Valid Output

```gherkin
GIVEN the generator service is invoked
WHEN analyzing a project
THEN output AGENTS.md with all 6 sections
AND file length within limits
AND no secrets in content
```

### AC-002: Dynamic Overlay Delivery

```gherkin
GIVEN a code change is submitted
WHEN governance checks complete
THEN dynamic overlay is posted
AND contains current stage, gate status, constraints
AND updates within defined latency targets
```

### AC-003: Security Validation

```gherkin
GIVEN AGENTS.md contains secrets
WHEN commit is attempted
THEN commit is blocked
AND developer receives remediation guidance
```

### AC-004: SASE Migration

```gherkin
GIVEN legacy SASE artifacts exist
WHEN migration is performed
THEN content is preserved in new format
AND old files are archived
AND hybrid mode functions correctly
```

---

## 8. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Tool compatibility issues | Medium | High | Test with all major AI tools |
| Secrets leakage | Low | High | Multiple detection layers, block commits |
| Migration data loss | Low | Medium | Dry-run mode, archive originals |
| Overlay staleness | Medium | Medium | Auto-expiration, timestamp display |

---

## 9. References

### Source Documents
- **SPEC-0001**: Anti-Vibecoding (Vibecoding Index, routing)
- **SPEC-0007**: AGENTS.md Technical Design
- **ADR-029**: AGENTS.md Integration Strategy

### External Standards
- AGENTS.md: Industry Standard for AI Code Governance (60K+ projects)
- OWASP ASVS: Security baseline reference

---

## Document Control

| Field | Value |
|-------|-------|
| **Spec ID** | SPEC-0016 |
| **Version** | 2.0.0 |
| **Status** | APPROVED |
| **Author** | Backend Lead |
| **Reviewer** | CTO |
| **Last Updated** | 2026-01-29 |
| **Framework Version** | 6.0.5 |

---

**Pure Methodology Notes**:
- This specification defines WHAT the AGENTS.md integration requires
- For HOW to implement (CLI commands, service code, API endpoints), see SDLC-Orchestrator documentation
- Static file structure is industry standard; dynamic overlay is governance differentiator
- Security validation is mandatory; implementation tools may vary

---

**End of Specification**
