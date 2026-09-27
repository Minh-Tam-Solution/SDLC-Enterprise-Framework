# Skills

> Who reads this: whoever installs, distributes or changes the `sdlc-*` agent skills.
> When: before copying them into a repo or an agent tool, and before editing one.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: people and policy repos that install or distribute the skills; authors of a skill change
**Review by**: 2026-12-26

*Shortens:* the time an agent needs to find the SEF file behind a rule, and the time a stale pointer survives.

## What these are

One folder per skill: [`sdlc-framework`](sdlc-framework/SKILL.md) · [`sdlc-audit`](sdlc-audit/SKILL.md) · [`sdlc-commit`](sdlc-commit/SKILL.md) · [`sdlc-cross-review`](sdlc-cross-review/SKILL.md) · [`sdlc-framework-upgrade`](sdlc-framework-upgrade/SKILL.md) · [`sdlc-gate-check`](sdlc-gate-check/SKILL.md) · [`sdlc-sprint-plan`](sdlc-sprint-plan/SKILL.md). A skill is a `SKILL.md` with `name` and `description` front matter; an agent tool loads the description at startup and the body when the skill is used. What each one is for is in its `description`.

They are **non-normative reference implementations** for agent tools. They may name tools (an agent CLI, `gh`); the normative folders stay vendor-neutral ([`CONTRIBUTING.md`](../CONTRIBUTING.md), "Vendor neutrality"). A skill states no rule of its own: it points to the SEF file that holds the rule, and **that file is the authority**. Where a skill and the file it cites disagree, the file wins and the skill is fixed.

**Route, do not restate.** A skill owns when it is used, its procedure, what it reports and when it stops. For everything else it gives the question and the SEF file and section that answer it, and tells the agent to read the value there at run time. It does not copy values out of that file — counts, names of tiers, classes or stages, exit-code meanings, thresholds, lists of required evidence. A pointer is checked (below); a copied value is not: if SEF changes it, the copy stays green and wrong.

## Install

- Copy or link the folders from a **pinned** SEF checkout — a release tag, recorded with its resolved SHA ([`adoption`](../adoption/adoption.md#policy-repo-pattern)) — into the skills folder your agent tool reads.
- A policy repo may distribute them to product repos the same way it distributes adapters. A copy is a derived file: re-copy from the pinned ref, never hand-edit it ([one home per fact](../standards/documentation.md#one-home-per-fact)).
- **A distributing policy repo also writes `.sef-pin` at the product repo's root**, two lines: `repo=<owner>/<name>` of SEF and `ref=<full commit SHA>` it pinned. The copied skills carry no revision of their own; this file is how an agent in the product repo finds the exact SEF they match. It is a derived file like the skills: regenerated, never hand-edited.
- Where the agent reads SEF from — this checkout, or the one a product repo pins — is in [`sdlc-framework`, "Find SEF"](sdlc-framework/SKILL.md#find-sef).

## Checked

[`scripts/check-skill-citations.sh`](../scripts/check-skill-citations.sh) (rule SKILL-1 in the [rule register](../controls/rule-contract.md#rule-register)): every SEF path, section and link a skill cites exists in the same commit, and every folder has a `SKILL.md` whose `name` is the folder name and whose `description` is not empty. A skill is a live document: it carries the header fields of a living document ([`documentation`](../standards/documentation.md#header-of-a-living-document)).

## Changing a skill

Through [`CONTRIBUTING.md`](../CONTRIBUTING.md), like any file here. People invoke a skill by its folder name, so renaming or retiring one follows [`policies/artifact-lifecycle.md`](../policies/artifact-lifecycle.md).
