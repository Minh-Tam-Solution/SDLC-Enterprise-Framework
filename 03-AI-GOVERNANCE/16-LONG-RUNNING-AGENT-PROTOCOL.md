---
title: "Long-Running Agent Protocol"
version: "6.2.0"
ring: 1
iceberg_layer: "Structures"
dt_phase: "Prototype"
sdlc_version: "6.2.0"
last_updated: "2026-03-18"
status: "ACTIVE"
pillar: "AI Governance"
---

# Long-Running Agent Protocol

> **Ring 1 (Core)** — Methodology for multi-session agent continuity.
> Traces to Mental Model #7: "Agent Continuity" (System Thinking Foundation).

## 1. Overview

Long-running agents work for hours to days, building complete systems with periodic human checkpoints. This protocol defines how agents maintain context, checkpoint their work, and hand off between sessions — independent of any specific tool or platform.

**Traces to**:
- Mental Model #7: "Agent Continuity" (System Thinking Foundation)
- Singapore MGF Dimension 3: Technical Controls — "reconstruct the chain of reasoning"
- NIST emerging direction: agent traceability and auditability

## 2. Checkpoint Policy

### 2.1 What to Checkpoint
- **Reasoning state**: Current plan, completed steps, pending decisions
- **Context summary**: Key facts discovered, constraints identified
- **Artifact inventory**: Files created/modified, tests written, evidence collected
- **Decision log**: Choices made and rationale (immutable audit trail)

### 2.2 When to Checkpoint

| Trigger | Type | Action |
|---------|------|--------|
| Task boundary crossed | Automatic | Checkpoint before starting new task |
| Time threshold (configurable, default 2h) | Automatic | Periodic checkpoint regardless of state |
| Budget threshold (80% consumed) | Automatic | Checkpoint + alert human |
| Human requests checkpoint | Manual | Immediate checkpoint + status report |
| Error/failure detected | Automatic | Checkpoint before retry or escalation |
| Security boundary (auth, payment, PII) | Mandatory | Checkpoint + require human approval |

### 2.3 Checkpoint Fidelity

**Lossless checkpoint** (default for <4h sessions):
- Full reasoning chain preserved
- All intermediate outputs retained
- Complete tool call history
- Cost: Higher storage, slower resume

**Lossy checkpoint** (for >4h sessions):
- Summarized reasoning chain (key decisions only)
- Final outputs only (intermediates discarded)
- Tool call summary (not full history)
- Cost: Lower storage, faster resume
- Risk: May lose context nuance — mitigated by structured note-taking

### 2.4 Checkpoint Format (Tool-Agnostic)

```yaml
checkpoint:
  session_id: "{unique_identifier}"
  created_at: "{ISO-8601}"
  fidelity: "lossless|lossy"
  reasoning_state:
    current_plan: "{text}"
    completed_steps: ["{step1}", "{step2}"]
    pending_decisions: ["{decision1}"]
  context_summary:
    key_facts: ["{fact1}", "{fact2}"]
    constraints: ["{constraint1}"]
  artifacts:
    created: ["{file1}", "{file2}"]
    modified: ["{existing_file}"]
    tests: ["{test_file}"]
  decision_log:
    - decision: "{chose X over Y}"
      rationale: "{because Z}"
      timestamp: "{ISO-8601}"
  budget:
    tokens_used: "{number}"
    tokens_remaining: "{number}"
    cost_estimate: "{currency_amount}"
```

## 3. Memory Policy

### 3.1 Structured Note-Taking

Agents MUST maintain structured notes OUTSIDE the context window:
- **Scratchpad**: Working memory for current task (ephemeral)
- **Session notes**: Key learnings persisted across context window resets
- **Project memory**: Long-term knowledge persisted across sessions

### 3.2 Context Compaction Strategies

| Strategy | When to Use | Preservation Rate |
|----------|------------|-------------------|
| **Trimming** | Context >80% full | ~70% of key info |
| **Summarization** | Session handoff | ~85% of key info |
| **Sub-agent synthesis** | Complex multi-file tasks | ~95% of key info |

### 3.3 Note Persistence Hierarchy

```
Session Notes (ephemeral, within session)
    ↓ summarize at checkpoint
Project Notes (persistent, across sessions)
    ↓ curate at project milestone
Organization Notes (permanent, across projects)
```

## 4. Handoff Policy

### 4.1 Agent-to-Agent Handoff

When one agent hands off to another:
1. Source agent creates **lossless checkpoint**
2. Source agent writes **handoff brief** (structured summary)
3. Target agent receives: checkpoint + handoff brief + original task spec
4. Target agent validates checkpoint integrity
5. Target agent resumes from checkpoint state

### 4.2 Session-to-Session Continuity

When the same agent resumes after interruption:
1. Load latest checkpoint
2. Verify checkpoint freshness (< configurable max_age, default 48h)
3. If stale: re-read affected files, diff against checkpoint artifacts
4. Resume from checkpoint + apply any external changes detected

### 4.3 Handoff Brief Template

```markdown
## Handoff Brief
- **Task**: {original task description}
- **Status**: {completed|in-progress|blocked}
- **Completed**: {list of done items}
- **In Progress**: {current work item + state}
- **Blocked On**: {what needs human input}
- **Key Decisions**: {top 3 decisions made and why}
- **Known Issues**: {any bugs, tech debt, or concerns}
- **Next Steps**: {recommended actions for receiving agent}
```

## 5. Timeout and Budget Controls

### 5.1 Time Limits (Tier-Dependent)

| Tier | Max Session Duration | Max Total Duration | Checkpoint Interval |
|------|---------------------|-------------------|-------------------|
| LITE | 30 min | 2 hours | 15 min |
| STANDARD | 2 hours | 8 hours | 30 min |
| PROFESSIONAL | 8 hours | 48 hours | 1 hour |
| ENTERPRISE | 24 hours | 168 hours (1 week) | 2 hours |

### 5.2 Budget Escalation

- **80% warning**: Automatic checkpoint + human notification
- **95% hard stop**: Checkpoint + escalate to human
- **100% abort**: Emergency checkpoint + terminate

### 5.3 Escalation Chain

```
Agent timeout/budget → Checkpoint → Notify human
    ↓ (if no response in configurable window)
Escalate to team lead
    ↓ (if no response)
Auto-pause agent (preserve state, wait for human)
```

## 6. Human Checkpoint Strategy

### 6.1 When Humans MUST Intervene

- **Security boundary**: Any action touching auth, payments, PII, or external APIs
- **Architecture decision**: Schema changes, new service creation, API contract changes
- **Quality gate**: G3/G4 gates always require human approval
- **Strategic decision**: Scope changes, priority shifts, design trade-offs
- **Conflict resolution**: Agent disagrees with existing code patterns or conventions

### 6.2 Human Checkpoint Format

Human receives:
1. **Status summary**: What agent has done, what it plans to do
2. **Decision request**: Specific question requiring human judgment
3. **Options**: 2-3 options with trade-offs explained
4. **Recommendation**: Agent's preferred option with rationale

Human responds with:
- **Approve**: Continue as planned
- **Redirect**: Change approach (agent re-plans from checkpoint)
- **Pause**: Stop and preserve state
- **Abort**: Terminate task (agent creates final checkpoint + cleanup)

## 7. Traceability Requirements

Per Singapore MGF and NIST emerging direction:
- Every checkpoint MUST be stored with immutable audit trail
- Every decision MUST include rationale and timestamp
- Every handoff MUST be logged with source/target agent identities
- Evidence chain: checkpoint → handoff → resume → output → evidence storage
- Reconstruction: Given any final output, MUST be able to trace back through all checkpoints to original intent

---

## Further Reading

> The protocol above is self-contained. References below are for deeper study.

**External Standards**:
- NIST AI Agent Standards Initiative (emerging, 2027+) — agent traceability requirements
- Singapore Model AI Governance Framework — Dimension 3: Technical Controls

**Academic**:
- arXiv:2509.06216v2 — SASE Framework (checkpoint patterns)

**Industry**:
- Anthropic: "Effective Context Engineering for AI Agents" (2026) — compaction + note-taking
- Anthropic: "2026 Agentic Coding Trends Report" — Trend 3: Long-running agents

**Internal**:
- Mental Model #7: "Agent Continuity" (02-Core-Methodology/SDLC-System-Thinking-Foundation.md)

---

**Document Status**: ACTIVE
**Framework Version**: SDLC 6.2.0
**Last Updated**: March 18, 2026
