# Sub-agent Orchestration
## Session Management Patterns for AI Development

**Version:** 6.0.5
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

## Research Delegation Pattern

### Problem

Manual task splitting doesn't leverage AI parallelization. Developers spend hours researching sequentially when tasks could run concurrently.

**Sequential Research** (Manual):
```
1. Research auth patterns (2 hours)
2. Research security best practices (1 hour)
3. Research test patterns (1 hour)
Total: 4 hours
```

**Parallel Research** (Subagents):
```
Launch 3 subagents simultaneously:
1. Subagent 1: Auth patterns (30 minutes)
2. Subagent 2: Security guidelines (20 minutes)
3. Subagent 3: Test patterns (20 minutes)
Total: 30 minutes (longest subagent) = 8x faster
```

### Solution

Delegate research to specialized subagents during Planning Mode Phase 1 (EXPLORE).

### Research Task Types

| Task | Subagent | Use Case | Expected Output |
|------|----------|----------|-----------------|
| **Codebase exploration** | Explore | Find similar implementations | 3-5 code examples |
| **Dependency research** | Explore | Research packages, compatibility | Library recommendations |
| **Pattern extraction** | Explore | Extract coding patterns | Pattern summary |
| **External docs** | WebFetch | Review OWASP, RFCs, guidelines | Best practices list |
| **Architecture review** | Explore | Review ADRs, conventions | Architecture constraints |

### When to Delegate

✅ **Delegate when:**
- Isolated research tasks (read-only)
- 3+ independent subtasks
- Parallel execution possible
- Planning Mode Phase 1 (EXPLORE)

❌ **Don't delegate when:**
- Tightly coupled tasks (sequential dependencies)
- Shared context needed across tasks
- Blocking operations (one depends on another)
- Simple tasks (<15 LOC, 1 subtask)

### Example: User Authentication Research

**Main Agent Spawns 3 Parallel Subagents:**

```yaml
Subagent 1 (Explore):
  Task: Find existing auth patterns in codebase
  Tools: Grep, Read
  Search: "auth", "jwt", "token"
  Duration: 30 minutes
  Output: Found JWT pattern in 3 implementations

Subagent 2 (WebFetch):
  Task: OWASP authentication guidelines
  Tools: WebFetch
  URLs: owasp.org, auth0.com
  Duration: 20 minutes
  Output: bcrypt cost 12+, MFA, 15min JWT expiry

Subagent 3 (Explore):
  Task: Test patterns for authentication
  Tools: Grep, Read
  Search: "test_auth", "pytest", "fixture"
  Duration: 20 minutes
  Output: Use pytest fixtures + Redis mock
```

**Main Agent Synthesis:**
- Aggregates findings from 3 subagents
- Creates implementation plan
- Presents to human for approval

### Expected Impact

**Time Savings:**
- Sequential: 4 hours research + 1 hour synthesis = 5 hours
- Parallel: 30 minutes (longest subagent) + 1 hour = 1.5 hours
- **Result: 3.3x faster research phase**

**Quality Benefits:**
- More patterns discovered (parallel exploration)
- Better coverage (multiple perspectives)
- Evidence trail (all subagent work auditable)

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
