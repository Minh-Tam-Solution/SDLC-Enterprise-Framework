# RFC-SDLC-607: Explanatory Documentation Pattern

**Status**: 📋 DRAFT
**Created**: March 6, 2026
**Author**: Framework Architect + Documentation Team
**Sprint**: 143 - Framework-First Track 1
**Related**: Boris Cherny Tactics Analysis (Partial Gap - Learn with Claude)
**Framework Version**: SDLC 6.0.3

---

## 1. Problem Statement

### Current Challenge

Technical documentation in software projects is typically **text-heavy markdown** without visual aids, making it difficult for new team members to quickly understand:
- Architectural decisions (why X was chosen over Y)
- Complex workflows (authentication flows, deployment pipelines)
- Code relationships (which modules depend on which)
- Decision timelines (when and why decisions were made)

**Current Documentation** (Text-Only):
```markdown
## Authentication Flow

1. User submits login credentials
2. Server validates username and password
3. If valid, server generates JWT token
4. Client stores token in localStorage
5. Subsequent requests include token in Authorization header

(No diagrams, no visualization, no decision context)
```

**Problem**: New developers spend **hours reading** to understand what a **single diagram** could explain in minutes.

### Boris Cherny Insight

Boris Cherny recommends:
> "Bật chế độ 'Explanatory', yêu cầu tạo HTML presentations hoặc ASCII diagrams."
> (Translation: "Enable 'Explanatory' mode, request HTML presentations or ASCII diagrams.")

**Key Insight**: AI can generate **visual, interactive documentation** (ASCII diagrams, HTML presentations) that explain architectural decisions and workflows far better than text alone.

### Gap Analysis

**Current State** (SDLC Orchestrator v1.6.0):
- ✅ Evidence-based development (all decisions documented)
- ✅ Skills explain methodology (tool-agnostic)
- ❌ **No explicit "explanatory mode" in CLI**
- ❌ No ASCII diagram generation
- ❌ No HTML presentation creation

**Industry Practice**:
- Standard: Markdown documentation
- Advanced: Mermaid diagrams (some tools)
- Best-in-class: Boris Cherny's explanatory mode

**Competitive Advantage**: Auto-generate visual documentation from Evidence Vault

---

## 2. Current State

### Evidence Vault Documentation (Text-Based)

**Evidence artifacts are JSON** (machine-readable, not human-friendly):
```json
{
  "artifact_id": "EVD-2026-03-001",
  "type": "architecture_decision",
  "decision": "Use JWT for authentication",
  "rationale": "Stateless, scalable, industry standard",
  "alternatives": ["Session cookies", "OAuth only"],
  "tradeoffs": "Token size larger than session ID"
}
```

**Problem**: Developers must manually parse JSON to understand decisions.

### ADRs (Standard Markdown)

**ADR-041: Progressive Routing** (standard format):
```markdown
# ADR-041: Progressive Routing

## Context
Need to categorize requirements by complexity...

## Decision
Use 4-zone progressive routing (Green/Yellow/Orange/Red)...

## Consequences
- Pro: Automatic categorization
- Con: Requires configuration
```

**Problem**: No diagrams, no decision timeline visualization.

---

## 3. Proposed Pattern

### 3.1 Explanatory Documentation Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ EVIDENCE VAULT (Source of Truth)                                │
│  - Architecture Decision Records (ADRs)                          │
│  - Evidence Artifacts (JSON)                                     │
│  - Sprint Plans, Design Specs                                   │
├─────────────────────────────────────────────────────────────────┤
│ EXPLANATORY GENERATOR (New Component)                           │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ 1. Read Evidence Artifacts                                │   │
│  │    - Parse JSON metadata                                  │   │
│  │    - Extract decisions, tradeoffs, timelines              │   │
│  └────────────────────┬─────────────────────────────────────┘   │
│  ┌────────────────────▼─────────────────────────────────────┐   │
│  │ 2. Generate ASCII Diagram                                 │   │
│  │    - Sequence diagrams (authentication flow)              │   │
│  │    - Architecture diagrams (service dependencies)         │   │
│  │    - Decision trees (Progressive Routing zones)           │   │
│  └────────────────────┬─────────────────────────────────────┘   │
│  ┌────────────────────▼─────────────────────────────────────┐   │
│  │ 3. Generate HTML Presentation (Optional)                  │   │
│  │    - Timeline view (decision history)                     │   │
│  │    - Interactive decision tree                            │   │
│  │    - Slide deck (onboarding)                              │   │
│  └────────────────────┬─────────────────────────────────────┘   │
├────────────────────────┴──────────────────────────────────────────┤
│ OUTPUT (Human-Friendly Documentation)                            │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐             │
│  │ASCII Diagrams│ │ HTML Slides  │ │ Markdown +   │             │
│  │(in markdown) │ │(standalone)  │ │ Embedded SVG │             │
│  └──────────────┘ └──────────────┘ └──────────────┘             │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Output Formats

#### Format 1: ASCII Diagram (Embedded in Markdown)

**Example: Progressive Routing Zones**

```
sdlcctl explain --decision ADR-041 --format ascii

Output:
┌──────────────────────────────────────────────────────────────┐
│           Progressive Routing Zones (ADR-041)                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  🟢 GREEN (0-30)                                             │
│  ├─ Auto-approve (trivial changes)                           │
│  ├─ Examples: Typo fixes, comment updates                    │
│  └─ Review: None required                                    │
│                                                              │
│  🟡 YELLOW (30-60)                                           │
│  ├─ Quick review (standard changes)                          │
│  ├─ Examples: New features, refactoring                      │
│  └─ Review: Tech Lead (15 min)                               │
│                                                              │
│  🟠 ORANGE (60-80)                                           │
│  ├─ Deep review (complex changes)                            │
│  ├─ Examples: API contracts, database schema                 │
│  └─ Review: Tech Lead + Senior Dev (1 hour)                  │
│                                                              │
│  🔴 RED (80+)                                                │
│  ├─ Full audit (security/architecture)                       │
│  ├─ Examples: Auth system, payment logic                     │
│  └─ Review: CTO + Security Lead (4 hours)                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

#### Format 2: Sequence Diagram (Authentication Flow)

```
sdlcctl explain --feature "user-auth" --format ascii

Output:
User          Frontend        Backend         Database
 │               │               │               │
 │ 1. Login      │               │               │
 ├──────────────>│               │               │
 │               │ 2. POST /auth/login           │
 │               ├──────────────>│               │
 │               │               │ 3. Query user │
 │               │               ├──────────────>│
 │               │               │<──────────────┤
 │               │               │ 4. bcrypt verify
 │               │               │               │
 │               │ 5. JWT token  │               │
 │               │<──────────────┤               │
 │ 6. Token      │               │               │
 │<──────────────┤               │               │
 │               │               │               │
```

#### Format 3: HTML Presentation (Decision Timeline)

```bash
sdlcctl explain --timeline --from "2025-11-01" --to "2026-03-01" --format html

Output: decision-timeline.html (standalone)
```

**HTML Presentation Content**:
- **Slide 1**: Project Overview (Nov 2025 - Mar 2026)
- **Slide 2**: Gate G1 Approval (Legal + Market Validation)
- **Slide 3**: Gate G2 Design Ready (ADR-041: Progressive Routing)
- **Slide 4**: Sprint 139-141 (E2E API Testing)
- **Slide 5**: Sprint 142 (Test Remediation)
- **Slide 6**: Sprint 143 (Boris Cherny Tactics - Framework-First)
- **Slide 7**: Gate G3 Ship Ready (98.2% compliance)

**Interactive Features**:
- Click ADR to see full decision
- Hover timeline to see Evidence artifacts
- Filter by category (security, architecture, process)

### 3.3 Use Cases

| Use Case | Format | When | Who |
|----------|--------|------|-----|
| **Onboarding** | ASCII + Markdown | New team member joins | All developers |
| **Knowledge Transfer** | HTML Presentation | Tech Lead leaves project | Team Lead |
| **Architecture Review** | ASCII Diagram | Gate G2 (Design Ready) | Architect, CTO |
| **Training Materials** | HTML Slides | Workshop, conference | Training team |
| **Decision History** | Timeline | Retrospective, audit | PM, CTO |

---

## 4. Integration with SDLC Framework

### 4.1 Evidence Vault Integration

**All explanations reference Evidence artifacts**:

```markdown
# Authentication Flow (Generated)

[ASCII diagram above]

## Evidence Artifacts Referenced:
- EVD-2026-01-042: ADR-041 Progressive Routing decision
- EVD-2026-02-015: Sprint 141 E2E Testing completion
- EVD-2026-03-001: User auth implementation plan

## Traceability:
- Decision made: 2026-01-18 (ADR-041)
- Approved by: CTO @nqh
- Evidence hash: sha256:a3f5b2...
- Signature: ed25519:8c9d1e...
```

**Benefit**: Visual documentation is **traceable** to Evidence artifacts.

### 4.2 Stage 09 (Govern) - Knowledge Management

**Explanatory Documentation fits Stage 09**:
- **Purpose**: Governance, knowledge retention, onboarding
- **When**: Continuous (especially after major decisions)
- **Output**: Visual documentation, presentations

### 4.3 Generated Documentation Artifacts

**Each explanatory document becomes Evidence artifact**:
```json
{
  "artifact_id": "EVD-2026-03-007",
  "type": "explanatory_documentation",
  "format": "ascii_diagram",
  "source_decision": "ADR-041",
  "generated_at": "2026-03-06T10:00:00Z",
  "diagram_path": "docs/09-govern/Diagrams/Progressive-Routing.md",
  "signature": "ed25519:..."
}
```

---

## 5. Tool-Agnostic Implementation

### 5.1 Works with Any AI Tool

**ASCII diagrams are text** (tool-agnostic):
- Claude Code can generate ASCII diagrams
- Cursor can generate ASCII diagrams
- Any AI tool with text generation

**No vendor lock-in**: ASCII is plain text.

### 5.2 Manual Creation (No Automation)

Teams can create explanatory docs **manually**:
```bash
# Manual ASCII diagram creation
vim docs/Architecture-Diagram.md
# Draw ASCII diagram manually
```

Or use tools like:
- **asciiflow.com** - Web-based ASCII diagram tool
- **PlantUML** - Text-to-diagram converter
- **Mermaid.js** - Markdown diagram syntax

---

## 6. Tradeoffs and Alternatives

### 6.1 Alternatives Considered

| Alternative | Pros | Cons | Decision |
|-------------|------|------|----------|
| **Text-Only Markdown** | Simple | Not visual | ❌ Reject (status quo) |
| **Mermaid.js** | Nice diagrams | Limited to Mermaid syntax | 🟡 Complementary |
| **PlantUML** | Powerful | Java dependency | 🟡 Complementary |
| **ASCII Diagrams** | Universal, simple | Lower visual quality | ✅ **Approved** (primary) |
| **HTML Presentations** | Interactive | Requires web server | ✅ **Approved** (optional) |

### 6.2 Tradeoffs Accepted

**Costs**:
- **Development**: 300 LOC, 12 hours (Sprint 144)
- **Learning Curve**: ASCII diagram syntax (1 hour)

**Benefits**:
- **Onboarding Speed**: 2 hours → 30 minutes (with diagrams)
- **Knowledge Retention**: Visual memory > text memory
- **Decision Clarity**: Diagrams explain tradeoffs visually

---

## 7. Decision

### 7.1 Recommendation

**APPROVE** Explanatory Documentation Pattern for SDLC Framework 6.0.3.

**Reasoning**:
1. ✅ Addresses Partial Gap (Learn with Claude - explanatory mode)
2. ✅ Tool-agnostic (ASCII diagrams are text)
3. ✅ Evidence Vault integration (traceable diagrams)
4. ✅ Low cost, high value (faster onboarding)
5. ✅ Incremental adoption (manual → automated)

### 7.2 Implementation Roadmap

**Track 1 (Sprint 143)**: ✅ **This RFC** (methodology documentation)
**Track 2 (Sprint 144)**: CLI implementation (conditional on Track 1 approval)

**Sprint 144 Implementation**:
```yaml
Component: Explanatory Generator
LOC: 300
Effort: 12 hours
Files:
  - sdlcctl/lib/diagram_generator.py (150 LOC)
  - sdlcctl/commands/explain.py (150 LOC)
CLI Commands:
  - sdlcctl explain --decision ADR-041 --format ascii
  - sdlcctl explain --feature "user-auth" --format ascii
  - sdlcctl explain --timeline --from DATE --to DATE --format html
```

### 7.3 Success Criteria

**Track 1 Success** (Sprint 143):
- ✅ RFC approved by CTO
- ✅ Diagram formats defined (ASCII, HTML)
- ✅ Tool-agnostic validation passed

**Track 2 Success** (Sprint 144):
- ✅ First ASCII diagram generated (Progressive Routing)
- ✅ First HTML presentation created (Decision timeline)
- ✅ Onboarding time reduced (2h → 30min measured)
- ✅ Evidence artifacts for all diagrams

---

## 8. Appendices

### A. ASCII Diagram Library

**Recommended ASCII diagram tools**:
- **Box Drawing**: Unicode characters (┌─┐│└┘)
- **Arrows**: Unicode arrows (→ ← ↑ ↓)
- **Emojis**: Zone indicators (🟢 🟡 🟠 🔴)

**Example Template**:
```
┌─────────────────┐
│ Component A     │
│ - Property 1    │
│ - Property 2    │
└────────┬────────┘
         │
         ▼
┌────────┴────────┐
│ Component B     │
└─────────────────┘
```

### B. References

- [Boris Cherny Implementation Plan](/home/dttai/.claude/plans/parallel-painting-turing.md)
- [Evidence Vault Specification](../../02-design/14-Technical-Specs/Evidence-Vault-Spec.md)
- [ASCII Flow](https://asciiflow.com/)
- [PlantUML](https://plantuml.com/)
- [Mermaid.js](https://mermaid.js.org/)

---

**RFC Status**: 📋 DRAFT → ⏳ CTO REVIEW → ✅ APPROVED → 🔄 IMPLEMENTED
**Current Phase**: Track 1 (Methodology Documentation)
**Next Phase**: Track 2 (Implementation - Sprint 144, conditional)

**Framework-First Compliance**: ✅ VERIFIED
**Tool-Agnostic**: ✅ VERIFIED
**Boris Cherny Coverage**: ✅ Partial Gap Addressed

---

*SDLC Framework 6.0.3 - Explanatory Documentation Pattern*
