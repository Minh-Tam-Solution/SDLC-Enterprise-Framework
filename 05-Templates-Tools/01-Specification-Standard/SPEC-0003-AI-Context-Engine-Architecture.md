# SPEC-0003: AI Context Engine Architecture

## Frontmatter

```yaml
spec_id: SPEC-0003
title: AI Context Engine Architecture (ADR-007)
version: 1.0.0
status: approved
tier: ALL
pillar: Pillar 4 - Build & Implementation
owner: Backend Team
last_updated: 2026-01-28
tags:
  - ai-context-engine
  - ollama
  - multi-provider
  - cost-optimization
  - adr-007
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
  - SPEC-0006  # Multi-Provider Codegen
epic: EP-02 AI Context Engine
sprint: Sprint 20-25 (Nov-Dec 2025)
```

---

## 1. Overview

The AI Context Engine provides intelligent AI capabilities for SDLC Orchestrator through a **Hybrid AI Architecture** with internal Ollama primary and cloud provider fallbacks. This ADR documents the architectural decision for multi-provider AI integration with cost optimization, data privacy, and reliability.

**Problem Statement**: SDLC Orchestrator requires AI for gate recommendations, policy generation, evidence analysis, intelligent search, and automated suggestions. Need cost-effective, private, and reliable AI architecture.

**Decision**: Hybrid architecture with Ollama (api.nhatquangholding.com) as primary provider, Claude/GPT-4/Gemini as fallbacks, unified AI Gateway with provider abstraction, and stage-aware context management.

**Key Benefits**:
- **80% cost reduction** ($50/month vs $1000/month cloud-only)
- **Data privacy** for sensitive evidence and code
- **99.9% availability** through multi-provider fallback
- **Stage-aware prompting** with evidence inclusion

---

## 2. Context

### 2.1 Problem Statement

SDLC Orchestrator requires AI capabilities for:

1. **Gate recommendations** based on team size and project type
2. **Policy generation** from natural language requirements
3. **Evidence analysis** for compliance verification
4. **Intelligent search** across documentation and evidence
5. **Automated suggestions** for gate approvals

### 2.2 Available Infrastructure

**Internal Resources**:
- Ollama at `https://api.nhatquangholding.com/`
- Model: qwen2.5:14b with 96.4% Vietnamese accuracy
- AI-Platform heritage from BFlow/NQH-Bot/MTEP (86% test coverage, Zero Mock Policy)

**Cloud Providers**:
- OpenAI GPT-4 ($0.03/$0.06 per 1K tokens)
- Anthropic Claude 3 Opus ($0.015/$0.075 per 1K tokens)
- Google Gemini (future)

### 2.3 Constraints

- **Budget**: $1000/month AI budget target
- **Privacy**: Sensitive data (PII, code, evidence) must stay on-premise
- **Performance**: <3s p95 response time
- **Compliance**: GDPR, SOC 2, ISO 27001

---

## 3. Requirements

### 3.1 Functional Requirements

#### FR-001: Multi-Provider AI Gateway
**Priority**: P0
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN multiple AI providers (Ollama, Claude, GPT-4)
  AND each provider has different capabilities and costs
WHEN a user requests AI processing
THEN the gateway routes to optimal provider
  AND falls back to next provider if primary fails
  AND logs metrics for cost tracking
```

**Rationale**: No single provider guarantees 100% uptime. Multi-provider ensures reliability.
**Verification**: Integration test with provider failure simulation.

#### FR-002: Ollama Primary Provider
**Priority**: P0
**Tier**: ALL

```gherkin
GIVEN Ollama is available at api.nhatquangholding.com
  AND model is qwen2.5:14b
WHEN 80% of AI requests are processed
THEN Ollama handles them successfully
  AND average cost is <$0.001 per 1K tokens
  AND response time is 2-6 seconds
```

**Rationale**: Cost optimization (80% cost reduction) and data privacy.
**Verification**: Load test with 1000 requests, measure cost and latency.

#### FR-003: Cloud Provider Fallback
**Priority**: P0
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN Ollama provider fails or times out
  AND cloud providers (Claude, GPT-4) are configured
WHEN AI gateway detects failure
THEN request automatically falls back to Claude
  AND if Claude fails, falls back to GPT-4
  AND final result is returned within 10 seconds total
```

**Rationale**: Ensure 99.9% availability through redundancy.
**Verification**: Integration test with Ollama mock failure.

#### FR-004: Stage-Aware Context Management
**Priority**: P0
**Tier**: PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN a project is in specific SDLC stage (00-09)
  AND stage has specific evidence requirements
WHEN AI processes a request
THEN prompt includes stage-specific context
  AND relevant evidence summaries are included
  AND response addresses stage-specific concerns
```

**Rationale**: AI guidance must be contextually relevant to current project stage.
**Verification**: Unit test with 10 stage scenarios, verify prompt structure.

#### FR-005: Response Caching
**Priority**: P1
**Tier**: ALL

```gherkin
GIVEN a user submits an AI request
  AND identical request was made within 1 hour
WHEN cache lookup succeeds
THEN cached response is returned
  AND response time is <100ms
  AND no AI provider is called
```

**Rationale**: Reduce costs and improve latency for repeated queries.
**Verification**: Integration test with duplicate requests, measure cache hit rate.

#### FR-006: PII Detection and Redaction
**Priority**: P0
**Tier**: ALL

```gherkin
GIVEN user input contains sensitive data (API keys, passwords, PII)
  AND cloud provider is selected (not Ollama)
WHEN input is sanitized before sending to provider
THEN all PII is redacted with [REDACTED]
  AND credentials are removed
  AND internal URLs are replaced with [INTERNAL_URL]
```

**Rationale**: Comply with GDPR and protect sensitive data.
**Verification**: Unit test with 50 PII patterns, verify 100% detection.

#### FR-007: Cost Tracking and Budget Controls
**Priority**: P1
**Tier**: PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN monthly AI budget is $1000
  AND current usage is tracked per provider
WHEN new request would exceed budget
THEN request is routed to cheaper provider (Ollama)
  AND if Ollama unavailable, BudgetExceededException is raised
  AND admin is notified of budget exhaustion
```

**Rationale**: Prevent unexpected AI costs.
**Verification**: Unit test with budget scenarios, verify exception handling.

### 3.2 Non-Functional Requirements

#### NFR-001: Performance
**Tier**: ALL

- **Response Time**: <3s p95 for AI requests
- **Cache Hit Rate**: >60% for repeated queries
- **Throughput**: >100 requests/minute

**Verification**: Load test with Locust (100 concurrent users).

#### NFR-002: Availability
**Tier**: ALL

- **Uptime**: >99.9% (multi-provider fallback)
- **Failover Time**: <2s between providers
- **Recovery**: Automatic with exponential backoff

**Verification**: Chaos engineering test with provider failures.

#### NFR-003: Cost Efficiency
**Tier**: ALL

- **Average Cost**: <$0.01 per request
- **Ollama Usage**: >80% of requests
- **Monthly Budget**: <$1000

**Verification**: Monitor production usage for 30 days.

#### NFR-004: Security
**Tier**: ALL

- **PII Redaction**: 100% detection rate for known patterns
- **Output Validation**: Check for code injection, bias
- **Audit Logging**: All AI requests logged with input/output

**Verification**: Security scan with Semgrep, manual penetration test.

---

## 4. Design Decisions

### 4.1 Hybrid Architecture (Primary Decision)

**Options Considered**:

| Option | Cost/Month | Privacy | Availability | Decision |
|--------|-----------|---------|--------------|----------|
| **Hybrid (Ollama + Cloud)** | **$50-200** | **On-premise** | **99.9%** | ✅ **CHOSEN** |
| Cloud-Only (OpenAI/Claude) | $1000+ | External | 99.5% | ❌ Too expensive |
| Ollama-Only | $50 | On-premise | 95% | ❌ Single point of failure |
| Build Custom Model | $5000+ | On-premise | TBD | ❌ 6-12 months effort |
| No AI Features | $0 | N/A | N/A | ❌ Competitive disadvantage |

**Decision Rationale**:
- **Cost**: 80% reduction vs cloud-only ($50 vs $1000/month)
- **Privacy**: Sensitive data stays on-premise with Ollama
- **Reliability**: Multi-provider fallback ensures 99.9% uptime
- **Flexibility**: Easy to add/remove providers

**Consequences**:
- ✅ **Positive**: Cost savings, data privacy, reliability
- ❌ **Negative**: Operational complexity, latency variance (Ollama 2-6s vs Cloud 1-3s)

### 4.2 Provider Routing Strategy

**Routing Logic**:
```
1. Cache Check (if enabled) → <100ms
2. Ollama (primary) → 2-6s
3. Claude (fallback 1) → 1-3s
4. GPT-4 (fallback 2) → 1-3s
5. Gemini (fallback 3) → TBD (future)
6. Error with graceful degradation
```

**Tier-Specific Routing**:
- **LITE**: Ollama only (no fallback)
- **STANDARD**: Ollama + GPT-4 fallback
- **PROFESSIONAL**: Ollama + Claude + GPT-4
- **ENTERPRISE**: All providers + custom fine-tuning

### 4.3 Context Management Strategy

**Stage-Aware Prompting**:
- Each SDLC stage (00-09) has specific prompt template
- Evidence summaries included (top 10 relevant)
- Gate requirements injected
- Token efficiency through summarization

**Context Compression**:
- Full evidence: 10KB → Summary: 500 chars (95% reduction)
- Only metadata for non-critical evidence
- Semantic chunking for large documents

### 4.4 Safety and Ethics

**Input Sanitization**:
- PII detection (regex + ML model)
- Credential removal (API keys, passwords)
- Internal URL redaction

**Output Validation**:
- Code injection detection (dangerous patterns)
- Bias scoring (threshold >0.7 flagged)
- Prohibited content filtering

---

## 5. Technical Specification

### 5.1 AI Gateway Architecture

```python
# Pseudo-code for architecture illustration
class AIGateway:
    """Unified AI interface with multi-provider fallback"""

    def __init__(self):
        self.providers = [
            OllamaProvider(),     # Primary (internal)
            ClaudeProvider(),      # Fallback 1
            OpenAIProvider(),      # Fallback 2
        ]
        self.cache = RedisCache()
        self.safety = AISafetyGuard()
        self.cost_manager = AICostManager()

    async def complete(
        self,
        prompt: str,
        context: Dict[str, Any],
        use_cache: bool = True
    ) -> Dict[str, Any]:
        """Execute with fallback chain"""

        # Sanitize input
        prompt = await self.safety.sanitize_input(prompt)

        # Check cache
        if use_cache:
            cache_key = self._generate_cache_key(prompt, context)
            cached = await self.cache.get(cache_key)
            if cached:
                return {"response": cached, "provider": "cache", "latency_ms": 5}

        # Try each provider
        for i, provider in enumerate(self.providers):
            # Check budget
            if not await self.cost_manager.check_budget(provider, prompt):
                continue

            try:
                start = time.time()
                response = await provider.complete(prompt, context)
                latency = (time.time() - start) * 1000

                # Validate output
                validation = await self.safety.validate_output(response)
                if not validation["safe"]:
                    logger.warning(f"Unsafe output: {validation['issues']}")
                    response = validation["sanitized_text"]

                # Cache and return
                if use_cache:
                    await self.cache.set(cache_key, response, ttl=3600)

                return {
                    "response": response,
                    "provider": provider.__class__.__name__,
                    "latency_ms": latency,
                    "fallback_level": i
                }

            except Exception as e:
                logger.warning(f"Provider {provider} failed: {e}")
                continue

        raise AIServiceUnavailable("All providers failed")
```

### 5.2 Provider Implementations

**Ollama Provider**:
- **Endpoint**: `https://api.nhatquangholding.com/api/generate`
- **Model**: qwen2.5:14b
- **Timeout**: 30s
- **Retry**: 3 attempts with exponential backoff
- **Cost**: $0.001 per 1K tokens (infrastructure only)

**Claude Provider**:
- **Endpoint**: `https://api.anthropic.com/v1/messages`
- **Model**: claude-3-opus-20240229
- **Timeout**: 20s
- **Cost**: $0.015 input, $0.075 output per 1K tokens

**OpenAI Provider**:
- **Endpoint**: `https://api.openai.com/v1/chat/completions`
- **Model**: gpt-4-turbo-preview
- **Timeout**: 20s
- **Cost**: $0.03 input, $0.06 output per 1K tokens

### 5.3 Context Engine Architecture

```python
class ContextEngine:
    """Stage-aware context management"""

    async def build_context(
        self,
        project_id: str,
        stage: SDLCStage,
        include_evidence: bool = True
    ) -> Dict[str, Any]:
        """Build rich context for AI"""

        context = {
            "stage": stage.value,
            "stage_prompt": self.stage_prompts[stage],
            "project_id": project_id,
            "timestamp": datetime.utcnow().isoformat()
        }

        if include_evidence:
            # Fetch top 10 relevant evidence
            evidence = await self.evidence_vault.get_stage_evidence(
                project_id=project_id,
                stage=stage
            )

            # Summarize for token efficiency
            context["evidence"] = [
                {
                    "id": e.id,
                    "title": e.title,
                    "type": e.type,
                    "summary": await self._summarize_evidence(e)
                }
                for e in evidence[:10]
            ]

        # Add gate requirements
        gates = await self._get_stage_gates(stage)
        context["gates"] = [
            {
                "id": g.id,
                "name": g.name,
                "status": g.status,
                "requirements": g.requirements
            }
            for g in gates
        ]

        return context
```

### 5.4 API Endpoints

**POST /api/v1/ai/complete**
- Execute AI request with fallback
- Request: `{ "prompt": str, "context": dict, "use_cache": bool }`
- Response: `{ "response": str, "provider": str, "latency_ms": float }`

**POST /api/v1/ai/gate-recommend**
- Get gate recommendations for project
- Request: `{ "team_size": int, "project_type": str, "compliance": [str] }`
- Response: `{ "recommendations": [{ "gate_id": str, "reason": str }] }`

**POST /api/v1/ai/policy-generate**
- Generate OPA policy from requirement
- Request: `{ "requirement": str, "examples": [str] }`
- Response: `{ "policy_code": str, "test_cases": [str], "validated": bool }`

**GET /api/v1/ai/usage**
- Get AI usage statistics
- Response: `{ "requests": int, "cost": float, "providers": { "Ollama": int, "Claude": int } }`

---

## 6. Acceptance Criteria

| ID | Criterion | Test Method | Status |
|----|-----------|-------------|--------|
| **AC-001** | Ollama provider handles >80% requests | Load test 1000 requests, measure routing | ⏳ |
| **AC-002** | Fallback to Claude when Ollama fails | Integration test with mock Ollama failure | ⏳ |
| **AC-003** | Response time <3s p95 | Load test with 100 concurrent users | ⏳ |
| **AC-004** | Cache hit rate >60% for repeated queries | Production monitoring for 7 days | ⏳ |
| **AC-005** | PII detection 100% for known patterns | Unit test with 50 PII samples | ⏳ |
| **AC-006** | Cost <$0.01 per request average | Production monitoring for 30 days | ⏳ |
| **AC-007** | Availability >99.9% with fallback | Chaos test with provider failures | ⏳ |
| **AC-008** | Budget controls prevent overrun | Unit test with budget exhaustion | ⏳ |
| **AC-009** | Output validation catches code injection | Unit test with 20 injection samples | ⏳ |
| **AC-010** | Stage-aware prompts include evidence | Unit test for 10 stages, verify prompts | ⏳ |
| **AC-011** | Gate recommendations >80% accuracy | Manual review of 50 recommendations | ⏳ |
| **AC-012** | Policy generation produces valid Rego | Integration test with OPA validation | ⏳ |

---

## 7. Consequences

### 7.1 Positive Consequences

1. **Cost Efficiency**: 80% cost reduction ($50/month vs $1000/month)
2. **Data Privacy**: Sensitive data stays on-premise with Ollama
3. **Reliability**: Multi-provider fallback ensures 99.9% availability
4. **Flexibility**: Easy to add new providers or switch primary
5. **Performance**: Cache layer <100ms for repeated queries
6. **Heritage**: Leverages battle-tested AI-Platform (86% test coverage)

### 7.2 Negative Consequences

1. **Complexity**: Managing multiple providers adds operational overhead
2. **Latency Variance**: Ollama (2-6s) vs Cloud (1-3s) creates inconsistent UX
3. **Feature Gaps**: Ollama may not support latest features (function calling, vision)
4. **Maintenance**: Need to maintain prompt compatibility across providers

### 7.3 Risks and Mitigations

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Ollama downtime | Low | High | Automatic fallback to cloud providers |
| Token limits exceeded | Medium | Medium | Context compression, chunking strategies |
| Cost overrun | Low | Medium | Budget controls, usage monitoring, alerts |
| Prompt injection attacks | Low | Critical | Input sanitization, output validation |
| Model bias | Medium | Medium | Bias scoring, human review for sensitive outputs |

---

## 8. Spec Delta

### 8.1 Changes from Previous Version

**Version**: 1.0.0 (Initial Framework 6.0 migration)
**Date**: 2026-01-28

**Changes**:
- Migrated from legacy ADR format to Framework 6.0.5 specification standard
- Added YAML frontmatter with tier classification
- Converted requirements to BDD format (GIVEN-WHEN-THEN)
- Added structured acceptance criteria table
- Linked to related specs (SPEC-0001, SPEC-0002)
- Added tier-specific routing strategies
- Enhanced safety and security requirements

**Breaking Changes**: None (additive migration)

**Migration Notes**:
- Original ADR-007 preserved in git history
- Framework 6.0 version is canonical going forward
- References updated in SPEC-0001, SPEC-0002

---

## 9. Dependencies

### 9.1 Internal Dependencies

| Dependency | Type | Reason |
|------------|------|--------|
| Evidence Vault | Service | Provides evidence for context inclusion |
| Redis Cache | Infrastructure | Caching layer for response storage |
| PostgreSQL | Database | Usage tracking, audit logging |
| OPA Service | Service | Policy validation (for generated policies) |

### 9.2 External Dependencies

| Dependency | Type | Reason |
|------------|------|--------|
| Ollama | Infrastructure | Primary AI provider (api.nhatquangholding.com) |
| Anthropic API | External API | Claude fallback provider |
| OpenAI API | External API | GPT-4 fallback provider |
| tenacity | Python Library | Retry logic with exponential backoff |
| httpx | Python Library | Async HTTP client |

### 9.3 Related Specifications

- **SPEC-0001**: Governance System Implementation (uses AI for recommendations)
- **SPEC-0002**: Quality Gates Codegen (uses AI for code analysis)
- **ADR-022**: Multi-Provider Codegen Architecture (similar fallback pattern)
- **ADR-036**: 4-Tier Policy Enforcement (tier-based AI routing)

---

## 10. Implementation Plan

### 10.1 Phase 1: Foundation (Week 1 BUILD)

**Tasks**:
- [ ] Setup AI Gateway with provider abstraction
- [ ] Implement Ollama provider with api.nhatquangholding.com
- [ ] Add Claude and OpenAI providers
- [ ] Create context engine with stage-aware prompting
- [ ] Add Redis caching layer

**Deliverables**:
- `ai_gateway.py` (200 LOC)
- `ollama_provider.py` (150 LOC)
- `claude_provider.py` (150 LOC)
- `openai_provider.py` (150 LOC)
- `context_engine.py` (300 LOC)

**Tests**: 50 unit tests, 20 integration tests

### 10.2 Phase 2: Core Features (Week 2 BUILD)

**Tasks**:
- [ ] Gate recommendation service
- [ ] Policy generation from natural language
- [ ] Evidence analysis and summarization
- [ ] Intelligent search with semantic similarity

**Deliverables**:
- `gate_recommendation.py` (200 LOC)
- `policy_generation.py` (250 LOC)
- `evidence_analysis.py` (200 LOC)
- `semantic_search.py` (150 LOC)

**Tests**: 40 unit tests, 15 integration tests

### 10.3 Phase 3: Safety & Optimization (Week 3 BUILD)

**Tasks**:
- [ ] PII detection and redaction
- [ ] Output validation and safety checks
- [ ] Cost tracking and budget controls
- [ ] Performance monitoring and alerts

**Deliverables**:
- `ai_safety.py` (300 LOC)
- `pii_detector.py` (200 LOC)
- `ai_cost_manager.py` (250 LOC)
- `usage_tracker.py` (150 LOC)

**Tests**: 60 unit tests, 10 integration tests

### 10.4 Phase 4: Advanced Features (Week 4+ BUILD)

**Tasks**:
- [ ] Multi-turn conversations with context
- [ ] Batch processing for large analyses
- [ ] Fine-tuning Ollama for SDLC domain
- [ ] A/B testing different models

**Deliverables**: TBD based on Phase 1-3 feedback

---

## 11. Approval

| Role | Name | Decision | Date | Comment |
|------|------|----------|------|---------|
| **CTO** | [CTO Name] | ✅ APPROVED | 2025-11-13 | Excellent cost/privacy balance with Ollama |
| **CPO** | [CPO Name] | ✅ APPROVED | 2025-11-13 | AI = 20% of competitive moat, critical for UX |
| **Security Lead** | [Security Name] | ✅ APPROVED | 2025-11-13 | On-premise option addresses data concerns |
| **Framework 6.0 Migration** | AI Partner | ✅ MIGRATED | 2026-01-28 | Converted to Framework 6.0.5 standard |

---

## Appendix A: Cost Analysis

### Monthly Cost Projection

| Scenario | Ollama % | Cloud % | Monthly Cost | Savings |
|----------|----------|---------|--------------|---------|
| **Hybrid (Actual)** | **80%** | **20%** | **$50-200** | **80-84%** |
| Cloud-Only | 0% | 100% | $1000-1200 | 0% |
| Ollama-Only | 100% | 0% | $50 | 95% |

**Assumptions**:
- 100,000 requests/month
- Average 1K tokens per request
- Ollama: $0.001 per 1K tokens
- Claude/GPT-4: $0.045 per 1K tokens (average)

---

## Appendix B: Performance Benchmarks

| Provider | p50 Latency | p95 Latency | p99 Latency | Cost per 1K |
|----------|-------------|-------------|-------------|-------------|
| **Cache** | **5ms** | **10ms** | **20ms** | **$0** |
| **Ollama** | **2.5s** | **4.5s** | **6s** | **$0.001** |
| **Claude** | **1.2s** | **2.5s** | **3.5s** | **$0.045** |
| **GPT-4** | **1.5s** | **2.8s** | **4s** | **$0.045** |

---

**Decision Status**: ✅ **APPROVED** - Hybrid AI Architecture with Ollama primary + cloud fallback

**Priority**: **CRITICAL** - Blocks 20% of product differentiation

**Timeline**: 4 weeks implementation in BUILD phase (Phase 1-4)

**Success Metrics**:
- Cost per request <$0.01 average
- Response time <3s p95
- Availability >99.9%
- User satisfaction >4.0/5 for AI features

---

*Framework 6.0.5 Migration - Sprint 117*
*"Leverage internal AI infrastructure (Ollama) while maintaining cloud flexibility"* 🤖
