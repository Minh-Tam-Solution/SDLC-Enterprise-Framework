# Example Specification: LITE Tier

This example demonstrates the minimal specification format for LITE tier projects.

---

```markdown
---
spec_id: SPEC-0042
spec_name: "Basic User Authentication"
spec_version: "1.0.0"
status: approved
tier: LITE
stage: "03"
category: security
owner: "backend-team"
created: 2026-01-15
last_updated: 2026-01-28
---

## 1. Overview

Basic User Authentication provides email/password login for small projects with a single team (<10 users).

**Key Objectives**:
- Enable user login with email and password
- Issue session tokens for authenticated requests
- Provide logout functionality

**Scope**:
- **In Scope**: Email/password login, session management
- **Out of Scope**: OAuth, MFA, SSO

## 3. Requirements

### 3.1 Functional Requirements

#### FR-001: User Login
**Priority**: P0
**Tier**: LITE

```gherkin
GIVEN a registered user with valid email and password
WHEN they submit login credentials
THEN they receive a session token valid for 24 hours
  AND they are redirected to the dashboard
```

#### FR-002: User Logout
**Priority**: P0
**Tier**: LITE

```gherkin
GIVEN an authenticated user
WHEN they click the logout button
THEN their session token is invalidated
  AND they are redirected to the login page
```

#### FR-003: Invalid Credentials
**Priority**: P1
**Tier**: LITE

```gherkin
GIVEN a user with invalid credentials
WHEN they attempt to login
THEN they receive an error message "Invalid email or password"
  AND the login attempt is logged
```

### 3.2 Non-Functional Requirements

| Metric | Target | Measurement |
|--------|--------|-------------|
| Login API latency | <500ms | Server logs |
| Session token expiry | 24 hours | Configuration |
| Password hash | bcrypt cost=10 | Code review |

## 6. Acceptance Criteria

| ID | Criterion | Test Type | Priority |
|----|-----------|-----------|----------|
| AC-001 | Valid credentials return 200 + token | Unit | P0 |
| AC-002 | Invalid credentials return 401 | Unit | P0 |
| AC-003 | Logout invalidates session | Integration | P0 |
| AC-004 | Token expires after 24 hours | Unit | P1 |
```

---

## Notes

This LITE tier example demonstrates:

1. **Minimal frontmatter** - Only required fields
2. **Focused scope** - Limited features, clear boundaries
3. **Simple requirements** - Core functionality only
4. **Basic acceptance criteria** - Essential tests

LITE tier specifications are appropriate for:
- Small projects (<10 users)
- Single team ownership
- Limited compliance requirements
- MVP or prototype phases
