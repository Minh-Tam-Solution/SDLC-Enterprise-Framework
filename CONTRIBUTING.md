# Contributing to the SDLC 6.3.2 Universal Framework

Thanks for your interest in contributing.

The SDLC Framework is a **tool-agnostic methodology repository** — it defines *what* AI+Human teams should do (principles, processes, gates), not *how* a specific tool implements it. Contributions therefore differ from typical software project PRs: the bar for adding a pattern is **why this generalizes across implementations**, not just "this works for my team."

## Contribution Categories

Different change types follow different review paths:

| Category | Examples | Review Path |
|----------|----------|-------------|
| **Editorial** | Typo fixes, broken-link repairs, grammar | 1 maintainer review |
| **Clarifying** | Expanded examples for an existing principle, table reformatting, cross-reference improvements | 1 maintainer review |
| **Pattern addition** | New SOUL, new template, new section under an existing pillar | ADR-lite proposal first → 2 maintainer review |
| **Methodology change** | Gate semantic change, pillar revision, anti-vibecoding rule change | Full ADR + 2+ maintainer review + version bump |
| **Removal / deprecation** | Sunsetting a pattern | Must follow [DEPRECATION-POLICY.md](DEPRECATION-POLICY.md) |

## Before You Open a PR

For **methodology changes** (anything beyond editorial or clarifying), please open an issue or RFC discussion first. The Framework's value depends on internal coherence across the 7 Pillars — uncoordinated changes risk fragmenting that coherence.

For all changes:

1. Read the [README.md](README.md) "Framework vs. Platform" section to confirm your change belongs in the Framework, not in an implementing platform's repo
2. Check [CHANGELOG.md](CHANGELOG.md) — your change may already be in flight
3. Check [DEPRECATION-POLICY.md](DEPRECATION-POLICY.md) if your change touches an existing pattern

## PR Process

1. Fork the repo and create a feature branch (e.g. `feat/soul-data-engineer`, `fix/pillar-4-gate-table`, `docs/clarify-pillar-2`)
2. Make your changes, keeping each PR focused on a single concern
3. Update relevant cross-references and `CONTENT-MAP.md` if you add/move/rename files
4. Update `CHANGELOG.md` with a one-line entry under the next version's "Unreleased" section
5. Open a PR with:
   - Clear description of what changes and why it generalizes
   - Reference to the issue/RFC for non-trivial changes
   - DCO sign-off (see below)

## Developer Certificate of Origin (DCO)

All commits must include a `Signed-off-by` line:

```bash
git commit -s -m "feat(pillar-4): clarify G3 evidence requirements"
```

The DCO certifies that you wrote the contribution or otherwise have the right to submit it under the open source license used by the project. Full text: <https://developercertificate.org/>

## Conventional Commits

Use conventional commit prefixes for clarity:

- `feat(scope): ...` — new pattern, template, SOUL, or section
- `fix(scope): ...` — correction to an existing pattern
- `docs(scope): ...` — documentation-only changes (no methodology change)
- `refactor(scope): ...` — restructuring without semantic change
- `chore(scope): ...` — repository housekeeping

Scope examples: `pillar-4`, `soul-pm`, `template-sprint-plan`, `governance`, `g3-gate`.

## Style Conventions

- **Markdown** — GitHub-flavored Markdown; tables for structured comparisons; headings follow the existing hierarchy in each section
- **Voice** — write in the active voice; prefer concrete examples to abstract claims; cite version numbers when referencing patterns that have evolved
- **Vendor neutrality** — do not name specific company products in normative content (Pillars 0-7, Sections 8-9). The Framework is implementation-neutral by design. Examples and case studies belong in `06-Case-Studies/` and may be specific
- **Cite ADRs** — when adding or changing a pattern, link to the originating or governing ADR (in the implementing platform repo if no Framework-side ADR exists yet)
- **Don't add a comment when a clearer name would do** — prefer self-explanatory section names and headings over explanatory prose

## Review Criteria

Maintainers evaluate PRs against these questions:

1. **Generalization** — does this pattern work across implementations, team sizes, tech stacks?
2. **Coherence** — does this fit with the existing 7-Pillar structure and the relationships between pillars?
3. **Evidence** — for methodology changes, what real-world signal motivated this? (case study, retrospective, audit finding, cross-team feedback)
4. **Reversibility** — can this change be rolled back without breaking adopters' existing implementations?
5. **Tool-agnosticism** — is this free of assumptions about specific tools, platforms, or vendors?

## Reporting Security Issues

If you discover a security or methodology-integrity issue, please report it via email per [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Code of Conduct

By participating, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the MIT License (see [LICENSE](LICENSE)).
