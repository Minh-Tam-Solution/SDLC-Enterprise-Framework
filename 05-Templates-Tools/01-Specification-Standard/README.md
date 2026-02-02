# Section 8: Unified Specification Standard

**Version**: 6.0.3
**Status**: ACTIVE - PRODUCTION READY
**Date**: February 1, 2026
**Architecture**: 7-Pillar + 2-Section (Core + Extensions)
**Framework**: SDLC 6.0.3

---

## Overview

This directory contains the **Section 8: Unified Specification Standard** for SDLC Framework: 6.0.3. All specifications in the SDLC ecosystem MUST follow this format to ensure AI-parseability, consistency, and tier-awareness.

**Key Features**:
- YAML frontmatter for metadata extraction (MANDATORY)
- BDD requirements format (GIVEN-WHEN-THEN)
- Tier-aware specifications (LITE/STANDARD/PROFESSIONAL/ENTERPRISE)
- OpenSpec-inspired patterns + SDLC governance

---

## What's New in 6.0.1

**SPEC-0021: Stage Consistency Validation** - Ensures 4-stage alignment (Planning → Design → Integrate → Build)

| Feature | Description |
|---------|-------------|
| **4-Stage Model** | Stage 01 ↔ 02 ↔ 03 ↔ 04 consistency validation |
| **Pre/Post Checklists** | Verify alignment before and after implementation |
| **Artifact Hashing** | SHA256 checksums detect post-approval modifications |
| **CLI Commands** | `sdlcctl validate-consistency` automation |
| **CI/CD Integration** | GitHub Actions + GitLab examples |

**Reference**: [SPEC-0021-Stage-Consistency-Validation.md](SPEC-0021-Stage-Consistency-Validation.md)

---

## Contents

```
01-Specification-Standard/
├── README.md                           # This file (start here!)
│
├── Core Templates/
│   ├── SDLC-Specification-Standard.md  # Core spec template (YAML + BDD)
│   ├── DESIGN_DECISIONS.md             # Lightweight ADR template
│   ├── SPEC_DELTA.md                   # Version change tracking
│   └── CONTEXT_AUTHORITY_METHODOLOGY.md  # Dynamic AGENTS.md patterns
│
├── Governance Specifications/
│   └── SPEC-0021-Stage-Consistency-Validation.md  # ⭐ NEW in 6.0.1
│
└── examples/                           # Tier-specific examples
    ├── Example-Spec-LITE.md            # Minimal spec (1-2 people)
    ├── Example-Spec-STANDARD.md        # Standard spec (3-10 people)
    └── Example-Spec-PROFESSIONAL.md    # Full spec (10+ people)
```

> **Note**: OpenSpec analysis and decision records have been archived to `99-Legacy/OpenSpec-Analysis-2026/`.

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
| [CONTEXT_AUTHORITY_METHODOLOGY.md](CONTEXT_AUTHORITY_METHODOLOGY.md) | Dynamic AGENTS.md | P1 | ALL |

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
**Last Updated**: February 1, 2026
**Owner**: CTO + CPO Office
**Framework**: SDLC 6.0.3 (7-Pillar + 2-Section)

***"Consistent specifications enable consistent quality."***
