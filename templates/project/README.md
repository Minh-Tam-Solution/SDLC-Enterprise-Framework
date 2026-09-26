# Project templates

**SDLC Framework Version**: 7.0.0

Copy-and-edit files for a new repo. The rules they follow: [`lifecycle.md`](../../core/lifecycle.md) · [`project-structure.md`](../../standards/project-structure.md) · [`documentation.md`](../../standards/documentation.md).

## Create the docs tree

```bash
mkdir -p docs/{00-foundation,01-planning,02-design/01-ADRs,03-integrate,04-build,05-test,06-deploy,07-operate,08-collaborate,09-govern,10-archive}
```

Keep the folders for the stages your tier must cover ([`lifecycle`](../../core/lifecycle.md#which-stages-each-tier-must-cover)); add the others when a document needs them.

## Templates

| File | Copy to | Tier |
|---|---|---|
| [`current-sprint.md`](current-sprint.md) | `docs/04-build/current-sprint.md` | STANDARD+ (LITE optional) |
| [`sprint-index.md`](sprint-index.md) | `docs/04-build/sprint-index.md` | STANDARD+ |
| [`roadmap.md`](roadmap.md) | `docs/01-planning/roadmap.md` | PROFESSIONAL+ |
| [`ADR-template.md`](ADR-template.md) | `docs/02-design/01-ADRs/ADR-NNN-<topic>.md` | all |
| [`SPEC-template.md`](SPEC-template.md) | `docs/02-design/SPEC-NNNN-<topic>.md` | all |

Agent context files (`AGENTS.md`, PREAMBLE, SOUL): [`../03-Agent-Templates/`](../agent/).
