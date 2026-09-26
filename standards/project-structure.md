# Project structure

> Who reads this: whoever creates a repo, moves documents, or writes a tool that reads another repo's docs.
> When: at repo setup, when adding a stage folder, and before archiving anything.

**SDLC Framework Version**: 7.0.0
**Owner**: @dttai71
**Consumer**: developers creating a repo; tools that read another repo's docs
**Review by**: 2026-12-26

*Shortens:* the time a newcomer — person or agent — needs to find the current sprint, the last decision and the running state of a repo. Every repo answers those three questions in the same place.

## Recommended, not mandatory

The `docs/00–09` layout below is the **recommended** layout. Teams already know it, and tools that report on a repo read it without configuration. Existing repos keep it. A new repo may choose another layout, provided its `AGENTS.md` maps each of the ten stages to where that stage's documents live, so people and tools still find them. What is not optional is the evidence each stage requires by tier ([`lifecycle.md`](../core/lifecycle.md)) and the root and planning files below.

## Documentation is stage-mapped; code is not

| Kind | Where | Mapped to a stage? |
|---|---|---|
| Documentation | `docs/00-foundation/` … `docs/09-govern/` | yes — one folder per stage ([`lifecycle.md`](../core/lifecycle.md)) |
| Code | `backend/`, `frontend/`, `mobile/`, `tools/`, `tests/`, `infra/`, `migrations/` … | no — code is written across stages 02–07 |
| Configuration | files at the repo root | no |

Code folders are named by what they contain, in the language's own convention. A `migrations/` folder raises the tier floor ([`tiers.md`](../controls/tiers.md)), so do not hide migrations under another name.

## The `docs/` tree

```text
docs/
├── 00-foundation/     WHY      problem statement, business case, personas
├── 01-planning/       WHAT     requirements, roadmap, backlog
├── 02-design/         HOW      architecture, ADRs (02-design/01-ADRs/), specs
├── 03-integrate/      CONNECT  API contracts, external dependencies
├── 04-build/          BUILD    sprint plans, current sprint, sprint index, dev guides
├── 05-test/           VERIFY   test plans, QA reports
├── 06-deploy/         SHIP     deployment guides, release notes, runbooks for release
├── 07-operate/        RUN      operations runbooks, monitoring, incident records
├── 08-collaborate/    TOGETHER hand-overs, directives, reviews, meeting records
├── 09-govern/         COMPLY   decisions register, compliance, audits
└── 10-archive/        (not a stage) superseded documents, read-only
```

Rules:

- Folder names are `NN-stage-name/`, two digits, lower-case kebab-case. Tools that read this layout look for the number; a repo with a different layout declares its stage mapping in `AGENTS.md` instead.
- Subfolders inside a stage are numbered the same way when order matters (`02-design/01-ADRs/`), and plain kebab-case when it does not.
- `10-archive/` is not a stage. A document moved there keeps its content unchanged — no header is added; the archive folder's README records what replaced it ([`documentation.md`](documentation.md#archived-documents)).
- A stage folder may hold a `99-legacy/` subfolder for documents that are superseded but still referenced. Tools skip `99-legacy/`; nobody updates it.
- One topic, one living document. Before creating a file, search the stage folder for the topic. A second file on the same topic is how two versions of the truth start.

## Root files

| File | Purpose | LITE | STANDARD | PRO | ENT |
|---|---|---|---|---|---|
| `README.md` | what it is, how to run it — commands that work as written | required | required | required | required |
| `AGENTS.md` (+ tool-specific file, [`context-and-hats`](../ai-engineering/context-and-hats.md)) | always-loaded agent context: stack, commands, owners, current sprint pointer | optional | required | required | required |
| `.gitignore` | keeps secrets and build output out of git | required | required | required | required |
| `.env.example` | every environment variable, no values | if env is used | required | required | required |
| build entry (`Makefile`, `package.json` scripts …) | one command each for build, test, run | optional | optional | required | required |
| local dev environment (`docker-compose.yml` or equivalent) | the stack starts with one command | optional | optional | required | required |
| risk-floor declaration | which paths need independent review ([`risk-floor-paths.md`](../controls/risk-floor-paths.md)) | — | optional | required | required |

`AGENTS.md` points to documents; it does not copy them. A sprint number written into `AGENTS.md` is out of date by the next sprint — write the path of the sprint file instead.

## Planning files

| Level | Horizon | Recommended location | LITE | STANDARD | PRO+ |
|---|---|---|---|---|---|
| Roadmap | 6–12 months, by quarter | `docs/01-planning/roadmap.md` | — | optional | required |
| Phase | 4–8 weeks, one theme | a section of the roadmap, or `docs/01-planning/phases/` | — | — | required |
| Sprint | 5–10 working days, committed | `docs/04-build/current-sprint.md` | optional | required | required |
| Sprint history | all closed sprints | `docs/04-build/sprint-index.md` | — | required | required |
| Backlog | items of hours to days | the issue tracker, linked from the sprint file | optional | required | required |

- The locations are recommendations; the files are what each tier requires. A repo that keeps them elsewhere names the path in `AGENTS.md`.
- `current-sprint.md` has one owner and is updated when a stage gate is passed or re-opened, an ADR is accepted, or a release ships. Its `last_updated` older than the latest merged PR is drift.
- At sprint close, the sprint section moves to `sprint-index.md` with its outcome, and `current-sprint.md` is rewritten for the next sprint.
- Sprint records with numbers in their names (`SPRINT-12-retro.md`) live only in `docs/08-collaborate/sprint-logs/` ([`documentation`](documentation.md#file-names)).
- Templates: [`templates/project/`](../templates/project/).

## Reading order for a newcomer

`README.md` → `AGENTS.md` → `docs/04-build/current-sprint.md` → `docs/04-build/sprint-index.md` → the last five merged PRs → `docs/00-foundation/` and `docs/02-design/` when the task needs the *why* or the *how*.

A tool that reports on a repo reads in the same order and names the file and line it took each fact from. A count without a location cannot be traced, and `0` looks the same as a successful measurement.

## Moving and archiving

- Move with `git mv` so history follows the file. A move and a content change go in separate commits.
- Before archiving a folder, list every file in it and say where each one went. A single-file folder leaves no visible gap when it disappears — a standard was lost that way for thirteen versions.
- After a move, search the whole repo and the known consumers for the old path. A pinned reference (commit SHA) keeps working; the next re-pin must use the new path.
