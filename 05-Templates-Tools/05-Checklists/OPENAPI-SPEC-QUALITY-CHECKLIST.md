# OpenAPI Specification Quality Checklist (SDLC 6.2.0)

**Version**: 1.0.0
**Date**: February 2, 2026
**Status**: ACTIVE
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Framework**: SDLC 6.2.1
**Purpose**: Ensure high-quality OpenAPI specifications for E2E testing

---

## Why OpenAPI Quality Matters

**Impact of Poor Quality**:
- ❌ **E2E Tests Fail**: Incomplete schemas → test generation fails
- ❌ **Client Code Breaks**: Missing examples → SDK generation produces unusable code
- ❌ **Documentation Gaps**: No descriptions → developers confused
- ❌ **Security Blind Spots**: Missing auth schemes → vulnerabilities undetected

**Benefits of High Quality**:
- ✅ **Auto-Generated Tests**: Complete spec → 80%+ test coverage automatic
- ✅ **SDK Generation**: Accurate spec → Python/TypeScript/Go clients auto-generated
- ✅ **Interactive Docs**: Rich spec → Swagger UI/ReDoc fully functional
- ✅ **Contract Validation**: Spec as truth → backend/frontend drift detected

---

## OpenAPI 3.1.0 Basic Structure

### Required Top-Level Fields

```yaml
openapi: 3.1.0  # ✅ Version must be 3.0.x or 3.1.x
info:
  title: My API
  version: 1.2.0
  description: Human-readable API description
paths:
  /users:
    get: ...
components:
  schemas: ...
  securitySchemes: ...
security: ...
```

**Checklist**:
- [ ] ✅ `openapi` field present (value: `3.0.x` or `3.1.0`)
- [ ] ✅ `info` object complete (title, version, description)
- [ ] ✅ `paths` object defines all endpoints
- [ ] ✅ `components` defines reusable schemas
- [ ] ✅ `security` defines authentication

---

## Phase 1: Metadata Quality

### Info Object

```yaml
info:
  title: SDLC Orchestrator API  # ✅ Clear, descriptive
  version: 1.2.0                 # ✅ Semantic versioning
  description: |
    AI-Native SDLC Governance Platform with Quality Gates.

    **Features**:
    - Evidence Vault with immutable audit trail
    - OPA Policy-as-Code engine
    - AI Task Decomposition
  contact:
    name: API Support
    email: api@sdlc-orchestrator.com
    url: https://docs.sdlc-orchestrator.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
```

**Checklist**:
- [ ] ✅ Title is human-readable (not just "API")
- [ ] ✅ Version follows semver (MAJOR.MINOR.PATCH)
- [ ] ✅ Description >100 characters (explains purpose)
- [ ] ✅ Contact info provided (email or URL)
- [ ] ✅ License specified (if open-source)

---

## Phase 2: Endpoint Completeness

### Path Item Quality

**Good Example**:
```yaml
/users/{user_id}:
  get:
    summary: Get user by ID
    description: Retrieves detailed information for a specific user.
    operationId: getUserById  # ✅ Unique ID for SDK generation
    tags:
      - Users  # ✅ Grouped for organization
    parameters:
      - name: user_id
        in: path
        required: true
        description: Unique user identifier (UUID)
        schema:
          type: string
          format: uuid
          example: "550e8400-e29b-41d4-a716-446655440000"
    responses:
      '200':
        description: User found
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
            examples:
              admin_user:
                summary: Admin user example
                value:
                  id: "550e8400-e29b-41d4-a716-446655440000"
                  email: "admin@example.com"
                  role: "admin"
      '404':
        description: User not found
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Error'
    security:
      - BearerAuth: []  # ✅ Auth required
```

**Checklist (Per Endpoint)**:
- [ ] ✅ `summary` present (1 sentence, <80 chars)
- [ ] ✅ `description` present (detailed explanation)
- [ ] ✅ `operationId` unique (snake_case or camelCase)
- [ ] ✅ `tags` assigned (for grouping in docs)
- [ ] ✅ `parameters` fully defined (name, in, schema, example)
- [ ] ✅ `responses` include success + error codes (200, 201, 400, 401, 404, 500)
- [ ] ✅ `security` specified (if auth required)

---

## Phase 3: Schema Quality

### Component Schemas

**Good Example**:
```yaml
components:
  schemas:
    User:
      type: object
      required:  # ✅ Required fields marked
        - id
        - email
        - created_at
      properties:
        id:
          type: string
          format: uuid
          description: Unique user identifier
          example: "550e8400-e29b-41d4-a716-446655440000"
        email:
          type: string
          format: email
          description: User's email address
          example: "user@example.com"
        role:
          type: string
          enum: [admin, developer, qa, viewer]  # ✅ Enum for fixed values
          description: User's role in the system
          example: "developer"
        created_at:
          type: string
          format: date-time
          description: Account creation timestamp
          example: "2026-02-02T10:30:00Z"
```

**Checklist (Per Schema)**:
- [ ] ✅ `type` specified (object, array, string, number, boolean)
- [ ] ✅ `required` array lists mandatory fields
- [ ] ✅ `properties` define all fields
- [ ] ✅ `description` for each property (explains purpose)
- [ ] ✅ `example` for each property (realistic value)
- [ ] ✅ `format` where applicable (uuid, email, date-time, uri)
- [ ] ✅ `enum` for fixed value sets
- [ ] ✅ `pattern` for validated strings (regex)
- [ ] ✅ Min/max constraints (minLength, maxLength, minimum, maximum)

---

## Phase 4: Security Schemes

### Authentication Definition

```yaml
components:
  securitySchemes:
    BearerAuth:  # ✅ JWT authentication
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: JWT token from POST /auth/login
    OAuth2:  # ✅ OAuth 2.0
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://auth.example.com/oauth/authorize
          tokenUrl: https://auth.example.com/oauth/token
          scopes:
            read:gates: Read gate status
            write:evidence: Upload evidence
            admin:policies: Manage policies

security:  # ✅ Default security for all endpoints
  - BearerAuth: []
```

**Checklist**:
- [ ] ✅ At least 1 security scheme defined
- [ ] ✅ `bearerFormat` specified for JWT
- [ ] ✅ OAuth scopes documented
- [ ] ✅ Global `security` applied (or per-endpoint)
- [ ] ✅ Public endpoints explicitly override with `security: []`

---

## Phase 5: Examples & Documentation

### Request Examples

```yaml
requestBody:
  description: User creation data
  required: true
  content:
    application/json:
      schema:
        $ref: '#/components/schemas/UserCreate'
      examples:  # ✅ Multiple examples for clarity
        developer:
          summary: Create developer account
          value:
            email: "dev@example.com"
            role: "developer"
            name: "Jane Developer"
        admin:
          summary: Create admin account
          value:
            email: "admin@example.com"
            role: "admin"
            name: "John Admin"
```

**Checklist**:
- [ ] ✅ Request body includes `examples` (not just schema)
- [ ] ✅ Response includes `examples` for each status code
- [ ] ✅ Examples use realistic data (not "string", "foo", "bar")
- [ ] ✅ Examples cover common use cases (success + error scenarios)

---

## Phase 6: Validation & Testing

### Automated Validation

**Tools**:
```bash
# 1. JSON Schema validation
npx @stoplight/spectral lint docs/03-integrate/01-api-specifications/openapi.json

# 2. OpenAPI 3.1 spec validation
docker run --rm -v ${PWD}:/spec redocly/cli lint /spec/docs/03-integrate/01-api-specifications/openapi.json

# 3. Breaking change detection
oasdiff breaking docs/03-integrate/01-api-specifications/openapi.v1.json docs/03-integrate/01-api-specifications/openapi.json
```

**Checklist**:
- [ ] ✅ No linting errors (Spectral/Redocly)
- [ ] ✅ No breaking changes (unless major version bump)
- [ ] ✅ All `$ref` resolve correctly
- [ ] ✅ No unused components

### Manual Review

**Spot Checks**:
```bash
# Check endpoint count
jq '.paths | keys | length' openapi.json
# Expected: Match actual API endpoints

# Check schema count
jq '.components.schemas | keys | length' openapi.json
# Expected: All DTOs/Models defined

# Check security schemes
jq '.components.securitySchemes | keys' openapi.json
# Expected: BearerAuth, OAuth2, etc.
```

**Checklist**:
- [ ] ✅ Endpoint count matches backend routes
- [ ] ✅ Schema count ≥ 80% of backend models
- [ ] ✅ All auth methods documented
- [ ] ✅ Deprecated endpoints marked with `deprecated: true`

---

## Phase 7: E2E Test Readiness

### Test Generation Checklist

**Can Auto-Generate Tests When**:
- [ ] ✅ All endpoints have `operationId`
- [ ] ✅ All parameters have `schema` + `example`
- [ ] ✅ All request bodies have `schema` + `examples`
- [ ] ✅ All responses have `schema` (200, 201, 400, 401, 404, 500)
- [ ] ✅ Security schemes are testable (have auth flow documented)

**Test Generation Command**:
```bash
sdlcctl e2e parse-openapi \
  docs/03-integrate/01-api-specifications/openapi.json \
  --generate-tests \
  --test-output tests/e2e/
```

**Expected Output**:
```
✅ Parsed 58 endpoints
✅ Generated 174 test cases
✅ Coverage: 100% (all endpoints)
✅ Output: tests/e2e/test_*.py
```

---

## Common Quality Issues & Fixes

### Issue 1: Missing Examples

**Problem**:
```yaml
parameters:
  - name: user_id
    in: path
    schema:
      type: string  # ❌ No example
```

**Fix**:
```yaml
parameters:
  - name: user_id
    in: path
    schema:
      type: string
      format: uuid
      example: "550e8400-e29b-41d4-a716-446655440000"  # ✅ Added
```

### Issue 2: Vague Descriptions

**Problem**:
```yaml
summary: Get user  # ❌ Too vague
```

**Fix**:
```yaml
summary: Get user by ID  # ✅ Specific
description: Retrieves detailed user information including profile, role, and metadata.  # ✅ Detailed
```

### Issue 3: Missing Error Responses

**Problem**:
```yaml
responses:
  '200':
    description: Success  # ❌ Only success case
```

**Fix**:
```yaml
responses:
  '200':
    description: User found
    # ...
  '401':
    description: Unauthorized - invalid or missing JWT token
    # ...
  '404':
    description: User not found
    # ...
  '500':
    description: Internal server error
    # ...
```

---

## Quality Score

### Scoring System

| Metric | Weight | Target | Score Calculation |
|--------|--------|--------|-------------------|
| Metadata complete | 10% | 100% | (title + version + description + contact) / 4 |
| Endpoint completeness | 30% | 100% | (endpoints with summary + description + operationId) / total |
| Schema quality | 30% | 100% | (schemas with examples + descriptions) / total |
| Security defined | 15% | 100% | (endpoints with auth) / protected endpoints |
| Examples provided | 15% | 100% | (requests with examples) / total POST/PUT/PATCH |

**Quality Grades**:
- **90-100%**: ✅ **Excellent** - Ready for auto-generation
- **75-89%**: ⚠️ **Good** - Minor improvements needed
- **60-74%**: ⚠️ **Fair** - Significant gaps, manual testing required
- **<60%**: 🔴 **Poor** - Not suitable for E2E testing

**Calculation Tool**:
```bash
sdlcctl e2e parse-openapi \
  docs/03-integrate/01-api-specifications/openapi.json \
  --quality-report
```

---

## Sign-Off

**Checklist Owner**: [Tech Lead / API Architect]
**Review Date**: [YYYY-MM-DD]
**Quality Score**: [X]% ([Grade])
**Status**: [✅ APPROVED | ⚠️ NEEDS IMPROVEMENT | 🔴 REJECTED]

---

**Document Status**: ACTIVE
**Created**: February 2, 2026
**Framework**: SDLC 6.2.1
**RFC**: RFC-SDLC-602-E2E-API-TESTING
**Owner**: Engineering Teams
