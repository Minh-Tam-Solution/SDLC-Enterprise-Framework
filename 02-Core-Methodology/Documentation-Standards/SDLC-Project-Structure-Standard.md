# SDLC Project Structure Standard

**Version**: 1.0.0
**SDLC Framework Version**: 5.1.2
**Date**: December 24, 2025
**Status**: ACTIVE
**Authority**: CTO Approved

---

## 1. Overview

This document defines the standard project folder structure for SDLC 5.1.2 compliant projects. It establishes clear separation between:

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
  - `00-Project-Foundation/` (legacy - supported for backward compatibility)
  - `foundation/` (incorrect - missing stage number)

### 3.3 Legacy Folder Support

For backward compatibility, these legacy folder names are also recognized:

| Legacy Name | Maps To Stage |
|-------------|---------------|
| `docs/00-Project-Foundation/` | STAGE_00 |
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

## 7. Examples

### 7.1 Compliant Project (STANDARD Tier)

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

### 7.2 Non-Compliant Project (PROFESSIONAL Tier)

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

## 8. Migration Guide

### 8.1 From SDLC 4.x to 5.1.2

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

### 8.2 Automated Migration

Use `sdlcctl migrate` command:

```bash
# Analyze current structure
sdlcctl validate --tier standard

# Generate migration plan
sdlcctl migrate --from 4.x --to 5.1.2 --dry-run

# Execute migration
sdlcctl migrate --from 4.x --to 5.1.2
```

---

## 9. Related Documents

- [SDLC-Core-Methodology.md](../SDLC-Core-Methodology.md) - 10-stage lifecycle definition
- [SDLC-Document-Naming-Standards.md](./SDLC-Document-Naming-Standards.md) - File naming rules
- [SDLC-Code-File-Naming-Standards.md](./SDLC-Code-File-Naming-Standards.md) - Code file naming rules
- [AI-ONBOARDING-TEMPLATE.md](../../03-Templates-Tools/5-Project-Templates/AI-ONBOARDING-TEMPLATE.md) - CLAUDE.md template

---

## 10. Changelog

### v1.0.0 (December 24, 2025)
- Initial release for SDLC 5.1.2
- Defined separation between documentation stage mapping and project structure validation
- Established tier matrix for requirements
- Added backward compatibility for legacy folder names
- Specified validation output format
