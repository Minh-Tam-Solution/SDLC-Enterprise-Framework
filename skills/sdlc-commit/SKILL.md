---
name: sdlc-commit
description: Use when committing work in a repo that follows the SDLC Enterprise Framework (SEF), or when writing a PR title and description. Stages files by name, blocks secrets, writes a conventional commit message that says why, and keeps commits small and single-purpose. It commits only; it does not push or merge.
---

# Commit and PR conventions

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: agents committing or writing a PR description in a repo that follows SEF
**Review by**: 2026-12-26

Paths are relative to the SEF root; find it with the `sdlc-framework` skill ("Find SEF"). This skill matches SEF version 7. The repo's own `CONTRIBUTING.md`, `AGENTS.md` or hooks win where they are stricter.

| Question while committing | Read |
|---|---|
| What may never be committed, and what to do with a secret already in the repo | `standards/security.md` "Secrets" |
| How a scan result reads (pass, violation, cannot measure) | `controls/rule-contract.md` §1 |
| How large a change may be; drift from its intent; branch lifetime | `standards/change-and-deployment.md` "Small changes, short branches" |
| A move and an edit in one change | `standards/project-structure.md` "Moving and archiving" |
| Deleting, skipping or weakening a test | `standards/testing.md` "Agents and tests" |
| Editing a generated file | `standards/documentation.md` "One home per fact" |
| Quoting a decision; what trailers may claim | `standards/collaboration.md` "Decisions" · `adoption/adoption.md` "Agent identity" |
| How a task ends | `standards/collaboration.md` "How a task ends" |

## Steps

1. **Look first.** `git status` (never `-uall`) and `git diff --cached --stat`. A commit takes the whole index: if it already holds staged changes that are not part of this change, stop and ask how to handle them before staging anything. Nothing to commit ⇒ say so and stop.
2. **Stage by name.** `git add <path> …` for the files of this one change. Never `git add -A` or `git add .`. One concern per commit; split moves from edits as `standards/project-structure.md` "Moving and archiving" says.
3. **Secrets.** Refuse to stage anything `standards/security.md` "Secrets" forbids. Scan the staged content **before** committing with the repo's secret hook or scanner. If SEF's SECRET-1 (`scripts/rule-no-new-secrets.sh`, which reads lines added between a base and `HEAD`) is the only scanner, commit locally, run it before any push, and read its exit code per `controls/rule-contract.md` §1: a violation ⇒ undo the local commit (`git reset --soft HEAD~1`) and remove the value; a result that could not measure is not "clean". A secret already in the repository: follow the same "Secrets" section — deleting it is not enough.
4. **Check the diff against the intent** that authorised it, as `standards/change-and-deployment.md` "Small changes, short branches" describes: for each piece of drift say whether it is kept, reverted or deferred, and flag what that section says to flag.
5. **Tests and generated files.** A test deleted, skipped or weakened ⇒ do what `standards/testing.md` "Agents and tests" requires and give the reason in the message. A generated file changed ⇒ regenerate it by its command (`standards/documentation.md` "One home per fact").
6. **Message.** English, conventional commit form (the 72-character subject limit is this skill's convention, not SEF's):

   ```text
   <type>(<scope>): <what changed, imperative, ≤72 chars>

   <why: the problem, the decision and its source (issue, ADR, PR), anything a reviewer must know>

   <trailers the repo or the user asks for, e.g. Co-Authored-By or Signed-off-by>
   ```

   Types: the repo's own list; SEF's is in its `CONTRIBUTING.md` "Conventional Commits". Scope = the area changed, from the paths. A decision quoted in the message is sourced as `standards/collaboration.md` "Decisions" requires. Trailers claim only what `adoption/adoption.md` "Agent identity" allows them to.
7. **Commit**, then `git log -1 --stat` and show hash, subject and files.

## PR description

When asked to open a PR: what changed and why, the issue or decision it implements, how it was verified (commands and results, CI run on the head SHA), any drift from the intent, risk-floor paths touched, and how the task ended in the terms of `standards/collaboration.md` "How a task ends".

## Rules

- Branch lifetime and the review path to the main branch: `standards/change-and-deployment.md` "Small changes, short branches" and the repo's tier (`controls/tiers.md` "Per-tier controls").
- Do not push, merge or approve unless the user asks. Whose approval counts: `controls/gates.md` "Approver independence".
- A local hook passing is not evidence that CI will (`controls/gates.md` "Hooks nudge; CI enforces").
