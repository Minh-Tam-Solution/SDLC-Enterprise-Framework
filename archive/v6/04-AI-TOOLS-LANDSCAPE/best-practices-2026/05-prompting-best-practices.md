# Prompting Best Practices
## Effective Communication with AI Coding Agents

**Version:** 6.3.1
**Status:** ACTIVE
**Date:** January 27, 2026

---

## Core Principles

### 1. Be Specific and Actionable

```bash
# ✅ GOOD - Specific, actionable, with context
"Implement OAuth2 authentication for our API.
Use the auth patterns from @src/auth/legacy.js"

# ❌ BAD - Vague, no context
"Can you suggest some changes to improve security?"
```

### 2. Use Explicit Actions

```bash
# ✅ GOOD - Direct command
"Change the return type to Promise<User>"
"Add error handling for network failures"
"Refactor to use dependency injection"

# ❌ BAD - Suggestion requests
"Can you suggest improvements?"
"What do you think about...?"
"Could you help with...?"
```

### 3. Provide Context with @

```bash
# Reference specific files
@src/utils/auth.js          # Include file content
@package.json               # For npm commands
@docs/architecture.md       # For design context

# Reference resources
@server:resource            # MCP resource
@github:repos/owner/repo    # GitHub context
@terminal:name              # Terminal output
```

### 4. Treat AI as Pair Programmer

- Talk naturally, not like to a robot
- Explain the "why" not just the "what"
- Share constraints and context
- Discuss tradeoffs

---

## Extended Thinking

### Activation

```bash
# Toggle in session
Tab  # On/Off extended thinking

# Trigger phrases
"Think deeply about the best approach..."
"Keep hard, think more, think longer"
"Consider all options carefully..."
```

### When to Use

**✅ Use Extended Thinking for:**
- Architectural decisions
- Complex bugs
- Tradeoff evaluation
- Multi-step implementations
- Security-critical code

**❌ Skip Extended Thinking for:**
- Simple CRUD operations
- Standard implementations
- Quick fixes
- Code formatting

---

## Context Management

### Chat History Awareness

**Don't rely on chat history:**
```bash
# ❌ BAD - Assumes context
"Now fix the other issue"
"Apply the same pattern here"

# ✅ GOOD - Explicit context
"Fix the authentication timeout issue in auth_service.py"
"Apply the error handling pattern from user_service.py to order_service.py"
```

### System Prompt for Long Sessions

```bash
# Add to CLAUDE.md for sessions with auto-compaction
"Your context window will be automatically compacted
as it approaches its limit, allowing you to continue
working indefinitely. Do not stop tasks early due
to token budget concerns."
```

### Request Summaries

```bash
# Claude 4.5 tends toward efficiency - may skip summaries
# If you want visibility:
"After completing tasks involving tool use,
provide a quick summary of the work you've done."
```

---

## Task Structure

### Single Task

```markdown
**Task:** [Clear description]
**Context:** [Relevant files, constraints]
**Expected:** [What success looks like]
```

### Multi-Step Task

```markdown
**Goal:** [High-level objective]

**Steps:**
1. [First step with specifics]
2. [Second step with specifics]
3. [Validation step]

**Constraints:**
- [Constraint 1]
- [Constraint 2]
```

### Debugging Task

```markdown
**Bug:** [Description of the issue]
**Reproduction:** [Steps to reproduce]
**Expected:** [What should happen]
**Actual:** [What actually happens]
**Files:** @path/to/relevant/file.py
```

---

## Memory (CLAUDE.md) Best Practices

### Structure for Clarity

```markdown
<!-- ✅ GOOD - Specific, structured -->
# Code Style
- Use 2-space indentation
- Prefer const over let
- Always use TypeScript strict mode

# Testing Requirements
- Unit tests required for all business logic
- Integration tests for API endpoints
- Coverage threshold: 80%

<!-- ❌ BAD - Vague -->
# General Rules
- Write good code
- Test properly
- Follow best practices
```

### Organization Tips

1. **Use bullet points** over paragraphs
2. **Group related instructions** under headers
3. **Be specific** over general
4. **Use .claude/rules/** for large codebases

### Quick Memory Commands

```bash
/memory          # View loaded memories
#<text>          # Quick add via shortcut
/memory edit     # Direct edit interface
```

---

## Common Patterns

### Feature Implementation

```markdown
Implement [feature name] for [component].

Requirements:
- [Functional requirement 1]
- [Functional requirement 2]

Constraints:
- Follow patterns from @similar/file.py
- Use async/await for I/O
- Add unit tests

Files to modify:
- @path/to/main/file.py
- @path/to/test/file.py
```

### Bug Fix

```markdown
Fix [bug description] in @path/to/file.py

Issue: [What's wrong]
Cause: [Root cause if known]
Solution approach: [Suggested fix]

Verify by: [How to test the fix]
```

### Refactoring

```markdown
Refactor [component] to [new pattern].

Current: [Current state description]
Target: [Desired state description]

Constraints:
- Maintain backward compatibility
- No behavior changes
- Add deprecation warnings if needed

Test: Run existing tests to verify no regression
```

### Code Review

```markdown
Review changes in @path/to/file.py

Focus on:
- [Specific concern 1]
- [Specific concern 2]

Check for:
- Security issues
- Performance implications
- Pattern consistency
```

---

## Anti-patterns

### ❌ Vague Prompts

```bash
# Bad
"Can you help with this?"
"Make it better"
"Fix the bug"

# Good
"Refactor UserService to use dependency injection"
"Improve the response time of getUserById by adding caching"
"Fix the null pointer exception in line 42 of order_service.py"
```

### ❌ No Context

```bash
# Bad
"Add error handling"

# Good
"Add error handling for network failures in api_client.py,
following the pattern used in auth_client.py @src/auth/auth_client.py"
```

### ❌ Ambiguous Scope

```bash
# Bad
"Update the authentication"

# Good
"Add JWT token refresh logic to auth_service.py.
When access token expires, use refresh token to get new access token.
Return 401 if refresh token is also expired."
```

---

## Integration with SDLC Orchestrator

### Gate-Aware Prompting

Reference current gate status in prompts:

```markdown
We're in BUILD stage (G2 passed).
Focus on implementation, not design changes.
All code needs unit tests per our G3 requirements.
```

### Evidence-Aware Prompting

Request evidence creation:

```markdown
After implementing, create evidence for:
- Test results
- Code coverage
- Security scan results
```

---

**Document Status:** ACTIVE
**Last Updated:** January 22, 2026
