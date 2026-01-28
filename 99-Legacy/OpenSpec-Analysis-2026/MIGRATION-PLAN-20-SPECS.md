# Framework 6.0 Migration Plan: 20 Priority Specifications
## Sprint 116-118 Track 1 Execution

**Version**: 1.0.0
**Status**: APPROVED
**Created**: January 28, 2026
**Author**: PM/PJM Team
**Framework**: SDLC 5.3.0 → 6.0.0

---

## 1. Executive Summary

This document identifies and prioritizes **20 specifications** for migration to SDLC Framework 6.0 format. Specs are selected based on:

- **Active Development**: Currently used in Sprint 114-119
- **Governance Critical**: Core to Anti-Vibecoding system
- **Reference Frequency**: Frequently linked by other specs/code
- **Compliance Impact**: Required for audit/governance

**Timeline**: Sprint 117-118 (Feb 24 - Mar 7, 2026)
**Effort**: 10 days @ 60% Track 1 capacity

---

## 2. Priority Matrix

### 2.1 Priority Tiers

| Tier | Priority | Count | Criteria | Sprint |
|------|----------|-------|----------|--------|
| **P0** | Critical | 5 | Active governance, blocking | 117 Week 1 |
| **P1** | High | 7 | Core architecture, frequent reference | 117 Week 1-2 |
| **P2** | Medium | 5 | Supporting specs, API contracts | 118 Week 1 |
| **P3** | Standard | 3 | Nice-to-have, lower impact | 118 Week 2 |

### 2.2 Selection Criteria Scoring

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Active Development | 30% | Used in current sprints |
| Governance Critical | 25% | Core to quality gates |
| Reference Frequency | 20% | Linked by other specs |
| Compliance Impact | 15% | Audit/regulatory need |
| Migration Complexity | 10% | Effort to convert (inverse) |

---

## 3. P0 - Critical Priority (5 Specs)

### 3.1 Governance-System-Implementation-Spec.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Type** | Technical Specification |
| **Lines** | ~400 |
| **Priority Score** | 95/100 |
| **Sprint** | 117 Day 1 |

**Rationale**: Core governance spec - Vibecoding Index, routing logic, enforcement modes. Active in Sprint 114-116.

**Migration Tasks**:
- [ ] Add YAML frontmatter (spec_id, tier, stage)
- [ ] Convert requirements to BDD format
- [ ] Add tier-specific requirements (SOFT/FULL modes)
- [ ] Link to ADR-035, ADR-036

---

### 3.2 Quality-Gates-Codegen-Specification.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Type** | Technical Specification |
| **Lines** | ~350 |
| **Priority Score** | 92/100 |
| **Sprint** | 117 Day 1 |

**Rationale**: 4-Gate Pipeline (Syntax → Security → Context → Tests). Core to EP-06 codegen.

**Migration Tasks**:
- [ ] Add YAML frontmatter
- [ ] Document gate-specific requirements (BDD)
- [ ] Add validation timing requirements
- [ ] Link to ADR-022

---

### 3.3 ADR-007-AI-Context-Engine.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/01-ADRs/ |
| **Type** | Architecture Decision Record |
| **Lines** | ~200 |
| **Priority Score** | 90/100 |
| **Sprint** | 117 Day 1 |

**Rationale**: Multi-provider AI integration (Ollama → Claude). Referenced by 15+ specs.

**Migration Tasks**:
- [ ] Add ADR-specific frontmatter
- [ ] Standardize decision format
- [ ] Add consequences section
- [ ] Link to related specs

---

### 3.4 Policy-Guards-Design.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Type** | Technical Specification |
| **Lines** | ~300 |
| **Priority Score** | 88/100 |
| **Sprint** | 117 Day 2 |

**Rationale**: OPA integration, policy evaluation. Active in Sprint 43-44.

**Migration Tasks**:
- [ ] Add YAML frontmatter
- [ ] Convert policy rules to BDD scenarios
- [ ] Add tier requirements (policy packs per tier)
- [ ] Link to ADR-036

---

### 3.5 System-Architecture-Document.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/02-System-Architecture/ |
| **Type** | Architecture Document |
| **Lines** | ~500 |
| **Priority Score** | 87/100 |
| **Sprint** | 117 Day 2 |

**Rationale**: 5-Layer architecture reference. Foundation for all other specs.

**Migration Tasks**:
- [ ] Add YAML frontmatter (spec_version, tier: ALL)
- [ ] Standardize layer descriptions
- [ ] Add component acceptance criteria
- [ ] Link to all related ADRs

---

## 4. P1 - High Priority (7 Specs)

### 4.1 ADR-022-Multi-Provider-Codegen-Architecture.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/01-ADRs/ |
| **Priority Score** | 85/100 |
| **Sprint** | 117 Day 3 |

**Rationale**: IR-based codegen architecture. Core to EP-06.

---

### 4.2 AGENTS-MD-Technical-Design.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 84/100 |
| **Sprint** | 117 Day 3 |

**Rationale**: Context Authority foundation. Links to CONTEXT_AUTHORITY_METHODOLOGY.

---

### 4.3 ADR-036-4-Tier-Policy-Enforcement.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/01-ADRs/ |
| **Priority Score** | 82/100 |
| **Sprint** | 117 Day 4 |

**Rationale**: Tier-based enforcement (LITE/STANDARD/PRO/ENTERPRISE).

---

### 4.4 Codegen-Service-Specification.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 80/100 |
| **Sprint** | 117 Day 4 |

**Rationale**: Code generation service. Active development.

---

### 4.5 IR-Processor-Specification.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 78/100 |
| **Sprint** | 117 Day 5 |

**Rationale**: Intermediate Representation processor. EP-06 core.

---

### 4.6 ADR-012-AI-Task-Decomposition.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/01-ADRs/ |
| **Priority Score** | 76/100 |
| **Sprint** | 117 Day 5 |

**Rationale**: AI council decomposition. CEO brain encoding.

---

### 4.7 Validation-Pipeline-Interface.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 75/100 |
| **Sprint** | 118 Day 1 |

**Rationale**: Validation pipeline for code quality.

---

## 5. P2 - Medium Priority (5 Specs)

### 5.1 Teams-Data-Model-Specification.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 72/100 |
| **Sprint** | 118 Day 1 |

---

### 5.2 ADR-028-Teams-Feature-Architecture.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/01-ADRs/ |
| **Priority Score** | 70/100 |
| **Sprint** | 118 Day 2 |

---

### 5.3 Planning-Orchestrator-Service-Design.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 68/100 |
| **Sprint** | 118 Day 2 |

---

### 5.4 ADR-013-Planning-Hierarchy.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/01-ADRs/ |
| **Priority Score** | 66/100 |
| **Sprint** | 118 Day 3 |

---

### 5.5 Governance-Metrics-Collection-Specification.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 65/100 |
| **Sprint** | 118 Day 3 |

---

## 6. P3 - Standard Priority (3 Specs)

### 6.1 ADR-029-AGENTS-MD-Integration-Strategy.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/01-ADRs/ |
| **Priority Score** | 62/100 |
| **Sprint** | 118 Day 4 |

---

### 6.2 Feedback-Learning-Service-Design.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 60/100 |
| **Sprint** | 118 Day 4 |

---

### 6.3 Conformance-Check-Service-Design.md

| Field | Value |
|-------|-------|
| **Path** | docs/02-design/14-Technical-Specs/ |
| **Priority Score** | 58/100 |
| **Sprint** | 118 Day 5 |

---

## 7. Migration Checklist Template

### 7.1 Per-Spec Migration Checklist

```yaml
Migration Checklist: [SPEC-NAME]

Pre-Migration:
  [ ] Read existing spec completely
  [ ] Identify requirements (functional/non-functional)
  [ ] List related ADRs/specs
  [ ] Determine tier classification

Frontmatter:
  [ ] Add spec_id (SPEC-NNNN)
  [ ] Add spec_name
  [ ] Add spec_version (start at 1.0.0)
  [ ] Set status (draft → approved when reviewed)
  [ ] Set tier (LITE/STANDARD/PROFESSIONAL/ENTERPRISE or ALL)
  [ ] Set stage (00-10)
  [ ] Set category (functional/technical/security)
  [ ] Add owner
  [ ] Add created/last_updated dates
  [ ] Link related_adrs
  [ ] Link related_specs

Content Structure:
  [ ] Section 1: Overview (concise, 2-3 paragraphs)
  [ ] Section 2: Context (problem, stakeholders)
  [ ] Section 3: Requirements (BDD format)
  [ ] Section 4: Design Decisions (ADR references)
  [ ] Section 5: Technical Specification
  [ ] Section 6: Acceptance Criteria (table format)
  [ ] Section 7: Spec Delta (if updating existing spec)
  [ ] Section 8: Dependencies
  [ ] Section 9: Appendix (if needed)

Requirements Conversion:
  [ ] Convert each requirement to BDD format
  [ ] Add priority (P0/P1/P2/P3)
  [ ] Add tier applicability
  [ ] Add rationale
  [ ] Add verification method

Validation:
  [ ] Run sdlcctl spec validate [file]
  [ ] Fix any validation errors
  [ ] Self-review against template
  [ ] Peer review
  [ ] Tech Lead approval

Post-Migration:
  [ ] Update CONTENT-MAP.md
  [ ] Update any linking specs
  [ ] Commit with proper message
  [ ] Announce to team
```

### 7.2 BDD Conversion Template

**Before (Legacy Format)**:
```markdown
## Requirements

- The system shall authenticate users via OAuth
- Password must be at least 12 characters
- Sessions expire after 15 minutes
```

**After (Framework 6.0 BDD)**:
```markdown
## 3. Requirements

### 3.1 Functional Requirements

#### FR-001: OAuth Authentication
**Priority**: P0
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN a user with a valid GitHub account
  AND the user is not currently logged in
WHEN the user clicks "Login with GitHub"
  AND authorizes the application
THEN the user is redirected to the dashboard
  AND a session token is issued with 15-minute expiry
```

**Rationale**: OAuth provides secure, passwordless authentication
**Verification**: Integration test with GitHub OAuth flow
```

---

## 8. Effort Estimation

### 8.1 Per-Spec Effort Matrix

| Spec Size | Lines | Effort | Description |
|-----------|-------|--------|-------------|
| Small | <200 | 1-2 hours | Simple spec, few requirements |
| Medium | 200-400 | 2-4 hours | Standard spec, 10-20 requirements |
| Large | 400-600 | 4-6 hours | Complex spec, many requirements |
| XL | >600 | 6-8 hours | Architecture doc, extensive content |

### 8.2 20-Spec Total Effort

| Priority | Count | Avg Size | Total Hours |
|----------|-------|----------|-------------|
| P0 | 5 | Large | 25 hours |
| P1 | 7 | Medium | 21 hours |
| P2 | 5 | Medium | 15 hours |
| P3 | 3 | Small | 6 hours |
| **Total** | **20** | - | **67 hours** |

**Sprint 117-118 Capacity**: 10 days × 60% × 8 hours = 48 hours
**Buffer**: 67 - 48 = 19 hours over

**Mitigation**:
- Parallel migration (2 specs/day by different team members)
- Template automation reduces effort by ~30%
- P3 specs can defer to Sprint 119 if needed

---

## 9. Schedule

### 9.1 Sprint 117 Week 1 (Feb 24-28)

| Day | Date | P0 Specs | P1 Specs |
|-----|------|----------|----------|
| 1 | Feb 24 | Governance-System-Implementation, Quality-Gates-Codegen | - |
| 2 | Feb 25 | ADR-007-AI-Context-Engine, Policy-Guards-Design | - |
| 3 | Feb 26 | System-Architecture-Document | ADR-022-Multi-Provider, AGENTS-MD-Technical |
| 4 | Feb 27 | - | ADR-036-4-Tier, Codegen-Service |
| 5 | Feb 28 | - | IR-Processor, ADR-012-Task-Decomposition |

### 9.2 Sprint 118 Week 1-2 (Mar 3-7)

| Day | Date | P1 Specs | P2 Specs | P3 Specs |
|-----|------|----------|----------|----------|
| 1 | Mar 3 | Validation-Pipeline | Teams-Data-Model | - |
| 2 | Mar 4 | - | ADR-028-Teams, Planning-Orchestrator | - |
| 3 | Mar 5 | - | ADR-013-Planning, Governance-Metrics | - |
| 4 | Mar 6 | - | - | ADR-029-AGENTS-MD, Feedback-Learning |
| 5 | Mar 7 | - | - | Conformance-Check, Buffer |

---

## 10. Success Criteria

### 10.1 Migration Quality

| Criterion | Target | Measurement |
|-----------|--------|-------------|
| Specs migrated | 20/20 | Count |
| Format compliance | >95% | sdlcctl spec validate |
| BDD coverage | 100% | All requirements in BDD |
| ADR linking | 100% | All related ADRs linked |
| Peer reviewed | 100% | Review comments addressed |

### 10.2 Post-Migration Validation

```bash
# Validate all migrated specs
sdlcctl spec validate docs/02-design/

# Check for broken links
sdlcctl spec links --check

# Generate migration report
sdlcctl spec report --format markdown > MIGRATION-REPORT.md
```

---

## 11. Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Scope creep | Medium | Medium | Strict 20-spec limit |
| Quality vs speed | Medium | High | Review checkpoints |
| Template gaps | Low | Medium | Update templates early |
| Team availability | Low | High | Cross-training |

---

## 12. Approval

| Role | Status | Date |
|------|--------|------|
| PM/PJM | ✅ Created | Jan 28, 2026 |
| Tech Lead | ⏳ Pending | - |
| CTO | ⏳ Pending | - |

---

*Framework 6.0 Migration Plan - Sprint 116-118 Track 1*
*SDLC Enterprise Framework*
