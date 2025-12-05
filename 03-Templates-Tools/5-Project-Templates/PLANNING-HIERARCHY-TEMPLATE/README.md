# Planning Hierarchy Templates

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 00 - FOUNDATION
**Status**: ACTIVE - Production Templates
**Authority**: CPO Office

---

## Purpose

This folder contains templates for the **4-Level Planning Hierarchy** defined in ADR-013. These templates ensure consistent planning structure from strategic vision to daily execution.

---

## The 4-Level Hierarchy

```
┌─────────────────────────────────────────────────────────────────────┐
│                          ROADMAP                                     │
│                    (12 months, quarterly)                            │
│                    Strategic goals & milestones                      │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                           PHASE                                      │
│                      (4-8 weeks, themed)                             │
│                    Groups related sprints                            │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          SPRINT                                      │
│                      (5-10 days, committed)                          │
│                    Time-boxed delivery                               │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          BACKLOG                                     │
│                    (Individual items, hours)                         │
│                    Stories, tasks, bugs                              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Templates in This Folder

| Template | Purpose | Tier Required |
|----------|---------|---------------|
| [ROADMAP-TEMPLATE.md](ROADMAP-TEMPLATE.md) | 12-month strategic planning | PROFESSIONAL+ |
| [PHASE-TEMPLATE.md](PHASE-TEMPLATE.md) | 4-8 week themed groupings | PROFESSIONAL+ |
| [SPRINT-TEMPLATE.md](SPRINT-TEMPLATE.md) | 5-10 day committed work | STANDARD+ |
| [BACKLOG-TEMPLATE.md](BACKLOG-TEMPLATE.md) | Individual work items | STANDARD+ |

---

## Tier Requirements

| Tier | Required Levels | Notes |
|------|-----------------|-------|
| LITE | None | Simple version tracking (v1.0, v1.1) |
| STANDARD | Sprint + Backlog | Basic sprint planning |
| PROFESSIONAL | All 4 levels | Full hierarchy |
| ENTERPRISE | All 4 levels + metrics | With governance reporting |

---

## How to Use

### Step 1: Determine Your Tier
```yaml
LITE (1-2 people, <$50K):
  → Skip these templates, use simple version tracking

STANDARD (3-10 people, $50-200K):
  → Use SPRINT-TEMPLATE.md + BACKLOG-TEMPLATE.md

PROFESSIONAL (10-50 people, $200K-1M):
  → Use all 4 templates

ENTERPRISE (50+ people, $1M+):
  → Use all 4 templates + weekly reporting
```

### Step 2: Copy Templates
```bash
# For PROFESSIONAL+ tier
cp ROADMAP-TEMPLATE.md /your-project/docs/00-Project-Foundation/04-Roadmap/
cp PHASE-TEMPLATE.md /your-project/docs/03-Development-Implementation/02-Sprint-Plans/
cp SPRINT-TEMPLATE.md /your-project/docs/03-Development-Implementation/02-Sprint-Plans/
cp BACKLOG-TEMPLATE.md /your-project/docs/03-Development-Implementation/
```

### Step 3: Customize
- Replace all `[placeholders]` with actual values
- Remove sections not applicable to your tier
- Add project-specific sections as needed

---

## Connection Between Levels

```yaml
Traceability:
  Roadmap Goal → Phase Objective → Sprint Goal → Backlog Item

Example:
  Roadmap: "Achieve 10K active users by Q2"
  └─► Phase 1: "Launch MVP with core features"
      └─► Sprint 5: "Complete user authentication"
          └─► US-042: "As a user, I want to login with GitHub OAuth"
```

---

## Related Documents

- [ADR-013: 4-Level Planning Hierarchy](../../../02-Design-Architecture/ADRs/)
- [SDLC-Team-Collaboration-Standards.md](../../../08-Documentation-Standards/Team-Collaboration/)

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY template adoption for PROFESSIONAL+ tier
**Last Updated**: December 5, 2025
**Owner**: CPO Office
