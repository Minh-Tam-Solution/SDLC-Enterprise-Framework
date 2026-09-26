# Contributing to the SDLC Enterprise Framework

**Owner**: @dttai71
**Consumer**: anyone proposing a change to this repository
**Review by**: 2026-12-26

Thanks for your interest in contributing.

The SDLC Framework is a **tool-agnostic methodology repository** — it defines *what* AI+Human teams should do (principles, processes, gates), not *how* a specific tool implements it. Contributions therefore differ from typical software project PRs: the bar for adding a pattern is **why this generalizes across implementations**, not just "this works for my team."

## Contribution Categories

Different change types follow different review paths:

| Category | Examples | Review Path |
|----------|----------|-------------|
| **Editorial** | Typo fixes, broken-link repairs, grammar | 1 maintainer review |
| **Clarifying** | Expanded examples for an existing principle, table reformatting, cross-reference improvements | 1 maintainer review |
| **Pattern addition** | New template, new standard or practice, new section in an existing document | issue first, naming the consumer → maintainer review |
| **Methodology change** | Change to a core principle, a policy, a tier, a gate or a rule row | issue with the burn case first → maintainer review → CHANGELOG entry and a version bump |
| **Removal / deprecation / move** | Retiring, renaming or moving an artifact | Must follow [`policies/artifact-lifecycle.md`](policies/artifact-lifecycle.md) |

## Before You Open a PR

For **methodology changes** (anything beyond editorial or clarifying), please open an issue or RFC discussion first. The Framework's value depends on each topic having one owning document — uncoordinated changes create two versions of the truth.

For all changes:

1. Read the [README.md](README.md) sections "What the framework is" and "Layout of this repo" to confirm your change belongs in the Framework — not in an adopting repo — and which folder owns it
2. Check [CHANGELOG.md](CHANGELOG.md) — your change may already be in flight
3. Check [`policies/artifact-lifecycle.md`](policies/artifact-lifecycle.md) if your change renames, moves or retires anything

## PR Process

1. Fork the repo and create a feature branch (e.g. `feat/standard-testing`, `fix/gates-catalog`, `docs/clarify-tiers`)
2. Make your changes, keeping each PR focused on a single concern
3. Update cross-references; a moved or renamed file gets a row in the `MIGRATION-MAP.md` path map; a new live doc carries `**Owner**`, `**Consumer**` and `**Review by**`
4. Update `CHANGELOG.md` with a one-line entry under the next version's "Unreleased" section
5. Open a PR with:
   - Clear description of what changes and why it generalizes
   - Reference to the issue/RFC for non-trivial changes
   - DCO sign-off (see below)

## Developer Certificate of Origin (DCO)

Contributions from outside the maintainers must include a `Signed-off-by` line on each commit (not yet checked by CI):

```bash
git commit -s -m "fix(gates): clarify G3 evidence requirements"
```

The DCO certifies that you wrote the contribution or otherwise have the right to submit it under the open source license used by the project. Full text: <https://developercertificate.org/>

## Conventional Commits

Use conventional commit prefixes for clarity:

- `feat(scope): ...` — new pattern, template, SOUL, or section
- `fix(scope): ...` — correction to an existing pattern
- `docs(scope): ...` — documentation-only changes (no methodology change)
- `refactor(scope): ...` — restructuring without semantic change
- `chore(scope): ...` — repository housekeeping

Scope examples: `core`, `controls`, `standards`, `gates`, `templates`, `scripts`.

## Kinds of document

Each folder holds one kind. Put a change where its kind lives; a topic has one owning document.

| Folder | Kind | Test |
|---|---|---|
| `core/` | methodology that outlives tools | would it still be true with different agents and vendors? |
| `policies/` | normative decisions for the framework itself | does it decide how this repository or its artifacts are governed? |
| `standards/` | what every adopting repo follows | can a repo be checked against it? |
| `controls/` | rules and gates a machine runs | does it name a command with an exit code? |
| `ai-engineering/` | working with agents | would it change if the agent tooling changed? |
| `practices/` | how to do it well, by choice | is it advice rather than a requirement? |
| `adoption/` | bringing the framework to a team or repo | is it about the first weeks of use? |

## Script naming

Scripts in `scripts/` use English, kebab-case, verb-first names: `check-*` for a validator/report,
`rule-*` for a rule-contract gate, `gen-*` for a generator. (Adopted 2026-09-25.) The v6
Python tools that predated this convention were archived to `archive/v6/scripts/` on
2026-09-26; no grandfathered names remain.

## Style Conventions

- **Markdown** — GitHub-flavored Markdown; tables for structured comparisons; headings follow the existing hierarchy in each section
- **Voice** — write in the active voice; prefer concrete examples to abstract claims; cite version numbers when referencing patterns that have evolved
- **Vendor neutrality** — do not name specific company products in normative content (`core/`, `controls/`, `standards/`, `ai-engineering/`, `adoption/`, `practices/`, `templates/`, `scripts/`). The Framework is implementation-neutral by design; a burn case describes the incident, not the company
- **Cite ADRs** — when adding or changing a pattern, link to the originating or governing ADR (in the implementing platform repo if no Framework-side ADR exists yet)
- **Don't add a comment when a clearer name would do** — prefer self-explanatory section names and headings over explanatory prose

## Naming & size

Each rule below says what it shortens.

| Rule | Shortens |
|---|---|
| **English only** in docs, scripts, commit messages | translation and two versions drifting apart |
| **kebab-case** file names (`tiers.md`, `check-doc-count.sh`) | guessing paths |
| **Verb-first scripts**: `check-*` for gates, `rule-*` for single-rule checks | finding the gate behind a rule |
| **Each doc ≤150 lines** | docs nobody finishes reading |
| **Every live doc carries `**Owner**`, `**Consumer**` and `**Review by**`** in its header; the ownership gate ([`scripts/check-doc-ownership.sh`](scripts/check-doc-ownership.sh)) blocks a missing field or a passed date | docs written for nobody, and docs nobody re-checks |
| **The doc-count gate** ([`scripts/check-doc-count.sh`](scripts/check-doc-count.sh)): live docs outside `archive/` and `templates/` >40 is flagged, never blocked | the framework growing back to hundreds of files unnoticed |

Prefer editing an existing doc over adding one. Prefer a table over prose. Prefer a gate over a paragraph.

## Review Criteria

Maintainers evaluate PRs against these questions:

1. **Generalization** — does this pattern work across implementations, team sizes, tech stacks?
2. **Coherence** — does one document own this topic, and is it in the folder for its kind (see "Kinds of document")?
3. **Evidence** — for methodology changes, what real-world signal motivated this? (case study, retrospective, audit finding, cross-team feedback)
4. **Reversibility** — can this change be rolled back without breaking adopters' existing implementations?
5. **Tool-agnosticism** — is this free of assumptions about specific tools, platforms, or vendors?

## Reporting Security Issues

If you discover a security or methodology-integrity issue, please report it via email per [SECURITY.md](SECURITY.md) instead of opening a public issue.

## Code of Conduct

By participating, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

By contributing, you agree that your contributions will be licensed under the MIT License (see [LICENSE](LICENSE)).
