# Developer Role Evolution
## Software Engineering 3.0 Responsibilities

**Version:** 6.0.5
**Status:** ACTIVE
**Date:** January 27, 2026

---

## Overview

In Software Engineering 3.0, the developer role shifts from writing code to designing feedback loops and guiding AI agents. This guide outlines the evolved responsibilities.

---

## The Shift

### SE 2.0 (2010s-2020s)
Developer writes code with tool assistance.

### SE 3.0 (2020s+)
Developer designs feedback loops, AI writes code.

> "Developer role = Design feedback loops, NOT write code"

---

## 2026 Developer Responsibilities

### 1. Design Feedback Loops

**What it means:**
- Define quality criteria for AI output
- Set up validation pipelines
- Create checkpoints for human review
- Establish pattern libraries for AI reference

**Instead of:** Writing the code yourself

**You now:** Define what good looks like, let AI generate, validate output

### 2. Monitor AI Output Quality

**Activities:**
- Review AI-generated code for patterns
- Identify recurring mistakes
- Track quality metrics over time
- Adjust context when quality drops

**Tools:**
- Code review workflows
- Automated test suites
- Quality dashboards
- Pattern violation alerts

### 3. Extract Patterns and Update Context

**Workflow:**
```
1. Review AI output
2. Identify good patterns → Add to CLAUDE.md
3. Identify bad patterns → Add to "Don't do" section
4. Test pattern adherence → Refine as needed
```

**Example:**
```markdown
# Learned Patterns (from code reviews)

## Error Handling
✅ DO: Use specific exception types
❌ DON'T: Catch bare Exception

## API Design
✅ DO: Return consistent response schema
❌ DON'T: Mix response formats
```

### 4. Make Architecture Decisions

**Still human responsibility:**
- System design choices
- Technology selection
- Trade-off decisions
- Security architecture
- Performance strategy

**AI assists with:**
- Generating options
- Documenting decisions
- Implementing choices
- Validating alignment

### 5. Maintain Context Files

**Responsibilities:**
- Keep CLAUDE.md current
- Update after project changes
- Add learned patterns
- Remove outdated info
- Organize for clarity

**Cadence:**
- Review weekly
- Update after major features
- Clean up quarterly

### 6. Configure Tools and Skills

**Set up:**
- Sub-agents for common tasks
- Skills for workflows
- Hooks for automation
- MCP servers for integrations

**Example skill setup:**
```markdown
# .claude/agents/test-runner.md
---
name: test-runner
description: PROACTIVELY run tests after code changes
tools: Bash, Read, Write
---
Run pytest, analyze failures, suggest fixes.
```

---

## Daily Workflow

### Morning
1. Review overnight AI work (PRs, commits)
2. Update context if needed
3. Prioritize tasks for AI sessions

### During Development
1. Define task clearly
2. Use Planning Mode for >15 LOC
3. Review AI output
4. Provide feedback
5. Update patterns

### End of Day
1. Review completed work
2. Document learnings
3. Update CLAUDE.md
4. Queue overnight tasks

---

## Feedback Loop Design

### For Code Generation

```
┌─────────────────────────────────────────────────────────────────┐
│                    CODE GENERATION LOOP                          │
└─────────────────────────────────────────────────────────────────┘

1. DEFINE
   └──→ Clear task description
        - Specific requirements
        - Reference files
        - Constraints

2. GENERATE
   └──→ AI creates code
        - Uses context from CLAUDE.md
        - Follows patterns
        - Generates tests

3. VALIDATE
   └──→ Automated checks
        - Tests pass?
        - Linting clean?
        - Security scan pass?

4. REVIEW
   └──→ Human inspection
        - Pattern adherence?
        - Edge cases covered?
        - Maintainable?

5. FEEDBACK
   └──→ Update context
        - Good patterns → Add to CLAUDE.md
        - Bad patterns → Add to "Don't do"
        - Refine prompts
```

### For Code Review

```
1. AI generates code
2. AI creates self-review
3. Human reviews AI review
4. Human spots what AI missed
5. Learnings → Context update
```

---

## Pattern Extraction Process

### From PR Reviews

```yaml
Review Comment Analysis:
  1. Categorize comments
     - Pattern violation
     - Missing requirement
     - Edge case
     - Performance issue

  2. Track recurring issues
     - Same mistake > 2 times = pattern gap

  3. Update context
     - Add example to CLAUDE.md
     - Add to "Common Mistakes" section

  4. Verify fix
     - Future PRs should not have same issue
```

### From Production Issues

```yaml
Incident Analysis:
  1. Root cause identification
  2. Could AI have prevented?
  3. What context was missing?
  4. Update CLAUDE.md with guard

Example:
  Issue: SQL injection in user input
  Update: Add to security rules:
    "Always use parameterized queries.
     Never concatenate user input into SQL."
```

---

## Metrics to Track

### AI Productivity

| Metric | Target | Action if Below |
|--------|--------|-----------------|
| First-pass acceptance | >80% | Improve context |
| Rework cycles | <2 per task | Better prompts |
| Time to completion | Decreasing | Optimize workflow |

### Quality

| Metric | Target | Action if Below |
|--------|--------|-----------------|
| Test coverage | >90% | Add test patterns |
| Bug rate | Decreasing | Add constraints |
| Pattern adherence | >95% | Update examples |

### Developer Efficiency

| Metric | Healthy Sign |
|--------|--------------|
| Context updates/week | 1-3 (active learning) |
| Time reviewing vs writing | 70/30 (mostly review) |
| AI tasks/day | Increasing |

---

## Anti-patterns

### ❌ Still Writing All Code

**Problem:** Not leveraging AI capabilities
**Fix:** Start with simple tasks, build trust

### ❌ Accepting AI Output Without Review

**Problem:** Quality degradation
**Fix:** Always validate, even briefly

### ❌ Not Updating Context

**Problem:** Same mistakes repeat
**Fix:** Schedule weekly context review

### ❌ Over-Engineering Prompts

**Problem:** Diminishing returns
**Fix:** Simple, clear prompts work best

### ❌ Ignoring AI Suggestions

**Problem:** Missing good ideas
**Fix:** Evaluate suggestions fairly

---

## Integration with SDLC 5.2.0

### Sprint Governance (Pillar 2)

Developer responsibilities in sprints:
- Define sprint goals clearly for AI
- Update context for sprint constraints
- Monitor AI work against sprint scope
- Review AI output for gate compliance

### Gate Awareness

At each gate:
- Update CLAUDE.md with stage context
- Adjust AI permissions for stage
- Review AI work for gate requirements

---

**Document Status:** ACTIVE
**Last Updated:** January 22, 2026
