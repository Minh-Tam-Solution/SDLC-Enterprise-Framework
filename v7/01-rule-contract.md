# 01 — v7 Rule Contract

**Version**: 1.0.0
**SDLC Framework Version**: 7.0.0
**Status**: DRAFT
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
result=pass|insufficient_evidence|violation gate=<id> reason=<slug> [fix=<rest of line>]
```

`pass ↔ 0` · `insufficient_evidence ↔ 1` · `violation ↔ 2`. A label that contradicts the exit code, or is malformed, is mis-declared. The cause of a failure is read from the last line of **stderr** — never discard it.

**Unit of routing = FILE; unit of enforcement = ROW.** A rule file has a `## Rules v7` table; each row is one command with one exit code. `ratio = rule_files / files_in_scope` is a **measurement, not a target**: adding a row whose `cmd` does not measure what the rule says raises the ratio and destroys the measurement.

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

1. **Rule** — has `class` + `cmd` + `burn_case` ⇒ a row in `## Rules v7`
2. **Reference** — content is right, no command ⇒ kept, stops pretending to be a gate
3. **`10-Archive/`** — no longer in force

⛔ **No bulk version-label bumps.** Aligning references by hand has been done (hundreds of them) and they drifted back — one manual clean-up has nothing holding it in place. Aggregate numbers in documents carry the command that produces them, or they are removed.

---

## Rules v7

> **The framework's single rule register.** No other file holds a rule table; a rule in two tables runs twice and is counted twice.
> 🔴 Never list the rules runner itself **without** `--l3` in a row: the runner runs `cmd`, `cmd` is the runner ⇒ infinite recursion.

| id | class | cmd | burn_case | run_scope |
|---|---|---|---|---|
| L2 | MACHINE | `bash scripts/rule-no-swallowed-stderr.sh` | G2: a gate called a checker with `2>/dev/null`, which swallowed a missing-module error; the gate reported "README out of sync with YAML" — the wrong cause, and two readers went to fix the wrong thing. Exemptions are declared in a file, each with a deadline. | FRAMEWORK_REPO |
| L3 | MACHINE | `bash scripts/check-rules-v7.sh --l3` | G3: a duplicate-document gate compared file names across trees and stayed 100% green while the work was unfinished — nobody had ever made it red. Every script in the `cmd` column must have `--selftest` (a red case + a green case), pass it, and contain no `exit $?`. | FRAMEWORK_REPO |
| L4 | MACHINE | `bash scripts/rule-no-git-grep-word-boundary.sh` | G1: `git grep -E '\bMUST\b'` matched nothing and exited successfully; the same person then got a count wrong in the opposite direction (5 vs. hundreds), both silent, both exposed only by a positive control. Use `-w`/`-P` with a positive control. | FRAMEWORK_REPO |
| C21-4 | MACHINE | `bash scripts/check-advisory-deadline.sh` | G4: a "kill" gate for an internal tool ran 8 days past its deadline with its deciding metric still "NOT MEASURED"; nobody promoted it, nobody deleted it — a report-only gate that was dead yet stayed green. | FRAMEWORK_REPO |

**Pending rows (not in the table, with the reason):**
- `scripts/check-version-declared.sh` (which framework version was a document verified against) — `ADVISORY` at step 1. It needs `--selftest`, `--chan` returning `2`, a `count=` line, and a **deadline published in advance** (§4). Adding it earlier would turn L3 red or make C21-4 flag it as mis-declared.
- G1 content (does the positive control really plant a violation) and §2 (does a `cmd` call a model on any branch) are `REVIEW` with no `cmd`: the reviewer of the PR that adds a row judges them. They are not rows.
