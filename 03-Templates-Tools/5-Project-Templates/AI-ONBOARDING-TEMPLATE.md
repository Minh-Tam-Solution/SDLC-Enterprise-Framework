# AI Onboarding Template (CLAUDE.md)

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 00 - FOUNDATION
**Status**: ACTIVE - Production Template
**Authority**: CTO Office

---

## Purpose

This template provides a standard structure for AI assistant onboarding documents (CLAUDE.md). Use this when setting up a new project to ensure AI assistants can quickly understand context.

**Target**: AI assistants should understand project context in <30 seconds.

---

## Template

```markdown
# [PROJECT NAME] - AI Context

**Version**: [X.Y.Z]
**Status**: [Stage] - [Sprint/Phase]
**Updated**: [YYYY-MM-DD]

---

## Project Overview

[2-3 sentences describing what this project does and why it exists]

**Core Value**: [One sentence value proposition]

---

## Current Status

| Metric | Value |
|--------|-------|
| Stage | [00-09] - [Stage Name] |
| Sprint | [Number] - [Name] |
| Progress | [X]% |
| Next Gate | [Gate] - [Target Date] |

---

## Tech Stack

```yaml
Backend:
  - [Language/Framework]
  - [Database]
  - [Cache]

Frontend:
  - [Framework]
  - [UI Library]

DevOps:
  - [CI/CD]
  - [Container]
  - [Monitoring]
```

---

## Architecture

[Brief description of architecture pattern]

```
[Simple ASCII diagram showing main components]
```

**Key Principles**:
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]

---

## Key Decisions (ADRs)

| ADR | Decision | Rationale |
|-----|----------|-----------|
| ADR-001 | [Decision] | [Why] |
| ADR-002 | [Decision] | [Why] |

---

## Critical Constraints

### [Constraint 1 Name]
```yaml
DO:
  - [Action 1]
  - [Action 2]

DON'T:
  - [Anti-pattern 1]
  - [Anti-pattern 2]
```

### [Constraint 2 Name]
[Description]

---

## Development Guidelines

### Code Standards
- [Standard 1]
- [Standard 2]
- [Standard 3]

### Testing Requirements
- Unit: [Coverage target]%
- Integration: [Coverage target]%
- E2E: [Critical paths]

### Performance Budget
- API latency (p95): <[X]ms
- Page load: <[X]s
- Database query: <[X]ms

---

## Key Documents

| Document | Purpose | Location |
|----------|---------|----------|
| README.md | Entry point | [Root] |
| docs/README.md | Documentation index | [docs/] |
| OpenAPI Spec | API contract | [Path] |
| Architecture | System design | [Path] |

---

## Current Priorities

### This Sprint ([Number])
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

### Blockers/Risks
- [Risk 1]: [Mitigation]
- [Risk 2]: [Mitigation]

---

## Team Contacts

| Role | Responsibility |
|------|----------------|
| [Role 1] | [Area] |
| [Role 2] | [Area] |

---

## AI Assistant Mandate

When working on this project:

**DO**:
- [Guideline 1]
- [Guideline 2]
- [Guideline 3]

**DON'T**:
- [Anti-pattern 1]
- [Anti-pattern 2]

---

**Last Updated**: [YYYY-MM-DD]
**Owner**: [Team/Role]
```

---

## Tier-Specific Guidelines

### LITE Tier (1-2 people)
- **Size**: 50-200 lines
- **Required sections**: Overview, Tech Stack, Key Documents
- **Optional**: Architecture diagram, ADRs

### STANDARD Tier (3-10 people)
- **Size**: 200-500 lines
- **Required sections**: All LITE + Current Status, Development Guidelines
- **Optional**: Team Contacts, Constraints

### PROFESSIONAL Tier (10-50 people)
- **Size**: 500-1000 lines
- **Required sections**: All STANDARD + ADRs, Constraints, Performance Budget
- **Optional**: None (all sections recommended)

### ENTERPRISE Tier (50+ people)
- **Size**: 1000+ lines
- **Required sections**: All sections mandatory
- **Additional**: Gate references, Compliance requirements, Security baseline

---

## Checklist

Before finalizing CLAUDE.md, verify:

- [ ] Project overview is clear (2-3 sentences)
- [ ] Current status is accurate (stage, sprint, progress)
- [ ] Tech stack is complete with versions
- [ ] Key ADRs are documented
- [ ] Critical constraints are clear (DO/DON'T format)
- [ ] Key documents are linked
- [ ] Current priorities are listed
- [ ] AI guidelines are specific to project

---

**Template Status**: ACTIVE
**Compliance**: MANDATORY for STANDARD+ tier projects
**Last Updated**: December 5, 2025
**Owner**: CTO Office
