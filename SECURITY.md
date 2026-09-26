# Security Policy

**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: anyone reporting a vulnerability
**Review by**: 2026-12-26

## Scope

The SDLC Enterprise Framework is a **tool-agnostic methodology repository** — it ships documentation, templates, governance patterns and small gate scripts, not production code. The "security" surface here is therefore narrower than for a typical software project, but not zero.

This policy covers:

- **Methodology integrity** — corruption of governance patterns, dilution of gate semantics, malicious PRs that weaken quality controls
- **Document supply chain** — tampering with templates, SOULs, or scaffolds that downstream implementers consume
- **Cross-reference safety** — broken or misleading links to external resources that could mislead adopters
- **Sensitive data hygiene** — accidental inclusion of credentials, internal hostnames, or proprietary names in documentation

This policy does **not** cover:

- Security of platforms that *implement* the Framework (e.g., orchestration platforms, third-party tools) — those have their own security policies
- Security of contributor tooling (Git, editors, CI providers)

## Supported Versions

| Version | Supported |
|---------|-----------|
| 7.x (`main`, latest tag) | Yes (current) |
| 6.x and earlier | No — archived in `archive/`, no maintenance |

Earlier versions remain readable in `archive/` and in git tags for historical reference.

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to: **dttai@mtsolution.com.vn**

Include:

- Description of the issue (methodology corruption, document tampering, sensitive data leak, etc.)
- Affected file(s) or pattern(s)
- Impact assessment (which adopters, gates or rules are affected)
- Suggested remediation (if any)

## Response Timeline

| Action | Timeline |
|--------|----------|
| Acknowledge receipt | 48 hours |
| Initial assessment | 5 business days |
| Critical fix (e.g., credential leak, gate-bypass pattern) | 7-14 days |
| Non-critical fix (e.g., cross-reference tightening) | Next minor release cycle |

## Methodology Integrity Controls

The Framework applies the following controls to protect governance pattern integrity:

- **Gate semantics protected** — Changes to stage gates (G0.1–G4), tiers, the rule register or a gate script go through a PR with CI green on its head commit and maintainer review; every gate keeps a selftest with a case that turns it red
- **Agent templates protected** — Changes to the PREAMBLE and SOUL templates require maintainer review
- **Template provenance** — Templates in `templates/` point to the document they implement
- **Cross-reference audit** — Internal links checked by hand at every move; no link-checking gate yet (candidate rule in `policies/artifact-lifecycle.md`)

## Document Supply Chain

- Releases are annotated tags on a merge commit of `main`. They are **not GPG-signed** today
- `CHANGELOG.md` is the authoritative record of methodology changes per version
- [`policies/artifact-lifecycle.md`](policies/artifact-lifecycle.md) governs how artifacts are moved, deprecated and archived (no silent removals; every move is recorded in `MIGRATION-MAP.md`)

## Sensitive Data Hygiene

The Framework is intentionally **vendor-neutral** — internal company names, tenant identifiers, or product brand names of any specific implementer must not appear in normative content (`core/`, `policies/`, `standards/`, `controls/`, `ai-engineering/`, `adoption/`, `practices/`, `templates/`, `scripts/`). `archive/` may contain historical references for context.

If you find sensitive data leakage in normative content, please report via the email channel above — this is treated as a critical issue.

## Acknowledgements

We are grateful to the security and methodology research communities. Reporters of valid issues will be credited (with permission) in the corresponding `CHANGELOG.md` entry.
