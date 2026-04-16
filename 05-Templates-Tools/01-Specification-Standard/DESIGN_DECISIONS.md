# DESIGN_DECISIONS.md Template
## Framework 6.3.0 Lightweight Decision Records - Section 8

**Version**: 6.3.0
**Status**: ACTIVE - PRODUCTION READY
**Created**: January 28, 2026
**Author**: PM/PJM Team
**Framework**: SDLC 6.3.0 (7-Pillar + 2-Section)
**Section**: Section 8: Unified Specification Standard

---

## 1. Purpose

DESIGN_DECISIONS.md provides a **lightweight alternative to full ADRs** for documenting technical decisions during active development. Use this template when:

- Decision is feature-scoped (not architectural)
- Quick documentation needed during sprint
- Full ADR process is overkill
- Decision may evolve rapidly

**When to use full ADR instead**:
- Cross-cutting architectural decisions
- Security-critical choices
- Decisions affecting multiple systems
- Long-term strategic choices

---

## 2. Template Structure

### 2.1 YAML Frontmatter

```yaml
---
# Decision Metadata
decision_id: DD-[NNNN]
spec_id: SPEC-[NNNN]              # Parent specification
title: "[Short descriptive title]"
status: proposed | accepted | deprecated | superseded
category: technical | ux | performance | security | integration

# Context
created: YYYY-MM-DD
decided: YYYY-MM-DD | null
author: "[name/team]"
reviewers: ["reviewer1", "reviewer2"]

# Classification
impact: low | medium | high
reversibility: easy | moderate | difficult
urgency: immediate | sprint | quarter

# Relationships
supersedes: DD-[NNNN] | null
superseded_by: DD-[NNNN] | null
related_adrs: ["ADR-XXX"]
related_decisions: ["DD-XXX", "DD-YYY"]
---
```

### 2.2 Content Sections

```markdown
## Decision: [Title]

### Context
[1-2 paragraphs describing the situation requiring a decision]

### Options Considered

#### Option A: [Name]
- **Description**: [Brief description]
- **Pros**: [List benefits]
- **Cons**: [List drawbacks]
- **Effort**: [S/M/L/XL]

#### Option B: [Name]
- **Description**: [Brief description]
- **Pros**: [List benefits]
- **Cons**: [List drawbacks]
- **Effort**: [S/M/L/XL]

#### Option C: [Name] (if applicable)
...

### Decision
**Chosen Option**: [Option X]

**Rationale**: [Why this option was selected]

### Consequences
- [Consequence 1]
- [Consequence 2]

### Implementation Notes
- [Note 1]
- [Note 2]
```

---

## 3. Complete Template

```markdown
---
decision_id: DD-0001
spec_id: SPEC-0042
title: "Theme Storage Mechanism"
status: accepted
category: technical

created: 2026-01-28
decided: 2026-01-28
author: "frontend-team"
reviewers: ["tech-lead", "senior-dev"]

impact: low
reversibility: easy
urgency: sprint

supersedes: null
superseded_by: null
related_adrs: []
related_decisions: []
---

## Decision: Theme Storage Mechanism

### Context

The dark mode feature requires persisting user theme preference across sessions.
We need to decide how to store this preference considering:
- User experience (instant loading without flash)
- Privacy (no unnecessary server calls)
- Complexity (team bandwidth)

### Options Considered

#### Option A: localStorage
- **Description**: Store theme in browser localStorage
- **Pros**:
  - Simple implementation
  - No server dependency
  - Instant access on page load
- **Cons**:
  - Not synced across devices
  - Cleared if user clears browser data
- **Effort**: S

#### Option B: User Profile API
- **Description**: Store in user profile on backend
- **Pros**:
  - Synced across devices
  - Persists with account
- **Cons**:
  - Requires API call on load
  - Flash of wrong theme possible
  - More complex implementation
- **Effort**: M

#### Option C: Hybrid (localStorage + API sync)
- **Description**: localStorage for instant load, API for cross-device sync
- **Pros**:
  - Best of both worlds
  - Instant load + sync
- **Cons**:
  - Most complex
  - Conflict resolution needed
- **Effort**: L

### Decision

**Chosen Option**: Option A (localStorage)

**Rationale**:
- MVP scope prioritizes simplicity
- Cross-device sync not required for initial release
- Can upgrade to hybrid approach in future sprint
- Aligns with performance budget (<1s dashboard load)

### Consequences

- Users must set preference on each device
- Theme loads instantly without flash
- No backend changes required
- Future: Consider Option C for v2.0

### Implementation Notes

- Use `localStorage.setItem('theme', 'dark' | 'light')`
- Check on app initialization before render
- Provide system preference detection as fallback
- Add to user settings page with toggle switch
```

---

## 4. Quick Reference

### 4.1 Status Transitions

```
proposed → accepted → [implemented]
    ↓
deprecated → superseded (by new DD)
```

### 4.2 Impact Levels

| Level | Definition | Examples |
|-------|------------|----------|
| **Low** | Isolated change, easy rollback | UI component choice, library selection |
| **Medium** | Affects multiple components | State management approach, API design |
| **High** | Cross-cutting, hard to change | Database schema, authentication flow |

### 4.3 Reversibility

| Level | Definition | Examples |
|-------|------------|----------|
| **Easy** | Can change in 1 sprint | Config change, UI tweak |
| **Moderate** | Requires refactoring | Library swap, data migration |
| **Difficult** | Major effort to change | Architecture shift, breaking API change |

### 4.4 Decision Categories

| Category | Description |
|----------|-------------|
| **technical** | Implementation approach, libraries, patterns |
| **ux** | User experience, UI/UX choices |
| **performance** | Optimization strategies, caching |
| **security** | Authentication, authorization, data protection |
| **integration** | Third-party services, API design |

---

## 5. Best Practices

### 5.1 Writing Effective Decisions

**DO**:
- ✅ Keep context concise (1-2 paragraphs)
- ✅ List at least 2 options considered
- ✅ Explain rationale clearly
- ✅ Document consequences honestly
- ✅ Link to related specs and ADRs
- ✅ Update status when implemented

**DON'T**:
- ❌ Write essay-length context
- ❌ Skip alternatives analysis
- ❌ Forget implementation notes
- ❌ Leave decisions as "proposed" indefinitely
- ❌ Create DD for trivial choices

### 5.2 When to Escalate to ADR

Escalate a Design Decision to full ADR when:

| Trigger | Action |
|---------|--------|
| Impact becomes HIGH | Create ADR, link DD as context |
| Affects multiple specs | Create ADR, consolidate decisions |
| Security implications | Create ADR with security review |
| Cross-team coordination | Create ADR for alignment |
| Reversibility is DIFFICULT | Create ADR for documentation |

### 5.3 Review Guidelines

| Impact | Review Requirement |
|--------|-------------------|
| Low | Self-review + 1 peer |
| Medium | Tech Lead review required |
| High | Tech Lead + Senior Dev review |

---

## 6. Integration with SDLC 6.3.0

### 6.1 Linking to Specifications

In the parent specification, reference design decisions:

```markdown
## 4. Design Decisions

### 4.1 Related Decisions

| ID | Title | Status | Impact |
|----|-------|--------|--------|
| [DD-0001](./decisions/DD-0001.md) | Theme Storage | Accepted | Low |
| [DD-0002](./decisions/DD-0002.md) | Animation Library | Proposed | Low |

### 4.2 Related ADRs

| ADR | Title | Status |
|-----|-------|--------|
| [ADR-015](../ADRs/ADR-015.md) | Theme System Architecture | Accepted |
```

### 6.2 Directory Structure

```
project/
├── docs/
│   └── specs/
│       ├── SPEC-0042-dark-mode.md
│       └── decisions/
│           ├── DD-0001-theme-storage.md
│           ├── DD-0002-animation-library.md
│           └── README.md
└── ...
```

### 6.3 Naming Convention

```
DD-[NNNN]-[short-description].md

Examples:
- DD-0001-theme-storage.md
- DD-0002-animation-library.md
- DD-0015-cache-strategy.md
```

---

## 7. Validation Rules

### 7.1 Required Fields

```yaml
Mandatory:
  - decision_id
  - spec_id
  - title
  - status
  - created
  - author
  - impact
  - reversibility

Recommended:
  - decided (if status = accepted)
  - reviewers
  - related_adrs
  - related_decisions
```

### 7.2 CLI Validation

```bash
# Validate design decision format
sdlcctl decision validate decisions/DD-0001.md

# List all decisions for a spec
sdlcctl decision list --spec SPEC-0042

# Check for stale proposed decisions
sdlcctl decision stale --days 14
```

---

## 8. Examples by Category

### 8.1 Technical Decision

```yaml
decision_id: DD-0010
title: "State Management Library"
category: technical
impact: medium
options:
  - Zustand (chosen): Simple, lightweight
  - Redux: Powerful but complex
  - Jotai: Atomic but less ecosystem
```

### 8.2 UX Decision

```yaml
decision_id: DD-0020
title: "Error Message Display Strategy"
category: ux
impact: low
options:
  - Toast notifications (chosen): Non-intrusive
  - Inline errors: Contextual but cluttered
  - Modal dialogs: Attention-grabbing but disruptive
```

### 8.3 Performance Decision

```yaml
decision_id: DD-0030
title: "Image Loading Strategy"
category: performance
impact: medium
options:
  - Lazy loading (chosen): Better initial load
  - Eager loading: Simpler but slower
  - Progressive loading: Best UX but complex
```

### 8.4 Security Decision

```yaml
decision_id: DD-0040
title: "Token Storage Location"
category: security
impact: high
reversibility: moderate
options:
  - HttpOnly cookie (chosen): XSS-safe
  - localStorage: Convenient but XSS-vulnerable
  - Memory only: Safest but loses on refresh
note: "HIGH impact - consider escalating to ADR"
```

---

## 9. Document Control

| Field | Value |
|-------|-------|
| **Template ID** | SDLC-DD-TPL-001 |
| **Version** | 1.0.0 |
| **Status** | APPROVED |
| **Created** | January 28, 2026 |
| **Author** | PM/PJM Team |
| **Reviewers** | CTO, Tech Lead |
| **Framework** | SDLC 6.3.0 |

---

## 10. Changelog

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-01-28 | PM Team | Initial template |

---

*SDLC Enterprise Framework 6.3.0 - Design Decisions Template*
*"Document decisions while they're fresh. Lightweight by design."*
