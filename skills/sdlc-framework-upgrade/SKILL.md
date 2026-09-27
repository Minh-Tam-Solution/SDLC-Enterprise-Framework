---
name: sdlc-framework-upgrade
description: Use when a repository should adopt the current SDLC Enterprise Framework (SEF), when it still follows the old v6 framework (Vibecoding Index, MRP, G-Sprint, 7 pillars, SASE artifacts), or when someone asks to "upgrade the framework version" in a repo. Moving from v6 is not an upgrade; this skill plans an adoption and a harvest of what is still true, never a bulk version bump.
---

# Adopt SEF in a repository

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7, which is rebuilt, not upgraded: nothing from v6 applies unless `MIGRATION-MAP.md` gives it a live successor (`README.md` "What the framework is").

The folder keeps its old name because people invoke it by that name.

## Steps

1. **Refuse the bump.** Do not search-and-replace version strings or add "v7" labels. Hand-aligned references drift back (`controls/rule-contract.md` §5). A document's `SDLC Framework Version` field says which version it was last *checked* against; an older value is legal (`standards/documentation.md` "Header of a living document").
2. **Inventory** what the repo has today: agent context (`CLAUDE.md`, `AGENTS.md`), `docs/`, gate scripts, CI workflows, hooks, and every v6 concept in use. `git grep -n` for the retired names listed in `sdlc-framework` ("What SEF no longer has"), with one known hit as a positive control.
3. **Route each existing artifact** one of three ways (`controls/rule-contract.md` §5) — there is no fourth route called "rewrite it for v7":
   - **rule** — it has a class, a runnable command and a burn case ⇒ a row in the rule register;
   - **reference** — still true, no command ⇒ keep, stop presenting it as a gate;
   - **archive** — no longer in force ⇒ `git mv` into the repo's archive folder unchanged, and record where its content went in that folder's README (`standards/documentation.md` "Archived documents").
   Harvest claims, not files: look up each v6 concept in `MIGRATION-MAP.md` ("Retired concepts" and "Live successor") and point to the successor instead of copying it.
4. **Tier by evidence** (`controls/tiers.md`): derive it from repo, declared metadata and deploy evidence; declare it in the policy repo with `tier_scheme: v7-risk`. Team size is not an input.
5. **Policy repo** (`adoption/adoption.md` "Policy repo pattern"): `projects.yaml` (tier, metadata, risk-floor paths, data classes), `tiers.yaml`, `rules.md` with `## Rule register`, hats, gates, `adapters/gen.sh`, `.approvers`, `CONTROL_SURFACE`. The product pins a release tag; CI regenerates adapters and expects an empty diff; the reusable workflow reads the tier from the policy, never from the product. A second consuming repo is what justifies a separate policy repo (`adoption/adoption.md` "Kill criteria").
6. **Agent identity** (`adoption/adoption.md` "Agent identity"): agents act as a least-privilege bot, the owner credential is off the agent's machine, every agent identity is mapped to its operator in `.approvers`, and authority comes from the authenticated actor.
7. **Risk floor and data classes**: declare the paths (`controls/risk-floor-paths.md`, add, never remove) and the class of each path (`standards/security.md` "Data classes and model access"), enforced at the OS boundary for `restricted` and `no-ai`.
8. **Rules enter at the bottom of the ladder**: `ADVISORY` with a counter, a deadline and thresholds published before step 1; climb on measured rates (`controls/gates.md` "The ladder"). Entering at `MACHINE` directly only under the two named cases (`controls/rule-contract.md` "Entering at MACHINE directly").
9. **Relink.** Links to moved SEF files follow the path map in `MIGRATION-MAP.md`; a reference pinned to a commit SHA keeps working, the next re-pin uses the new path.
10. **Measure the adoption**, pre-registered before it starts (`adoption/adoption.md` "Four 30-day experiments"): time from clone to the first safe change (CI green), refusals by evidence-based tiering, drift caught in one CI run. Write the kill criteria first.

## Output

A plan, not a diff: the inventory with a route per artifact and its `MIGRATION-MAP.md` row, the derived tier, the policy-repo files to create or change, the rules to register at `ADVISORY`, and the experiments with their thresholds. Each change then goes through its own PR in the product or policy repo (`sdlc-commit`).

## Rules

- Do not edit SEF or its `archive/`; do not edit archived files in the product repo.
- Do not delete content except what is harmful (a secret, a vulnerable instruction, personal data) — and a leaked secret is rotated (`policies/artifact-lifecycle.md`).
- Structural moves (many files, folders) need a decision record first (`standards/collaboration.md` "Roles for one to a few people").
