# Complete API Endpoint Reference Template

**Version**: 1.0.0
**Framework**: SDLC 6.3.0
**Stage**: 03-integrate
**Last Updated**: February 2026

---

## Instructions

This template defines the standard structure for API documentation in SDLC Framework projects. Copy this template to `docs/03-integrate/01-api-specifications/COMPLETE-API-ENDPOINT-REFERENCE.md`.

---

# Complete API Endpoint Reference

**Project**: {PROJECT_NAME}
**API Version**: v1
**Base URL**: `{BASE_URL}/api/v1`
**Last Updated**: {DATE}
**OpenAPI Spec**: [openapi.json](./openapi.json)

---

## Summary

| Category | Count | Coverage | Test Status | Test Report |
|----------|-------|----------|-------------|-------------|
| Authentication | {N} | {%} | {PASS/FAIL} | [Link](#) |
| Users | {N} | {%} | {PASS/FAIL} | [Link](#) |
| Projects | {N} | {%} | {PASS/FAIL} | [Link](#) |
| Resources | {N} | {%} | {PASS/FAIL} | [Link](#) |
| **Total** | **{TOTAL}** | **{AVG}%** | **{RATE}%** | [Latest Report](../../05-test/03-e2e-testing/reports/) |

---

## Authentication

All endpoints require authentication unless marked as `Public`.

| Method | Header | Format |
|--------|--------|--------|
| Bearer Token | `Authorization` | `Bearer {token}` |
| API Key | `X-API-Key` | `{api_key}` |

### Rate Limits

| Tier | Requests/min | Requests/day |
|------|-------------|--------------|
| Free | 60 | 1,000 |
| Pro | 300 | 10,000 |
| Enterprise | Unlimited | Unlimited |

---

## Endpoints by Category

### 1. Authentication

| # | Method | Endpoint | Auth | Description | Test Status | Last Tested |
|---|--------|----------|------|-------------|-------------|-------------|
| 1 | POST | `/auth/login` | Public | User login | PASS | {DATE} |
| 2 | POST | `/auth/register` | Public | User registration | PASS | {DATE} |
| 3 | POST | `/auth/refresh` | Bearer | Refresh token | PASS | {DATE} |
| 4 | POST | `/auth/logout` | Bearer | User logout | PASS | {DATE} |
| 5 | POST | `/auth/forgot-password` | Public | Request password reset | PASS | {DATE} |

### 2. Users

| # | Method | Endpoint | Auth | Description | Test Status | Last Tested |
|---|--------|----------|------|-------------|-------------|-------------|
| 1 | GET | `/users/me` | Bearer | Get current user | PASS | {DATE} |
| 2 | PUT | `/users/me` | Bearer | Update current user | PASS | {DATE} |
| 3 | GET | `/users/{id}` | Bearer | Get user by ID | PASS | {DATE} |
| 4 | GET | `/users` | Admin | List all users | PASS | {DATE} |

### 3. Projects

| # | Method | Endpoint | Auth | Description | Test Status | Last Tested |
|---|--------|----------|------|-------------|-------------|-------------|
| 1 | GET | `/projects` | Bearer | List projects | PASS | {DATE} |
| 2 | POST | `/projects` | Bearer | Create project | PASS | {DATE} |
| 3 | GET | `/projects/{id}` | Bearer | Get project | PASS | {DATE} |
| 4 | PUT | `/projects/{id}` | Bearer | Update project | PASS | {DATE} |
| 5 | DELETE | `/projects/{id}` | Bearer | Delete project | PASS | {DATE} |

---

## Detailed Endpoints

### Authentication

#### POST /api/v1/auth/login

**Description**: Authenticate user and receive access token.

**Authentication**: Public (no auth required)

**Request Schema**:
```json
{
  "email": "string (required, email format)",
  "password": "string (required, min 8 chars)"
}
```

**Response Schema** (200 OK):
```json
{
  "access_token": "string (JWT)",
  "refresh_token": "string",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Error Responses**:
| Code | Description | Body |
|------|-------------|------|
| 400 | Invalid request | `{"error": "validation_error", "details": [...]}` |
| 401 | Invalid credentials | `{"error": "invalid_credentials"}` |
| 429 | Rate limited | `{"error": "rate_limited", "retry_after": 60}` |

**Example Request**:
```bash
curl -X POST "{BASE_URL}/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePass123!"
  }'
```

**Example Response** (from E2E test):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "refresh_token": "dGhpcyBpcyBhIHJlZnJl...",
  "token_type": "Bearer",
  "expires_in": 3600
}
```

**Validation Rules**:
- Email: Valid email format, max 255 chars
- Password: Min 8 chars, must contain uppercase, lowercase, number

**Test Report**: [E2E Report - Authentication](../../05-test/03-e2e-testing/reports/E2E-API-REPORT-{DATE}.md#authentication)

**Test Status**: PASS | **Last Tested**: {DATE}

---

#### POST /api/v1/auth/register

**Description**: Register a new user account.

**Authentication**: Public

**Request Schema**:
```json
{
  "email": "string (required, email format)",
  "password": "string (required, min 8 chars)",
  "name": "string (required, 2-100 chars)"
}
```

**Response Schema** (201 Created):
```json
{
  "id": "string (UUID)",
  "email": "string",
  "name": "string",
  "created_at": "string (ISO 8601)"
}
```

**Example Request**:
```bash
curl -X POST "{BASE_URL}/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newuser@example.com",
    "password": "SecurePass123!",
    "name": "New User"
  }'
```

**Test Status**: PASS | **Last Tested**: {DATE}

---

### Users

#### GET /api/v1/users/me

**Description**: Get currently authenticated user's profile.

**Authentication**: Bearer Token (required)

**Request**: No body required

**Response Schema** (200 OK):
```json
{
  "id": "string (UUID)",
  "email": "string",
  "name": "string",
  "avatar_url": "string | null",
  "role": "string (enum: user, admin)",
  "created_at": "string (ISO 8601)",
  "updated_at": "string (ISO 8601)"
}
```

**Example Request**:
```bash
curl -X GET "{BASE_URL}/api/v1/users/me" \
  -H "Authorization: Bearer {token}"
```

**Test Status**: PASS | **Last Tested**: {DATE}

---

### Projects

#### GET /api/v1/projects

**Description**: List all projects accessible to the current user.

**Authentication**: Bearer Token (required)

**Query Parameters**:
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number |
| limit | integer | No | 20 | Items per page (max 100) |
| sort | string | No | created_at | Sort field |
| order | string | No | desc | Sort order (asc/desc) |
| status | string | No | all | Filter by status |

**Response Schema** (200 OK):
```json
{
  "data": [
    {
      "id": "string (UUID)",
      "name": "string",
      "description": "string | null",
      "status": "string (enum: active, archived)",
      "created_at": "string (ISO 8601)"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 100,
    "pages": 5
  }
}
```

**Example Request**:
```bash
curl -X GET "{BASE_URL}/api/v1/projects?page=1&limit=20" \
  -H "Authorization: Bearer {token}"
```

**Test Status**: PASS | **Last Tested**: {DATE}

---

#### POST /api/v1/projects

**Description**: Create a new project.

**Authentication**: Bearer Token (required)

**Request Schema**:
```json
{
  "name": "string (required, 3-100 chars)",
  "description": "string (optional, max 1000 chars)",
  "tier": "string (enum: LITE, STANDARD, PROFESSIONAL, ENTERPRISE)"
}
```

**Response Schema** (201 Created):
```json
{
  "id": "string (UUID)",
  "name": "string",
  "description": "string | null",
  "tier": "string",
  "status": "active",
  "created_at": "string (ISO 8601)",
  "created_by": "string (UUID)"
}
```

**Validation Rules**:
- Name: 3-100 characters, alphanumeric with spaces/hyphens
- Tier: Must be valid enum value

**Test Status**: PASS | **Last Tested**: {DATE}

---

## Cross-Reference Links

### Stage 05 - Testing & Quality
- [E2E Test Reports](../../05-test/03-e2e-testing/reports/)
- [Security Testing Results](../../05-test/05-Security-Testing/)
- [Integration Test Results](../../05-test/04-integration-testing/)

### Stage 03 - Integration & APIs
- [OpenAPI Specification](./openapi.json) (SSOT)
- [API Design Decisions](./API-Design-Decisions.md)
- [Integration Guides](../03-Integration-Guides/)

---

## Changelog

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| {DATE} | 1.0.0 | Initial API documentation | {AUTHOR} |
| {DATE} | 1.0.1 | Added E2E test status | {AUTHOR} |

---

## Appendix

### HTTP Status Codes

| Code | Meaning | When Used |
|------|---------|-----------|
| 200 | OK | Successful GET, PUT |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Missing/invalid auth |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 429 | Too Many Requests | Rate limited |
| 500 | Internal Server Error | Server error |

### Common Error Format

```json
{
  "error": "error_code",
  "message": "Human readable message",
  "details": [
    {
      "field": "email",
      "message": "Invalid email format"
    }
  ],
  "request_id": "req_abc123"
}
```
