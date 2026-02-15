# SPEC-0017: Feedback Learning Service

## Frontmatter

```yaml
spec_id: SPEC-0017
title: Feedback Learning Service - Code Review Loop Closure
version: 2.0.0
status: approved
tier: PROFESSIONAL
pillar: Section 7 - Quality Assurance System
owner: Backend Lead + CTO
last_updated: 2026-01-29
tags:
  - feedback
  - learning
  - pr-review
  - continuous-improvement
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
  - SPEC-0014  # Planning Hierarchy
epic: Continuous Improvement Loop
sprint: Sprint 85-90
implementation_ref: "SDLC-Orchestrator/docs/02-design/14-Technical-Specs/Feedback-Learning-Service-Design.md"
```

---

## Executive Summary

This specification defines the **governance requirements** for closing the feedback loop from code review comments back to AI planning improvements, enabling continuous learning and quality enhancement.

**Key Governance Principles**:
- Extract learnings from code review feedback automatically
- Categorize feedback into actionable types for pattern recognition
- Generate decomposition hints to improve future AI-generated plans
- Maintain audit trail of learning provenance

**Business Value**:
- Reduce recurring review comments by capturing and applying patterns
- Improve AI plan quality through accumulated wisdom
- Enable pattern drift detection for early issue identification
- Preserve developer context across PR reviews

> **Implementation Reference**: For technical implementation details (service classes, database schemas, API endpoints), see SDLC-Orchestrator documentation.

---

## 1. Overview

### 1.1 Purpose

The Feedback Learning Service closes the learning cycle from code review feedback back to specification refinement. This enables continuous improvement of AI-generated plans based on real-world review outcomes.

**Key Insight**:
> "No learning from code review feedback" - Identified as critical gap in governance systems
>
> **Solution**: Close feedback loop from Code Review → AI Planning Improvement
> - Extract learnings from review comments
> - Categorize by type (pattern violation, missing requirement, edge case, etc.)
> - Update decomposition hints for future generations
> - Improve AI context files with accumulated wisdom

### 1.2 Scope

**In Scope**:
- PR learning extraction with AI-powered categorization
- Feedback categorization (10 standard categories)
- Decomposition hints generation from recurring patterns
- AI context file update suggestions (quarterly)
- Integration with planning services for hint injection
- Learning statistics and dashboards

**Out of Scope**:
- Human-in-the-loop hint approval (ENTERPRISE tier enhancement)
- Cross-project learning aggregation (deferred to Phase 2)
- Multi-platform webhook support (single platform in v1.0.0)

### 1.3 Business Value

| Metric | Before | After | Impact |
|--------|--------|-------|--------|
| Recurring review comments | Many | -20% reduction | Developer productivity |
| AI plan quality | Static | Continuously improving | Reduced rework |
| Pattern drift detection | Manual | Automated | Early issue detection |
| Developer context | Lost between PRs | Preserved and applied | Knowledge retention |

---

## 2. Functional Requirements

### FR-001: PR Learning Extraction

**Description**: Extract learnings from merged pull request review comments.

**Requirement**:

```gherkin
GIVEN a pull request is merged with review comments
WHEN the learning extraction process is triggered
THEN the system SHALL:
  - Fetch all review comments from the version control platform
  - Filter actionable comments (exclude trivial approvals)
  - Analyze each comment using AI categorization
  - Extract corrective patterns and recommendations
  - Store learnings with metadata and provenance
  - Track which comments were processed
AND the system SHALL validate:
  - Comment categorization accuracy (target: >80%)
  - Pattern extraction relevance
  - Proper metadata attachment (reviewer, file, line)
```

---

### FR-002: AI-Powered Feedback Categorization

**Description**: Categorize review comments into standard feedback types.

**Requirement**:

```gherkin
GIVEN a code review comment with file context
WHEN AI categorization is applied
THEN the system SHALL:
  - Use multi-provider AI with fallback chain
  - Analyze semantic meaning of the comment
  - Categorize into one of 10 feedback types
  - Assign severity (low, medium, high)
  - Extract reusable pattern if applicable
  - Generate corrected approach recommendation
AND the system SHALL ensure:
  - Fallback to rule-based classification if AI fails
  - Consistent categorization across similar comments
  - Confidence score for AI-generated categories
```

**Feedback Categories** (10 standard types):

| Category | Description | Typical Severity |
|----------|-------------|------------------|
| **Pattern Violation** | Violated established pattern | High |
| **Missing Requirement** | Missed a requirement | High |
| **Edge Case** | Unhandled edge case | Medium |
| **Performance** | Performance concern | Medium |
| **Security** | Security issue | High |
| **Code Style** | Style/convention issue | Low |
| **Architecture** | Architectural concern | High |
| **Testing** | Missing/inadequate tests | Medium |
| **Documentation** | Documentation issue | Low |
| **Other** | Uncategorized | Variable |

---

### FR-003: Decomposition Hints Generation

**Description**: Aggregate learnings into reusable hints for planning.

**Requirement**:

```gherkin
GIVEN accumulated PR learnings over a time period
WHEN hint generation is triggered (monthly)
THEN the system SHALL:
  - Aggregate learnings since last run
  - Identify recurring patterns (minimum threshold: 3 occurrences)
  - Calculate confidence scores (0.0-1.0)
  - Create or update decomposition hints
  - Track provenance (source learnings)
  - Mark processed learnings as applied
AND the system SHALL classify hints:
  - Pattern: Good practice to follow
  - Antipattern: Pattern to avoid
  - Convention: Naming/style convention
```

**Hint Confidence Calculation**:
- Confidence = occurrences / total_learnings
- Minimum threshold for hint creation: 3 occurrences
- Confidence capped at 1.0

---

### FR-004: AI Context File Update Suggestions

**Description**: Generate suggestions for improving AI context files.

**Requirement**:

```gherkin
GIVEN accumulated learnings over a quarterly period
WHEN context update generation is triggered
THEN the system SHALL:
  - Fetch learnings from last 90 days
  - Analyze recurring issues and patterns
  - Generate markdown sections for AI context files
  - Include pattern examples and antipatterns
  - Provide confidence scores for each suggestion
AND suggestions SHALL include:
  - Section title and content
  - Number of learnings the suggestion is based on
  - Confidence score for relevance
  - Formatted markdown with code examples
```

---

### FR-005: Learning Statistics Dashboard

**Description**: Provide visibility into learning metrics and trends.

**Requirement**:

```gherkin
GIVEN a project with accumulated learnings
WHEN learning statistics are requested
THEN the system SHALL provide:
  - Total learnings for specified period
  - Breakdown by feedback type
  - Breakdown by severity
  - Top patterns (good practices)
  - Top antipatterns (issues to avoid)
  - Improvement score (0-100)
AND the system SHALL support:
  - Period selection (weekly, monthly, quarterly)
  - Trend visualization over time
  - Export capability for reporting
```

**Improvement Score Calculation**:
- Baseline: First 30 days average learnings per PR
- Current: Last 30 days average learnings per PR
- Score = max(0, 100 × (1 - current/baseline))
- Higher score = fewer learnings = better quality

---

### FR-006: Version Control Webhook Integration

**Description**: Automatically trigger learning extraction on PR merge.

**Requirement**:

```gherkin
GIVEN a repository connected to the governance system
WHEN a pull request is merged
THEN the webhook handler SHALL:
  - Receive event notification from version control platform
  - Validate webhook signature for security
  - Extract project mapping from repository
  - Queue learning extraction asynchronously
  - Return acknowledgment immediately
AND the handler SHALL:
  - Reject requests with invalid signatures
  - Log security warnings for failed validations
  - Handle gracefully if project mapping not found
```

---

### FR-007: Planning Service Integration

**Description**: Inject learned hints into plan generation.

**Requirement**:

```gherkin
GIVEN a planning service generating implementation plans
WHEN plan generation is invoked
THEN the service SHALL:
  - Load active decomposition hints (minimum confidence threshold)
  - Inject hints into plan generation context
  - Track hint applications in usage counters
  - Include patterns in "Patterns to Follow" section
  - Include antipatterns in "Risks to Avoid" section
AND integration SHALL:
  - Limit hints to prevent prompt bloat (maximum: 20)
  - Prioritize by confidence score
  - Filter by relevance to task context
```

---

### FR-008: Scheduled Aggregation Jobs

**Description**: Run periodic jobs for hint aggregation and reporting.

**Requirement**:

```gherkin
GIVEN scheduled job execution time
WHEN the aggregation job runs
THEN the system SHALL:
  - Process all active projects
  - Call hint update for each project
  - Log success/failure for each project
  - Continue processing on individual failures
  - Send summary notification to administrators
AND the system SHALL support:
  - Monthly hint aggregation (default: 1st of month)
  - Quarterly context suggestion generation
  - Configurable scheduling for ENTERPRISE tier
```

---

## 3. Tier-Specific Requirements

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| **Learning Extraction** | Not available | Automatic on merge | Automatic + manual trigger | Automatic + manual + bulk |
| **Feedback Categories** | Not available | 10 standard categories | 10 categories | 10 categories + custom |
| **Decomposition Hints** | Not available | Auto-generated (monthly) | Auto-generated + editable | Auto + editable + approval |
| **Context Update Suggestions** | Not available | Not available | Quarterly (auto) | Quarterly + on-demand |
| **Learning Dashboard** | Not available | Basic stats | Basic + trends | Full analytics + export |
| **Webhook Integration** | Not available | Enabled | Enabled | Enabled + custom events |
| **Planning Integration** | Not available | Top 10 hints | Top 20 hints | All hints + weighting |
| **Scheduled Aggregation** | Not available | Enabled | Enabled | Customizable schedule |
| **Confidence Threshold** | N/A | 0.5 (fixed) | 0.4 (configurable) | 0.3 (configurable) |
| **Cross-Project Learning** | Not available | Not available | Not available | Portfolio-wide hints |

---

## 4. Data Requirements

### 4.1 Learning Record Structure

Learning records SHALL contain:

| Field | Purpose | Required |
|-------|---------|----------|
| Project reference | Link to owning project | Yes |
| PR identification | URL, ID, title, number | Yes |
| Feedback classification | Type and severity | Yes |
| Learning content | Original comment, corrected approach, pattern | Yes |
| Reviewer metadata | Reviewer identity for attribution | No |
| File context | File path and line number | No |
| Application status | Whether applied to hints | Yes |

### 4.2 Hint Record Structure

Hint records SHALL contain:

| Field | Purpose | Required |
|-------|---------|----------|
| Project reference | Link to owning project | Yes |
| Hint classification | Type (pattern/antipattern/convention) and category | Yes |
| Content | Title, description, example | Yes |
| Provenance | Source learnings and count | Yes |
| Quality metrics | Confidence, times applied, times helpful | Yes |
| Lifecycle | Active status, expiration | Yes |

---

## 5. Non-Functional Requirements

### NFR-001: Performance Targets

| Operation | Target | Notes |
|-----------|--------|-------|
| Learning extraction (per PR) | <30s | Includes platform API + AI analysis |
| Hint aggregation (per project) | <60s | Monthly batch job |
| Context suggestion generation | <2min | Quarterly, AI-intensive |
| Hint lookup (planning) | <100ms | Indexed database query |
| Dashboard statistics | <500ms | Cached aggregations |
| Webhook response | <200ms | Return acknowledgment immediately |

### NFR-002: Accuracy Targets

| Metric | Target | Notes |
|--------|--------|-------|
| Categorization accuracy | >80% | AI vs human review |
| Hint relevance | >70% | Manual review sample |
| Pattern extraction | >75% | Meaningful, reusable patterns |

---

## 6. Design Decisions

### Decision 1: Multi-Provider AI Fallback

**Rationale**: Ensure categorization always succeeds even if primary AI fails.

**Approach**:
- Primary provider: Fast, cost-effective
- Secondary provider: Reasoning fallback
- Tertiary: Rule-based classification (no AI)

### Decision 2: Monthly Aggregation Frequency

**Rationale**: Balance between freshness and signal quality.

**Approach**:
- Monthly aggregation for hints (enough data to identify patterns)
- Quarterly for context suggestions (needs larger sample)
- Configurable for ENTERPRISE (flexibility)

### Decision 3: Confidence Threshold by Tier

**Rationale**: Higher tiers can handle more speculative hints.

**Approach**:
- STANDARD: 0.5 threshold (conservative)
- PROFESSIONAL: 0.4 threshold (moderate)
- ENTERPRISE: 0.3 threshold (aggressive, with approval workflow)

### Decision 4: Hint Injection Limits

**Rationale**: Prevent prompt bloat while maintaining usefulness.

**Approach**:
- Maximum 20 hints per plan generation
- Prioritize by confidence score
- Filter by task relevance when possible

---

## 7. Acceptance Criteria

### AC-001: Learning Extraction Accuracy

```gherkin
GIVEN a merged PR with 10 review comments
WHEN learning extraction is performed
THEN all actionable comments are extracted
AND trivial comments are filtered correctly
AND categorization accuracy exceeds 80%
AND extraction completes within 30 seconds
```

### AC-002: Hint Generation Correctness

```gherkin
GIVEN 30 learnings with a pattern occurring 5 times
WHEN hint aggregation runs
THEN the pattern is identified as recurring
AND confidence is calculated correctly
AND hint is created with proper provenance
AND source learnings are marked as applied
```

### AC-003: Planning Integration

```gherkin
GIVEN a project with 5 active hints above confidence threshold
WHEN plan generation is invoked
THEN all 5 hints are loaded and injected
AND usage counters are incremented
AND patterns appear in plan output
```

### AC-004: Webhook Security

```gherkin
GIVEN a webhook request with invalid signature
WHEN the webhook endpoint receives the request
THEN the request is rejected with forbidden status
AND no learning extraction is triggered
AND security warning is logged
```

### AC-005: Context Suggestion Quality

```gherkin
GIVEN 50 learnings about a recurring topic over 90 days
WHEN context suggestion generation runs
THEN the topic is identified as significant
AND generated markdown is valid and actionable
AND confidence reflects occurrence frequency
```

---

## 8. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Low categorization accuracy | Medium | Medium | Multi-provider fallback, rule-based backup |
| Hint staleness | Medium | Low | Expiration policy, confidence decay |
| Webhook security breach | Low | High | HMAC validation, signature verification |
| Prompt bloat from too many hints | Medium | Medium | Injection limits, confidence filtering |
| Cross-project learning leakage | Low | High | Strict project isolation, no cross-project by default |

---

## 9. Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Learning extraction accuracy | >80% | AI categorization vs human review |
| Hint relevance | >70% | Manual review sample (quarterly) |
| Planning improvement | Measurable | A/B test plan quality before/after |
| Developer adoption | >50% teams | Teams reviewing hints dashboard |
| Reduced review comments | -20% | Recurring comments before/after 6 months |
| Improvement score increase | +15 points | LearningStats improvement over time |

---

## 10. References

### Source Documents
- **SPEC-0001**: Anti-Vibecoding (quality assurance context)
- **SPEC-0014**: Planning Hierarchy (planning integration)
- **ADR-034**: Planning Sub-agent Orchestration

### External Standards
- DORA Metrics: Continuous improvement measurement
- Learning organization principles: Knowledge capture and application

---

## Document Control

| Field | Value |
|-------|-------|
| **Spec ID** | SPEC-0017 |
| **Version** | 2.0.0 |
| **Status** | APPROVED |
| **Author** | Backend Lead |
| **Reviewer** | CTO |
| **Last Updated** | 2026-01-29 |
| **Framework Version** | 6.0.5 |

---

**Pure Methodology Notes**:
- This specification defines WHAT feedback learning requires
- For HOW to implement (service classes, database schemas, API endpoints), see SDLC-Orchestrator documentation
- Feedback categories are governance standard; implementation tools may vary
- Tier requirements define capability expectations, not technical constraints

---

**End of Specification**
