# SPEC-0009: Codegen Service Specification

## Frontmatter

```yaml
spec_id: SPEC-0009
title: Codegen Service Technical Specification - EP-06 Vietnamese SME Engine
version: 1.0.0
status: approved
tier: PROFESSIONAL
pillar: Pillar 4 - Build & Implementation
owner: Backend Lead + CTO
last_updated: 2026-02-03
tags:
  - codegen
  - ep-06
  - vietnamese-sme
  - ollama
related_specs:
  - SPEC-0006  # Multi-Provider Codegen
  - SPEC-0020  # Quality Gates Codegen
epic: EP-06 IR-Based Codegen Engine
sprint: Sprint 46-47
```

---

## Executive Summary

**Problem**: Vietnam SME founders need production-ready code generation without writing code themselves. Existing AI coding tools (Cursor, Claude Code) require programming expertise. SME founders need a **natural language → working software** pipeline optimized for Vietnamese business domains (F&B, E-commerce, HRM).

**Solution**: Implement **Codegen Service** with IR-based multi-provider architecture:
- **Provider-Agnostic Interface**: CodegenProvider contract enabling multiple AI providers
- **Multi-Provider Fallback**: Ollama (primary) → Claude (fallback) → DeepCode (future)
- **Vietnamese-Optimized**: Prompt templates in Vietnamese with SME business domain understanding
- **Cost-Optimized**: Ollama primary provider reduces cost 95% vs Claude-only ($0.005 vs $0.075 per request)

**Key Components**:
- **CodegenProvider Interface**: Abstract base class with `generate()`, `validate()`, `estimate_cost()` methods
- **ProviderRegistry**: Dynamic provider registration + automatic fallback routing
- **CodegenService**: Orchestrator coordinating providers + quality validation
- **4 API Endpoints**: `/providers`, `/generate`, `/validate`, `/estimate`
- **Ollama Integration**: Primary provider with qwen2.5-coder:14b model (<60s generation target)

**Business Value**:
- **Vietnam SME Wedge**: Enable non-technical founders to generate enterprise-grade code
- **95% Cost Reduction**: Ollama primary provider ($50/month vs $1,000+ for Claude-only)
- **<60s Generation Time**: Fast iteration cycle for SME founders
- **Production-Ready Output**: Zero Mock Policy enforcement - no placeholders, real implementations

**Success Criteria**:
- ✅ Ollama provider primary (is_available = true)
- ✅ Claude provider fallback (configurable with ANTHROPIC_API_KEY)
- ✅ 4 API endpoints functional (providers, generate, validate, estimate)
- ✅ Generation time <60s (p95)
- ✅ Integration test passes (Ollama-only boot test)
- ✅ Vietnamese prompt templates active

---

## 1. Functional Requirements

### FR-001: Provider Interface Contract (Abstract Base Class)

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN a codegen provider implementation (Ollama, Claude, or DeepCode)
WHEN the provider is registered with the Codegen Service
THEN the provider MUST implement the CodegenProvider abstract base class with:
- name property: Unique identifier (e.g., "ollama", "claude", "deepcode")
- is_available property: Boolean indicating provider health/configuration status
- generate() method: Async code generation from IR specification → CodegenResult
- validate() method: Async code validation with context → ValidationResult
- estimate_cost() method: Sync cost estimation without network calls → CostEstimate
```

**Implementation Details**:
```python
from abc import ABC, abstractmethod
from app.services.codegen.base_provider import CodegenSpec, CodegenResult, ValidationResult, CostEstimate

class CodegenProvider(ABC):
    """Abstract base class for all codegen providers.

    All providers MUST implement:
    - name property: Unique identifier
    - is_available property: Health check status
    - generate(): Code generation from IR
    - validate(): Code validation
    - estimate_cost(): Cost estimation
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Provider identifier (e.g., 'ollama', 'claude', 'deepcode')"""
        pass

    @property
    @abstractmethod
    def is_available(self) -> bool:
        """Returns True if provider is configured and reachable"""
        pass

    @abstractmethod
    async def generate(self, spec: CodegenSpec) -> CodegenResult:
        """Generate code from IR specification.

        Args:
            spec: CodegenSpec with app_blueprint, target_module, language, framework

        Returns:
            CodegenResult with generated files, provider name, tokens, timing

        Raises:
            ProviderUnavailableError: Provider not reachable
            GenerationError: Generation failed
            TimeoutError: Generation timed out (>60s)
        """
        pass

    @abstractmethod
    async def validate(self, code: str, context: Dict[str, Any]) -> ValidationResult:
        """Validate generated code against quality standards"""
        pass

    @abstractmethod
    def estimate_cost(self, spec: CodegenSpec) -> CostEstimate:
        """Estimate generation cost (sync, no network call)"""
        pass
```

**Rationale**: Provider contract ensures consistent interface across all AI providers (Ollama, Claude, DeepCode).

---

### FR-002: Provider Registry & Dynamic Routing

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN multiple registered codegen providers (Ollama, Claude, DeepCode)
WHEN a code generation request arrives with optional preferred_provider
THEN the ProviderRegistry MUST:
1. Return preferred provider if specified and available
2. Fall back to next available provider in fallback_chain if preferred unavailable
3. Iterate through fallback_chain until available provider found
4. Raise NoProviderAvailableError if ALL providers unavailable
5. Track fallback events in metrics (codegen_fallback_count_total)
```

**Provider Fallback Chain**:
```yaml
Default Fallback Chain: ["ollama", "claude", "deepcode"]

Selection Logic:
  1. If preferred_provider specified:
     - Check if preferred provider is_available
     - If available: Return preferred provider
     - If unavailable: Continue to fallback chain

  2. Iterate fallback_chain in order:
     - For each provider name in chain:
       - Get provider from registry
       - Check is_available property
       - If available: Return this provider

  3. If NO provider available:
     - Raise NoProviderAvailableError
     - Log critical alert
     - Return 503 Service Unavailable to client
```

**Implementation**:
```python
class ProviderRegistry:
    def __init__(self):
        self._providers: Dict[str, CodegenProvider] = {}
        self._fallback_chain: List[str] = ["ollama", "claude", "deepcode"]

    def register(self, provider: CodegenProvider) -> None:
        """Register a codegen provider"""
        self._providers[provider.name] = provider

    def select_provider(self, preferred: Optional[str] = None) -> Optional[CodegenProvider]:
        """Select best available provider based on preference and fallback chain"""
        # Try preferred provider first
        if preferred and preferred in self._providers:
            provider = self._providers[preferred]
            if provider.is_available:
                return provider

        # Try fallback chain
        for provider_name in self._fallback_chain:
            if provider_name in self._providers:
                provider = self._providers[provider_name]
                if provider.is_available:
                    return provider

        # No provider available
        return None
```

**Rationale**: Dynamic provider selection enables graceful degradation when primary provider (Ollama) is unavailable.

---

### FR-003: Multi-Provider Fallback with Retry Logic

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN a code generation request
WHEN the CodegenService processes the request
THEN the service MUST:
1. Select provider via ProviderRegistry (preferred or fallback)
2. Attempt generation with selected provider
3. On failure: Try next provider in fallback chain (max 3 attempts total)
4. On timeout (>60s): Try next provider in fallback chain
5. Return result from first successful provider
6. Log all retry attempts with provider names and error reasons
```

**Retry Strategy**:
```yaml
Max Attempts: 3 providers (Ollama → Claude → DeepCode)
Timeout Per Provider: 60 seconds
Retry On:
  - ProviderUnavailableError: Try next provider immediately
  - TimeoutError: Try next provider immediately
  - GenerationError: Try next provider immediately (but log details)

Do NOT Retry On:
  - Invalid input (400 Bad Request): Return error immediately
  - Authentication failure (401 Unauthorized): Return error immediately
  - Rate limit exceeded: Return 429 with retry-after header
```

**Metrics Tracking**:
- `codegen_fallback_count_total{from="ollama", to="claude"}`: Counter for fallback events
- `codegen_provider_failures_total{provider="ollama", reason="timeout"}`: Counter for failures

**Rationale**: Automatic fallback ensures 99.9% service availability even if primary provider (Ollama) is down.

---

### FR-004: Code Generation from IR Specification

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN a valid CodegenSpec with app_blueprint, language, framework
WHEN the CodegenService.generate() method is called
THEN the service MUST:
1. Select available provider via ProviderRegistry
2. Invoke provider.generate(spec) with timeout=60s
3. Parse provider response into GeneratedFile objects (path, content, language)
4. Validate generated files:
   - Python: ast.parse() syntax check
   - TypeScript: tsc --noEmit syntax check
   - No TODO/placeholder comments
5. Return CodegenResult with:
   - success: boolean (true if generation succeeded)
   - files: List[GeneratedFile] (all generated files)
   - provider: string (provider that generated the code)
   - tokens_used: int (total token count)
   - generation_time_ms: int (end-to-end latency)
   - metadata: dict (model name, prompt tokens, completion tokens)
```

**Validation Rules (Zero Mock Policy Enforcement)**:
```python
VALIDATION_RULES = {
    "no_placeholders": {
        "patterns": [r"# TODO", r"// TODO", r"PLACEHOLDER", r"FIXME"],
        "severity": "error",
        "message": "Generated code contains placeholders - violates Zero Mock Policy"
    },
    "syntax_valid": {
        "python": "ast.parse(code) must succeed",
        "typescript": "tsc --noEmit must pass",
        "severity": "error"
    },
    "imports_valid": {
        "check": "No import errors",
        "severity": "warning"
    }
}
```

**API Endpoint**: POST /api/v1/codegen/generate

**Request Example**:
```json
{
  "app_blueprint": {
    "name": "Restaurant Order System",
    "version": "1.0.0",
    "business_domain": "restaurant",
    "modules": [
      {
        "name": "orders",
        "entities": ["Order", "OrderItem"],
        "operations": ["create", "list", "update_status"]
      }
    ]
  },
  "language": "python",
  "framework": "fastapi",
  "preferred_provider": "ollama"
}
```

**Response Example**:
```json
{
  "success": true,
  "result": {
    "success": true,
    "files": [
      {
        "path": "app/models/order.py",
        "content": "from sqlalchemy import Column, Integer, String...",
        "language": "python"
      },
      {
        "path": "app/api/routes/orders.py",
        "content": "from fastapi import APIRouter...",
        "language": "python"
      }
    ],
    "provider": "ollama",
    "tokens_used": 2500,
    "generation_time_ms": 3200,
    "metadata": {
      "model": "qwen2.5-coder:14b",
      "prompt_tokens": 800,
      "completion_tokens": 1700
    }
  }
}
```

**Rationale**: IR-based generation ensures deterministic output from declarative specification.

---

### FR-005: Code Validation with Context

**Priority**: P1 (HIGH)

**Requirement**:
```gherkin
GIVEN generated code from a provider
WHEN the CodegenService.validate() method is called
THEN the service MUST:
1. Perform syntax validation (ast.parse for Python, tsc for TypeScript)
2. Check for security issues (eval, exec, os.system usage)
3. Validate imports are resolvable
4. Check for hardcoded secrets (regex scan for API keys, passwords)
5. Return ValidationResult with:
   - valid: boolean (overall validation passed)
   - issues: List[ValidationIssue] (severity, message, file, line, rule)
   - suggestions: List[str] (improvement recommendations)
```

**Validation Checks**:
```yaml
Security Checks:
  - SEC-001: No eval() or exec() usage
  - SEC-002: No os.system() or subprocess with shell=True
  - SEC-003: No hardcoded secrets (API keys, passwords)
  - SEC-004: SQL injection patterns (if using raw SQL)

Code Quality Checks:
  - CQ-001: Type hints present (Python 3.11+)
  - CQ-002: Docstrings for all public functions
  - CQ-003: Error handling present (try/except)
  - CQ-004: No print() statements (use logging)

Import Checks:
  - IMP-001: All imports resolvable
  - IMP-002: No circular imports
  - IMP-003: No wildcard imports (from x import *)
```

**API Endpoint**: POST /api/v1/codegen/validate

**Rationale**: Validation ensures generated code meets SDLC Orchestrator quality standards before deployment.

---

### FR-006: Cost Estimation Across Providers

**Priority**: P1 (HIGH)

**Requirement**:
```gherkin
GIVEN a CodegenSpec (app_blueprint, language, framework)
WHEN the CodegenService.estimate_cost() method is called
THEN the service MUST:
1. Call estimate_cost() on ALL available providers (Ollama, Claude)
2. Return estimates for each provider with:
   - provider: string (provider name)
   - estimated_tokens: int (based on app_blueprint size)
   - estimated_cost_usd: float (tokens × provider pricing)
   - confidence: float (0-1, estimation confidence level)
3. Enable users to compare costs before generation
4. Use token estimation formula: tokens ≈ app_blueprint_chars × 0.4
```

**Provider Pricing** (as of Jan 2026):
```yaml
Ollama:
  model: qwen2.5-coder:14b
  cost_per_1k_tokens: $0.001
  estimated_tokens: 5000 (typical SME app)
  estimated_cost: $0.005
  confidence: 0.8

Claude:
  model: claude-sonnet-3.5
  cost_per_1k_tokens: $0.015
  estimated_tokens: 5000
  estimated_cost: $0.075
  confidence: 0.7

DeepCode:
  model: deepcode-v1 (not yet available)
  cost: TBD (Q2 2026)
  confidence: 0.0
```

**API Endpoint**: POST /api/v1/codegen/estimate

**Cost Comparison Dashboard**:
- Display cost estimates side-by-side
- Highlight cheapest option (usually Ollama)
- Show cost savings vs most expensive option

**Rationale**: Cost transparency enables SME founders to make informed provider selection decisions.

---

### FR-007: Ollama Provider Implementation (Primary)

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the Ollama provider (api.nhatquangholding.com)
WHEN the OllamaCodegenProvider is initialized
THEN the provider MUST:
1. name property: Return "ollama"
2. is_available property: Check Ollama API reachability (GET /api/tags)
3. generate() method:
   - Format Vietnamese-optimized prompt template
   - POST to /api/generate with model=qwen2.5-coder:14b
   - Parse response into GeneratedFile objects
   - Extract tokens_used and generation_time_ms
   - Return CodegenResult
4. validate() method: Use Ollama for code review suggestions
5. estimate_cost() method: Return $0.001 per 1K tokens estimate
```

**Vietnamese Prompt Template**:
```python
VIETNAMESE_CODEGEN_PROMPT = """Bạn là một AI chuyên gia phát triển phần mềm cho doanh nghiệp SME Việt Nam.

## Yêu cầu
Dựa trên đặc tả IR (Intermediate Representation) sau, hãy tạo code {framework} hoàn chỉnh:

## App Blueprint
```json
{app_blueprint}
```

## Thông số
- Ngôn ngữ: {language}
- Framework: {framework}
- Module mục tiêu: {target_module}

## Quy tắc
1. Code phải production-ready, không có placeholder
2. Thêm comments tiếng Việt cho logic phức tạp
3. Tuân thủ chuẩn PEP8 (Python) hoặc ESLint (TypeScript)
4. Xử lý lỗi đầy đủ (try/except)
5. Thêm type hints cho tất cả functions

## Output Format
Trả về code theo format sau:

### FILE: path/to/file.py
```python
# code here
```

### FILE: path/to/another_file.py
```python
# code here
```

Hãy bắt đầu tạo code:
"""
```

**Configuration**:
```python
# backend/app/core/config.py
class Settings(BaseSettings):
    OLLAMA_API_URL: str = "https://api.nhatquangholding.com"
    OLLAMA_CODEGEN_MODEL: str = "qwen2.5-coder:14b"
    OLLAMA_TIMEOUT_SECONDS: int = 60
    OLLAMA_MAX_RETRIES: int = 3
```

**Rationale**: Ollama primary provider reduces costs 95% vs Claude ($0.005 vs $0.075) while maintaining quality.

---

### FR-008: Vietnamese Business Domain Optimization

**Priority**: P1 (HIGH)

**Requirement**:
```gherkin
GIVEN a CodegenSpec with business_domain field (e.g., "restaurant", "ecommerce", "hrm")
WHEN the Ollama provider generates code
THEN the prompt template MUST include Vietnamese business context:
1. Domain-specific terminology in Vietnamese (e.g., "đơn hàng" for orders)
2. Vietnamese comments for complex business logic
3. Vietnamese validation messages (e.g., "Email không hợp lệ")
4. Business rule examples relevant to Vietnam SME (e.g., VAT 10%, VND currency)
```

**Domain-Specific Enhancements**:
```yaml
Restaurant Domain:
  - Comments: "Tính tổng tiền đơn hàng (bao gồm VAT 10%)"
  - Validation: "Số lượng món phải lớn hơn 0"
  - Currency: VND (₫) instead of USD ($)
  - Date Format: dd/MM/yyyy (Vietnamese standard)

E-commerce Domain:
  - Comments: "Kiểm tra tồn kho trước khi tạo đơn"
  - Validation: "Sản phẩm đã hết hàng"
  - Payment Methods: Momo, ZaloPay, VNPay (Vietnam)

HRM Domain:
  - Comments: "Tính lương theo quy định Luật Lao động VN"
  - Validation: "Mã nhân viên phải đúng format NV-XXXX"
  - Benefits: Social insurance (BHXH), health insurance (BHYT)
```

**Rationale**: Vietnamese business context reduces post-generation editing for SME founders.

---

## 2. Technical Requirements

### TR-001: API Endpoints Implementation

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the Codegen Service API layer
WHEN implementing API endpoints
THEN the service MUST provide 4 REST endpoints:
1. GET /api/v1/codegen/providers - List available providers
2. POST /api/v1/codegen/generate - Generate code from IR
3. POST /api/v1/codegen/validate - Validate generated code
4. POST /api/v1/codegen/estimate - Estimate generation cost
```

**Endpoint Specifications**:

**1. GET /api/v1/codegen/providers**
```yaml
Description: List all registered codegen providers with availability status
Authentication: JWT required
Response (200 OK):
  {
    "providers": [
      {"name": "ollama", "available": true, "primary": true, "status": "healthy"},
      {"name": "claude", "available": false, "primary": false, "status": "not_configured"}
    ],
    "fallback_chain": ["ollama", "claude", "deepcode"]
  }
```

**2. POST /api/v1/codegen/generate**
```yaml
Description: Generate code from IR specification
Authentication: JWT required
Rate Limit: 10 requests/minute per user
Timeout: 60 seconds
Request Body:
  {
    "app_blueprint": {...},  # IR specification
    "language": "python",
    "framework": "fastapi",
    "preferred_provider": "ollama"  # optional
  }
Response (200 OK):
  {
    "success": true,
    "result": {
      "files": [{...}],
      "provider": "ollama",
      "tokens_used": 2500,
      "generation_time_ms": 3200
    }
  }
Error (503 Service Unavailable):
  {
    "success": false,
    "error": "No codegen providers available"
  }
```

**3. POST /api/v1/codegen/validate**
```yaml
Description: Validate generated code
Authentication: JWT required
Request Body:
  {
    "code": "...",
    "context": {"language": "python", "framework": "fastapi"}
  }
Response (200 OK):
  {
    "success": true,
    "result": {
      "valid": true,
      "issues": [{...}],
      "suggestions": ["..."]
    }
  }
```

**4. POST /api/v1/codegen/estimate**
```yaml
Description: Estimate generation cost across providers
Authentication: JWT required
Response (200 OK):
  {
    "estimates": {
      "ollama": {"estimated_tokens": 5000, "estimated_cost_usd": 0.005},
      "claude": {"estimated_tokens": 5000, "estimated_cost_usd": 0.075}
    }
  }
```

**File Location**: `backend/app/api/routes/codegen.py`

**Rationale**: RESTful API design enables integration with frontend and external tools.

---

### TR-002: Pydantic Data Models

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the Codegen Service data layer
WHEN defining request/response schemas
THEN the service MUST use Pydantic models with:
1. Type hints for all fields
2. Field validation (min/max length, regex patterns)
3. JSON schema examples for OpenAPI documentation
4. Enums for constrained values (CodegenLanguage, CodegenFramework)
```

**Core Models** (backend/app/services/codegen/base_provider.py):
```python
from pydantic import BaseModel, Field
from enum import Enum

class CodegenLanguage(str, Enum):
    PYTHON = "python"
    TYPESCRIPT = "typescript"
    JAVASCRIPT = "javascript"

class CodegenFramework(str, Enum):
    FASTAPI = "fastapi"
    FLASK = "flask"
    NEXTJS = "nextjs"
    REACT = "react"

class CodegenSpec(BaseModel):
    """Input specification for code generation"""
    app_blueprint: Dict[str, Any] = Field(..., description="AppBlueprint from IR schema")
    target_module: Optional[str] = Field(None, description="Specific module to generate")
    language: CodegenLanguage = Field(CodegenLanguage.PYTHON)
    framework: CodegenFramework = Field(CodegenFramework.FASTAPI)

class GeneratedFile(BaseModel):
    """Single generated file"""
    path: str = Field(..., description="Relative file path")
    content: str = Field(..., description="File content")
    language: str = Field(..., description="File language/type")

class CodegenResult(BaseModel):
    """Output from code generation"""
    success: bool
    files: List[GeneratedFile] = Field(default_factory=list)
    provider: str
    tokens_used: int = 0
    generation_time_ms: int = 0
    metadata: Dict[str, Any] = Field(default_factory=dict)

class ValidationIssue(BaseModel):
    """Single validation issue"""
    severity: str  # "error", "warning", "info"
    message: str
    file: Optional[str] = None
    line: Optional[int] = None
    rule: Optional[str] = None

class ValidationResult(BaseModel):
    """Output from code validation"""
    valid: bool
    issues: List[ValidationIssue] = Field(default_factory=list)
    suggestions: List[str] = Field(default_factory=list)

class CostEstimate(BaseModel):
    """Cost estimation for generation"""
    provider: str
    estimated_tokens: int
    estimated_cost_usd: float
    confidence: float = Field(..., ge=0.0, le=1.0)
```

**Rationale**: Pydantic models provide type safety, validation, and automatic OpenAPI schema generation.

---

### TR-003: Configuration Management

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the Codegen Service configuration
WHEN loading settings from environment variables
THEN the service MUST read:
1. OLLAMA_API_URL: Ollama server URL (default: https://api.nhatquangholding.com)
2. OLLAMA_CODEGEN_MODEL: Model name (default: qwen2.5-coder:14b)
3. OLLAMA_TIMEOUT_SECONDS: Request timeout (default: 60)
4. OLLAMA_MAX_RETRIES: Retry attempts (default: 3)
5. ANTHROPIC_API_KEY: Claude API key (optional, for fallback)
6. CODEGEN_DEFAULT_PROVIDER: Default provider (default: ollama)
7. CODEGEN_FALLBACK_CHAIN: Comma-separated provider list (default: ollama,claude,deepcode)
```

**Configuration File** (backend/app/core/config.py):
```python
from pydantic import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    # ... existing settings ...

    # Codegen - Ollama (Primary)
    OLLAMA_API_URL: str = "https://api.nhatquangholding.com"
    OLLAMA_CODEGEN_MODEL: str = "qwen2.5-coder:14b"
    OLLAMA_TIMEOUT_SECONDS: int = 60
    OLLAMA_MAX_RETRIES: int = 3

    # Codegen - Claude (Fallback)
    ANTHROPIC_API_KEY: Optional[str] = None

    # Codegen - Service Config
    CODEGEN_DEFAULT_PROVIDER: str = "ollama"
    CODEGEN_FALLBACK_CHAIN: List[str] = ["ollama", "claude", "deepcode"]
    CODEGEN_MAX_GENERATION_TIME_MS: int = 60000

    class Config:
        env_file = ".env"
```

**Environment File** (.env.example):
```bash
# Codegen - Ollama (Primary)
OLLAMA_API_URL=https://api.nhatquangholding.com
OLLAMA_CODEGEN_MODEL=qwen2.5-coder:14b
OLLAMA_TIMEOUT_SECONDS=60
OLLAMA_MAX_RETRIES=3

# Codegen - Claude (Fallback, optional)
ANTHROPIC_API_KEY=  # Leave empty to disable

# Codegen - Service Config
CODEGEN_DEFAULT_PROVIDER=ollama
CODEGEN_FALLBACK_CHAIN=ollama,claude,deepcode
CODEGEN_MAX_GENERATION_TIME_MS=60000
```

**Rationale**: Environment-based configuration enables easy deployment across dev/staging/production.

---

### TR-004: Error Handling & Custom Exceptions

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the Codegen Service error handling
WHEN errors occur during generation
THEN the service MUST define custom exceptions:
1. CodegenError: Base exception for all codegen errors
2. ProviderUnavailableError: Provider not configured or unreachable
3. NoProviderAvailableError: All providers unavailable
4. GenerationError: Code generation failed
5. GenerationTimeoutError: Generation exceeded timeout
6. ValidationError: Code validation failed
```

**Custom Exceptions** (backend/app/services/codegen/exceptions.py):
```python
class CodegenError(Exception):
    """Base exception for codegen errors"""
    pass

class ProviderUnavailableError(CodegenError):
    """Provider is not configured or not reachable"""
    def __init__(self, provider: str, reason: str = ""):
        self.provider = provider
        self.reason = reason
        super().__init__(f"Provider {provider} unavailable: {reason}")

class NoProviderAvailableError(CodegenError):
    """No providers are available in the fallback chain"""
    pass

class GenerationError(CodegenError):
    """Code generation failed"""
    def __init__(self, provider: str, message: str):
        self.provider = provider
        super().__init__(f"Generation failed ({provider}): {message}")

class GenerationTimeoutError(CodegenError):
    """Code generation timed out"""
    def __init__(self, provider: str, timeout_ms: int):
        self.provider = provider
        self.timeout_ms = timeout_ms
        super().__init__(f"Generation timed out ({provider}): {timeout_ms}ms")

class ValidationError(CodegenError):
    """Code validation failed"""
    pass
```

**Error Response Format** (JSON):
```json
{
  "success": false,
  "error": "Provider ollama unavailable: connection timeout",
  "error_code": "PROVIDER_UNAVAILABLE",
  "provider": "ollama",
  "retry_available": true,
  "retry_provider": "claude"
}
```

**Rationale**: Custom exceptions enable precise error handling and informative error messages to clients.

---

### TR-005: Logging & Monitoring Metrics

**Priority**: P1 (HIGH)

**Requirement**:
```gherkin
GIVEN the Codegen Service operations
WHEN processing generation requests
THEN the service MUST log structured events and emit Prometheus metrics:

Metrics:
1. codegen_requests_total{provider, status}: Counter for total requests
2. codegen_generation_duration_ms{provider}: Histogram for latency
3. codegen_tokens_used_total{provider}: Counter for token consumption
4. codegen_provider_availability{provider}: Gauge for provider health (1/0)
5. codegen_fallback_count_total{from, to}: Counter for fallback events

Logs:
- Event: generation_start, generation_complete, generation_failed
- Fields: timestamp, level, service, event, provider, tokens, duration_ms, user_id, project_id, trace_id
```

**Structured Logging Format**:
```json
{
  "timestamp": "2026-01-30T10:30:00Z",
  "level": "INFO",
  "service": "codegen",
  "event": "generation_complete",
  "provider": "ollama",
  "tokens": 2500,
  "duration_ms": 3200,
  "user_id": "uuid-here",
  "project_id": "uuid-here",
  "trace_id": "abc123",
  "model": "qwen2.5-coder:14b"
}
```

**Alert Rules**:
```yaml
Alerts:
  - Alert: CodegenNoProviderAvailable
    Condition: All providers unavailable for 5min
    Severity: Critical

  - Alert: CodegenHighLatency
    Condition: p95 latency > 30s for 10min
    Severity: Warning

  - Alert: CodegenHighErrorRate
    Condition: Error rate > 10% for 5min
    Severity: Warning
```

**Rationale**: Observability enables proactive monitoring and incident detection.

---

## 3. Quality Requirements

### QR-001: Performance - Generation Latency

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN a code generation request
WHEN the CodegenService processes the request
THEN the service MUST meet performance targets:
- Generation time (p95): <60 seconds (Ollama primary)
- Generation time (p99): <90 seconds
- API response time: <100ms for /providers endpoint
- Cost estimation time: <50ms (no network calls)
```

**Performance Budget**:
```yaml
Ollama Generation:
  p50: <15s
  p95: <60s (HARD REQUIREMENT)
  p99: <90s
  timeout: 60s

Claude Generation (Fallback):
  p50: <10s
  p95: <25s
  p99: <40s
  timeout: 30s

API Endpoints:
  /providers: <100ms (p95)
  /estimate: <50ms (sync, no network)
  /validate: <2s (depends on code size)
```

**Optimization Strategies**:
- Ollama connection pooling (reuse HTTP connections)
- Prompt caching (cache IR → prompt transformation)
- Response streaming (return files as generated)
- Async execution (non-blocking provider calls)

**Benchmarking**:
```python
# pytest-benchmark
def test_generation_performance(benchmark):
    result = benchmark(codegen_service.generate, test_spec)
    assert result.generation_time_ms < 60000  # <60s
```

**Rationale**: <60s generation enables fast iteration for SME founders.

---

### QR-002: Availability - Multi-Provider Resilience

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the multi-provider architecture
WHEN Ollama primary provider is unavailable
THEN the service MUST:
1. Detect Ollama unavailability within 5 seconds (health check timeout)
2. Automatically fall back to Claude provider
3. Maintain service availability >= 99.9% (excluding all-provider outages)
4. Return generation within 90s (Ollama 60s + Claude 30s fallback)
```

**Availability Targets**:
```yaml
Service Level Objectives (SLOs):
  Availability: 99.9% (8.76h downtime/year)
  Error Budget: 43 minutes/month

Provider-Specific Availability:
  Ollama: 99.5% (primary, self-hosted)
  Claude: 99.9% (Anthropic SLA)
  Multi-Provider Combined: 99.99% (2 providers)
```

**Health Check Strategy**:
```python
async def check_ollama_health() -> bool:
    """Check if Ollama is reachable and healthy"""
    try:
        response = await httpx.get(
            f"{OLLAMA_API_URL}/api/tags",
            timeout=5.0
        )
        return response.status_code == 200
    except (httpx.TimeoutException, httpx.ConnectError):
        return False
```

**Fallback Decision Logic**:
```
if ollama.is_available:
    use ollama  # Primary path (95% of requests)
elif claude.is_available:
    use claude  # Fallback path (4% of requests)
else:
    return 503 Service Unavailable  # <1% of requests
```

**Rationale**: Multi-provider architecture ensures Vietnam SME users always have access to code generation.

---

### QR-003: Security - Input/Output Validation

**Priority**: P0 (CRITICAL)

**Requirement**:
```gherkin
GIVEN the Codegen Service security requirements
WHEN processing user inputs and generating code
THEN the service MUST:

Input Validation:
1. Validate app_blueprint against JSON schema (max 100KB size)
2. Sanitize all string inputs (prevent injection attacks)
3. Rate limit: 10 generation requests per minute per user
4. JWT authentication required for all endpoints

Output Validation:
5. Scan generated code for hardcoded secrets (regex: /api[_-]?key|password|secret/i)
6. Detect malicious patterns: eval(), exec(), os.system(), subprocess with shell=True
7. Validate generated code doesn't contain shell commands
8. Log all generation requests with user context for audit trail
```

**Security Checks**:
```python
SECURITY_PATTERNS = [
    r"eval\s*\(",              # eval() usage
    r"exec\s*\(",              # exec() usage
    r"os\.system\s*\(",        # os.system() usage
    r"subprocess.*shell=True", # subprocess with shell=True
    r"api[_-]?key\s*=",       # Hardcoded API key
    r"password\s*=",           # Hardcoded password
    r"secret\s*=",             # Hardcoded secret
]

def scan_for_security_issues(code: str) -> List[ValidationIssue]:
    """Scan generated code for security issues"""
    issues = []
    for pattern in SECURITY_PATTERNS:
        matches = re.finditer(pattern, code, re.IGNORECASE)
        for match in matches:
            issues.append(ValidationIssue(
                severity="error",
                message=f"Security issue detected: {pattern}",
                line=code[:match.start()].count('\n') + 1,
                rule="SEC-001"
            ))
    return issues
```

**Authentication**:
- All endpoints require JWT token (X-Auth-Token header)
- Token validation via auth middleware
- Unauthorized access returns 401 Unauthorized

**Rate Limiting**:
```yaml
Per User:
  /generate: 10 requests/minute
  /validate: 20 requests/minute
  /estimate: 50 requests/minute
  /providers: 100 requests/minute

Per IP (Anonymous):
  All endpoints: 5 requests/minute
```

**Rationale**: Security validation prevents malicious code generation and protects user data.

---

## 4. Tier-Specific Requirements

### TSR-001: PROFESSIONAL Tier - Ollama Primary Provider

**Applicable Tier**: PROFESSIONAL

**Requirement**:
```gherkin
GIVEN a project on PROFESSIONAL tier
WHEN generating code
THEN the system MUST:
- Use Ollama as primary provider (95% of requests)
- Fall back to Claude if Ollama unavailable
- Track provider usage in metrics dashboard
- Allow 10 generation requests per minute per user
```

**Rationale**: PROFESSIONAL tier gets cost-optimized Ollama access (95% cost savings).

---

### TSR-002: ENTERPRISE Tier - Claude Fallback Enabled

**Applicable Tier**: ENTERPRISE

**Requirement**:
```gherkin
GIVEN a project on ENTERPRISE tier
WHEN Ollama provider is unavailable
THEN the system MUST:
- Automatically fall back to Claude provider (zero manual intervention)
- Guarantee 99.9% service availability (multi-provider SLA)
- Allow 50 generation requests per minute per user (5x PROFESSIONAL)
- Provide priority queue for generation requests
```

**Priority Queue**:
- ENTERPRISE requests: Priority 1 (processed first)
- PROFESSIONAL requests: Priority 2
- LITE requests: Priority 3 (best-effort)

**Rationale**: ENTERPRISE tier gets highest reliability with Claude fallback and priority processing.

---

## 5. Acceptance Criteria

| ID | Criterion | Test Method | PRO | ENT |
|----|-----------|-------------|-----|-----|
| AC-001 | Ollama provider primary (is_available = true) | Integration test (Ollama health check) | ✅ | ✅ |
| AC-002 | Claude provider fallback (configurable) | Unit test (ANTHROPIC_API_KEY set → available) | ✅ | ✅ |
| AC-003 | 4 API endpoints functional | E2E test (call all 4 endpoints, verify responses) | ✅ | ✅ |
| AC-004 | Generation time <60s (p95) | Load test (100 concurrent requests, measure p95) | ✅ | ✅ |
| AC-005 | Vietnamese prompt templates active | Integration test (check prompt contains Vietnamese) | ✅ | ✅ |
| AC-006 | Zero Mock Policy enforcement | Unit test (scan generated code for TODO/PLACEHOLDER) | ✅ | ✅ |
| AC-007 | Multi-provider fallback works | Integration test (mock Ollama down, verify Claude used) | ✅ | ✅ |
| AC-008 | Cost estimation accurate within 20% | Unit test (compare estimated vs actual tokens) | ✅ | ✅ |
| AC-009 | Security validation blocks malicious code | Unit test (generate code with eval(), verify blocked) | ✅ | ✅ |
| AC-010 | Rate limiting enforced | E2E test (send 11 requests/min, verify 11th blocked) | ✅ | ✅ |
| AC-011 | Metrics emitted correctly | Integration test (verify Prometheus metrics exist) | ✅ | ✅ |
| AC-012 | Smoke test passes (Ollama-only boot) | Shell script (smoke_test_codegen.sh passes) | ✅ | ✅ |

**Total**: 12 acceptance criteria (100% coverage for PROFESSIONAL and ENTERPRISE tiers)

---

## 6. Cross-References

### Related Specifications
- **[SPEC-0006](./SPEC-0006-Multi-Provider-Codegen-Architecture.md)**: Multi-provider architecture design (ADR-022)
- **[SPEC-0010](./SPEC-0010-IR-Processor-Specification.md)**: IR Processor Specification (transforms app_blueprint → IR)
- **[SPEC-0011](./SPEC-0011-AI-Task-Decomposition.md)**: AI Task Decomposition (pre-generation planning)
- **[SPEC-0012](./SPEC-0012-Validation-Pipeline-Interface.md)**: Validation Pipeline Interface (4-Gate quality checks)

### Framework Documents
- **SDLC 5.1.3 - Section 04-BUILD**: Build & Implementation guidelines
- **SDLC 5.3.0 - Section 7**: Quality Assurance System (Zero Mock Policy)

### Implementation Files
- `backend/app/services/codegen/base_provider.py`: CodegenProvider abstract base class
- `backend/app/services/codegen/provider_registry.py`: ProviderRegistry + routing logic
- `backend/app/services/codegen/codegen_service.py`: CodegenService orchestrator
- `backend/app/services/codegen/ollama_provider.py`: OllamaCodegenProvider implementation
- `backend/app/api/routes/codegen.py`: API endpoints (4 endpoints)
- `backend/app/schemas/codegen.py`: Request/Response Pydantic schemas

---

## 7. Dependencies

### Upstream Dependencies (Must Exist Before Implementation)
- ✅ **FastAPI Framework**: API endpoint framework
- ✅ **Pydantic v2**: Data validation and schemas
- ✅ **Ollama API Access**: api.nhatquangholding.com reachable
- ✅ **JWT Authentication**: Auth middleware for endpoint security
- ⏳ **IR Schema**: app_blueprint JSON schema (Sprint 46 - SPEC-0010)

### Downstream Dependencies (Blocked Until This Spec Completes)
- ⏳ **IR Processor Service**: Transforms high-level spec → app_blueprint (SPEC-0010)
- ⏳ **4-Gate Quality Pipeline**: Validates generated code (SPEC-0012)
- ⏳ **Frontend Codegen UI**: User interface for code generation
- ⏳ **Vietnamese Domain Templates**: F&B, E-commerce, HRM templates (Sprint 47)

---

## 8. Related Standards

### Industry Standards
- **OpenAPI 3.0**: API specification format (auto-generated from FastAPI)
- **JSON Schema**: app_blueprint validation standard
- **Prometheus Metrics**: Observability metrics format
- **OWASP Top 10**: Security validation rules (SQL injection, XSS, eval() prevention)

### Internal Standards
- **Zero Mock Policy**: All generated code production-ready (no placeholders)
- **Contract-First API Design**: OpenAPI schema drives implementation
- **Multi-Provider Architecture**: ADR-022 design pattern
- **Performance Budget**: <60s generation (p95), <100ms API latency (p95)

---

## 9. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-01-30 | Backend Lead + Architect | Initial Framework 6.0.2 migration from Codegen Service Specification |

---

## 10. Approval

| Role | Name | Status | Date | Signature |
|------|------|--------|------|-----------|
| **CEO** | [CEO Name] | ✅ APPROVED | 2025-12-23 | [Digital Signature] |
| **CTO** | [CTO Name] | ✅ APPROVED | 2025-12-23 | [Digital Signature] |
| **Backend Lead** | [Backend Lead Name] | ✅ APPROVED | 2025-12-23 | [Digital Signature] |

---

**Document Status**: ✅ APPROVED - Ready for Implementation (Sprint 45 - Jan 6-17, 2026)
**Framework Compliance**: ✅ Framework 6.0.2 (YAML frontmatter, BDD requirements, tier-specific tables)
**Spec Migration**: ✅ Complete (Codegen Service Specification → SPEC-0009)

---

*SPEC-0009 - Codegen Service. IR-based multi-provider code generation for Vietnam SME. Zero Mock Policy compliant. Framework-First methodology.*
