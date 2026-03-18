# Testing Artifacts Folder Structure

**Version**: 1.0.0
**Framework**: SDLC 6.1.2
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Last Updated**: February 2026

---

## Overview

This document defines the standardized folder structure for testing artifacts in SDLC Framework projects. It ensures consistent organization across Stage 03 (Integration) and Stage 05 (Testing), with proper cross-referencing and SSOT compliance.

---

## Complete Structure

```
<PROJECT_ROOT>/docs/
│
├── 03-integrate/                    # Stage 03 - Integration & APIs
│   ├── 01-API-Contracts/
│   │   ├── README.md                       # Links to integration tests
│   │   └── api-contracts/
│   │
│   ├── 01-api-specifications/              # SSOT for API documentation
│   │   ├── COMPLETE-API-ENDPOINT-REFERENCE.md   # Main API docs
│   │   │   └── [Links to Stage 05 test reports]
│   │   ├── openapi.json                    # SINGLE SOURCE (SSOT)
│   │   ├── openapi.yaml                    # Alternative format (optional)
│   │   └── README.md                       # Links to Stage 05
│   │
│   └── 03-Integration-Guides/
│       └── README.md
│
└── 05-test/                     # Stage 05 - Testing & Quality
    │
    ├── 01-test-plans/
    │   └── TEST-STRATEGY.md
    │
    ├── 02-Unit-Testing/
    │   ├── coverage/
    │   │   └── coverage-report.html
    │   └── README.md
    │
    ├── 03-e2e-testing/                     # E2E API Testing
    │   ├── reports/                        # Test reports (committed)
    │   │   ├── E2E-API-REPORT-2026-02-15.md
    │   │   ├── E2E-API-REPORT-2026-02-01.md
    │   │   └── README.md                   # Report index
    │   │
    │   ├── scripts/                        # Test scripts (committed)
    │   │   ├── test_all_endpoints.py
    │   │   ├── test_authentication.py
    │   │   ├── test_authorization.py
    │   │   └── README.md
    │   │
    │   ├── artifacts/                      # Runtime artifacts (gitignored)
    │   │   ├── .gitignore                  # Ignore sensitive files
    │   │   ├── README.md                   # Explains what goes here
    │   │   ├── auth_token.txt              # Ephemeral (gitignored)
    │   │   ├── test_results_*.json         # Raw results (gitignored)
    │   │   └── openapi.json                # SYMLINK to Stage 03 (NOT copy)
    │   │
    │   ├── changelogs/                     # Test changelog
    │   │   └── CHANGELOG-2026-02.md
    │   │
    │   └── README.md                       # Links to Stage 03
    │
    ├── 04-integration-testing/
    │   ├── reports/
    │   ├── scripts/
    │   └── README.md
    │
    ├── 05-Security-Testing/                # Security testing (NEW)
    │   ├── owasp-top10/
    │   │   ├── SECURITY-REPORT-2026-02-15.md
    │   │   └── findings/
    │   │       ├── API1-BOLA.md
    │   │       └── API2-AUTH.md
    │   │
    │   ├── penetration/
    │   │   └── PENTEST-REPORT-2026-Q1.md
    │   │
    │   ├── scripts/
    │   │   ├── security_scan.py
    │   │   └── owasp_checker.py
    │   │
    │   └── README.md
    │
    ├── 06-Performance-Testing/
    │   ├── reports/
    │   ├── scripts/
    │   └── README.md
    │
    └── README.md                           # Stage 05 overview with links
```

---

## Detailed Specifications

### Stage 03: API Specifications (SSOT)

#### Location
```
docs/03-integrate/01-api-specifications/
```

#### Files

| File | Purpose | SSOT |
|------|---------|------|
| `openapi.json` | API specification | YES - Single source |
| `COMPLETE-API-ENDPOINT-REFERENCE.md` | Human-readable API docs | YES |
| `README.md` | Index with Stage 05 links | - |

#### SSOT Rules
```yaml
openapi.json:
  Location: docs/03-integrate/01-api-specifications/openapi.json
  Rule: This is the ONLY location for openapi.json
  Access from Stage 05:
    - Symlink: artifacts/openapi.json -> ../../../03-integrate/...
    - OR relative path in scripts
  Prohibited:
    - Copying to Stage 05
    - Generating duplicate in Stage 05
    - Multiple copies anywhere
```

---

### Stage 05: E2E Testing

#### Location
```
docs/05-test/03-e2e-testing/
```

#### Subfolders

##### reports/
```yaml
Purpose: Store test reports (committed to git)
Contents:
  - E2E-API-REPORT-{YYYY-MM-DD}.md
  - README.md (index of reports)

Naming Convention:
  Pattern: E2E-API-REPORT-{YYYY-MM-DD}.md
  Example: E2E-API-REPORT-2026-02-15.md

Required Sections:
  - Executive Summary
  - Results by Category
  - Failed Endpoints
  - Cross-Reference Links to Stage 03
```

##### scripts/
```yaml
Purpose: Store test scripts (committed to git)
Contents:
  - test_all_endpoints.py
  - test_authentication.py
  - test_authorization.py
  - conftest.py (pytest fixtures)
  - README.md

Requirements:
  - Must reference openapi.json from Stage 03 (not copy)
  - Must output results to artifacts/ folder
  - Must generate reports to reports/ folder
```

##### artifacts/
```yaml
Purpose: Runtime artifacts (NOT committed to git)
Contents:
  - auth_token.txt (authentication tokens)
  - test_results_{timestamp}.json (raw results)
  - openapi.json (SYMLINK to Stage 03)
  - .gitignore
  - README.md

.gitignore Contents:
  # Ignore sensitive and ephemeral files
  auth_token.txt
  *.json
  !.gitignore

README.md Contents:
  Explains purpose of folder and what should be here
```

##### changelogs/
```yaml
Purpose: Track changes to test suite
Contents:
  - CHANGELOG-{YYYY-MM}.md

Format:
  ## [2026-02-15]
  ### Added
  - New endpoint tests for /api/v1/users
  ### Changed
  - Updated authentication test flow
```

---

### Stage 05: Security Testing

#### Location
```
docs/05-test/05-Security-Testing/
```

#### Subfolders

##### owasp-top10/
```yaml
Purpose: OWASP API Security Top 10 testing results
Contents:
  - SECURITY-REPORT-{YYYY-MM-DD}.md (main report)
  - findings/ (detailed per-vulnerability)
    - API1-BOLA.md
    - API2-AUTH.md
    - ... (one per OWASP item)

Report Requirements:
  - Summary table with all 10 items
  - Status per item (PASS/FAIL/WARN/N/A)
  - Detailed findings with evidence
  - Recommendations
```

##### penetration/
```yaml
Purpose: Penetration testing reports
Contents:
  - PENTEST-REPORT-{YYYY-Qn}.md (quarterly reports)

Report Requirements:
  - Scope definition
  - Methodology
  - Findings with severity
  - Remediation status
```

---

## Gitignore Patterns

### Project Root .gitignore
```gitignore
# Testing artifacts - ephemeral files
docs/05-test/*/artifacts/auth_token.txt
docs/05-test/*/artifacts/*.json

# Keep README files
!docs/05-test/*/artifacts/README.md
!docs/05-test/*/artifacts/.gitignore

# Coverage reports (if large/binary)
docs/05-test/02-Unit-Testing/coverage/*.html

# Security testing sensitive data
docs/05-test/05-Security-Testing/*/credentials/
```

### artifacts/.gitignore
```gitignore
# Ignore all files
*

# Except these
!.gitignore
!README.md
```

---

## Cross-Reference Links

### Required README Links

#### Stage 03 README
```markdown
# docs/03-integrate/README.md

## Testing & Validation

The APIs documented in this stage are tested in Stage 05:

- **E2E Testing**: [docs/05-test/03-e2e-testing/](../05-test/03-e2e-testing/)
- **Security Testing**: [docs/05-test/05-Security-Testing/](../05-test/05-Security-Testing/)
- **Latest E2E Report**: [Latest Report](../05-test/03-e2e-testing/reports/)

## SSOT

The `openapi.json` file in this stage is the Single Source of Truth.
Stage 05 should reference this file via symlink or relative path.
```

#### Stage 05 README
```markdown
# docs/05-test/03-e2e-testing/README.md

## API Specifications

Tests in this folder validate the APIs documented in Stage 03:

- **API Reference**: [docs/03-integrate/01-api-specifications/](../../03-integrate/01-api-specifications/)
- **OpenAPI Spec**: [openapi.json](../../03-integrate/01-api-specifications/openapi.json)

## SSOT Note

The `openapi.json` file is maintained in Stage 03.
The `artifacts/openapi.json` in this folder is a symlink, not a copy.
```

---

## Setup Commands

### Create Structure
```bash
# Create Stage 05 E2E testing folders
mkdir -p docs/05-test/03-e2e-testing/{reports,scripts,artifacts,changelogs}

# Create Security testing folders
mkdir -p docs/05-test/05-Security-Testing/{owasp-top10/findings,penetration,scripts}

# Create symlink to Stage 03 openapi.json
cd docs/05-test/03-e2e-testing/artifacts
ln -s ../../../03-integrate/01-api-specifications/openapi.json openapi.json

# Create .gitignore for artifacts
echo -e "*\n!.gitignore\n!README.md" > .gitignore

# Create README for artifacts
cat > README.md << 'EOF'
# Testing Artifacts

This folder contains ephemeral testing artifacts that are NOT committed to git.

## Contents (gitignored)
- `auth_token.txt` - Authentication tokens for test execution
- `test_results_*.json` - Raw test results
- `openapi.json` - Symlink to Stage 03 API spec (SSOT)

## SSOT

The `openapi.json` here is a SYMLINK to:
`docs/03-integrate/01-api-specifications/openapi.json`

Do NOT copy the file - always use the symlink.
EOF
```

### Validate Structure
```bash
# Using SDLC CLI
[SDLC CLI] validate-structure --stage 05

# Manual check
ls -la docs/05-test/03-e2e-testing/artifacts/openapi.json
# Should show: openapi.json -> ../../../03-integrate/...
```

---

## Validation Checklist

### For New Projects
```yaml
Stage 03:
  - [ ] docs/03-integrate/01-api-specifications/ exists
  - [ ] openapi.json present (SSOT)
  - [ ] COMPLETE-API-ENDPOINT-REFERENCE.md present
  - [ ] README.md links to Stage 05

Stage 05 - E2E:
  - [ ] docs/05-test/03-e2e-testing/ exists
  - [ ] reports/, scripts/, artifacts/, changelogs/ subfolders
  - [ ] artifacts/.gitignore configured
  - [ ] artifacts/openapi.json is SYMLINK (not copy)
  - [ ] README.md links to Stage 03

Stage 05 - Security:
  - [ ] docs/05-test/05-Security-Testing/ exists
  - [ ] owasp-top10/ subfolder for OWASP reports
  - [ ] README.md with links

Cross-Reference:
  - [ ] Stage 03 README links to Stage 05
  - [ ] Stage 05 README links to Stage 03
  - [ ] No duplicate openapi.json
```

---

## References

- [E2E API Testing Workflow](../../05-Templates-Tools/02-AI-Tools/testing_e2e-api-testing-workflow.md)
- [Stage Cross-Reference Matrix](../SDLC-Stage-Cross-Reference.md)
- [Security Testing Checklist](../../05-Templates-Tools/02-AI-Tools/testing_security-testing-checklist.md)
- [API Documentation Template](../../05-Templates-Tools/06-Manual-Templates/API-DOCUMENTATION-TEMPLATE.md)
