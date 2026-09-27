---
name: sdlc-framework-upgrade
description: Use when a repository should adopt the current SDLC Enterprise Framework (SEF), when it still follows the old v6 framework (Vibecoding Index, MRP, G-Sprint, 7 pillars, SASE artifacts), or when someone asks to "upgrade the framework version" in a repo. Moving from v6 is not an upgrade; this skill plans an adoption and a harvest of what is still true, never a bulk version bump.
---

# Adopt SEF in a repository

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents planning SEF adoption in a repository; the repo owner who approves the plan
**Review by**: 2026-12-26

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). No SEF ⇒ stop with `insufficient_evidence`. This skill matches SEF version 7. What still applies from v6: `README.md` "What the framework is".

The folder keeps its old name because people invoke it by that name.

## Steps

1. **Refuse the bump.** Do not search-and-replace version strings or add version labels (`controls/rule-contract.md` §5). What a document's version field claims, and whether an older value is legal: `standards/documentation.md` "Header of a living document".
2. **Inventory** what the repo has today: agent context (`CLAUDE.md`, `AGENTS.md`), `docs/`, gate scripts, CI workflows, hooks, and every v6 concept in use. `git grep -n` for the search terms in `sdlc-framework` ("What SEF no longer has"), with one known hit as a positive control, and settle each hit's status with the steps there.
3. **Route each existing artifact** along one of the routes in `controls/rule-contract.md` §5 — read the conditions for each route there; there is no other route. Harvest claims, not files: look up each v6 concept in the rows under `migration-map/` (index: `MIGRATION-MAP.md` "Map") and point to its live successor instead of copying it. Archiving: `standards/documentation.md` "Archived documents" and `standards/project-structure.md` "Moving and archiving".
4. **Tier by evidence**: derive and declare it as `controls/tiers.md` "Derivation" says, from the evidence it lists.
5. **Policy repo**: the files in the table of `adoption/adoption.md` "Policy repo pattern", and the bullets under it (pinning, drift, control surface, where the tier comes from). Whether a separate policy repo is justified yet: `adoption/adoption.md` "Kill criteria".
6. **Agent identity**: each mechanism in `adoption/adoption.md` "Agent identity", with its red case.
7. **Risk floor and data classes**: the paths per `controls/risk-floor-paths.md` "Paths that are never downgraded" (plus the repo's own), and the class of each path per `standards/security.md` "Data classes and model access", enforced where that section says.
8. **Rules** enter and climb as `controls/gates.md` "The ladder" says; the only exceptions are in `controls/rule-contract.md` "Entering at MACHINE directly". Plan each rule at the entry state and with the declarations those sections require.
9. **Relink.** Links to moved SEF files follow `MIGRATION-MAP.md` "Path map"; pinned references and re-pins follow `standards/project-structure.md` "Moving and archiving".
10. **Measure the adoption**, pre-registered before it starts: pick the experiments, metrics and thresholds from `adoption/adoption.md` "Four 30-day experiments", and write the kill criteria first (`adoption/adoption.md` "Kill criteria").

## Output

A plan, not a diff: the inventory with a route per artifact and its migration-map row, the derived tier, the policy-repo files to create or change, the rules to register with their entry state, and the experiments with their thresholds — each with the SEF section it came from and the SEF revision read. Each change then goes through its own PR in the product or policy repo (`sdlc-commit`).

## Rules

- Do not edit SEF or its `archive/`; do not edit archived files in the product repo.
- Delete content only as `policies/artifact-lifecycle.md` "Transitions" allows.
- Before a structural move (many files, folders), do what `standards/collaboration.md` "Roles for one to a few people" requires.
