# E2E API Testing Workflow

**Version**: 1.0.0
**Framework**: SDLC 6.0.5
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Last Updated**: February 2026

---

## Overview

This template defines the standardized 6-phase E2E API testing workflow for SDLC Framework projects. It ensures comprehensive API validation with Stage 03 ↔ Stage 05 cross-reference traceability.

---

## Phase 0: API Documentation Check (Stage 03)

### Objective
Verify API documentation exists and is complete before testing begins.

### Checklist

```yaml
Phase 0 Tasks:
  - [ ] Locate COMPLETE-API-ENDPOINT-REFERENCE.md in Stage 03
  - [ ] Verify openapi.json exists (SSOT location: docs/03-Integration-APIs/02-API-Specifications/)
  - [ ] Check API documentation completeness (all endpoints documented)
  - [ ] Identify undocumented endpoints for later documentation
  - [ ] Note authentication requirements

SSOT Principle:
  - openapi.json MUST exist in Stage 03 (single source)
  - Stage 05 references via symlink or relative path (NOT duplicate)
```

### Actions if Documentation Missing

1. **Create API Reference**: Generate from codebase using OpenAPI extraction
2. **Export openapi.json**: Use `/api/v1/openapi.json` endpoint
3. **Document manually**: For endpoints without OpenAPI annotations

### Exit Criteria
- [ ] API documentation exists in Stage 03
- [ ] openapi.json available and valid
- [ ] Endpoint count known

---

## Phase 1: Setup & Authentication (Stage 05)

### Objective
Prepare testing environment with proper authentication.

### Checklist

```yaml
Phase 1 Tasks:
  - [ ] Create Stage 05 folder structure (if not exists)
  - [ ] Locate test credentials (environment variables, secrets)
  - [ ] Authenticate against API
  - [ ] Save authentication token
  - [ ] Verify token validity

Folder Structure:
  docs/05-Testing-Quality/
  └── 03-E2E-Testing/
      ├── reports/           # Test reports go here
      ├── scripts/           # Test scripts
      ├── artifacts/         # Runtime artifacts (gitignored)
      │   ├── auth_token.txt # Ephemeral token
      │   └── .gitignore     # Ignore sensitive files
      └── README.md          # Links to Stage 03
```

### Authentication Methods

| Method | Implementation |
|--------|---------------|
| JWT Bearer | `Authorization: Bearer {token}` |
| API Key | `X-API-Key: {key}` or query param |
| OAuth 2.0 | Client credentials flow |
| Session | Cookie-based with CSRF |

### Exit Criteria
- [ ] Test environment configured
- [ ] Authentication successful
- [ ] Token saved securely (gitignored)

---

## Phase 2: Test Execution

### Objective
Execute comprehensive API tests against all endpoints.

### Checklist

```yaml
Phase 2 Tasks:
  - [ ] Parse OpenAPI specification from Stage 03
  - [ ] Generate test cases for each endpoint
  - [ ] Execute tests with authentication
  - [ ] Capture all responses (success and failure)
  - [ ] Record timing metrics

Test Categories:
  1. Functional Tests:
     - All HTTP methods (GET, POST, PUT, DELETE, PATCH)
     - Required vs optional parameters
     - Valid and invalid inputs

  2. Authentication Tests:
     - Valid token access
     - Expired token handling
     - Missing token response

  3. Authorization Tests:
     - Role-based access control
     - Resource ownership validation
     - Cross-tenant isolation

  4. Edge Cases:
     - Empty payloads
     - Maximum payload sizes
     - Special characters
     - Unicode handling
```

### Test Script Template

```python
# test_all_endpoints.py
import requests
from pathlib import Path
import json

def load_openapi_spec():
    """Load OpenAPI spec from Stage 03 (SSOT)"""
    spec_path = Path("docs/03-Integration-APIs/02-API-Specifications/openapi.json")
    return json.loads(spec_path.read_text())

def execute_endpoint_tests(spec, auth_token):
    """Execute tests for all endpoints"""
    results = []
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            result = test_endpoint(path, method, details, auth_token)
            results.append(result)
    return results

def generate_report(results):
    """Generate E2E test report"""
    pass_count = sum(1 for r in results if r["status"] == "pass")
    total = len(results)
    return {
        "total_endpoints": total,
        "passed": pass_count,
        "failed": total - pass_count,
        "pass_rate": round(pass_count / total * 100, 1)
    }
```

### Exit Criteria
- [ ] All endpoints tested
- [ ] Responses captured
- [ ] Metrics recorded

---

## Phase 3: Report Generation

### Objective
Generate comprehensive E2E test report with actionable findings.

### Report Template

```markdown
# E2E API Test Report

**Date**: {DATE}
**Project**: {PROJECT_NAME}
**Environment**: {ENV}
**Tester**: {NAME}

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Endpoints | {COUNT} |
| Passed | {PASS} |
| Failed | {FAIL} |
| Pass Rate | {RATE}% |
| Duration | {TIME} |

## Results by Category

### Authentication Endpoints
| # | Method | Endpoint | Status | Response Time |
|---|--------|----------|--------|---------------|
| 1 | POST | /api/v1/auth/login | PASS | 120ms |

### Failed Endpoints (Requires Attention)

#### Endpoint: {METHOD} {PATH}
- **Expected**: {EXPECTED}
- **Actual**: {ACTUAL}
- **Root Cause**: {ANALYSIS}
- **Recommendation**: {FIX}

## Cross-Reference

- **API Documentation**: [Stage 03 API Reference](../../../03-Integration-APIs/02-API-Specifications/COMPLETE-API-ENDPOINT-REFERENCE.md)
- **OpenAPI Spec**: [openapi.json](../../../03-Integration-APIs/02-API-Specifications/openapi.json)

## Appendix

### Test Environment
- Base URL: {URL}
- Auth Method: {AUTH}
- Test Framework: {TOOL}
```

### Report Location
```
docs/05-Testing-Quality/03-E2E-Testing/reports/E2E-API-REPORT-{YYYY-MM-DD}.md
```

### Exit Criteria
- [ ] Report generated with all sections
- [ ] Pass rate calculated
- [ ] Failed endpoints documented with root cause
- [ ] Cross-reference links included

---

## Phase 4: Stage 03 Update

### Objective
Update API documentation with findings from E2E testing.

### Checklist

```yaml
Phase 4 Tasks:
  - [ ] Update COMPLETE-API-ENDPOINT-REFERENCE.md with test status
  - [ ] Add real examples from successful tests
  - [ ] Document validation rules discovered
  - [ ] Add "Last Tested" dates
  - [ ] Link to E2E report

Updates to API Reference:
  Per Endpoint:
    - Test Status: PASS/FAIL
    - Last Tested: {DATE}
    - Test Report: Link to Stage 05 report
    - Real Examples: From actual test responses
```

### Example Update

```markdown
### Endpoint: POST /api/v1/users

- **Test Status**: PASS
- **Last Tested**: 2026-02-15
- **Test Report**: [E2E Report 2026-02-15](../../05-Testing-Quality/03-E2E-Testing/reports/E2E-API-REPORT-2026-02-15.md#users)

#### Real Example (from E2E test)
```json
// Request
POST /api/v1/users
{
  "email": "test@example.com",
  "name": "Test User"
}

// Response (201 Created)
{
  "id": "usr_abc123",
  "email": "test@example.com",
  "name": "Test User",
  "created_at": "2026-02-15T10:30:00Z"
}
```
```

### Exit Criteria
- [ ] API Reference updated with test status
- [ ] Real examples added
- [ ] Links to test report included

---

## Phase 5: Cross-Reference Validation (NEW)

### Objective
Ensure bidirectional traceability between Stage 03 and Stage 05.

### Cross-Reference Matrix

```yaml
Stage 03 → Stage 05:
  docs/03-Integration-APIs/02-API-Specifications/:
    COMPLETE-API-ENDPOINT-REFERENCE.md:
      - Links to: E2E-API-REPORT-{DATE}.md
      - Per endpoint: Test status, last tested date

    openapi.json:
      - Single source of truth (SSOT)
      - Stage 05 references via relative path

    README.md:
      - Links to Stage 05 E2E Testing folder
      - Lists related test reports

Stage 05 → Stage 03:
  docs/05-Testing-Quality/03-E2E-Testing/:
    reports/E2E-API-REPORT-{DATE}.md:
      - Links to: COMPLETE-API-ENDPOINT-REFERENCE.md
      - References: openapi.json (via relative path)

    README.md:
      - Links to Stage 03 API Specifications
      - Documents SSOT principle
```

### Validation Checklist

```yaml
Cross-Reference Validation:
  Stage 03:
    - [ ] API Reference links to test report
    - [ ] README links to Stage 05
    - [ ] openapi.json is SINGLE source (not duplicated)

  Stage 05:
    - [ ] Test report links to API Reference
    - [ ] README links to Stage 03
    - [ ] No duplicate openapi.json (symlink or relative path only)

  Bidirectional:
    - [ ] Can navigate Stage 03 → Stage 05 → Stage 03
    - [ ] All links valid and not broken
```

### Exit Criteria
- [ ] All cross-references validated
- [ ] Bidirectional navigation working
- [ ] SSOT principle enforced

---

## Stage Transition Notes

### Stage 03 → Stage 05
- API documentation MUST exist before testing begins
- openapi.json is the SSOT in Stage 03
- Test scripts reference Stage 03 spec (not duplicate)

### Stage 05 → Stage 03
- Test findings update API documentation
- Real examples from tests enrich documentation
- Test status visible in API Reference

### Circular Dependency
- Both stages reference each other (by design)
- This creates comprehensive traceability
- Updates in either stage trigger cross-reference validation

---

## Integration with SDLC Orchestrator

### Evidence Artifacts
```yaml
Evidence Types:
  - e2e_testing_report: E2E-API-REPORT-{DATE}.md
  - api_documentation_reference: COMPLETE-API-ENDPOINT-REFERENCE.md
  - stage_cross_reference: Links between Stage 03 ↔ 05

Validation Rules:
  - E2E report required for Stage 05 → 06 transition
  - Minimum pass rate: 80% (configurable)
  - Cross-reference validation before gate approval
```

### CLI Commands
```bash
# Validate E2E testing artifacts
sdlcctl validate-e2e --project-path . --min-pass-rate 80

# Validate cross-references
sdlcctl validate-cross-reference --stage-03 docs/03-Integration-APIs --stage-05 docs/05-Testing-Quality

# Generate report from test results
sdlcctl generate-e2e-report --results test_results.json --output docs/05-Testing-Quality/03-E2E-Testing/reports/
```

---

## Compatibility

- **e2e-api-testing skill**: v1.1.0+
- **SDLC Framework**: 6.0.2+
- **SDLC Orchestrator**: Sprint 137+

---

## References

- [RFC-SDLC-602-E2E-API-TESTING](../../../09-Continuous-Improvement/RFC/RFC-SDLC-602-E2E-API-TESTING.md)
- [Stage Cross-Reference Matrix](../../../02-Core-Methodology/SDLC-Stage-Cross-Reference.md)
- [Security Testing Checklist](./testing_security-testing-checklist.md)
- [Testing Artifacts Structure](../../../02-Core-Methodology/Documentation-Standards/SDLC-Testing-Artifacts-Structure.md)
