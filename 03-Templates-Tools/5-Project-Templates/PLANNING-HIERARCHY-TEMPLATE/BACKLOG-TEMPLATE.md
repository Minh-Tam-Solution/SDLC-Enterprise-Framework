# Backlog Template

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 03 - DEVELOPMENT
**Status**: ACTIVE - Production Template
**Authority**: CPO Office

---

## Purpose

This template provides a standard structure for Product Backlog management. Individual backlog items represent the smallest unit of work with hour estimates.

**Position in Hierarchy**: Roadmap → Phase → Sprint → **Backlog**

---

## Template

```markdown
# Product Backlog - [Project Name]

**Version**: [X.Y.Z]
**Status**: Active
**Owner**: [Product Owner]
**Last Refined**: [YYYY-MM-DD]

---

## Backlog Overview

| Metric | Value |
|--------|-------|
| Total Items | [N] |
| Ready for Sprint | [N] |
| In Refinement | [N] |
| Icebox | [N] |

---

## Priority Legend

| Priority | Meaning | SLA |
|----------|---------|-----|
| P0 - Critical | Production blocker, revenue impact | Within 24h |
| P1 - High | Important for current phase goals | Within sprint |
| P2 - Medium | Valuable but not urgent | Within 2 sprints |
| P3 - Low | Nice to have, can defer | Backlog |

---

## Ready for Sprint

Items that meet Definition of Ready and can be pulled into next sprint.

### User Stories

| ID | Title | Priority | Points | Acceptance Criteria |
|----|-------|----------|--------|---------------------|
| US-001 | [Title] | [P0-P3] | [X] | [Brief AC summary] |
| US-002 | [Title] | [Priority] | [X] | [Brief AC] |

### Technical Debt

| ID | Title | Priority | Estimate | Impact |
|----|-------|----------|----------|--------|
| TD-001 | [Title] | [Priority] | [Xh] | [Impact description] |

### Bugs

| ID | Title | Priority | Estimate | Reported |
|----|-------|----------|----------|----------|
| BUG-001 | [Title] | [Priority] | [Xh] | [Date] |

---

## In Refinement

Items being refined with the team. Not yet ready for sprint.

| ID | Title | Status | Blocker |
|----|-------|--------|---------|
| US-010 | [Title] | [Needs AC / Needs estimate / Needs tech review] | [Blocker] |

---

## Icebox

Low priority items parked for future consideration.

| ID | Title | Reason for Icebox | Last Reviewed |
|----|-------|-------------------|---------------|
| US-050 | [Title] | [Reason] | [Date] |

---

## Definition of Ready

A backlog item is READY when:

- [ ] User story follows format: "As a [role], I want [feature], so that [benefit]"
- [ ] Acceptance criteria are clear and testable
- [ ] Story points estimated by team
- [ ] Dependencies identified
- [ ] Technical approach discussed
- [ ] No blockers preventing work

---

## User Story Template

```
### US-[ID]: [Title]

**As a** [role]
**I want** [feature]
**So that** [benefit]

**Priority**: [P0/P1/P2/P3]
**Points**: [X]
**Sprint**: [Assigned sprint or "Backlog"]

**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

**Technical Notes**:
[Any technical considerations, dependencies, or approach notes]

**Links**:
- Design: [Link]
- API Spec: [Link]
```

---

## Bug Template

```
### BUG-[ID]: [Title]

**Severity**: [P0/P1/P2/P3]
**Estimate**: [Xh]
**Reported By**: [Name]
**Reported Date**: [YYYY-MM-DD]

**Description**:
[Clear description of the bug]

**Steps to Reproduce**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Behavior**:
[What should happen]

**Actual Behavior**:
[What actually happens]

**Environment**:
- Browser/OS: [Details]
- Version: [App version]

**Screenshots/Logs**:
[Attach if applicable]
```

---

## Technical Task Template

```
### TT-[ID]: [Title]

**Type**: [Refactor / Performance / Security / DevOps]
**Priority**: [P0/P1/P2/P3]
**Estimate**: [Xh]

**Description**:
[What needs to be done and why]

**Approach**:
[Technical approach or implementation notes]

**Acceptance Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]

**Related Stories**: [US-XXX, US-YYY]
```

---

## Refinement Log

| Date | Items Refined | Participants | Notes |
|------|---------------|--------------|-------|
| [Date] | US-001, US-002 | [Names] | [Key decisions] |

---

## Backlog Health Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Items Ready | 2 sprints worth | [N items] | [✅/⚠️/❌] |
| Avg Item Age | <30 days | [X days] | [Status] |
| Groomed Rate | 100% of sprint items | [X%] | [Status] |

---

**Document Status**: Active
**Refinement Cadence**: Weekly
**Last Updated**: [YYYY-MM-DD]
```

---

## Tier-Specific Guidelines

### LITE Tier
- **Optional** - Simple task list in README or issue tracker

### STANDARD Tier
- **Recommended** - Basic backlog (user stories + bugs)

### PROFESSIONAL Tier
- **Mandatory** - Full backlog with Definition of Ready

### ENTERPRISE Tier
- **Mandatory** - Full backlog + refinement log + health metrics

---

## Checklist

For effective backlog management:

- [ ] Backlog is prioritized (P0 → P3)
- [ ] Top items meet Definition of Ready
- [ ] Regular refinement sessions scheduled
- [ ] Technical debt tracked separately
- [ ] Bugs triaged within 24h of report
- [ ] Icebox reviewed quarterly

---

**Template Status**: ACTIVE
**Compliance**: RECOMMENDED for STANDARD+ tier projects
**Last Updated**: December 5, 2025
**Owner**: CPO Office
