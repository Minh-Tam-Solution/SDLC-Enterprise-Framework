# SPEC-0006: Multi-Provider Codegen Architecture

## Frontmatter

```yaml
spec_id: SPEC-0006
title: Multi-Provider Codegen Architecture (ADR-022)
version: 1.0.0
status: approved
tier: PROFESSIONAL
pillar: Pillar 4 - Build & Implementation
owner: CTO + Backend Lead
last_updated: 2026-01-29
tags:
  - codegen
  - multi-provider
  - ep-06
  - ir-based
  - ollama
  - vietnam-sme
related_specs:
  - SPEC-0003  # AI Context Engine
  - SPEC-0004  # Policy Guards
  - SPEC-0009  # Codegen Service
  - SPEC-0010  # IR Processor
epic: EP-06 IR-Based Codegen Engine
sprint: Sprint 45 (Jan 6-17, 2026)
implementation_ref: "SDLC-Orchestrator/docs/02-design/03-ADRs/ADR-022-Multi-Provider-Codegen-Architecture.md"
```

---

## Executive Summary

This specification defines a **provider-agnostic codegen architecture** for SDLC Orchestrator's EP-06 IR-based code generation engine. The architecture enables Vietnamese SME to generate production-ready code using Ollama as primary provider (cost: $50/month), with graceful fallback to Claude ($1000/month) and DeepCode (Q2 2026), avoiding vendor lock-in while achieving **96% token reduction** and **10x faster generation** through Intermediate Representation (IR) schemas.

**Strategic Impact**:
- Vietnam SME wedge: Non-tech founders generate MVPs without coding (40% market)
- Global EM wedge: Engineering Managers govern AI-generated code (40% market)
- Cost efficiency: $11,400/year savings (95% cost reduction vs Claude-first)
- No hard dependencies: System works with any AI provider, degrades gracefully

---

## 1. Context and Problem Statement

### 1.1 Strategic Requirements

**Software 3.0 Positioning**: SDLC Orchestrator is pivoting to become the **"Operating System for Software 3.0"** - a control plane that orchestrates ALL AI coders under governance, evidence, and policy-as-code.

**Key Requirements**:

| Requirement | Description | Priority | Business Impact |
|------------|-------------|----------|-----------------|
| **Vietnam SME Wedge** | Non-tech founders need MVP generation without coding | **P0** | 40% of target market |
| **Global EM Wedge** | Engineering Managers need to govern AI-generated code | **P0** | 40% of target market |
| **No Hard Dependencies** | System must work with any AI provider, fallback gracefully | **P0** | Vendor lock-in avoidance |
| **Cost Efficiency** | Prefer Ollama (~$50/month) over Claude ($1000/month) | **P1** | $11,400/year savings |
| **IR-Based Generation** | Use IR schemas to reduce token usage (96% reduction) | **P1** | 10x faster, 25x cheaper |

### 1.2 Current Pain Points

**Before Multi-Provider Architecture**:

| Pain Point | Impact | Severity |
|-----------|---------|----------|
| Hard dependency on single AI provider | Vendor lock-in, no fallback | **HIGH** |
| Full context generation (128K tokens) | Slow (30s), expensive ($0.50/gen) | **HIGH** |
| Large model requirement (100B+ params) | Cannot run locally/edge | **MEDIUM** |
| No cost optimization strategy | $1000/month vs $50/month | **MEDIUM** |
| No graceful degradation | Complete failure if provider down | **MEDIUM** |

### 1.3 3-Layer Architecture Context

```
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 3: AI CODERS (They Generate)                                 │
│  Claude Code | Cursor | Copilot | Aider | Ollama                    │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 2: SDLC ORCHESTRATOR (We Govern) ← THIS SPEC                 │
│  ★ Multi-Provider Architecture: Ollama → Claude → DeepCode         │
│  ★ EP-06 Codegen: IR-based generation for Vietnam SME              │
├─────────────────────────────────────────────────────────────────────┤
│  LAYER 1: SDLC-ENTERPRISE-FRAMEWORK (Methodology)                   │
│  10 Stages | 4 Tiers | Quality Gates                                │
└─────────────────────────────────────────────────────────────────────┘
```

**Strategic Position**: SDLC Orchestrator operates in Layer 2 as the governance layer, orchestrating Layer 3 AI coders using Layer 1 methodology definitions.

---

## 2. Requirements (BDD Format)

### 2.1 FR-001: Abstract Provider Interface

**GIVEN** a code generation request with IR specification
**WHEN** the system needs to generate code
**THEN** the system MUST use a provider-agnostic interface with:
- Standard methods: `generate()`, `validate()`, `estimate_cost()`
- Input: `CodegenSpec` (IR blueprint, language, framework, target module)
- Output: `CodegenResult` (generated code, files, metadata, tokens, timing)
- Error handling: Provider-specific exceptions mapped to standard errors

**Acceptance Criteria**:
- ✅ Abstract base class `CodegenProvider` with 3 required methods
- ✅ Pydantic models for input/output validation
- ✅ Type hints for all method signatures (Python 3.11+)
- ✅ Docstrings with examples (Google style)

**Tier-Specific Requirements**:
- **LITE**: Single provider only (Ollama)
- **STANDARD**: Primary + 1 fallback (Ollama → Claude)
- **PROFESSIONAL**: Multi-provider with fallback chain (Ollama → Claude → DeepCode)
- **ENTERPRISE**: Multi-provider + custom provider registration

### 2.2 FR-002: Provider Registry and Dynamic Discovery

**GIVEN** multiple codegen providers registered
**WHEN** a generation request arrives with optional preferred provider
**THEN** the system MUST:
- Select preferred provider if available
- Fall back to next provider in chain if preferred unavailable
- Return `NoProviderAvailableError` if all providers unavailable
- Log provider selection decisions for audit

**Acceptance Criteria**:
- ✅ `ProviderRegistry` class with register/unregister methods
- ✅ Dynamic provider discovery and availability checking
- ✅ Configurable fallback chain (default: ollama → claude → deepcode)
- ✅ Thread-safe provider selection (singleton registry)

**Tier-Specific Requirements**:
- **LITE**: Static configuration only
- **STANDARD**: Dynamic configuration, restart required
- **PROFESSIONAL**: Dynamic registration, hot reload supported
- **ENTERPRISE**: Runtime provider plugin system

### 2.3 FR-003: Ollama as Primary Provider

**GIVEN** Ollama provider configured at api.nhatquangholding.com
**WHEN** a Vietnamese SME user generates code
**THEN** the system MUST:
- Use Ollama with Vietnamese-optimized prompts
- Parse IR blueprint into code generation prompt
- Extract multi-file output from Ollama response
- Return structured `CodegenResult` with timing metrics

**Acceptance Criteria**:
- ✅ `OllamaCodegenProvider` implementation complete
- ✅ Vietnamese prompt templates for common SME domains
- ✅ IR-to-prompt translation (<5K tokens input)
- ✅ Multi-file parsing with `### FILE:` markers
- ✅ <15s generation time (p95) for typical IR

**Tier-Specific Requirements**:
- **LITE**: Basic code generation, single-file output
- **STANDARD**: Multi-file generation, basic validation
- **PROFESSIONAL**: Vietnamese comments, production-ready code
- **ENTERPRISE**: Domain-specific templates (E-commerce, HRM, CRM)

### 2.4 FR-004: Graceful Fallback Chain

**GIVEN** primary provider (Ollama) unavailable or timeout
**WHEN** generation request fails
**THEN** the system MUST:
- Log primary provider failure with reason
- Attempt next provider in fallback chain (Claude)
- If all providers fail, return `NoProviderAvailableError`
- Track fallback frequency metrics for monitoring

**Acceptance Criteria**:
- ✅ Fallback chain configurable via YAML config
- ✅ Retry logic with exponential backoff (max 3 attempts)
- ✅ Provider-specific timeout configuration
- ✅ Prometheus metrics for fallback events

**Tier-Specific Requirements**:
- **LITE**: No fallback (single provider only)
- **STANDARD**: 1 fallback provider
- **PROFESSIONAL**: Full fallback chain (3 providers)
- **ENTERPRISE**: Custom fallback logic (e.g., round-robin, load balancing)

### 2.5 FR-005: Cost Estimation Across Providers

**GIVEN** an IR specification
**WHEN** user requests cost estimation before generation
**THEN** the system MUST:
- Estimate token usage for each available provider
- Calculate cost based on provider pricing (Ollama ~$0.001/1K, Claude $0.015/1K)
- Return cost comparison table
- Recommend cheapest provider meeting quality threshold

**Acceptance Criteria**:
- ✅ `estimate_cost()` method on all providers
- ✅ Cost comparison API endpoint (`POST /codegen/estimate`)
- ✅ Confidence score for each estimate (0-1)
- ✅ Recommendation algorithm (cost vs quality tradeoff)

**Tier-Specific Requirements**:
- **LITE**: Single provider estimate only
- **STANDARD**: Cost comparison between 2 providers
- **PROFESSIONAL**: Full cost matrix + recommendation
- **ENTERPRISE**: Historical cost tracking + budget alerts

### 2.6 FR-006: Validation Across Providers

**GIVEN** generated code from any provider
**WHEN** user requests validation
**THEN** the system MUST:
- Parse code for syntax errors (ast.parse for Python)
- Check security issues (Semgrep integration)
- Validate against IR specification (all entities generated)
- Return structured `ValidationResult` (valid, errors, warnings, suggestions)

**Acceptance Criteria**:
- ✅ `validate()` method on all providers
- ✅ Static analysis integration (ruff, mypy for Python)
- ✅ Security scanning (Semgrep SAST rules)
- ✅ IR completeness check (all blueprint entities present)

**Tier-Specific Requirements**:
- **LITE**: Syntax validation only
- **STANDARD**: Syntax + basic security checks
- **PROFESSIONAL**: Full validation pipeline (4-gate quality)
- **ENTERPRISE**: Custom validation rules per project

### 2.7 FR-007: Stub Providers (No Hard Dependencies)

**GIVEN** Claude and DeepCode providers registered
**WHEN** these providers are not configured with API keys
**THEN** the system MUST:
- Report provider as unavailable (`is_available = False`)
- Skip in fallback chain
- Provide cost estimates even when unavailable
- NOT import provider-specific SDKs (AGPL containment)

**Acceptance Criteria**:
- ✅ `ClaudeCodegenProvider` stub with no Anthropic SDK import
- ✅ `DeepCodeProvider` stub (deferred to Q2 2026)
- ✅ Network-only API calls (httpx/requests, no SDK)
- ✅ AGPL containment validated (zero SDK imports)

**Tier-Specific Requirements**:
- **ALL TIERS**: Stub providers allowed, gracefully skipped in fallback

---

## 3. Architecture Design

### 3.1 Core Components

```python
# Component Hierarchy:
# 1. CodegenProvider (Abstract Interface) - 3 methods
#    ├── OllamaCodegenProvider (Primary)
#    ├── ClaudeCodegenProvider (Fallback 1, stub)
#    └── DeepCodeProvider (Fallback 2, stub)
#
# 2. ProviderRegistry (Singleton) - Dynamic registration
#    ├── Fallback chain: ollama → claude → deepcode
#    └── Provider selection algorithm
#
# 3. CodegenService (Orchestrator) - Main entry point
#    ├── generate() - Route to provider
#    ├── validate() - Validate generated code
#    └── estimate_cost() - Cost comparison
#
# 4. API Routes (/codegen/*) - REST API
#    ├── POST /codegen/generate
#    ├── POST /codegen/validate
#    ├── POST /codegen/estimate
#    └── GET /codegen/providers
```

### 3.2 Data Models (Pydantic)

**CodegenSpec** (Input):
```python
class CodegenSpec(BaseModel):
    """Input specification for code generation"""
    app_blueprint: Dict[str, Any]  # IR schema
    target_module: Optional[str] = None
    language: str = "python"
    framework: str = "fastapi"
```

**CodegenResult** (Output):
```python
class CodegenResult(BaseModel):
    """Output from code generation"""
    code: str                      # Raw generated code
    files: Dict[str, str]          # filename -> content
    metadata: Dict[str, Any]       # Model, tokens, etc.
    provider: str                  # Provider name used
    tokens_used: int               # Total tokens
    generation_time_ms: int        # Generation duration
```

**ValidationResult** (Validation):
```python
class ValidationResult(BaseModel):
    """Output from code validation"""
    valid: bool                    # Overall validity
    errors: list[str]              # Blocking issues
    warnings: list[str]            # Non-blocking issues
    suggestions: list[str]         # Improvement suggestions
```

**CostEstimate** (Estimation):
```python
class CostEstimate(BaseModel):
    """Cost estimation for generation"""
    estimated_tokens: int          # Token count estimate
    estimated_cost_usd: float      # Cost in USD
    provider: str                  # Provider name
    confidence: float              # 0-1 confidence score
```

### 3.3 Provider Interface Contract

**CodegenProvider (Abstract Base Class)**:

| Method | Parameters | Returns | Raises | Description |
|--------|-----------|---------|--------|-------------|
| `name` | - | `str` | - | Property: Provider identifier |
| `is_available` | - | `bool` | - | Property: Provider availability check |
| `generate()` | `spec: CodegenSpec` | `CodegenResult` | `ProviderUnavailableError`, `GenerationError` | Generate code from IR |
| `validate()` | `code: str`, `context: dict` | `ValidationResult` | - | Validate generated code |
| `estimate_cost()` | `spec: CodegenSpec` | `CostEstimate` | - | Estimate generation cost |

### 3.4 Configuration Schema

**config/codegen.yaml**:
```yaml
codegen:
  default_provider: ollama           # Used if project doesn't specify

  fallback_chain:                    # Fallback order
    - ollama
    - claude
    - deepcode

  providers:
    ollama:
      enabled: true
      base_url: "https://api.nhatquangholding.com"
      model: "qwen2.5-coder:14b"    # Vietnamese-optimized
      timeout_seconds: 60
      max_retries: 3

    claude:
      enabled: false                 # Stub only
      api_key: "${ANTHROPIC_API_KEY}"

    deepcode:
      enabled: false                 # Deferred to Q2 2026
```

---

## 4. Implementation Details

### 4.1 OllamaCodegenProvider - Vietnamese Prompts

**Vietnamese-Optimized Prompt Template**:
```python
def _build_prompt(self, spec: CodegenSpec) -> str:
    """Build Vietnamese-optimized prompt for code generation"""
    return f"""Bạn là một AI chuyên gia phát triển phần mềm cho doanh nghiệp SME Việt Nam.

Dựa trên đặc tả IR (Intermediate Representation) sau, hãy tạo code {spec.framework} hoàn chỉnh:

## App Blueprint
```json
{spec.app_blueprint}
```

## Yêu cầu:
- Ngôn ngữ: {spec.language}
- Framework: {spec.framework}
- Module mục tiêu: {spec.target_module or 'Tất cả'}

## Output Format:
Trả về code theo format sau:

### FILE: path/to/file.py
```python
# code here
```

### FILE: path/to/another_file.py
```python
# code here
```

Hãy tạo code production-ready, có comments tiếng Việt khi cần thiết.
"""
```

**Key Features**:
- Vietnamese instructions for Vietnam SME context
- IR blueprint embedded as JSON
- Multi-file output format with `### FILE:` markers
- Production-ready code requirement

### 4.2 Multi-File Output Parsing

**Output Parsing Algorithm**:
```python
def _parse_code_output(self, output: str) -> Dict[str, str]:
    """Parse Ollama output into file dictionary"""
    files = {}
    current_file = None
    current_content = []

    for line in output.split('\n'):
        if line.startswith('### FILE:'):
            # New file section
            if current_file:
                files[current_file] = '\n'.join(current_content)
            current_file = line.replace('### FILE:', '').strip()
            current_content = []
        elif current_file:
            # Accumulate file content
            current_content.append(line)

    # Last file
    if current_file:
        files[current_file] = '\n'.join(current_content)

    return files
```

### 4.3 Error Handling and Retry Policy

**Error Types and Handling**:

| Error | Cause | Handling Strategy | Retry |
|-------|-------|-------------------|-------|
| `ProviderUnavailableError` | Provider not configured/unreachable | Try fallback chain | No |
| `GenerationError` | Code generation failed | Retry with exponential backoff | Yes (3x) |
| `ValidationError` | Code validation failed | Return validation result | No |
| `NoProviderAvailableError` | All providers unavailable | Return 503 HTTP error | No |
| `TimeoutError` | Generation took too long | Retry once, then fail | Yes (1x) |

**Retry Logic (tenacity)**:
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(min=1, max=10)
)
async def generate_with_retry(spec: CodegenSpec) -> CodegenResult:
    # Generation logic with automatic retry
    pass
```

---

## 5. API Endpoints

### 5.1 List Providers

**Endpoint**: `GET /api/v1/codegen/providers`

**Request**: None

**Response** (200 OK):
```json
{
  "providers": [
    {
      "name": "ollama",
      "available": true,
      "primary": true
    },
    {
      "name": "claude",
      "available": false,
      "primary": false
    },
    {
      "name": "deepcode",
      "available": false,
      "primary": false
    }
  ],
  "fallback_chain": ["ollama", "claude", "deepcode"]
}
```

### 5.2 Generate Code

**Endpoint**: `POST /api/v1/codegen/generate`

**Request**:
```json
{
  "app_blueprint": {
    "entities": [
      {
        "name": "User",
        "fields": [
          {"name": "id", "type": "UUID"},
          {"name": "email", "type": "String"}
        ]
      }
    ]
  },
  "target_module": "users",
  "language": "python",
  "framework": "fastapi",
  "preferred_provider": "ollama"
}
```

**Response** (200 OK):
```json
{
  "success": true,
  "result": {
    "code": "...",
    "files": {
      "backend/app/models/user.py": "...",
      "backend/app/api/routes/users.py": "..."
    },
    "metadata": {
      "model": "qwen2.5-coder:14b",
      "prompt_tokens": 450,
      "completion_tokens": 1250
    },
    "provider": "ollama",
    "tokens_used": 1700,
    "generation_time_ms": 8500
  }
}
```

**Error Response** (503 Service Unavailable):
```json
{
  "detail": "No codegen providers available"
}
```

### 5.3 Validate Code

**Endpoint**: `POST /api/v1/codegen/validate`

**Request**:
```json
{
  "code": "def hello():\n    print('Hello')",
  "context": {
    "language": "python",
    "framework": "fastapi"
  },
  "provider": "ollama"
}
```

**Response** (200 OK):
```json
{
  "success": true,
  "result": {
    "valid": true,
    "errors": [],
    "warnings": ["Function 'hello' has no docstring"],
    "suggestions": ["Add type hints for better IDE support"]
  }
}
```

### 5.4 Estimate Cost

**Endpoint**: `POST /api/v1/codegen/estimate`

**Request**: Same as `/generate`

**Response** (200 OK):
```json
{
  "estimates": {
    "ollama": {
      "estimated_tokens": 1800,
      "estimated_cost_usd": 0.0018,
      "provider": "ollama",
      "confidence": 0.8
    },
    "claude": {
      "estimated_tokens": 1800,
      "estimated_cost_usd": 0.027,
      "provider": "claude",
      "confidence": 0.7
    }
  }
}
```

---

## 6. Performance Targets

### 6.1 Generation Performance

| Metric | Target (p95) | Measurement | Tier |
|--------|-------------|-------------|------|
| **Generation Time (Ollama)** | <15s | End-to-end API latency | ALL |
| **Generation Time (Claude)** | <25s | End-to-end API latency | PRO+ |
| **Token Usage (IR-based)** | <5K input tokens | IR size measurement | ALL |
| **Cost per Generation (Ollama)** | <$0.002 | Token usage × pricing | ALL |
| **Validation Time** | <10s | Syntax + SAST checks | PRO+ |

### 6.2 IR-Based Optimization Results

**Comparison: Full Context vs IR-Based**:

| Metric | Full Context | IR-Based | Improvement |
|--------|--------------|----------|-------------|
| **Token Usage** | 128,000 tokens | 5,000 tokens | **96% reduction** |
| **Generation Time** | 30 seconds | <3 seconds | **10x faster** |
| **Cost per Generation** | $0.50 | $0.02 | **25x cheaper** |
| **Model Requirement** | 100B+ params | 7-14B params | **Smaller models work** |

### 6.3 Availability Targets

| SLA Metric | Target | Measurement | Tier |
|------------|--------|-------------|------|
| **Primary Provider Uptime** | >99.5% | Ollama availability | PRO+ |
| **Fallback Success Rate** | >95% | Fallback to Claude when Ollama fails | PRO+ |
| **Total System Availability** | >99.9% | Any provider available | ENT |

---

## 7. Security Considerations

### 7.1 AGPL Containment (Critical)

**Requirement**: Zero SDK imports for AGPL-licensed providers

**Enforcement**:
- ✅ Use `httpx` or `requests` for network-only API calls
- ✅ NO `import anthropic` (Claude SDK)
- ✅ NO `from minio import` (MinIO SDK, if used)
- ✅ Pre-commit hook blocks AGPL imports

**Validation**:
```bash
# CI/CD check
grep -r "import anthropic" backend/app/services/codegen/ && exit 1
grep -r "from minio import" backend/app/services/codegen/ && exit 1
echo "PASS: No AGPL SDK imports"
```

### 7.2 API Key Management

**Requirements**:
- Claude API key stored in HashiCorp Vault
- 90-day rotation policy
- Encrypted at-rest (AES-256)
- Never logged or exposed in responses

### 7.3 Code Injection Prevention

**Requirements**:
- Validate IR blueprint schema before generation
- Sanitize generated code for SQL injection, XSS
- Semgrep SAST scan on generated code
- Reject code with critical security issues

---

## 8. Monitoring and Observability

### 8.1 Prometheus Metrics

**Metrics to Collect**:

| Metric | Type | Description | Labels |
|--------|------|-------------|--------|
| `codegen_requests_total` | Counter | Total generation requests | provider, success/failure |
| `codegen_generation_duration_seconds` | Histogram | Generation time distribution | provider |
| `codegen_tokens_used_total` | Counter | Total tokens consumed | provider |
| `codegen_cost_usd_total` | Counter | Total cost in USD | provider |
| `codegen_fallback_events_total` | Counter | Fallback to secondary provider | primary, fallback |
| `codegen_provider_availability` | Gauge | Provider availability (0/1) | provider |

### 8.2 Logging

**Log Events**:
- Provider selection decision (info level)
- Fallback events (warning level)
- Generation failures (error level with stack trace)
- Cost per generation (info level)

**Log Format** (structured JSON):
```json
{
  "timestamp": "2026-01-29T10:15:30Z",
  "level": "INFO",
  "event": "provider_selected",
  "provider": "ollama",
  "preferred": "ollama",
  "fallback_used": false,
  "generation_time_ms": 8500,
  "tokens_used": 1700,
  "cost_usd": 0.0017
}
```

---

## 9. Acceptance Criteria

### 9.1 Functional Acceptance (PROFESSIONAL Tier)

| Criterion | Pass Condition | Test Method |
|-----------|---------------|-------------|
| **Provider Interface** | All providers implement `CodegenProvider` | Unit test |
| **Ollama Generation** | Generate multi-file FastAPI app from IR | Integration test |
| **Fallback Chain** | Claude used when Ollama unavailable | Integration test |
| **Cost Estimation** | Estimate within 20% of actual cost | Integration test |
| **Vietnamese Prompts** | Ollama uses Vietnamese instructions | Manual review |
| **AGPL Containment** | Zero SDK imports in provider code | CI/CD check |
| **API Endpoints** | All 4 endpoints return correct response schema | API test |

### 9.2 Performance Acceptance

| Criterion | Target | Pass Condition | Test Method |
|-----------|--------|----------------|-------------|
| **Generation Time (Ollama)** | <15s p95 | 95% of requests < 15s | Load test (100 req) |
| **Generation Time (Claude)** | <25s p95 | 95% of requests < 25s | Load test (50 req) |
| **IR Token Usage** | <5K tokens input | Average < 5000 tokens | Log analysis |
| **Fallback Success** | >95% | Claude succeeds when Ollama fails | Fault injection test |

### 9.3 Security Acceptance

| Criterion | Pass Condition | Test Method |
|-----------|----------------|-------------|
| **AGPL Containment** | Zero AGPL SDK imports | Automated scan |
| **API Key Security** | Keys in Vault, never logged | Security audit |
| **Code Injection** | Generated code passes SAST scan | Semgrep integration |

---

## 10. Decision Rationale

### 10.1 Why Provider-Agnostic?

| Approach | Pros | Cons | Decision |
|----------|------|------|----------|
| **DeepCode-first** | Advanced capabilities, Vietnamese-optimized | $16K budget, hard dependency, DeepCode-specific | ❌ Rejected |
| **Claude-first** | High quality, proven at scale | $1000/month, external API, internet required | ❌ Rejected |
| **Ollama-first** | $50/month, internal hosting, Vietnamese support | Smaller model (14B params) | ✅ Selected |
| **Provider-agnostic** | Flexibility, no vendor lock-in, graceful degradation | More abstraction overhead | ✅ Selected |

**Final Decision**: Ollama-first + Provider-agnostic architecture

**Rationale**:
- **Cost**: $11,400/year savings (95% cost reduction)
- **Flexibility**: Can switch providers without code changes
- **Graceful Degradation**: System continues working if Ollama fails
- **Vietnam SME Focus**: Vietnamese prompts optimized for target market

### 10.2 Why IR-Based Generation?

**Token Reduction Comparison**:

| Approach | Input Tokens | Output Tokens | Total | Cost |
|----------|--------------|---------------|-------|------|
| **Full Context** | 100K (all files) | 28K (generated) | 128K | $0.50 |
| **IR-Based** | 3K (blueprint) | 2K (generated) | 5K | $0.02 |

**Benefits**:
- **96% token reduction**: From 128K → 5K tokens
- **10x faster**: From 30s → 3s generation time
- **25x cheaper**: From $0.50 → $0.02 per generation
- **Smaller models work**: 7-14B params sufficient (vs 100B+ for full context)

---

## 11. Consequences

### 11.1 Positive Consequences

1. **No Vendor Lock-in**: Can switch providers without code changes
2. **Cost Efficiency**: Ollama-first saves ~$950/month vs Claude-first (~$11,400/year)
3. **Graceful Degradation**: Fallback chain ensures high availability (>99.9%)
4. **Easy Extension**: Add new providers by implementing `CodegenProvider` interface
5. **Testable**: Can mock providers for unit testing
6. **Vietnam SME Friendly**: Vietnamese prompts improve generation quality for target market

### 11.2 Negative Consequences

1. **Abstraction Overhead**: Slight performance cost from abstraction layer (estimated <50ms)
2. **Complexity**: More code than single-provider approach (~500 LOC vs ~200 LOC)
3. **Provider Output Differences**: Quality may vary between providers (requires monitoring)
4. **Maintenance Burden**: Must keep multiple provider implementations updated

### 11.3 Neutral Consequences

1. **Configuration Required**: Must configure providers in config file (YAML)
2. **Monitoring Needed**: Should track provider usage and fallback frequency (Prometheus)
3. **Provider Compatibility**: Must ensure all providers support same IR schema version

---

## 12. Implementation Plan

### 12.1 Sprint 45 Week 1 (Jan 6-10, 2026)

| Task | Assignee | Estimated Hours | Priority |
|------|----------|----------------|----------|
| Create `base_provider.py` with abstract interface | Backend Lead | 4h | **P0** |
| Create `provider_registry.py` with routing logic | Backend Lead | 6h | **P0** |
| Create `codegen_service.py` orchestrator | Backend Developer | 8h | **P0** |
| Create `codegen.py` API routes (4 endpoints) | Backend Developer | 6h | **P0** |
| Write integration test for ollama-only boot | QA Engineer | 4h | **P1** |

**Milestone**: Abstract architecture complete, ready for provider implementation

### 12.2 Sprint 45 Week 2 (Jan 13-17, 2026)

| Task | Assignee | Estimated Hours | Priority |
|------|----------|----------------|----------|
| Implement `OllamaCodegenProvider` with Vietnamese prompts | Backend Lead | 12h | **P0** |
| Create stub `ClaudeCodegenProvider` | Backend Developer | 4h | **P1** |
| Create stub `DeepCodeProvider` | Backend Developer | 2h | **P2** |
| Create configuration schema (codegen.yaml) | DevOps Engineer | 3h | **P1** |
| Write runbook for disabling providers | Tech Writer | 4h | **P1** |
| Demo with minimal AppBlueprint | Product Manager | 2h | **P0** |

**Milestone**: Ollama provider working end-to-end, demo-ready

---

## 13. Testing Strategy

### 13.1 Unit Tests

**Coverage Target**: >95%

**Test Cases**:
- `test_provider_interface_contract()`: All providers implement required methods
- `test_ollama_prompt_generation()`: Vietnamese prompts generated correctly
- `test_multi_file_parsing()`: Parse Ollama output into file dictionary
- `test_cost_estimation()`: Cost estimates within expected range
- `test_validation_result_parsing()`: Parse validation output correctly

### 13.2 Integration Tests

**Coverage Target**: >90%

**Test Cases**:
- `test_ollama_end_to_end()`: Generate FastAPI app from minimal IR
- `test_fallback_to_claude()`: Claude used when Ollama unavailable
- `test_no_provider_available()`: Return 503 when all providers down
- `test_api_endpoints()`: All 4 API endpoints return correct schema
- `test_agpl_containment()`: Zero AGPL SDK imports detected

### 13.3 Performance Tests

**Tool**: Locust

**Test Cases**:
- `test_generation_latency_p95()`: 100 concurrent requests, measure p95 latency
- `test_token_usage()`: Verify IR-based generation uses <5K input tokens
- `test_cost_per_generation()`: Measure actual cost vs estimated cost

---

## 14. Rollout Plan

### 14.1 Phase 1: Internal Dogfooding (Sprint 45)

**Duration**: 2 weeks
**Audience**: Internal SDLC Orchestrator team (5 developers)

**Success Criteria**:
- [ ] Generate 10+ FastAPI apps from IR
- [ ] Fallback to Claude tested (simulated Ollama failure)
- [ ] Zero AGPL violations detected
- [ ] <15s generation time (p95) achieved

### 14.2 Phase 2: Vietnam SME Pilot (Sprint 49 - Q1 2026)

**Duration**: 4 weeks
**Audience**: 5 founding Vietnam SME customers

**Success Criteria**:
- [ ] 5 customers generate production MVPs
- [ ] Vietnamese prompts validated by native speakers
- [ ] >95% generation success rate
- [ ] <$0.002 average cost per generation

### 14.3 Phase 3: General Availability (Sprint 50 - Q1 2026)

**Duration**: Ongoing
**Audience**: All SDLC Orchestrator users

**Success Criteria**:
- [ ] Ollama provider uptime >99.5%
- [ ] Fallback success rate >95%
- [ ] Cost savings vs Claude-first validated ($11K+/year)

---

## 15. Runbook

### 15.1 Disable Provider

**Scenario**: Ollama provider causing issues, need to disable

**Steps**:
1. Edit `config/codegen.yaml`:
   ```yaml
   providers:
     ollama:
       enabled: false  # Disable Ollama
   ```
2. Restart SDLC Orchestrator backend
3. Verify fallback to Claude: `curl http://localhost:8000/api/v1/codegen/providers`
4. Monitor fallback metrics in Grafana

### 15.2 Add New Provider

**Scenario**: Add new provider (e.g., GPT-4)

**Steps**:
1. Create provider class:
   ```python
   # backend/app/services/codegen/gpt4_provider.py
   class GPT4CodegenProvider(CodegenProvider):
       # Implement abstract methods
   ```
2. Register in `CodegenService.__init__()`:
   ```python
   registry.register(GPT4CodegenProvider())
   ```
3. Update fallback chain in config:
   ```yaml
   fallback_chain:
     - ollama
     - gpt4
     - claude
   ```
4. Deploy and test

### 15.3 Monitor Costs

**Scenario**: Unexpected cost spike

**Steps**:
1. Query Prometheus: `sum(rate(codegen_cost_usd_total[1h])) by (provider)`
2. Check logs for high-token generations: `grep "tokens_used" logs/codegen.log | jq 'select(.tokens_used > 50000)'`
3. If Ollama costs high → investigate IR size or model misconfiguration
4. If Claude costs high → check fallback frequency (Ollama may be down)

---

## 16. Related Specifications

| Spec ID | Title | Relationship |
|---------|-------|--------------|
| **SPEC-0003** | ADR-007: AI Context Engine | Provider integration patterns |
| **SPEC-0004** | Policy Guards Design | Code validation integration |
| **SPEC-0009** | Codegen Service Specification | Implementation details |
| **SPEC-0010** | IR Processor Specification | IR schema definitions |

---

## 17. References

### Source Specifications
- **[SPEC-0003](./SPEC-0003-AI-Context-Engine-Architecture.md)** - AI Context Engine architecture patterns
- **[SPEC-0009](./SPEC-0009-Codegen-Service-Specification.md)** - Codegen Service implementation specification
- **[SPEC-0010](./SPEC-0010-IR-Processor-Specification.md)** - IR Processor specification

### External Standards
- Ollama API Documentation: Provider integration patterns
- OpenAI API Standard: Fallback provider interface

> **Implementation Reference**: For implementation details (sprint plans, epic breakdown, strategic decisions), see SDLC-Orchestrator documentation.

---

## 18. Document Control

| Field | Value |
|-------|-------|
| **Specification ID** | SPEC-0006 |
| **Version** | 1.0.0 |
| **Date Created** | January 29, 2026 |
| **Last Updated** | January 29, 2026 |
| **Author** | Backend Lead + Architect |
| **Approvals** | CTO ✅ (Dec 23, 2025), CEO ✅ (Dec 23, 2025) |
| **Framework Version** | SDLC 6.0.5 |
| **Status** | APPROVED |
| **Migration From** | ADR-022-Multi-Provider-Codegen-Architecture.md |

---

*SPEC-0006: Multi-Provider Codegen Architecture - Provider-agnostic IR-based code generation for Vietnam SME*
*Framework 6.0.5 Specification Format - BDD Requirements + Tier Classification*
*Sprint 117 Track 1 Day 3 - P1 Spec Migration*
