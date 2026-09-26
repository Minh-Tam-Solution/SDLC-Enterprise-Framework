# 07 — Stage lifecycle

> Who reads this: whoever starts a project, plans a sprint, or asks "are we ready to move on?"
> When: at project start, at each stage exit, and when a reviewer asks where a document belongs.

**SDLC Framework Version**: 7.0.0

*Shortens:* the argument about what "done" means for a stage, and the search for where a decision was written.

## Ten stages, one question each

Every piece of work passes through the same ten questions. A stage is a question you must be able to answer with a document or a check, not a phase on a calendar.

| # | Stage | Question | Docs folder | Stage gate |
|---|---|---|---|---|
| 00 | FOUNDATION | Why build it? Is the problem real? | `docs/00-foundation/` | G0.1 problem validated · G0.2 solutions explored |
| 01 | PLANNING | What exactly will it do? | `docs/01-planning/` | G1 requirements agreed |
| 02 | DESIGN | How will it work? | `docs/02-design/` | G2 architecture validated |
| 03 | INTEGRATE | How does it connect to other systems? | `docs/03-integrate/` | G2 (same gate, integration side) |
| 04 | BUILD | Are we building it right? | `docs/04-build/` | G3 code + tests validated |
| 05 | TEST | Does it work correctly? | `docs/05-test/` | G3 (same gate, test side) |
| 06 | DEPLOY | Can we ship it safely? | `docs/06-deploy/` | G4 deployed successfully |
| 07 | OPERATE | Is it running reliably? | `docs/07-operate/` | G4 (same gate, operations side) |
| 08 | COLLABORATE | Is the team working together effectively? | `docs/08-collaborate/` | none — runs throughout |
| 09 | GOVERN | Is it compliant and still worth running? | `docs/09-govern/` | G4 onwards, recurring |

- **Stages are not a waterfall.** Code is written from stage 02 onwards; a bug fix may touch 04–06 in one day. The stages say *which question a document answers*, not *when* it may be written.
- **Stage gates are decision points; [`gates.md`](../controls/gates.md) gates are scripts.** A stage gate is passed when its evidence exists and, where the tier requires it, the right person has signed. Every piece of evidence that a script can check should be checked by one.
- Folder layout, required files per tier and naming: [`project-structure.md`](../standards/project-structure.md) and [`documentation.md`](../standards/documentation.md).

## Exit evidence per stage

"Minimum" applies to every tier that requires the stage. "PROFESSIONAL+" is added on top for PROFESSIONAL and ENTERPRISE ([`tiers.md`](../controls/tiers.md)).

| # | Minimum to exit | PROFESSIONAL+ adds |
|---|---|---|
| 00 | problem statement · business case (who pays, what it saves or earns) · evidence the problem exists (user interviews, tickets, numbers) | personas · alternatives considered and rejected, with reasons |
| 01 | requirements with acceptance criteria · scope in/out · first API or data sketch | data model · legal and data-residency check · non-functional targets with numbers |
| 02 | ADRs for every decision that is expensive to reverse · one architecture diagram | security architecture · risk-floor paths declared ([`risk-floor-paths.md`](../controls/risk-floor-paths.md)) |
| 03 | skip if there are no integrations; otherwise the contract of each external call | contract tests · failure behaviour of each dependency written down |
| 04 | code merged · tests for the changed behaviour · README runs as written | CI green on the merge commit · fresh-context review artifact bound to the commit ([`tiers.md`](../controls/tiers.md)) |
| 05 | unit tests pass · one smoke test against a real environment | integration + end-to-end tests · performance measured, not estimated |
| 06 | deployment guide someone other than the author has followed · one successful deploy | automated deploy · rollback tested with a timed restore · deploy log |
| 07 | uptime check · error logging someone reads | SLOs with a probe · on-call named · incident records carry `price_paid` |
| 08 | skip when solo; otherwise sprint records and hand-over notes | review cadence · knowledge hand-over checked by the receiver |
| 09 | skip for internal tools with no regulated data | audit trail · recurring recertification row in the deadline ledger |

**Negative evidence is still evidence.** "No integrations" or "no regulated data" is written as a one-line document where that stage's documents live, with the date and the author. An empty place cannot be told apart from forgotten work.

## Which stages each tier must cover

| Stage | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---|---|---|---|---|
| 00, 01, 02, 04 | required | required | required | required |
| 05, 06 | optional | required | required | required |
| 03, 07, 08, 09 | optional | optional | required | required |

"Required" means the stage's exit evidence must exist. Where it lives is the project's choice: the recommended place is the stage folder of the `docs/00–09` layout ([`project-structure.md`](../standards/project-structure.md)). "Optional" means the stage may be skipped; once its documents exist, they follow the same standards as required ones.

## Who signs a stage gate

Signing follows the tier, not a job title:

| Tier | Who signs |
|---|---|
| LITE | the author records the exit in the sprint file; nobody else signs |
| STANDARD | the author records the exit; the PR is the record |
| PROFESSIONAL | a fresh-context AI review artifact bound to the commit; content reviewed by a human when flagged |
| ENTERPRISE | as PROFESSIONAL, plus a named human who is not the author signs G2 and G4 |

The usual owner of each gate — product owner for G0–G1, technical lead for G2–G3, operations for G4 — is the person the author asks first, not an extra approval.

## Moving back is normal

A stage gate can be re-opened. A failed G3 sends the work to 02 or 04 with a note in the sprint file saying why. Record the move; do not rewrite the earlier exit.

## Sprint closure

At the end of every sprint the sprint file ([`project-structure.md`](../standards/project-structure.md#planning-files)) states, for each stage touched: what exited, what was re-opened, and what evidence is still missing. A sprint closes when the file is updated, not when the calendar says so.
