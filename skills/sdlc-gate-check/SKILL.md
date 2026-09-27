---
name: sdlc-gate-check
description: Use before asking someone to pass a stage gate (G0.1, G0.2, G1, G2, G3, G4), when asked "are we ready to move on?", or when a gate script's result needs reading. Finds the exit evidence the repo's tier requires for that gate, says who must sign, and reads gate script exit codes and result lines. It never signs or approves.
---

# Stage gate readiness

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7.

A stage gate is a decision point: passed when its evidence exists and, where the tier requires it, the right person has signed (`core/lifecycle.md`). Gate scripts are a different thing (`controls/gates.md`); step 5 covers how to read them.

## Steps

1. **Gate.** Take it from the arguments; none ⇒ ask. Map it to its stages with the table in `core/lifecycle.md` "Ten stages": G0.1/G0.2 → 00 · G1 → 01 · G2 → 02 + 03 · G3 → 04 + 05 · G4 → 06 + 07 (and 09 from G4 on). There is no sprint gate.
2. **Tier.** Read the repo's declared tier (policy repo `projects.yaml`, or the repo's own declaration) and check it against evidence per `controls/tiers.md` "Derivation" (a `migrations/` folder, a risk-floor path, money/payroll/PII path segments). Declared below derived ⇒ report it; use the derived tier. Evidence only gives a floor (declare up only). No declaration and no evidence ⇒ "tier not measured" and readiness `insufficient_evidence` — never assume the lowest tier.
3. **Is the stage required?** `core/lifecycle.md` "Which stages each tier must cover". Optional and absent ⇒ note it, nothing to check.
4. **Evidence.** For each stage of the gate, take the "Minimum to exit" row, plus "PROFESSIONAL+ adds" for PROFESSIONAL and ENTERPRISE (`core/lifecycle.md` "Exit evidence per stage"). For each item find the thing that answers it — a doc, README section, issue, ADR, PR, CI run or deploy record — and give its path or link. Evidence need not be a document. A stated negative ("no integrations", with a date, in README or `AGENTS.md`) counts; silence does not.
5. **Machine evidence.** Where a script can check an item, run it (or read its CI run on the exact head SHA) and read it per the gate contract (`controls/rule-contract.md` §1):
   - exit `0` pass · `1` cannot measure · `2` violation · `≥3` reserved, read as cannot measure;
   - the last stdout line must be `result=… gate=… reason=… [fix=…]` and agree with the exit code, else the gate is mis-declared;
   - the cause of a failure is the last line of stderr — keep it, never `2>/dev/null` a command whose result becomes evidence;
   - a gate with no `--selftest` red case, or a "0 found" with no positive control, is "not measured", not green (`controls/gates.md` G1, G3);
   - read exit codes and CI check-runs, never an agent's text about whether something passed (`controls/gates.md` "Hooks nudge; CI enforces").
6. **Who signs.** `core/lifecycle.md` "Who signs a stage gate": LITE — author records the exit in the sprint file · STANDARD — the author records the exit; the PR is the record · PROFESSIONAL — a fresh-context AI review artifact bound to the commit (`controls/tiers.md`), content reviewed by a human when flagged · ENTERPRISE — plus a named human who is not the author signs G2 and G4. Approver independence: not the author and not the person operating the author's agent (`controls/gates.md` "Approver independence").
7. **Report** and stop. The person named in step 6 decides.

## Output

```text
Gate <id> — stages <nn[,nn]> — tier <TIER> (declared <x>, derived <y>)
[found]    <evidence item> — <path | PR | CI run>
[missing]  <evidence item> — <what would answer it>
[not measured] <item> — <why: no positive control / script exit 1 / tool missing>
Signs: <who, per tier>
Readiness: ready | not_ready | insufficient_evidence
```

`ready` only when every required item is `found`. Any `missing` ⇒ `not_ready`. Tier or SEF unknown, or a required item `not measured` ⇒ `insufficient_evidence`.

## Rules

- Evidence depth follows the tier and the change, not habit: a change re-opens only the stages it can affect (`core/lifecycle.md` "Ten stages"); controls are proportional to risk (`core/constitution.md` principles).
- A gate can be re-opened; record the move in the sprint file, do not rewrite the earlier exit (`core/lifecycle.md` "Moving back is normal").
- Never approve, never sign, never mark a gate passed. Never lower a tier to make evidence fit.
