# Security

> Who reads this: whoever builds, reviews or runs a product that has real users — person or agent — and whoever lets agents act on it.
> When: at design, on every change that touches the risk floor, when adding a dependency, and when setting up CI.

**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: developers and agents building products; reviewers of risk-floor changes; whoever maintains CI
**Review by**: 2026-12-26

*Shortens:* the time a vulnerability lives between being written and being caught — and the blast radius when a credential or an agent is misused.

Risk-floor paths and who must approve them are in [`controls/risk-floor-paths.md`](../controls/risk-floor-paths.md); tiers and data kinds in [`controls/tiers.md`](../controls/tiers.md); rotate-on-leak in [`policies/artifact-lifecycle.md`](../policies/artifact-lifecycle.md). Reference editions today: OWASP ASVS 5.0, OWASP Top 10:2025, OWASP Top 10 for LLM Applications 2025, NIST SSDF (SP 800-218).

## Design

- **Threat-model the change, not only the product.** A change that touches authentication, authorisation, payment, personal data, an external integration or infrastructure gets a short threat model before it is built: for each asset, ask how it could be spoofed, tampered with, denied, disclosed, made unavailable or used to gain privilege. Required from PROFESSIONAL up on risk-floor changes; recommended below.
- **Authorisation is enforced on the server, at object and function level,** with the least privilege that works — never in the client, and never by trusting a model's output.
- **Inbound integrations are checked at the boundary:** verify the signature, validate the payload against its schema, grant read-only scopes by default, rate-limit.
- **Where tenant isolation is not written down, an agent stops and asks.** It does not pick an isolation scheme.
- **Collect and keep only the personal data the feature needs**, for as long as it needs it; the retention period is a decision, written down.

## Authentication

- **Passwords follow current guidance:** at least 15 characters when the password is the only factor (8 with a second factor), checked against a list of known-compromised passwords, no composition rules, no forced periodic change without evidence of compromise.
- **Test hostile tokens:** expired, tampered and unsigned tokens are rejected; a token stops working after logout; repeated failed logins are rate-limited or locked.
- **Security tests run through the real authentication and authorisation code** ([`testing.md`](testing.md)); a skip marker on a security test is not accepted.
- **Authorisation tests prove denial,** not only access: user A's token on user B's object returns 403, and changing an object id in the path, query or body is refused.

## Secrets

- **No secret in git, ever.** Commit a template of variable names (`.env.example`); keep the real file ignored.
- **Block secrets at push time on the server, not only in a local hook,** and scan again in CI and before a deploy. A local hook runs on the machine the agent controls. A secret found in the repository is treated as leaked: revoke and rotate; rewriting history does not undo it.
- **Prefer short-lived, narrowly scoped credentials** to long-lived keys; CI never holds the most sensitive ones if it can avoid it.
- **Keep secrets out of what agents see and write:** not in the agent's environment, not in instruction files, not in its outputs. Scan agent output before it is stored as a log or evidence.
- **Rule SECRET-1 blocks secret-shaped values in the lines a change adds** ([`scripts/rule-no-new-secrets.sh`](../scripts/rule-no-new-secrets.sh)); old findings go into `.secret-allowlist` with an owner and an expiry. A scanner proves itself with a planted fake secret ([`controls/gates.md`](../controls/gates.md), G1), and a broken scanner reports "cannot measure", never "clean".

## Dependencies and the supply chain

- **Check before adding:** every new dependency gets a known-vulnerability and licence check, and — when an agent suggested it — a check that the package exists and is the one intended. Agents propose packages that do not exist, and attackers register those names.
- **Scan dependencies on every change,** with a fix deadline per severity (critical within days, not weeks). A new scanner starts as a report and climbs the ladder ([`controls/gates.md`](../controls/gates.md)).
- **Licence policy is declared,** and a dependency under a licence the product cannot accept blocks the release unless it sits behind a process or network boundary that the architecture shows.
- **Pin dependencies — including CI actions — by hash,** install through the official package manager, and keep a dependency-update bot whose pull requests actually get merged.
- **From PROFESSIONAL up, each release carries a software bill of materials** generated in CI and stored with the artifact, and build provenance showing which commit and which builder produced it.

## CI is part of the product

- **CI definitions are on the risk floor** (`.github/workflows/`, or your code host's equivalent — [`controls/risk-floor-paths.md`](../controls/risk-floor-paths.md)); review container build files and environment files as carefully.
- **The CI token is read-only by default;** a job that must write gets write for that job only.
- **Contributions from outside run without secrets** — sandboxed with no network and no credentials, or held until a maintainer approves.
- **Never run untrusted code in a privileged workflow,** and never paste untrusted text (titles, branch names, comments) into a script: pass it through an environment variable.

## Agents

Coding agents read untrusted text all day while holding write credentials.

- **Treat everything an agent reads as possibly hostile:** files, issues, pull requests, web pages and tool output can carry instructions.
- **Give an agent the fewest tools and permissions that do the job;** prefer narrow tools to an open shell. An agent that has a shell can reach any network, whatever its network allow-list says.
- **Authorisation for an agent's actions lives in the system it acts on,** not in its instructions: a privileged call from an agent identity is refused unless that identity may make it ([`adoption/adoption.md`](../adoption/adoption.md), agent identity).
- **High-impact actions wait for a person:** payments, deletion of data, permission changes, sending messages outside the team.

## Operating securely

- **No personal data or secrets in logs or error responses;** always log security events ([`observability.md`](observability.md)).
- **Browser-facing services** set security headers and never allow any origin by wildcard.
- **Security incidents have a severity, a response target and an escalation path,** and the record states whether a regulator or the affected people must be told.

## Candidate rules

Each enters through [`practices/lessons-to-rules.md`](../practices/lessons-to-rules.md).

| Candidate | Command idea |
|---|---|
| secrets in added lines (SECRET-1, now in the register) | `scripts/rule-no-new-secrets.sh` |
| secret push protection on every repository | repository settings check |
| new dependency exists and is allowed | diff of the dependency manifest against the registry and an allow-list |
| pinned CI actions, read-only default token | workflow lint |
| denial tests exist | a 403 test per route with an object id |
| no mocks or skips in security tests | scan of auth test files, with a planted positive control |
| threat model on risk-floor changes | a link in the PR when a risk-floor path changed |

## Sources

From the archive: the rows for this standard in [`MIGRATION-MAP.md`](../MIGRATION-MAP.md).

Current practice, each opened on the date shown:

- NIST Special Publication 800-63B (revision 4) — <https://pages.nist.gov/800-63-4/sp800-63b.html> (accessed 2026-09-26)
- OWASP Top 10 for LLM Applications 2025 — LLM01 Prompt Injection — <https://genai.owasp.org/llmrisk/llm01-prompt-injection/> (accessed 2026-09-26)
- OWASP Top 10 for LLM Applications 2025 — LLM06 Excessive Agency — <https://genai.owasp.org/llmrisk/llm062025-excessive-agency/> (accessed 2026-09-26)
- OpenSSF — Security-Focused Guide for AI Code Assistant Instructions — <https://best.openssf.org/Security-Focused-Guide-for-AI-Code-Assistant-Instructions.html> (accessed 2026-09-26)
- NIST SP 800-204D — Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines — <https://csrc.nist.gov/pubs/sp/800/204/d/final> (accessed 2026-09-26)
- OWASP — Secrets Management Cheat Sheet — <https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html> (accessed 2026-09-26)
- OpenSSF Scorecard — Checks — <https://github.com/ossf/scorecard/blob/main/docs/checks.md> (accessed 2026-09-26)
- SLSA v1.0 — Security levels — <https://slsa.dev/spec/v1.0/levels> (accessed 2026-09-26)
- OWASP Application Security Verification Standard (5.0) — <https://github.com/OWASP/ASVS> (accessed 2026-09-26)
- OWASP Top 10:2025 — <https://top10.owasp.org/2025> (accessed 2026-09-26)
- NIST SP 800-218 — Secure Software Development Framework (SSDF) Version 1.1 — <https://csrc.nist.gov/pubs/sp/800/218/final> (accessed 2026-09-26)
