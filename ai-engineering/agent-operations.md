# Agent operations

> Who reads this: whoever runs agents on shared repos — one agent or several — and the lead who sets up how a team works with them.
> When: before giving an agent credentials, before running agents in parallel, when a guard blocks an agent, and at the monthly review.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: framework maintainers
**Consumer**: people who run agents; leads introducing agent work to a team; maintainers of agent credentials and CI
**Review by**: 2026-12-26

*Shortens:* the blast radius of an agent that is wrong or misled, the time lost to agents overwriting each other, and the time a lead stays the bottleneck.

Identity layers and the operator mapping live in [`adoption/adoption.md`](../adoption/adoption.md#agent-identity-separate-the-agent-from-the-approver); hooks versus CI in [`controls/gates.md`](../controls/gates.md#hooks-nudge-ci-enforces); secrets in general in [`standards/security.md`](../standards/security.md#secrets); context files in [`context-and-hats.md`](context-and-hats.md). This page adds the operating rules. MUST / SHOULD carry their RFC 2119 meaning.

## Agent identity

- **MUST** run each agent under its own identity — a bot or app — with the fewest permissions and repositories the task needs. **MUST NOT** run an agent on a person's credential.
  *Why:* a person's credential carries every right that person has, and it makes the agent's actions indistinguishable from theirs, so "approver ≠ author" stops meaning anything.
- **SHOULD** use short-lived tokens issued per task (an app installation token, narrowed to the repositories and permissions needed) over long-lived personal tokens.
  *Why:* a leaked token that expires within the hour is a smaller incident than one that lives for months.
- **MUST** confine agent writes to agent-only branches (a reserved prefix) and keep the default branch writable only through a reviewed merge.
  *Why:* an agent that can push to the default branch can ship unreviewed code by mistake or by instruction.
- **MUST** enforce these limits on the server — rulesets, required checks, environment protection — and treat client-side hooks as an early warning only. CI jobs that run agent work **SHOULD** use ephemeral runners, one job each.
  *Why:* a hook runs on the machine the agent controls; a persistent runner carries one job's state into the next.
- **MUST** stop and report when a guard, hook, ruleset or permission check blocks an agent — with the exact command and the block message. **MUST NOT** look for an alternate route: another ref, the API instead of git, another credential, or switching a sandbox off. Only the owner of the guard decides to change it.
  *Why:* a guard that an agent routes around protects nothing, and the route it found is now a habit.

## Parallelism

- **SHOULD** parallelise reading, research and review; **MUST** keep one writer per task (one branch, one set of files).
  *Why:* readers do not conflict; two writers on one task overwrite each other silently.
- **MUST** claim a task before starting to write (an assignment, a draft pull request, a claim record), and **MUST** stop when the task is already claimed.
  *Why:* without a lock, two agents finish the same work and someone throws one away — or merges both.
- **MUST** give each agent its own worktree or sandbox.
  *Why:* a shared working tree mixes uncommitted changes from different tasks.
- **MUST NOT** use the stash to carry work between agents or tasks; commit to the agent's own branch, or write a patch file.
  *Why:* worktrees of one repository share every ref under `refs/`, the stash included; one agent can apply or drop another's stash.

## Secrets

- **MUST** mask secrets by machine — the CI runner's masking, an output filter, a scanner in front of every stored log — never by instructing the agent not to print them.
  *Why:* an instruction is followed most of the time; a secret printed once is leaked.
- **MUST** make detectors report counts and locations (file, line, rule) only, never the matched value. A review of a change that removes a secret reads the counts, not the diff's removed lines.
  *Why:* a detector or a reviewer that echoes the value creates a second leak, in logs nobody planned to protect.
- **MUST**, when a secret leaks: revoke and rotate first, then remove it and review the removal. Removing it from the code or history does not undo the leak.
  *Why:* the exposed value works until it is revoked; every review cycle before rotation keeps it usable.
- **MUST NOT** give one agent all three of: access to private data, exposure to untrusted content, and a way to send data out. Remove one leg.
  *Why:* no current defence reliably stops untrusted text from steering an agent; only the missing leg does.

## Observability

- **MUST** check silent paths end to end: for every send, count what was received and compare. **MUST** fail closed at startup when required configuration is missing — refuse to start, never default to "off".
  *Why:* a sender that reports success while nothing arrives, or a service that starts with its check disabled, looks healthy until someone asks.
- **MUST** report merged, deployed and used as three separate states.
  *Why:* merged code that is not deployed, or deployed code nobody uses, has delivered nothing, and a single "done" hides which.
- **SHOULD** derive the delivery numbers from the deploy log ([`standards/change-and-deployment.md`](../standards/change-and-deployment.md#measure-delivery-from-the-deploy-log)) — including the change fail rate — and add the time a change waits for approval, per review tier.
  *Why:* when agents write faster, waiting for a human approval can grow into a large share of lead time, and the delivery numbers alone do not show it.

## Minimal context files

- **SHOULD** keep the always-loaded agent context file short ([`context-and-hats.md`](context-and-hats.md#three-tiers), Tier 1); move rules into on-demand docs or skills, and rules that must always hold into hooks or checks.
  *Why:* one study found context files did not generally raise task success and raised inference cost by over 20%; that is one study's finding, and it points the same way as the Tier 1 guidance in [`context-and-hats.md`](context-and-hats.md).
- **MUST NOT** delete a rule that was paid for by an incident when slimming the file. Move it and leave a one-line pointer to where it now lives.
  *Why:* the rule is the only trace of what the incident cost; without the pointer the next reader re-learns it the same way.

## Transfer loop

How a practice moves from the lead to the team: **explore → codify → teach → team runs → lead steps back.**

| Step | Output |
|---|---|
| explore | the lead works the problem and finds what holds |
| codify | a doc, skill or check in the repo, not in the lead's head |
| teach | the team runs it once with the lead watching |
| team runs | the team runs it; the lead reviews results, not steps |
| lead steps back | the lead is consulted only on exceptions |

- **MUST** write the step-back criteria before teaching, as numbers: for example, the team ran the practice a declared number of consecutive times without the lead stepping in; its rework or failure rate is at or below the lead's baseline; someone other than the lead has updated the codified doc.
  *Why:* without criteria, stepping back happens by fatigue, or never.
- **SHOULD** review each practice monthly: criteria met ⇒ step back further; missed ⇒ the lead steps in, and the doc or check is fixed before the next round.
  *Why:* a monthly look catches drift before it becomes the way the team works.

## Sources

Current practice, each opened on the date shown:

- GitHub Docs — Generating an installation access token for a GitHub App (expires after one hour; narrowed by repositories and permissions) — <https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-an-installation-access-token-for-a-github-app> (accessed 2026-10-08)
- GitHub Docs — Managing your personal access tokens (fine-grained over classic; use an app for organization access and long-lived integrations) — <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens> (accessed 2026-10-08)
- GitHub Docs — Available rules for rulesets — <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets> (accessed 2026-10-08)
- GitHub Docs — Autoscaling with self-hosted runners (ephemeral runners: one job each, a clean environment per job) — <https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/autoscaling-with-self-hosted-runners> (accessed 2026-10-08)
- GitHub Docs — About push protection — <https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection> (accessed 2026-10-08)
- GitHub Docs — Using secrets in GitHub Actions (mask values with `add-mask`; values printed outside the masking are not redacted) — <https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions> (accessed 2026-10-08)
- git documentation — git-worktree, Refs (refs under `refs/` are shared across worktrees, except `refs/bisect`, `refs/worktree` and `refs/rewritten`) — <https://git-scm.com/docs/git-worktree> (accessed 2026-10-08)
- OWASP — Secrets Management Cheat Sheet (revocation, rotation, then deletion; secrets never logged in plaintext) — <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html> (accessed 2026-10-08)
- Simon Willison — The lethal trifecta for AI agents: private data, untrusted content, and external communication — <https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/> (accessed 2026-10-08)
- DORA — Software delivery performance metrics (change fail rate; deployment rework rate) — <https://dora.dev/guides/dora-metrics/> (accessed 2026-10-08)
- DORA — Streamlining change approval — <https://dora.dev/capabilities/streamlining-change-approval/> (accessed 2026-10-08)
- Gloaguen et al. — Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents? (arXiv 2602.11988; one study) — <https://arxiv.org/abs/2602.11988> (accessed 2026-10-08)
