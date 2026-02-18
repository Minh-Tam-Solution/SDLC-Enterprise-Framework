# E2E API Testing Methodology (SDLC 6.1.0)

**Version**: 1.0.0
**Date**: February 2, 2026
**Status**: ACTIVE
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Framework**: SDLC 6.1.0
**Stage**: 05-TEST
**Purpose**: Standardized methodology for End-to-End API testing using OpenAPI specifications

---

## Overview

**E2E API Testing** validates that all API endpoints work correctly together as a complete system, from authentication through data retrieval, creation, update, and deletion.

**Key Principles**:
1. **Contract-First**: OpenAPI spec is the source of truth
2. **Automated**: 80%+ tests auto-generated from spec
3. **SSOT**: Single Source of Truth for API documentation (Stage 03)
4. **Cross-Referenced**: Stage 03 (Integration) ↔ Stage 05 (Testing) bidirectional links
5. **Security-Aware**: OWASP API Top 10 built into methodology

---

## 6-Phase E2E API Testing Workflow

```
Phase 0: Check Docs → Phase 1: Auth → Phase 2: Execute →
Phase 3: Report → Phase 4: Update Docs → Phase 5: Cross-Ref
```

---

### Phase 0: API Documentation Check (SSOT Validation)

**Purpose**: Ensure API specification exists, is valid, and follows SSOT principle

**Tasks**:
1. Verify OpenAPI spec exists in canonical location:
   ```
   docs/03-integrate/02-API-Specifications/openapi.json
   ```

2. Validate SSOT compliance:
   ```bash
   # No duplicate openapi.json files allowed
   find . -name "openapi.json" -type f
   # Expected: EXACTLY ONE file in Stage 03
   ```

3. Check OpenAPI spec quality:
   - OpenAPI version 3.0.x or 3.1.0
   - All endpoints have `operationId`, `summary`, `description`
   - All schemas have `examples`
   - Security schemes defined

4. Generate human-readable reference (if missing):
   ```bash
   # Auto-generate markdown from openapi.json
   python3 scripts/generate_api_reference.py
   ```

**Deliverable**: ✅ openapi.json validated and ready for testing

**Reference**: [SSOT Compliance Checklist](../05-Templates-Tools/05-Checklists/SSOT-COMPLIANCE-CHECKLIST.md)

---

### Phase 1: Authentication & Authorization Setup

**Purpose**: Establish authentication mechanisms and validate access controls

**Tasks**:
1. Identify auth methods from OpenAPI spec:
   ```yaml
   components:
     securitySchemes:
       BearerAuth:
         type: http
         scheme: bearer
   ```

2. Obtain test credentials:
   - **Development**: Create test user accounts
   - **Staging**: Use dedicated test@example.com accounts
   - **Production**: Read-only API keys only (never write)

3. Test authentication flow:
   ```bash
   # Example: JWT authentication
   curl -X POST https://api.example.com/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","password":"test123"}'

   # Expected: 200 + {"token":"eyJ..."}
   ```

4. Validate authorization (RBAC):
   - Test role-based access (admin, developer, qa, viewer)
   - Verify 403 Forbidden for unauthorized actions
   - Check 401 Unauthorized for expired tokens

**Deliverable**: ✅ Test credentials configured, auth flow validated

**Reference**: OWASP API2:2023 Broken Authentication

---

### Phase 2: Test Execution (Automated + Manual)

**Purpose**: Execute comprehensive test suite covering all endpoints

#### 2A: Auto-Generated Tests (80% Coverage)

**Generate from OpenAPI**:
```bash
# Using SDLC CLI tool
[SDLC CLI] e2e parse-openapi \
  docs/03-integrate/02-API-Specifications/openapi.json \
  --generate-tests \
  --test-output tests/e2e/

# Expected output:
# ✅ Generated 174 test cases from 58 endpoints
# ✅ Coverage: 100% (all endpoints)
```

**Run Tests**:
```bash
# pytest (Python)
pytest tests/e2e/ -v --html=report.html

# Newman (Postman)
newman run postman_collection.json -e test.env.json
```

#### 2B: Manual Tests (20% Coverage)

**Edge Cases** (not auto-generated):
- Multi-step workflows (e.g., create project → add members → submit gate)
- Race conditions (concurrent requests)
- File uploads (multipart/form-data)
- WebSocket connections
- Pagination edge cases (page=0, page=999999)

**Security Tests** (OWASP API Top 10):
- BOLA (Broken Object-Level Authorization)
- Mass assignment vulnerabilities
- Rate limiting bypass attempts
- SQL injection in query parameters
- SSRF (Server-Side Request Forgery)

**Deliverable**: ✅ Test results with pass/fail status per endpoint

---

### Phase 3: Report Generation

**Purpose**: Create human-readable E2E test report

**Report Structure** (use template):
```
docs/05-test/03-E2E-Testing/reports/E2E-API-REPORT-YYYY-MM-DD.md
```

**Required Sections**:
1. **Test Execution Summary**:
   - Total endpoints: N
   - Endpoints tested: N (X%)
   - Tests passed: N (X%)
   - Tests failed: N (X%)
   - Pass rate: X% (target ≥80%)

2. **Test Results by Category**:
   - Group by OpenAPI tags (Users, Projects, Gates, etc.)
   - Include method, endpoint, status code, response time

3. **Failures & Root Causes**:
   - Detailed failure analysis
   - Request/response samples
   - Resolution steps

4. **OWASP Security Findings**:
   - Security issues detected
   - Severity (P0/P1/P2)
   - Remediation recommendations

**Automated Report Generation**:
```bash
# pytest HTML report
pytest tests/e2e/ --html=docs/05-test/03-E2E-Testing/reports/report.html

# Convert to markdown (optional)
pandoc report.html -o E2E-API-REPORT-2026-02-02.md
```

**Deliverable**: ✅ E2E test report in Stage 05

**Reference**: [E2E API Test Report Template](../05-Templates-Tools/06-Manual-Templates/E2E-API-TEST-REPORT-TEMPLATE.md)

---

### Phase 4: Update Stage 03 Documentation

**Purpose**: Keep API documentation synchronized with test findings

**Update Triggers**:
1. **New Endpoint Found**: Undocumented endpoint discovered during testing
2. **Schema Mismatch**: Actual response differs from openapi.json
3. **Deprecated Endpoint**: Endpoint returns 410 Gone
4. **Auth Changes**: New security scheme required

**Update Process**:
```bash
# 1. Regenerate openapi.json from backend
python3 scripts/generate_openapi.py > docs/03-integrate/02-API-Specifications/openapi.json

# 2. Regenerate human-readable reference
python3 scripts/generate_api_reference.py

# 3. Commit changes
git add docs/03-integrate/02-API-Specifications/
git commit -m "docs(Stage 03): Update API spec based on E2E test findings"
```

**Documentation Improvements**:
- Add missing `examples` to schemas
- Clarify `description` fields based on actual behavior
- Document error responses (400, 401, 404, 500)
- Add `deprecated: true` to sunset endpoints

**Deliverable**: ✅ Stage 03 documentation updated and synchronized

---

### Phase 5: Cross-Reference Validation

**Purpose**: Ensure bidirectional links between Stage 03 (Integration) and Stage 05 (Testing)

**Validation Tasks**:
1. **Stage 03 → Stage 05 Link**:
   ```markdown
   # In docs/03-integrate/02-API-Specifications/README.md
   ## Test Reports
   - [Latest E2E Test Report](../../05-test/03-E2E-Testing/reports/)
   ```

2. **Stage 05 → Stage 03 Link**:
   ```markdown
   # In docs/05-test/03-E2E-Testing/README.md
   ## API Specification
   **Canonical Source**: [openapi.json](../../03-integrate/02-API-Specifications/openapi.json)
   ```

3. **SSOT Compliance** (no duplicates):
   ```bash
   [SDLC CLI] e2e cross-reference \
     --stage-03 docs/03-integrate \
     --stage-05 docs/05-test

   # Expected:
   # ✅ Cross-reference validation PASSED
   # ✅ 58 endpoints linked to test reports
   # ✅ SSOT: openapi.json in Stage 03 (no duplicates)
   ```

4. **Test Coverage Mapping**:
   - Each endpoint in openapi.json → test case in Stage 05
   - Each test result → references openapi.json operationId

**Deliverable**: ✅ Cross-reference validation passed

---

## Manual vs Automated Decision Tree

**When to Auto-Generate Tests** (80% of cases):
```
IF endpoint has:
  - operationId defined
  - Complete schema with examples
  - Standard CRUD operation (GET, POST, PUT, DELETE)
  - Simple authentication (Bearer token, API key)
THEN:
  Auto-generate test from OpenAPI spec
```

**When Manual Tests Required** (20% of cases):
```
IF endpoint involves:
  - Multi-step workflow (stateful)
  - File upload/download
  - WebSocket connections
  - Complex business logic
  - Race condition testing
  - Security edge cases (OWASP Top 10)
THEN:
  Write manual test
```

---

## Success Criteria

**E2E API Testing = PASS** when:
- ✅ **Pass Rate** ≥80% (for SDLC 6.1.0 LITE/STANDARD)
- ✅ **Pass Rate** ≥90% (for SDLC 6.1.0 PROFESSIONAL/ENTERPRISE)
- ✅ **SSOT Compliance**: openapi.json is single source
- ✅ **Cross-Reference**: Stage 03 ↔ Stage 05 bidirectional links validated
- ✅ **Security**: No P0/P1 OWASP vulnerabilities
- ✅ **Documentation**: Test report exists in Stage 05

**Minimum Requirements by Tier**:

| Tier | Pass Rate | SSOT | Cross-Ref | OWASP | Automation |
|------|-----------|------|-----------|-------|------------|
| LITE | ≥80% | ✅ | ⚠️ Optional | ⚠️ Basic | 50%+ |
| STANDARD | ≥85% | ✅ | ✅ | ✅ | 70%+ |
| PROFESSIONAL | ≥90% | ✅ | ✅ | ✅ | 80%+ |
| ENTERPRISE | ≥95% | ✅ | ✅ | ✅ + Audit | 90%+ |

---

## Tools & Technologies

### Recommended Tools

**OpenAPI Validation**:
- Spectral (linting)
- Redocly CLI (validation)
- oasdiff (breaking change detection)

**Test Generation**:
- SDLC CLI e2e parse-openapi (compliance validator tool)
- Schemathesis (Python auto-generation)
- Portman (Postman collection generator)

**Test Execution**:
- pytest + httpx (Python)
- Newman (Postman CLI)
- curl scripts (shell)

**Reporting**:
- pytest-html (Python HTML reports)
- Allure (interactive reports)
- ReportPortal (centralized test management)

---

## Common Pitfalls & Solutions

### Pitfall 1: Duplicate OpenAPI Specs

**Problem**:
```
backend/openapi.json (auto-generated, not tracked)
docs/03-integrate/02-API-Specifications/openapi.json (canonical)
frontend/openapi.json (copy for SDK generation)
```

**Solution**: SSOT Principle
```bash
# Delete duplicates
rm backend/openapi.json frontend/openapi.json

# Add to .gitignore
echo "backend/openapi.json" >> .gitignore
echo "frontend/openapi.json" >> .gitignore

# Use symlinks if needed
cd frontend/
ln -sf ../docs/03-integrate/02-API-Specifications/openapi.json openapi.json
```

### Pitfall 2: Outdated OpenAPI Spec

**Problem**: Code changes but openapi.json not updated

**Solution**: CI/CD Gate
```yaml
# .github/workflows/openapi-sync.yml
name: OpenAPI Sync Check

on: [pull_request]

jobs:
  openapi-drift-detection:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate current spec
        run: python3 scripts/generate_openapi.py > openapi-current.json
      - name: Compare with canonical
        run: |
          diff openapi-current.json docs/03-integrate/02-API-Specifications/openapi.json
          if [ $? -ne 0 ]; then
            echo "⚠️ OpenAPI spec is out of sync. Run: python3 scripts/generate_openapi.py"
            exit 1
          fi
```

### Pitfall 3: Skipping Phase 5 (Cross-Reference)

**Problem**: Tests pass but documentation not linked

**Solution**: Mandatory checklist in PR template
```markdown
## E2E Testing Checklist

Before merging, ensure:
- [ ] E2E test report created in Stage 05
- [ ] Stage 03 README links to test report
- [ ] Stage 05 README links to openapi.json
- [ ] SDLC E2E cross-reference validation passes
```

---

## Integration with SDLC Stages

**Stage 01 (PLANNING)**:
- Define API requirements
- Create initial OpenAPI draft

**Stage 02 (DESIGN)**:
- Refine OpenAPI spec with schemas
- Define security schemes

**Stage 03 (INTEGRATE)**:
- ✅ **CANONICAL LOCATION**: openapi.json lives here
- Document all endpoints, schemas, examples

**Stage 04 (BUILD)**:
- Implement API endpoints
- Auto-generate openapi.json from code

**Stage 05 (TEST)**: ← **THIS METHODOLOGY**
- Execute 6-phase E2E testing workflow
- Create test reports
- Cross-reference with Stage 03

**Stage 06 (DEPLOY)**:
- Deploy API with validated spec
- Publish openapi.json for client SDK generation

---

## References

**Templates**:
- [E2E API Test Report Template](../05-Templates-Tools/06-Manual-Templates/E2E-API-TEST-REPORT-TEMPLATE.md)
- [SSOT Compliance Checklist](../05-Templates-Tools/05-Checklists/SSOT-COMPLIANCE-CHECKLIST.md)
- [OpenAPI Spec Quality Checklist](../05-Templates-Tools/05-Checklists/OPENAPI-SPEC-QUALITY-CHECKLIST.md)

**Guides**:
- [E2E Testing Quick Start](../07-Implementation-Guides/E2E-TESTING-QUICKSTART.md)

**Methodology**:
- [SSOT Principle](./SDLC-SSOT-Principle.md)
- [Stage Cross-Reference](./SDLC-Stage-Cross-Reference.md)
- [Stage Dependencies](./SDLC-Stage-Dependencies.md)

**External**:
- [OpenAPI 3.1.0 Specification](https://spec.openapis.org/oas/v3.1.0)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [RFC-SDLC-602](../../docs/01-planning/02-RFCs/RFC-SDLC-602-E2E-API-TESTING.md) (Orchestrator-specific)

---

**Document Status**: ACTIVE
**Created**: February 2, 2026
**Updated**: February 2, 2026
**Framework**: SDLC 6.1.0
**Owner**: Engineering + QA Teams
**Approval**: CTO @nqh ✅
