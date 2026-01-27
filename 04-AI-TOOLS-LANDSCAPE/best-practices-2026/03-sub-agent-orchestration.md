# Sub-agent Orchestration
## Session Management Patterns for AI Development

**Version:** 5.3.0
**Status:** ACTIVE
**Date:** January 27, 2026

---

## Overview

Sub-agents are isolated AI sessions that handle focused tasks without polluting the main conversation context. This guide covers when and how to use sub-agents effectively.

---

## When to Use Sub-agents

### ✅ Use Sub-agents For

| Use Case | Rationale |
|----------|-----------|
| **Complex, focused tasks** | Testing, code reviews, security scans |
| **Tool restrictions needed** | Read-only analysis, specific permissions |
| **Context isolation** | Research without polluting main session |
| **Concurrent execution** | Multiple checks in parallel |
| **Exploration** | Pattern extraction before implementation |

### ❌ Avoid Sub-agents For

| Use Case | Why Not |
|----------|---------|
| **Simple operations** | Overhead not worth it |
| **Main conversation flow** | Keep in primary session |
| **Nested delegation** | Not supported, creates confusion |
| **Parallel editing same files** | Coordination issues |

---

## Sub-agent Types

### Explore Sub-agents

**Purpose:** Pattern extraction, codebase research, context gathering

```yaml
Context: Fork (isolated)
Tools: Read, Grep, Glob
Duration: Short-lived
Output: Findings report
```

**Use for Planning Mode Phase 1:**
- Similar code search
- Architecture exploration
- Test pattern discovery

### Specialist Sub-agents

**Purpose:** Focused expertise on specific tasks

```yaml
Context: Fork (isolated)
Tools: Task-specific (Bash for testing, etc.)
Duration: Task completion
Output: Task results + evidence
```

**Examples:**
- Test Runner: Execute and fix tests
- Security Scanner: Vulnerability analysis
- Code Reviewer: PR review automation

### Proactive Sub-agents

**Purpose:** Auto-triggered on specific events

```yaml
Context: Fork (isolated)
Trigger: Code changes, file saves, commits
Tools: Task-specific
Duration: Event completion
```

**Examples:**
- Auto-test after code changes
- Auto-lint before commits
- Auto-doc for new functions

---

## Session Management

### Main Session Hygiene

Keep the main session clean:
- Use sub-agents for research
- Bring back only findings, not raw exploration
- Update CLAUDE.md with learned patterns

### Sub-agent Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    SUB-AGENT LIFECYCLE                           │
└─────────────────────────────────────────────────────────────────┘

1. SPAWN
   └──→ Create isolated fork session
        - Define purpose and tools
        - Set up permissions
        - Establish timeout

2. EXECUTE
   └──→ Sub-agent works on focused task
        - Isolated from main context
        - Uses only allowed tools
        - Tracks progress

3. RETURN
   └──→ Report findings to main session
        - Synthesized results
        - Relevant patterns
        - Recommended actions

4. CLEANUP
   └──→ Archive or terminate
        - Move learnings to CLAUDE.md
        - Clear temporary state
        - Release resources
```

### Resume vs New Instance

```bash
# New instance (default) - fresh context
"Run tests with test-runner"

# Resume existing - keeps previous context
"Continue the previous test-runner work"
"Resume the code review subagent"
```

**When to Resume:**
- Multi-step tasks
- Iterative refinement
- Building on previous findings

**When to Start Fresh:**
- Independent tasks
- Clean slate needed
- Different context required

---

## Parallel Execution

### Safe Parallelism

✅ **Safe to parallelize:**
- Read-only operations
- Independent file sets
- Different task types

❌ **Avoid parallel:**
- Same file editing
- Dependent operations
- Shared state modifications

### Coordination Pattern

```
┌───────────────────────────────────────────────────────────────┐
│                    PARALLEL SUB-AGENTS                         │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  MAIN SESSION                                                 │
│       │                                                       │
│       ├──→ Spawn: Code Explorer (read-only)                   │
│       │         └──→ Find similar implementations             │
│       │                                                       │
│       ├──→ Spawn: Test Explorer (read-only)                   │
│       │         └──→ Find test patterns                       │
│       │                                                       │
│       ├──→ Spawn: Doc Explorer (read-only)                    │
│       │         └──→ Find architecture constraints            │
│       │                                                       │
│       └──→ Wait for all to complete                           │
│                 │                                             │
│                 ▼                                             │
│           SYNTHESIZE FINDINGS                                 │
│                 │                                             │
│                 ▼                                             │
│           CONTINUE IN MAIN SESSION                            │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## Creating Sub-agents

### Via CLI

```bash
# Interactive creation
/agents → Create new → Generate with Claude

# Manual creation
mkdir -p .claude/agents
```

### Agent Definition Template

```markdown
# .claude/agents/test-runner.md
---
name: test-runner
description: Use PROACTIVELY to run tests and fix failures
tools: Bash, Read, Write
model: sonnet
---

You are a test automation expert.

## Responsibilities
- Run test suites after code changes
- Analyze failures and fix issues
- Preserve test intent while fixing

## Workflow
1. Run tests: `pytest -v`
2. If failures, analyze error output
3. Fix issues while preserving test intent
4. Re-run to verify fix

## Constraints
- Never skip tests
- Never weaken assertions
- Always report results
```

### Proactive Triggering

Add keywords to trigger automatic usage:

```markdown
# Keywords that trigger auto-use
description: Use PROACTIVELY for code quality checks
description: MUST BE USED after database changes
description: ALWAYS invoke for security reviews
```

---

## Best Practices

### ✅ DO

1. **Isolate exploration** - Use sub-agents for research
2. **Clean main context** - Don't pollute with exploration noise
3. **Define clear scope** - Each sub-agent has one job
4. **Set timeouts** - Prevent runaway sub-agents
5. **Document findings** - Update CLAUDE.md with patterns

### ❌ DON'T

1. **Edit same files** - Coordination nightmare
2. **Nest sub-agents** - Not supported
3. **Share mutable state** - Leads to conflicts
4. **Forget cleanup** - Archive completed sub-agents
5. **Skip synthesis** - Raw findings aren't actionable

---

## Hooks Integration

### Pre-execution Validation

```yaml
# Validate before sub-agent runs
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly.sh"
```

### Post-execution Logging

```yaml
# Log sub-agent activity
hooks:
  PostToolUse:
    - matcher: "Edit|Write"
      hooks:
        - type: command
          command: "echo '$file_path' >> .claude/agent-edits.log"
```

---

## Example: Security Scanner Sub-agent

```markdown
# .claude/agents/security-scanner.md
---
name: security-scanner
description: MUST BE USED proactively for security reviews
tools: Bash, Read, Grep
model: opus
---

You are a security specialist.

## Scan Targets
- SQL injection risks
- XSS vulnerabilities
- Authentication bypasses
- Secrets in code
- Dependency vulnerabilities

## Report Format
1. Severity: Critical/High/Medium/Low
2. Location: file:line
3. Description: What's the issue
4. Recommended fix: How to address

## Workflow
1. Grep for common vulnerability patterns
2. Check dependency versions
3. Review authentication code
4. Scan for hardcoded secrets
5. Generate report
```

---

## Integration with Planning Mode

| Planning Phase | Sub-agent Usage |
|----------------|-----------------|
| Pattern Extraction | Parallel explore sub-agents |
| Synthesis | Main session (needs all context) |
| Approval | Main session (human interaction) |
| Execution | Main session or specialist sub-agent |
| Validation | Test-runner sub-agent |

---

**Document Status:** ACTIVE
**Last Updated:** January 22, 2026
