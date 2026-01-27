# Model Selection Matrix
## Task-Appropriate Model Routing for AI Agents

**Version:** 5.3.0
**Status:** ACTIVE
**Date:** January 27, 2026

---

## Overview

Different AI tasks require different model capabilities. This guide provides a framework for selecting the right model for each task type, optimizing for quality, speed, and cost.

---

## Key Principle

> "Switch models when stuck - different model = different perspective"

Each model has unique training data and reasoning patterns. When one model is stuck, switching to another often provides fresh insights.

---

## Model Selection Matrix

### By Task Type

| Task Type | Model Class | Characteristics | Use When |
|-----------|-------------|-----------------|----------|
| **Large Features** (>50 LOC, multi-file) | Premium Reasoning | Best at complex reasoning, multi-file refactoring | New features, major refactors |
| **Small Fixes** (<15 LOC, single file) | Fast Balanced | Quick, accurate for targeted changes | Bug fixes, minor updates |
| **Architecture & Debugging** | Alternative Provider | Different perspective helps when stuck | Complex bugs, design decisions |
| **Design & Creativity** | Large Context | Creative solutions, synthesis | PRDs, design docs, brainstorming |
| **Quick Answers & Micro-edits** | Fast Compact | Fastest response time | Code lookup, simple questions |

### By Context Requirements

| Context Size | Recommended Model | Rationale |
|--------------|-------------------|-----------|
| Small (<10K tokens) | Fast compact | Minimize cost, maximize speed |
| Medium (10-50K) | Fast balanced | Good balance of speed and capability |
| Large (50-100K) | Large context | Full codebase awareness |
| Very Large (>100K) | Premium with large context | Complex reasoning over large scope |

### By Accuracy Requirements

| Accuracy Need | Recommended Model | Use Case |
|---------------|-------------------|----------|
| Critical | Premium reasoning | Security code, financial logic |
| High | Fast balanced | Production code, tests |
| Medium | Fast balanced or compact | Drafts, exploration |
| Low | Fast compact | Prototypes, experiments |

---

## Model Categories

### Premium Reasoning Models

**Characteristics:**
- Best at complex, multi-step reasoning
- Excellent at multi-file refactoring
- Strong architectural understanding
- Higher cost, slower response

**Use for:**
- Planning Mode synthesis
- Architecture decisions
- Complex bug debugging
- Code review with deep analysis
- Multi-file refactoring

**Examples:** Claude Opus, GPT-4, Gemini Ultra

### Fast Balanced Models

**Characteristics:**
- Good balance of speed and quality
- Accurate for targeted changes
- Reasonable cost
- Fast response time

**Use for:**
- Daily coding tasks
- Single-file changes
- Test writing
- Documentation updates
- Standard implementations

**Examples:** Claude Sonnet, GPT-4o, Gemini Pro

### Fast Compact Models

**Characteristics:**
- Fastest response time
- Lowest cost
- Good for simple tasks
- Limited complex reasoning

**Use for:**
- Quick lookups
- Simple edits
- Syntax fixes
- Code formatting
- Quick answers

**Examples:** Claude Haiku, GPT-4o-mini, Gemini Flash

### Large Context Models

**Characteristics:**
- Can process very large codebases
- Good at synthesis across files
- Strong at documentation
- Moderate speed

**Use for:**
- Codebase analysis
- PRD/design doc creation
- Cross-file understanding
- Documentation generation

**Examples:** Gemini 1.5 Pro (1M context), Claude with extended context

---

## Decision Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    MODEL SELECTION FLOW                          │
└─────────────────────────────────────────────────────────────────┘

START: What's the task?
         │
         ├──→ Complex reasoning needed?
         │         │
         │         ├──→ YES: Use PREMIUM REASONING
         │         │         (Opus, GPT-4)
         │         │
         │         └──→ NO: Continue ↓
         │
         ├──→ Large codebase context needed?
         │         │
         │         ├──→ YES: Use LARGE CONTEXT
         │         │         (Gemini 1.5 Pro)
         │         │
         │         └──→ NO: Continue ↓
         │
         ├──→ Speed critical?
         │         │
         │         ├──→ YES: Use FAST COMPACT
         │         │         (Haiku, GPT-4o-mini)
         │         │
         │         └──→ NO: Continue ↓
         │
         └──→ Default: Use FAST BALANCED
                       (Sonnet, GPT-4o)

STUCK? Switch to ALTERNATIVE PROVIDER
        (Different training = Different perspective)
```

---

## Extended Thinking

### When to Enable

**Use Extended Thinking for:**
- Architectural decisions
- Complex bugs
- Tradeoff evaluation
- Multi-step implementations

**Skip Extended Thinking for:**
- Simple CRUD operations
- Standard implementations
- Quick fixes
- Code formatting

### Trigger Phrases

```bash
# Enable extended thinking
"Think deeply about the best approach..."
"Keep hard, think more, think longer"
"Consider all options carefully..."
```

---

## Cost Optimization

### Strategy

1. **Default to Fast Balanced** for most tasks
2. **Upgrade to Premium** only when stuck or for critical tasks
3. **Use Fast Compact** for simple operations
4. **Batch similar tasks** to reuse context

### Cost-Quality Matrix

| Model Type | Quality | Speed | Cost | When to Use |
|------------|---------|-------|------|-------------|
| Premium | 95% | Slow | $$$ | Critical, complex |
| Balanced | 85% | Medium | $$ | Daily work |
| Compact | 70% | Fast | $ | Simple tasks |

---

## Multi-Provider Strategy

### Primary Provider

Choose based on:
- API reliability
- Cost structure
- Feature availability
- Team familiarity

### Fallback Strategy

```yaml
Provider Chain:
  1. Primary: Local/Self-hosted (lowest cost)
  2. Fallback 1: Claude (high quality)
  3. Fallback 2: GPT-4 (different perspective)
  4. Fallback 3: Rule-based (deterministic)
```

### When to Switch Providers

- Rate limited on primary
- Primary returning poor results
- Need different perspective on stuck problem
- Specific capability needed (e.g., vision, code execution)

---

## Per-Session Configuration

### CLI Example

```bash
# Start with specific model
claude --model opus        # Complex reasoning
claude --model sonnet      # Balanced (default)
claude --model haiku       # Fast, simple tasks

# Switch during session
/model opus
Tab  # Toggle extended thinking
```

### Project Configuration

```json
{
  "model": {
    "default": "sonnet",
    "planning": "opus",
    "quick": "haiku"
  }
}
```

---

## Best Practices

### ✅ DO

1. **Match model to task** - Don't use premium for simple tasks
2. **Switch when stuck** - Different model = different perspective
3. **Use extended thinking strategically** - Not for everything
4. **Monitor costs** - Track usage by model type
5. **Document model choices** - In ADRs for critical decisions

### ❌ DON'T

1. **Always use premium** - Overkill for simple tasks
2. **Always use compact** - Misses quality on complex tasks
3. **Ignore model context limits** - Check before loading large codebases
4. **Stay stuck on one provider** - Switch for fresh perspective

---

## Integration with Planning Mode

| Planning Phase | Recommended Model | Rationale |
|----------------|-------------------|-----------|
| Pattern Extraction | Fast Balanced | Quick parallel searches |
| Synthesis | Premium Reasoning | Complex pattern merging |
| Human Presentation | Fast Balanced | Clear communication |
| Code Generation | Premium Reasoning | Quality implementation |
| Validation | Fast Balanced | Quick verification |

---

**Document Status:** ACTIVE
**Last Updated:** January 22, 2026
