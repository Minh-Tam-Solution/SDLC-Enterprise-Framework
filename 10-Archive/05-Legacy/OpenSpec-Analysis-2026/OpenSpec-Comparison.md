# OpenSpec vs SDLC 6.0 Comparison Matrix
## Framework 6.0 Evaluation - Sprint 114 Day 4

**Version**: 1.0.0
**Date**: January 28, 2026
**Author**: PM/PJM Team
**Status**: COMPLETE

---

## 1. Executive Summary

This document provides a comprehensive comparison between OpenSpec CLI and SDLC Framework 6.0 Specification Standard to inform the Week 8 Gate decision (February 21, 2026).

**Key Finding**: OpenSpec and SDLC 6.0 are **complementary**, not competing. OpenSpec excels at proposal generation; SDLC 6.0 excels at governance and tier-awareness.

---

## 2. Feature Comparison Matrix

### 2.1 Core Capabilities

| Feature | OpenSpec | SDLC 6.0 | Winner | Notes |
|---------|----------|----------|--------|-------|
| **Specification Format** | Markdown | Markdown + YAML | SDLC 6.0 | YAML frontmatter for automation |
| **AI-Parseability** | Good | Excellent | SDLC 6.0 | Structured metadata extraction |
| **Requirements Format** | Scenarios | BDD (GIVEN-WHEN-THEN) | SDLC 6.0 | Industry standard BDD |
| **Tier Classification** | None | LITE/STD/PRO/ENT | SDLC 6.0 | Critical for enterprise |
| **Stage Awareness** | None | 00-10 SDLC stages | SDLC 6.0 | Lifecycle integration |
| **ADR Integration** | design.md | Linked references | SDLC 6.0 | Traceability |
| **Version Tracking** | Archive folder | SPEC_DELTA.md | Tie | Different approaches |
| **Proposal Generation** | Automated | Manual | OpenSpec | AI-assisted creation |
| **Fast-Forward Mode** | /opsx:ff | None | OpenSpec | Rapid planning |
| **Multi-Tool Support** | 26+ tools | Any AI | OpenSpec | Broader compatibility |

### 2.2 Workflow Capabilities

| Feature | OpenSpec | SDLC 6.0 | Winner | Notes |
|---------|----------|----------|--------|-------|
| **Initialization** | CLI command | Manual template | OpenSpec | Faster setup |
| **Artifact Generation** | Automated | Template-based | OpenSpec | AI-driven |
| **Iteration Support** | Built-in | Manual update | OpenSpec | Phase flexibility |
| **Archival System** | Timestamped | Version control | Tie | Both effective |
| **Governance Hooks** | None | OPA + Evidence | SDLC 6.0 | Enterprise governance |
| **Quality Gates** | None | 4-Gate Pipeline | SDLC 6.0 | Automated validation |
| **Vibecoding Detection** | None | Index calculation | SDLC 6.0 | Anti-vibecoding |

### 2.3 Enterprise Features

| Feature | OpenSpec | SDLC 6.0 | Winner | Notes |
|---------|----------|----------|--------|-------|
| **Tier Requirements** | Not supported | Full support | SDLC 6.0 | Enterprise scaling |
| **Compliance Audit** | Limited | Full audit trail | SDLC 6.0 | SOC 2/HIPAA ready |
| **Role-Based Access** | None | RBAC (13 roles) | SDLC 6.0 | Security |
| **Evidence Storage** | Git only | Evidence Vault | SDLC 6.0 | Immutable storage |
| **Approval Workflow** | None | Tiered approval | SDLC 6.0 | Governance |
| **Kill Switch** | None | Automatic | SDLC 6.0 | Safety mechanism |

### 2.4 Developer Experience

| Feature | OpenSpec | SDLC 6.0 | Winner | Notes |
|---------|----------|----------|--------|-------|
| **Learning Curve** | Low (3 commands) | Medium (9 sections) | OpenSpec | Simpler workflow |
| **Documentation** | Good | Comprehensive | SDLC 6.0 | More examples |
| **Output Verbosity** | Concise (~250 LOC) | Detailed (~350 LOC) | Context-dependent | Trade-off |
| **Speed** | Fast | Standard | OpenSpec | AI-generated |
| **Flexibility** | High | Structured | OpenSpec | Less rigid |
| **Brownfield Support** | Excellent | Good | OpenSpec | Designed for legacy |

---

## 3. Artifact Format Comparison

### 3.1 Proposal/Overview Section

**OpenSpec proposal.md**:
```markdown
# Add Dark Mode

## Summary
Implement dark mode toggle in application settings.

## Business Rationale
- User feedback requests dark mode
- Competitive parity

## Scope
### In Scope
- Theme toggle component

### Out of Scope
- System preference detection
```

**SDLC 6.0 Overview Section**:
```markdown
---
spec_id: SPEC-0042
spec_version: "1.0.0"
status: draft
tier: STANDARD
stage: "03"
owner: "frontend-team"
created: 2026-01-28
---

## 1. Overview

Add Dark Mode provides theme switching capability for users.

**Key Objectives**:
- Enable dark mode toggle
- Persist user preference

**Scope**:
- **In Scope**: Theme toggle, CSS variables
- **Out of Scope**: System preference detection
```

**Analysis**: SDLC 6.0 adds structured metadata (tier, stage, owner) critical for automation and governance. OpenSpec is more concise but lacks governance hooks.

### 3.2 Technical Decisions

**OpenSpec design.md**:
```markdown
# Technical Approach

## Architecture
- Use CSS custom properties for theming
- Store preference in localStorage

## Trade-offs
- CSS variables: broader support vs. dynamic theming
```

**SDLC 6.0 Design Decisions Section**:
```markdown
## 4. Design Decisions

### 4.1 Related ADRs

| ADR | Title | Status | Impact |
|-----|-------|--------|--------|
| ADR-015 | Theme System | Accepted | CSS variables |

### 4.2 Key Decisions

#### Decision 1: CSS Custom Properties
- **Status**: Decided
- **ADR Reference**: ADR-015
- **Summary**: CSS variables for theming
- **Impact**: Enables runtime switching
```

**Analysis**: SDLC 6.0 enforces ADR traceability, critical for architectural consistency.

### 3.3 Tasks/Acceptance Criteria

**OpenSpec tasks.md**:
```markdown
# Implementation Tasks

## Phase 1: Foundation
1.1 Add ThemeContext provider
1.2 Create useTheme hook

## Phase 2: UI
2.1 Add toggle switch component
2.2 Integrate with settings page
```

**SDLC 6.0 Acceptance Criteria Section**:
```markdown
## 6. Acceptance Criteria

| ID | Criterion | Test Type | Priority |
|----|-----------|-----------|----------|
| AC-001 | Toggle switches theme | E2E | P0 |
| AC-002 | Preference persists | Integration | P0 |
| AC-003 | No flash on load | Unit | P1 |

### Definition of Done
- [ ] All P0 criteria pass
- [ ] Code review approved (2+)
- [ ] Documentation updated
```

**Analysis**: OpenSpec uses numbered tasks for implementation; SDLC 6.0 uses testable acceptance criteria with priorities.

---

## 4. Integration Effort Assessment

### 4.1 Option A: Adopt OpenSpec + Extend

**Integration Tasks**:

| Task | Effort | Complexity |
|------|--------|------------|
| Install OpenSpec CLI | 0.5 days | Low |
| Create YAML frontmatter extension | 2 days | Medium |
| Add tier/stage classification | 2 days | Medium |
| ADR linking mechanism | 1 day | Low |
| Orchestrator governance hooks | 3 days | High |
| Format conversion utilities | 2 days | Medium |
| Testing & documentation | 2 days | Medium |

**Total Effort**: 12.5 days
**Risk Level**: Medium

### 4.2 Option B: Extend SDLC 6.0 (Custom)

**Development Tasks**:

| Task | Effort | Complexity |
|------|--------|------------|
| Proposal generation AI | 4 days | High |
| Fast-forward mode | 3 days | High |
| CLI tool (sdlcctl spec new) | 3 days | Medium |
| Multi-tool integration | 4 days | High |
| Archival system | 2 days | Medium |
| Testing & documentation | 2 days | Medium |

**Total Effort**: 18 days
**Risk Level**: High (building from scratch)

### 4.3 Option C: Hybrid Approach (Recommended)

**Best-of-Both Tasks**:

| Task | Effort | Complexity |
|------|--------|------------|
| Use OpenSpec for proposal phase | 0.5 days | Low |
| Convert OpenSpec → SDLC 6.0 format | 3 days | Medium |
| Governance layer (SDLC 6.0) | 2 days | Medium |
| Validation integration | 2 days | Medium |
| Testing & documentation | 2 days | Medium |

**Total Effort**: 9.5 days
**Risk Level**: Low

---

## 5. Pros and Cons Analysis

### 5.1 OpenSpec Adoption

**Pros**:
- ✅ Faster proposal generation (AI-driven)
- ✅ Low learning curve (3 commands)
- ✅ Active community (20K+ stars)
- ✅ MIT license (commercial-safe)
- ✅ Multi-tool support (26+ AI assistants)
- ✅ Brownfield-first design
- ✅ Concise output

**Cons**:
- ❌ No tier classification
- ❌ No SDLC stage awareness
- ❌ No governance hooks
- ❌ No ADR traceability
- ❌ No quality gate integration
- ❌ External dependency risk
- ❌ Format conversion overhead

### 5.2 SDLC 6.0 Custom Development

**Pros**:
- ✅ Full governance integration
- ✅ Tier-aware requirements
- ✅ Stage-aware workflow
- ✅ ADR traceability
- ✅ Evidence Vault integration
- ✅ Quality gate hooks
- ✅ No external dependencies

**Cons**:
- ❌ Higher development effort
- ❌ Slower initial setup
- ❌ Manual artifact creation
- ❌ Less AI automation
- ❌ Steeper learning curve
- ❌ Maintenance burden

### 5.3 Hybrid Approach

**Pros**:
- ✅ Best of both worlds
- ✅ Fast proposal with OpenSpec
- ✅ Full governance with SDLC 6.0
- ✅ Lower effort than custom build
- ✅ Reduced risk
- ✅ Industry alignment

**Cons**:
- ⚠️ Format conversion step
- ⚠️ Two systems to maintain
- ⚠️ Training on both tools

---

## 6. Decision Criteria Matrix

| Criterion | Weight | OpenSpec | SDLC 6.0 | Hybrid |
|-----------|--------|----------|----------|--------|
| Developer Experience | 20% | 9/10 | 7/10 | 8/10 |
| Governance Integration | 25% | 3/10 | 10/10 | 9/10 |
| Implementation Effort | 15% | 8/10 | 5/10 | 9/10 |
| Enterprise Readiness | 20% | 4/10 | 10/10 | 9/10 |
| AI Tool Compatibility | 10% | 10/10 | 7/10 | 9/10 |
| Long-term Maintenance | 10% | 7/10 | 8/10 | 7/10 |
| **Weighted Score** | **100%** | **6.1** | **7.9** | **8.6** |

---

## 7. Gap Summary

### 7.1 OpenSpec Gaps (Bridgeable)

| Gap | SDLC 6.0 Solution | Bridge Effort |
|-----|-------------------|---------------|
| No tier classification | YAML frontmatter tier field | Low |
| No stage awareness | YAML frontmatter stage field | Low |
| No ADR linking | related_adrs field | Low |
| No governance hooks | Orchestrator wrapper | Medium |
| No quality gates | 4-Gate pipeline integration | Medium |
| Format differences | Conversion utility | Medium |

### 7.2 SDLC 6.0 Gaps (Addressable)

| Gap | OpenSpec Solution | Address Effort |
|-----|-------------------|----------------|
| Manual creation | /opsx:new automation | Low (adopt OpenSpec) |
| No fast-forward | /opsx:ff | Low (adopt OpenSpec) |
| Slower iteration | OpenSpec workflow | Low (adopt OpenSpec) |

---

## 8. Recommendation Summary

Based on the comparison matrix, the **Hybrid Approach** scores highest (8.6/10):

1. **Use OpenSpec** for proposal and initial planning phases
2. **Convert to SDLC 6.0 format** for governance and storage
3. **Integrate with Orchestrator** for quality gates and evidence

This approach provides:
- Fast proposal generation (OpenSpec strength)
- Full governance integration (SDLC 6.0 strength)
- Tier and stage awareness (SDLC 6.0 strength)
- AI tool compatibility (OpenSpec strength)

**Week 8 Gate Recommendation**: **EXTEND** (Hybrid Approach)
- Adopt OpenSpec for planning phase
- Extend SDLC 6.0 for governance phase
- Build conversion layer in Sprint 117-119

---

## 9. References

- [OpenSpec Official Site](https://openspec.dev/)
- [SDLC 6.0 Specification Standard](./SDLC-Specification-Standard.md)
- [OpenSpec POC Results](./OpenSpec-POC-Results.md)

---

*Comparison Matrix created as part of Sprint 114 Track 1 Day 4*
*SDLC Enterprise Framework 6.0 Evaluation*
