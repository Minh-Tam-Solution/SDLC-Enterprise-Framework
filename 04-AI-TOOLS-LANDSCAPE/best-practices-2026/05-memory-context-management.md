# Memory & Context Management
## CLAUDE.md Patterns and Best Practices

**Version:** 6.0.0
**Status:** ACTIVE
**Date:** January 27, 2026

---

## Overview

CLAUDE.md files are the primary mechanism for providing persistent context to AI coding agents. This guide covers hierarchy, structure, and best practices.

---

## File Hierarchy

### Loading Order (Precedence)

```
1. Managed (Enterprise)   ~/.claude/managed/CLAUDE.md    ← Cannot override
2. User                   ~/.claude/CLAUDE.md           ← Personal defaults
3. Project                ./CLAUDE.md or ./.claude/CLAUDE.md
4. Local (personal)       ./CLAUDE.local.md             ← Git-ignored
```

**Key behaviors:**
- Claude recurses UP from cwd to root `/`
- Discovers nested CLAUDE.md ONLY when reading files in subtrees
- Higher hierarchy loads first = foundation
- Managed settings CANNOT be overridden

---

## Project Setup

### Basic Structure

```
your-project/
├── CLAUDE.md                # Main instructions (git tracked)
├── CLAUDE.local.md          # Personal overrides (git ignored)
└── .claude/
    ├── settings.json        # Project settings
    ├── settings.local.json  # Personal settings (git ignored)
    └── rules/               # Focused rule files
        ├── code-style.md
        ├── testing.md
        └── security.md
```

### Bootstrapping

```bash
# Generate initial CLAUDE.md
claude -p "Create a CLAUDE.md for this project"

# Or start from template
cp ~/.claude/templates/CLAUDE.md ./CLAUDE.md
```

---

## CLAUDE.md Structure

### Recommended Sections

```markdown
# Project Context
Brief description of what this project does.

# Architecture
- Tech stack: [list]
- Key patterns: [list]
- Directory structure: [brief overview]

# Code Standards
- Style guide references
- Naming conventions
- Required practices

# Testing Requirements
- Coverage thresholds
- Test patterns
- Required test types

# Security Requirements
- Authentication approach
- Authorization rules
- Sensitive data handling

# Workflows
- Git workflow
- PR requirements
- Deployment process
```

### Example

```markdown
# SDLC Orchestrator

Operating System for Software 3.0 - governance platform for AI coders.

# Architecture
- Backend: FastAPI + PostgreSQL + Redis
- Frontend: React + TypeScript + shadcn/ui
- Integration: OPA (policy), MinIO (storage), Ollama (AI)

# Code Standards
- Python: snake_case, Google docstrings, type hints required
- TypeScript: camelCase/PascalCase, strict mode
- Max file length: 500 lines
- Test coverage: 95%+

# Critical Constraints
- AGPL Containment: Network-only access to MinIO/Grafana
- Zero Mock Policy: No placeholders, real implementations only
- Performance: <100ms p95 API latency

# Testing
- pytest + pytest-asyncio for backend
- Vitest + Playwright for frontend
- Integration tests required for all APIs

# Workflows
- Feature branches from main
- PR requires 2 approvers
- All tests must pass before merge
```

---

## Imports

### Syntax

```markdown
<!-- Import specific files -->
See @README for project overview
@package.json for npm commands

<!-- Import documentation -->
@docs/git-instructions.md

<!-- Import personal preferences -->
@~/.claude/personal-preferences.md
```

### Limits

- **Max depth:** 5 hops
- **NOT evaluated** in code blocks/spans
- Alternative to CLAUDE.local.md for git worktrees

---

## Rules Directory

### For Large Codebases

```
.claude/rules/
├── code-style.md      # Formatting, naming
├── testing.md         # Test requirements
├── security.md        # Security rules
├── api-design.md      # API conventions
└── database.md        # DB patterns
```

### Rule File Format

```markdown
# Testing Rules

## Unit Tests
- Every function with business logic needs tests
- Use pytest fixtures for setup
- Mock external dependencies
- Assert both success and failure paths

## Integration Tests
- Test API contract compliance
- Use real database (test container)
- Clean up after each test

## Coverage
- Minimum: 90% line coverage
- Critical paths: 100% branch coverage
```

---

## Quick Memory Commands

```bash
/memory          # View loaded memories
#<text>          # Quick add via shortcut
/memory edit     # Direct edit interface
/compact         # Manual context compaction
/context         # View context status
```

---

## Best Practices

### ✅ DO

```markdown
# ✅ GOOD - Specific, actionable
## Code Style
- Use 2-space indentation in all .ts files
- Prefer const over let
- Always use TypeScript strict mode
- Use async/await instead of .then()

## Error Handling
- Wrap external calls in try/catch
- Use custom error classes from @errors/
- Log errors with context (user_id, action)
- Return appropriate HTTP status codes
```

### ❌ DON'T

```markdown
# ❌ BAD - Vague, unactionable
## General Rules
- Write good code
- Test properly
- Follow best practices
- Be careful with security
```

---

## Organization Tips

### 1. Use Bullet Points Over Paragraphs

```markdown
# ❌ BAD
The code should be well-formatted with proper indentation
and should follow our naming conventions...

# ✅ GOOD
- 2-space indentation
- camelCase for variables
- PascalCase for classes
- UPPER_CASE for constants
```

### 2. Group Related Instructions

```markdown
# ✅ GOOD
## Authentication
- JWT tokens expire in 15 minutes
- Refresh tokens expire in 7 days
- Use bcrypt with cost=12

## Authorization
- RBAC with 13 roles
- Row-level security enabled
- Check permissions before DB queries
```

### 3. Be Specific Over General

```markdown
# ❌ BAD
Use proper error handling

# ✅ GOOD
Error handling pattern:
1. Catch specific exceptions first
2. Log with context: logger.error(f"Failed to {action}: {e}", extra={"user_id": user_id})
3. Return HTTPException with appropriate status code
4. Never expose stack traces to clients
```

---

## Enterprise/Team Settings

### Managed Settings (Cannot Override)

```bash
# Deploy via MDM/Group Policy
~/.claude/managed/managed-settings.json
~/.claude/managed/managed-mcp.json
~/.claude/managed/CLAUDE.md
```

### Example Managed Settings

```json
{
  "permissions": {
    "deny": [
      "Bash(rm:*)",
      "Edit(**/production/**)",
      "WebFetch(*.internal.corp)"
    ]
  },
  "allowManagedHooksOnly": true,
  "environmentVariables": {
    "COMPANY_STANDARDS": "true"
  }
}
```

### Settings Precedence

```
1. Managed (Enterprise) ← CANNOT OVERRIDE
2. CLI arguments
3. Local project (.claude/settings.local.json)
4. Shared project (.claude/settings.json)
5. User (~/.claude/settings.json)
```

---

## Dynamic Context Overlay

### Gate-Aware Updates

CLAUDE.md can be dynamically updated based on gate status:

```yaml
Context updates by gate:
  G0.2 Pass (Solution Approved):
    → "Design approved. Architecture in docs/arch.md"

  G1 Pass (Legal Validated):
    → "Stage: Build. Unit tests required"

  G3 Pass (Feature Ready):
    → "STRICT MODE. Only bug fixes allowed"

  Security Scan Fails:
    → "BLOCKED: CVE-XXX detected. Fix before proceeding"
```

### Implementation

```markdown
# Dynamic Context (Auto-updated)

## Current Stage: BUILD
- Architecture decisions are LOCKED
- Focus on implementation
- All changes need tests

## Known Issues
- Auth service has rate limiting bug (WIP)
- Do not modify auth_service.py lines 100-150

## Recent Decisions
- ADR-034: Use planning mode for >15 LOC changes
- ADR-029: Migrated to AGENTS.md format
```

---

## Context Size Management

### Monitor Usage

```bash
/context  # Check current context size

# Warning if skills excluded due to budget
# Increase budget if needed:
export SLASH_COMMAND_TOOL_CHAR_BUDGET=30000
```

### Optimization Tips

1. **Keep CLAUDE.md focused** - Don't repeat what's in code comments
2. **Use imports** - Reference other docs instead of copying
3. **Archive old context** - Move outdated info to archived files
4. **Use rules directory** - Split large CLAUDE.md into focused files

---

**Document Status:** ACTIVE
**Last Updated:** January 22, 2026
