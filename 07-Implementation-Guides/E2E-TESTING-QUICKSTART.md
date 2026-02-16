# E2E API Testing Quick Start (SDLC 6.0.6)

**Version**: 1.0.0
**Date**: February 2, 2026
**Status**: ACTIVE
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Audience**: Developers, QA Engineers, Tech Leads

---

## Overview

This guide helps you set up standardized E2E API testing in under 30 minutes using SDLC 6.0.6 templates and workflows.

**Time Savings**: 3 hours (manual) → 30 minutes (with templates)

---

## Prerequisites

- [ ] OpenAPI 3.0+ specification (Stage 03: `docs/03-integrate/02-API-Specifications/openapi.json`)
- [ ] Test credentials (API keys, OAuth tokens)
- [ ] e2e-api-testing skill v1.2.0+ (Claude Code skill)
- [ ] sdlcctl CLI installed (optional, for automation)

**Framework References**:
- [E2E API Testing Methodology](../02-Core-Methodology/SDLC-E2E-API-Testing-Methodology.md) - 6-Phase workflow
- [SSOT Principle](../02-Core-Methodology/SDLC-SSOT-Principle.md) - Single Source of Truth guidelines

---

## 5-Minute Setup

### Step 1: Verify Stage 03 Documentation (Phase 0: SSOT Check)

```bash
# Check API documentation exists (SSOT compliance)
find . -name "openapi.json" -type f
# Expected: EXACTLY ONE file at docs/03-integrate/02-API-Specifications/openapi.json

# Validate OpenAPI spec quality
sdlcctl validate --stage 03 --check api-docs

# Expected output:
# ✅ openapi.json found at docs/03-integrate/02-API-Specifications/openapi.json
# ✅ SSOT Compliance: PASS (no duplicates)
# ✅ 58 endpoints defined
# ✅ Schema validation PASSED
```

**Reference**: [SSOT Compliance Checklist](../05-Templates-Tools/05-Checklists/SSOT-COMPLIANCE-CHECKLIST.md)

### Step 2: Create Testing Folder Structure (Stage 05 Setup)

```bash
# Create SDLC 6.0.6 compliant folder structure
mkdir -p docs/05-test/03-E2E-Testing/{reports,scripts,artifacts,security-tests}

# Initialize README with SSOT cross-reference
cat > docs/05-test/03-E2E-Testing/README.md << 'EOF'
# E2E API Testing

**Stage**: 05-TEST
**Framework**: SDLC 6.0.6
**Cross-Reference**: [Stage 03 API Specifications](../../03-integrate/02-API-Specifications/)

## Contents

- `reports/` - E2E test reports (E2E-API-REPORT-YYYY-MM-DD.md)
- `scripts/` - Test scripts and automation
- `artifacts/` - Test data and fixtures
- `security-tests/` - OWASP API Top 10 security test results

## SSOT Principle

**Canonical API Spec**: [openapi.json](../../03-integrate/02-API-Specifications/openapi.json)

**DO NOT COPY** - Always reference Stage 03 canonical source. Use symlinks if needed.

## Stage 03 ↔ Stage 05 Links

| API Document (Stage 03) | Test Report (Stage 05) |
|-------------------------|------------------------|
| [openapi.json](../../03-integrate/02-API-Specifications/openapi.json) | [Latest Report](reports/) |
| API Endpoint Reference (see project's API docs) | [Test Coverage](reports/) |
EOF
```

**Reference**: [E2E API Test Report Template](../05-Templates-Tools/06-Manual-Templates/E2E-API-TEST-REPORT-TEMPLATE.md)

### Step 3: Run E2E Tests (Phase 2: Test Execution)

```bash
# Option 1: Using e2e-api-testing skill (Claude Code)
/e2e-api-testing --openapi docs/03-integrate/02-API-Specifications/openapi.json

# Option 2: Using sdlcctl CLI (automated)
sdlcctl e2e validate \
  --openapi docs/03-integrate/02-API-Specifications/openapi.json \
  --min-pass-rate 80

# Option 3: Manual testing (curl/Postman)
# See: E2E API Test Report Template for manual test checklist
```

**Reference**: [E2E API Testing Methodology - Phase 2](../02-Core-Methodology/SDLC-E2E-API-Testing-Methodology.md#phase-2-test-execution-automated--manual)

### Step 4: Validate Cross-References (Phase 5: Cross-Ref Validation)

```bash
# Validate Stage 03 ↔ 05 bidirectional links
sdlcctl e2e cross-reference \
  --stage-03 docs/03-integrate \
  --stage-05 docs/05-test

# Expected output:
# ✅ Cross-reference validation PASSED
# ✅ 58 endpoints linked to test reports
# ✅ SSOT: openapi.json in Stage 03 (no duplicates)
# ✅ Bidirectional links verified
```

**Reference**: [E2E API Testing Methodology - Phase 5](../02-Core-Methodology/SDLC-E2E-API-Testing-Methodology.md#phase-5-cross-reference-validation)

### Step 5: Check OWASP Compliance

```bash
# Run security tests using OWASP API Top 10 checklist
/e2e-api-testing --mode security --owasp-checklist

# Manual checklist at:
# SDLC-Enterprise-Framework/05-Templates-Tools/02-AI-Tools/testing_security-testing-checklist.md
```

---

## Expected Outcome

After completing this guide:

| Metric | Target |
|--------|--------|
| **Setup Time** | < 30 minutes |
| **E2E Report** | Generated in `reports/E2E-API-REPORT-YYYY-MM-DD.md` |
| **Cross-References** | Stage 03 ↔ 05 validated |
| **OWASP Coverage** | All 10 items checked |
| **Pass Rate** | ≥ 80% (minimum threshold) |

---

## Templates Reference

| Template | Location | Purpose |
|----------|----------|---------|
| **E2E Workflow** | `05-Templates-Tools/02-AI-Tools/testing_e2e-api-testing-workflow.md` | 6-phase testing process |
| **Security Checklist** | `05-Templates-Tools/02-AI-Tools/testing_security-testing-checklist.md` | OWASP API Top 10 |
| **Stage Cross-Reference** | `02-Core-Methodology/SDLC-Stage-Cross-Reference.md` | Stage 03 ↔ 05 traceability |
| **Artifacts Structure** | `02-Core-Methodology/Documentation-Standards/SDLC-Testing-Artifacts-Structure.md` | Folder layout |

---

## CLI Commands Reference

### E2E Validation

```bash
# Basic validation
sdlcctl e2e validate --openapi <path>

# With minimum pass rate
sdlcctl e2e validate --openapi <path> --min-pass-rate 80

# Verbose output
sdlcctl e2e validate --openapi <path> --verbose
```

### Cross-Reference Validation

```bash
# Validate Stage 03 ↔ 05 links
sdlcctl e2e cross-reference \
  --stage-03 <stage-03-path> \
  --stage-05 <stage-05-path>

# Check specific files
sdlcctl e2e cross-reference \
  --openapi docs/03-Integration-APIs/openapi.json \
  --test-report docs/05-Testing-Quality/03-E2E-Testing/reports/latest.md
```

### Report Generation

```bash
# Generate report from test results
sdlcctl e2e generate-report \
  --results test-results.json \
  --output reports/ \
  --openapi docs/03-Integration-APIs/openapi.json
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `openapi.json not found` | Ensure file is at `docs/03-Integration-APIs/02-API-Specifications/openapi.json` |
| `Cross-reference FAILED` | Add links in Stage 05 README pointing to Stage 03 |
| `SSOT violation` | Remove duplicate openapi.json from Stage 05 (only keep in Stage 03) |
| `Pass rate below threshold` | Fix failing tests or adjust `--min-pass-rate` |

### Getting Help

- **RFC**: RFC-SDLC-602-E2E-API-TESTING (see Orchestrator `docs/` for implementation details)
- **SDLC Orchestrator Team**: Slack #sdlc-orchestrator
- **FAQ**: See below

---

## FAQ

### Q: Why Stage 03 and Stage 05?

**A**: Stage 03 (INTEGRATE) contains API contracts/specifications. Stage 05 (TEST) contains test reports. Cross-referencing ensures every API endpoint is tested and every test links back to its specification.

### Q: What is SSOT?

**A**: Single Source of Truth. The `openapi.json` file should exist ONLY in Stage 03. Stage 05 should reference it via links, not duplicate it.

### Q: How often should I run E2E tests?

**A**:
- **CI/CD**: On every PR merge to main
- **Scheduled**: Nightly for comprehensive testing
- **Manual**: After significant API changes

### Q: What's the minimum pass rate?

**A**:
- **LITE tier**: 60%
- **STANDARD tier**: 70%
- **PROFESSIONAL tier**: 80%
- **ENTERPRISE tier**: 90%

### Q: How do I integrate with GitHub Actions?

**A**: See the workflow template in `testing_e2e-api-testing-workflow.md` Phase 6 (CI/CD Integration).

---

## Next Steps

1. **Run First Test**: Follow steps 1-5 above
2. **Review Report**: Check generated E2E report for failures
3. **Fix Issues**: Address failing tests
4. **OWASP Security**: Complete security checklist
5. **CI/CD**: Integrate into pipeline

---

**Questions?** Reach out to the SDLC Orchestrator team.

---

*RFC: RFC-SDLC-602-E2E-API-TESTING*
*CTO Approval: February 2, 2026 (9.2/10)*
*Sprint: 137 (Templates) + 138 (Validation & Release)*
