# 05 — Adoption

> Who reads this: whoever brings v7 to an organisation or a product repo.
> When: the first week, and when you add a second consuming repo.

**SDLC Framework Version**: 7.0.0

*Shortens:* onboarding to "clone and open the CLI", and policy changes to one PR in one repo.

## Day one in a repo

Clone. Open the agent CLI. That is all a developer does. The generated files already carry the policy, the hats and the gates for the repo's tier. Nothing to remember, nothing to install by hand.

Measure it: time from clone to the first safe change, where "safe" = CI green, not "the developer says done".

## Policy repo pattern

One repo holds the policy. Product repos consume it. Derivation runs one way: **framework → policy repo → adapters and product CI**. The framework learns back from an instance only through a versioned PR.

| Path | Holds |
|---|---|
| `projects.yaml` | each product repo: tier scheme, declared metadata, [risk-floor](risk-floor-paths.md) and residency paths |
| `tiers.yaml` | tier definitions and model/agent lanes allowed per tier |
| `rules-v7.md` | the rule table for product scope (format: [`01`](01-rule-contract.md)) |
| `souls/` | hats — role files a person or agent wears per product (see [`04`](04-context-and-hats.md)) |
| `gates/` | gate scripts for `PRODUCT_CI` and `RUNTIME_PROBE` |
| `adapters/gen.sh` | generates vendor files for each CLI you actually use; byte-identical on two runs |
| `.approvers` | who may approve risk-floor deploys, and which person operates each agent identity; checked as `reviewer ≠ author` and `reviewer ≠ operator(author)` |
| `CONTROL_SURFACE` | the list of paths above that can change enforcement |

- **Pinning.** Products pin a release tag; generated files record the resolved SHA. Upgrades go by tag, not by bare SHA — bumping bare SHAs by hand across many repos gets abandoned.
- **Drift check.** Product CI regenerates adapters at the pinned ref; any diff is drift. Count hand edits of generated files — it measures use, not ceremony.
- **Control surface.** Changes to `CONTROL_SURFACE` need independent review. `.approvers` is not a trust anchor if a PR can edit it; authority comes from a protected team or ruleset. The policy repo inherits the governance tier of its highest consumer.
- **Tier comes from the policy.** The reusable workflow reads it from the policy repo at the pinned ref. It takes no tier input from the product.

## Agent identity: separate the agent from the approver

Without this, every "human ≠ author" rule is satisfied by the agent itself.

| Mechanism | Concretely | Red case |
|---|---|---|
| **Bot actor** | agents act as a least-privilege bot/app: write content, open PRs; no admin, no environment approval, no ruleset edits | agent calls environment approval ⇒ 403 |
| **Owner token off the agent machine** | the agent's CLI is logged in as the bot only; owner actions go through a browser or mobile app with 2FA, or a separate OS user | `auth status` inside the agent session ≠ owner |
| **Bypass empty — owner still root of trust** | rulesets with no bypass actors prove only that bypass is not configured; an org owner can still edit them. The real control is the **audit log + a daily live↔policy diff** | ruleset edited ⇒ drift red within a day |
| **Four identity layers** | `accountable_member` (a person) · `execution_actor` (the authenticated code-host actor) · `agent_role` (e.g. `agent:reviewer` — never the same label as a person) · `agent_session` | commit without trailers ⇒ 2 |

Authority comes from the **authenticated actor**, never from commit trailers. Trailers are for trace only. Count "two agents edited the same file within 24h"; above 0 ⇒ look.

**Operator mapping.** An agent's `execution_actor` is a bot; its `accountable_member` is the person who runs it. Record that pair in the protected approvers file (`bot:<bot-login> operated_by=<human-login>`), so the approver gate refuses a person approving their own agent's PR ([`03`](03-gates.md)). List every agent identity, including machine users the code host reports as ordinary users: the gate can only map what the file lists. The file is in `CONTROL_SURFACE`; a PR cannot edit the file it is judged by.

This is also the cheapest way to observe: identity fixed at the source beats any collector.

## Four 30-day experiments

Try before you standardise. Pre-register metric, threshold and adjudicator **before** the start. The adjudicator is one real person who is not the author — never the agent that built the thing.

| Experiment | Metric | Kill / continue |
|---|---|---|
| **Tier by evidence** on a few repos | ≥1 repo moves up because of evidence, and ≥1 merge or deploy is refused that headcount tiers would have allowed; 10 diffs hand-judged for false positives/negatives | 0 refusals ⇒ the tier is a label; withdraw it |
| **Fresh-context AI reviewer** in the production lane (CI check-run, own key, budget cap) | (i) fixed defect set, n ≥ 20, taxonomy published first, built by someone other than the prompt author: precision and recall; (ii) real PRs: 5 findings a week judged confirmed/false | recall < 0.6 or precision < 0.5, or < 3/5 confirmed ⇒ the AI is supplementary, not independent |
| **New developer**, scripted and timed checklist | time to first safe change (CI green) + steps outside the checklist | > 2 extra steps or > 30 min ⇒ fix the GUIDE |
| **Policy repo + generated adapters** on **2** repos, then plant one deliberate drift | 0 hand edits of generated files; drift detection latency | drift not caught in one CI run ⇒ the distribution model is not usable yet |

- **Evaluate the mechanism you rely on, not a surrogate.** Test the reviewer in the CI lane it will run in, not in a developer session.
- One consuming repo is a compiler demo, not proof that the distribution model is worth keeping.
- Leading signals for the first 14 days: the agent-approval red case returns 403 · approval latency p50/p90 · break-glass per week · decisions taking effect by default · known-debt entries that never expire.
- 30 days is too short for change-fail rate. Record the baseline now; compare at 90 days.

## Kill criteria — examples

Write them before you build. A kill is the experiment speaking in numbers, not a failure.

- A gate with no real red case by its deadline gets **one** new deadline in the ledger; missing it twice ⇒ drop the gate.
- A policy repo with < 2 real consumers at its deadline ⇒ fold it back into one repo.
- A ritual whose output is not cited in any decision for 6 weeks ⇒ stop the ritual.
- An advisory gate still > 0 at its deadline ⇒ `REVIEW` or delete (G4).
