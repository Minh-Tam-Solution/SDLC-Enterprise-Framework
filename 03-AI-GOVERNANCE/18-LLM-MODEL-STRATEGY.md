---
title: "LLM Model Strategy — 3-Tier Cascade Standard"
version: "6.3.1"
ring: 2
sdlc_version: "6.3.1"
last_updated: "2026-04-06"
status: "ACTIVE"
pillar: "NEW — LLM Model Strategy"
source: "SDLC Orchestrator v2 Sprint 10 + MTClaw Sprint 94 + CEO Federated AI OS directive"
---

# LLM Model Strategy — 3-Tier Cascade Standard

> NEW in Framework 6.3.0. Validated by SDLC Orchestrator v2 (Sprint 10, dogfooding confirmed) and MTClaw (Sprint 94).

## Standard

All SDLC platforms MUST implement a 3-tier LLM provider cascade:

```
Tier 1: Claude Code CLI (OAuth, Max subscription) — primary, best quality
Tier 2: OpenAI / Gemini API (API key, per-token) — backup
Tier 3: Ollama local (free, role-specific models) — last fallback
```

## Role-Specific Model Assignment

| SDLC Role | Primary | Fallback | Rationale |
|---|---|---|---|
| PM | Claude Code (Sonnet) | Ollama qwen3.5:9b | Coordination needs strong reasoning |
| Architect | Claude Code (Sonnet) | Ollama Opus-Distilled 27B | Complex design analysis |
| Coder | Claude Code (Sonnet) | Ollama qwen3-coder:30b | Code generation quality |
| Reviewer | Claude Code (Sonnet) | Ollama Opus-Distilled 27B | Deep code understanding |
| Tester | Claude Code (Sonnet) | Ollama qwen3-coder:30b | Test code quality |

## Model Registry Pattern

Every platform MUST have a Single Source of Truth (SSOT) for model configuration:

```python
# Example: model_registry.py
ROLE_DEFAULTS = {
    "pm":       {"provider": "claude_code", "model": "sonnet", "fallback_model": "qwen3.5:9b"},
    "architect": {"provider": "claude_code", "model": "sonnet", "fallback_model": "opus-distilled-27b"},
    ...
}
```

**Rules**:
- No hardcoded model names in business logic — always reference registry
- Timeouts from settings, not hardcoded
- Use real Ollama model names (no aliases)
- `validate_model_config()` at startup — warn if primary unavailable

## Cost Model

| Provider | Billing | Use When |
|---|---|---|
| Claude Code CLI | $200/month flat (Max subscription) | Primary — $0 marginal cost |
| OpenAI/Gemini | Per-token API key | Claude unavailable |
| Ollama | Free (local GPU) | All cloud APIs unavailable |

## Federated Alignment

All 3 SDLC platforms use the same cascade:
- **SDLC Orchestrator** (BRAIN): Gate evaluation agents
- **MTClaw** (VOICE): Team execution agents
- **EndiorBot** (ADVISOR): Personal AI assistant

Same roles → same models → same quality expectations across platforms.
