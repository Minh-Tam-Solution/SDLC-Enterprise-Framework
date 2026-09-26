# Example Specification: STANDARD Tier

This example demonstrates the standard specification format with full section requirements.

---

```markdown
---
# Core Metadata
spec_id: SPEC-0108
spec_name: "Evidence Vault Upload Service"
spec_version: "1.2.0"
status: approved
tier: STANDARD
stage: "03"
category: functional

# Ownership
owner: "backend-team"
reviewers: ["tech-lead", "security-lead"]
approver: "CTO"

# Timestamps
created: 2025-12-01
last_updated: 2026-01-28
approved_date: 2026-01-15

# Relationships
related_adrs: ["ADR-005", "ADR-012"]
related_specs: ["SPEC-0042", "SPEC-0055"]
parent_spec: null
supersedes: "SPEC-0087"

# Tags
tags: ["evidence", "storage", "audit"]
priority: P0
effort: M
---

## 1. Overview

Evidence Vault Upload Service enables secure upload and storage of development artifacts (screenshots, documents, code samples) with full audit trail and integrity verification.

**Key Objectives**:
- Secure file upload to S3-compatible storage (MinIO)
- SHA256 integrity hashing for all files
- Metadata storage in PostgreSQL
- Audit trail for compliance

**Scope**:
- **In Scope**: File upload, metadata, integrity verification, audit logs
- **Out of Scope**: File editing, version control, real-time collaboration

## 2. Context

### 2.1 Problem Statement

Development teams need a centralized, secure storage for evidence artifacts that support gate evaluation. Current ad-hoc storage lacks integrity verification and audit trail.

### 2.2 Background

Evidence Vault is part of the SDLC Orchestrator governance layer. Files uploaded are linked to gate evaluations and provide audit trail for compliance.

### 2.3 Stakeholders

| Stakeholder | Role | Interest |
|-------------|------|----------|
| Development Team | Users | Easy upload, retrieval |
| QA Team | Reviewers | Access evidence for testing |
| Compliance | Auditors | Immutable audit trail |
| Security | Approvers | Secure storage, access control |

### 2.4 Assumptions

- MinIO is deployed and accessible
- PostgreSQL database available
- JWT authentication configured
- Network connectivity stable

### 2.5 Constraints

- AGPL containment: Network-only access to MinIO (no SDK import)
- File size limit: 100MB per file
- Storage quota: 10GB per project (STANDARD tier)

## 3. Requirements

### 3.1 Functional Requirements

#### FR-001: File Upload
**Priority**: P0
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN an authenticated user with write permissions
  AND a file smaller than 100MB
WHEN they upload a file to Evidence Vault
THEN the file is stored in MinIO with SHA256 hash
  AND metadata is recorded in PostgreSQL
  AND an audit log entry is created
  AND the file URL is returned
```

#### FR-002: File Retrieval
**Priority**: P0
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN an authenticated user with read permissions
  AND a valid evidence ID
WHEN they request the file
THEN the file is returned with correct content-type
  AND the access is logged in audit trail
```

#### FR-003: Integrity Verification
**Priority**: P1
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN a stored file in Evidence Vault
WHEN the system performs integrity check
THEN the current SHA256 hash is computed
  AND compared with stored hash
  AND result is logged (PASS/FAIL)
```

#### FR-004: Audit Trail
**Priority**: P1
**Tier**: STANDARD, PROFESSIONAL, ENTERPRISE

```gherkin
GIVEN any action on Evidence Vault
WHEN upload, download, delete, or verify occurs
THEN an immutable audit log is created
  AND includes: user_id, action, timestamp, IP, resource_id
```

### 3.2 Non-Functional Requirements

#### NFR-001: Performance
| Metric | Target | Measurement |
|--------|--------|-------------|
| Upload latency (10MB) | <2s | Prometheus histogram |
| Download latency (10MB) | <1s | Prometheus histogram |
| API p95 latency | <200ms | Prometheus histogram |

#### NFR-002: Security
| Requirement | Standard | Verification |
|-------------|----------|--------------|
| Encryption at-rest | AES-256 (MinIO) | Config audit |
| Encryption in-transit | TLS 1.3 | SSL Labs |
| Access control | RBAC | Integration test |

#### NFR-003: Availability
| Metric | Target | Measurement |
|--------|--------|-------------|
| Uptime | 99.9% | Prometheus |
| Data durability | 99.99% | MinIO config |

### 3.3 Tier-Specific Requirements

| Requirement | LITE | STANDARD | PROFESSIONAL | ENTERPRISE |
|-------------|------|----------|--------------|------------|
| Storage quota | 1GB | 10GB | 100GB | Unlimited |
| File size limit | 10MB | 100MB | 500MB | 1GB |
| Retention | 30 days | 1 year | 5 years | Custom |
| Audit logs | 7 days | 30 days | 1 year | 7 years |
| Integrity check | Manual | Daily | Hourly | Real-time |

## 4. Design Decisions

### 4.1 Related ADRs

| ADR | Title | Status | Impact on This Spec |
|-----|-------|--------|---------------------|
| ADR-005 | MinIO AGPL Containment | Accepted | Network-only access |
| ADR-012 | Evidence State Machine | Accepted | 8-state lifecycle |

### 4.2 Key Decisions

#### Decision 1: Network-Only MinIO Access
- **Status**: Decided
- **ADR Reference**: ADR-005
- **Summary**: Use HTTP API calls to MinIO, no SDK import
- **Impact**: Slightly more code, but AGPL-safe

#### Decision 2: SHA256 for Integrity
- **Status**: Decided
- **Summary**: SHA256 chosen for balance of security and performance
- **Impact**: Hashing adds ~50ms per 10MB file

## 5. Technical Specification

### 5.1 Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Evidence Vault Service                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────┐      ┌───────────┐      ┌───────────┐          │
│  │  FastAPI  │─────▶│  Service  │─────▶│  MinIO    │          │
│  │  Router   │      │  Layer    │      │  (S3 API) │          │
│  └───────────┘      └───────────┘      └───────────┘          │
│        │                  │                                    │
│        ▼                  ▼                                    │
│  ┌───────────┐      ┌───────────┐                             │
│  │  Auth     │      │ PostgreSQL│                             │
│  │  Middleware│     │ (Metadata)│                             │
│  └───────────┘      └───────────┘                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Data Model

```yaml
Entity: Evidence
  Fields:
    - id: UUID (PK)
    - project_id: UUID (FK) NOT NULL
    - file_name: VARCHAR(255) NOT NULL
    - file_size: BIGINT NOT NULL
    - content_type: VARCHAR(100) NOT NULL
    - sha256_hash: CHAR(64) NOT NULL
    - storage_path: VARCHAR(500) NOT NULL
    - uploaded_by: UUID (FK) NOT NULL
    - created_at: TIMESTAMP DEFAULT NOW()
    - state: ENUM('uploaded', 'verified', 'locked', 'deleted')
  Indexes:
    - project_id
    - sha256_hash
    - created_at
```

### 5.3 API Contracts

```yaml
Endpoint: POST /api/v1/evidence/upload
  Description: Upload file to Evidence Vault
  Authentication: Bearer token
  Request:
    Content-Type: multipart/form-data
    Body:
      file: binary (required, max 100MB)
      project_id: UUID (required)
      description: string (optional)
  Response:
    201:
      id: UUID
      file_name: string
      sha256_hash: string
      storage_url: string
    400:
      error: "File too large" | "Invalid format"
    401:
      error: "Unauthorized"
    403:
      error: "Insufficient permissions"
```

### 5.4 Security Considerations

- **Authentication**: JWT token required for all endpoints
- **Authorization**: RBAC with project-level permissions
- **Data Protection**: AES-256 at-rest, TLS 1.3 in-transit
- **Audit**: All actions logged with user, timestamp, IP

## 6. Acceptance Criteria

### 6.1 Functional Acceptance

| ID | Criterion | Test Type | Priority |
|----|-----------|-----------|----------|
| AC-001 | Upload 10MB file <2s | Integration | P0 |
| AC-002 | SHA256 hash computed correctly | Unit | P0 |
| AC-003 | Metadata stored in PostgreSQL | Integration | P0 |
| AC-004 | Audit log created on upload | Integration | P1 |
| AC-005 | Unauthorized access returns 401 | Unit | P0 |

### 6.2 Performance Acceptance

| Metric | Threshold | Test Method | Blocker |
|--------|-----------|-------------|---------|
| Upload 10MB | <2s | pytest-benchmark | Yes |
| API p95 | <200ms | Locust | Yes |
| Concurrent uploads | 50 | Locust | No |

### 6.3 Definition of Done

- [ ] All P0 acceptance criteria pass
- [ ] Code review approved (2+ reviewers)
- [ ] Security review passed
- [ ] Documentation updated
- [ ] No P0/P1 bugs outstanding

## 7. Spec Delta

### 7.1 Current Version Changes (v1.1.0 → v1.2.0)

**Summary**: Added integrity verification and audit trail enhancements

**Impact**: non-breaking

#### Added
- FR-003: Integrity Verification (automatic daily check)
- Hourly integrity check for PROFESSIONAL tier

#### Modified

| Original | New | Rationale |
|----------|-----|-----------|
| Audit logs 7 days | Audit logs 30 days (STANDARD) | Compliance requirement |

#### Deprecated
- None

## 8. Dependencies

### 8.1 Upstream Dependencies

| Dependency | Type | Version | Status | Risk |
|------------|------|---------|--------|------|
| SPEC-0042 | Specification | 1.0.0 | Approved | Low |
| MinIO | Storage | Latest | Stable | Low |
| PostgreSQL | Database | 15.5 | Stable | Low |

### 8.2 Downstream Dependencies

| Dependent | Type | Impact if Changed |
|-----------|------|-------------------|
| Gate Evaluation | Service | Evidence links break |
| Audit Report | Feature | Data format change |

## 9. Appendix

### 9.1 Glossary

| Term | Definition |
|------|------------|
| Evidence | File artifact supporting gate evaluation |
| Integrity Hash | SHA256 checksum for file verification |
| Audit Trail | Immutable log of all actions |

### 9.2 References

- [MinIO S3 API](https://min.io/docs/minio/linux/developers/minio-drivers.html)
- [OWASP File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)
```

---

## Notes

This STANDARD tier example demonstrates:

1. **Complete frontmatter** - All recommended fields
2. **Full context section** - Problem, stakeholders, constraints
3. **Detailed requirements** - BDD format with rationale
4. **Technical specification** - Architecture, data model, API
5. **Tier-specific requirements** - Clear differentiation
6. **Comprehensive acceptance criteria** - Testable items
7. **Spec delta** - Version tracking

STANDARD tier specifications are appropriate for:
- Medium projects (10-100 users)
- Multiple team collaboration
- Standard compliance requirements
- Production-ready features
