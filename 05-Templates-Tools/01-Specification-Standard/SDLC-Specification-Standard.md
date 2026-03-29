# SDLC Specification Standard v1.1
## Framework 6.2.0 Unified Specification Template - Section 8

**Version**: 6.2.1
**Status**: ACTIVE - PRODUCTION READY
**Created**: January 28, 2026
**Last Updated**: February 14, 2026
**Author**: PM/PJM Team
**Framework**: SDLC 6.2.1 (7-Pillar + 2-Section)
**Inspiration**: OpenSpec best practices + SDLC 6.2.0 evolution
**Architecture**: Section 8: Unified Specification Standard
**NEW in 6.0.4**: Spec Converter Methodology (SpecIR, BDD↔OpenSpec conversion)

---

## 1. Purpose

This document defines the **unified specification standard** for SDLC Framework 6.0. All specifications in the SDLC ecosystem MUST follow this format to ensure:

- **AI-Parseability**: Structured format for automated extraction
- **Consistency**: Uniform structure across all specifications
- **Traceability**: Clear links between requirements, decisions, and evidence
- **Tier-Awareness**: Requirements scaled to project complexity

---

## 2. Template Structure

### 2.1 YAML Frontmatter (MANDATORY)

Every specification MUST begin with YAML frontmatter containing metadata:

```yaml
---
# Core Metadata (MANDATORY)
spec_id: SPEC-[NNNN]              # Unique identifier
spec_name: "[Human-readable name]"
spec_version: "1.0.0"             # Semantic versioning
status: draft | review | approved | implemented | deprecated

# Classification (MANDATORY)
tier: LITE | STANDARD | PROFESSIONAL | ENTERPRISE
stage: "00" | "01" | "02" | "03" | "04" | "05" | "06" | "07" | "08" | "09" | "10"
category: functional | technical | security | performance | integration

# Ownership (MANDATORY)
owner: "[team/person]"
reviewers: ["[reviewer1]", "[reviewer2]"]
approver: "[approver name/role]"

# Timestamps (MANDATORY)
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
approved_date: YYYY-MM-DD | null

# Relationships (RECOMMENDED)
related_adrs: ["ADR-XXX", "ADR-YYY"]
related_specs: ["SPEC-XXX", "SPEC-YYY"]
parent_spec: "SPEC-XXX" | null
supersedes: "SPEC-XXX" | null

# Tags (OPTIONAL)
tags: ["tag1", "tag2", "tag3"]
priority: P0 | P1 | P2 | P3
effort: S | M | L | XL
---
```

### 2.2 Section Structure

```markdown
## 1. Overview
[Brief description - 2-3 paragraphs maximum]

## 2. Context
[Problem statement and motivation]

## 3. Requirements
### 3.1 Functional Requirements
[BDD format: GIVEN-WHEN-THEN]

### 3.2 Non-Functional Requirements
[Performance, Security, Scalability]

### 3.3 Tier-Specific Requirements
[Requirements by LITE/STANDARD/PROFESSIONAL/ENTERPRISE]

## 4. Design Decisions
[References to ADRs, not duplication]

## 5. Technical Specification
[Implementation details]

## 6. Acceptance Criteria
[Testable criteria]

## 7. Spec Delta
[Changes from previous version]

## 8. Dependencies
[Related systems and specifications]

## 9. Appendix
[Additional materials]
```

---

## 3. Detailed Section Guidelines

### 3.1 Overview Section

**Purpose**: Provide a concise summary of the specification.

**Format**:
```markdown
## 1. Overview

[Specification Name] defines [what it does] for [target audience/system].

**Key Objectives**:
- [Objective 1]
- [Objective 2]
- [Objective 3]

**Scope**:
- **In Scope**: [What is covered]
- **Out of Scope**: [What is NOT covered]
```

**Guidelines**:
- Keep to 2-3 paragraphs maximum
- Use bullet points for clarity
- Define scope explicitly to prevent scope creep

---

### 3.2 Context Section

**Purpose**: Explain why this specification exists and what problem it solves.

**Format**:
```markdown
## 2. Context

### 2.1 Problem Statement

[Describe the problem or opportunity that motivates this specification]

### 2.2 Background

[Provide relevant history, constraints, or context]

### 2.3 Stakeholders

| Stakeholder | Role | Interest |
|-------------|------|----------|
| [Name/Team] | [Role] | [What they care about] |

### 2.4 Assumptions

- [Assumption 1]
- [Assumption 2]

### 2.5 Constraints

- [Constraint 1]
- [Constraint 2]
```

---

### 3.3 Requirements Section

**Purpose**: Define what the system must do (functional) and how well it must do it (non-functional).

#### 3.3.1 Functional Requirements (BDD Format)

**Format**:
```markdown
### 3.1 Functional Requirements

#### FR-001: [Requirement Title]
**Priority**: P0 | P1 | P2 | P3
**Tier**: LITE | STANDARD | PROFESSIONAL | ENTERPRISE

**Scenario**: [Scenario Name]
```gherkin
GIVEN [initial context or precondition]
  AND [additional context if needed]
WHEN [action or trigger occurs]
  AND [additional action if needed]
THEN [expected outcome]
  AND [additional outcome if needed]
```

**Rationale**: [Why this requirement exists]
**Verification**: [How to verify this requirement is met]
```

**Example**:
```markdown
#### FR-001: User Authentication with OAuth
**Priority**: P0
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

**Scenario**: Successful OAuth Login
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

#### 3.3.2 Non-Functional Requirements

**Format**:
```markdown
### 3.2 Non-Functional Requirements

#### NFR-001: Performance
| Metric | Target | Measurement |
|--------|--------|-------------|
| API Latency (p95) | <100ms | Prometheus histogram |
| Dashboard Load | <1s | Lighthouse |
| Concurrent Users | 10,000 | Load test (Locust) |

#### NFR-002: Security
| Requirement | Standard | Verification |
|-------------|----------|--------------|
| Authentication | OWASP ASVS L2 | Security audit |
| Encryption at-rest | AES-256 | Config review |
| Encryption in-transit | TLS 1.3 | SSL Labs test |

#### NFR-003: Availability
| Metric | Target | Measurement |
|--------|--------|-------------|
| Uptime | 99.9% | Prometheus |
| RTO | 4 hours | DR drill |
| RPO | 1 hour | Backup verification |

#### NFR-004: Scalability
| Dimension | Current | Target | Strategy |
|-----------|---------|--------|----------|
| Users | 1,000 | 100,000 | Horizontal scaling |
| Data | 100GB | 10TB | Sharding |
| Throughput | 100 req/s | 10,000 req/s | Caching + CDN |
```

#### 3.3.3 Tier-Specific Requirements

**Format**:
```markdown
### 3.3 Tier-Specific Requirements

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| Authentication | Basic | OAuth | OAuth + MFA | SSO + MFA |
| Audit Logs | 7 days | 30 days | 1 year | 7 years |
| SLA | None | 99% | 99.9% | 99.99% |
| Support | Community | Email | Priority | Dedicated |
| Data Residency | Any | Regional | Custom | On-premise |

#### LITE Tier
- Minimal requirements for small projects
- Single team, <10 users
- Basic authentication sufficient

#### STANDARD Tier
- Standard requirements for typical projects
- Multiple teams, 10-100 users
- OAuth authentication required

#### PROFESSIONAL Tier
- Enhanced requirements for regulated industries
- Compliance features required
- Audit trail mandatory

#### ENTERPRISE Tier
- Full requirements for mission-critical systems
- Custom deployment options
- Dedicated support and SLA
```

---

### 3.4 Design Decisions Section

**Purpose**: Reference architectural decisions without duplicating ADR content.

**Format**:
```markdown
## 4. Design Decisions

### 4.1 Related ADRs

| ADR | Title | Status | Impact on This Spec |
|-----|-------|--------|---------------------|
| [ADR-007](../ADRs/ADR-007.md) | Ollama AI Integration | Accepted | Primary AI provider |
| [ADR-022](../ADRs/ADR-022.md) | IR-Based Codegen | Proposed | Code generation flow |

### 4.2 Key Decisions

#### Decision 1: [Decision Title]
- **Status**: Decided | Pending | Superseded
- **ADR Reference**: [ADR-XXX](link)
- **Summary**: [One-line summary of decision]
- **Impact**: [How this affects the specification]

### 4.3 Open Questions

- [ ] [Question 1 - awaiting decision]
- [ ] [Question 2 - under investigation]
```

**Guidelines**:
- NEVER duplicate ADR content in specifications
- Link to ADRs, summarize impact only
- Track open questions that need resolution

---

### 3.5 Technical Specification Section

**Purpose**: Provide implementation details for developers.

**Format**:
```markdown
## 5. Technical Specification

### 5.1 Architecture Overview

[Diagram or description of system architecture]

```
┌─────────────────────────────────────────────────────────────────┐
│                     [Component Diagram]                         │
├─────────────────────────────────────────────────────────────────┤
│  [Description of components and their interactions]            │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Data Model

[Entity definitions, relationships, constraints]

```yaml
Entity: [EntityName]
  Fields:
    - id: UUID (PK)
    - name: VARCHAR(255) NOT NULL
    - created_at: TIMESTAMP DEFAULT NOW()
  Relationships:
    - belongs_to: [ParentEntity]
    - has_many: [ChildEntity]
  Constraints:
    - UNIQUE(name)
    - CHECK(status IN ('active', 'inactive'))
```

### 5.3 API Contracts

[OpenAPI-style endpoint definitions]

```yaml
Endpoint: POST /api/v1/[resource]
  Description: [What this endpoint does]
  Authentication: Bearer token
  Request:
    Content-Type: application/json
    Body:
      field1: string (required)
      field2: integer (optional)
  Response:
    200:
      - id: string
      - created_at: timestamp
    400:
      - error: string
      - details: object
    401:
      - error: "Unauthorized"
```

### 5.4 Integration Points

| System | Protocol | Direction | Data Format |
|--------|----------|-----------|-------------|
| [System A] | REST | Inbound | JSON |
| [System B] | gRPC | Outbound | Protobuf |
| [System C] | Webhook | Bidirectional | JSON |

### 5.5 Security Considerations

- **Authentication**: [Method and implementation]
- **Authorization**: [RBAC rules, scopes]
- **Data Protection**: [Encryption, masking]
- **Audit**: [Logging requirements]
```

---

### 3.6 Acceptance Criteria Section

**Purpose**: Define testable criteria for completion.

**Format**:
```markdown
## 6. Acceptance Criteria

### 6.1 Functional Acceptance

| ID | Criterion | Test Type | Priority |
|----|-----------|-----------|----------|
| AC-001 | User can login via OAuth | E2E | P0 |
| AC-002 | Session expires after 15 minutes | Integration | P0 |
| AC-003 | Failed login shows error message | Unit | P1 |

### 6.2 Performance Acceptance

| Metric | Threshold | Test Method | Blocker |
|--------|-----------|-------------|---------|
| API p95 latency | <100ms | Locust load test | Yes |
| Dashboard load | <1s | Lighthouse | Yes |
| Memory usage | <512MB | Prometheus | No |

### 6.3 Security Acceptance

| Criterion | Standard | Verification | Blocker |
|-----------|----------|--------------|---------|
| No critical CVEs | Grype scan | CI/CD gate | Yes |
| OWASP Top 10 | Semgrep rules | Pre-commit | Yes |
| Secrets scan | GitLeaks | Pre-commit | Yes |

### 6.4 Definition of Done

- [ ] All P0 acceptance criteria pass
- [ ] Code review approved (2+ reviewers)
- [ ] Documentation updated
- [ ] No P0/P1 bugs outstanding
- [ ] Performance benchmarks met
- [ ] Security scan PASS
```

---

### 3.7 Spec Delta Section

**Purpose**: Track changes between specification versions.

**Format**:
```markdown
## 7. Spec Delta

### 7.1 Current Version Changes (v1.0.0 → v1.1.0)

**Summary**: [Brief description of changes]

**Impact**: breaking | non-breaking | patch

#### Added
- [New requirement/feature 1]
- [New requirement/feature 2]

#### Modified

| Original | New | Rationale |
|----------|-----|-----------|
| [old text] | [new text] | [why changed] |

#### Removed
- [Removed item 1] - Reason: [...]
- [Removed item 2] - Reason: [...]

#### Deprecated
- [Item 1] - Will be removed in v2.0.0
- [Item 2] - Use [alternative] instead

### 7.2 Migration Guide

**Steps to update implementations:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

### 7.3 Breaking Changes

⚠️ **Warning**: The following changes require code updates:

- [Breaking change 1]: [How to fix]
- [Breaking change 2]: [How to fix]

### 7.4 Backward Compatibility

[How to maintain compatibility during transition]
```

---

### 3.8 Dependencies Section

**Purpose**: Document relationships with other systems and specifications.

**Format**:
```markdown
## 8. Dependencies

### 8.1 Upstream Dependencies

| Dependency | Type | Version | Status | Risk |
|------------|------|---------|--------|------|
| [SPEC-001](link) | Specification | 1.2.0 | Stable | Low |
| [ADR-007](link) | ADR | Accepted | Active | Low |
| PostgreSQL | Database | 15.5 | Stable | Low |
| OPA | Policy Engine | 0.58.0 | Stable | Low |

### 8.2 Downstream Dependencies

| Dependent | Type | Impact if Changed |
|-----------|------|-------------------|
| [SPEC-010](link) | Specification | Requires update |
| Frontend Dashboard | Component | Requires update |

### 8.3 External Systems

| System | Purpose | Owner | SLA |
|--------|---------|-------|-----|
| GitHub API | OAuth, Repos | GitHub | 99.9% |
| MinIO | Storage | Self-hosted | 99.9% |

### 8.4 Dependency Update Policy

- **Security patches**: Apply within 24 hours
- **Minor versions**: Apply within 1 sprint
- **Major versions**: Requires ADR review
```

---

### 3.9 Appendix Section

**Purpose**: Additional materials, references, and supporting documentation.

**Format**:
```markdown
## 9. Appendix

### 9.1 Glossary

| Term | Definition |
|------|------------|
| [Term 1] | [Definition] |
| [Term 2] | [Definition] |

### 9.2 References

- [Reference 1](link) - [Description]
- [Reference 2](link) - [Description]

### 9.3 Diagrams

[Additional diagrams not included in main sections]

### 9.4 Examples

[Code examples, sample requests/responses]

### 9.5 Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | [Author] | Initial version |
| 1.1.0 | YYYY-MM-DD | [Author] | [Changes] |
```

---

## 4. Validation Rules

### 4.1 Mandatory Fields

The following frontmatter fields are **MANDATORY** for all specifications:

```yaml
Required Fields:
  - spec_id        # Unique identifier
  - spec_name      # Human-readable name
  - spec_version   # Semantic version
  - status         # Current status
  - tier           # LITE/STANDARD/PROFESSIONAL/ENTERPRISE
  - stage          # SDLC stage (00-10)
  - category       # Type of specification
  - owner          # Responsible party
  - created        # Creation date
  - last_updated   # Last modification date
```

### 4.2 Section Requirements

| Section | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|---------|------|----------|--------------|------------|
| 1. Overview | MANDATORY | MANDATORY | MANDATORY | MANDATORY |
| 2. Context | OPTIONAL | MANDATORY | MANDATORY | MANDATORY |
| 3. Requirements | MANDATORY | MANDATORY | MANDATORY | MANDATORY |
| 4. Design Decisions | OPTIONAL | RECOMMENDED | MANDATORY | MANDATORY |
| 5. Technical Spec | OPTIONAL | MANDATORY | MANDATORY | MANDATORY |
| 6. Acceptance Criteria | MANDATORY | MANDATORY | MANDATORY | MANDATORY |
| 7. Spec Delta | OPTIONAL | RECOMMENDED | MANDATORY | MANDATORY |
| 8. Dependencies | OPTIONAL | MANDATORY | MANDATORY | MANDATORY |
| 9. Appendix | OPTIONAL | OPTIONAL | OPTIONAL | OPTIONAL |

### 4.3 Validation Commands

```bash
# Validate specification format
sdlcctl spec validate [file.md]

# Fix common issues automatically
sdlcctl spec validate --fix [file.md]

# Generate validation report
sdlcctl spec validate --report [directory]

# Check tier-specific requirements
sdlcctl spec validate --tier PROFESSIONAL [file.md]
```

---

## 5. AI-Parseability Guidelines

### 5.1 Structured Data Extraction

Specifications following this standard enable automated extraction:

```yaml
Extractable Elements:
  Metadata:
    - All frontmatter fields
    - Section headings
    - Tables

  Requirements:
    - Functional requirements (BDD scenarios)
    - Non-functional requirements (metrics)
    - Acceptance criteria (testable items)

  Relationships:
    - ADR links
    - Spec dependencies
    - System integrations
```

### 5.2 Consistent Formatting

For optimal AI parsing:

1. **Use Markdown tables** for structured data
2. **Use code blocks** for YAML, JSON, and code
3. **Use consistent heading levels** (## for sections, ### for subsections)
4. **Use frontmatter** for metadata (YAML format)
5. **Use BDD format** for functional requirements

### 5.3 Avoid Anti-Patterns

```yaml
Anti-Patterns to Avoid:
  - Nested bullet points deeper than 3 levels
  - Inline HTML (use Markdown instead)
  - Inconsistent date formats (use YYYY-MM-DD)
  - Ambiguous requirements ("fast", "secure")
  - Missing success metrics
  - Duplicating ADR content
```

---

## 6. Examples

### 6.1 Minimal Specification (LITE Tier)

```markdown
---
spec_id: SPEC-0001
spec_name: "User Authentication"
spec_version: "1.0.0"
status: draft
tier: LITE
stage: "03"
category: security
owner: "backend-team"
created: 2026-01-28
last_updated: 2026-01-28
---

## 1. Overview

User Authentication specification for basic login functionality.

## 3. Requirements

### 3.1 Functional Requirements

#### FR-001: Email/Password Login
**Priority**: P0
**Tier**: LITE

GIVEN a registered user
WHEN they submit valid credentials
THEN they receive a session token

## 6. Acceptance Criteria

| ID | Criterion | Test Type | Priority |
|----|-----------|-----------|----------|
| AC-001 | Valid credentials return token | Unit | P0 |
| AC-002 | Invalid credentials return 401 | Unit | P0 |
```

### 6.2 Complete Specification (PROFESSIONAL Tier)

See [Example-Spec-Professional.md](./examples/Example-Spec-Professional.md) for a full example.

---

## 7. Migration Guide

### 7.1 From SDLC 6.2.0 Specs

**Steps to migrate existing specifications:**

1. **Add YAML frontmatter**
   - Extract metadata from document
   - Add required fields

2. **Restructure sections**
   - Map existing sections to new structure
   - Add missing required sections

3. **Convert requirements to BDD**
   - Identify functional requirements
   - Rewrite in GIVEN-WHEN-THEN format

4. **Add tier-specific requirements**
   - Classify requirements by tier
   - Add tier matrix table

5. **Validate with sdlcctl**
   ```bash
   sdlcctl spec validate --fix [file.md]
   ```

### 7.2 Estimated Migration Effort

| Spec Complexity | Estimated Time |
|-----------------|----------------|
| Simple (1-2 pages) | 15-30 minutes |
| Medium (3-5 pages) | 30-60 minutes |
| Complex (5+ pages) | 1-2 hours |

---

## 8. Spec Converter Methodology (NEW in 6.0.4)

### 8.1 Overview

The **Spec Converter** enables bidirectional conversion between specification formats using an **Intermediate Representation (SpecIR)**. This methodology standardizes specification handling across different input sources and output formats.

**Key Benefits**:
- **Format-agnostic**: Convert between BDD, OpenSpec, User Stories, Jira, Linear
- **Lossless conversion**: SpecIR preserves all semantic information
- **Tool independence**: Works with any specification management tool
- **TDD validated**: 113 tests written first, 100% pass rate (Sprint 154)

### 8.2 SpecIR (Intermediate Representation)

SpecIR is the **canonical internal format** for specifications:

```yaml
SpecIR Structure:
  spec_id: string          # SPEC-NNNN unique identifier
  title: string            # Human-readable title
  version: string          # Semantic version (1.0.0)
  status: string           # DRAFT | REVIEW | APPROVED | IMPLEMENTED | DEPRECATED
  tier: list[string]       # [LITE, STANDARD, PROFESSIONAL, ENTERPRISE]
  owner: string            # Responsible team/person
  last_updated: string     # ISO date (2026-02-04)
  tags: list[string]       # Classification tags
  related_adrs: list[string]    # [ADR-001, ADR-002]
  related_specs: list[string]   # [SPEC-001, SPEC-002]

  requirements: list[SpecRequirement]
    - id: string           # REQ-001
      title: string        # Requirement title
      priority: string     # P0 | P1 | P2 | P3
      tier: list[string]   # Applicable tiers
      given: string        # BDD GIVEN clause
      when: string         # BDD WHEN clause
      then: string         # BDD THEN clause
      user_story: string   # Optional user story format
      acceptance_criteria: list[string]  # Optional inline AC

  acceptance_criteria: list[AcceptanceCriterion]
    - id: string           # AC-001
      scenario: string     # Scenario description
      given: string        # BDD GIVEN
      when: string         # BDD WHEN
      then: string         # BDD THEN
      tier: list[string]   # Applicable tiers
      testable: boolean    # Can be automated
```

### 8.3 Conversion Patterns

#### Pattern 1: OpenSpec → SpecIR → OpenSpec (Roundtrip)

```
┌──────────────────┐      ┌──────────────┐      ┌──────────────────┐
│   OpenSpec.md    │ ──── │    SpecIR    │ ──── │   OpenSpec.md    │
│  (YAML + BDD)    │parse │  (Internal)  │render│  (YAML + BDD)    │
└──────────────────┘      └──────────────┘      └──────────────────┘
```

**Use Case**: Normalize, validate, and re-render specifications.

#### Pattern 2: User Story → SpecIR → BDD Requirements

```
┌──────────────────┐      ┌──────────────┐      ┌──────────────────┐
│   User Story     │ ──── │    SpecIR    │ ──── │  BDD Format      │
│  "As a user..."  │parse │  (Internal)  │render│  GIVEN-WHEN-THEN │
└──────────────────┘      └──────────────┘      └──────────────────┘
```

**Use Case**: Convert informal requirements to testable BDD scenarios.

#### Pattern 3: Jira/Linear Import → SpecIR → OpenSpec

```
┌──────────────────┐      ┌──────────────┐      ┌──────────────────┐
│  Jira/Linear     │ ──── │    SpecIR    │ ──── │   OpenSpec.md    │
│  (API JSON)      │adapt │  (Internal)  │render│  (Unified Spec)  │
└──────────────────┘      └──────────────┘      └──────────────────┘
```

**Use Case**: Migrate specifications from external tools to SDLC standard.

### 8.4 Parser Implementation

Parsers extract structured data from source formats into SpecIR:

| Parser | Input Format | Features |
|--------|--------------|----------|
| **OpenSpecParser** | YAML frontmatter + BDD markdown | Frontmatter extraction, BDD clause parsing, AC table parsing |
| **UserStoryParser** | "As a... I want... So that..." | Story decomposition, acceptance criteria extraction |
| **JiraAdapter** | Jira API JSON | Issue mapping, epic/story hierarchy |
| **LinearAdapter** | Linear API JSON | Cycle mapping, label conversion |
| **TextParser** | Plain text requirements | NL pattern matching, heuristic extraction |

**OpenSpec Parser Example**:

```python
# Parses SDLC 6.2.0 specification format
async def parse(content: str) -> SpecIR:
    # 1. Extract YAML frontmatter
    frontmatter = extract_frontmatter(content)

    # 2. Extract markdown body
    body = extract_body(content)

    # 3. Parse BDD requirements (GIVEN-WHEN-THEN)
    requirements = extract_requirements(body)

    # 4. Parse acceptance criteria tables
    acceptance_criteria = extract_acceptance_criteria(body)

    # 5. Build and return SpecIR
    return SpecIR(
        spec_id=frontmatter.get("spec_id"),
        title=frontmatter.get("title"),
        requirements=requirements,
        acceptance_criteria=acceptance_criteria,
        ...
    )
```

### 8.5 Renderer Implementation

Renderers transform SpecIR back to target formats:

| Renderer | Output Format | Features |
|----------|---------------|----------|
| **OpenSpecRenderer** | YAML frontmatter + BDD markdown | Section 8 compliant output |
| **BDDRenderer** | Pure Gherkin feature files | Cucumber/SpecFlow compatible |
| **JSONRenderer** | Structured JSON | API integration, tooling |
| **MarkdownRenderer** | Simple markdown | Human-readable summaries |

**OpenSpec Renderer Example**:

```python
# Renders to SDLC 6.2.0 specification format
async def render(ir: SpecIR) -> str:
    lines = []

    # 1. Render YAML frontmatter
    lines.append("---")
    lines.append(yaml.dump(build_frontmatter(ir)))
    lines.append("---")

    # 2. Render Requirements section
    lines.append("# Requirements")
    for req in ir.requirements:
        lines.append(f"## {req.id}: {req.title} [{req.priority}] [{req.tier}]")
        lines.append(f"**GIVEN** {req.given}")
        lines.append(f"**WHEN** {req.when}")
        lines.append(f"**THEN** {req.then}")

    # 3. Render Acceptance Criteria table
    if ir.acceptance_criteria:
        lines.append("## Acceptance Criteria")
        lines.append("| ID | Scenario | Given | When | Then | Tier | Testable |")
        ...

    return "\n".join(lines)
```

### 8.6 Tier-Aware TDD Coverage Requirements

Spec Converter validates test coverage by tier (validated Sprint 154):

| Tier | Minimum Coverage | Test Types Required |
|------|------------------|---------------------|
| **LITE** | 70% | Unit tests |
| **STANDARD** | 85% | Unit + Integration tests |
| **PROFESSIONAL** | 95% | Unit + Integration + E2E tests |
| **ENTERPRISE** | 95%+ | All + Performance + Security tests |

**Validation Example**:

```bash
# Validate spec coverage by tier
sdlcctl spec validate --tier PROFESSIONAL --coverage spec.md

# Output:
# ✅ Coverage: 96.2% (target: 95%)
# ✅ Unit tests: 85 passing
# ✅ Integration tests: 23 passing
# ✅ E2E tests: 5 passing
```

### 8.7 CLI Integration

```bash
# Convert User Story to OpenSpec
sdlcctl spec convert --from user-story --to openspec input.txt -o spec.md

# Convert Jira issues to OpenSpec
sdlcctl spec convert --from jira --project PROJ-123 --to openspec -o spec.md

# Validate OpenSpec format
sdlcctl spec validate spec.md

# Roundtrip validation (parse → render → compare)
sdlcctl spec validate --roundtrip spec.md
```

### 8.8 Sprint 154 Validation Results

The Spec Converter methodology was validated through Sprint 154:

```yaml
TDD Metrics (Sprint 154):
  total_tests: 113
  pass_rate: 100%

  test_breakdown:
    unit_tests: 85
    integration_tests: 23
    e2e_tests: 5

  parser_coverage:
    openspec_parser: 95%
    user_story_parser: 92%
    text_parser: 88%

  renderer_coverage:
    openspec_renderer: 96%
    bdd_renderer: 94%
    json_renderer: 97%

  roundtrip_validation:
    openspec_roundtrip: ✅ Pass (lossless)
    bdd_roundtrip: ✅ Pass (semantic equivalent)
```

---

## 9. Document Control

| Field | Value |
|-------|-------|
| **Document ID** | SDLC-SPEC-STD-001 |
| **Version** | 6.2.0 |
| **Status** | ACTIVE - PRODUCTION READY |
| **Created** | January 28, 2026 |
| **Last Updated** | February 8, 2026 |
| **Author** | PM/PJM Team |
| **Reviewers** | CTO, Tech Lead |
| **Approver** | CTO |
| **Framework** | SDLC 6.2.0 (7-Pillar + 2-Section) |
| **Section** | Section 8: Unified Specification Standard |
| **Inspiration** | OpenSpec, SDLC 6.2.0, Sprint 154 TDD Validation |

---

## 10. Approval

| Role | Status | Date |
|------|--------|------|
| Tech Lead | ✅ APPROVED | January 28, 2026 |
| CTO | ✅ APPROVED | January 28, 2026 |
| CTO (6.0.4 Spec Converter) | ✅ APPROVED | February 8, 2026 |

*This specification standard is APPROVED and ACTIVE for SDLC Framework 6.2.0.*

---

**Document Status**: ACTIVE
**Last Updated**: February 14, 2026
**Owner**: CTO + CPO Office

*SDLC Enterprise Framework 6.2.0 - Section 8: Unified Specification Standard*

***"Consistent specifications enable consistent quality."***
