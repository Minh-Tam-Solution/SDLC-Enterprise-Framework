# SPEC_DELTA.md Template
## Framework 6.0.6 Specification Change Tracking - Section 8

**Version**: 6.0.6
**Status**: ACTIVE - PRODUCTION READY
**Created**: January 28, 2026
**Author**: PM/PJM Team
**Framework**: SDLC 6.0.6 (7-Pillar + 2-Section)
**Section**: Section 8: Unified Specification Standard

---

## 1. Purpose

SPEC_DELTA.md tracks **changes between specification versions**, providing:

- Clear changelog for each version transition
- Breaking change identification and migration paths
- Impact assessment for downstream consumers
- Audit trail for compliance requirements

**Key Use Cases**:
- API contract evolution
- Requirements refinement
- Feature scope changes
- Deprecation tracking

---

## 2. Template Structure

### 2.1 YAML Frontmatter

```yaml
---
# Delta Metadata
delta_id: DELTA-[NNNN]
spec_id: SPEC-[NNNN]
spec_name: "[Specification Name]"

# Version Information
from_version: "X.Y.Z"
to_version: "X.Y.Z"
delta_type: major | minor | patch

# Classification
breaking_changes: true | false
migration_required: true | false
backward_compatible: true | false

# Timeline
created: YYYY-MM-DD
effective_date: YYYY-MM-DD
deprecation_date: YYYY-MM-DD | null
sunset_date: YYYY-MM-DD | null

# Ownership
author: "[name/team]"
reviewers: ["reviewer1", "reviewer2"]
approver: "[approver]"

# Relationships
related_deltas: ["DELTA-XXX"]
affected_specs: ["SPEC-XXX", "SPEC-YYY"]
affected_systems: ["system1", "system2"]
---
```

### 2.2 Content Sections

```markdown
## Spec Delta: [Spec Name] v[from] → v[to]

### Summary
[1-2 sentence summary of changes]

### Change Classification

| Metric | Value |
|--------|-------|
| Delta Type | major/minor/patch |
| Breaking Changes | Yes/No |
| Migration Required | Yes/No |
| Backward Compatible | Yes/No |
| Affected Systems | [count] |

### Changes

#### Added
- [New requirement/feature 1]
- [New requirement/feature 2]

#### Modified
| Original | New | Rationale |
|----------|-----|-----------|
| [old] | [new] | [why] |

#### Deprecated
| Item | Deprecated In | Sunset Date | Alternative |
|------|---------------|-------------|-------------|
| [item] | v1.2.0 | 2026-06-01 | [use this instead] |

#### Removed
- [Removed item 1] - Reason: [...]
- [Removed item 2] - Reason: [...]

### Breaking Changes

⚠️ **Breaking Change 1: [Title]**
- **What Changed**: [Description]
- **Impact**: [Who/what is affected]
- **Migration**: [How to update]
- **Timeline**: [When migration required]

### Migration Guide

#### Prerequisites
- [Prerequisite 1]
- [Prerequisite 2]

#### Step-by-Step Migration
1. [Step 1]
2. [Step 2]
3. [Step 3]

#### Validation
- [ ] [Validation check 1]
- [ ] [Validation check 2]

### Backward Compatibility

[Notes on backward compatibility, if applicable]

### Rollback Procedure

[How to rollback if issues arise]
```

---

## 3. Complete Template

```markdown
---
delta_id: DELTA-0001
spec_id: SPEC-0042
spec_name: "User Authentication"

from_version: "1.0.0"
to_version: "2.0.0"
delta_type: major

breaking_changes: true
migration_required: true
backward_compatible: false

created: 2026-01-28
effective_date: 2026-02-15
deprecation_date: null
sunset_date: null

author: "backend-team"
reviewers: ["security-lead", "tech-lead"]
approver: "CTO"

related_deltas: []
affected_specs: ["SPEC-0055", "SPEC-0078"]
affected_systems: ["api-gateway", "mobile-app", "web-dashboard"]
---

## Spec Delta: User Authentication v1.0.0 → v2.0.0

### Summary

Major upgrade introducing OAuth 2.0 and MFA support, deprecating basic email/password-only authentication.

### Change Classification

| Metric | Value |
|--------|-------|
| Delta Type | Major |
| Breaking Changes | Yes |
| Migration Required | Yes |
| Backward Compatible | No |
| Affected Systems | 3 |

### Changes

#### Added

- **FR-010**: OAuth 2.0 authentication (GitHub, Google, Microsoft)
- **FR-011**: Multi-factor authentication (TOTP)
- **FR-012**: Session management with refresh tokens
- **NFR-005**: 15-minute access token expiry
- **NFR-006**: 7-day refresh token rotation

#### Modified

| Original | New | Rationale |
|----------|-----|-----------|
| Session token (24h expiry) | Access token (15min) + Refresh token | Security hardening |
| Password min 8 chars | Password min 12 chars | OWASP compliance |
| bcrypt cost=10 | bcrypt cost=12 | Increased security |

#### Deprecated

| Item | Deprecated In | Sunset Date | Alternative |
|------|---------------|-------------|-------------|
| Basic auth header | v2.0.0 | 2026-06-01 | Bearer token |
| `/api/v1/login` endpoint | v2.0.0 | 2026-06-01 | `/api/v2/auth/token` |

#### Removed

- Legacy session cookie authentication - Reason: Replaced by JWT
- Password reset via email link only - Reason: Now requires MFA verification

### Breaking Changes

⚠️ **Breaking Change 1: Token Format Change**
- **What Changed**: Session tokens replaced with JWT access/refresh token pair
- **Impact**: All API clients must update authentication handling
- **Migration**:
  1. Update token storage (separate access/refresh)
  2. Implement token refresh flow
  3. Handle 401 with automatic refresh
- **Timeline**: Complete by 2026-02-15 (effective date)

⚠️ **Breaking Change 2: Endpoint Migration**
- **What Changed**: `/api/v1/login` → `/api/v2/auth/token`
- **Impact**: All login flows must update endpoint
- **Migration**:
  1. Update API base URL to v2
  2. Adjust request/response handling
  3. Test with staging environment
- **Timeline**: v1 endpoints sunset 2026-06-01

⚠️ **Breaking Change 3: Password Requirements**
- **What Changed**: Minimum password length 8 → 12 characters
- **Impact**: Existing users with short passwords
- **Migration**:
  1. Flag accounts with non-compliant passwords
  2. Force password update on next login
  3. Send notification emails
- **Timeline**: Enforcement begins 2026-02-15

### Migration Guide

#### Prerequisites

- Access to API v2 staging environment
- Updated SDK version (≥3.0.0)
- Test accounts with OAuth providers configured

#### Step-by-Step Migration

1. **Update Authentication SDK**
   ```bash
   npm install @sdlc/auth-sdk@^3.0.0
   ```

2. **Configure OAuth Providers**
   ```javascript
   authClient.configure({
     providers: ['github', 'google'],
     tokenEndpoint: '/api/v2/auth/token',
     refreshEndpoint: '/api/v2/auth/refresh'
   });
   ```

3. **Implement Token Refresh Flow**
   ```javascript
   authClient.onTokenExpired(async () => {
     const newTokens = await authClient.refreshTokens();
     // Store new tokens
   });
   ```

4. **Update Password Validation**
   ```javascript
   const passwordPolicy = {
     minLength: 12,
     requireUppercase: true,
     requireNumber: true,
     requireSpecial: true
   };
   ```

5. **Test Authentication Flows**
   - [ ] Email/password login
   - [ ] OAuth login (each provider)
   - [ ] MFA enrollment
   - [ ] MFA verification
   - [ ] Token refresh
   - [ ] Logout

#### Validation

- [ ] All login flows work with v2 API
- [ ] Token refresh handles expiry gracefully
- [ ] MFA enrollment completes successfully
- [ ] Logout invalidates all tokens
- [ ] Error handling covers all edge cases

### Backward Compatibility

**v1 API Deprecation Timeline**:
- v2.0.0 release: v1 endpoints marked deprecated
- 2026-04-01: v1 returns deprecation warning header
- 2026-06-01: v1 endpoints return 410 Gone

**Compatibility Layer** (optional):
A compatibility shim is available for gradual migration:
```javascript
import { v1Compat } from '@sdlc/auth-sdk/compat';
// Wraps v1 calls and translates to v2
```

### Rollback Procedure

If critical issues arise post-migration:

1. **Immediate (< 24h post-migration)**
   - Revert to v1 endpoints (still available)
   - Rollback SDK to v2.x.x
   - Notify users of temporary regression

2. **Extended (> 24h post-migration)**
   - Assess issue severity
   - Patch v2 or extend v1 availability
   - Communicate timeline to stakeholders

### Approval

| Role | Status | Date |
|------|--------|------|
| Author | ✅ Created | 2026-01-28 |
| Security Lead | ✅ Reviewed | 2026-01-29 |
| Tech Lead | ✅ Reviewed | 2026-01-29 |
| CTO | ✅ Approved | 2026-01-30 |
```

---

## 4. Delta Types

### 4.1 Semantic Versioning Alignment

| Delta Type | Version Bump | Description | Breaking |
|------------|--------------|-------------|----------|
| **Major** | X.0.0 | Breaking changes, removed features | Yes |
| **Minor** | 0.X.0 | New features, backward compatible | No |
| **Patch** | 0.0.X | Bug fixes, documentation | No |

### 4.2 Examples

**Major (Breaking)**:
- API endpoint removed or renamed
- Required field added
- Response format changed
- Authentication method changed

**Minor (Additive)**:
- New optional field added
- New endpoint added
- New feature flag
- Enhanced error messages

**Patch (Fix)**:
- Typo corrections
- Clarified requirements
- Bug fix documentation
- Example updates

---

## 5. Impact Assessment

### 5.1 Affected Systems Checklist

When creating a delta, assess impact on:

```yaml
Systems Checklist:
  Frontend:
    - [ ] Web dashboard
    - [ ] Mobile app
    - [ ] Admin portal

  Backend:
    - [ ] API gateway
    - [ ] Microservices
    - [ ] Background jobs

  Integrations:
    - [ ] Third-party APIs
    - [ ] Webhooks
    - [ ] SDK consumers

  Documentation:
    - [ ] API docs
    - [ ] User guides
    - [ ] Developer portal
```

### 5.2 Risk Matrix

| Breaking Changes | Migration Effort | Risk Level |
|------------------|------------------|------------|
| None | None | 🟢 Low |
| None | Low | 🟢 Low |
| Minor | Low | 🟡 Medium |
| Minor | Medium | 🟡 Medium |
| Major | Any | 🔴 High |

---

## 6. Directory Structure

### 6.1 Organization

```
project/
├── docs/
│   └── specs/
│       ├── SPEC-0042-authentication.md
│       └── deltas/
│           ├── DELTA-0001-v1-to-v2.md
│           ├── DELTA-0002-v2-to-v2.1.md
│           └── README.md (delta index)
└── ...
```

### 6.2 Naming Convention

```
DELTA-[NNNN]-v[from]-to-v[to].md

Examples:
- DELTA-0001-v1.0.0-to-v2.0.0.md
- DELTA-0002-v2.0.0-to-v2.1.0.md
- DELTA-0015-v3.5.0-to-v4.0.0.md
```

---

## 7. Validation Rules

### 7.1 Required Fields

```yaml
Mandatory:
  - delta_id
  - spec_id
  - from_version
  - to_version
  - delta_type
  - breaking_changes
  - created
  - author

Conditional:
  - migration_guide (if breaking_changes = true)
  - sunset_date (if deprecations exist)
  - affected_systems (if breaking_changes = true)
```

### 7.2 CLI Commands

```bash
# Create new delta
sdlcctl delta new --spec SPEC-0042 --from 1.0.0 --to 2.0.0

# Validate delta format
sdlcctl delta validate deltas/DELTA-0001.md

# List deltas for a spec
sdlcctl delta list --spec SPEC-0042

# Check for breaking changes
sdlcctl delta breaking --spec SPEC-0042

# Generate migration checklist
sdlcctl delta migration-checklist DELTA-0001
```

---

## 8. Integration with CI/CD

### 8.1 Pre-Merge Validation

```yaml
# .github/workflows/spec-delta.yml
name: Spec Delta Validation

on:
  pull_request:
    paths:
      - 'docs/specs/**/*.md'

jobs:
  validate-delta:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Check for spec changes
        id: spec-changes
        run: |
          if git diff --name-only origin/main | grep -q "docs/specs/SPEC-"; then
            echo "spec_changed=true" >> $GITHUB_OUTPUT
          fi

      - name: Require delta for breaking changes
        if: steps.spec-changes.outputs.spec_changed == 'true'
        run: |
          sdlcctl delta validate --require-for-major
```

### 8.2 Release Notes Generation

```bash
# Generate release notes from deltas
sdlcctl delta release-notes \
  --from v1.0.0 \
  --to v2.0.0 \
  --output RELEASE-NOTES.md
```

---

## 9. Best Practices

### 9.1 Writing Effective Deltas

**DO**:
- ✅ Document ALL breaking changes explicitly
- ✅ Provide complete migration steps
- ✅ Include code examples for migrations
- ✅ Set realistic sunset dates
- ✅ Test migration steps before publishing
- ✅ Notify affected teams early

**DON'T**:
- ❌ Combine unrelated changes in one delta
- ❌ Omit rollback procedures
- ❌ Set unrealistic migration timelines
- ❌ Forget to update affected_systems
- ❌ Skip validation checklist

### 9.2 Communication Timeline

| Milestone | Action |
|-----------|--------|
| Delta Created | Notify tech leads |
| Delta Approved | Announce to affected teams |
| 30 days before effective | Send reminder + migration guide |
| 7 days before effective | Final warning |
| Effective date | Enforce new version |
| Sunset date | Disable old version |

---

## 10. Document Control

| Field | Value |
|-------|-------|
| **Template ID** | SDLC-DELTA-TPL-001 |
| **Version** | 1.0.0 |
| **Status** | APPROVED |
| **Created** | January 28, 2026 |
| **Author** | PM/PJM Team |
| **Reviewers** | CTO, Tech Lead |
| **Framework** | SDLC 6.0 |

---

*SDLC Enterprise Framework 6.0 - Spec Delta Template*
*"Track changes. Communicate impact. Migrate safely."*
