# Rule Contract

**Version**: 1.0.0
**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: rule and gate authors; `scripts/check-rules.sh`
**Review by**: 2026-12-26
**Status**: ACTIVE
**Date**: 2026-09-25

> v7 is the first time the framework can **measure itself**. It is not a writing campaign: more documents make a team slower and costlier, which is the opposite of the goal.
> Acceptance criterion for anything in v7: good product, faster, with less time, fewer tokens, less money. A proposal that cannot say what it shortens is not in v7.
> **The measurable promise: fewer rules, more of them enforced.**

---

## §1 — A rule is a command, or it is reference

> **A rule without a runnable command is not a rule. It is reference material.**

Every rule declares these fields. Without `class` + `cmd` + `burn_case` it is reference; reference is still useful, it just stops pretending to be a gate.

| Field | Meaning |
|---|---|
| `class` | `MACHINE` · `REVIEW` · `ADVISORY` (§2) |
| `cmd` | a runnable command that returns an exit code |
| `burn_case` | the real incident that paid for this rule — why it exists |
| `run_scope` | where `cmd` can run: `FRAMEWORK_REPO` (root of this repo) · `PRODUCT_CI` (CI of a repo that adopts the framework) · `RUNTIME_PROBE` (the host running the service). Empty = `FRAMEWORK_REPO`. Any other value = mis-declared. |

**`cmd` must be our own script** (`bash`/`python3` + a path in the repo). External tools give exit code `1` their own meaning (`grep`: no match, often a *pass*; linters: findings). The wrapper owns its exit code and maps it explicitly. **No `exit $?`.**

**Exit codes:**

```text
0  = PASS
1  = CANNOT MEASURE   ← the default of anything broken (uncaught exception, set -e, missing tool)
2  = VIOLATION        ← must be returned ON PURPOSE, after the check ran to the end
≥3 = reserved (read as cannot measure)
```

The default exit code of a broken tool must land in the **honest** bucket. A gate may claim "violation" only after it ran to the end and decided.

**Label line** — the last line of `cmd`'s stdout:

```text
result=pass|insufficient_evidence|violation gate=<gate-name> reason=<slug> [fix=<rest of line>]
```

`pass ↔ 0` · `insufficient_evidence ↔ 1` · `violation ↔ 2`. `gate=` names the script (e.g. `check-advisory-deadline`); the rule id lives in the table, not in the label. A label that contradicts the exit code, or is malformed, is mis-declared. The cause of a failure is read from the last line of **stderr** — never discard it.

**Unit of routing = FILE; unit of enforcement = ROW.** A rule file has a `## Rule register` table; each row is one command with one exit code. `ratio = rule_files / files_in_scope` is a **measurement, not a target**: adding a row whose `cmd` does not measure what the rule says raises the ratio and destroys the measurement.

---

## §2 — Three classes (definitions, not examples)

| Class | Definition | When it fails |
|---|---|---|
| **MACHINE** | deterministic · same input, same result · no human judgement | **fail-closed**, blocks |
| **REVIEW** | needs a human, but **who judges and what they judge** is fixed | flags, does not block |
| **ADVISORY** | a suggestion with no pass/fail criterion | **counted**, with a deadline (G4) |

🔴 **A probabilistic model is NEVER `MACHINE`**, whatever its accuracy — that is a category error that breaks the axis v7 stands on. Models sit in `REVIEW`/`ADVISORY` and **add** a differently-blind instrument; they never **replace** a deterministic one.
*Burn case: a classifier tested on Vietnamese text scored 0.26 with calibration error 0.52 — wrong and confident, with no warning signal.*

---

## §3 — G1–G4: four rules about GATES (including gates run by people)

**G1 — A NEGATIVE result needs a POSITIVE control.** "Not found / 0 / clean" is not evidence unless a positive case shows the instrument can see what it looks for. Without one, record "not measured", not `0`.
*Burn case: a secret scanner ran in redact mode, then the masked string was grepped ⇒ `0`; the truth was 49 live secrets. A search API blind to private repos reported a contributor with merged PRs as "activity 0".*

**G2 — A gate needs its own value for "CANNOT MEASURE".** Without it the gate fails both ways:
- *fail-open:* an output type with no "unknown" slot returns the nearest value, always toward "clean". *Cases: a boolean judge on empty input read as "clean"; a monitor reading the wrong path reported healthy for 25 days; a scanner that scanned 0 files reported clean.*
- *fail-closed with the WRONG LABEL:* red for the wrong cause, so people fix the wrong thing. *Case: `2>/dev/null` swallowed a missing-module error and the gate printed "README out of sync with YAML".*
⇒ no `2>/dev/null` on a command whose result becomes evidence. One variable never carries two meanings.

**G3 — Write gates from the DEFINITION, not from EXAMPLES, and make them go RED.** Every gate ships with a case that deliberately turns it red and a clean case that must stay green. **Until someone has made it red, "green" means "not measured".**
*Burn case: a duplicate-document gate compared file names across trees; real duplicates never share a name, so it stayed 100% green while the work was unfinished.*

**G4 — `ADVISORY` needs a COUNTER + a DEADLINE.** Backlog in a report-only gate means the gate is dead: people have learned not to read it. Deadline passed with count > 0 ⇒ promote to `REVIEW` or **delete the rule**. There is no third option.
*Declaration (machine-read by C21-4):* the row's `burn_case` carries `deadline=YYYY-MM-DD`; its `cmd` prints `count=<n>` on stdout before the label line. Missing deadline ⇒ `2` · deadline passed ∧ `count>0` ⇒ `2` · no `count=` ⇒ `1`. A `cmd` that prints a made-up count is a G1 defect of that `cmd`, not of C21-4.

---

## §4 — Turn gates on along a TRAJECTORY, not as a wall

A gate switched on while violations are many turns CI red on day one ⇒ **it gets switched off within a day**, and the safe path goes with it.

| Step | State | Condition to move up |
|---|---|---|
| 1 | `ADVISORY` + counter, number printed weekly | violation ratio **< 20%** |
| 2 | `REVIEW` — flags, does not block | **< 5%** for **2 consecutive weeks** |
| 3 | `MACHINE` — blocks | — |

**Publish the thresholds BEFORE step 1.** Setting a threshold after seeing the number is grading yourself.

---

## §5 — Existing documents: a route, not a rewrite

Every existing document takes **one of three** routes. There is **no fourth route called "rewrite it for v7"**.

1. **Rule** — has `class` + `cmd` + `burn_case` ⇒ a row in `## Rule register`
2. **Reference** — content is right, no command ⇒ kept, stops pretending to be a gate
3. **`archive/`** — no longer in force

⛔ **No bulk version-label bumps.** Aligning references by hand has been done (hundreds of them) and they drifted back — one manual clean-up has nothing holding it in place. Aggregate numbers in documents carry the command that produces them, or they are removed.

---

### Entering at MACHINE directly

Every rule climbs the ladder from `ADVISORY` ([`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md)). A rule may enter at `MACHINE` only under one of two named cases, stated in its `burn_case`:

**(a) Same-rule replacement.** It enforces the **same invariant** — the same failure class — as a gate that already blocks, with equal or narrower scope and fail-closed semantics no weaker; its count is 0 on the day it lands; a named person decided it. A gate that checks something different is a new control and does not inherit the old gate's maturity.

**(b) Irreversible harm.** All six hold:

1. the harm it prevents is irreversible or materially security-critical;
2. the detector's scope is narrow and deterministic;
3. baseline violations are 0, or known debt is bounded separately (owner, expiry);
4. a red case and a green case both pass in `--selftest`;
5. escaping a false positive needs more authority than the actor being checked (e.g. an exemption read from the base commit and on the risk floor);
6. a named person's decision is recorded.

Uses: SECRET-1 (b), 2026-09-26. DOC-2 entered at `MACHINE` on 2026-09-26 as a **one-time recorded exception** (CEO): it measures ownership, not the document count it replaced, so it does not meet (a) and is not a precedent.

## Rule register

> **The framework's single rule register.** No other file holds a rule table; a rule in two tables runs twice and is counted twice.
> 🔴 Never list the rules runner itself **without** `--l3` in a row: the runner runs `cmd`, `cmd` is the runner ⇒ infinite recursion.

| id | class | cmd | burn_case | run_scope |
|---|---|---|---|---|
| L2 | MACHINE | `bash scripts/rule-no-swallowed-stderr.sh` | G2: a gate called a checker with `2>/dev/null`, which swallowed a missing-module error; the gate reported "README out of sync with YAML" — the wrong cause, and two readers went to fix the wrong thing. Exemptions are declared in a file, each with a deadline. | FRAMEWORK_REPO |
| L3 | MACHINE | `bash scripts/check-rules.sh --l3` | G3: a duplicate-document gate compared file names across trees and stayed 100% green while the work was unfinished — nobody had ever made it red. Every script in the `cmd` column must have `--selftest` (a red case + a green case), pass it, and contain no `exit $?`. | FRAMEWORK_REPO |
| L4 | MACHINE | `bash scripts/rule-git-grep-no-word-boundary.sh` | G1: `git grep -E '\bMUST\b'` matched nothing and exited successfully; the same person then got a count wrong in the opposite direction (5 vs. hundreds), both silent, both exposed only by a positive control. Use `-w`/`-P` with a positive control. | FRAMEWORK_REPO |
| C21-4 | MACHINE | `bash scripts/check-advisory-deadline.sh` | G4: a "kill" gate for an internal tool ran 8 days past its deadline with its deciding metric still "NOT MEASURED"; nobody promoted it, nobody deleted it — a report-only gate that was dead yet stayed green. | FRAMEWORK_REPO |
| DOC-1 | ADVISORY | `bash scripts/check-doc-count.sh` | v6.x reached 189 live docs (502 with archive); nobody could say which were still true. deadline=2026-10-25 | FRAMEWORK_REPO |
| DOC-2 | MACHINE | `bash scripts/check-doc-ownership.sh` | v6.x reached 189 live docs and nobody could say which were still true; `DEPRECATION-POLICY.md` still said ACTIVE for Framework 6.3.0 a major version later. A count ceiling limited the number, not whether a doc had an owner, a reader, or was still right. Entered at MACHINE as a one-time recorded exception (CEO, 2026-09-26), not a precedent: it replaced the blocking doc-count ceiling but checks a different invariant (see "Entering at MACHINE directly") | FRAMEWORK_REPO |
| SECRET-1 | MACHINE | `bash scripts/rule-no-new-secrets.sh` | Secrets pushed to shared repositories had to be rotated after the fact; deleting them from the tree did not un-leak them. Scans only the lines a change adds. Exemptions (false positives only) are read from the base commit, need owner, reason and an expiry within 90 days, and the exemption file is on the risk floor — an exemption added in the same change does not count. This row protects this repository; adopting repos register the same command at `PRODUCT_CI` in their policy repo. Entered at MACHINE under case (b) of "Entering at MACHINE directly" (CEO, 2026-09-26, m141) | FRAMEWORK_REPO |
| MIG-1 | ADVISORY | `bash scripts/check-migration-class.sh` | Migrations that could not be rolled back were found only while rolling back: an enum value that cannot be removed, two migrations that collided on the way down, a policy dropped on a live database. The machine classifies each migration none, expand, unknown or contract per operation and its arguments (a column added NOT NULL without a default, any added constraint, foreign key or unique index is contract; inserted rows are unknown). A migration labelled expand that the machine classifies contract is counted. While ADVISORY it decides nothing: any deploy with a migration follows the human runbook. Not promoted until a labelled corpus measures the unknown and false-expand rates. deadline=2026-10-26 | PRODUCT_CI |
| C21-5 | ADVISORY | `bash scripts/check-version-declared.sh` | A document's own version was read as the framework version it had been checked against; hundreds of references were then bumped by hand and drifted back, and nobody could say which documents had really been verified against the current framework. Counts documents with no `sdlc_framework` / `**SDLC Framework Version**` field; an older declared version is legal and not counted. deadline=2026-10-09 | FRAMEWORK_REPO |
| NAME-1 | ADVISORY | `bash scripts/rule-no-version-in-names.sh` | The core lived in `v7/`; moving it to version-neutral folders broke ~100 link lines in four consuming repos on 2026-09-26, and the next major version would have broken them again. A heading is a link anchor, so it counts too. deadline=2026-10-26 | FRAMEWORK_REPO |

**Pending rows (not in the table, with the reason):**
- G1 content (does the positive control really plant a violation) and §2 (does a `cmd` call a model on any branch) are `REVIEW` with no `cmd`: the reviewer of the PR that adds a row judges them. They are not rows.
