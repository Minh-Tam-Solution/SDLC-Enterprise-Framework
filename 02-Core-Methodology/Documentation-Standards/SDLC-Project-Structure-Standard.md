# SDLC Project Structure Standard

**Version**: 6.3.0
**SDLC Framework Version**: 6.3.0
**Date**: January 29, 2026
**Status**: ACTIVE
**Authority**: CTO Approved
**Pillar**: 1 (10-Stage Lifecycle) + Pillar 6 (Documentation Permanence)

---

## 1. Overview

This document defines the standard project folder structure for SDLC 6.3.0 compliant projects. It establishes clear separation between:

1. **Documentation Stage Mapping** - `/docs` folders mapped to SDLC lifecycle stages (00-09)
2. **Project Structure Validation** - Root-level code folders validated for presence (NOT stage-mapped)

This separation ensures that documentation follows the 10-stage SDLC lifecycle while code organization remains flexible and technology-agnostic.

---

## 2. Core Principles

### 2.1 Documentation vs Code Separation

| Concept | Folders | Stage Mapping | Validation |
|---------|---------|---------------|------------|
| **Documentation** | `/docs/*` | YES (stages 00-09) | Stage compliance |
| **Code Organization** | `backend/`, `frontend/`, etc. | NO | Presence validation |
| **Configuration** | Root files | NO | Presence validation |

### 2.2 Key Rules

1. **Only `/docs` subfolders are stage-mapped** - Stages 00-09 correspond to SDLC lifecycle phases
2. **`10-archive/` is NOT a stage** - It's a project-level archive folder for legacy documentation
3. **Code folders are technology-agnostic** - `backend/`, `frontend/`, `tools/`, `tests/` are organizational units
4. **Code folders cut across ALL stages** - Development happens throughout the lifecycle, not just in Stage 04 (BUILD)

---

## 3. Documentation Stage Mapping Rules

### 3.1 Standard `/docs` Structure

```
docs/
├── 00-foundation/      # Stage 00: WHY? - Strategic Discovery & Validation
├── 01-planning/        # Stage 01: WHAT? - Requirements & User Stories
├── 02-design/          # Stage 02: HOW? - Architecture & Technical Design
├── 03-integrate/       # Stage 03: How connect? - API Contracts & Third-party Setup
├── 04-build/           # Stage 04: Building right? - Sprint Plans & Dev Docs
├── 05-test/            # Stage 05: Works correctly? - Test Plans & QA Docs
├── 06-deploy/          # Stage 06: Ship safely? - Deployment & Release Docs
├── 07-operate/         # Stage 07: Running reliably? - Operations & Monitoring
├── 08-collaborate/     # Stage 08: Team effective? - Team Docs & Sprint Logs
├── 09-govern/          # Stage 09: Compliant? - Compliance & Strategic Oversight
└── 10-archive/         # Project Archive (NOT a stage) - Legacy/Historical Docs
```

### 3.2 Folder Naming Convention

- **Format**: `{XX}-{stage-name}/` where `XX` is 00-09 (or 10 for archive)
- **Stage name**: lowercase, kebab-case
- **Examples**:
  - `00-foundation/` (correct)
  - `01-planning/` (correct)
  - `00-foundation/` (legacy - supported for backward compatibility)
  - `foundation/` (incorrect - missing stage number)

### 3.3 Legacy Folder Support

For backward compatibility, these legacy folder names are also recognized:

| Legacy Name | Maps To Stage |
|-------------|---------------|
| `docs/00-foundation/` | STAGE_00 |
| `docs/why/` | STAGE_00 |
| `docs/problem/` | STAGE_00 |
| `docs/requirements/` | STAGE_01 |
| `docs/specs/` | STAGE_01 |
| `docs/architecture/` | STAGE_02 |
| `docs/api/` | STAGE_03 |
| `docs/development/` | STAGE_04 |
| `docs/testing/` | STAGE_05 |
| `docs/deployment/` | STAGE_06 |
| `docs/operations/` | STAGE_07 |
| `docs/team/` | STAGE_08 |
| `docs/compliance/` | STAGE_09 |
| `docs/governance/` | STAGE_09 |
| `docs/archive/` | STAGE_10 (archive) |

### 3.4 Per-Stage Legacy Folders

Each stage folder (00-09) MAY contain a `99-legacy/` subfolder for deprecated documentation:

```
docs/
├── 00-foundation/
│   ├── current-docs.md
│   └── 99-legacy/           # Deprecated foundation docs
│       └── old-problem-statement.md
├── 01-planning/
│   ├── requirements.md
│   └── 99-legacy/           # Deprecated planning docs
...
```

**Rule**: Content in `99-legacy/` folders is NOT validated or upgraded.

---

## 4. Root Structure Validation Rules

### 4.1 Standard Root Structure

```
project-root/
├── docs/                    # Documentation (stage-mapped)
├── backend/                 # Backend code (NOT stage-mapped)
│   └── 99-legacy/           # Deprecated backend code (PROFESSIONAL+)
├── frontend/                # Frontend code (NOT stage-mapped)
│   └── 99-legacy/           # Deprecated frontend code (PROFESSIONAL+)
├── tools/                   # Utility scripts (NOT stage-mapped)
│   └── 99-legacy/           # Deprecated tools (PROFESSIONAL+)
├── tests/                   # Test suites (NOT stage-mapped)
├── README.md                # Project overview
├── CLAUDE.md                # AI Assistant context (STANDARD+)
├── .env.example             # Environment template (STANDARD+)
├── docker-compose.yml       # Local dev environment (PROFESSIONAL+)
├── Makefile                 # Build automation (PROFESSIONAL+)
├── .gitignore               # Git ignore rules
└── [other config files]     # package.json, pyproject.toml, etc.
```

### 4.2 Code Folders

Code folders are organizational units that exist **independently of SDLC stages**:

| Folder | Purpose | Stage Mapping |
|--------|---------|---------------|
| `backend/` | Server-side code (Python, Go, Java, etc.) | NONE |
| `frontend/` | Client-side code (React, Vue, Angular, etc.) | NONE |
| `tools/` | Utility scripts, CLI tools, generators | NONE |
| `tests/` | Test suites (unit, integration, e2e) | NONE |
| `mobile/` | Mobile app code (React Native, Flutter, etc.) | NONE |
| `infra/` | Infrastructure as Code (Terraform, Pulumi, etc.) | NONE |

**Important**: These folders are NOT mapped to Stage 04 (BUILD). Code development happens throughout all stages.

### 4.3 Configuration Files

Root-level configuration files are validated for presence but NOT stage-mapped:

| File | Purpose | Required For |
|------|---------|--------------|
| `README.md` | Project overview | ALL tiers |
| `CLAUDE.md` | AI Assistant onboarding context | STANDARD+ |
| `.env.example` | Environment variable template | STANDARD+ |
| `docker-compose.yml` | Local development environment | PROFESSIONAL+ |
| `Makefile` | Build automation commands | PROFESSIONAL+ |
| `.gitignore` | Git ignore rules | ALL tiers |

---

## 5. Tier Matrix

### 5.1 Documentation Requirements by Tier

| Stage Folder | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|--------------|------|----------|--------------|------------|
| `00-foundation/` | Required | Required | Required | Required |
| `01-planning/` | Required | Required | Required | Required |
| `02-design/` | Required | Required | Required | Required |
| `03-integrate/` | Optional | Optional | Required | Required |
| `04-build/` | Required | Required | Required | Required |
| `05-test/` | Optional | Required | Required | Required |
| `06-deploy/` | Optional | Required | Required | Required |
| `07-operate/` | Optional | Optional | Required | Required |
| `08-collaborate/` | Optional | Optional | Required | Required |
| `09-govern/` | Optional | Optional | Required | Required |
| `10-archive/` | Optional | Optional | Optional | Required |
| `99-legacy/` in stages | N/A | Optional | Required | Required |

### 5.2 Root Structure Requirements by Tier

| Item | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|------|------|----------|--------------|------------|
| `README.md` | Required | Required | Required | Required |
| `CLAUDE.md` | Optional | Required | Required | Required |
| `.env.example` | Optional | Required | Required | Required |
| `docker-compose.yml` | Optional | Optional | Required | Required |
| `Makefile` | Optional | Optional | Required | Required |
| `99-legacy/` in code folders | N/A | Optional | Required | Required |

### 5.3 Tier Definitions

| Tier | Team Size | Description |
|------|-----------|-------------|
| **LITE** | 1-2 people | Solo developers, MVPs, prototypes |
| **STANDARD** | 3-10 people | Small teams, startup projects |
| **PROFESSIONAL** | 10-50 people | Medium teams, enterprise projects |
| **ENTERPRISE** | 50+ people | Large organizations, regulated industries |

---

## 6. Validation Behavior

### 6.1 Stage Mapping Validation

When validating `/docs` folder structure:

1. **Detect stage folders** - Match folder names against stage patterns
2. **Map to stages** - Assign STAGE_00 through STAGE_09 (or archive)
3. **Calculate confidence** - Higher for exact matches (e.g., `00-foundation/`), lower for legacy names
4. **Report missing stages** - Based on selected tier requirements

### 6.2 Structure Validation

When validating root structure:

1. **Check code folders** - Verify presence of `backend/`, `frontend/`, etc.
2. **Check required files** - Verify presence based on tier
3. **Check legacy folders** - For PROFESSIONAL+, verify `99-legacy/` in code folders
4. **Report as warnings** - Missing items should NOT block, only warn

### 6.3 Validation Output Format

```json
{
  "stage_mappings": [
    {
      "path": "docs/00-foundation",
      "stage": "STAGE_00",
      "stage_name": "FOUNDATION",
      "confidence": 0.95,
      "status": "found"
    }
  ],
  "structure_validation": {
    "code_folders": {
      "backend": {"found": true, "required_for": "all"},
      "frontend": {"found": true, "required_for": "all"},
      "tools": {"found": false, "required_for": "professional+"}
    },
    "required_files": {
      "README.md": {"found": true, "required_for": "all"},
      "CLAUDE.md": {"found": false, "required_for": "standard+"}
    },
    "compliance_score": null,
    "breakdown": {
      "found": 5,
      "missing": 2,
      "total": 7
    }
  }
}
```

---

## 7. Specifications Location (MANDATORY)

### 7.1 Where to Put Specs?

**All specifications MUST be placed in `02-design/` with proper SPEC-XXXX numbering:**

```
docs/02-design/
├── 01-ADRs/                          # Architecture Decision Records
│   ├── SPEC-0001-ADR-001-Database-Choice.md
│   ├── SPEC-0002-ADR-002-Auth-Strategy.md
│   └── ...
│
├── 14-Technical-Specs/               # Technical Specifications
│   ├── SPEC-0010-Auth-Service.md
│   ├── SPEC-0011-API-Gateway.md
│   ├── SPEC-0012-Event-Bus.md
│   └── ...
│
└── 15-API-Specs/                     # API Specifications (optional subfolder)
    ├── SPEC-0050-REST-API-v1.md
    ├── SPEC-0051-WebSocket-API.md
    └── ...
```

### 7.2 Specification Numbering Convention

```
SPEC-XXXX[-Type]-Name.md

Format:
  SPEC-    : Prefix (mandatory)
  XXXX     : 4-digit sequential number (0001-9999)
  Type     : Optional type (ADR, API, etc.)
  Name     : Descriptive name (kebab-case)

Examples:
  SPEC-0001-ADR-001-Database-Choice.md    # ADR type
  SPEC-0010-Auth-Service.md               # Technical spec
  SPEC-0050-API-User-Management.md        # API spec
```

### 7.3 Numbering Ranges (Recommended)

| Range | Type | Example |
|-------|------|---------|
| `0001-0099` | ADRs (Architecture Decisions) | `SPEC-0001-ADR-001-...` |
| `0100-0499` | Technical Specs (Services) | `SPEC-0100-Auth-Service.md` |
| `0500-0799` | API Specs | `SPEC-0500-REST-API-v1.md` |
| `0800-0999` | Integration Specs | `SPEC-0800-GitHub-Integration.md` |

### 7.4 Anti-Pattern: Specs Outside 02-design

```
# ❌ WRONG - Non-compliant locations
docs/specs/                    # No stage prefix
docs/specifications/           # No stage prefix
docs/04-build/specs/           # Wrong stage (BUILD ≠ DESIGN)
docs/01-planning/specs/        # Wrong stage (PLANNING ≠ DESIGN)

# ✅ CORRECT - Always in 02-design
docs/02-design/01-ADRs/SPEC-0001-*.md
docs/02-design/14-Technical-Specs/SPEC-0100-*.md
docs/02-design/15-API-Specs/SPEC-0500-*.md
```

### 7.5 Rationale

- **Why 02-design?** Specifications define HOW to build, which is Stage 02's purpose
- **Why numbered?** Ensures unique identification, easy referencing, and chronological tracking
- **Why SPEC prefix?** Distinguishes from other documents, enables automated validation

---

## 8. SDLC Compliance Folder (Project Context)

### 8.1 Purpose

Every project implementing SDLC 6.3.0 should have an **SDLC Compliance folder** containing:
- Project-specific summary of the SDLC Framework
- AI context files (CLAUDE.md, AGENTS.md)
- Quick reference for team members (human + AI)

**This folder helps new team members quickly understand the project's SDLC implementation without reading the entire Framework.**

### 8.2 Standard Location: `08-collaborate/01-SDLC-Compliance/`

```
docs/08-collaborate/
└── 01-SDLC-Compliance/               # SDLC Context for this project
    ├── CLAUDE.md                     # AI assistant context (project-specific)
    ├── AGENTS.md                     # Agent guidelines & boundaries
    ├── PROJECT-CONTEXT.md            # Human-readable quick reference
    ├── COMPLIANCE-CHECKLIST.md       # Progress tracking
    └── FRAMEWORK-SUMMARY.md          # SDLC 6.3.0 summary (optional)
```

### 8.3 Why 08-collaborate (Not 09-govern)?

| Aspect | 08-collaborate | 09-govern |
|--------|----------------|-----------|
| **Primary audience** | Team members (AI + Human) | Leadership, Auditors |
| **Content type** | Context, onboarding, quick reference | Audit trails, compliance reports |
| **Update frequency** | Per sprint/feature | Monthly/Quarterly |
| **SDLC Compliance fits** | ✅ **Yes** - Team context | ❌ No - Not audit material |

**Decision**: SDLC Compliance folder is for **team collaboration** (helping members understand the project), not for **governance audits** (tracking compliance).

### 8.4 Root-Level Symlinks (Recommended)

For convenience, create symlinks at project root to match industry standard (60K+ repos use root-level AGENTS.md):

```bash
# Create symlinks for quick access
ln -s docs/08-collaborate/01-SDLC-Compliance/CLAUDE.md ./CLAUDE.md
ln -s docs/08-collaborate/01-SDLC-Compliance/AGENTS.md ./AGENTS.md
```

**Result:**
```
your-project/
├── CLAUDE.md → docs/08-collaborate/01-SDLC-Compliance/CLAUDE.md
├── AGENTS.md → docs/08-collaborate/01-SDLC-Compliance/AGENTS.md
├── docs/
│   └── 08-collaborate/
│       └── 01-SDLC-Compliance/
│           ├── CLAUDE.md           # Source of truth
│           ├── AGENTS.md           # Source of truth
│           └── ...
└── src/
```

### 8.5 SDLC Compliance Contents

| File | Purpose | Required Tier |
|------|---------|---------------|
| `CLAUDE.md` | AI context: project overview, tech stack, conventions | STANDARD+ |
| `AGENTS.md` | Agent boundaries, tools, permissions | PROFESSIONAL+ |
| `PROJECT-CONTEXT.md` | Human-readable summary (non-technical) | LITE+ |
| `COMPLIANCE-CHECKLIST.md` | SDLC stage completion tracking | STANDARD+ |
| `FRAMEWORK-SUMMARY.md` | SDLC 6.3.0 quick reference | Optional |

### 8.6 Migration for Existing Projects

If your project uses a non-standard location:

```bash
# Old locations (migrate from)
docs/08-collaborate/01-SDLC-Compliance/    # Old folder naming
docs/08-collaborate/02-SDLC-Compliance/    # Old folder naming
docs/09-govern/SDLC-Compliance/                # Wrong stage

# New standard location (migrate to)
docs/08-collaborate/01-SDLC-Compliance/        # Correct
```

---

## 9. Examples

### 9.1 Compliant Project (STANDARD Tier)

```
my-project/
├── docs/
│   ├── 00-foundation/
│   │   └── problem-statement.md
│   ├── 01-planning/
│   │   └── requirements.md
│   ├── 02-design/
│   │   └── architecture.md
│   ├── 04-build/
│   │   └── sprint-plans/
│   ├── 05-test/
│   │   └── test-plan.md
│   └── 06-deploy/
│       └── deployment-guide.md
├── backend/
│   └── app/
├── frontend/
│   └── src/
├── README.md           # Required
├── CLAUDE.md           # Required for STANDARD
├── .env.example        # Required for STANDARD
└── .gitignore
```

**Validation Result**: PASS (all STANDARD tier requirements met)

### 9.2 Non-Compliant Project (PROFESSIONAL Tier)

```
my-project/
├── docs/
│   ├── 00-foundation/
│   ├── 01-planning/
│   └── 02-design/
│   # MISSING: 03-integrate/, 04-build/, 05-test/, 06-deploy/, 07-operate/, 08-collaborate/, 09-govern/
├── backend/
│   # MISSING: 99-legacy/
├── frontend/
│   # MISSING: 99-legacy/
├── README.md
# MISSING: CLAUDE.md, .env.example, docker-compose.yml, Makefile
```

**Validation Result**: WARNINGS
- Missing stage folders: 03-integrate, 04-build, 05-test, 06-deploy, 07-operate, 08-collaborate, 09-govern
- Missing files: CLAUDE.md, .env.example, docker-compose.yml, Makefile
- Missing legacy folders in code directories

---

## 10. Migration Guide

### 10.1 From SDLC 4.x/5.x to 6.3.0

If your project uses old stage names (WHY, WHAT, HOW, BUILD, etc.):

1. **Rename documentation folders**:
   - `docs/why/` → `docs/00-foundation/`
   - `docs/what/` → `docs/01-planning/`
   - `docs/how/` → `docs/02-design/`
   - etc.

2. **Keep code folders unchanged** - `backend/`, `frontend/` are already correct

3. **Add missing files based on tier**:
   - STANDARD+: Add `CLAUDE.md`, `.env.example`
   - PROFESSIONAL+: Add `docker-compose.yml`, `Makefile`

### 10.2 Automated Migration

Use the SDLC CLI migration tool:

```bash
# Analyze current structure
[SDLC CLI] validate --tier standard

# Generate migration plan
[SDLC CLI] migrate --from 5.x --to 6.3.0 --dry-run

# Execute migration
[SDLC CLI] migrate --from 5.x --to 6.3.0
```

---

## 11. Sprint Documentation Structure (Pillar 2 Integration)

### 11.1 Sprint Folder Standard Location

```
docs/
├── 04-build/
│   └── sprints/              # Standard location for sprint docs
│       ├── README.md         # Sprint overview & index
│       ├── SPRINT-001-*.md   # Sprint 1 documents
│       ├── SPRINT-002-*.md   # Sprint 2 documents
│       └── templates/        # Sprint templates
│           ├── SPRINT-PLAN-TEMPLATE.md
│           └── SPRINT-RETROSPECTIVE-TEMPLATE.md
```

### 11.2 Sprint Document Naming Convention

| Document Type | Pattern | Example |
|--------------|---------|---------|
| Sprint Plan | `SPRINT-{XXX}-{PHASE}-{TITLE}.md` | `SPRINT-001-PHASE2-USER-AUTH.md` |
| Sprint Retrospective | `SPRINT-{XXX}-RETRO.md` | `SPRINT-001-RETRO.md` |
| Sprint Review | `SPRINT-{XXX}-REVIEW.md` | `SPRINT-001-REVIEW.md` |
| Sprint Scope Change | `SPRINT-{XXX}-SCOPE-CHANGE-{YY}.md` | `SPRINT-001-SCOPE-CHANGE-01.md` |

### 11.3 Required Sprint Documentation by Tier

| Document | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|----------|------|----------|--------------|------------|
| Sprint Plan | Required | Required | Required | Required |
| Scope Definition | Optional | Required | Required | Required |
| Daily Progress | Optional | Optional | Required | Required |
| Sprint Retrospective | Optional | Required | Required | Required |
| Scope Change Records | Optional | Optional | Required | Required |
| Sprint Metrics | Optional | Optional | Required | Required |

### 11.4 Sprint Plan Validation

Sprint plans MUST contain (validated by SDLC compliance tools):

```markdown
## Required Sections
- [ ] Sprint Goal (clear, measurable)
- [ ] Scope Definition (explicit boundaries)
- [ ] Story List with Story Points
- [ ] Acceptance Criteria per story
- [ ] Dependencies declared
- [ ] Risk Assessment (PROFESSIONAL+)
- [ ] Phase alignment (which phase of Roadmap)
```

### 11.5 Sprint Governance Integration

Per **Pillar 2: Sprint Planning Governance**:

| Stage | Sprint Documentation Requirement |
|-------|----------------------------------|
| 00-FOUNDATION | Project Roadmap with Phase definitions |
| 01-PLANNING | Sprint Plan template customization |
| 02-DESIGN | Sprint scope aligned with design decisions |
| 04-BUILD | Sprint Plan, Daily Progress, Retrospective |
| 09-GOVERN | Sprint Governance compliance records |

**Cross-Reference**:
- [SDLC-Sprint-Governance.md](../Governance-Compliance/SDLC-Sprint-Governance.md)
- [When-Planning-Sprint.md](./Situation-Specific-Guides/When-Planning-Sprint.md)

---

## 12. Related Documents

- [SDLC-Core-Methodology.md](../SDLC-Core-Methodology.md) - 7-Pillar Architecture definition
- [SDLC-Naming-Standards.md](./SDLC-Naming-Standards.md) - File and document naming rules
- [SDLC-Team-Collaboration.md](./SDLC-Team-Collaboration.md) - Team communication and escalation
- [SDLC-Sprint-Governance.md](../Governance-Compliance/SDLC-Sprint-Governance.md) - Pillar 2 governance
- [AI-ONBOARDING-TEMPLATE.md](../../05-Templates-Tools/5-Project-Templates/AI-ONBOARDING-TEMPLATE.md) - CLAUDE.md template

---

## 13. Changelog

### v6.0.1 (January 29, 2026)
- Added Section 7: Specifications Location (MANDATORY)
  - SPEC-XXXX numbering convention
  - Numbering ranges for ADRs, Technical Specs, API Specs
  - Anti-pattern guidance (specs outside 02-design)
- Added Section 8: SDLC Compliance Folder (Project Context)
  - Standardized location: `08-collaborate/01-SDLC-Compliance/`
  - Root-level symlinks recommendation
  - Migration guide for existing projects

### v6.0.0 (January 28, 2026)
- Folder flattening (remove layer 3), version upgrade
- Updated all SDLC version references to 6.0.0
- Aligned with 8-Pillar Architecture (Pillar 7: Quality Assurance System)

### v5.1.3 (January 2026)
- Added Section 9: Sprint Documentation Structure (Pillar 2 Integration)
- Added Sprint folder standard location under `docs/04-build/sprints/`
- Added Sprint document naming conventions
- Added Sprint documentation requirements by tier
- Updated related documents with Sprint Governance references
- Aligned with 7-Pillar Architecture

### v1.0.0 (December 24, 2025)
- Initial release for SDLC 5.1.2
- Defined separation between documentation stage mapping and project structure validation
- Established tier matrix for requirements
- Added backward compatibility for legacy folder names
- Specified validation output format
