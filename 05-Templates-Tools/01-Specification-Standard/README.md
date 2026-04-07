# Section 8: Unified Specification Standard

**Version**: 6.3.0
**Status**: ACTIVE - PRODUCTION READY
**Date**: February 15, 2026
**Architecture**: 7-Pillar + 2-Section (Core + Extensions)
**Framework**: SDLC 6.3.0

---

> **MORATORIUM (Sprint 173, Feb 2026)**: No new SPEC documents until Sprint 175.
> CTO approval required to create new SPECs before moratorium lifts.

> **CLEANUP (Sprint 173)**: 16 Orchestrator-specific SPECs archived to `10-archive/03-Legacy/sprint-173-orchestrator-specs/`.
> Those SPECs describe platform implementation (codegen, AI engine, database models), not Framework methodology.
> Only 5 methodology-level SPECs remain here: SPEC-0001, 0002, 0004, 0008, 0012.

## Overview

This directory contains the **Section 8: Unified Specification Standard** — the format definition that ALL specifications in the SDLC ecosystem MUST follow.

**This section defines the SPEC format itself (tool-agnostic). Individual product SPECs belong in their respective platform repos.**

**Key Features**:
- YAML frontmatter for metadata extraction (MANDATORY)
- BDD requirements format (GIVEN-WHEN-THEN)
- Tier-aware specifications (LITE/STANDARD/PROFESSIONAL/ENTERPRISE)
- OpenSpec-inspired patterns + SDLC governance

---

## Methodology SPECs (Retained)

| SPEC | Title | Scope |
|------|-------|-------|
| SPEC-0001 | Anti-Vibecoding QA System | Quality methodology principle |
| SPEC-0002 | Specification Standard | SPEC format definition |
| SPEC-0003 | Policy Guards Design | Policy enforcement pattern |
| SPEC-0004 | 4-Tier Policy Enforcement | Tier governance model |
| SPEC-0005 | Validation Pipeline Interface | Validation contract |

## Archived (Orchestrator-Specific)

16 SPECs that describe SDLC Orchestrator platform implementation have been moved to
`10-archive/03-Legacy/sprint-173-orchestrator-specs/`. See [archive README](../../10-archive/03-Legacy/sprint-173-orchestrator-specs/README.md) for details and migration path.

---

## Contents

```
01-Specification-Standard/
├── README.md                           # This file (start here!)
│
├── Core Templates/
│   ├── SDLC-Specification-Standard.md  # Core spec template (YAML + BDD)
│   ├── DESIGN_DECISIONS.md             # Lightweight ADR template
│   └── SPEC_DELTA.md                   # Version change tracking
│
├── Governance Specifications/
│   └── (SPEC-0021 moved to Orchestrator docs/05-test/)
│
└── examples/                           # Tier-specific examples
    ├── Example-Spec-LITE.md            # Minimal spec (1-2 people)
    ├── Example-Spec-STANDARD.md        # Standard spec (3-10 people)
    └── Example-Spec-PROFESSIONAL.md    # Full spec (10+ people)
```

> **Note**: OpenSpec analysis and decision records have been archived to `10-archive/05-Legacy/OpenSpec-Analysis-2026/`.

---

## Quick Start

### 1. Create a New Specification

```bash
# Copy the template
cp SDLC-Specification-Standard.md ../your-project/specs/New-Feature-Spec.md

# Or use the CLI (when available)
sdlcctl spec init --tier STANDARD --name "New Feature"
```

### 2. Fill Required Fields

Minimum required frontmatter:

```yaml
---
spec_id: SPEC-0001
spec_name: "Your Specification Name"
spec_version: "1.0.0"
status: draft
tier: LITE | STANDARD | PROFESSIONAL | ENTERPRISE
stage: "03"  # SDLC stage (00-09)
category: functional | technical | security
owner: "your-team"
created: 2026-01-28
last_updated: 2026-01-28
---
```

### 3. Add Requirements (BDD Format)

```markdown
#### FR-001: [Requirement Title]
**Priority**: P0
**Tier**: STANDARD

GIVEN [initial context]
WHEN [action occurs]
THEN [expected outcome]
```

### 4. Validate

```bash
# Validate format compliance
sdlcctl spec validate your-spec.md

# Auto-fix common issues
sdlcctl spec validate --fix your-spec.md
```

---

## Tier Requirements

| Section | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---------|------|----------|--------------|------------|
| Frontmatter | Required | Required | Required | Required |
| Overview | Required | Required | Required | Required |
| Context | Optional | Required | Required | Required |
| Requirements (BDD) | Required | Required | Required | Required |
| Design Decisions | Optional | Recommended | Required | Required |
| Technical Spec | Optional | Required | Required | Required |
| Acceptance Criteria | Required | Required | Required | Required |
| Spec Delta | Optional | Recommended | Required | Required |
| Dependencies | Optional | Required | Required | Required |

---

## Core Templates

| Document | Purpose | Priority | Tier |
|----------|---------|----------|------|
| [SDLC-Specification-Standard.md](SDLC-Specification-Standard.md) | Main spec template | P0 | ALL |
| [DESIGN_DECISIONS.md](DESIGN_DECISIONS.md) | Lightweight ADR | P1 | STD+ |
| [SPEC_DELTA.md](SPEC_DELTA.md) | Version tracking | P1 | PRO+ |
| [SDLC-Context-Authority-Methodology.md](../../02-Core-Methodology/SDLC-Context-Authority-Methodology.md) | Dynamic AGENTS.md | P1 | ALL |

---

## Tier Examples

| Example | Tier | Team Size | Use Case |
|---------|------|-----------|----------|
| [Example-Spec-LITE.md](examples/Example-Spec-LITE.md) | LITE | 1-2 | Solo developer, MVP |
| [Example-Spec-STANDARD.md](examples/Example-Spec-STANDARD.md) | STANDARD | 3-10 | Small team, typical project |
| [Example-Spec-PROFESSIONAL.md](examples/Example-Spec-PROFESSIONAL.md) | PROFESSIONAL | 10-50 | Regulated industries |

---

## Migration from 5.3.0

Existing specifications can be migrated:

1. Add YAML frontmatter
2. Convert requirements to BDD format
3. Add tier-specific requirements
4. Validate with sdlcctl

Estimated effort: 15-60 minutes per spec depending on complexity.

See [SDLC-Specification-Standard.md](./SDLC-Specification-Standard.md) Section 7 for detailed migration guide.

---

## Related Documents

- [../README.md](../README.md) - Templates & Tools overview
- [../../03-AI-GOVERNANCE/](../../03-AI-GOVERNANCE/) - 7 AI Governance Principles
- [../../CONTENT-MAP.md](../../CONTENT-MAP.md) - Topic -> canonical file mapping
- [../../CHANGELOG.md](../../CHANGELOG.md) - Framework version history

---

**Document Status**: ACTIVE
**Last Updated**: February 14, 2026
**Owner**: CTO + CPO Office
**Framework**: SDLC 6.3.0 (7-Pillar + 2-Section)

***"Consistent specifications enable consistent quality."***
