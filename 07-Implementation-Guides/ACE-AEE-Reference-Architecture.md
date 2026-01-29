# ACE-AEE Reference Architecture
## Agent Command Environment & Agent Execution Environment

**Reference:** arXiv:2509.06216v2 - Software Agentic Software Engineering (SASE)

**Purpose:** Define the dual workbench architecture for human-agent collaboration
**Framework:** SDLC 6.0.0 (7-Pillar + Section 7 Quality Assurance System)
**Version:** 1.1.0
**Created:** December 2025
**Updated:** January 29, 2026
**Status:** ACTIVE - PRODUCTION READY
**AI Governance:** Aligned with [03-AI-GOVERNANCE/](../03-AI-GOVERNANCE/) principles

---

## 📋 DOCUMENT OVERVIEW

This document defines the reference architecture for the two complementary environments in SASE:

| Environment | Acronym | Primary User | Purpose |
|-------------|---------|--------------|---------|
| **Agent Command Environment** | ACE | SE4H (Human) | Command, monitor, and review agent work |
| **Agent Execution Environment** | AEE | SE4A (Agent) | Execute tasks in isolated, secure sandbox |

**Key Principle:** ACE and AEE are separated to ensure security, auditability, and clear responsibility boundaries.

---

## 🏗️ ARCHITECTURAL OVERVIEW

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           USER LAYER (SE4H)                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   Web Dashboard  │  │  VS Code Ext    │  │   CLI (sdlcctl) │             │
│  │   (React)        │  │  (TypeScript)   │  │   (Python)      │             │
│  └────────┬─────────┘  └────────┬────────┘  └────────┬────────┘             │
└───────────┼──────────────────────┼───────────────────┼──────────────────────┘
            │                      │                   │
            └──────────────────────┼───────────────────┘
                                   │
┌──────────────────────────────────┼──────────────────────────────────────────┐
│                    ACE - AGENT COMMAND ENVIRONMENT                          │
│  ┌───────────────────────────────┴───────────────────────────────┐          │
│  │                      ACE Gateway (FastAPI)                     │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │          │
│  │  │ Auth Service │  │ BRS Manager │  │ VCR Reviewer│            │          │
│  │  │ (JWT/OAuth)  │  │ (Create/Edit)│  │ (Approve)   │            │          │
│  │  └─────────────┘  └─────────────┘  └─────────────┘            │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │          │
│  │  │ Agent Monitor│  │ CRP Handler │  │ MRP Reviewer│            │          │
│  │  │ (Status)     │  │ (Respond)   │  │ (Verify)    │            │          │
│  │  └─────────────┘  └─────────────┘  └─────────────┘            │          │
│  └───────────────────────────────┬───────────────────────────────┘          │
└──────────────────────────────────┼──────────────────────────────────────────┘
                                   │
                          ┌────────┴────────┐
                          │  Message Queue   │
                          │  (Redis/RabbitMQ)│
                          └────────┬────────┘
                                   │
┌──────────────────────────────────┼──────────────────────────────────────────┐
│                    AEE - AGENT EXECUTION ENVIRONMENT                        │
│  ┌───────────────────────────────┴───────────────────────────────┐          │
│  │                    AEE Orchestrator (Python)                   │          │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │          │
│  │  │ Task Scheduler│ │ LPS Engine  │  │ MRP Generator│           │          │
│  │  │ (Queue)      │  │ (Execute)   │  │ (Produce)   │            │          │
│  │  └─────────────┘  └─────────────┘  └─────────────┘            │          │
│  └───────────────────────────────┬───────────────────────────────┘          │
│                                  │                                          │
│  ┌───────────────────────────────┴───────────────────────────────┐          │
│  │                      SANDBOX LAYER                             │          │
│  │  ┌──────────────────────────────────────────────────────────┐ │          │
│  │  │                   Docker Container                        │ │          │
│  │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │ │          │
│  │  │  │ AI Provider │  │ Code Executor│  │ Test Runner │       │ │          │
│  │  │  │ (Ollama/    │  │ (Isolated)  │  │ (pytest)    │       │ │          │
│  │  │  │  Claude)    │  │             │  │             │       │ │          │
│  │  │  └─────────────┘  └─────────────┘  └─────────────┘       │ │          │
│  │  └──────────────────────────────────────────────────────────┘ │          │
│  └───────────────────────────────────────────────────────────────┘          │
└─────────────────────────────────────────────────────────────────────────────┘
                                   │
┌──────────────────────────────────┼──────────────────────────────────────────┐
│                         SHARED SERVICES                                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │ Evidence    │  │ Policy      │  │ Observability│  │ Secret      │         │
│  │ Vault       │  │ Engine      │  │ Stack        │  │ Redaction   │         │
│  │ (MinIO)     │  │ (OPA)       │  │ (Prometheus) │  │ Service     │         │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🎮 ACE - AGENT COMMAND ENVIRONMENT

### Purpose

ACE is the **human-facing interface** where SE4H (Agent Coach) performs:
- Create and manage BriefingScripts (BRS)
- Monitor agent execution progress
- Respond to Consultation Request Protocols (CRP)
- Review Merge-Readiness Packs (MRP)
- Issue Version Controlled Resolutions (VCR)

### ACE Components

#### 1. ACE Gateway (FastAPI)

```yaml
Component: ACE Gateway
Technology: FastAPI + Python 3.11+
Purpose: Central API for all human interactions

Endpoints:
  Authentication:
    - POST /auth/login
    - POST /auth/refresh
    - POST /auth/logout

  BriefingScript Management:
    - POST /brs                    # Create new BRS
    - GET /brs/{id}               # Get BRS details
    - PUT /brs/{id}               # Update BRS
    - POST /brs/{id}/submit       # Submit BRS for execution

  Agent Monitoring:
    - GET /agents                 # List active agents
    - GET /agents/{id}/status     # Get agent status
    - GET /lps/{id}/progress      # Get LoopScript progress
    - POST /lps/{id}/pause        # Pause execution
    - POST /lps/{id}/resume       # Resume execution

  CRP Handling:
    - GET /crp                    # List pending CRPs
    - GET /crp/{id}              # Get CRP details
    - POST /crp/{id}/respond     # Respond to CRP

  MRP Review:
    - GET /mrp                    # List pending MRPs
    - GET /mrp/{id}              # Get MRP details
    - POST /mrp/{id}/verify      # Verify MRP evidence

  VCR Decisions:
    - POST /vcr                   # Create VCR decision
    - GET /vcr/{id}              # Get VCR details
```

#### 2. Web Dashboard (React)

```yaml
Component: Web Dashboard
Technology: React 18 + TypeScript + shadcn/ui
Purpose: Visual interface for ACE operations

Pages:
  /dashboard:
    - Active projects overview
    - Agent status summary
    - Pending CRP/MRP alerts

  /brs:
    - BRS creation wizard
    - Template library
    - BRS history

  /agents:
    - Agent grid view
    - Real-time status updates
    - Execution logs

  /review:
    - CRP inbox
    - MRP review queue
    - VCR history

Features:
  - Real-time updates (WebSocket)
  - Drag-and-drop BRS editor
  - Side-by-side MRP comparison
  - Inline CRP response
```

#### 3. VS Code Extension

```yaml
Component: VS Code Extension
Technology: TypeScript + VS Code API
Purpose: IDE-integrated ACE access

Features:
  - BRS creation from selection
  - Agent status in sidebar
  - CRP notifications
  - Quick VCR approval
  - Evidence submission (Cmd+Shift+E)

Commands:
  - sdlc.createBRS         # Create BRS from context
  - sdlc.viewAgentStatus   # Show agent panel
  - sdlc.respondToCRP      # Open CRP response
  - sdlc.approveVCR        # Quick approve VCR
```

#### 4. CLI (sdlcctl)

```yaml
Component: sdlcctl CLI
Technology: Python + Typer
Purpose: Command-line ACE access

Commands:
  # BRS Management
  sdlcctl brs create --template <name>
  sdlcctl brs submit <brs-id>
  sdlcctl brs list --status pending

  # Agent Monitoring
  sdlcctl agent status
  sdlcctl agent logs <agent-id>
  sdlcctl lps progress <lps-id>

  # CRP/MRP/VCR
  sdlcctl crp list
  sdlcctl crp respond <crp-id> --message "..."
  sdlcctl mrp review <mrp-id>
  sdlcctl vcr approve <mrp-id> --comment "..."
```

### ACE Security Model

```yaml
Authentication:
  Primary: JWT tokens (15min access, 7d refresh)
  SSO: OAuth 2.0 (GitHub, Google, Microsoft)
  MFA: TOTP (Google Authenticator)

Authorization (RBAC):
  Owner:
    - Full project access
    - Delete projects
    - Manage team members

  Admin:
    - Create/edit BRS
    - Approve VCR
    - Manage agents

  PM/PO:
    - Create/edit BRS
    - Respond to CRP
    - Review MRP (cannot approve VCR)

  Developer:
    - View BRS
    - View agent status
    - Submit evidence

  Viewer:
    - Read-only access
    - View dashboards

Row-Level Security:
  - Users see only their team's projects
  - Cross-team access requires explicit grant
  - Audit log for all access

Session Management:
  - Single active session per user (configurable)
  - Session invalidation on password change
  - Idle timeout: 30 minutes
```

---

## 🤖 AEE - AGENT EXECUTION ENVIRONMENT

### Purpose

AEE is the **agent-facing environment** where SE4A (Agent Executor) performs:
- Parse and execute LoopScripts (LPS)
- Generate code in isolated sandbox
- Run tests and validations
- Produce Merge-Readiness Packs (MRP)
- Request human guidance via CRP

### AEE Components

#### 1. AEE Orchestrator

```yaml
Component: AEE Orchestrator
Technology: Python 3.11+ + asyncio
Purpose: Coordinate agent task execution

Responsibilities:
  Task Scheduling:
    - Queue management (FIFO with priority)
    - Concurrent execution limits
    - Resource allocation

  LPS Execution:
    - Parse LPS YAML structure
    - Execute steps sequentially
    - Handle checkpoints (pause for SE4H)
    - Track iterations

  Agent Coordination:
    - Multi-agent parallel execution
    - Agent switching (Ollama → Claude → GPT-4)
    - Fallback handling

  Output Collection:
    - Aggregate step outputs
    - Generate MRP artifacts
    - Upload to Evidence Vault
```

#### 2. AI Provider Adapter

```yaml
Component: AI Provider Adapter
Technology: Python + httpx (async)
Purpose: Unified interface to AI providers

Supported Providers:
  Primary: Ollama (local, cost-effective)
    - Endpoint: http://api.nqh.vn/ollama
    - Models: qwen2.5:14b, llama3.1:70b
    - Latency: <100ms (local)
    - Cost: ~$50/month

  Fallback 1: Claude (Anthropic)
    - Endpoint: https://api.anthropic.com
    - Models: claude-3-opus, claude-3-sonnet
    - Latency: ~300ms
    - Cost: ~$1000/month

  Fallback 2: GPT-4 (OpenAI)
    - Endpoint: https://api.openai.com
    - Models: gpt-4o, gpt-4-turbo
    - Latency: ~250ms
    - Cost: ~$800/month

  Fallback 3: Rule-based
    - No external API
    - Template-based responses
    - Cost: $0

Fallback Strategy:
  - Try Ollama first (95% of requests)
  - If timeout/error → Claude
  - If Claude fails → GPT-4
  - If all fail → Rule-based + CRP
```

#### 3. Sandbox Executor

```yaml
Component: Sandbox Executor
Technology: Docker + Python
Purpose: Isolated code execution environment

Container Specification:
  Base Image: python:3.11-slim
  Memory Limit: 128MB (configurable)
  CPU Limit: 1 core
  Timeout: 30 seconds (configurable)
  Network: Disabled (isolated)
  Filesystem: Read-only (except /tmp)

Security Measures:
  - No root access (run as non-root user)
  - No network access (air-gapped)
  - Resource limits enforced
  - Automatic cleanup after execution
  - No persistent storage

Execution Flow:
  1. Create container from base image
  2. Mount code files (read-only)
  3. Execute command with timeout
  4. Capture stdout/stderr
  5. Destroy container
  6. Return results

AGPL Compliance:
  - Docker accessed via Docker API (network-only)
  - No Docker SDK imports in Orchestrator code
  - Container images are separate artifacts
```

#### 4. Test Runner

```yaml
Component: Test Runner
Technology: pytest + coverage
Purpose: Execute tests within sandbox

Capabilities:
  Unit Tests:
    - pytest execution
    - Coverage measurement
    - Assertion validation

  Integration Tests:
    - API contract testing
    - Database transaction tests
    - Service integration

  Quality Checks:
    - Linting (ruff)
    - Type checking (mypy)
    - Security scanning (semgrep)

Output:
  - Test results (pass/fail counts)
  - Coverage report (percentage)
  - Lint results (errors/warnings)
  - Security findings (severity levels)
```

#### 5. MRP Generator

```yaml
Component: MRP Generator
Technology: Python + Jinja2
Purpose: Produce Merge-Readiness Pack from execution results

Input Sources:
  - LPS execution log
  - Test results
  - Coverage report
  - Security scan results
  - Performance benchmarks
  - Code diff

Output:
  - MRP document (Markdown)
  - Evidence files (JSON)
  - SHA256 hashes (integrity)

Quality Checks:
  - All BRS requirements addressed
  - Test coverage threshold met
  - No critical security findings
  - Performance targets achieved
```

### AEE Security Model

```yaml
Isolation:
  Container Isolation:
    - Each task runs in separate container
    - No shared state between executions
    - Automatic cleanup

  Network Isolation:
    - Sandbox has no network access
    - AI providers accessed from orchestrator (outside sandbox)
    - Evidence Vault accessed from orchestrator

  Resource Isolation:
    - Memory limits enforced
    - CPU limits enforced
    - Disk quotas enforced

Secret Protection:
  Pre-execution:
    - Scan BRS for embedded secrets
    - Reject if secrets found

  During Execution:
    - No environment variables with secrets in sandbox
    - AI provider credentials in orchestrator only

  Post-execution:
    - Scan output for secrets
    - Redact before MRP generation
    - Alert if secrets detected

Audit Trail:
  - All executions logged
  - Input/output hashes recorded
  - Execution timing captured
  - Resource usage tracked
```

---

## 🔄 ACE-AEE COMMUNICATION

### Message Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MESSAGE FLOW DIAGRAM                                  │
└─────────────────────────────────────────────────────────────────────────────┘

SE4H (Human)                    Message Queue                   SE4A (Agent)
     │                               │                               │
     │  1. Submit BRS                │                               │
     │──────────────────────────────>│                               │
     │                               │  2. BRS Available             │
     │                               │──────────────────────────────>│
     │                               │                               │
     │                               │  3. Generate LPS              │
     │                               │<──────────────────────────────│
     │                               │                               │
     │                               │  4. Execute Steps             │
     │                               │──────────────────────────────>│
     │                               │                               │
     │                               │  5. CRP (if needed)           │
     │  6. CRP Notification          │<──────────────────────────────│
     │<──────────────────────────────│                               │
     │                               │                               │
     │  7. Respond to CRP            │                               │
     │──────────────────────────────>│  8. CRP Response              │
     │                               │──────────────────────────────>│
     │                               │                               │
     │                               │  9. Continue Execution        │
     │                               │──────────────────────────────>│
     │                               │                               │
     │                               │  10. Generate MRP             │
     │  11. MRP Ready                │<──────────────────────────────│
     │<──────────────────────────────│                               │
     │                               │                               │
     │  12. Review MRP               │                               │
     │  13. Issue VCR                │                               │
     │──────────────────────────────>│  14. VCR Decision             │
     │                               │──────────────────────────────>│
     │                               │                               │
     │                               │  15. Merge (if approved)      │
     │                               │──────────────────────────────>│
     │                               │                               │
```

### Message Types

```yaml
BRS_SUBMITTED:
  direction: ACE → AEE
  payload:
    brs_id: UUID
    project_id: UUID
    priority: P0 | P1 | P2 | P3
  triggers: LPS generation

LPS_GENERATED:
  direction: AEE → ACE (notification)
  payload:
    lps_id: UUID
    brs_id: UUID
    estimated_duration: duration
  triggers: Dashboard update

STEP_COMPLETED:
  direction: AEE → ACE (notification)
  payload:
    lps_id: UUID
    step_id: string
    status: COMPLETED | FAILED
    duration: duration
  triggers: Progress update

CRP_CREATED:
  direction: AEE → ACE
  payload:
    crp_id: UUID
    lps_id: UUID
    priority: P0 | P1 | P2 | P3
    question: string
    options: list
  triggers: Human notification

CRP_RESPONDED:
  direction: ACE → AEE
  payload:
    crp_id: UUID
    decision: OPTION_A | OPTION_B | OPTION_C
    guidance: string
  triggers: Resume execution

MRP_READY:
  direction: AEE → ACE
  payload:
    mrp_id: UUID
    lps_id: UUID
    evidence_urls: list
  triggers: Review notification

VCR_ISSUED:
  direction: ACE → AEE
  payload:
    vcr_id: UUID
    mrp_id: UUID
    decision: APPROVED | REJECTED | REVISION_REQUIRED
    changes: list (if revision)
  triggers: Merge or revision
```

### Queue Configuration

```yaml
Message Queue: Redis (primary) or RabbitMQ (enterprise)

Queues:
  brs_submissions:
    purpose: New BRS for processing
    priority: true
    dead_letter: brs_failures

  lps_executions:
    purpose: Active LPS step execution
    priority: true
    dead_letter: lps_failures

  crp_requests:
    purpose: CRP awaiting response
    ttl: 24 hours
    dead_letter: crp_expired

  mrp_reviews:
    purpose: MRP awaiting review
    ttl: 48 hours
    dead_letter: mrp_expired

  vcr_decisions:
    purpose: VCR decisions to process
    priority: true

Retry Policy:
  max_retries: 3
  backoff: exponential (1s, 5s, 30s)
  dead_letter_after: 3 failures

Monitoring:
  - Queue depth alerts (>100 pending)
  - Processing time alerts (>5min average)
  - Dead letter alerts (any message)
```

---

## 📊 OBSERVABILITY

### Metrics (Prometheus)

```yaml
ACE Metrics:
  ace_brs_created_total:
    type: counter
    labels: [project_id, status]

  ace_vcr_decisions_total:
    type: counter
    labels: [decision, reviewer]

  ace_crp_response_time_seconds:
    type: histogram
    buckets: [60, 300, 900, 3600, 14400]

  ace_active_sessions:
    type: gauge

AEE Metrics:
  aee_lps_execution_duration_seconds:
    type: histogram
    buckets: [60, 300, 900, 1800, 3600]

  aee_step_execution_total:
    type: counter
    labels: [status, step_type]

  aee_sandbox_executions_total:
    type: counter
    labels: [status, exit_code]

  aee_ai_provider_requests_total:
    type: counter
    labels: [provider, model, status]

  aee_ai_provider_latency_seconds:
    type: histogram
    labels: [provider]
    buckets: [0.1, 0.5, 1, 2, 5]

  aee_mrp_generated_total:
    type: counter
    labels: [project_id]
```

### Logging (Structured)

```yaml
Log Format: JSON

Fields:
  timestamp: ISO 8601
  level: DEBUG | INFO | WARNING | ERROR
  service: ace | aee
  component: gateway | orchestrator | sandbox
  trace_id: UUID (correlation)
  span_id: UUID
  message: string
  context: object

Example (ACE):
  {
    "timestamp": "2025-12-16T10:30:00Z",
    "level": "INFO",
    "service": "ace",
    "component": "gateway",
    "trace_id": "abc123",
    "span_id": "def456",
    "message": "BRS submitted",
    "context": {
      "brs_id": "BRS-2026-001",
      "user_id": "user-123",
      "project_id": "PRJ-001"
    }
  }

Example (AEE):
  {
    "timestamp": "2025-12-16T10:31:00Z",
    "level": "INFO",
    "service": "aee",
    "component": "orchestrator",
    "trace_id": "abc123",
    "span_id": "ghi789",
    "message": "Step completed",
    "context": {
      "lps_id": "LPS-2026-001",
      "step_id": "STEP-2.1",
      "duration_ms": 1250
    }
  }
```

### Tracing (OpenTelemetry)

```yaml
Trace Spans:

ACE Spans:
  - ace.brs.create
  - ace.brs.submit
  - ace.crp.respond
  - ace.mrp.review
  - ace.vcr.issue

AEE Spans:
  - aee.lps.generate
  - aee.lps.execute
  - aee.step.execute
  - aee.sandbox.run
  - aee.ai.request
  - aee.mrp.generate

Span Attributes:
  brs_id: string
  lps_id: string
  step_id: string
  agent_provider: string
  execution_duration_ms: number
```

### Dashboards (Grafana)

```yaml
Dashboard: ACE-AEE Overview

Panels:
  Row 1 - Summary:
    - Total BRS submitted (24h)
    - Active LPS executions
    - Pending CRP count
    - VCR approval rate

  Row 2 - ACE Activity:
    - BRS creation timeline
    - CRP response time distribution
    - VCR decisions by outcome

  Row 3 - AEE Performance:
    - LPS execution duration
    - Step success rate
    - AI provider latency
    - Sandbox resource usage

  Row 4 - Queue Health:
    - Queue depth over time
    - Processing latency
    - Dead letter count
    - Retry rate

Alerts:
  - CRP response time > 2h (P1)
  - Queue depth > 100 (P2)
  - Sandbox failure rate > 10% (P1)
  - AI provider latency > 5s (P2)
```

---

## 🔒 SECURITY ARCHITECTURE

### Defense in Depth

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LAYER 1: PERIMETER                                 │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  - WAF (Web Application Firewall)                                      │  │
│  │  - DDoS Protection                                                     │  │
│  │  - Rate Limiting (100 req/min per user)                               │  │
│  │  - IP Allowlisting (optional)                                         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LAYER 2: AUTHENTICATION                           │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  - JWT validation (RS256, 15min expiry)                               │  │
│  │  - OAuth 2.0 / OIDC                                                   │  │
│  │  - MFA enforcement (TOTP)                                             │  │
│  │  - Session management (single active)                                 │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LAYER 3: AUTHORIZATION                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  - RBAC (13 roles defined)                                            │  │
│  │  - Row-level security (PostgreSQL RLS)                                │  │
│  │  - API scopes (read:brs, write:vcr, etc.)                            │  │
│  │  - OPA policy evaluation                                              │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LAYER 4: DATA PROTECTION                          │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  - Encryption at rest (AES-256)                                       │  │
│  │  - Encryption in transit (TLS 1.3)                                    │  │
│  │  - Secret redaction (pre-storage)                                     │  │
│  │  - PII masking in logs                                                │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                     │
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LAYER 5: SANDBOX ISOLATION                        │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  - Container isolation (Docker)                                       │  │
│  │  - No network access                                                  │  │
│  │  - Resource limits (CPU, memory, disk)                               │  │
│  │  - Non-root execution                                                 │  │
│  │  - Automatic cleanup                                                  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### OWASP ASVS L2 Alignment

```yaml
V1 - Architecture:
  - ACE/AEE separation enforced ✅
  - Trust boundaries defined ✅
  - Threat model documented ✅

V2 - Authentication:
  - Password policy (12+ chars) ✅
  - MFA support ✅
  - Session management ✅
  - Credential storage (bcrypt) ✅

V3 - Session Management:
  - JWT with short expiry ✅
  - Refresh token rotation ✅
  - Session invalidation ✅

V4 - Access Control:
  - RBAC implemented ✅
  - Row-level security ✅
  - API authorization ✅

V5 - Validation:
  - Input validation (Pydantic) ✅
  - Output encoding ✅
  - SQL injection prevention ✅

V8 - Data Protection:
  - Encryption at rest ✅
  - Encryption in transit ✅
  - Secret management ✅

V9 - Communications:
  - TLS 1.3 enforced ✅
  - Certificate validation ✅

V11 - Business Logic:
  - Workflow validation ✅
  - State machine enforcement ✅

V12 - Files:
  - Upload validation ✅
  - Path traversal prevention ✅

V13 - API Security:
  - Rate limiting ✅
  - API versioning ✅
  - Error handling ✅
```

---

## 🚀 DEPLOYMENT ARCHITECTURE

### Container Architecture

```yaml
Docker Compose (Development):
  services:
    ace-gateway:
      image: sdlc/ace-gateway:latest
      ports: ["8000:8000"]
      depends_on: [postgres, redis]

    ace-dashboard:
      image: sdlc/ace-dashboard:latest
      ports: ["3000:3000"]
      depends_on: [ace-gateway]

    aee-orchestrator:
      image: sdlc/aee-orchestrator:latest
      depends_on: [postgres, redis]
      volumes:
        - /var/run/docker.sock:/var/run/docker.sock

    aee-sandbox:
      image: sdlc/aee-sandbox:latest
      # Ephemeral, created per execution

    postgres:
      image: postgres:15.5
      volumes: [pgdata:/var/lib/postgresql/data]

    redis:
      image: redis:7.2
      volumes: [redisdata:/data]

    minio:
      image: minio/minio:latest
      ports: ["9000:9000", "9001:9001"]
      volumes: [miniodata:/data]

    prometheus:
      image: prom/prometheus:latest
      ports: ["9090:9090"]

    grafana:
      image: grafana/grafana:10.2
      ports: ["3001:3000"]

Kubernetes (Production):
  namespaces:
    - sdlc-ace (ACE components)
    - sdlc-aee (AEE components)
    - sdlc-shared (databases, queues)
    - sdlc-monitoring (observability)

  scaling:
    ace-gateway: HPA (2-10 replicas)
    aee-orchestrator: HPA (2-20 replicas)
    aee-sandbox: Job-based (ephemeral)
```

### Resource Requirements

```yaml
Minimum (Development):
  CPU: 4 cores
  Memory: 8GB
  Storage: 50GB SSD

Recommended (Staging):
  CPU: 8 cores
  Memory: 16GB
  Storage: 200GB SSD

Production (per node):
  CPU: 16 cores
  Memory: 32GB
  Storage: 500GB SSD
  Nodes: 3 (minimum for HA)
```

---

## 📋 IMPLEMENTATION CHECKLIST

### Phase 2-Pilot Prerequisites

```yaml
ACE Components:
  - [ ] ACE Gateway (FastAPI) deployed
  - [ ] Authentication (JWT + OAuth) working
  - [ ] BRS CRUD operations functional
  - [ ] Agent status API implemented
  - [ ] CRP/MRP/VCR workflows operational
  - [ ] Web Dashboard MVP ready

AEE Components:
  - [ ] AEE Orchestrator deployed
  - [ ] AI Provider adapter (Ollama) working
  - [ ] Sandbox executor (Docker) operational
  - [ ] LPS parser implemented
  - [ ] MRP generator functional
  - [ ] Secret redaction active

Integration:
  - [ ] Message queue (Redis) configured
  - [ ] ACE-AEE communication tested
  - [ ] Evidence Vault integration complete
  - [ ] Observability stack deployed

Security:
  - [ ] OWASP ASVS L2 compliance verified
  - [ ] Penetration testing scheduled
  - [ ] AGPL containment validated
```

### Track 2 Enhancements (Q2 2026)

```yaml
Secret Redaction Service:
  - Pattern-based detection (API keys, passwords, tokens)
  - Integration with Evidence Vault
  - Configurable patterns from Framework

Sandbox Execution Service:
  - Enhanced resource limits
  - Execution traces
  - Performance monitoring

SASE Kanban Board:
  - BRS/MRP/VCR workflow visualization
  - Agent status panel
  - Real-time progress updates
```

---

## 📚 REFERENCES

### Related Documents

| Document | Location | Purpose |
|----------|----------|---------|
| SDLC-Agentic-Core-Principles | 02-Core-Methodology/ | SE4H/SE4A framework |
| BriefingScript Template | 05-Templates-Tools/SASE-Artifacts/ | BRS structure |
| MRP Template | 05-Templates-Tools/SASE-Artifacts/ | MRP structure |
| Security Baseline | docs/02-Design-Architecture/ | OWASP ASVS L2 |
| ADR-007 | docs/02-Design-Architecture/03-ADRs/ | AI Provider integration |

### External References

- arXiv:2509.06216v2 - Software Agentic Software Engineering (SASE)
- OWASP ASVS v4.0.3 - Application Security Verification Standard
- Docker Security Best Practices
- Kubernetes Security Guide

---

## 📝 REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-12-16 | PM/PO + AI | Initial version |
| 1.0.3 | 2026-01-22 | Framework Team | SDLC 5.2.0 alignment |

---

**Document Status:** Phase 1-Spec (SE 3.0 Track 1)
**Next Review:** CTO Final Review (Q1 2026)
**Framework Version:** SDLC 6.0.0 (7-Pillar Architecture + Section 7 Quality Assurance System)
