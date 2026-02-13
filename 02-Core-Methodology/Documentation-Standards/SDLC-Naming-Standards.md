# SDLC Naming Standards - Universal Framework

**Version**: 6.0.5
**Date**: January 28, 2026
**Status**: MANDATORY ENFORCEMENT
**Authority**: CPO Approved Standard
**Component**: Document Governance Framework (DGF)
**Pillar**: 6 - Documentation Permanence
**Stage**: 08 - COLLABORATE (Documentation Standards)

---

## Table of Contents

1. [Part 1: Overview & Principles](#part-1-overview--principles)
2. [Part 2: Code File Naming Standards](#part-2-code-file-naming-standards)
3. [Part 3: Document Naming Standards](#part-3-document-naming-standards)
4. [Part 4: Folder & Directory Standards](#part-4-folder--directory-standards)
5. [Part 5: Document Header Templates](#part-5-document-header-templates)
6. [Part 6: Archival Standards](#part-6-archival-standards)
7. [Part 7: Enforcement & Validation](#part-7-enforcement--validation)
8. [Part 8: Quick Reference](#part-8-quick-reference)

---

## Part 1: Overview & Principles

### Purpose

This document consolidates **all naming and header standards** for SDLC 6.0.5 Framework:
- Code file naming (Python, TypeScript, migrations)
- Document naming (markdown, documentation)
- Folder structure (10 stages, legacy handling)
- Header templates (active, archived, migration)
- Archival standards (superseded documents)

### Key Principles

```yaml
Principle 1: Permanence
  - Names remain meaningful over time
  - No temporal references in filenames
  - Version information inside documents, not filenames

Principle 2: Discoverability
  - Descriptive names that explain content
  - Consistent conventions across project
  - Searchable and scannable structure

Principle 3: Convention Consistency
  - Python: snake_case
  - TypeScript: camelCase/PascalCase
  - Documentation: kebab-case
  - Folders: NN-kebab-case (numbered stages)

Principle 4: Traceability
  - Clear header metadata
  - Version tracking
  - Authority and ownership documented
```

### Consolidation Note

This document merges four previous standards:
- SDLC-Code-File-Naming-Standards.md → Part 2
- SDLC-Document-Naming-Standards.md → Parts 3-4
- SDLC-Document-Header-Templates.md → Part 5
- ARCHIVAL-HEADER-TEMPLATE.md → Part 6

---

## Part 2: Code File Naming Standards

### 2.1 Python File Standards

**Convention**: snake_case (lowercase with underscores)
**Maximum Length**: 50 characters (excluding .py extension)

```yaml
Correct Examples:
  ✅ models.py
  ✅ views.py
  ✅ user_service.py
  ✅ customer_serializers.py
  ✅ bcc_generator.py
  ✅ orchestrator_workflow.py

Incorrect Examples:
  ❌ UserService.py (PascalCase)
  ❌ user-service.py (kebab-case)
  ❌ userService.py (camelCase)
  ❌ CONSTANTS.py (UPPERCASE - except special cases)
```

#### Python Naming Patterns

```yaml
Service Files:
  Pattern: {entity}_service.py
  Examples: user_service.py, customer_service.py, bcc_service.py

Model Files:
  Pattern: {entity}.py or {entity}_models.py
  Examples: user.py, customer.py, bcc_sequence.py

Repository Files:
  Pattern: {entity}_repository.py
  Examples: user_repository.py, bcc_repository.py

Schema/Serializer Files:
  Pattern: {entity}_schemas.py or {entity}_serializers.py
  Examples: user_schemas.py, customer_serializers.py

Router/API Files:
  Pattern: {entity}_router.py or {entity}_api.py
  Examples: user_router.py, customer_api.py

Test Files:
  Pattern: test_{module}.py
  Examples: test_user_service.py, test_bcc_repository.py
```

### 2.2 TypeScript/JavaScript File Standards

**Convention**: camelCase for files, PascalCase for React components
**Maximum Length**: 50 characters (excluding extension)

```yaml
Regular Files (camelCase):
  ✅ userService.ts
  ✅ customerApi.ts
  ✅ bccGenerator.ts
  ✅ authUtils.ts

React Components (PascalCase):
  ✅ UserProfile.tsx
  ✅ CustomerList.tsx
  ✅ BCCDashboard.tsx
  ✅ LeadForm.tsx

Incorrect Examples:
  ❌ user_service.ts (snake_case)
  ❌ user-service.ts (kebab-case for non-components)
  ❌ userprofile.tsx (lowercase component)
```

#### TypeScript Naming Patterns

```yaml
Service Files:
  Pattern: {entity}Service.ts
  Examples: userService.ts, customerService.ts, authService.ts

API Files:
  Pattern: {entity}Api.ts
  Examples: userApi.ts, customerApi.ts, bccApi.ts

Hook Files:
  Pattern: use{Entity}.ts
  Examples: useAuth.ts, useCustomer.ts, useBCC.ts

Utility Files:
  Pattern: {description}Utils.ts
  Examples: dateUtils.ts, formatUtils.ts, validationUtils.ts

Component Files:
  Pattern: {ComponentName}.tsx
  Examples: UserProfile.tsx, CustomerList.tsx, LeadForm.tsx

Test Files:
  Pattern: {module}.test.ts or {module}.spec.ts
  Examples: userService.test.ts, CustomerList.spec.tsx
```

### 2.3 Alembic Migration Standards

**Convention**: {revision}_{description}.py
**Maximum Length**: 60 characters (excluding .py extension)

```yaml
Good Examples:
  ✅ 001_bcc_sequence_tables.py (23 chars)
  ✅ 20251129_001_create_bpm_schema.py (33 chars)
  ✅ a502ce0d_seed_mtc_data.py (24 chars)

Bad Examples (Too Long):
  ❌ a502ce0d23a7_seed_data_realistic_mtc_nqh_examples.py (52 chars)
  ❌ 20251128_0730_001_create_bpm_service_schema_with_master_process_awareness.py (76 chars)

Description Guidelines:
  ✅ create_user_tables (action-focused)
  ✅ add_bcc_indexes (specific)
  ✅ seed_mtc_data (clear purpose)
  ❌ seed_data_realistic_mtc_nqh_examples (too verbose)
```

### 2.4 Django Migration Standards

**Convention**: {number}_{description}.py
**Maximum Length**: 50 characters (excluding .py extension)

```yaml
Good Examples:
  ✅ 0001_initial.py (14 chars)
  ✅ 0002_add_customer_fields.py (26 chars)
  ✅ 0003_update_tenant_indexes.py (28 chars)

Custom Names (Use --name flag):
  python manage.py makemigrations --name add_bcc_fields
```

### 2.5 Database Naming Standards

**Convention**: snake_case

```yaml
Table Names:
  ✅ users, customers, bcc_records, bcc_sequences

Column Names:
  ✅ user_id, created_at, tenant_id, bcc_code

Index Names:
  ✅ ix_users_tenant_id
  ✅ ix_bcc_records_bcc_code
  ✅ uq_bcc_sequence_tenant_mp_year_month
```

---

## Part 3: Document Naming Standards

### 3.1 Document Convention: Kebab-Case

Documentation files (.md) MUST use kebab-case.

```yaml
Correct:
  ✅ Customer-Portal-Design.md
  ✅ DNA-Framework-API.md
  ✅ Database-Migration-Guide.md

Incorrect:
  ❌ customer_portal_design.md (snake_case)
  ❌ CustomerPortalDesign.md (PascalCase)
  ❌ customerportaldesign.md (lowercase)
```

### 3.2 Prohibited Patterns (CRITICAL)

**ABSOLUTELY FORBIDDEN in Document Names:**

```yaml
Sprint References:
  ❌ SPRINT-7, SPRINT-X, Sprint7
  ❌ Any sprint number or identifier

Day/Date References:
  ❌ DAY-1, DAY-X, Day1
  ❌ 2025-09-27, Sep27, 27Sep
  ❌ TODAY, YESTERDAY, TOMORROW

Phase References:
  ❌ PHASE-1, PHASE-X, Phase1
  ❌ ALPHA, BETA, RC, GA

Version in Filename:
  ❌ V8.0, V7.5, v2, version2
  ❌ Rev1, Revision2

Team References:
  ❌ LOCAL-TEAM, REMOTE-TEAM
  ❌ BACKEND-TEAM, FRONTEND-TEAM

Temporary Markers:
  ❌ TEMP, TMP, TEST, DRAFT
  ❌ WIP, TODO, FIXME
  ❌ OLD, NEW, LATEST, FINAL

Person Names:
  ❌ John-API-Design.md
  ❌ CTO-Database-Schema.md
```

**Why These Are Forbidden:**
- Sprint references become meaningless after sprint ends
- Date stamps make documents appear outdated
- Phase references lose relevance after phase completion
- Version numbers belong in content, not filenames
- Team references don't indicate content purpose
- Temporary markers create confusion about document status
- Person names create ownership confusion

### 3.3 Document Naming Patterns

#### Design Documents
**Location**: `/docs/02-Design-Architecture/[subdomain]/`

```yaml
Pattern: Feature-Component-Type.md

Examples:
  ✅ Authentication-API-Design.md
  ✅ Customer-Portal-UI-Design.md
  ✅ Database-Schema-Design.md
  ✅ DNA-Framework-Architecture.md

Incorrect:
  ❌ SPRINT-7-Authentication-API.md
  ❌ Authentication-API-V8.0.md
  ❌ Authentication-FINAL.md
```

#### Technical Documentation
**Location**: `/docs/04-build/[category]/`

```yaml
Pattern: Technology-Purpose.md

Examples:
  ✅ React-Component-Guidelines.md
  ✅ Django-Best-Practices.md
  ✅ Performance-Optimization-Guide.md
```

#### API Documentation
**Location**: `/docs/03-integrate/api-contracts/`

```yaml
Pattern: Service-API-Documentation.md

Examples:
  ✅ Authentication-API-Documentation.md
  ✅ Customer-API-Documentation.md
  ✅ Webhook-Integration-Guide.md
```

#### Sprint Documents (EXCEPTION)
**Location**: `/docs/08-collaborate/sprint-logs/`

```yaml
ONLY HERE can sprint references be used:
  ✅ SPRINT-[number]-Planning.md
  ✅ SPRINT-[number]-Retrospective.md
  ✅ SPRINT-[number]-Review.md
  ✅ SPRINT-[number]-Completion.md
```

### 3.4 Document Naming Best Practices

```yaml
Use Kebab-Case:
  ✅ Customer-Portal-Design.md
  ❌ customer_portal_design.md

Be Descriptive and Specific:
  ✅ Payment-Gateway-Integration.md
  ❌ Payment.md (too vague)

Use Full Words:
  ✅ Authentication-Service.md
  ❌ Auth-Svc.md (abbreviated)

Feature-Based Naming:
  ✅ Customer-Management-System.md (describes WHAT)
  ❌ Sprint-7-Customer-Work.md (describes WHEN)
  ❌ John-Customer-Design.md (describes WHO)

No Status Markers (version goes INSIDE):
  ✅ API-Design.md (with version: 4.7 inside)
  ❌ API-Design-FINAL.md
  ❌ API-Design-v2.md
```

---

## Part 4: Folder & Directory Standards

### 4.1 Stage Folders (Level 1) - SDLC 6.0.5

**10 Stages (00-09)** - exactly 10 stages:

```yaml
Pattern: NN-shortname/

Stages:
  00-foundation/    # WHY - Design Thinking + Business Case
  01-planning/      # WHAT - Requirements + User Stories
  02-design/        # HOW - Architecture + ADRs
  03-integrate/     # INTEGRATE - API Contracts + Third-party
  04-build/         # BUILD - Development + Sprint Plans
  05-test/          # TEST - QA + Test Reports
  06-deploy/        # DEPLOY - Release + Deployment Guides
  07-operate/       # OPERATE - Runbooks + Monitoring
  08-collaborate/   # COLLABORATE - Team + Training
  09-govern/        # GOVERN - Compliance + Executive Reports
```

### 4.2 Legacy/Archive Folders

```yaml
Structure:
  docs/
  ├── 00-foundation/
  │   └── 99-legacy/     # Legacy docs for this stage
  ├── 01-planning/
  │   └── 99-legacy/
  ├── ... (each stage 00-09 has its own 99-legacy/)
  ├── 09-govern/
  │   └── 99-legacy/
  └── 10-archive/        # Project-level archive (NOT a stage)

  backend/
  └── 99-legacy/         # Legacy code/docs in backend

  frontend/
  └── 99-legacy/         # Legacy code/docs in frontend

Rules:
  - 10-archive: ONLY at docs root (holds unsorted legacy docs)
  - 99-legacy: within EACH stage (00-09) AND in code folders
  - Never validate/upgrade content in legacy/archive folders
```

### 4.3 Subdirectories (Level 2+)

```yaml
Pattern: NN-Feature-Category/

Examples:
  01-System-Architecture/
  02-Database-Design/
  03-API-Design/
  04-UI-UX-Design/
  99-legacy/  (lowercase for archive)
```

---

## Part 5: Document Header Templates

### 5.1 Active Document Header

Apply to **all active SDLC 6.0.5 documents**:

```markdown
# [Document Title]
## [Subtitle - Purpose]

**Version**: 6.0.5
**Date**: January 28, 2026
**Status**: ACTIVE - [Specific Status]
**Authority**: [Who Approved]
**Pillar**: [Pillar Number] - [Pillar Name]
**Stage**: [Stage Number] - [Stage Name]
**Foundation**: [What This Builds On - Optional]
**Enhancement**: [What's New - Optional]

---

[Document content starts here]
```

#### Header Field Definitions

```yaml
Version:
  Format: MAJOR.MINOR.PATCH (e.g., 5.3.0)
  Rule: Always use current framework version for active docs

Date:
  Format: Month DD, YYYY (e.g., January 28, 2026)
  Rule: Update when major content changes

Status:
  Format: ACTIVE - [Context]
  Examples:
    - ACTIVE - PRODUCTION READY
    - ACTIVE - ESSENTIAL FOR 10x PRODUCTIVITY
    - ACTIVE - BATTLE-TESTED PATTERNS

Authority:
  Examples:
    - CEO + CPO + CTO Leadership
    - CTO Technical Review
    - CPO Office (email)

Pillar (Optional):
  Format: [Number] - [Name]
  Examples:
    - Pillar 2 - Sprint Planning Governance
    - Pillar 6 - Documentation Permanence

Stage (Optional):
  Format: [Number] - [Name]
  Examples:
    - Stage 02 - Core Methodology
    - Stage 08 - COLLABORATE
```

### 5.2 Archived Document Header

Apply to **documents superseded** by newer versions:

```markdown
# [Document Title]

**ARCHIVAL STATUS**: 🔒 ARCHIVED (READ-ONLY)
**Original Version**: [Version Tag]
**Superseded By**: [Active Version Doc Reference]
**Archival Date**: [Month DD, YYYY]
**Archive Location**: [Path to Archive]
**Reason**: [Why Archived]

---

## ⚠️ ARCHIVE NOTICE

This document has been **archived** and is **READ-ONLY**. For current active version, see:
- **Active Version**: [Link to Active Document]
- **Migration Guide**: [Link to Migration Guide if applicable]

**When to Reference This Archive**:
- Historical context and evolution understanding
- Version comparison studies
- Research on methodology origins

**Do NOT Use This Archive For**:
- New implementations (use active SDLC 5.3.0)
- Active projects (upgrade to current version)
- Team training (use current materials)

---

**Original Document Content Below (Preserved As-Is)**

[Original document content - UNMODIFIED]
```

### 5.3 Migration Document Header

Apply to **version migration guides**:

```markdown
# Migration Guide: SDLC [Old Version] → [New Version]

**Version**: [New Version]
**Date**: [Migration Date]
**Status**: ACTIVE - MIGRATION GUIDE
**Source**: SDLC [Old Version]
**Target**: SDLC [New Version]
**Timeline**: [Estimated Migration Time]
**Disruption**: [None|Minimal|Moderate]

---

## 🎯 Migration Summary

**Migration Type**: [Enhancement|Replacement|Consolidation]
**Breaking Changes**: [Yes|No]
**Backward Compatible**: [Yes|No]
**Estimated Time**: [Time estimate]

---

[Migration guide content]
```

---

## Part 6: Archival Standards

### 6.1 Archival Header Template (Detailed)

Apply unmodified at the very top of any superseded document:

```text
ARCHIVAL STATUS: ARCHIVED (READ-ONLY)
ORIGINAL VERSION: <VERSION TAG>
SUPERSEDED BY: <ACTIVE VERSION DOC REF>
ARCHIVAL DATE: <YYYY-MM-DD>
RETENTION CATEGORY: {REGULATORY|AUDIT|HISTORICAL|REFERENCE}
CHANGE TYPE: {RESTRUCTURE|ELEVATION|DEPRECATION|MERGE}
AUTHORIZATION: <ROLE / APPROVER>
INTEGRITY HASH: <PLACEHOLDER_SHA256_OR_PENDING>
TRACEABILITY LINK: <JIRA/WORK ITEM/CHANGE REQUEST ID>
NOTES: <SHORT CONTEXT – WHY RETAINED>
```

### 6.2 Archival Usage Rules

```yaml
Core Rules:
  - Do not edit archived body content except to insert header
  - If partial extraction, mark with "BEGIN LEGACY BLOCK <ID>" / "END LEGACY BLOCK <ID>"
  - For merged content, include mapping table referencing new locations

Mapping Table Example:
  | Legacy Element | New Location | Status | Notes |
  |----------------|--------------|--------|-------|
  | SDLC 6.0.5 Sprint Governance | SDLC-Sprint-Governance.md | Merged | Consolidated 3 files |
```

### 6.3 Archival Anti-Patterns

```yaml
Anti-Patterns to AVOID:
  ❌ Copying active content into legacy file (duplication drift risk)
  ❌ Editing legacy text to match new terminology (breaks historical evidence)
  ❌ Removing rationale/context sections
  ❌ Updating archived content without archival header

Correct Approach:
  ✅ Add archival header only
  ✅ Preserve original content exactly as-is
  ✅ Link to active version
  ✅ Include migration decision log if complex
```

---

## Part 7: Enforcement & Validation

### 7.1 Pre-Commit Hooks

```python
# Pre-commit hook example for document names
def validate_document_name(filename):
    forbidden_patterns = [
        r'SPRINT-\d+', r'DAY-\d+', r'PHASE-\d+',
        r'V\d+\.\d+', r'v\d+', r'TEAM',
        r'TEMP', r'DRAFT', r'FINAL', r'TEST'
    ]

    for pattern in forbidden_patterns:
        if re.search(pattern, filename, re.IGNORECASE):
            raise ValueError(f"Forbidden pattern '{pattern}' in {filename}")

    return True
```

### 7.2 Code Review Checklist

**For Code Files:**
- [ ] Python files use snake_case
- [ ] TypeScript files use camelCase/PascalCase
- [ ] File names ≤50 characters
- [ ] Alembic migrations ≤60 characters

**For Documentation Files:**
- [ ] Uses kebab-case
- [ ] No sprint/day/phase references
- [ ] No version numbers in filename
- [ ] No team/person names
- [ ] No temporary markers
- [ ] Descriptive and permanent

**For Document Headers:**
- [ ] Version is 6.0.2 (or current)
- [ ] Date is current
- [ ] Status clearly stated
- [ ] Authority/ownership documented
- [ ] For archived: archival header complete

### 7.3 Violation Consequences

```yaml
Enforcement Levels:
  1. First violation: Immediate correction required
  2. Pattern violations: Additional training
  3. Continued violations: Performance review impact

Automation (Future):
  - Pre-commit blocks non-compliant names
  - CI/CD validates naming conventions
  - Quarterly audit of naming compliance
```

---

## Part 8: Quick Reference

### Code File Summary

| File Type | Convention | Max Length | Example |
|-----------|------------|------------|---------|
| Python (.py) | snake_case | 50 chars | user_service.py |
| TypeScript (.ts) | camelCase | 50 chars | userService.ts |
| React Component (.tsx) | PascalCase | 50 chars | UserProfile.tsx |
| Alembic Migration | {rev}_{desc} | 60 chars | 001_create_users.py |
| Django Migration | {num}_{desc} | 50 chars | 0001_initial.py |
| Database Tables | snake_case | 63 chars | bcc_records |
| Database Columns | snake_case | 63 chars | tenant_id |

### Document File Summary

| File Type | Convention | Prohibited | Example |
|-----------|------------|------------|---------|
| Markdown (.md) | kebab-case | Sprint/Day/Version | User-Guide.md |
| README | UPPERCASE | N/A | README.md |
| CLAUDE/AGENTS | UPPERCASE | N/A | CLAUDE.md |

### Header Quick Templates

**Active Document (Minimal):**
```markdown
# Document Title

**Version**: 6.0.5
**Date**: January 28, 2026
**Status**: ACTIVE - [Context]
**Authority**: [Owner]

---
```

**Archived Document (Minimal):**
```markdown
# Document Title

**ARCHIVAL STATUS**: 🔒 ARCHIVED (READ-ONLY)
**Original Version**: [Old Version]
**Superseded By**: [New Document]
**Archival Date**: January 28, 2026

---

## ⚠️ ARCHIVE NOTICE
See: [Link to Active Version]

---

[Original content - UNMODIFIED]
```

### DO's and DON'Ts

```yaml
DO's ✅:
  - Use consistent conventions
  - Be descriptive
  - Focus on content
  - Use full words
  - Keep it permanent
  - Update headers when content changes

DON'Ts ❌:
  - No sprint numbers
  - No dates/days in names
  - No versions in names
  - No team names
  - No status markers
  - No person names
  - No editing archived content
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 6.0.0 | Jan 28, 2026 | Folder flattening (remove layer 3), version upgrade |
| 5.3.0 | Jan 28, 2026 | Consolidated from 4 files (Code, Document, Header, Archival) |
| 5.0.0 | Dec 5, 2025 | Initial SDLC 5.0.0 versions |
| 4.9.1 | Nov 29, 2025 | Restored from SDLC 4.3/4.4 |

---

## Related Documents

- [SDLC-Core-Methodology.md](../SDLC-Core-Methodology.md) - 8-Pillar Architecture
- [SDLC-Project-Structure-Standard.md](./SDLC-Project-Structure-Standard.md) - Folder structure
- [SDLC-Tier-Stage-Requirements.md](./SDLC-Tier-Stage-Requirements.md) - Tier requirements

---

**Document Status**: ACTIVE - MANDATORY ENFORCEMENT
**Compliance**: Required for all SDLC 6.0.5 projects
**Last Updated**: January 28, 2026
**Owner**: CPO Office

---

*"Permanent names for permanent value."* 📂
*"Every document tells its story through its header."* ✨
