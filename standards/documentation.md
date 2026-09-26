# Documentation standards

> Who reads this: whoever writes a document, a spec, an ADR or a source file, and whoever writes a tool that reads them.
> When: before creating a file, and when a checker reports a missing field.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
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

Directly under the title — five required fields, checked by gate DOC-2 ([`scripts/check-doc-ownership.sh`](../scripts/check-doc-ownership.sh)):

```markdown
# Payment retry design

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: <role or handle>
**Consumer**: <who reads or runs it>
**Review by**: 2026-12-26
```

| Field | Meaning | Rule |
|---|---|---|
| `SDLC Framework Version` | the framework version this document was last checked against | counted by `scripts/check-version-declared.sh`; older than current is legal and counted, missing is the finding |
| `Status` | `DRAFT` · `ACTIVE` · `DEPRECATED` · `SUPERSEDED` · `ARCHIVED` ([`policies/artifact-lifecycle.md`](../policies/artifact-lifecycle.md)) | `DEPRECATED` and `SUPERSEDED` name the successor on the next line |
| `Owner` | who answers questions about it and keeps it true | a role or handle that exists today |
| `Consumer` | who reads or runs it, and when | named; "everyone" is not a consumer |
| `Review by` | ISO date by which the owner re-checks it | a passed date blocks (DOC-2); after review, move the date — do not bulk-bump it |

**Optional:** `Version` — only for an artifact others depend on by version (a contract, a template consumed elsewhere). Otherwise git already versions the file, and a hand-kept number drifts. Do not add a `Last updated` field: git knows when the file changed, and a hand-kept date goes stale.

A status field is a claim, not a measurement. When a document says *what is running*, it names the command or probe that shows it; otherwise `Review by` is the claim's expiry date.

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

## One home per fact

Every fact — a contract, a schema, a status, a setting, a number — has **one authoritative home**. Everywhere else links to it, imports it or is generated from it; nothing restates it by hand. "One topic, one living document" ([`project-structure.md`](project-structure.md#the-docs-tree)) is the same rule for topics; agent context files point instead of copying ([`context-and-hats`](../ai-engineering/context-and-hats.md)).

| Rule | Means | Candidate rule (command idea) |
|---|---|---|
| **Name the home first** | before writing a fact, find or name its home; a second place that needs it links there | count files of a known kind (an API description, `.env.example`) outside their home |
| **Derived is generated** | a file made from another — an endpoint list from the API description, a vendor adapter from the policy — is produced by a command, carries a line saying so (`Code generated … DO NOT EDIT.`), and CI regenerates it and expects an empty diff. A committed copy is fine; an unchecked one is drift | regenerate and diff |
| **State is written once** | the current sprint, the release in production, a gate's status live in one file with one owner; other documents name that file, never the value | compare the state file's last change with the latest merge that should have moved it |
| **One writer per section** | a file written by both a person and a tool is split into fenced sections; the tool regenerates only its fence, and people do not edit inside it | regenerate the fenced block and diff |
| **Configuration inherits** | shared settings live at one root; lower levels extend it and override only what differs | list configuration files that do not extend the root |

- *Burn case:* a team's "current sprint" read differently in four documents; three sprints closed without the documents moving (a 27-day lag), and untangling the direction took two weeks. The lesson recorded then still holds: one source is useless if nothing notices when the others diverge.
- *Burn case:* a duplicate-file hook excluded a folder name that did not match the real home, so it counted the one legitimate file as a duplicate and would have blocked every commit containing it. Nobody had run it red and green ([`gates.md`](../controls/gates.md), G3). A duplicate check needs a planted copy that must fail and the real home that must pass.
- **Not kept from v6:** context "zones" ranked by authority, "higher authority wins" conflict rules, freshness timers and a context-refresh service, symlinks as the default, a fixed canonical path per artifact type, "never commit a generated copy". None enter the rule register; each candidate above climbs through [`lessons-to-rules.md`](../practices/lessons-to-rules.md).

## Archived documents

A document moved to `archive/` (in a product repo: `docs/10-archive/`) is **not edited**: no header is added, nothing is reworded. The move itself is the record — a `git mv` commit — and where its content went is recorded outside it: in this repository in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md), in a product repo in the archive folder's README. Editing an archived file to add a notice would make it no longer the thing that was archived ([`policies/artifact-lifecycle.md`](../policies/artifact-lifecycle.md)).

## Checking

These standards become gates through [`lessons-to-rules.md`](../practices/lessons-to-rules.md): a rule row with a burn case and a command, starting at `ADVISORY` with a counter and a deadline ([`gates.md`](../controls/gates.md)). A standard with no command behind it is a request, and it drifts. The candidates, each with its burn case, are listed in [`rule-contract.md`](../controls/rule-contract.md) once proposed.

## Sources

From the archive: the rows for this standard in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

Current practice, each opened on the date shown:

- The Pragmatic Programmer — Pragmatic Programmer Tips (tip 15, DRY) — <https://pragprog.com/tips/> (accessed 2026-09-26)
- Software Engineering at Google, ch. 10 — Documentation — <https://abseil.io/resources/swe-book/html/ch10.html> (accessed 2026-09-26)
- Write the Docs — Docs as Code — <https://www.writethedocs.org/guide/docs-as-code/> (accessed 2026-09-26)
- Go command documentation — Generate Go files by processing source (generated-file marker) — <https://pkg.go.dev/cmd/go> (accessed 2026-09-26)
- GitHub Docs — Customizing how changed files appear on GitHub (marking generated files) — <https://docs.github.com/en/repositories/working-with-files/managing-files/customizing-how-changed-files-appear-on-github> (accessed 2026-09-26)
- GitHub Docs — About code owners (one owner per path, last match wins) — <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners> (accessed 2026-09-26)
