# SSOT Compliance Checklist (SDLC 6.0.6)

**Version**: 1.0.0
**Date**: February 2, 2026
**Status**: ACTIVE
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Framework**: SDLC 6.0.6
**Purpose**: Validate Single Source of Truth principle compliance

---

## SSOT Principle

**Definition**: Each artifact type must have exactly ONE canonical source in the project structure. All other references must be symlinks, imports, or cross-references—never copies.

**Why It Matters**:
- ❌ **Drift Risk**: Duplicate files diverge over time (copy-paste errors)
- ❌ **Update Burden**: Change one file, must update N copies manually
- ❌ **Truth Ambiguity**: Which version is correct when files conflict?
- ✅ **SSOT Benefits**: Update once, automatically propagates everywhere

---

## API Specification SSOT Checklist

### Phase 0: Locate Canonical Source

**Canonical Location** (SDLC 6.0.6):
```
docs/03-integrate/02-API-Specifications/openapi.json
```

- [ ] ✅ openapi.json exists in Stage 03 Integration folder
- [ ] ✅ File is valid JSON (no syntax errors)
- [ ] ✅ OpenAPI version 3.0.x or 3.1.x
- [ ] ✅ File size reasonable (<10MB for most projects)

**Validation Command**:
```bash
# Check file exists
test -f docs/03-integrate/02-API-Specifications/openapi.json && echo "✅ Found" || echo "🔴 Missing"

# Validate JSON syntax
python3 -c "import json; json.load(open('docs/03-integrate/02-API-Specifications/openapi.json'))" && echo "✅ Valid JSON" || echo "🔴 Invalid JSON"

# Check OpenAPI version
jq -r '.openapi' docs/03-integrate/02-API-Specifications/openapi.json
```

---

### Phase 1: Detect Duplicates

**Common Duplicate Locations**:
- ❌ `backend/openapi.json` (should be auto-generated only, not checked in)
- ❌ `frontend/openapi.json`
- ❌ `docs/05-test/openapi.json`
- ❌ `docs/01-planning/openapi.json`
- ❌ Any other directory with `openapi.json`

**Detection Command**:
```bash
# Find ALL openapi.json files in project
find . -name "openapi.json" -type f 2>/dev/null

# Expected output: EXACTLY ONE file
# ✅ ./docs/03-integrate/02-API-Specifications/openapi.json

# If more than 1 file found → SSOT VIOLATION
```

**Automated Validation**:
```bash
# Using sdlcctl (if available)
sdlcctl e2e cross-reference --check-ssot

# Expected output:
# ✅ SSOT Compliance: PASS
# ✅ openapi.json canonical source: docs/03-integrate/02-API-Specifications/openapi.json
# ✅ No duplicates found
```

---

### Phase 2: Validate Symlinks (If Used)

**Acceptable Pattern**: Symlink to canonical source

```bash
# Example: docs/05-test/api/ needs openapi.json
cd docs/05-test/api/
ln -sf ../../../03-integrate/02-API-Specifications/openapi.json openapi.json

# Verify symlink
ls -la openapi.json
# Expected: openapi.json -> ../../../03-integrate/02-API-Specifications/openapi.json
```

**Symlink Validation**:
- [ ] ✅ Symlink points to canonical source (not a copy)
- [ ] ✅ Symlink is relative path (not absolute)
- [ ] ✅ Symlink is committed to git (tracked)
- [ ] ✅ README.md documents symlink purpose

**Detection Command**:
```bash
# Find all symlinks named openapi.json
find . -type l -name "openapi.json" -ls
```

---

### Phase 3: Check Git History

**Git Tracking Check**:
```bash
# Verify canonical source is tracked
git log --oneline docs/03-integrate/02-API-Specifications/openapi.json | head -5

# Check for accidentally committed duplicates (should return empty)
git log --all --full-history -- "**/openapi.json" | grep -v "03-integrate/02-API-Specifications"
```

**Gitignore Rules**:
```gitignore
# .gitignore - Prevent auto-generated copies from being committed
backend/openapi.json
frontend/openapi.json
**/openapi.json
!docs/03-integrate/02-API-Specifications/openapi.json  # Allow canonical source only
```

- [ ] ✅ .gitignore prevents duplicate commits
- [ ] ✅ Only canonical source tracked in git
- [ ] ✅ Auto-generated files ignored

---

### Phase 4: Validate Cross-References

**Stage 03 → Stage 05 Link**:

In `docs/05-test/03-E2E-Testing/README.md`:
```markdown
## API Specification

**Canonical Source**: [openapi.json](../../03-integrate/02-API-Specifications/openapi.json)

**DO NOT COPY** - Always reference the Stage 03 canonical source.
```

**Stage 01 → Stage 03 Link**:

In `docs/01-planning/05-API-Design/API-Specification.md`:
```markdown
## OpenAPI Specification

**Canonical Source**: [openapi.json](../../03-integrate/02-API-Specifications/openapi.json)

**Implementation Notes**: Design decisions documented here, but OpenAPI spec lives in Stage 03.
```

**Checklist**:
- [ ] ✅ Stage 01 references (not copies) Stage 03 spec
- [ ] ✅ Stage 05 references (not copies) Stage 03 spec
- [ ] ✅ All cross-references use relative markdown links
- [ ] ✅ READMEs document SSOT principle

---

### Phase 5: Automation & CI/CD

**Pre-Commit Hook** (Prevent SSOT violations):
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Check for duplicate openapi.json
duplicates=$(find . -name "openapi.json" -type f | grep -v "03-integrate/02-API-Specifications" | wc -l)

if [ "$duplicates" -gt 0 ]; then
  echo "🔴 SSOT VIOLATION: Duplicate openapi.json files found"
  echo "Only docs/03-integrate/02-API-Specifications/openapi.json is allowed"
  find . -name "openapi.json" -type f | grep -v "03-integrate/02-API-Specifications"
  exit 1
fi

echo "✅ SSOT Check: PASS"
```

**CI/CD Gate**:
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
          duplicates=$(find . -name "openapi.json" -type f | grep -v "03-integrate/02-API-Specifications" | wc -l)
          if [ "$duplicates" -gt 0 ]; then
            echo "SSOT violation detected"
            exit 1
          fi
```

- [ ] ✅ Pre-commit hook installed
- [ ] ✅ CI/CD pipeline checks SSOT
- [ ] ✅ Pull requests blocked on SSOT violations

---

## Other Artifact Types SSOT

### Database Schema

**Canonical Source**: `docs/01-planning/04-Data-Model/Data-Model-ERD.md`

- [ ] ✅ No duplicate ERD files
- [ ] ✅ Alembic migrations reference canonical schema
- [ ] ✅ ORM models synced with ERD

### Environment Variables

**Canonical Source**: `.env.example` in repo root

- [ ] ✅ No duplicate .env.example files
- [ ] ✅ All services reference same .env.example
- [ ] ✅ Documentation cross-references .env.example

### API Endpoint List

**Canonical Source**: `docs/03-integrate/02-API-Specifications/COMPLETE-API-ENDPOINT-REFERENCE.md`

- [ ] ✅ Auto-generated from openapi.json (SSOT)
- [ ] ✅ No manually maintained endpoint lists
- [ ] ✅ README.md references canonical list

---

## SSOT Violation Remediation

### If Duplicate Found:

**Step 1: Determine Which is Canonical**
```bash
# Compare file sizes and modification times
ls -lh docs/03-integrate/02-API-Specifications/openapi.json
ls -lh backend/openapi.json  # Duplicate found

# Check which has more recent changes
git log --oneline docs/03-integrate/02-API-Specifications/openapi.json | head -1
git log --oneline backend/openapi.json | head -1
```

**Step 2: Backup & Remove Duplicate**
```bash
# Backup duplicate (in case it has unique changes)
cp backend/openapi.json backend/openapi.json.bak

# Remove duplicate
git rm backend/openapi.json

# Add to .gitignore
echo "backend/openapi.json" >> .gitignore
```

**Step 3: Update References**
```bash
# If code imports backend/openapi.json, update to reference Stage 03
# Example: Python script
# OLD: spec = json.load(open("backend/openapi.json"))
# NEW: spec = json.load(open("docs/03-integrate/02-API-Specifications/openapi.json"))
```

**Step 4: Document in PR**
```markdown
## SSOT Compliance Fix

**Issue**: Duplicate openapi.json found in backend/
**Resolution**: Removed duplicate, updated references to Stage 03 canonical source
**Validation**: `find . -name "openapi.json" -type f` returns 1 file only
```

---

## Success Criteria

**SSOT Compliance = PASS** when:
- ✅ Exactly 1 openapi.json file (canonical source in Stage 03)
- ✅ All other locations use symlinks or cross-references
- ✅ CI/CD enforces SSOT on every PR
- ✅ Pre-commit hook prevents violations
- ✅ Documentation cross-references canonical source

**Tools**:
- Manual: `find . -name "openapi.json" -type f`
- Automated: `sdlcctl e2e cross-reference --check-ssot`
- CI/CD: GitHub Actions workflow

---

**Document Status**: ACTIVE
**Created**: February 2, 2026
**Framework**: SDLC 6.0.6
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Owner**: Engineering + QA Teams
