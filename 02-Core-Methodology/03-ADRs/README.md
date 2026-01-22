# Architecture Decision Records (ADRs)

This folder contains Architecture Decision Records for the SDLC Enterprise Framework.

## ADR Index

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [ADR-034](ADR-034-Planning-Subagent-Orchestration.md) | Planning Sub-agent Orchestration | APPROVED | Jan 2026 |

## Legacy ADRs

For historical ADRs (pre-5.1.3), see:
- [99-Legacy/ADR-029-AGENTS-MD-Migration.md](../../99-Legacy/ADR-029-AGENTS-MD-Migration.md) - BRS/MTS/LPS to AGENTS.md migration

## ADR Format

All ADRs follow this structure:

```markdown
# ADR-XXX: Title

**Status:** PROPOSED | APPROVED | DEPRECATED | SUPERSEDED
**Date:** Month Day, Year
**Decision Makers:** Names
**Impact:** LOW | MEDIUM | HIGH

## Context
What is the issue that we're seeing that is motivating this decision?

## Decision
What is the change that we're proposing and/or doing?

## Consequences
What becomes easier or more difficult to do because of this change?
```

## Creating New ADRs

1. Use next sequential number (ADR-035, ADR-036, etc.)
2. Follow naming convention: `ADR-XXX-Short-Title.md`
3. Include all required sections
4. Get CTO approval before APPROVED status

---

**Last Updated:** January 2026
**Framework Version:** SDLC 5.1.3
