# ADR-034: Planning Sub-agent Orchestration

**Status:** APPROVED
**Date:** January 22, 2026
**Decision Makers:** CTO, Framework Architecture Team
**Impact:** HIGH - Affects all agentic development workflows
**Framework Version:** SDLC 5.1.3+

---

## Context

### Expert AI Coding Workflow Analysis (January 2026)

Analysis of expert AI coding workflows reveals a 4-phase approach that achieves superior code quality and reduced architectural drift:

```
┌─────────────────────────────────────────────────────────────────────┐
│              EXPERT AI CODING WORKFLOW (2026)                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Phase 1: SPECIFICATION GENERATION                                   │
│  ├── Reference Collection (screenshots, examples)                    │
│  ├── PRD Synthesis (large context model)                            │
│  └── Interactive Refinement (ask_user_question pattern)             │
│                                                                      │
│  Phase 2: PLANNING MODE (>15 LOC changes)                           │
│  ├── Spawn Explore Sub-agents (3-5 parallel)                        │
│  ├── Extract Patterns (agentic grep > RAG)                          │
│  ├── Review ADRs and Conventions                                    │
│  └── Build Implementation Plan                                       │
│                                                                      │
│  Phase 3: IMPLEMENTATION                                             │
│  ├── Execute Plan with Selected Model                                │
│  ├── Apply Model Selection Matrix                                    │
│  └── Evidence Collection (MRP)                                       │
│                                                                      │
│  Phase 4: REVIEW & LEARNING                                          │
│  ├── Code Review (PR comments)                                       │
│  ├── Pattern Extraction from Feedback                                │
│  └── Update Context Files (AGENTS.md, CLAUDE.md)                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Insight: Agentic Grep > RAG

**Problem:** Traditional RAG (Retrieval-Augmented Generation) indexing can miss context and produce stale results.

**Solution:** Pre-planning pattern extraction via sub-agents using direct codebase exploration (agentic grep) finds real patterns with current state.

```yaml
Why Agentic Grep > RAG:
  - Real-time: Always reflects current codebase state
  - Contextual: Sub-agents understand search intent
  - Comprehensive: Multiple parallel searches
  - Adaptive: Can refine search based on findings

RAG Limitations:
  - Stale: Index may be outdated
  - Context loss: Embedding may miss nuances
  - Single-shot: One search, no refinement
```

### Current Gap (SDLC 5.1.3)

SDLC Orchestrator is 92% aligned with expert workflow. The 8% gap is in:

1. **No formal planning mode** - Changes >15 LOC often start without pattern extraction
2. **No sub-agent orchestration** - Explore agents not systematically spawned
3. **No conformance check** - Plans not validated against ADRs before execution
4. **No feedback loop closure** - PR review learnings not systematically captured

---

## Decision

**We will implement Planning Sub-agent Orchestration as a core agentic principle.**

### 1. Add `sdlcctl plan <task>` Command

```bash
# Launch planning mode with sub-agent orchestration
sdlcctl plan "Add user authentication feature"

# Options
sdlcctl plan <task> \
  --path <project-path>     # Project to analyze (default: .)
  --depth <n>               # Search depth 1-5 (default: 3)
  --auto                    # Auto-approve plan (skip human gate)
  --output <format>         # terminal | json | markdown
```

### 2. Spawn Explore Sub-agents (3-5 Parallel)

For each planning task, spawn sub-agents to discover:

```yaml
Sub-agent 1: Similar Implementations
  Query: "Find similar features in codebase"
  Method: Agentic grep for related functions, classes, patterns
  Output: List of similar implementations with file paths

Sub-agent 2: Related ADRs
  Query: "Find ADRs related to this feature area"
  Method: Search docs/02-design/03-ADRs/ and AGENTS.md
  Output: List of relevant ADRs with key decisions

Sub-agent 3: Existing Test Patterns
  Query: "Find test patterns for similar features"
  Method: Search tests/ for related test files
  Output: Test patterns to follow, coverage expectations

Sub-agent 4: Code Standards Check
  Query: "Extract code standards for affected areas"
  Method: Read CLAUDE.md, AGENTS.md, MentorScript sections
  Output: Applicable code standards and anti-patterns

Sub-agent 5: Dependency Analysis (optional)
  Query: "Identify dependencies and integration points"
  Method: Analyze imports, API contracts, database schemas
  Output: Integration requirements and constraints
```

### 3. Synthesize Findings into Implementation Plan

```yaml
Implementation Plan Schema:
  task_description: string
  estimated_complexity: low | medium | high | very_high
  estimated_loc_change: number

  patterns_found:
    - file: string
      relevance: high | medium | low
      key_patterns: string[]

  adrs_applicable:
    - adr_id: string
      key_decisions: string[]
      constraints: string[]

  test_patterns:
    - test_file: string
      pattern_type: unit | integration | e2e
      coverage_expectations: string

  implementation_steps:
    - step: number
      description: string
      files_affected: string[]
      human_checkpoint: boolean

  conformance_checks:
    - check: string
      status: pass | warning | fail
      details: string
```

### 4. Human Approval Gate Before Execution

```
┌─────────────────────────────────────────────────────────────────────┐
│                     PLAN APPROVAL WORKFLOW                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Sub-agents Complete → Plan Synthesized → Human Review              │
│                                                                      │
│  Human Options:                                                      │
│  ├── [Approve] - Execute plan as-is                                 │
│  ├── [Modify]  - Edit plan, then approve                            │
│  ├── [Reject]  - Back to specification phase                        │
│  └── [Escalate] - Create CRP for complex decisions                  │
│                                                                      │
│  Auto-Approve Mode (--auto):                                        │
│  └── Only for changes <15 LOC with 100% conformance pass            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 5. Optional: GitHub Check for Conformance

For PRs, add conformance check as GitHub Status Check:

```yaml
GitHub Check: plan-conformance
  Triggers: On PR open, on PR update
  Actions:
    - Extract changed files from PR diff
    - Run conformance check against ADRs
    - Report violations as check annotations

  Status:
    ✅ Pass: All changes conform to ADRs
    ⚠️ Warning: Minor deviations (advisory)
    ❌ Fail: Critical ADR violations (blocks merge)
```

---

## Model Selection Matrix

The planning phase should also apply task-type aware model routing:

| Task Type | Primary Model | Fallback | Reasoning |
|-----------|---------------|----------|-----------|
| Large Feature (>50 LOC, multi-file) | Claude Opus 4.5 | GPT 5.2 | Best at complex reasoning, multi-file refactoring |
| Small Fix (<15 LOC, single file) | Claude Sonnet 4.5 | Haiku 4.5 | Fast, accurate for targeted changes |
| Architecture & Debugging | GPT 5.2 | Claude Opus | Strong reasoning, different perspective helps |
| Design & Creativity | Gemini 3 Pro | Claude Opus | Large context, creative solutions |
| Quick Answers & Micro-edits | Claude Haiku 4.5 | Sonnet | Fastest response time |

**Expert Rule:** "Switch models when stuck - different model = different perspective"

---

## Implementation Phases

### Phase 1: Framework Documentation (Sprint 97)
- [x] ADR-034 created in SDLC-Enterprise-Framework ← THIS DOCUMENT
- [ ] Update CLAUDE.md with AI Best Practices 2026
- [ ] Document planning mode workflow in Core Methodology

### Phase 2: Orchestrator Backend (Sprint 98)
- [ ] PlanningOrchestratorService
- [ ] PatternExtractionService
- [ ] SubAgentManager
- [ ] API endpoints for planning mode

### Phase 3: Integration (Sprint 99)
- [ ] ConformanceCheckService
- [ ] Plan Approval UI component
- [ ] GitHub Check integration
- [ ] `sdlcctl plan` CLI command

### Phase 4: Feedback Loop (Sprint 100)
- [ ] `pr_learnings` table
- [ ] FeedbackLearningService
- [ ] Automated CLAUDE.md updates from PR reviews

---

## Consequences

### Positive

1. **Reduced Architectural Drift** - Plans validated against ADRs before implementation
2. **Better Pattern Reuse** - Sub-agents find existing patterns, reducing redundancy
3. **Faster Reviews** - Code follows discovered patterns, reviewers know what to expect
4. **Knowledge Capture** - Learnings from reviews feed back to context files
5. **Expert Workflow Parity** - Closes 8% gap with expert AI coding workflow
6. **Model Efficiency** - Task-appropriate models reduce cost and latency

### Negative

1. **Overhead for Small Changes** - Planning adds latency (mitigated by <15 LOC auto-skip)
2. **Sub-agent Costs** - Parallel exploration uses tokens (mitigated by Ollama primary)
3. **Learning Curve** - Teams need to understand planning workflow (mitigated by CLI)

### Risks

1. **Sub-agent Coordination** - Risk of conflicting patterns found (mitigated by synthesis logic)
2. **Over-planning** - Risk of excessive planning for simple tasks (mitigated by complexity threshold)
3. **Stale ADRs** - Plans may validate against outdated ADRs (mitigated by ADR review process)

---

## Success Metrics

| Metric | Current | Target | Method |
|--------|---------|--------|--------|
| Architectural drift rate | ~15% | <5% | PR review tracking |
| Pattern reuse rate | ~40% | >70% | Code analysis |
| First-pass review approval | ~60% | >85% | PR metrics |
| CLAUDE.md freshness | Manual | <7 days | Automated updates |
| Expert workflow alignment | 92% | 100% | Workflow audit |

---

## References

- **Expert AI Coding Workflow Analysis** - Internal research (January 2026)
- **SDLC 5.1.3 Core Methodology** - 7-Pillar Architecture
- **ADR-029** - AGENTS.md Migration
- **ADR-022** - EP-06 IR-Based Codegen
- **SASE Framework** - arXiv:2509.06216v2

---

## Document Control

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | Jan 22, 2026 | AI + CTO | Initial ADR - Sprint 97 deliverable |

**Review Schedule:**
- CTO Review: January 2026 - PENDING
- Implementation Review: March 2026 (Post Sprint 100)

---

**Document Status:** APPROVED
**Last Updated:** January 22, 2026
**Framework Alignment:** SDLC 5.1.3 (7-Pillar Architecture)
