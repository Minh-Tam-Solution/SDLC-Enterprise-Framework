---
name: sdlc-framework
description: Use when someone asks what the SDLC Enterprise Framework (SEF) requires, which tier a repo is, what a stage or stage gate needs, how a gate script must behave, or where a rule lives in SEF — and before answering any SDLC question from memory. Routes each kind of question to the SEF file and section that answers it; the answer is read there, not here. The other sdlc-* skills rely on its "Find SEF" section.
---

# SDLC Enterprise Framework — where each answer lives

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents answering a question about SEF; the other sdlc-* skills, through "Find SEF"
**Review by**: 2026-12-26

This skill matches SEF version 7. It holds pointers, not rules: every count, name, threshold and exit code is read from the SEF file at the time of the question ([`skills/README.md`](../README.md#what-these-are)).

## Find SEF

SEF is the repository `github.com/Minh-Tam-Solution/SDLC-Enterprise-Framework`. The sdlc-* skills ship inside it, in `skills/`, and every path in them is relative to its root.

1. Loaded from a SEF checkout: this file is `skills/sdlc-framework/SKILL.md` there, and the folder two levels up holds `controls/rule-contract.md`. That folder is SEF at the skill's own revision; read the cited files there, so the skill and the files it cites come from one commit. Say which revision you read.
2. Copied or linked into another repo: first read `.sef-pin` at the repo root if present (format in [`skills/README.md`](../README.md#install)); its `ref` is the revision to read — from a local checkout at that commit, or fetched from its `repo` at that exact commit; if you can reach neither, stop with `insufficient_evidence`, never fall back to `main`. Without `.sef-pin`, look for a local checkout: a submodule or folder named `SDLC-Enterprise-Framework/`, a symlink `.sdlc-framework/`, or a clone the user names. Read the SEF revision the repo pins: the release tag in its policy repo (`adoption/adoption.md` "Pinning"); `git show <tag>:<path>` reads it without moving anyone's checkout. No pin ⇒ read `main` after `git pull --ff-only` (a fetch alone does not change the files you read). Say which revision you read.
3. None reachable ⇒ say so and stop with `insufficient_evidence`. Do not answer from memory: the rules below are pointers, the SEF file is the source.
4. SEF is read-only for these skills. A change to SEF, these skills included, goes through its own `CONTRIBUTING.md`.

## Where each answer lives

| Question | Read |
|---|---|
| What an adopter owns, and what is rented | `core/constitution.md` "Four assets you own" |
| What a rule is; the fields of a register row; rule vs reference | `controls/rule-contract.md` §1 · `controls/rule-contract.md` "Rule register" |
| The rule classes, and which of them may block | `controls/rule-contract.md` §2 |
| The tiers, and how a repo's tier is derived and declared | `controls/tiers.md` "Definitions" · `controls/tiers.md` "Derivation" |
| How much control one change needs (repo tier vs the diff's harm) | `controls/tiers.md` "Two axes" · `controls/risk-floor-paths.md` |
| What each tier requires: gates, agent autonomy, independent review, ritual | `controls/tiers.md` "Per-tier controls" |
| The stages, the question each answers, and the stage gates | `core/lifecycle.md` "Ten stages" |
| What a stage must show to exit | `core/lifecycle.md` "Exit evidence per stage" |
| Which stages a tier must cover | `core/lifecycle.md` "Which stages each tier must cover" |
| Who signs a stage gate | `core/lifecycle.md` "Who signs a stage gate" |
| How a gate script must behave: exit codes, last line, self-test | `controls/rule-contract.md` §1 · `controls/gates.md` "Contract" |
| When a gate may block, and on what measured rate it climbs | `controls/gates.md` "The ladder" · `controls/rule-contract.md` "Entering at MACHINE directly" |
| What a gate needs before its result counts (these are not the stage gates) | `controls/gates.md` "G1–G4" |
| Whose approval counts | `controls/gates.md` "Approver independence" · `adoption/adoption.md` "Agent identity" |
| How a repo adopts SEF: policy repo, adapters, pinning, CI | `adoption/adoption.md` "Policy repo pattern" |
| How an incident becomes a rule | `practices/lessons-to-rules.md` "The path" |
| Whether an artifact should exist at all | `core/constitution.md` "Demand before surface" |
| What SEF will not build | `core/constitution.md` "What the framework does NOT build" |
| Whether systems or design thinking can block | `core/systems-thinking.md` · `core/design-thinking.md` |
| An engineering standard on one topic (testing, security, data classes, deploys …) | the file named for it in `standards/` — list the folder, do not guess |
| Agent context files, hats, the reviewer and its verdict | `ai-engineering/context-and-hats.md` |
| Whether an older (first-generation) idea still applies | `README.md` "What the framework is" · `MIGRATION-MAP.md` "Map" |

A row that does not answer the question means SEF is silent there or the table is out of date: search the live tree (`git grep -n -i '<term>' -- ':!archive'`) before saying SEF is silent.

## What SEF no longer has

Whether a first-generation concept is current is decided by SEF at the revision you read, not by this skill. For each term:

1. `git grep -n -i '<term>' -- migration-map/ ':!archive'` in SEF. A row that names it under "Retired concepts" ⇒ retired; take its successor from the same row's "Live successor".
2. No row, and no hit in the live tree outside `archive/` ⇒ not current (`README.md` "What the framework is" says which ideas apply).
3. Never teach it as current; name the successor, or say there is none.

Search terms that mark a first-generation repo (names used by the archived v6 framework; the list carries no status): Vibecoding Index · 7 pillars · Merge-Readiness Package (MRP) · G-Sprint · zero-mock · coverage quotas per tier · tiers by team size · 10 golden rules · nine mental models · 3-ring architecture · SASE artifacts.

## How to answer

1. Find SEF. Read the file named in the table for the question; quote the section, give the path and the revision.
2. If the question is about a repo, find its tier first (`sdlc-audit` step 2), because most answers depend on it.
3. If SEF does not answer it, say so. Do not fill the gap with a first-generation concept or with a value remembered from an earlier read.
