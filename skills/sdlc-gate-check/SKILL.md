---
name: sdlc-gate-check
description: Use before asking someone to pass a stage gate (a decision point of the SEF lifecycle), when asked "are we ready to move on?", or when a gate script's result needs reading. Finds the exit evidence the repo's tier requires for that gate, says who must sign, and reads gate script exit codes and result lines. It never signs or approves.
---

# Stage gate readiness

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents checking stage-gate readiness; the person who signs the gate
**Review by**: 2026-12-26

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7.

Every value this check needs — gate ids, stages, evidence items, exit codes, signers — is read from SEF at run time, from these places:

| The step needs | Read |
|---|---|
| which stages a gate covers; what a stage gate is | `core/lifecycle.md` "Ten stages" |
| how evidence derives a tier | `controls/tiers.md` "Derivation" |
| whether the tier must cover a stage | `core/lifecycle.md` "Which stages each tier must cover" |
| the exit evidence per stage and tier | `core/lifecycle.md` "Exit evidence per stage" |
| exit codes and the result line of a gate script | `controls/rule-contract.md` §1 |
| when a script's green or "0 found" counts | `controls/gates.md` "G1–G4" |
| who signs, and whose signature is independent | `core/lifecycle.md` "Who signs a stage gate" · `controls/gates.md` "Approver independence" |

## Steps

1. **Gate.** Take it from the arguments; none ⇒ ask. Find its stages in the "Stage gate" column of `core/lifecycle.md` "Ten stages". A gate id that column does not name does not exist in SEF: say so and stop.
2. **Tier.** Read the repo's declared tier (policy repo `projects.yaml`, or the repo's own declaration). Look for each signal listed in `controls/tiers.md` "Derivation" and derive the tier as that section says. Declared below derived ⇒ report it and use the derived tier. No declaration and no evidence ⇒ "tier not measured" and readiness `insufficient_evidence` — never assume the lowest tier.
3. **Is the stage required?** Look up tier × stage in `core/lifecycle.md` "Which stages each tier must cover". Not required and absent ⇒ note it, nothing to check.
4. **Evidence.** For each stage of the gate, list every item `core/lifecycle.md` "Exit evidence per stage" requires at this tier (the section says which columns apply to which tier). For each item find what answers it and give its path or link. What counts as evidence, and when a stated negative counts, is in the same file: `core/lifecycle.md` "Negative evidence is still evidence".
5. **Machine evidence.** Where a script can check an item, run it, or read its CI run on the exact head SHA. Read the result against `controls/rule-contract.md` §1 — take the exit-code meanings and the result-line format from there, not from memory:
   - a result line that is missing or disagrees with the exit code ⇒ report the gate as mis-declared;
   - keep the last line of stderr in the report; never discard stderr of a command whose result becomes evidence;
   - a green or a "0 found" that fails the conditions of `controls/gates.md` "G1–G4" ⇒ "not measured";
   - read exit codes and CI check-runs, never an agent's text about whether something passed (`controls/gates.md` "Hooks nudge; CI enforces").
6. **Who signs.** Read the row for the tier in `core/lifecycle.md` "Who signs a stage gate", and check anyone named against `controls/gates.md` "Approver independence".
7. **Report**, with the SEF revision you read (tag or SHA, from "Find SEF"), and stop. The person named in step 6 decides.

## Output

```text
Gate <id> — stages <nn[,nn]> — tier <TIER> (declared <x>, derived <y>) — SEF <revision>
[found]    <evidence item> — <path | PR | CI run>
[missing]  <evidence item> — <what would answer it>
[not measured] <item> — <why: no positive control / script could not measure / tool missing>
Signs: <who, per the SEF row read in step 6>
Readiness: ready | not_ready | insufficient_evidence
```

`ready` only when every required item is `found`. Any `missing` ⇒ `not_ready`. Tier or SEF unknown, or a required item `not measured` ⇒ `insufficient_evidence`.

## Rules

- Check only the stages the change can affect; which ones those are is in `core/lifecycle.md` "Ten stages".
- A re-opened gate follows `core/lifecycle.md` "Moving back is normal"; do not rewrite the earlier exit.
- Never approve, never sign, never mark a gate passed. Never lower a tier to make evidence fit.
