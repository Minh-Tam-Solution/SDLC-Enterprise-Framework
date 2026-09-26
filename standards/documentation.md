# Documentation standards

> Who reads this: whoever writes a document, a spec, an ADR or a source file, and whoever writes a tool that reads them.
> When: before creating a file, and when a checker reports a missing field.

**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: authors of documents, specs, ADRs and source files; tools that read them
**Review by**: 2026-12-26

*Shortens:* the time to tell whether a document is current, who owns it, and which design a piece of code implements.

## File names

- Documents: kebab-case, `.md`. Words say what the document is about: `authentication-api-design.md`, `database-migration-guide.md`. Capitalised words are accepted (`Authentication-API-Design.md`); pick one style per repo.
- IDs lead when the document has one: `ADR-004-event-bus-choice.md`, `SPEC-0012-payment-retry.md`.
- **Never in a living document's name, folder or heading:** version numbers (`v2`, `v7/`, `rev3`, `6.3.0`) — a heading is a link anchor, so it breaks links the same way a file name does, sprint or phase numbers, status words (`draft`, `final`, `new`, `old`, `wip`, `temp`), team or person names. The name outlives all of them. Version and status belong in the header.
- **Dated records are the exception.** A record of something that happened on a day — a meeting, a directive, a review, a hand-over, an incident, a sprint log — carries the date in its name (`review-payment-service-2026-09-26.md`) and is never edited afterwards; a correction is a new record that links the old one. Records live in `08-collaborate/`, `09-govern/` or `07-operate/incidents/`, never in the stage folders that hold living documents.
- Code files follow the language's own convention (`snake_case.py`, `kebab-case.ts` or `PascalCase.tsx` for components, `YYYYMMDDHHMM_description.sql` for migrations). Short, no version numbers, no person names.

## Header of a living document

Directly under the title:

```markdown
# Payment retry design

**Version**: 1.2.0
**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: <role or handle>
**Consumer**: <who reads or runs it>
**Review by**: 2026-12-26
**Last updated**: 2026-09-26
```

| Field | Meaning | Rule |
|---|---|---|
| `Version` | the document's own semver | bump when content changes meaning; independent of the framework version |
| `SDLC Framework Version` | the framework version this document was last checked against | counted by `scripts/check-version-declared.sh`; older than current is legal and counted, missing is the finding |
| `Status` | `DRAFT` · `ACTIVE` · `SUPERSEDED` · `ARCHIVED` | `SUPERSEDED` names its successor on the next line |
| `Owner` | who answers questions about it and keeps it true | a role or handle that exists today |
| `Consumer` | who reads or runs it, and when | named; "everyone" is not a consumer |
| `Review by` | ISO date by which the owner re-checks it | a passed date blocks (DOC-2); after review, move the date — do not bulk-bump it |
| `Last updated` | ISO date of the last change of meaning | a typo fix does not change it |

A status field is a claim, not a measurement. When a document says *what is running*, it names the command or probe that shows it; otherwise `Last updated` is the claim's expiry date.

## Front matter: two schemas, chosen by document kind

Specs and ADRs carry YAML front matter so tools can index them. **They are two different schemas.** A checker classifies the file first, then applies the matching schema. Do not give an ADR `spec_*` fields to satisfy a checker that reads everything as a spec; fix the checker.

Classification: a file under a `01-ADRs/` folder, or with an `adr_id` field, is an ADR. Any other file with `spec_id` is a spec. A file with both is an error.

| Field | Spec | ADR | Values |
|---|---|---|---|
| id | `spec_id` | `adr_id` | `SPEC-NNNN` · `ADR-NNN`, unique in the repo |
| name | `spec_name` | `adr_name` | human-readable |
| version | `spec_version` | `adr_version` | semver string |
| `status` | required | required | spec: `draft` · `review` · `approved` · `implemented` · `deprecated`; ADR: `proposed` · `accepted` · `superseded` · `deprecated` · `rejected` (lower-case) |
| `sdlc_framework` | required | required | framework version the document was last checked against, e.g. `"7.0.0"` |
| `tier` | required | required | `LITE` · `STANDARD` · `PROFESSIONAL` · `ENTERPRISE` (one value) |
| `stage` | required | required | `"00"`…`"09"` as a string; ADRs are normally `"02"` |
| `category` | required | optional | `functional` · `technical` · `security` · `performance` · `integration` |
| `owner` | required | required | role or handle |
| `created`, `last_updated` | required | required | ISO dates |
| `related_adrs`, `related_specs` | optional | optional | lists of ids |
| `supersedes` / `superseded_by` | optional | required when status is `superseded` | id |

Spec body sections, in order: overview · context · requirements (with acceptance criteria) · design decisions (link ADRs, do not copy them) · technical specification · dependencies. ADR body: context · decision · consequences · alternatives rejected, with reasons.

## Header of a source file

Every source file in a code folder, from STANDARD up, starts with a short header in the language's comment syntax:

```python
# Purpose: retry failed card captures with an idempotency key.
# Design: docs/02-design/SPEC-0012-payment-retry.md
```

| Field | Rule |
|---|---|
| `Purpose` | one line: what this file does, not how |
| `Design` | repo-relative path of the spec or ADR it implements; the path must exist. Write `Design: none` for utilities with no design document — said out loud, not left blank |
| `Covers` (test files, instead of `Design`) | the source path or spec id the tests exercise |

Not required in generated files, migrations (the migration name carries the purpose), or files under 20 lines. Version, author and date are not in the header: git holds them and never lets them drift.

## Archived documents

A document moved to `10-archive/` (or `archive/` in this repository) keeps its content and gains, directly under the title:

```markdown
> **ARCHIVED** 2026-09-26 — superseded by [new-document.md](../path/new-document.md). Read-only.
```

Archived documents are never updated, only linked.

## Checking

These standards become gates through [`lessons-to-rules.md`](../practices/lessons-to-rules.md): a rule row with a burn case and a command, starting at `ADVISORY` with a counter and a deadline ([`gates.md`](../controls/gates.md)). A standard with no command behind it is a request, and it drifts. The candidates, each with its burn case, are listed in [`rule-contract.md`](../controls/rule-contract.md) once proposed.
