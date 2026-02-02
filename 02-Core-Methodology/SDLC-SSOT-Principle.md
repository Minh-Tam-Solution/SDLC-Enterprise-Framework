# SSOT Principle (Single Source of Truth) - SDLC 6.0.2

**Version**: 1.0.0
**Date**: February 2, 2026
**Status**: ACTIVE
**Framework**: SDLC 6.0.2
**Purpose**: Define and enforce Single Source of Truth across all SDLC stages

---

## Definition

**SSOT (Single Source of Truth)**: Each artifact type must have exactly **ONE** canonical source in the project structure. All other references must be symlinks, imports, or cross-references—never copies.

**Core Principle**:
```
1 Artifact Type = 1 Canonical Location = 1 File
All other locations → Symlink or Reference
```

---

## Why SSOT Matters

### Problem: Without SSOT

```
project/
├── backend/openapi.json          ← Version 1.2.0
├── docs/api/openapi.json         ← Version 1.1.0 (outdated copy)
├── frontend/openapi.json         ← Version 1.2.1 (manual edit, never synced)
└── tests/openapi.json            ← Version 1.0.0 (ancient copy)
```

**Consequences**:
- ❌ **Drift**: 4 versions of the same file, all different
- ❌ **Update Burden**: Change 1 endpoint = update 4 files manually
- ❌ **Truth Ambiguity**: Which version is correct?
- ❌ **Test Failures**: Tests use outdated schema → false negatives/positives
- ❌ **Client Breakage**: SDK generated from wrong version → production bugs

**Real-World Impact**:
> "We spent 6 hours debugging a test failure, only to discover frontend was using openapi.json v1.1.0 while backend was v1.2.0. The API worked fine, but tests failed because schemas didn't match." — NQH-Bot Crisis (2024)

### Solution: With SSOT

```
project/
├── docs/03-integrate/02-API-Specifications/
│   └── openapi.json              ← ✅ CANONICAL SOURCE (v1.2.0)
│
├── backend/
│   └── openapi.json → symlink    ← Points to canonical
├── frontend/
│   └── openapi.json → symlink    ← Points to canonical
└── tests/
    └── openapi.json → symlink    ← Points to canonical
```

**Benefits**:
- ✅ **No Drift**: Update canonical → all consumers get update instantly
- ✅ **Update Once**: Change 1 endpoint = update 1 file
- ✅ **Truth Clarity**: Canonical location is documented and known
- ✅ **Test Reliability**: All tests use same schema version
- ✅ **Client Consistency**: SDK generation always uses latest spec

---

## SSOT by Artifact Type

### 1. API Specification (OpenAPI/Swagger)

**Canonical Location**: `docs/03-integrate/02-API-Specifications/openapi.json`

**Generation**:
```bash
# Auto-generate from backend code (FastAPI, Express, Spring Boot)
python3 scripts/generate_openapi.py > docs/03-integrate/02-API-Specifications/openapi.json
```

**Consumers** (symlinks or imports):
- Backend: `import json; spec = json.load(open("docs/03-integrate/.../openapi.json"))`
- Frontend: Symlink for SDK generation
- Tests: Load from canonical location

**Validation**:
```bash
# Detect duplicates
find . -name "openapi.json" -type f
# Expected: EXACTLY 1 file in docs/03-integrate/

# CI/CD gate (block PR if duplicates found)
duplicates=$(find . -name "openapi.json" -type f | wc -l)
if [ "$duplicates" -gt 1 ]; then
  echo "🔴 SSOT violation: Duplicate openapi.json files"
  exit 1
fi
```

---

### 2. Database Schema (ERD)

**Canonical Location**: `docs/01-planning/04-Data-Model/Data-Model-ERD.md`

**Generation**: Manual design → Markdown ERD
**Consumers**:
- Alembic migrations: Reference ERD for schema design
- ORM models (SQLAlchemy, Prisma): Implement ERD design
- Tests: Validate actual schema matches ERD

**Validation**:
```bash
# Check ERD exists
test -f docs/01-planning/04-Data-Model/Data-Model-ERD.md

# Verify ORM models match ERD
python3 scripts/validate_schema_consistency.py
```

---

### 3. Environment Variables

**Canonical Location**: `.env.example` (repo root)

**Derivations** (not duplicates):
- `.env.development` (local only, gitignored)
- `.env.staging` (CI/CD only, gitignored)
- `.env.production` (secrets manager, gitignored)

**All environments** reference `.env.example` for structure.

**Validation**:
```bash
# Check .env.example is complete
diff <(sort .env.example) <(sort .env.development | grep -v "^#")
# Expected: All keys in .env.development exist in .env.example
```

---

### 4. API Endpoint List (Human-Readable)

**Canonical Location**: `docs/03-integrate/02-API-Specifications/COMPLETE-API-ENDPOINT-REFERENCE.md`

**Generation**: Auto-generated from openapi.json (SSOT)
```bash
python3 scripts/generate_api_reference.py
```

**Consumers**:
- Developers: Read for API overview
- Documentation site: Embed or link

**Validation**:
```bash
# Ensure auto-generated (not manually edited)
grep "Auto-Generated from OpenAPI Specification" COMPLETE-API-ENDPOINT-REFERENCE.md
```

---

### 5. Configuration Files (ESLint, Prettier, TypeScript)

**Canonical Locations**:
- `.eslintrc.json` (repo root)
- `.prettierrc.json` (repo root)
- `tsconfig.json` (repo root)

**Derivations** (extends canonical):
```json
// apps/frontend/tsconfig.json
{
  "extends": "../../tsconfig.json",  // ← Extends SSOT
  "compilerOptions": {
    "outDir": "./dist"  // ← Project-specific only
  }
}
```

**Validation**:
```bash
# Check all TypeScript configs extend root
find . -name "tsconfig.json" ! -path "./node_modules/*" -exec grep -L "extends" {} \;
# Expected: Only root tsconfig.json
```

---

## SSOT Enforcement Strategies

### Strategy 1: Symlinks (Filesystem-Level)

**When to Use**: Binary files, JSON, YAML that need to exist in multiple locations

**Example**:
```bash
# Create symlink from frontend to canonical OpenAPI spec
cd frontend/
ln -sf ../docs/03-integrate/02-API-Specifications/openapi.json openapi.json

# Verify symlink
ls -la openapi.json
# Expected: openapi.json -> ../docs/03-integrate/...
```

**Pros**:
- ✅ Automatic sync (no manual update needed)
- ✅ Filesystem enforces SSOT

**Cons**:
- ❌ Symlinks break on Windows (use Git symlink support or WSL)
- ❌ Adds Git complexity (must commit symlink itself)

---

### Strategy 2: Build-Time Copy (Automation)

**When to Use**: Files needed in specific locations for tooling (e.g., Swagger UI)

**Example**:
```bash
# package.json script
{
  "scripts": {
    "copy-openapi": "cp docs/03-integrate/02-API-Specifications/openapi.json public/openapi.json"
  }
}

# Run on build (never commit copy)
```

**Pros**:
- ✅ Works on all OS (no symlink issues)
- ✅ Build-time ensures latest version

**Cons**:
- ❌ Requires build step
- ❌ Copy could be accidentally committed (.gitignore required)

---

### Strategy 3: Import/Reference (Code-Level)

**When to Use**: Code needs to load artifact dynamically

**Example**:
```python
# Python: Load canonical OpenAPI spec
import json
from pathlib import Path

OPENAPI_PATH = Path(__file__).parent.parent / "docs/03-integrate/02-API-Specifications/openapi.json"
spec = json.load(open(OPENAPI_PATH))
```

**Pros**:
- ✅ No file duplication
- ✅ Works in any environment

**Cons**:
- ❌ Hardcoded path (must match repo structure)

---

### Strategy 4: Cross-Reference (Documentation)

**When to Use**: Markdown docs reference other docs

**Example**:
```markdown
## API Specification

**Canonical Source**: [openapi.json](../../03-integrate/02-API-Specifications/openapi.json)

**DO NOT COPY** - Always reference the Stage 03 canonical source.
```

**Pros**:
- ✅ Clear documentation
- ✅ No file duplication

**Cons**:
- ❌ Manual link maintenance (broken link risk)

---

## SSOT Validation Workflow

### Step 1: Design Phase (Define Canonical Locations)

During project setup, document SSOT locations:

```markdown
# docs/README.md - SSOT Index

## Canonical Artifact Locations

| Artifact Type | Canonical Location | Consumers |
|---------------|-------------------|-----------|
| OpenAPI Spec | docs/03-integrate/02-API-Specifications/openapi.json | Backend, Frontend, Tests |
| Database Schema | docs/01-planning/04-Data-Model/Data-Model-ERD.md | Alembic, ORM, Tests |
| Environment Vars | .env.example | All environments |
| API Endpoint List | docs/03-integrate/.../COMPLETE-API-ENDPOINT-REFERENCE.md | Docs, Developers |
```

### Step 2: Development (Enforce SSOT)

**Pre-Commit Hook**:
```bash
#!/bin/bash
# .git/hooks/pre-commit

echo "Checking SSOT compliance..."

# Check for duplicate openapi.json
duplicates=$(find . -name "openapi.json" -type f | grep -v "03-integrate/02-API-Specifications" | wc -l)
if [ "$duplicates" -gt 0 ]; then
  echo "🔴 SSOT VIOLATION: Duplicate openapi.json files found"
  find . -name "openapi.json" -type f | grep -v "03-integrate/02-API-Specifications"
  exit 1
fi

echo "✅ SSOT compliance check passed"
```

### Step 3: CI/CD (Automated Validation)

```yaml
# .github/workflows/ssot-validation.yml
name: SSOT Compliance

on: [push, pull_request]

jobs:
  ssot-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check for duplicate openapi.json
        run: |
          duplicates=$(find . -name "openapi.json" -type f | wc -l)
          expected_count=1
          if [ "$duplicates" -ne "$expected_count" ]; then
            echo "Expected $expected_count openapi.json file, found $duplicates"
            find . -name "openapi.json" -type f
            exit 1
          fi
```

### Step 4: Code Review (Manual Check)

**PR Template**:
```markdown
## SSOT Compliance Checklist

- [ ] No duplicate artifact files added
- [ ] All references use canonical locations
- [ ] Symlinks (if added) point to canonical source
- [ ] Documentation updated if canonical location changed
```

---

## Common SSOT Violations & Remediation

### Violation 1: Copy-Paste Artifact

**Detected**:
```bash
$ find . -name "openapi.json" -type f
./docs/03-integrate/02-API-Specifications/openapi.json  ← Canonical
./backend/openapi.json  ← DUPLICATE
```

**Remediation**:
```bash
# Backup duplicate (in case it has unique content)
cp backend/openapi.json backend/openapi.json.bak

# Compare files
diff docs/03-integrate/02-API-Specifications/openapi.json backend/openapi.json

# If identical, delete duplicate
rm backend/openapi.json

# If different, merge changes into canonical
# (Manual review required)

# Add to .gitignore to prevent re-commit
echo "backend/openapi.json" >> .gitignore
git add .gitignore
git commit -m "fix: Remove duplicate openapi.json, enforce SSOT"
```

### Violation 2: Outdated Canonical Source

**Detected**: Code generates new openapi.json but canonical not updated

**Remediation**:
```bash
# Regenerate canonical from code
python3 scripts/generate_openapi.py > docs/03-integrate/02-API-Specifications/openapi.json

# Commit update
git add docs/03-integrate/02-API-Specifications/openapi.json
git commit -m "docs: Update canonical OpenAPI spec from backend v1.3.0"
```

### Violation 3: Hardcoded Values (Anti-SSOT)

**Problem**: .env values copied into code

```python
# ❌ BAD: Hardcoded (not SSOT)
DATABASE_URL = "postgresql://user:pass@localhost:5432/db"

# ✅ GOOD: Load from canonical .env
from os import getenv
DATABASE_URL = getenv("DATABASE_URL")  # References .env.example structure
```

---

## SSOT Benefits by Role

**Developers**:
- ✅ Update once, changes propagate everywhere
- ✅ No "which version is correct?" confusion
- ✅ Less manual work (no sync 4 copies)

**QA Engineers**:
- ✅ Tests always use latest schema
- ✅ No false failures from outdated specs
- ✅ Easier test maintenance

**Tech Leads**:
- ✅ Clear ownership (canonical = authority)
- ✅ Easier code review (check SSOT compliance)
- ✅ Reduced technical debt

**DevOps**:
- ✅ CI/CD enforces SSOT automatically
- ✅ Deployment uses canonical configs
- ✅ Less "works on my machine" issues

---

## Success Criteria

**SSOT Compliance = PASS** when:
- ✅ Each artifact type has exactly 1 canonical file
- ✅ All duplicates replaced with symlinks/references
- ✅ CI/CD blocks PRs with SSOT violations
- ✅ Pre-commit hook prevents violations
- ✅ Documentation lists canonical locations

**Measurement**:
```bash
# Run SSOT validator
sdlcctl validate --ssot

# Expected:
# ✅ openapi.json: 1 canonical, 0 duplicates
# ✅ ERD: 1 canonical, 0 duplicates
# ✅ .env.example: 1 canonical, 0 duplicates
# ✅ SSOT Compliance: PASS
```

---

## References

**Related Principles**:
- [E2E API Testing Methodology](./SDLC-E2E-API-Testing-Methodology.md)
- [Stage Cross-Reference](./SDLC-Stage-Cross-Reference.md)
- [Stage Dependencies](./SDLC-Stage-Dependencies.md)

**Checklists**:
- [SSOT Compliance Checklist](../05-Templates-Tools/05-Checklists/SSOT-COMPLIANCE-CHECKLIST.md)
- [OpenAPI Spec Quality Checklist](../05-Templates-Tools/05-Checklists/OPENAPI-SPEC-QUALITY-CHECKLIST.md)

**Guides**:
- [E2E Testing Quick Start](../07-Implementation-Guides/E2E-TESTING-QUICKSTART.md)

---

**Document Status**: ACTIVE
**Created**: February 2, 2026
**Updated**: February 2, 2026
**Framework**: SDLC 6.0.2
**Owner**: Architecture + Engineering Teams
**Approval**: CTO @nqh ✅
