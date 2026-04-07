---
team: engineering
full_name: SDLC Engineering
lead: pm
mention: "@engineering"
sdlc_stage: "01-08"
sdlc_framework: "6.3.0"
version: 1.0.0
created: 2026-03-03
---

# TEAM Charter — SDLC Engineering

## Mission

Governance-first software delivery: requirements → design → implementation → review. Every feature follows the SDLC 6.3.0 lifecycle with gate approvals before progression.

## Coverage

- SDLC Stages 00-08 (Discovery through Deployment)
- Gates G0.1 through G4
- All 3 Rails: Spec Factory, PR Gate, Knowledge & Answering

## Members

- **pm** (lead): Requirements, specs, user stories, sprint planning, gate proposals
- **architect**: System design, ADRs, technical decisions, architecture reviews
- **coder**: Implementation, code quality, unit tests, PR submissions
- **reviewer**: Code review, quality assurance, PR Gate rule tuning
- **researcher**: User research, competitive analysis, evidence gathering
- **writer**: Documentation, technical writing, runbooks
- **pjm**: Sprint coordination, task tracking, velocity reporting
- **devops**: Deployment, infrastructure, CI/CD, Docker Compose
- **tester**: Test strategy, QA validation, pen testing
- **itadmin**: Infrastructure ops, server management, network configuration

## Delegation Rules

- Lead (pm) can delegate to any team member based on task domain
- Members delegate back to lead for cross-cutting decisions or scope questions
- Gate approvals escalate to Advisory Board (@advisory)
- Code implementation tasks route to @coder
- Architecture decisions route to @architect
- Infrastructure tasks route to @devops or @itadmin

## Interaction Patterns

- `@engineering design auth system` → PM receives with full team context, delegates to @architect
- `@engineering implement login flow` → PM receives, delegates to @coder with spec reference
- `@engineering review PR #42` → PM receives, delegates to @reviewer
