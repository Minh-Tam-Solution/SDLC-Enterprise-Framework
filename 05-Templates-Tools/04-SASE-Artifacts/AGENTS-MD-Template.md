# AGENTS.md Template

**Version**: 2.0.0
**Status**: RECOMMENDED
**Framework**: SDLC 6.1.0
**Target**: <60 lines (per HumanLayer research)

---

## Overview

`AGENTS.md` is the **industry standard** for AI coding assistant context (60K+ repos).
Keep it **under 60 lines** for maximum effectiveness.

> "Frontier thinking LLMs can follow ~150-200 instructions with reasonable consistency."
> "HumanLayer's CLAUDE.md is less than sixty lines." — HumanLayer Research

---

## The Template (<60 lines)

```markdown
# AGENTS.md

## Quick Start
- `docker compose up -d` - Start services
- `npm run dev` - Frontend dev server
- `npm test` - Run tests

## Architecture
- Backend: Python 3.11+ / FastAPI
- Frontend: React 18 / TypeScript
- Database: PostgreSQL 15 / Redis 7

## Conventions
- Python: snake_case, type hints, Google docstrings
- TypeScript: PascalCase components, camelCase utils
- Git: `type(scope): description` commits

## Security
- NEVER commit secrets
- AGPL Containment: network-only access (no SDK imports)
- Follow OWASP Top 10

## DO NOT
- Add TODO/placeholder code (Zero Mock Policy)
- Skip error handling or tests
- Import AGPL libraries directly
- Push to main without PR review
```

**Line count: 28 lines** ✅

---

## What NOT to Include

| Don't Include | Why | Alternative |
|---------------|-----|-------------|
| Code style rules | Linters enforce this | Use ruff.toml, eslint |
| Full documentation | Too verbose | Link to /docs |
| Sprint context | Changes often | Deliver via PR comments |
| Historical info | Clutters | Use ADRs |

> "Never send an LLM to do a linter's job." — HumanLayer

---

## Progressive Disclosure (Large Projects)

For codebases needing >60 lines of context:

```
.claude/rules/
├── building.md    # Build commands
├── testing.md     # Test patterns
└── security.md    # Security rules
```

Reference from AGENTS.md: `See .claude/rules/ for details`

**Limit**: Max 5 import hops.

---

## Dynamic Context (NOT in AGENTS.md)

Sprint/gate context is delivered via:
- **PR comments** (auto-posted)
- **CLI**: `sdlcctl context pull`
- **IDE extension** panel

**Never commit dynamic context to AGENTS.md.**

---

## Migration

```bash
# Generate from project analysis
sdlcctl agents init

# Validate line count
wc -l AGENTS.md  # Should be <60
```

---

## Related

- [05-Context-Management.md](../../03-AI-GOVERNANCE/05-Context-Management.md) - Full principle
- [DEPRECATION-POLICY.md](../../DEPRECATION-POLICY.md) - MTS/BRS/LPS deprecated

---

**Document Status**: RECOMMENDED
**Replaces**: MTS, BRS, LPS (deprecated Jan 2026)
**Last Updated**: January 2026
