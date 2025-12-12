# PRE-COMMIT HOOKS LIST (v4.6)

## Purpose

Local enforcement layer to prevent low-quality or non-compliant changes from entering version control; complements CI gates. Enhanced for SDLC 4.6 with Zero Mock Tolerance enforcement and Testing Standards Integration.

## Hook Suite Overview

| Order | Hook Name | Function | Block Condition |
|-------|-----------|----------|-----------------|
| 5 | **mock-detection-v3** | **SDLC 4.6: Zero Mock Tolerance enforcement** | **Any mock instance detected** |
| 10 | check-python-format | Run black / isort on staged python | Formatting diff after auto-fix |
| 15 | check-ts-format | Run prettier on TS/JS | Formatting diff after auto-fix |
| 20 | lint-python | Run flake8 / mypy (fast mode) | Errors present |
| 25 | lint-ts | Run eslint (changed files) | Errors present |
| 30 | scan-secrets | Detect secrets via regex & entropy | Any secret hit without whitelist |
| 35 | enforce-design-tags | Verify new/changed files reference REQ/DES IDs in header comment if app logic | Missing ID annotation |
| 40 | forbid-direct-migrations | Block raw SQL migration edits unless flagged | Direct SQL without ALLOWED override |
| 45 | cultural-why-presence | Ensure user-facing text has cultural tag markers | Missing WHY tag in changed localization strings |
| 50 | openapi-sync-reminder | If backend endpoint added, ensure openapi spec staged | No spec change & new route signature |
| 55 | test-id-linker | Verify new test names include ID pattern (TC-*) | Missing pattern |
| 60 | **vietnamese-authenticity** | **SDLC 4.6: Validate BHXH/VAT calculations** | **Inauthentic rates detected** |

## Annotations Standard

Header comment example (Python):

```python
# REQ: REQ-AUTH-001 | DES: DES-AUTH-010
```

Header comment example (TypeScript):

```typescript
// REQ: REQ-AUTH-001 | DES: DES-AUTH-010
```

## Installation

1. Add hook scripts under `.githooks/` (planned path).
2. Configure in `.git/config`:
   core.hooksPath=.githooks
3. Make scripts executable: `chmod +x .githooks/*`

## Metrics Captured

| Metric | Description | Source |
|--------|-------------|--------|
| hooks_run | Count of executed hooks | wrapper script |
| hooks_failed | Count of failures | wrapper script |
| design_tag_missing | Missing design annotation events | enforce-design-tags |
| secret_hits | Potential secret detections | scan-secrets |

## Failure Handling

- Developer may rerun after fixing; no bypass unless documented emergency.
- Emergency bypass requires: `EMERGENCY-BYPASS.md` entry referencing incident ticket.

## Roadmap

- Central wrapper to emit JSON summary for compliance_report.
- Pre-push hook layering (run focused test subset).
- Auto-suggest missing REQ/DES from similarity search.

Last updated: v0.1 scaffold
