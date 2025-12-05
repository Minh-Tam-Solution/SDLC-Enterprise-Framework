# Phase Template

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 00 - FOUNDATION
**Status**: ACTIVE - Production Template
**Authority**: CPO Office

---

## Purpose

This template provides a standard structure for Phase planning (4-8 weeks). Phases group related sprints under a common theme and connect Roadmap milestones to Sprint execution.

**Position in Hierarchy**: Roadmap → **Phase** → Sprint → Backlog

---

## Template

```markdown
# Phase [Number]: [Phase Name]

**Version**: [X.Y.Z]
**Status**: [Planning | Active | Complete]
**Duration**: [Start Date] - [End Date] ([X weeks])
**Owner**: [Phase Lead / PM]

---

## Phase Overview

### Theme
[One sentence describing the overarching theme of this phase]

### Objectives
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

### Success Criteria
| Criterion | Target | Measurement |
|-----------|--------|-------------|
| [Criterion 1] | [Target] | [How measured] |
| [Criterion 2] | [Target] | [How measured] |

---

## Roadmap Alignment

| Roadmap Item | Phase Contribution |
|--------------|-------------------|
| [Q[X] Milestone] | [How this phase contributes] |
| [Strategic Goal] | [Phase deliverable supporting goal] |

---

## Sprint Breakdown

| Sprint | Name | Duration | Focus | Status |
|--------|------|----------|-------|--------|
| Sprint [N] | [Name] | [X days] | [Focus area] | [Status] |
| Sprint [N+1] | [Name] | [X days] | [Focus area] | [Status] |

### Sprint [N]: [Name]
**Duration**: [Start] - [End]
**Team**: [Team name(s)]
**Focus**: [1-2 sentence focus]

Key Deliverables:
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

### Sprint [N+1]: [Name]
**Duration**: [Start] - [End]
**Team**: [Team name(s)]
**Focus**: [1-2 sentence focus]

Key Deliverables:
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

---

## Team Allocation

| Team | Members | Role in Phase | Sprints |
|------|---------|---------------|---------|
| [Team A] | [X FTE] | [Role] | Sprint N, N+1 |
| [Team B] | [X FTE] | [Role] | Sprint N+1 |

---

## Dependencies

### External Dependencies
| Dependency | Owner | Due Date | Status |
|------------|-------|----------|--------|
| [Dependency 1] | [Team/Person] | [Date] | [Status] |

### Internal Dependencies
| From | To | What | When |
|------|-----|------|------|
| [Sprint/Team] | [Sprint/Team] | [Deliverable] | [Date] |

---

## Risks

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] | [Name] |

---

## Quality Gates

| Gate | Date | Criteria | Status |
|------|------|----------|--------|
| Phase Start | [Date] | [Entry criteria met] | [Status] |
| Mid-Phase Review | [Date] | [Progress check criteria] | [Status] |
| Phase Complete | [Date] | [Exit criteria] | [Status] |

---

## Metrics

| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| Velocity (story points/sprint) | [Target] | [Actual] | [↑/↓/→] |
| Bug rate | [Target] | [Actual] | [Trend] |
| Test coverage | [Target%] | [Actual%] | [Trend] |

---

## Communication Plan

| Meeting | Frequency | Attendees | Purpose |
|---------|-----------|-----------|---------|
| Phase Kickoff | Once | All teams | Align on objectives |
| Sprint Reviews | Per sprint | Stakeholders | Demo progress |
| Phase Retro | Once | All teams | Lessons learned |

---

## Deliverables Checklist

### Required Deliverables
- [ ] [Deliverable 1] - [Owner]
- [ ] [Deliverable 2] - [Owner]
- [ ] [Deliverable 3] - [Owner]

### Documentation
- [ ] Phase summary report
- [ ] Updated architecture docs (if changed)
- [ ] Updated API specs (if changed)

---

## Notes

[Any additional notes, context, or decisions made during the phase]

---

**Document Status**: [Planning | Active | Complete]
**Last Updated**: [YYYY-MM-DD]
**Next Review**: [Date]
```

---

## Tier-Specific Guidelines

### LITE Tier
- **Not Required** - Use simple milestone tracking

### STANDARD Tier
- **Optional** - Simplified phase (objectives + sprint list only)

### PROFESSIONAL Tier
- **Recommended** - Full phase template with metrics

### ENTERPRISE Tier
- **Mandatory** - Full phase + risk register + communication plan

---

## Checklist

Before starting a Phase, verify:

- [ ] Objectives align with Roadmap milestones
- [ ] Success criteria are measurable
- [ ] Sprints are planned with clear focus
- [ ] Dependencies are identified and tracked
- [ ] Team allocation is confirmed
- [ ] Risks are documented with mitigations
- [ ] Quality gates are defined

---

**Template Status**: ACTIVE
**Compliance**: RECOMMENDED for PROFESSIONAL+ tier projects
**Last Updated**: December 5, 2025
**Owner**: CPO Office
