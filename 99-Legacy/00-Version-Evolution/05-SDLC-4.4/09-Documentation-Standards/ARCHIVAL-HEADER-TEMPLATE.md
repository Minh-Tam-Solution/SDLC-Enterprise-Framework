# 🔒 Archival Header (Standard Template)

> Apply this unmodified at the very top of any document or appendix that has been superseded.

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

## Usage Rules

- Do not edit archived body content except to insert this header.
- If partial extraction, clearly mark each extracted block with "BEGIN LEGACY BLOCK &lt;ID&gt;" / "END LEGACY BLOCK &lt;ID&gt;".
- For merged content, include mapping table referencing new locations.

## Mapping Table Example

| Legacy Element | New Location (4.4) | Status | Notes |
|----------------|--------------------|--------|-------|
| Role Compliance Checker v4.3 | Implementation Guide §2.2 Adaptive Checker | Replaced | Added coverage + continuity hooks |
| Framework Validation Suite 4.3 | Adaptive Validation Suite §9 | Extended | Added drift & anomaly placeholders |

## Integrity Workflow (Planned)

1. Generate SHA256 of frozen legacy file.
2. Store hash chain segment in continuity ledger (Phase 2).
3. Link ledger reference in INTEGRITY HASH field.

## Color Coding (Optional in HTML Export)

- ARCHIVED banner: amber
- SUPERSEDED pointer: green link to active doc
- RETENTION badges: distinct neutral tones

## Anti-Patterns

- Copying active content into legacy file (duplication drift risk)
- Editing legacy text to match new terminology (breaks historical evidence)
- Removing rationale/context sections

## Migration Decision Log (Embed if complex)

| Decision | Date | Driver | Impact | Owner |
|----------|------|--------|--------|-------|
| Consolidate 4.3 scripts into Appendix | 2025-09-16 | Reduce inline clutter | Easier maintenance | CPO Office |

---
End of template.
