# ADR-029: Migration from BRS/MTS/LPS to AGENTS.md Standard

**Status:** ACCEPTED  
**Date:** January 2026  
**Decision Makers:** CTO, Framework Architecture Team  
**Impact:** HIGH - Affects all SE3.0 agentic workflows

---

## Context

The SDLC 5.1.3 Framework originally defined three proprietary artifacts for AI agent coordination:

1. **BriefingScript (BRS)** - Task specifications for agents
2. **MentorScript (MTS)** - Code standards and best practices
3. **LoopScript (LPS)** - Execution plans and progress tracking

However, the industry has converged on **AGENTS.md** as the de facto standard for AI agent context files:

- **60,000+ projects** on GitHub use AGENTS.md
- **Native support** in Cursor, GitHub Copilot, Claude Code, Windsurf, OpenCode, Roo
- **Industry adoption** by major frameworks and tooling ecosystems
- **Standardization** through community consensus

**Problem:** Our proprietary BRS/MTS/LPS artifacts create:
- Tool fragmentation (no IDE support)
- Learning curve for developers
- Migration friction for teams
- Competitive disadvantage vs industry standard

---

## Decision

**We will migrate from BRS/MTS/LPS to AGENTS.md as the primary AI agent context artifact.**

### What Changes

| Aspect | Before (BRS/MTS/LPS) | After (AGENTS.md) |
|--------|---------------------|-------------------|
| **Primary Artifact** | BriefingScript + MentorScript + LoopScript | Single AGENTS.md file |
| **Tool Support** | None (proprietary) | Native in Cursor, Copilot, Claude Code |
| **Learning Curve** | High (3 new concepts) | Low (industry standard) |
| **Positioning** | "New methodology" | "Governance layer for AGENTS.md" |
| **Competitive Advantage** | Proprietary (weak) | Industry standard + governance (strong) |

### What Stays

**The following SASE governance artifacts remain ACTIVE:**

1. **CRP (Consultation Request Process)** - Human escalation for complex decisions
2. **MRP (Merge Request Process)** - Code review and approval workflow  
3. **VCR (Value Chain Record)** - Compliance and audit trail

**Rationale:** CRP/MRP/VCR are governance artifacts, not AI context files. They provide the "Operating System" layer that AGENTS.md lacks - gates, approvals, evidence chains, compliance tracking.

---

## Implementation

### Phase 1: Template Creation (COMPLETE ✅)

- Created `AGENTS-MD-Template.md` with comprehensive guidelines
- Added validation CLI (`sdlcctl agents validate`)
- Documented migration workflow in SASE-Artifacts/README.md

### Phase 2: Archive Legacy Artifacts (COMPLETE ✅)

Deprecated templates moved to `99-Legacy/SASE-Deprecated-Artifacts/`:
- `01-BriefingScript-Template.yaml`
- `02-LoopScript-Template.yaml`
- `03-MentorScript-Template.md`

### Phase 3: Documentation Updates (IN PROGRESS)

- [x] Framework README.md - Deprecation notice + AGENTS.md principle
- [x] SASE-Artifacts/README.md - Migration guide
- [ ] SDLC-Agentic-Core-Principles.md - Update terminology (P1)
- [ ] Other methodology docs referencing BRS/MTS/LPS (P4)

### Phase 4: Tool Integration (COMPLETE ✅)

SDLC Orchestrator already implements:
- AGENTS.md Generator (Sprint 80)
- Dynamic Context Overlay (Sprint 89)
- CLI validation (`sdlcctl agents validate`)

---

## Consequences

### Positive

1. **Industry Alignment** - Leverage 60K+ projects' momentum
2. **Tool Support** - Native IDE integration (Cursor, Copilot, etc.)
3. **Lower Barrier** - Developers already know AGENTS.md
4. **Unique Moat** - "Governance layer for AGENTS.md" is differentiated positioning
5. **Dynamic Context** - Gate-triggered updates (competitors lack this)

### Negative

1. **Terminology Shift** - Existing docs reference BRS/MTS/LPS
2. **Migration Effort** - Teams using old templates need guidance
3. **Learning Materials** - Some training content needs updates

### Mitigation

- Keep deprecated templates in `99-Legacy/` for reference
- Provide migration guide in SASE-Artifacts/README.md
- Update core methodology docs to reference AGENTS.md
- Clarify that CRP/MRP/VCR remain active (not deprecated)

---

## Decision Rationale

### Why AGENTS.md?

**Industry Standard:** 60K+ projects, native tool support, community consensus

**Better Positioning:** Instead of "yet another proprietary format", we become:
> "The Governance Layer for AGENTS.md"

This positions us as **complementary** to AI coding tools (Cursor, Copilot, OpenCode, Roo) rather than competing with them.

### Why Keep CRP/MRP/VCR?

**Governance Gap:** AGENTS.md is a context file, not a governance system. It lacks:
- Gate enforcement (Planning → Design → Build)
- Human approval workflows (VCR)
- Evidence chains (MRP with hash verification)
- Consultation escalation (CRP)

**Unique Moat:** Dynamic Context Engine that updates AGENTS.md based on gate status is a feature **no competitor has**. This is our true differentiator.

### Strategic Fit

| Layer | Artifact | Purpose |
|-------|----------|---------|
| **Context Layer** | AGENTS.md | AI agent instructions (industry standard) |
| **Governance Layer** | CRP/MRP/VCR | Gates, approvals, evidence (SDLC 5.1.3 unique) |
| **Dynamic Layer** | Context Overlay | Gate-triggered AGENTS.md updates (TRUE MOAT) |

---

## Migration Path

### For Existing Teams Using BRS/MTS/LPS

1. **Use migration tool:**
   ```bash
   sdlcctl agents migrate --from brs --to agents-md
   ```

2. **Manual migration:**
   - BriefingScript → AGENTS.md `## Project Context` + `## Tasks`
   - MentorScript → AGENTS.md `## Code Standards` + `## Best Practices`
   - LoopScript → Keep as LoopScript.yaml (execution tracking, not context)

3. **Governance unchanged:**
   - Continue using CRP for escalations
   - Continue using MRP for code reviews
   - Continue using VCR for approvals

### For New Projects

Start with AGENTS-MD-Template.md:
```bash
sdlcctl agents init
```

---

## References

- **Industry Standard:** 60K+ projects on GitHub use AGENTS.md
- **Tool Support:** Cursor, GitHub Copilot, Claude Code, Windsurf, OpenCode, Roo
- **Template:** `03-Templates-Tools/SASE-Artifacts/AGENTS-MD-Template.md`
- **Migration Guide:** `03-Templates-Tools/SASE-Artifacts/README.md`
- **Dynamic Context:** Sprint 89 (SDLC Orchestrator)
- **AGENTS.md Generator:** Sprint 80 (SDLC Orchestrator)

---

## Status Tracking

| Task | Status | Date |
|------|--------|------|
| Create AGENTS-MD-Template.md | ✅ Complete | Jan 2026 |
| Archive BRS/MTS/LPS templates | ✅ Complete | Jan 22, 2026 |
| Update Framework README.md | ✅ Complete | Jan 2026 |
| Update SASE-Artifacts/README.md | ✅ Complete | Jan 2026 |
| Create ADR-029 | ✅ Complete | Jan 22, 2026 |
| Update SDLC-Agentic-Core-Principles.md | 🚧 In Progress | Jan 22, 2026 |
| Update other methodology docs | 📋 Planned | TBD |
| Tool integration (Orchestrator) | ✅ Complete | Jan 2026 |

---

**Next Review Date:** March 2026 (Post Public Launch)

**Success Metrics:**
- All new projects start with AGENTS.md (not BRS/MTS/LPS)
- Tool adoption: 100% of teams using Cursor/Copilot benefit from native support
- Zero breaking changes for existing CRP/MRP/VCR workflows
