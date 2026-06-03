# Security Policy

## Scope

The SDLC 6.3.2 Universal Framework is a **tool-agnostic methodology repository** — it ships documentation, templates, and governance patterns, not executable production code. The "security" surface here is therefore narrower than for a typical software project, but not zero.

This policy covers:

- **Methodology integrity** — corruption of governance patterns, dilution of gate semantics, malicious PRs that weaken quality controls
- **Document supply chain** — tampering with templates, SOULs, or scaffolds that downstream implementers consume
- **Cross-reference safety** — broken or misleading links to external resources that could mislead adopters
- **Sensitive data hygiene** — accidental inclusion of credentials, internal hostnames, or proprietary names in documentation

This policy does **not** cover:

- Security of platforms that *implement* the Framework (e.g., SDLC Orchestrator, third-party tools) — those have their own security policies
- Security of contributor tooling (Git, editors, CI providers)

## Supported Versions

| Version | Supported |
|---------|-----------|
| 6.3.1   | Yes (current) |
| 6.3.0   | Security advisories only |
| < 6.3.0 | No |

Earlier versions remain available in `10-Archive/` for historical reference but receive no maintenance.

## Reporting a Vulnerability

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to: **dttai@mtsolution.com.vn**

Include:

- Description of the issue (methodology corruption, document tampering, sensitive data leak, etc.)
- Affected file(s) or pattern(s)
- Impact assessment (which adopters / gates / pillars affected)
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

- **Gate semantics protected** — Changes to G0-G4 gate definitions, Pillar 4 quality criteria, or Section 7 anti-vibecoding rules require ADR + maintainer review
- **SOUL conventions protected** — Changes to SOUL frontmatter or scaffolding patterns require contributor sign-off + maintainer review
- **Template provenance** — All templates in `05-Templates-Tools/` carry a header citing originating ADR or sprint
- **Cross-reference audit** — Internal links checked at release; broken links surfaced before tagging

## Document Supply Chain

- Releases are tagged signed commits (`git tag -s`)
- `CHANGELOG.md` is the authoritative record of methodology changes per version
- `DEPRECATION-POLICY.md` governs how patterns are sunset (no silent removals)

## Sensitive Data Hygiene

The Framework is intentionally **vendor-neutral** — internal company names, tenant identifiers, or product brand names of any specific implementer must not appear in normative content (`01-Overview/` through `09-Continuous-Improvement/`). The `06-Case-Studies/` and `10-Archive/` directories may contain historical references for context.

If you find sensitive data leakage in normative content, please report via the email channel above — this is treated as a critical issue.

## Acknowledgements

We are grateful to the security and methodology research communities. Reporters of valid issues will be credited (with permission) in the corresponding `CHANGELOG.md` entry.
