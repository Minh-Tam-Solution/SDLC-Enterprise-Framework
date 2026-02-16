# Stage 03 ↔ Stage 05 Cross-Reference Matrix

**Version**: 1.0.0
**Framework**: SDLC 6.0.6
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Last Updated**: February 2026

---

## Overview

This document defines the bidirectional cross-reference requirements between Stage 03 (Integration & APIs) and Stage 05 (Testing & Quality). It ensures traceability between API documentation and testing artifacts.

---

## Cross-Reference Matrix

### Stage 03 → Stage 05 Links

```
docs/03-Integration-APIs/
├── 01-API-Contracts/
│   └── README.md                              # Links to integration test results
│
├── 02-API-Specifications/
│   ├── COMPLETE-API-ENDPOINT-REFERENCE.md     # Links to E2E test reports
│   │   └── Per endpoint: Test status, last tested, report link
│   ├── openapi.json                           # SSOT (Single Source of Truth)
│   └── README.md                              # Links to Stage 05 testing folder
│
└── 03-Integration-Guides/
    └── README.md                              # Links to integration test guides
```

### Stage 05 → Stage 03 Links

```
docs/05-Testing-Quality/
├── 03-E2E-Testing/
│   ├── reports/
│   │   └── E2E-API-REPORT-{DATE}.md           # Links to API Reference
│   │       └── Cross-Reference section with Stage 03 links
│   ├── scripts/
│   │   └── test_all_endpoints.py              # Imports openapi.json from Stage 03
│   ├── artifacts/                             # Symlink to Stage 03 spec (NOT duplicate)
│   │   └── openapi.json -> ../../../03-Integration-APIs/02-API-Specifications/openapi.json
│   └── README.md                              # Links to Stage 03 API Specifications
│
├── 04-Integration-Testing/
│   └── README.md                              # Links to Stage 03 API Contracts
│
└── 05-Security-Testing/
    └── README.md                              # Links to Stage 03 for security testing
```

---

## SSOT Principle (Single Source of Truth)

### Definition
The **Single Source of Truth** principle ensures that critical artifacts exist in ONE location only, with other locations referencing (not duplicating) that source.

### Application to API Specification

```yaml
SSOT Configuration:
  Primary Location:
    Path: docs/03-Integration-APIs/02-API-Specifications/openapi.json
    Stage: 03 (Integration & APIs)
    Reason: API design is an integration concern

  Stage 05 Access Methods:
    Option 1 - Symlink (Recommended):
      artifacts/openapi.json -> ../../../03-Integration-APIs/02-API-Specifications/openapi.json

    Option 2 - Relative Path in Scripts:
      SPEC_PATH = "docs/03-Integration-APIs/02-API-Specifications/openapi.json"

    Option 3 - Environment Variable:
      OPENAPI_SPEC_PATH=docs/03-Integration-APIs/02-API-Specifications/openapi.json

  Prohibited:
    - Copying openapi.json to Stage 05
    - Maintaining duplicate copies
    - Auto-generating in multiple locations
```

### Why SSOT Matters

| Without SSOT | With SSOT |
|--------------|-----------|
| Multiple copies drift over time | Single source, always current |
| Confusion about "correct" version | Clear authoritative location |
| Sync issues between stages | Changes propagate automatically |
| Wasted storage and maintenance | Efficient, DRY principle |

---

## Cross-Reference Requirements

### Mandatory Links

#### From Stage 03 (API Reference)

```markdown
# In COMPLETE-API-ENDPOINT-REFERENCE.md

## Cross-Reference Links

### Stage 05 - Testing & Quality
- [E2E Test Reports](../../05-Testing-Quality/03-E2E-Testing/reports/)
- [Security Testing](../../05-Testing-Quality/05-Security-Testing/)
- [Latest E2E Report](../../05-Testing-Quality/03-E2E-Testing/reports/E2E-API-REPORT-{LATEST}.md)

### Per Endpoint
| Endpoint | Test Status | Last Tested | Report Link |
|----------|-------------|-------------|-------------|
| POST /auth/login | PASS | 2026-02-15 | [Link](../../05-Testing-Quality/...) |
```

#### From Stage 05 (E2E Report)

```markdown
# In E2E-API-REPORT-{DATE}.md

## Cross-Reference

### Stage 03 - Integration & APIs
- **API Documentation**: [Complete API Reference](../../../03-Integration-APIs/02-API-Specifications/COMPLETE-API-ENDPOINT-REFERENCE.md)
- **OpenAPI Spec**: [openapi.json](../../../03-Integration-APIs/02-API-Specifications/openapi.json)
- **API Design Decisions**: [ADRs](../../../03-Integration-APIs/01-API-Contracts/)
```

### README Cross-References

#### Stage 03 README

```markdown
# docs/03-Integration-APIs/README.md

## Related Stages

### Stage 05 - Testing & Quality
This stage's API specifications are tested in Stage 05:
- [E2E Testing](../05-Testing-Quality/03-E2E-Testing/)
- [Integration Testing](../05-Testing-Quality/04-Integration-Testing/)
- [Security Testing](../05-Testing-Quality/05-Security-Testing/)

**Note**: Test reports link back to this stage's API documentation for traceability.
```

#### Stage 05 README

```markdown
# docs/05-Testing-Quality/03-E2E-Testing/README.md

## Related Stages

### Stage 03 - Integration & APIs
Tests in this folder validate the APIs documented in Stage 03:
- [API Specification](../../03-Integration-APIs/02-API-Specifications/) (SSOT for openapi.json)
- [API Reference](../../03-Integration-APIs/02-API-Specifications/COMPLETE-API-ENDPOINT-REFERENCE.md)

**SSOT Note**: openapi.json is maintained in Stage 03. Use symlink or relative path to access.
```

---

## Validation Rules

### Automated Checks

```yaml
Cross-Reference Validation:
  Stage 03 Checks:
    - [ ] API Reference contains "Cross-Reference Links" section
    - [ ] Links to Stage 05 reports are valid (not 404)
    - [ ] Per-endpoint test status is present
    - [ ] openapi.json exists and is valid JSON

  Stage 05 Checks:
    - [ ] E2E reports contain "Cross-Reference" section
    - [ ] Links to Stage 03 API Reference are valid
    - [ ] No duplicate openapi.json (only symlink/reference allowed)
    - [ ] README links to Stage 03

  Bidirectional Checks:
    - [ ] Can navigate: Stage 03 → Stage 05 → Stage 03
    - [ ] All relative paths resolve correctly
    - [ ] No broken links between stages
```

### CLI Validation

```bash
# Validate cross-references
[SDLC CLI] validate-cross-reference \
  --stage-03 docs/03-Integration-APIs \
  --stage-05 docs/05-Testing-Quality

# Expected output
Cross-Reference Validation Report
=================================
Stage 03 → Stage 05: PASS (5 links validated)
Stage 05 → Stage 03: PASS (3 links validated)
SSOT Compliance: PASS (no duplicate openapi.json)
Bidirectional: PASS (all navigation paths work)

Overall: PASS
```

---

## Future Extensions

This matrix pattern can be extended to other stage relationships:

### Stage 01 ↔ Stage 02 (Requirements → Design)
```yaml
Stage 01 (Requirements):
  - User stories link to design specs
  - Acceptance criteria link to test plans

Stage 02 (Design):
  - Design specs reference requirements
  - Architecture decisions trace to user needs
```

### Stage 02 ↔ Stage 04 (Design → Implementation)
```yaml
Stage 02 (Design):
  - Technical specs link to code modules
  - ADRs link to implementing code

Stage 04 (Build):
  - Code comments reference design docs
  - Module READMEs link to specs
```

### Stage 04 ↔ Stage 05 (Implementation → Testing)
```yaml
Stage 04 (Build):
  - Code modules link to test files
  - Coverage reports link to source

Stage 05 (Testing):
  - Test files reference code under test
  - Test reports link to source code
```

---

## Implementation Checklist

### For New Projects

```yaml
Setup Checklist:
  Stage 03:
    - [ ] Create docs/03-Integration-APIs/02-API-Specifications/
    - [ ] Add COMPLETE-API-ENDPOINT-REFERENCE.md (use template)
    - [ ] Export openapi.json from API
    - [ ] Add Cross-Reference Links section
    - [ ] Update README with Stage 05 links

  Stage 05:
    - [ ] Create docs/05-Testing-Quality/03-E2E-Testing/
    - [ ] Create reports/, scripts/, artifacts/ subfolders
    - [ ] Add symlink to Stage 03 openapi.json
    - [ ] Add README with Stage 03 links
    - [ ] Generate first E2E report with cross-references
```

### For Existing Projects

```yaml
Migration Checklist:
  - [ ] Identify current openapi.json locations
  - [ ] Consolidate to Stage 03 (SSOT)
  - [ ] Replace duplicates with symlinks
  - [ ] Add Cross-Reference sections to docs
  - [ ] Validate with SDLC CLI cross-reference validator
```

---

## References

- [RFC-SDLC-602-E2E-API-TESTING](../../09-Continuous-Improvement/RFC/RFC-SDLC-602-E2E-API-TESTING.md)
- [E2E API Testing Workflow](../../05-Templates-Tools/02-AI-Tools/testing_e2e-api-testing-workflow.md)
- [Testing Artifacts Structure](./Documentation-Standards/SDLC-Testing-Artifacts-Structure.md)
- [API Documentation Template](../../05-Templates-Tools/06-Manual-Templates/API-DOCUMENTATION-TEMPLATE.md)
