---
version: "6.1.1"
document_type: "Framework Standard"
section: "03-AI-GOVERNANCE"
ring: "Core"
status: "APPROVED"
owner: "CTO"
last_updated: "2026-02-18"
context_zone: "Core"
update_frequency: "Per major version (quarterly)"
priority: "P1"
source: "3 production multi-agent codebases (2025-2026) + SASE Framework (arXiv:2509.06216v2)"
sprint: "176"
---

# Multi-Agent Collaboration Patterns

**Framework Version**: SDLC 6.1.1
**Pillar**: 03 — AI Governance
**Classification**: ORANGE (New Methodology — requires ADR)
**Effective Date**: February 18, 2026

---

## 1. Problem Statement

Single-agent AI workflows hit a ceiling when tasks require **division of labor**. A single agent cannot simultaneously:

- **Plan** the architecture AND **implement** the code AND **review** the output
- **Maintain context** across 50+ file changes without degradation
- **Apply domain expertise** in security, testing, DevOps, and product simultaneously
- **Self-correct** without an independent reviewer perspective

Multi-agent systems solve this by assigning **specialized roles** to purpose-built agents that collaborate through structured messaging. However, without governance patterns, multi-agent systems degrade into:

- **Infinite loops** — agents delegating endlessly without convergence
- **Lost context** — conversation state scattered across agents with no inheritance
- **Silent failures** — provider errors swallowed without classification or fallback
- **Budget overruns** — token consumption unchecked across agent chains

This document codifies **10 battle-tested patterns** extracted from 3 production multi-agent codebases and validated against the SASE Framework (SE 3.0).

---

## 2. Pattern Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                  Multi-Agent Collaboration                      │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐│
│  │  Messaging   │  │  Lifecycle   │  │   Organization          ││
│  │             │  │             │  │                         ││
│  │ • Lane Queue │  │ • Snapshot  │  │ • 12-Role SASE         ││
│  │ • Queue Mode │  │   Precedence│  │   Classification       ││
│  │ • @Mention  │  │ • Parent-   │  │ • Session Scoping      ││
│  │   Routing   │  │   Child     │  │ • Canonical Protocol   ││
│  │ • Dead-     │  │   Inherit   │  │                         ││
│  │   Letter    │  │ • Provider  │  │                         ││
│  │             │  │   Failover  │  │                         ││
│  └─────────────┘  └─────────────┘  └─────────────────────────┘│
│                                                                 │
│  Companion: Agent Safety Patterns (doc 13)                     │
└─────────────────────────────────────────────────────────────────┘
```

| # | Pattern | Category | Complexity | When to Apply |
|---|---------|----------|------------|---------------|
| 1 | Lane-Based Message Queue | Messaging | High | Any multi-agent system |
| 2 | Queue Modes | Messaging | Medium | Agent interaction control |
| 3 | @Mention Routing | Messaging | Low | Team-based agent collaboration |
| 4 | Dead-Letter + Deduplication | Messaging | Medium | Reliability requirement |
| 5 | Snapshot Precedence | Lifecycle | Medium | Agent configuration management |
| 6 | Parent-Child Inheritance | Lifecycle | High | Delegation chains |
| 7 | Provider Failover Chain | Lifecycle | High | Multi-provider AI usage |
| 8 | 12-Role SASE Classification | Organization | Medium | Enterprise agent governance |
| 9 | Session Scoping | Organization | Low | Multi-user/multi-channel agents |
| 10 | Canonical Protocol Owner | Organization | Low | Multi-platform ecosystems |

---

## 3. Pattern 1: Lane-Based Message Queue

### Problem

Multiple agents processing messages concurrently can create race conditions—two agents picking up the same message, or messages processed out of order for a single agent.

### Pattern

Assign each agent a **processing lane** (named queue). Messages within a lane are processed **serially** (one at a time). Messages across different lanes process **in parallel**.

```
Agent-A Lane:  [msg1] → [msg2] → [msg3]    (serial within lane)
Agent-B Lane:  [msg4] → [msg5]              (serial within lane)
                                              (parallel across lanes)
```

### Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Database is truth** | Persistent storage survives restarts; message state is always recoverable |
| **Pub/sub is notify-only** | Cache invalidation / wake-up signal; NOT the authoritative queue |
| **Lock-and-skip** | Concurrent workers skip locked rows instead of blocking; prevents queue head-of-line blocking |
| **Atomic state transitions** | Message status changes (pending → processing → completed) are single atomic operations |

### Implementation Guidance

```
Queue Claim Algorithm:
  1. SELECT next pending message WHERE lane = agent_lane
     ORDER BY created_at
     LIMIT 1
     FOR UPDATE SKIP LOCKED
  2. UPDATE status = 'processing'
  3. Process message (invoke AI provider)
  4. UPDATE status = 'completed' or 'failed'
  5. If failed_count >= max_retries → status = 'dead_letter'
  6. Publish notify event to wake next worker
```

### Anti-Patterns

- **Memory-only queue**: Messages lost on restart; no audit trail
- **Single global queue**: All agents contend for same lock; head-of-line blocking
- **Pub/sub as truth**: Messages lost if no subscriber is listening at publish time

---

## 4. Pattern 2: Queue Modes

### Problem

Different agent interactions require different message flow patterns. A code reviewer should queue messages for orderly processing, but a human override should interrupt immediately.

### Pattern

Define **7 queue modes** that control how messages flow to an agent:

| Mode | Behavior | Use Case |
|------|----------|----------|
| **queue** | FIFO, one-at-a-time | Default for most agents |
| **steer** | Replace current task, pause previous | Human redirects agent focus |
| **interrupt** | Halt current processing immediately | Emergency stop, human override |
| **broadcast** | Send to all agents in team | System announcements, status updates |
| **round-robin** | Distribute across agent pool | Load balancing identical agents |
| **priority** | Skip ahead of normal queue | High-priority gate evaluations |
| **direct** | Bypass queue, deliver immediately | Agent-to-agent targeted messages |

### Recommended P0 Scope

Start with **3 modes**: `queue`, `steer`, `interrupt`. Add remaining modes when use cases emerge.

### Decision Matrix

```
Is it an emergency?
  ├── YES → interrupt
  └── NO
      ├── Should agent change focus? → steer
      ├── Should all agents see it? → broadcast
      ├── Load balance across pool? → round-robin
      ├── Higher priority than current? → priority
      ├── Direct agent-to-agent? → direct
      └── Normal processing → queue
```

---

## 5. Pattern 3: @Mention Routing

### Problem

In team-based agent conversations, a user or agent needs to direct a message to a specific agent out of many. Without explicit routing, all agents would attempt to process every message.

### Pattern

Use **@mention syntax** to route messages to specific agents:

```
[@coder: Implement the login endpoint]
[@reviewer: Check the authentication logic]
[@architect: Review the database schema design]
```

### Routing Rules

| Scenario | Behavior |
|----------|----------|
| `[@specific-agent: message]` | Route to named agent only |
| No @mention in team conversation | Route to **team leader** (configurable) |
| `[@all: message]` | Broadcast to all team agents |
| Unknown @mention | Return error, suggest available agents |

### Design Principles

- **Explicit over implicit**: Prefer explicit routing to reduce wasted AI invocations
- **Leader fallback**: Unaddressed messages go to team leader (typically PM or Architect role)
- **Parse before queue**: Mention parsing happens before message enters any agent lane

---

## 6. Pattern 4: Dead-Letter Queue + Deduplication

### Problem

Messages that repeatedly fail should not retry forever. Duplicate messages (from retries, network issues) should not cause double-processing.

### Pattern

**Dead-letter**: After N consecutive failures (recommended: 3), move message to dead-letter status for manual review or automated triage.

**Deduplication**: Assign a unique idempotency key to each message. Reject or skip messages with duplicate keys.

```
Message Lifecycle:
  pending → processing → completed     (happy path)
  pending → processing → failed         (first failure)
  failed → pending → processing → failed (retry #2)
  failed → dead_letter                   (after max retries)

Retry Backoff (exponential):
  Attempt 1: immediate
  Attempt 2: 30 seconds
  Attempt 3: 60 seconds
  After 3: dead_letter
```

### Dead-Letter Handling

| Action | When | Who |
|--------|------|-----|
| Auto-retry with different provider | Provider-specific failure (rate limit, timeout) | System |
| Escalate to human | Persistent content failure (format, auth) | System → Human |
| Archive and skip | Non-critical notification | System |
| Requeue manually | After human fixes root cause | Human |

### Deduplication Strategy

- Generate idempotency key from: `{sender_id}:{content_hash}:{timestamp_bucket}`
- Reject duplicates within a configurable time window (recommended: 5 minutes)
- Unique constraint on deduplication key column for database-level enforcement

---

## 7. Pattern 5: Snapshot Precedence

### Problem

Agent configurations change over time (model upgrades, prompt refinements). Running conversations should not be affected by configuration changes mid-execution.

### Pattern

When a conversation is created, **snapshot** all relevant configuration fields from the agent definition into the conversation record. After creation, the **conversation copy is authoritative** — definition changes do NOT retroactively affect running conversations.

```
Agent Definition (template)     Conversation (instance)
═══════════════════════         ═══════════════════════
max_messages: 50          ──►   max_messages: 50 (snapshotted)
max_budget_cents: 1000    ──►   max_budget_cents: 1000 (snapshotted)
queue_mode: "queue"       ──►   queue_mode: "queue" (snapshotted)
session_scope: "per-sender" ──► session_scope: "per-sender" (snapshotted)

If definition.max_messages changes to 100:
  → Existing conversations keep 50
  → Only NEW conversations get 100
```

### Fields to Snapshot

| Field | Why Snapshot |
|-------|-------------|
| `max_messages` | Loop prevention must not change mid-conversation |
| `max_budget_cents` | Budget approval was for original amount |
| `queue_mode` | Changing mode mid-conversation breaks message ordering |
| `session_scope` | Scope change would orphan existing session state |
| `system_prompt` | Prompt change mid-conversation causes inconsistent behavior |

### Anti-Pattern: Live Reference

Do NOT read configuration from the definition table during conversation execution. This creates a race condition where configuration changes affect in-flight work.

---

## 8. Pattern 6: Parent-Child Conversation Inheritance

### Problem

When an agent delegates work to a sub-agent, the sub-agent needs context from the parent conversation. Without structured inheritance, context is lost at delegation boundaries.

### Pattern

Maintain an explicit **parent-child relationship** between conversations:

```
Root Conversation (Initializer Agent)
  └── Child Conversation (Coder Agent)
       └── Grandchild Conversation (Reviewer Agent)  -- if delegation depth allows
```

### Inheritance Rules

| Field | Inherited? | Rationale |
|-------|-----------|-----------|
| `project_id` | YES | Sub-agent works on same project |
| `parent_conversation_id` | SET to parent | Creates the chain |
| `delegation_depth` | parent + 1 | Tracks chain depth for limit enforcement |
| `initiator_type` | "agent" | Parent agent is the initiator |
| `max_budget_cents` | Reduced from parent | Child cannot exceed parent's remaining budget |
| `system_prompt` | NOT inherited | Each agent has its own role prompt |
| `allowed_tools` | May be more restrictive | Child should not have more permissions than parent |

### Depth Limit Enforcement

```
max_delegation_depth (configured per agent definition):
  0 = cannot delegate (leaf agent)
  1 = can delegate one level (most agents)
  2 = can delegate two levels (orchestrator agents)

On conversation creation:
  IF new_depth > agent_definition.max_delegation_depth:
    REJECT delegation with error
```

---

## 9. Pattern 7: Provider Failover Chain

### Problem

AI providers experience outages, rate limits, and billing issues. A single-provider system becomes unavailable when its provider fails.

### Pattern

Configure a **failover chain** of providers. On failure, classify the error and route to the next provider or abort.

### Six-Reason Error Classification

| Reason | Description | Action |
|--------|-------------|--------|
| `auth` | API key invalid or expired | **Abort** — no retry will help |
| `format` | Request malformed, model incompatible | **Abort** — fix request format |
| `rate_limit` | Provider throttle (429) | **Cooldown** then retry or failover |
| `billing` | Quota/budget exceeded | **Abort** — requires human intervention |
| `timeout` | Response took too long | **Failover** to next provider |
| `unknown` | Unexpected error | **Failover** with logging for investigation |

### Abort Matrix

Not all errors should trigger failover. Some require immediate abort:

| Error | Provider 1 (Local) | Provider 2 (Cloud) | Provider 3 (Fallback) |
|-------|-------------------|--------------------|-----------------------|
| auth | Skip → P2 | Skip → P3 | **ABORT** |
| format | Retry once → P2 | Retry once → P3 | **ABORT** |
| rate_limit | Cooldown → retry | Cooldown → P3 | **ABORT** |
| billing | Skip → P2 | Skip → P3 | **ABORT** |
| timeout | Skip → P2 | Skip → P3 | **ABORT** |
| unknown | Skip → P2 | Skip → P3 | **ABORT** |

### Cooldown Strategy

When a provider hits rate_limit:
- Set cooldown timestamp (recommended: 60 seconds)
- Skip provider during cooldown
- Automatically re-enable after cooldown expires
- Use in-memory cache for cooldown state (fast check, not persistence-critical)

---

## 10. Pattern 8: 12-Role SASE Classification

### Problem

Multi-agent teams need structured role definitions. Without standardized roles, agents overlap in responsibility, miss critical perspectives, or operate without appropriate authority boundaries.

### Pattern

Define **12 agent roles** classified into **3 types** based on the SASE Framework (SE 3.0):

| Type | Roles | Authority | Environment |
|------|-------|-----------|-------------|
| **SE4A** (Agent Executor) | researcher, pm, pjm, architect, coder, reviewer, tester, devops | Delegated by SE4H | Execution environment |
| **SE4H** (Human Advisor) | ceo, cpo, cto | VCR authority, final approval | Advisory environment |
| **Router** | assistant | No authority, guidance only | Both |

### SE4A Roles (8 Executors)

| Role | Responsibility | Typical Tasks |
|------|---------------|---------------|
| `researcher` | Information gathering, analysis | Market research, technology evaluation |
| `pm` | Product management, requirements | PRD drafting, user story synthesis |
| `pjm` | Project management, coordination | Sprint planning, progress tracking |
| `architect` | System design, technical decisions | Architecture review, ADR drafting |
| `coder` | Code generation, implementation | Feature implementation, bug fixes |
| `reviewer` | Code review, quality assurance | PR review, code quality analysis |
| `tester` | Testing, validation | Test generation, E2E testing |
| `devops` | Operations, deployment | CI/CD setup, infrastructure config |

### SE4H Roles (3 AI Advisors)

**Critical distinction**: SE4H entries represent **AI advisors supporting human decision-makers**, NOT the humans themselves. The actual human retains:
- Final decision authority (VCR — Verify, Correct, Ratify)
- Approval of all shipped code
- Accountability for all agent outputs

| Role | Advisory Scope | Output Type |
|------|---------------|-------------|
| `ceo` | Strategic decisions, roadmap synthesis | Analysis, recommendations, summaries |
| `cpo` | Product decisions, prioritization | Research summaries, draft proposals |
| `cto` | Architecture decisions, security analysis | Technical assessments, risk analysis |

### SE4H Behavioral Constraints

SE4H agents MUST have stricter configurations than SE4A agents:

| Constraint | SE4H | SE4A Default |
|-----------|------|-------------|
| Delegation depth | 0 (no delegation) | 1 |
| Spawn sub-agents | No | No (opt-in) |
| Tool permissions | Read-only subset | Full (configurable) |
| Queue mode | queue only | Any mode |
| Output reviewed before action | Always | Configurable |

### Router Role

The `assistant` role is a **routing agent** that:
- Guides users to the appropriate agent or workflow
- Explains available capabilities and stages
- Has no decision authority — purely navigational
- Uses a fast, low-cost model

### Model Tier Recommendations

Use **abstract capability tiers** rather than version-pinned model identifiers:

| Tier | Capability | Recommended For |
|------|-----------|-----------------|
| **Tier 1: Deep Reasoning** | Strategic analysis, architecture review | ceo, cto, architect, reviewer |
| **Tier 2: Fast Reasoning** | Code generation, product analysis | cpo, researcher, pm, coder, tester |
| **Tier 3: Fast Execution** | Coordination, routing, simple tasks | pjm, devops, assistant |

---

## 11. Pattern 9: Session Scoping

### Problem

Agents serving multiple users simultaneously need isolation. Without session scoping, one user's conversation bleeds into another's.

### Pattern

Define **2 session scoping modes**:

| Scope | Behavior | Use Case |
|-------|----------|----------|
| **per-sender** | Each user gets their own conversation instance | Default for most agents |
| **global** | All users share one conversation | Broadcast agents, shared dashboards |

### Session Key Derivation

```
per-sender key:  {agent_id}:{channel}:{sender_id}
global key:      {agent_id}:{channel}:global
```

For group channels (teams, chat groups), derive additional scoping:
```
per-chat key:    {agent_id}:{channel}:{chat_id}:{sender_id}
per-channel key: {agent_id}:{channel}:{chat_id}:global
```

### Recommendation

Start with `per-sender` (default). Use `global` only for agents that need shared state (team dashboards, announcement bots). Group scoping is P2 complexity.

---

## 12. Pattern 10: Canonical Protocol Owner

### Problem

When multiple platforms (enterprise orchestrator, lightweight CLI, mobile app, external channels) all interact with agents, message format divergence creates integration nightmares.

### Pattern

Designate **one system as the canonical protocol owner**. All other systems are **clients** that conform to the protocol.

```
Canonical Owner (Enterprise Orchestrator)
  ├── defines message schema
  ├── defines status codes
  ├── defines event types
  └── publishes protocol spec

Clients (conform to protocol):
  ├── Lightweight CLI tool → sends/receives via REST API
  ├── External channels (Telegram, Discord) → translates to/from protocol
  └── IDE extensions → sends/receives via REST API
```

### Protocol Contract

The canonical owner defines:

| Component | Owner Responsibility | Client Responsibility |
|-----------|---------------------|----------------------|
| Message schema | Define required/optional fields | Conform to schema |
| Status codes | Define all valid codes | Handle all codes |
| Event types | Define event taxonomy | Subscribe to relevant events |
| Versioning | Semantic versioning of protocol | Declare supported version |
| Rate limits | Define per-client limits | Respect limits |

### Anti-Pattern: Distributed Protocol Ownership

When each platform defines its own message format:
- Translation layers multiply (N×M adapters for N formats × M platforms)
- Schema drift goes undetected until production failures
- No single source of truth for message validation

---

## 13. SDLC Framework Enhancement

### Integration with Quality Gates

Multi-agent patterns integrate with the SDLC Quality Gate system:

| Gate | Multi-Agent Enhancement |
|------|------------------------|
| G0.1 Foundation | Researcher + PM agents for evidence gathering |
| G1 Consultation | AI advisor (SE4H) drafts, human reviews |
| G2 Design Ready | Architect agent proposes, Reviewer agent validates, CTO advisor assesses |
| G3 Ship Ready | Coder implements, Tester validates, DevOps deploys — all with agent collaboration |
| G4 Production | Monitoring agents detect issues, escalate to SE4H advisors |

### Integration with Evidence Vault

Every agent message generates traceable evidence:

| Evidence Type | Source |
|--------------|--------|
| `AGENT_CONVERSATION` | Full conversation transcript |
| `AGENT_DECISION` | Agent recommendations with reasoning |
| `AGENT_CODE_REVIEW` | Reviewer agent output |
| `AGENT_DELEGATION` | Parent-child delegation chain |
| `AGENT_FAILOVER` | Provider failover events with reasons |

### Governance Alignment

| AI Governance Principle | Multi-Agent Application |
|------------------------|------------------------|
| Principle 1: AI-Human Collaboration | SE4H roles enforce human review of all advisory output |
| Principle 2: Agent Accountability | Parent-child chains create clear delegation audit trails |
| Principle 3: Planning Mode | Architect and PM agents enforce planning before coding |
| Principle 4: Verification-First | Reviewer and Tester agents validate before merge |
| Principle 5: Context Management | Session scoping prevents context contamination |
| Principle 7: Anti-Patterns | Dead-letter queue catches infinite loops and budget overruns |

---

## 14. Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|------------|
| Infinite delegation chains | High (cost, quality) | `max_delegation_depth` enforced per agent |
| Provider cascade failure | High (availability) | Abort matrix prevents futile retries |
| Message loss | Medium (data) | Database-as-truth, dead-letter for failures |
| Budget overrun | High (cost) | Circuit breaker on `max_budget_cents` |
| Scope creep in agent roles | Medium (quality) | 12-role taxonomy with behavioral constraints |
| Protocol drift between platforms | Medium (integration) | Canonical protocol owner pattern |

---

## 15. Adoption Guide

### Tier-Based Adoption

| Tier | Patterns to Adopt | Rationale |
|------|-------------------|-----------|
| **LITE** | Patterns 1-3, 7 | Minimal multi-agent with failover |
| **STANDARD** | + Patterns 4-6 | Add reliability + configuration management |
| **PROFESSIONAL** | + Patterns 8-10 | Add SASE roles + full governance |
| **ENTERPRISE** | All patterns | Complete multi-agent governance |

### Maturity Progression

```
Level 0: Single agent, no collaboration
Level 1: Two agents (e.g., Coder + Reviewer) with simple queue
Level 2: Team of agents with role classification + failover
Level 3: Multi-team with parent-child delegation + budget control
Level 4: Cross-platform with canonical protocol + OTT channels
```

---

## 16. Comparison with Industry Approaches

| Approach | Strengths | Gaps Addressed by SDLC |
|----------|-----------|----------------------|
| **Crew AI** | Role-based agents, process types | No quality gates, no evidence trail, no budget control |
| **AutoGen** | Flexible conversation patterns | No lane-based concurrency, no fail classification |
| **LangGraph** | Graph-based state machines | No SASE role taxonomy, no snapshot precedence |
| **OpenAI Swarm** | Simple handoff paradigm | No persistence, no dead-letter, no delegation depth |
| **SDLC Multi-Agent** | All above + Quality Gates + Evidence Vault + SASE roles | — |

---

## 17. References

1. SASE Framework — arXiv:2509.06216v2 (SE4H, SE4A classification)
2. SDLC 6.1.1 Quality Assurance System — Section 7
3. SDLC Quality Gates — G0.1 through G4
4. AI Governance Principles — Documents 01-11 (this section)
5. Autonomous Codegen Patterns — Document 11 (two-agent pattern)

---

**Document Status**: APPROVED
**Owner**: CTO Office
**Last Updated**: February 18, 2026
**Framework**: SDLC 6.1.1
