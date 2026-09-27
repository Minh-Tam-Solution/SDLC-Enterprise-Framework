---
name: sdlc-framework
description: Use when someone asks what the SDLC Enterprise Framework (SEF) requires, which tier a repo is, what a stage or stage gate needs, how a gate script must behave, or where a rule lives in SEF — and before answering any SDLC question from memory. Gives the SEF model in one page with the SEF file that holds each claim. The other sdlc-* skills rely on its "Find SEF" section.
---

# SDLC Enterprise Framework — the model in one page

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents answering a question about SEF; the other sdlc-* skills, through "Find SEF"
**Review by**: 2026-12-26

This skill matches SEF version 7, the second generation: rebuilt, not upgraded. Older ideas apply only if `MIGRATION-MAP.md` gives them a row with a live successor.

## Find SEF

SEF is the repository `github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework`. The sdlc-* skills ship inside it, in `skills/`, and every path in them is relative to its root.

1. Loaded from a SEF checkout: this file is `skills/sdlc-framework/SKILL.md` there, and the folder two levels up holds `controls/rule-contract.md`. That folder is SEF at the skill's own revision; read the cited files there, so the skill and the files it cites come from one commit. Say which revision you read.
2. Copied or linked into another repo: look for a local checkout: a submodule or folder named `SDLC-Enterprise-Framework/`, a symlink `.sdlc-framework/`, or a clone the user names. Read the SEF revision the repo pins: the release tag in its policy repo (`adoption/adoption.md` "Pinning"); `git show <tag>:<path>` reads it without moving anyone's checkout. No pin ⇒ read `main` after `git pull --ff-only` (a fetch alone does not change the files you read). Say which revision you read.
3. None reachable ⇒ say so and stop with `insufficient_evidence`. Do not answer from memory: the rules below are pointers, the SEF file is the source.
4. SEF is read-only for these skills. A change to SEF, these skills included, goes through its own `CONTRIBUTING.md`.

## The model, each claim with its home

| Claim | SEF file |
|---|---|
| You own four assets: policy, repo knowledge, runnable gates, eval set. Everything else (agents, models, skills, hooks, CI runners) is rented. | `core/constitution.md` · `README.md` |
| Rules sit in three classes: `MACHINE` (deterministic, blocks), `REVIEW` (named reviewer judges fixed evidence, flags), `ADVISORY` (counted, with a deadline). A model is never `MACHINE`. | `controls/rule-contract.md` §2 |
| A rule is a register row with `class`, `cmd`, `burn_case`, `run_scope`. No runnable command ⇒ reference, not a rule. One register only. | `controls/rule-contract.md` §1, "Rule register" |
| Tier comes from the risk of the artefact, not team size: LITE · STANDARD · PROFESSIONAL · ENTERPRISE, derived as max(repo evidence, declared metadata, deploy evidence); declare up only. | `controls/tiers.md` |
| `effective_control = max(service_tier, change_harm)`; the diff's harm comes from risk-floor paths and data classes. | `controls/tiers.md` "Two axes" · `controls/risk-floor-paths.md` |
| Ten stages 00–09, one question each; stage gates G0.1, G0.2, G1, G2, G3, G4 are decision points with evidence; who signs follows the tier. | `core/lifecycle.md` |
| Gate contract: exit `0` pass · `1` cannot measure · `2` violation (on purpose) · `≥3` reserved (read as cannot measure); last stdout line `result=… gate=… reason=… [fix=…]`; every gate ships `--selftest` with a red and a green case. | `controls/rule-contract.md` §1 · `controls/gates.md` |
| Gates climb ADVISORY → REVIEW → MACHINE on measured rates (upper Wilson bound); entering at MACHINE directly only under the two named cases. | `controls/gates.md` "The ladder" · `controls/rule-contract.md` "Entering at MACHINE directly" |
| Four rules about gates, also named G1–G4 (not the stage gates): a negative needs a positive control; "cannot measure" has its own output; write from the definition and make it red; ADVISORY has a counter and a deadline. | `controls/gates.md` |
| Systems thinking and design thinking are lenses: they shape questions, never block. | `core/systems-thinking.md` · `core/design-thinking.md` |
| Demand before surface: every artifact names its consumer and the job that breaks without it. | `core/constitution.md` |
| Incidents become rules through one path: burn case → row → ADVISORY → REVIEW → MACHINE. | `practices/lessons-to-rules.md` |
| Adoption: one policy repo, generated adapters, reusable CI workflow; agent identity separated from the approver. | `adoption/adoption.md` |
| What every repo follows: structure, documentation headers, testing, security and data classes, change and deployment, integration, observability, collaboration. | `standards/*.md` |
| Agent context files, hats, fresh-context reviewer, typed verdict. | `ai-engineering/context-and-hats.md` |

## What SEF no longer has

Do not teach these as current; each is retired in `MIGRATION-MAP.md` or absent from the live tree: Vibecoding Index · 7 pillars · Merge-Readiness Package (MRP) · sprint gates (G-Sprint) · absolute zero-mock · coverage quotas per tier · tiers by team size · "10 golden rules" of sprint planning · the nine mental models as a canon · 3-ring architecture. Their surviving ideas: gates + rule register + independent review (`controls/`), real-over-fake testing (`standards/testing.md`), demand before surface (`core/constitution.md`).

## How to answer

1. Find SEF. Read the file named in the table for the question; quote the section, give the path.
2. If the question is about a repo, find its tier first (`sdlc-audit` step 2), because most answers depend on it.
3. If SEF does not answer it, say so. Do not fill the gap with a v6 concept.
