# Experiments and ADVISORY rows — review register

> Who reads this: the CEO (decides adopt, extend or drop) and @cto SCB (runs the weekly pass).
> When: every Monday, and on each row's date.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @cto SCB
**Consumer**: the CEO; maintainers of the [rule register](rule-contract.md)
**Review by**: 2026-12-01

*Shortens:* an experiment or an `ADVISORY` row that reaches its date and is neither adopted nor dropped. Origin: CEO
2026-11-04 (@cto SCB session): experiments for DevKit and SEF must be checked periodically to decide on official adoption.
MTS-DevKit keeps its own register in `experiments/REGISTER.md` of that repo.

## Why a register next to the deadline gate

[`scripts/check-advisory-deadline.sh`](../scripts/check-advisory-deadline.sh) (C21-4) fails only when a row is past its
date **with `count` > 0**, and runs `cmd` only for `FRAMEWORK_REPO` rows. Measured 2026-11-04 at `0d4abdb`:
`advisory=6 on_time=3 overdue=0 other_scope=3`, `result=pass` — yet **5 of the 6 rows are past their date**
(C21-5 2026-10-09, MIG-1 and NAME-1 2026-10-26, SKILL-1 2026-10-27, DEC-1 2026-11-02). A past date with `count=0`
still needs a decision ([`rule-contract.md`](rule-contract.md) §4: promote to `REVIEW` or delete); nothing asks for it.

## Weekly pass (Monday, @cto SCB)

1. For each row whose date is within 7 days or past: read the evidence named below (the row's `count=` from the last
   CI run, or the experiment's signal).
2. Add one log line: date · evidence (run id or file:line) · proposal `ADOPT` (one step up the ladder) / `EXTEND`
   (one more period, once) / `DROP` (delete the row or the experiment) · reason.
3. Send the proposals to the CEO's approval list in one batch through @ceo. The change goes by PR. A row past its date
   twice with no decision is reported to the CEO as overdue.

## Register

| id | kind | date | evidence to read | state | log |
|---|---|---|---|---|---|
| C21-5 | ADVISORY row | 2026-10-09 | `bash scripts/check-version-declared.sh` `count=` | **PAST DATE** | 2026-11-04: found past date; first pass 2026-11-09 |
| MIG-1 | ADVISORY row | 2026-10-26 | `bash scripts/check-migration-class.sh` `count=` | **PAST DATE** | 2026-11-04: found past date |
| NAME-1 | ADVISORY row | 2026-10-26 | `bash scripts/rule-no-version-in-names.sh` `count=` | **PAST DATE** | 2026-11-04: found past date |
| SKILL-1 | ADVISORY row | 2026-10-27 | `bash scripts/check-skill-citations.sh` `count=` | **PAST DATE** | 2026-11-04: found past date |
| DEC-1 | ADVISORY row | 2026-11-02 | `python3 scripts/check-decision-contract.py` `count=` | **PAST DATE** | 2026-11-04: found past date |
| DOC-3 | ADVISORY row | 2026-12-01 | `bash scripts/check-doc-cites.sh` `count=` | open | — |
| EGM S1, S2 | experiment ([`experiment-egm-spec-review-and-drift.md`](experiment-egm-spec-review-and-drift.md)) | 2026-12-01 | as written in that file | open | — |

## Proposed follow-up (not in this change)

Make the deadline gate print a `decision_due=<n>` count for rows past their date with `count=0`, advisory only, so the
weekly pass reads one number instead of a table. Decide after the first two weekly passes.
