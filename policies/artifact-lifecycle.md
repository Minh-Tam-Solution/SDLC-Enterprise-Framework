# Artifact lifecycle

> Who reads this: whoever adds, renames, moves, deprecates or archives a document, a script, a workflow or a template in this repository.
> When: before the change, not after a consumer reports a broken link.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: maintainers changing or retiring an artifact; consuming repos that follow links into this one
**Review by**: 2026-12-26

*Shortens:* the time from "this moved" to every consumer finding its new place, and the arguments about whether an old document still counts.

## The rule

**Validity and a successor decide the status of an artifact. Its age and the framework version it was written for do not.** A document written for 4.9 that is still true stays live under 8.0; a document written last week that is wrong is retired today.

## Statuses

The `Status` field in a document header ([`standards/documentation.md`](../standards/documentation.md)) takes one of these values.

| Status | Means | Required alongside it |
|---|---|---|
| `DRAFT` | proposed; nothing depends on it yet | an owner |
| `ACTIVE` | in force; consumers may rely on it | owner, consumer, review-by date (gate DOC-2) |
| `DEPRECATED` | still in force, being replaced | the successor and a removal date on the next line |
| `SUPERSEDED` | no longer in force; a successor answers the same question | the successor on the next line |
| `ARCHIVED` | moved to `archive/`; a record, never edited again | a row in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md) |

## Transitions

| Change | Do | Evidence |
|---|---|---|
| Rename or move a live file | `git mv`; a move and a content change are separate commits | a row in the MIGRATION-MAP path map; the path-map check prints `0` |
| Rename something executable (script, workflow, table heading, CLI flag) | keep the old name working with a deprecation notice and a removal date | the old name has a selftest case; the removal date is in the notice |
| Replace a document | write the successor first; mark the old one `SUPERSEDED` or archive it | successor linked from the old header or its MIGRATION-MAP row |
| Archive | `git mv` into `archive/`; do not edit the moved file | a MIGRATION-MAP row with an outcome (`ADOPTED` · `PARTIALLY_ADOPTED` · `SUPERSEDED` · `RETIRED` · `HISTORICAL_ONLY`) |
| Delete | only content that is wrong in a harmful way: a secret, a vulnerable instruction, personal data | the deletion commit says why; a leaked secret is rotated — deleting it from the tree does not un-leak it |

Before any rename or move, search the known consuming repositories for the old path. A reference pinned to a commit SHA keeps working; a reference to a branch breaks. Name the consumers in the PR.

## The archive

- `archive/**` is the payload: moved files, byte-identical, never edited. That is what makes it evidence.
- `archive/README.md` and `archive/INDEX.md` are **living navigation**: they describe what is in the archive and are kept current. Fixing them is not editing the record.
- Where the knowledge in an archived file went is recorded in `MIGRATION-MAP.md`, never by editing the file. A source with no row there has not been reviewed yet.
- Agents do not read `archive/` unless the person asks for history. Archived text in an agent's context competes with the live rules and loses nothing when absent.
- Live documents do not link into `archive/` for rules. To reuse an archived idea, harvest the claim into the live document that owns the topic and record the row.

## Review

`Review by` is a date, not a decoration. When it passes, gate DOC-2 turns the document red. The owner re-checks the content, then either moves the date (content still true), rewrites (content changed), or changes the status (content replaced). Never move every date at once: a bulk bump is a review that did not happen.

## Not yet checked by a machine

- **Broken internal links.** Checked by hand at every move so far (2026-09-26: relative links resolved, two example placeholders excepted). Candidate rule: a link checker over live documents, entering at `ADVISORY` through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md).
- **Signed release tags.** Release tags are annotated tags on a merge commit; they are not GPG-signed today.
