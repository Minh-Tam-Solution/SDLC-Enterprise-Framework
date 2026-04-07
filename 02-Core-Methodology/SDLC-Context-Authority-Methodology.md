# Context Authority Methodology
## Framework 6.3.0 Dynamic AGENTS.md Patterns - Section 8

**Version**: 6.3.0
**Status**: ACTIVE - PRODUCTION READY
**Created**: January 28, 2026
**Author**: PM/PJM Team
**Framework**: SDLC 6.3.0 (7-Pillar + 2-Section)
**Section**: Section 8: Unified Specification Standard

---

## 1. Executive Summary

Context Authority is a methodology for **dynamically managing AI coding assistant context** through structured AGENTS.md/CLAUDE.md files. Unlike static configuration files, Context Authority enables:

- **Gate-aware context updates** (context changes based on SDLC stage)
- **Dynamic guidance injection** (real-time updates from governance engine)
- **Context freshness tracking** (prevent stale context issues)
- **Tiered authority levels** (who can update what)

**Industry Standard**: AGENTS.md is the emerging standard for AI assistant configuration (60K+ repos). Context Authority extends this with **dynamic governance** — automated by any platform implementing the SDLC Framework.

---

## 2. The Context Problem

### 2.1 Static AGENTS.md Limitations

Traditional AGENTS.md files are **static**:

```markdown
# AGENTS.md (Static - Industry Standard)

## Project Guidelines
- Use TypeScript
- Follow ESLint rules
- Write tests for new features

## Architecture
- React frontend
- {web_framework} backend
- {database}
```

**Problems with Static Context**:
1. **Stale guidance** - Doesn't reflect current project state
2. **No stage awareness** - Same rules for design vs. production
3. **Manual updates** - Relies on developers to maintain
4. **No enforcement** - Guidance only, no governance

### 2.2 Context Authority Solution

Context Authority adds **dynamic governance layer**:

```markdown
# AGENTS.md (Dynamic - Context Authority Enhanced)

## Project Guidelines
- Use TypeScript
- Follow ESLint rules
- Write tests for new features

## Current Stage Context [AUTO-GENERATED]
<!-- SDLC-CONTEXT-START -->
Stage: BUILD (03)
Gate Status: G2 PASSED (2026-01-28)
Mode: FULL GOVERNANCE
Restrictions:
  - Only Green PRs auto-approve
  - Red PRs require CEO review
  - All changes need spec reference
Last Updated: 2026-01-28T10:30:00Z
<!-- SDLC-CONTEXT-END -->

## Architecture
- React frontend
- {web_framework} backend
- {database}
```

---

## 3. Core Concepts

### 3.1 Context Authority Levels

| Level | Authority | Can Update | Example |
|-------|-----------|------------|---------|
| **System** | Platform (automated) | Stage, gate status, restrictions | Gate pass → update stage |
| **Project** | Tech Lead | Architecture, patterns, conventions | New ADR → update guidelines |
| **Team** | Developers | Implementation notes, tips | Learned pattern → share |
| **Session** | AI Assistant | Current task context | Working on feature X |

### 3.2 Context Zones

```markdown
# AGENTS.md Structure

## Zone 1: Static (Manual Updates)
[Project guidelines, architecture, conventions]
[Updated by: Tech Lead]
[Frequency: Monthly or on major changes]

## Zone 2: Semi-Dynamic (Project Updates)
[Current phase, sprint goals, team assignments]
[Updated by: PM/Tech Lead]
[Frequency: Per sprint]

## Zone 3: Dynamic (System Updates)
<!-- SDLC-CONTEXT-START -->
[Gate status, governance mode, restrictions]
[Updated by: Governance Platform]
[Frequency: Real-time on gate changes]
<!-- SDLC-CONTEXT-END -->

## Zone 4: Ephemeral (Session Context)
[Current task, conversation history summary]
[Updated by: AI Assistant]
[Frequency: Per session]
```

### 3.3 Context Freshness

| Freshness | Age | Action |
|-----------|-----|--------|
| 🟢 Fresh | < 24 hours | Use as-is |
| 🟡 Stale | 1-7 days | Check for updates |
| 🔴 Expired | > 7 days | Force refresh |

---

## 4. Dynamic Context Templates

### 4.1 Gate-Triggered Updates

When gate status changes, inject corresponding context:

**G0.1 Pass (Problem Validated)**:
```markdown
<!-- SDLC-CONTEXT-START -->
Stage: DISCOVER (00)
Gate: G0.1 PASSED
Status: Problem validated, exploring solutions
Guidelines:
  - Focus on solution diversity
  - No implementation yet
  - Document alternatives in design docs
Next Gate: G0.2 (Solution Selection)
<!-- SDLC-CONTEXT-END -->
```

**G0.2 Pass (Solution Selected)**:
```markdown
<!-- SDLC-CONTEXT-START -->
Stage: DEFINE (01)
Gate: G0.2 PASSED
Status: Solution selected, defining requirements
Guidelines:
  - Architecture documented in /docs/arch.md
  - Follow selected approach from ADR-XXX
  - Create specifications before implementation
Next Gate: G1 (Design Ready)
<!-- SDLC-CONTEXT-END -->
```

**G1 Pass (Design Ready)**:
```markdown
<!-- SDLC-CONTEXT-START -->
Stage: BUILD (03)
Gate: G1 PASSED
Status: Design approved, implementation allowed
Guidelines:
  - Follow specs in /docs/specs/
  - Unit tests required for all new code
  - Reference spec ID in PR description
Next Gate: G2 (Integration Ready)
<!-- SDLC-CONTEXT-END -->
```

**G2 Pass (Integration Ready)**:
```markdown
<!-- SDLC-CONTEXT-START -->
Stage: BUILD (03)
Gate: G2 PASSED
Status: Integration tests mandatory
Guidelines:
  - No new features without approval
  - Focus on integration and stability
  - All PRs require 2+ reviewers
Next Gate: G3 (Ship Ready)
<!-- SDLC-CONTEXT-END -->
```

**G3 Pass (Ship Ready)**:
```markdown
<!-- SDLC-CONTEXT-START -->
Stage: DEPLOY (05)
Gate: G3 PASSED
Status: STRICT MODE - Production focus
Guidelines:
  - ⚠️ Only bug fixes allowed
  - ⚠️ No new features
  - ⚠️ All changes require Tech Lead approval
  - Security patches prioritized
Next Gate: G4 (Launch Validated)
<!-- SDLC-CONTEXT-END -->
```

### 4.2 Governance Mode Updates

**WARNING Mode**:
```markdown
<!-- GOVERNANCE-MODE-START -->
Mode: WARNING
Vibecoding Index: Active (logging only)
PR Routing: All PRs pass, quality logged
Action: No blocking, metrics collection
Developer Impact: None
<!-- GOVERNANCE-MODE-END -->
```

**SOFT Mode**:
```markdown
<!-- GOVERNANCE-MODE-START -->
Mode: SOFT
Vibecoding Index: Active (soft enforcement)
PR Routing:
  - Green (0-30): Auto-approve
  - Yellow (31-60): Logged, proceed
  - Orange (61-80): Warning displayed
  - Red (81-100): BLOCKED, CTO review
Action: Red PRs blocked, others logged
Developer Impact: Moderate - add intent to Red PRs
<!-- GOVERNANCE-MODE-END -->
```

**FULL Mode**:
```markdown
<!-- GOVERNANCE-MODE-START -->
Mode: FULL
Vibecoding Index: Active (full enforcement)
PR Routing:
  - Green (0-30): Auto-approve by Tech Lead
  - Yellow (31-60): Tech Lead required
  - Orange (61-80): BLOCKED, Senior review
  - Red (81-100): BLOCKED, CEO review
Action: Only Green PRs auto-approve
Developer Impact: High - all PRs need proper context
<!-- GOVERNANCE-MODE-END -->
```

### 4.3 Issue/Bug Context Injection

**Known Issue Alert**:
```markdown
<!-- KNOWN-ISSUES-START -->
⚠️ Known Issue: Auth service memory leak
  - File: services/auth_service.py
  - Lines: 145-160
  - Status: Under investigation
  - Action: Do not modify without consulting @backend-lead
  - Ticket: SDLC-1234
<!-- KNOWN-ISSUES-END -->
```

**Security Alert**:
```markdown
<!-- SECURITY-ALERT-START -->
🔴 Security Alert: CVE-2026-XXXXX detected
  - Package: {session_package}@2.3.0
  - Severity: HIGH
  - Action: BLOCKED - Upgrade required before merge
  - Fix: npm update {session_package}@2.4.0
<!-- SECURITY-ALERT-END -->
```

---

## 5. Implementation Patterns

### 5.1 AGENTS.md Complete Template

```markdown
# AGENTS.md
## AI Coding Assistant Configuration

<!--
  Context Authority Enhanced AGENTS.md
  Version: 2.0.0 (Context Authority)
  Last Updated: [AUTO-UPDATED]
-->

## Project Overview

**Name**: [Project Name]
**Repository**: [repo-url]
**Framework**: SDLC 6.0
**Tier**: [LITE | STANDARD | PROFESSIONAL | ENTERPRISE]

## Static Guidelines (Zone 1)

### Technology Stack
- Frontend: React 18, TypeScript, Tailwind
- Backend: {web_framework}, {language}
- Database: {database}
- Cache: Redis 7.2

### Coding Standards
- Follow ESLint/Prettier config
- Use TypeScript strict mode
- Write tests for new features (95%+ coverage)
- Document public APIs

### Architecture
- See /docs/architecture/system-design.md
- Follow ADRs in /docs/ADRs/

## Sprint Context (Zone 2)

### Current Sprint
- Sprint: 115
- Theme: Framework 6.0 Templates
- Duration: Feb 10-14, 2026

### Sprint Goals
1. Complete DESIGN_DECISIONS.md template
2. Complete SPEC_DELTA.md template
3. Complete Context Authority methodology

### Team Assignments
- @frontend-lead: UI components
- @backend-lead: API endpoints
- @devops: Infrastructure

## Dynamic Context (Zone 3)

<!-- SDLC-CONTEXT-START -->
Stage: BUILD (03)
Gate: G2 PASSED
Updated: 2026-01-28T10:30:00Z
Mode: FULL GOVERNANCE

Guidelines:
  - All PRs require spec reference
  - Integration tests mandatory
  - Only Green PRs auto-approve

Restrictions:
  - No new features without ADR
  - Security scan must pass
  - 2+ reviewers required
<!-- SDLC-CONTEXT-END -->

<!-- GOVERNANCE-MODE-START -->
Vibecoding Index: ACTIVE
Enforcement: FULL
Thresholds:
  Green: 0-30 (Auto-approve)
  Yellow: 31-60 (Tech Lead)
  Orange: 61-80 (BLOCKED)
  Red: 81-100 (CEO Review)
<!-- GOVERNANCE-MODE-END -->

<!-- KNOWN-ISSUES-START -->
No known issues at this time.
<!-- KNOWN-ISSUES-END -->

## Spec References (Zone 2)

### Active Specifications
- SPEC-0042: User Authentication v2.0.0
- SPEC-0108: Evidence Vault v1.2.0
- SPEC-0201: Anti-Vibecoding v2.0.0

### Related Implementation Patterns
- AI Provider Integration (multi-provider fallback chain)
- Code Generation Pipeline (IR-based codegen with quality gates)
- Progressive Routing (vibecoding index thresholds)

## Context Refresh

Last Full Refresh: 2026-01-28T10:30:00Z
Next Scheduled: 2026-01-29T10:30:00Z
Refresh Command: `[SDLC CLI] context refresh`
```

### 5.2 CLAUDE.md Integration

For Claude-specific projects, extend with CLAUDE.md:

```markdown
# CLAUDE.md
## Claude Code Assistant Configuration

<!-- Inherits from AGENTS.md -->
@import ./AGENTS.md

## Claude-Specific Guidelines

### Model Preferences
- Use Claude Opus 4.5 for complex reasoning
- Use Claude Sonnet for quick edits
- Use Claude Haiku for simple queries

### Tool Usage
- Prefer Edit over Write for existing files
- Use Grep for code search
- Use Task for parallel operations

### Response Style
- Concise, no unnecessary explanation
- Code-first, explain only when asked
- Follow project conventions strictly

## Claude Context Overlay

<!-- CLAUDE-CONTEXT-START -->
Session: Active development
Focus: Current sprint templates
Priority: DESIGN_DECISIONS.md completion
Constraints:
  - Zero Mock Policy enforced
  - AGPL containment required
  - <100ms API latency target
<!-- CLAUDE-CONTEXT-END -->
```

---

## 6. API Integration

### 6.1 Context Refresh Endpoint

```yaml
Endpoint: POST /api/v1/projects/{id}/context/refresh

Request:
  Content-Type: application/json
  Body:
    force: boolean (optional, default false)

Response:
  200:
    context:
      stage: string
      gate_status: string
      governance_mode: string
      restrictions: array
      known_issues: array
    agents_md_patch: string
    last_updated: timestamp
```

### 6.2 Context Query Endpoint

```yaml
Endpoint: GET /api/v1/projects/{id}/context

Response:
  200:
    stage: "BUILD"
    gate: "G2_PASSED"
    mode: "FULL"
    freshness: "FRESH"
    age_hours: 2
    next_refresh: timestamp
    context_zones:
      static: {...}
      semi_dynamic: {...}
      dynamic: {...}
```

### 6.3 Context Subscription (WebSocket)

```yaml
Endpoint: WS /api/v1/projects/{id}/context/subscribe

Events:
  - gate_changed: { gate, status, timestamp }
  - mode_changed: { mode, timestamp }
  - issue_added: { issue, severity, timestamp }
  - issue_resolved: { issue_id, timestamp }
```

---

## 7. CLI Commands

```bash
# Refresh project context
[SDLC CLI] context refresh [--force]

# View current context
[SDLC CLI] context show

# Validate AGENTS.md format
[SDLC CLI] context validate

# Generate AGENTS.md from template
[SDLC CLI] context init --tier PROFESSIONAL

# Check context freshness
[SDLC CLI] context freshness

# Subscribe to context updates (dev mode)
[SDLC CLI] context watch
```

---

## 8. Governance Rules

### 8.1 Update Authority Matrix

| Zone | Who Can Update | Trigger |
|------|----------------|---------|
| Static | Tech Lead | ADR approval |
| Semi-Dynamic | PM/Tech Lead | Sprint planning |
| Dynamic | System | Gate pass/fail |
| Ephemeral | AI | Session start |

### 8.2 Conflict Resolution

When multiple updates conflict:

1. **System updates win** - Gate changes override all
2. **Newer timestamps win** - For same authority level
3. **Higher authority wins** - Tech Lead > Developer
4. **Explicit overrides tracked** - Audit trail maintained

### 8.3 Audit Trail

All context changes are logged:

```yaml
ContextAuditLog:
  id: UUID
  project_id: UUID
  zone: static | semi_dynamic | dynamic
  change_type: update | override | refresh
  previous_value: JSON
  new_value: JSON
  changed_by: user_id | "system"
  changed_at: timestamp
  reason: string
```

---

## 9. Best Practices

### 9.1 Context Hygiene

**DO**:
- ✅ Refresh context at session start
- ✅ Check freshness before major changes
- ✅ Update sprint context at sprint start
- ✅ Clear ephemeral context between features
- ✅ Document context assumptions

**DON'T**:
- ❌ Ignore stale context warnings
- ❌ Manually edit dynamic zones
- ❌ Skip context refresh for quick fixes
- ❌ Assume context is current
- ❌ Override system context without approval

### 9.2 AI Assistant Guidelines

When working with Context Authority:

1. **Session Start**:
   - Check context freshness
   - Refresh if stale (>24h)
   - Read current restrictions

2. **Before Changes**:
   - Verify gate status allows changes
   - Check governance mode
   - Review known issues

3. **During Development**:
   - Reference relevant specs
   - Follow tier requirements
   - Respect restrictions

4. **Before Commit**:
   - Ensure PR meets routing criteria
   - Add spec references
   - Check governance thresholds

---

## 10. Static vs. Dynamic Context

### 10.1 Value of Dynamic Context Authority

| Aspect | Static AGENTS.md | Dynamic Context Authority |
|--------|------------------|---------------------------|
| Updates | Manual | Automatic (via any platform) |
| Gate Awareness | None | Full |
| Governance | Guidance only | Enforcement |
| Audit Trail | None | Complete |
| Context Freshness | Unknown | Tracked |
| Quality Gates | None | Integrated |

### 10.2 Key Advantage

```
┌─────────────────────────────────────────────────────────────────┐
│          CONTEXT AUTHORITY: STATIC vs DYNAMIC               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Static AGENTS.md (Industry baseline):                          │
│  ├── 60K+ repos use AGENTS.md                                  │
│  ├── Manual updates                                             │
│  └── Guidance only, no enforcement                             │
│                                                                 │
│  Dynamic Context Authority (SDLC Framework methodology):        │
│  ├── Dynamic context updates (automated by any platform)        │
│  ├── Gate-triggered changes                                    │
│  ├── Governance enforcement                                     │
│  ├── Vibecoding Index integration                              │
│  ├── Quality gate blocking                                      │
│  └── Full audit trail                                           │
│                                                                 │
│  Key Insight:                                                   │
│  "Static AGENTS.md is guidance.                                │
│   Dynamic AGENTS.md is governance."                             │
│                                                                 │
│  Platforms implementing this: e.g., platforms implementing this framework,          │
│  custom CI/CD pipelines, or any governance tooling.             │
└─────────────────────────────────────────────────────────────────┘
```

---

## 11. Document Control

| Field | Value |
|-------|-------|
| **Methodology ID** | SDLC-CTX-AUTH-001 |
| **Version** | 1.0.0 |
| **Status** | APPROVED |
| **Created** | January 28, 2026 |
| **Author** | PM/PJM Team |
| **Reviewers** | CTO, Tech Lead |
| **Framework** | SDLC 6.3.0 |

---

*SDLC Enterprise Framework 6.3.0 - Context Authority Methodology*
*"Dynamic context. Real governance. AI assistants that understand your project state."*
