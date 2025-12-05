# SDLC Code File Naming Standards - Universal Framework

**Version**: 5.0.0
**Date**: December 5, 2025
**Status**: MANDATORY ENFORCEMENT
**Authority**: CPO Approved Standard
**Component**: Document Governance Framework (DGF)
**Stage**: 08 - COLLABORATE (Documentation Standards)

---

## 1. Overview

This document defines code file naming standards for all SDLC 5.0 projects. These standards were originally restored from SDLC 4.3/4.4, enhanced for SDLC 4.9.1, and now upgraded for SDLC 5.0.0 compliance with Governance & Compliance Integration.

**CPO Gap Analysis Reference**: CPO-CODE-FILE-NAMING-STANDARDS-GAP-ANALYSIS-NOV29-2025.md

**Version History Note**: These standards were restored from SDLC 4.3/4.4 (November 2025) and upgraded to SDLC 5.0.0 (December 2025) with enhanced enforcement guidelines.

---

## 2. Python File Naming Standards

### 2.1 Convention: snake_case

All Python files MUST use lowercase with underscores (snake_case).

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

### 2.2 Maximum Length: 50 Characters

Python file names (excluding `.py` extension) MUST NOT exceed 50 characters.

```yaml
Length Examples:
  ✅ customer_cultural_intelligence.py (32 chars) - GOOD
  ✅ bcc_generation_service.py (21 chars) - GOOD
  ⚠️ customer_cultural_intelligence_serializers.py (45 chars) - ACCEPTABLE
  ❌ a502ce0d23a7_seed_data_realistic_mtc_nqh_examples.py (52 chars) - TOO LONG
  ❌ very_long_descriptive_name_that_exceeds_fifty_chars.py (52 chars) - TOO LONG
```

### 2.3 Naming Patterns

```yaml
Service Files:
  Pattern: {entity}_service.py
  Examples:
    - user_service.py
    - customer_service.py
    - bcc_service.py

Model Files:
  Pattern: {entity}.py or {entity}_models.py
  Examples:
    - user.py
    - customer.py
    - bcc_sequence.py

Repository Files:
  Pattern: {entity}_repository.py
  Examples:
    - user_repository.py
    - bcc_repository.py

Schema/Serializer Files:
  Pattern: {entity}_schemas.py or {entity}_serializers.py
  Examples:
    - user_schemas.py
    - customer_serializers.py

Router/API Files:
  Pattern: {entity}_router.py or {entity}_api.py
  Examples:
    - user_router.py
    - customer_api.py

Test Files:
  Pattern: test_{module}.py
  Examples:
    - test_user_service.py
    - test_bcc_repository.py
    - test_models.py
```

---

## 3. TypeScript/JavaScript File Naming Standards

### 3.1 Convention: camelCase for Files, PascalCase for Components

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

### 3.2 Maximum Length: 50 Characters

TypeScript/JavaScript file names (excluding extension) MUST NOT exceed 50 characters.

### 3.3 Naming Patterns

```yaml
Service Files:
  Pattern: {entity}Service.ts
  Examples:
    - userService.ts
    - customerService.ts
    - authService.ts

API Files:
  Pattern: {entity}Api.ts
  Examples:
    - userApi.ts
    - customerApi.ts
    - bccApi.ts

Hook Files:
  Pattern: use{Entity}.ts
  Examples:
    - useAuth.ts
    - useCustomer.ts
    - useBCC.ts

Utility Files:
  Pattern: {description}Utils.ts
  Examples:
    - dateUtils.ts
    - formatUtils.ts
    - validationUtils.ts

Component Files (React):
  Pattern: {ComponentName}.tsx
  Examples:
    - UserProfile.tsx
    - CustomerList.tsx
    - LeadForm.tsx

Test Files:
  Pattern: {module}.test.ts or {module}.spec.ts
  Examples:
    - userService.test.ts
    - CustomerList.spec.tsx
```

---

## 4. Alembic Migration File Standards

### 4.1 Convention: {revision}_{description}.py

Alembic migration files have a special format due to auto-generation.

```yaml
Format: {revision_id}_{short_description}.py
Maximum Length: 60 characters (excluding .py extension)

Good Examples:
  ✅ 001_bcc_sequence_tables.py (23 chars)
  ✅ 20251129_001_create_bpm_schema.py (33 chars)
  ✅ a502ce0d_seed_mtc_data.py (24 chars)

Bad Examples (Too Long):
  ❌ a502ce0d23a7_seed_data_realistic_mtc_nqh_examples.py (52 chars)
  ❌ 20251128_0730_001_create_bpm_service_schema_with_master_process_awareness.py (76 chars)
```

### 4.2 Description Guidelines

```yaml
Description Rules:
  - Use short, descriptive phrases
  - Avoid "and_more" suffixes
  - Use abbreviations when necessary
  - Focus on the main change

Good Descriptions:
  ✅ create_user_tables
  ✅ add_bcc_indexes
  ✅ seed_mtc_data
  ✅ update_customer_schema

Bad Descriptions:
  ❌ seed_data_realistic_mtc_nqh_examples (too verbose)
  ❌ rename_customers_tenant_active_idx_customers_tenant__3f74d3_idx_and_more (too long)
```

---

## 5. Django Migration File Standards

### 5.1 Convention: {number}_{description}.py

Django auto-generates migration names, but descriptions can be customized.

```yaml
Format: {migration_number}_{short_description}.py
Maximum Length: 50 characters (excluding .py extension)

Good Examples:
  ✅ 0001_initial.py (14 chars)
  ✅ 0002_add_customer_fields.py (26 chars)
  ✅ 0003_update_tenant_indexes.py (28 chars)

Bad Examples (Auto-generated, Too Long):
  ❌ 0002_rename_customers_tenant_active_idx_customers_tenant__3f74d3_idx_and_more.py (80 chars)
  ❌ 0004_alter_user_managers_user_is_active_user_is_staff_and_more.py (65 chars)
```

### 5.2 Custom Migration Names

When creating migrations manually, use the `--name` flag:

```bash
# Good: Custom short name
python manage.py makemigrations --name add_bcc_fields

# Bad: Let Django auto-generate (often too long)
python manage.py makemigrations  # Results in long auto-names
```

---

## 6. Documentation File Naming Standards

### 6.1 Convention: Kebab-Case

Documentation files (.md) MUST use kebab-case.

```yaml
Correct Examples:
  ✅ user-guide.md
  ✅ api-reference.md
  ✅ sprint-42-plan.md
  ✅ CLAUDE.md (special file - uppercase allowed)

Incorrect Examples:
  ❌ user_guide.md (snake_case)
  ❌ UserGuide.md (PascalCase)
  ❌ userguide.md (lowercase concatenated)
```

**Reference**: See SDLC-Document-Naming-Standards.md for complete documentation standards.

---

## 7. Database Naming Standards

### 7.1 Convention: snake_case

```yaml
Table Names:
  ✅ users
  ✅ customers
  ✅ bcc_records
  ✅ bcc_sequences

Column Names:
  ✅ user_id
  ✅ created_at
  ✅ tenant_id
  ✅ bcc_code

Index Names:
  ✅ ix_users_tenant_id
  ✅ ix_bcc_records_bcc_code
  ✅ uq_bcc_sequence_tenant_mp_year_month
```

---

## 8. Enforcement

### 8.1 Pre-Commit Hooks (Future Enhancement)

```yaml
Pre-Commit Validation:
  - Check file name length (max 50 chars for code, 60 for Alembic)
  - Check naming convention (snake_case for Python)
  - Block commits with violations
  - Report violations with suggestions

Configuration: .pre-commit-config.yaml
```

### 8.2 Code Review Checklist

During code review, verify:
- [ ] Python files use snake_case
- [ ] TypeScript files use camelCase/PascalCase
- [ ] File names ≤50 characters
- [ ] Alembic migrations ≤60 characters
- [ ] Documentation files use kebab-case

---

## 9. Quick Reference

| File Type | Convention | Max Length | Example |
|-----------|------------|------------|---------|
| Python (.py) | snake_case | 50 chars | user_service.py |
| TypeScript (.ts) | camelCase | 50 chars | userService.ts |
| React Component (.tsx) | PascalCase | 50 chars | UserProfile.tsx |
| Alembic Migration | {rev}_{desc} | 60 chars | 001_create_users.py |
| Django Migration | {num}_{desc} | 50 chars | 0001_initial.py |
| Documentation (.md) | kebab-case | No limit | user-guide.md |
| Database Tables | snake_case | 63 chars | bcc_records |
| Database Columns | snake_case | 63 chars | tenant_id |

---

## 10. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 5.0.0 | Dec 5, 2025 | SDLC Framework Team | Upgraded for SDLC 5.0.0 - Governance & Compliance Integration |
| 4.9.1 | Nov 29, 2025 | SDLC Framework Team | Initial version - Restored from SDLC 4.3/4.4, enhanced for SDLC 4.9.1 |

---

**SDLC 5.0.0**: Stage 08 (Documentation Standards)
**Component**: Document Governance Framework (DGF)
**Compliance**: MANDATORY for all code files
**English-Only**: MANDATORY

---

*This document defines code file naming standards for all SDLC 5.0 projects.*
*Originally restored from SDLC 4.3/4.4, enhanced for SDLC 4.9.1, upgraded for SDLC 5.0.0.*
*SDLC 5.0.0: Complete standards with enhanced enforcement and Governance & Compliance Integration.*
