# Migration map

> Who reads this: whoever finds an old document in `archive/` and asks "what replaced this?", and whoever brings old knowledge back into the live tree.
> When: before rewriting anything from the archive, and after every change that moves content between the archive and the live tree.

**SDLC Framework Version**: 7.0.0
**Status**: ACTIVE
**Owner**: @dttai71
**Consumer**: readers of `archive/`; consuming repos fixing links to moved files
**Review by**: 2026-12-26

*Shortens:* the search for where an old rule went, and the temptation to rewrite an old document instead of harvesting what is still true in it.

## Rules

- `archive/` is not edited. What happened to an archived document is recorded here, one row per source.
- Knowledge is harvested, not files: take the claims that are still true, merge them into the live document that owns the topic, record the row.
- Outcome is one of: `ADOPTED` (the substance lives on) · `PARTIALLY_ADOPTED` (some claims live on; the rest is listed as retired) · `SUPERSEDED` (a different live document answers the same question) · `RETIRED` (no longer true or no longer needed) · `HISTORICAL_ONLY` (kept as record, never in force again).
- A source with no row has not been reviewed yet. That is the default for most of `archive/v6/`.

## Path map

Where each live file of the 7.0.0 layout (`d363387`) went: the layout change of 2026-09-26 (#35) and the version-neutral control names after `v7.0.0-alpha`. Links in consuming repos are fixed with this table. A reference pinned to a commit SHA keeps working; the next re-pin uses the new path.

**Folder rule:** `10-Archive/<path>` → `archive/<path>`, every file, byte-identical.

| Old path | New path | Note |
|---|---|---|
| `v7/00-constitution.md` | `core/constitution.md` | |
| `v7/01-rule-contract.md` | `controls/rule-contract.md` | |
| `v7/02-tiers.md` | `controls/tiers.md` | |
| `v7/03-gates.md` | `controls/gates.md` | |
| `v7/04-context-and-hats.md` | `ai-engineering/context-and-hats.md` | |
| `v7/05-adoption.md` | `adoption/adoption.md` | |
| `v7/06-lessons-to-rules.md` | `practices/lessons-to-rules.md` | |
| `v7/risk-floor-paths.md` | `controls/risk-floor-paths.md` | |
| `v7/README.md` | `README.md` | removed; its index is the README section "Layout of this repo" |
| `templates/PREAMBLE-example.md` | `templates/agent/PREAMBLE-example.md` | |
| `templates/SOUL-example.md` | `templates/agent/SOUL-example.md` | |
| `05-Templates-Tools/07-Scripts/README.md` | `scripts/README.md` | removed; it only pointed to `scripts/` |
| `05-Templates-Tools/07-Scripts/kiem-luat-v7.sh` | `scripts/check-rules.sh` | deprecated shim removed; call the successor |
| `05-Templates-Tools/07-Scripts/kiem-nghiem-phien-ban.sh` | `scripts/check-version-declared.sh` | deprecated shim removed; call the successor |
| `scripts/check-rules-v7.sh` | `scripts/check-rules.sh` | renamed after 7.0.0-alpha; the table heading is now `## Rule register` (`## Rules v7` read until 2026-12-31) |
| `.github/workflows/v7-gate.yml` | `.github/workflows/version-declared.yml` | renamed after 7.0.0-alpha |
| `.github/workflows/v7-rules-gate.yml` | `.github/workflows/rules.yml` | renamed after 7.0.0-alpha |
| `DEPRECATION-POLICY.md` | `policies/artifact-lifecycle.md` | archived to `archive/by-topic/historical-documents/DEPRECATION-POLICY.md` |
| `.github/workflows/v7-gates-product.yml` | `.github/workflows/product-gates.yml` | renamed after 7.0.0-alpha; callers pinned to a SHA keep working, re-pins use the new file |

Check — every file of the old layout that is gone is mapped (expected output: `0`):

```bash
BASE=d363387; git fetch -q origin
comm -23 <(git ls-tree -r --name-only "$BASE" | sort) <(git ls-tree -r --name-only HEAD | sort) |
  while IFS= read -r f; do
    case "$f" in 10-Archive/*) [ -e "archive/${f#10-Archive/}" ] && continue ;; esac
    grep -qF "| \`$f\` |" MIGRATION-MAP.md || echo "UNMAPPED $f"
  done | tee /dev/stderr | wc -l
```

## Map

| Source (in `archive/`) | Outcome | Live successor | Retired concepts |
|---|---|---|---|
| `v6/02-Core-Methodology/SDLC-Stage-Lifecycle-Framework.md` | PARTIALLY_ADOPTED | [`core/lifecycle.md`](core/lifecycle.md) · [`standards/observability.md`](standards/observability.md) · [`standards/testing.md`](standards/testing.md) | stage dependency YAML matrix, artifact SHA256 integrity per stage, evidence vault |
| `v6/02-Core-Methodology/Documentation-Standards/SDLC-Project-Structure-Standard.md` | PARTIALLY_ADOPTED | [`standards/project-structure.md`](standards/project-structure.md) | legacy folder-name aliases (`docs/why/` …), mandatory `docs/00–09` (now recommended) |
| `v6/02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md` | PARTIALLY_ADOPTED | [`standards/documentation.md`](standards/documentation.md) | per-language naming tables, migration-document header |
| `v6/05-Templates-Tools/01-Specification-Standard/SDLC-Specification-Standard.md` | PARTIALLY_ADOPTED | [`standards/documentation.md`](standards/documentation.md) · [`templates/project/SPEC-template.md`](templates/project/SPEC-template.md) · [`standards/testing.md`](standards/testing.md) | reviewers/approver/effort/priority as mandatory front matter; single schema for specs and ADRs |
| `by-version/v4.5/09-Documentation-Standards/FILE-HEADER-STANDARDS-SDLC-4.5.md` | PARTIALLY_ADOPTED | [`standards/documentation.md`](standards/documentation.md#header-of-a-source-file) | framework version, approval, "authenticity" and business-value lines in code headers |
| `v6/05-Templates-Tools/08-Project-Templates/Planning-Hierarchy-*.md` | PARTIALLY_ADOPTED | [`templates/project/`](templates/project/README.md) | separate phase and backlog templates (phase = roadmap section; backlog = issue tracker) |
| `by-topic/ai-governance-v7-retired/08-Governance-Decision-Matrix.md` (risk classification table) | PARTIALLY_ADOPTED | [`controls/risk-floor-paths.md`](controls/risk-floor-paths.md) · [`standards/testing.md`](standards/testing.md) | the rest of the decision matrix |
| `by-topic/historical-documents/DEPRECATION-POLICY.md` (v6.3, live until 2026-09-26) | PARTIALLY_ADOPTED | [`policies/artifact-lifecycle.md`](policies/artifact-lifecycle.md) | redirect stubs at old paths (replaced by the path map), 6-month stub grace period, `CONTENT-MAP.md`, `{NN}-Legacy/` archive layout, `99-Legacy` linter; kept: archive never delete, delete only harmful content, agents do not read the archive, broken links block (now a candidate rule) |
| `v6/03-AI-GOVERNANCE/21-V7-RULE-CONTRACT.md` | SUPERSEDED | [`controls/rule-contract.md`](controls/rule-contract.md) | — |
| `v6/CHANGELOG-v6.md` | HISTORICAL_ONLY | [`CHANGELOG.md`](CHANGELOG.md) (from 7.0.0) | — |
| `v6/02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) · [`standards/testing.md`](standards/testing.md) · [`standards/change-and-deployment.md`](standards/change-and-deployment.md) · [`standards/observability.md`](standards/observability.md) | tiers by team size, per-tier coverage and DORA targets, vibecoding index, critical-path score routed to a role, ASVS 4 numbering, "Zero Skip", retry for flaky tests |
| `v6/02-Core-Methodology/Governance-Compliance/SDLC-Sprint-Governance.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | change approval board and lead times, impact × likelihood scoring, roadmap change requests by job title |
| `v6/05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-cso.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) | security roles and staffing by team size, fixed pen-test cadence, security coverage ≥90% |
| `v6/05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-devops.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | role prompts and message templates, fixed 5% canary |
| `v6/05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-itadmin.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | role prompts |
| `v6/05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-tester.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) | coverage targets |
| `v6/05-Templates-Tools/04-SASE-Artifacts/souls/SOUL-reviewer.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) · [`standards/testing.md`](standards/testing.md) | role prompt |
| `v6/05-Templates-Tools/04-SASE-Artifacts/02-MRP-Template.md` | RETIRED | — | merge-readiness package ritual; its "downgrade -1" migration rollback contradicts the migration rule in `controls/gates.md` |
| `v6/05-Templates-Tools/04-SASE-Artifacts/teams/TEAM-ops.md` | PARTIALLY_ADOPTED | [`standards/observability.md`](standards/observability.md) | team-card format |
| `v6/05-Templates-Tools/01-Specification-Standard/SPEC-0003-Policy-Guards-Design.md` | RETIRED | — | fail-open on a broken check (contradicts G2), secret policy exempting a PR with any test file (contradicts G3), policy-engine service |
| `v6/05-Templates-Tools/01-Specification-Standard/SPEC_DELTA.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | `sdlcctl delta` commands, spec-only versioning |
| `v6/05-Templates-Tools/05-Checklists/SDLC-Observability-Checklist.md` | PARTIALLY_ADOPTED | [`standards/observability.md`](standards/observability.md) | tiers by team size, named tools, cause-based pages (CPU, memory), four required dashboards, ML anomaly detection |
| `v6/05-Templates-Tools/05-Checklists/SDLC-Scope-Drift-Detection.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | blocking from day one (now a candidate rule on the ladder) |
| `v6/05-Templates-Tools/05-Checklists/Stage-Transition-Checklist.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) · [`standards/testing.md`](standards/testing.md) | kickoff meetings, sign-off by job title, coverage by tier |
| `v6/05-Templates-Tools/05-Checklists/SDLC-Testing-Artifacts-Structure.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) · [`standards/security.md`](standards/security.md) | numbered test folders, dated report files in git, monthly test changelog |
| `v6/07-Implementation-Guides/SDLC-Deployment-Guide.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) · [`standards/observability.md`](standards/observability.md) | deployment profiles and productivity claims, vendor quickstarts, one `/health` as liveness |
| `v6/07-Implementation-Guides/SDLC-Crisis-Response-Guide.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) · [`standards/observability.md`](standards/observability.md) | response SLAs and escalation by org level, "AI crisis team" of named tools, case stories and amounts |
| `v6/07-Implementation-Guides/SDLC-E2E-API-Testing-Methodology.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) · [`standards/security.md`](standards/security.md) | pass-rate thresholds (60–95%), CLI-specific generation |
| `v6/07-Implementation-Guides/E2E-TESTING-QUICKSTART.md` | RETIRED | — | CLI quickstart; pass-rate thresholds that disagree with the methodology |
| `v6/07-Implementation-Guides/SDLC-Code-Review-Guide.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) · [`standards/testing.md`](standards/testing.md) | "mocks only for external APIs", two approvers in the definition of done |
| `v6/07-Implementation-Guides/MCP-Integration-Guide.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) | protocol-specific setup |
| `v6/07-Implementation-Guides/ACE-AEE-Reference-Architecture.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) | platform architecture and its metrics |
| `v6/07-Implementation-Guides/MULTI-AGENT-PATTERNS.md` | PARTIALLY_ADOPTED | [`standards/observability.md`](standards/observability.md) | platform-specific patterns |
| `v6/07-Implementation-Guides/AUTONOMOUS-CODEGEN-PATTERNS.md` | PARTIALLY_ADOPTED | [`standards/observability.md`](standards/observability.md) · [`standards/security.md`](standards/security.md) | platform-specific patterns |
| `v6/08-Training-Materials/Module-03-Zero-Mock-Policy.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) | absolute ban on test doubles, keyword mock scanner, blocking from day one; kept: real code on the risk floor, no stand-ins in production, "temporary" doubles expire |
| `v6/08-Training-Materials/Module-04-Code-Quality.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) · [`standards/security.md`](standards/security.md) | coverage quotas per level, 2017-era OWASP Top 10, password composition rules |
| `v6/08-Training-Materials/Module-05-Development-Workflow.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | long-lived `develop` branch, mandatory staging, human approval on every merge |
| `v6/08-Training-Materials/Module-06-AI-Tools.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) | human review of every AI-written line |
| `v6/06-Case-Studies/SDLC-4.6-Mock-Contamination-Crisis-Case-Study.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) · [`standards/security.md`](standards/security.md) | headline numbers (inconsistently attributed), ROI claims, undefined scores; kept as a burn case |
| `v6/06-Case-Studies/SDLC-Orchestrator-V1-Case-Study.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) | kept only the skip-marker burn case |
| `v6/06-Case-Studies/BFLOW-PLATFORM-LESSONS-LEARNED.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) | kept only the shared seed-data lesson |
| `v6/03-AI-GOVERNANCE/04-Verification-Principle.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) | coverage figure |
| `v6/03-AI-GOVERNANCE/07-Anti-Patterns.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) · [`standards/security.md`](standards/security.md) | scanners mandatory from day one |
| `v6/03-AI-GOVERNANCE/13-AGENTIC-CORE-PRINCIPLES.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) · [`standards/observability.md`](standards/observability.md) | retry logic for flaky tests |
| `v6/03-AI-GOVERNANCE/16-LONG-RUNNING-AGENT-PROTOCOL.md` | PARTIALLY_ADOPTED | [`standards/observability.md`](standards/observability.md) | full tool-call content captured by default |
| `v6/03-AI-GOVERNANCE/06-Tool-Evaluation-Criteria.md` | PARTIALLY_ADOPTED | [`standards/observability.md`](standards/observability.md) | tool scoring |
| `v6/04-AI-TOOLS-LANDSCAPE/best-practices-2026/03-sub-agent-orchestration.md` | PARTIALLY_ADOPTED | [`standards/testing.md`](standards/testing.md) | tool-specific orchestration |
| `v6/04-AI-TOOLS-LANDSCAPE/best-practices-2026/04-git-workflow-patterns.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | branch-per-component naming, worktree speed figures, chat channel per feature |
| `v6/04-AI-TOOLS-LANDSCAPE/best-practices-2026/07-permissions-security.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) | tool-specific deny-rule syntax |
| `v6/02-Core-Methodology/SDLC-Crisis-To-Pattern-Methodology.md` | PARTIALLY_ADOPTED | [`standards/observability.md`](standards/observability.md) · [`practices/lessons-to-rules.md`](practices/lessons-to-rules.md) | promotion after two sprints, near-miss as a rule trigger, evidence vault |
| `by-version/v5.2.0/Governance-Compliance/SDLC-Change-Management-Standard.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | change approval board, change windows and freezes, per-tier retention |
| `by-version/v5.1.3/08-Team-Management/02-SDLC-Compliance/SDLC-Change-Management-Standard.md` | PARTIALLY_ADOPTED | [`standards/observability.md`](standards/observability.md) | rollback after a migration without a runbook, change approval board |
| `by-version/v4.3/09-Documentation-Standards/FRAMEWORK-CONTROLS-4.3.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | the rest of the 4.3 controls |
| `by-version/v4.4/02-Core-Methodology/specs/GOV-DRIFT-001-Drift-Diff-Spec.md` | PARTIALLY_ADOPTED | [`standards/change-and-deployment.md`](standards/change-and-deployment.md) | the rest of the drift spec |
| `by-topic/ai-tools-templates/testing_security-testing-checklist.md` | PARTIALLY_ADOPTED | [`standards/security.md`](standards/security.md) | prompt-template framing |

## Next to harvest

Done 2026-09-26: security, testing, change and deployment, observability (four standards, rows above). Next: systems thinking, design thinking, ship-useful (methodology, `core/`); then SSOT, integration and data, team collaboration and hand-over.
