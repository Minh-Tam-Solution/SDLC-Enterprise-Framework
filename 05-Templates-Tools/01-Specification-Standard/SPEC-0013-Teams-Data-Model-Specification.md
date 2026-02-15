# SPEC-0013: Teams Data Model Specification

## Frontmatter

```yaml
spec_id: SPEC-0013
title: Teams Data Model Specification - Multi-Tenant Collaboration Schema
version: 2.0.0
status: approved
tier: PROFESSIONAL
pillar: Pillar 1 - Planning & Requirements
owner: Backend Lead + CTO
last_updated: 2026-01-29
tags:
  - teams
  - data-model
  - multi-tenant
  - collaboration
  - rbac
  - sase
related_specs:
  - SPEC-0001  # Anti-Vibecoding
  - SPEC-0002  # Specification Standard
epic: Multi-Tenant Teams System
sprint: Sprint 60-65
implementation_ref: "SDLC-Orchestrator/docs/02-design/14-Technical-Specs/Teams-Data-Model-Specification.md"
```

---

## Executive Summary

This specification defines the **governance requirements** for multi-tenant team management, introducing organizational hierarchy, team collaboration units, and AI agent membership aligned with SASE principles (Software Engineering for Humans & Agents).

**Key Governance Principles**:
- Multi-tenant isolation with clear billing and compliance boundaries
- Team-based collaboration units within organizations
- Role-based access control (owner, admin, member, ai_agent)
- SASE-compliant AI agent restrictions (Coaches vs Executors)
- Zero-downtime migration strategy

**Business Value**:
- Enables enterprise multi-tenancy with clear billing boundaries
- Supports hybrid human-AI teams per SDLC AI Governance Principles
- Provides VCR authority hierarchy (owner → admin → member → ai_agent)
- Facilitates team-scoped policy enforcement and evidence collection

> **Implementation Reference**: For technical implementation details (database schemas, ORM models, migrations), see SDLC-Orchestrator documentation.

---

## 1. Functional Requirements

### FR-001: Organizations - Multi-Tenant Root Entity

**Description**: Organizations serve as the multi-tenant root entity containing teams and users, with plan-based billing and configurable settings.

**Requirement**:

```gherkin
GIVEN the system requires multi-tenant isolation
WHEN an organization is created
THEN the system SHALL:
  - Assign a globally unique identifier
  - Enforce globally unique URL-safe slug
  - Associate a plan tier (free, pro, enterprise)
  - Store configurable settings (policy pack, MFA requirement, allowed domains, limits, branding)
  - Track creation and update timestamps
AND the organization can contain multiple teams and users
AND plan values are validated against allowed options
```

**Entity Attributes** (Semantic):

| Attribute | Description | Constraints |
|-----------|-------------|-------------|
| Identifier | Unique organization ID | Globally unique |
| Name | Display name | 1-255 characters, required |
| Slug | URL-safe identifier | Lowercase alphanumeric + hyphens, globally unique |
| Plan | Subscription tier | Enumerated: free, pro, enterprise |
| Settings | Configuration object | Default policy, MFA, domains, limits, branding |
| Timestamps | Created/Updated | System-managed |

**Tier Requirements**:

| Tier | Organizations | Max Teams | Max Projects/Team | MFA |
|------|--------------|-----------|-------------------|-----|
| **LITE** | Not supported | - | - | - |
| **STANDARD** | 1 (personal) | 5 | 20 | Optional |
| **PROFESSIONAL** | 1 | 20 | Unlimited | Optional |
| **ENTERPRISE** | Multiple | Unlimited | Unlimited | Configurable |

---

### FR-002: Teams - Collaboration Units

**Description**: Teams are collaboration units within organizations, grouping users and projects together with team-level configuration.

**Requirement**:

```gherkin
GIVEN the system supports team-based collaboration
WHEN a team is created within an organization
THEN the system SHALL:
  - Assign a unique identifier
  - Link to parent organization (cascade on delete)
  - Enforce slug uniqueness within organization scope
  - Allow optional description
  - Store team-specific settings (approvers, notifications, webhooks)
  - Track creation and update timestamps
AND the team can contain multiple members
AND the team can own multiple projects
```

**Entity Attributes** (Semantic):

| Attribute | Description | Constraints |
|-----------|-------------|-------------|
| Identifier | Unique team ID | Globally unique |
| Organization | Parent organization | Required, cascade delete |
| Name | Display name | 1-255 characters, required |
| Slug | URL-safe identifier | Unique within organization |
| Description | Team description | Optional text |
| Settings | Configuration object | Approvers, notifications, webhooks |
| Timestamps | Created/Updated | System-managed |

**Tier Requirements**:

| Tier | Teams/Org | Members/Team | Projects/Team | Description Limit |
|------|-----------|--------------|---------------|-------------------|
| **LITE** | N/A | - | - | - |
| **STANDARD** | 5 | 10 | 20 | 500 chars |
| **PROFESSIONAL** | 20 | 50 | Unlimited | 2000 chars |
| **ENTERPRISE** | Unlimited | Unlimited | Unlimited | Unlimited |

---

### FR-003: Team Membership - SASE-Compliant Roles

**Description**: Team membership supports hybrid human-AI team composition with role-based access control aligned with SASE principles.

**Requirement**:

```gherkin
GIVEN the system supports hybrid human-AI team composition
WHEN a user is added to a team with role and member type
THEN the system SHALL:
  - Assign a unique membership identifier
  - Link to team and user (cascade on delete)
  - Enforce role assignment (owner, admin, member, ai_agent)
  - Enforce member type (human, ai_agent)
  - Record join timestamp
  - Prevent duplicate memberships (one per user per team)
AND the system SHALL enforce SASE principle:
  - AI agents (member_type=ai_agent) CANNOT have owner or admin roles
  - Human members can have any role
```

**Role Definitions (SASE Aligned)**:

| Role | SASE Role | Member Type | Description | Permissions |
|------|-----------|-------------|-------------|-------------|
| `owner` | SE4H (Coach) | human only | Team creator, VCR authority | Full control, delete team, transfer ownership, approve MRP |
| `admin` | SE4H (Coach) | human only | Team administrator | Manage members, settings, MentorScript maintenance |
| `member` | SE4H/SE4A | human/ai_agent | Regular team member | View team, contribute to projects, create MRP |
| `ai_agent` | SE4A (Executor) | ai_agent only | AI agent executor | Read-only BRS, create MRP/CRP, execute tasks |

**Member Type Definitions**:

| Member Type | Description | Allowed Roles | SASE Constraint |
|-------------|-------------|---------------|-----------------|
| `human` | Human team member (SE4H) | owner, admin, member | Full role access |
| `ai_agent` | AI agent (SE4A) | member, ai_agent | **CANNOT** be owner/admin |

**Tier Requirements**:

| Tier | Max Members | AI Agents | VCR Approval | SASE Enforcement |
|------|-------------|-----------|--------------|------------------|
| **LITE** | N/A | - | - | - |
| **STANDARD** | 10 | Not supported | Not required | N/A |
| **PROFESSIONAL** | 50 | Max 5/team | Required | Mandatory |
| **ENTERPRISE** | Unlimited | Unlimited | Required | Mandatory |

---

### FR-004: User-Organization Association

**Description**: Users are associated with organizations for multi-tenant isolation.

**Requirement**:

```gherkin
GIVEN the system requires multi-tenant user isolation
WHEN a user is associated with an organization
THEN the system SHALL:
  - Store organization reference on user record
  - Enforce referential integrity
  - Support migration from single-tenant to multi-tenant
AND existing users are assigned to a default organization during migration
```

---

### FR-005: Project-Team Association

**Description**: Projects are associated with teams for team-scoped management.

**Requirement**:

```gherkin
GIVEN the system requires team-scoped project management
WHEN a project is associated with a team
THEN the system SHALL:
  - Store team reference on project record
  - Enforce referential integrity
  - Support migration from unassigned to team-based
AND existing projects are assigned to a default team during migration
```

---

## 2. Non-Functional Requirements

### NFR-001: Performance Targets

| Operation | Target Latency (p95) | Concurrency | Tier |
|-----------|---------------------|-------------|------|
| Organization create | <50ms | 10 req/s | ALL |
| Team create | <50ms | 50 req/s | ALL |
| Team member add | <30ms | 100 req/s | ALL |
| Team list (with members) | <100ms | 500 req/s | ALL |
| Organization lookup by slug | <10ms | 1000 req/s | ALL |

### NFR-002: Security & Compliance

| Requirement | Tier | Description |
|-------------|------|-------------|
| Row-level security | PROFESSIONAL+ | Filter queries by organization scope |
| Audit logging | ENTERPRISE | Track all role changes immutably |
| MFA enforcement | ENTERPRISE | Configurable per organization |
| SASE compliance | PROFESSIONAL+ | Enforce AI agent role restrictions |

### NFR-003: Scalability Limits

| Tier | Max Organizations | Max Teams/Org | Max Members/Team | Max Projects/Team |
|------|------------------|---------------|------------------|-------------------|
| **STANDARD** | 1 | 5 | 10 | 20 |
| **PROFESSIONAL** | 1 | 20 | 50 | Unlimited |
| **ENTERPRISE** | Unlimited | Unlimited | Unlimited | Unlimited |

---

## 3. Acceptance Criteria

### AC-001: Organization Entity

```gherkin
GIVEN the multi-tenant system is deployed
WHEN an organization is created with valid name, slug, and plan
THEN the organization is persisted with unique identifier
AND the slug is globally unique
AND the plan is validated against allowed values
AND timestamps are automatically managed
```

### AC-002: Team Entity

```gherkin
GIVEN an organization exists
WHEN a team is created with valid name and slug
THEN the team is persisted with unique identifier
AND the team is linked to the parent organization
AND the slug is unique within the organization scope
AND deleting the organization cascades to delete the team
```

### AC-003: SASE Constraint Enforcement

```gherkin
GIVEN the SASE principle "AI agents cannot be decision-makers"
WHEN an AI agent is added to a team with role 'owner' or 'admin'
THEN the system SHALL reject the request with clear error message
AND when an AI agent is added with role 'member' or 'ai_agent'
THEN the system SHALL accept the request
```

### AC-004: Membership Uniqueness

```gherkin
GIVEN a user is already a member of a team
WHEN the same user is added to the same team again
THEN the system SHALL reject the duplicate membership
```

### AC-005: Cascade Delete Behavior

```gherkin
GIVEN an organization with teams and team members
WHEN the organization is deleted
THEN all child teams are deleted
AND all team memberships are deleted
AND users are NOT deleted (remain orphaned from organization)
AND projects are NOT deleted (remain with orphaned team reference)
```

### AC-006: Migration Compatibility

```gherkin
GIVEN existing users and projects without organization/team associations
WHEN the multi-tenant feature is deployed
THEN existing users are assigned to a default organization
AND existing projects are assigned to a default team
AND zero downtime is achieved during migration
```

---

## 4. Design Decisions

### Decision 1: Flexible Settings over Fixed Schema

**Rationale**: Use flexible configuration objects for organization and team settings to allow schema evolution without breaking changes.

**Pros**:
- No schema changes required for new settings
- Supports tenant-specific configuration
- Queryable and indexable

**Cons**:
- Validation must be done in application layer
- No referential integrity for nested keys

### Decision 2: Slug Uniqueness Scoped to Organization

**Rationale**: Team slugs are unique per organization, not globally, allowing different orgs to use the same slug (e.g., "backend-team").

**Pros**:
- Natural naming for teams
- Cleaner URLs: `/orgs/{org-slug}/teams/{team-slug}`

**Cons**:
- Slug lookup requires organization context

### Decision 3: SASE-Compliant AI Agent Restrictions

**Rationale**: Enforce SASE principles at data layer: AI agents (SE4A Executors) cannot have owner/admin roles (SE4H Coaches).

**Pros**:
- Cannot be bypassed by application bugs
- Aligns with SDLC AI Governance Principles
- Prevents VCR authority delegation to AI agents

**Reference**: SDLC Framework Section "AI Governance Principles", Principle 2: "AI agents are executors, not decision-makers"

### Decision 4: Zero-Downtime Migration Strategy

**Rationale**: Use phased migration (nullable → data migration → required) for zero-downtime deployment.

**Pros**:
- Application continues running during migration
- Safe rollback capability

---

## 5. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Data migration failure | MEDIUM | HIGH | Test with production-like dataset, maintain rollback plan |
| SASE constraint breaks workflows | LOW | MEDIUM | Audit existing AI agent usage before migration |
| Performance degradation | MEDIUM | MEDIUM | Index all foreign keys, optimize relationship queries |

---

## 6. Tier-Specific Summary

### STANDARD Tier: Personal Team Collaboration

- 1 organization (personal)
- Max 5 teams, 10 members/team, 20 projects/team
- AI Agents: NOT supported
- VCR Approval: NOT required

### PROFESSIONAL Tier: Team Collaboration with AI Agents

- 1 organization
- Max 20 teams, 50 members/team, unlimited projects
- AI Agents: Max 5 per team, SASE-compliant
- VCR Approval: Required (owner/admin only)

### ENTERPRISE Tier: Multi-Tenant with Unlimited Scale

- Unlimited organizations, teams, members, projects
- AI Agents: Unlimited, SASE-compliant
- VCR Approval: Required
- Additional: MFA enforcement, row-level security, audit logging

---

## Document Control

| Field | Value |
|-------|-------|
| **Spec ID** | SPEC-0013 |
| **Version** | 2.0.0 |
| **Status** | APPROVED |
| **Author** | Backend Lead |
| **Reviewer** | CTO |
| **Last Updated** | 2026-01-29 |
| **Framework Version** | 6.0.5 |

---

**Pure Methodology Notes**:
- This specification defines WHAT governance requirements apply to multi-tenant team management
- For HOW to implement (database schemas, ORM models, migrations), see SDLC-Orchestrator technical documentation
- SASE principles referenced from SDLC Framework AI Governance section
- Tier requirements are semantic limits, implementation enforces via appropriate mechanism

---

**End of Specification**
