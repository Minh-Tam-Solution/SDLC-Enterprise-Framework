# OWASP API Security Top 10 Testing Checklist

**Version**: 1.0.0
**Framework**: SDLC 6.1.0
**Standard**: OWASP API Security Top 10 (2023)
**Last Updated**: February 2026

---

## Overview

This checklist provides comprehensive security testing guidance based on the OWASP API Security Top 10 (2023). Each vulnerability includes test procedures, expected results, and recommended tools.

---

## Quick Reference

| # | Vulnerability | Risk | Priority | Automation |
|---|---------------|------|----------|------------|
| API1 | Broken Object Level Authorization (BOLA) | Critical | P0 | High |
| API2 | Broken Authentication | Critical | P0 | Medium |
| API3 | Broken Object Property Level Authorization | High | P1 | Medium |
| API4 | Unrestricted Resource Consumption | High | P1 | High |
| API5 | Broken Function Level Authorization | Critical | P0 | High |
| API6 | Unrestricted Access to Sensitive Business Flows | High | P1 | Low |
| API7 | Server-Side Request Forgery (SSRF) | High | P1 | Medium |
| API8 | Security Misconfiguration | Medium | P2 | High |
| API9 | Improper Inventory Management | Medium | P2 | High |
| API10 | Unsafe Consumption of APIs | Medium | P2 | Low |

---

## API1:2023 - Broken Object Level Authorization (BOLA/IDOR)

### Description
Attackers can access unauthorized objects by manipulating object IDs in API requests.

### Test Procedures

```yaml
Test Cases:
  1. Horizontal Privilege Escalation:
     - Login as User A
     - Note User A's resource IDs
     - Try accessing User B's resources using User A's token
     - Expected: 403 Forbidden

  2. ID Enumeration:
     - Access /api/v1/users/1
     - Try /api/v1/users/2, /3, etc.
     - Expected: 403 for other users' data

  3. UUID Prediction:
     - If using UUIDs, verify randomness
     - Try sequential patterns (v1 UUIDs leak timestamp)
     - Expected: UUIDv4 or similar non-predictable format

  4. Parameter Tampering:
     - Modify user_id, account_id, order_id in requests
     - Test in query params, body, and path
     - Expected: Authorization check at object level
```

### Test Script Example

```python
def test_bola_horizontal_escalation(api_client, user_a_token, user_b_id):
    """Test BOLA - User A should not access User B's data"""
    headers = {"Authorization": f"Bearer {user_a_token}"}

    # Attempt to access User B's profile
    response = api_client.get(f"/api/v1/users/{user_b_id}", headers=headers)

    assert response.status_code == 403, f"BOLA vulnerability: User A accessed User B's data"
```

### Tools
- Burp Suite (Autorize extension)
- Custom scripts with session swapping
- OWASP ZAP with active scan

### Expected Results
- [ ] 403 Forbidden for unauthorized object access
- [ ] Consistent authorization across all endpoints
- [ ] No data leakage in error messages

---

## API2:2023 - Broken Authentication

### Description
Weak authentication mechanisms allow attackers to compromise user accounts.

### Test Procedures

```yaml
Test Cases:
  1. JWT Weakness Testing:
     - Check for algorithm confusion (alg: none)
     - Test weak signing keys
     - Verify token expiration enforcement
     - Test token after logout (should be invalidated)

  2. Brute Force Protection:
     - Attempt multiple failed logins
     - Expected: Account lockout or rate limiting after 5-10 attempts

  3. Password Policy:
     - Test weak passwords (123456, password)
     - Expected: Rejection with clear error message

  4. Token Handling:
     - Test expired tokens
     - Test tampered tokens (modify payload)
     - Test token reuse after refresh
     - Expected: 401 Unauthorized

  5. Session Management:
     - Test session fixation
     - Verify secure cookie flags (HttpOnly, Secure, SameSite)
     - Test concurrent session limits
```

### Test Script Example

```python
def test_jwt_algorithm_none(api_client):
    """Test JWT algorithm confusion vulnerability"""
    # Create token with alg: none
    fake_token = base64.b64encode('{"alg":"none","typ":"JWT"}'.encode()).decode()
    fake_payload = base64.b64encode('{"user_id":"admin"}'.encode()).decode()
    malicious_jwt = f"{fake_token}.{fake_payload}."

    response = api_client.get("/api/v1/users/me",
                               headers={"Authorization": f"Bearer {malicious_jwt}"})

    assert response.status_code == 401, "JWT algorithm confusion vulnerability detected"

def test_token_after_logout(api_client, valid_token):
    """Test that tokens are invalidated after logout"""
    # Logout
    api_client.post("/api/v1/auth/logout",
                    headers={"Authorization": f"Bearer {valid_token}"})

    # Try to use the same token
    response = api_client.get("/api/v1/users/me",
                               headers={"Authorization": f"Bearer {valid_token}"})

    assert response.status_code == 401, "Token still valid after logout"
```

### Tools
- jwt_tool
- Burp Suite JWT plugin
- Hydra (brute force testing)

### Expected Results
- [ ] Strong JWT implementation (RS256 or ES256)
- [ ] Token invalidation on logout
- [ ] Rate limiting on login endpoint
- [ ] Secure cookie configuration

---

## API3:2023 - Broken Object Property Level Authorization

### Description
API exposes object properties that should be restricted based on user permissions.

### Test Procedures

```yaml
Test Cases:
  1. Mass Assignment:
     - Send extra fields in request body
     - Try: {"name": "test", "role": "admin", "is_verified": true}
     - Expected: Extra fields ignored or rejected

  2. Excessive Data Exposure:
     - Check response for sensitive fields
     - Look for: password_hash, internal_id, credit_card
     - Expected: Only necessary fields returned

  3. Field-Level Authorization:
     - Regular user requests admin-only fields
     - Expected: Fields filtered or 403

  4. Response Filtering:
     - Compare responses for different user roles
     - Expected: Sensitive fields hidden for lower roles
```

### Test Script Example

```python
def test_mass_assignment(api_client, user_token):
    """Test mass assignment vulnerability"""
    response = api_client.put("/api/v1/users/me",
        headers={"Authorization": f"Bearer {user_token}"},
        json={
            "name": "Updated Name",
            "role": "admin",  # Should not be assignable
            "is_verified": True  # Should not be assignable
        })

    # Verify role wasn't changed
    user = api_client.get("/api/v1/users/me",
                          headers={"Authorization": f"Bearer {user_token}"}).json()

    assert user["role"] != "admin", "Mass assignment vulnerability: role was changed"

def test_excessive_data_exposure(api_client, user_token):
    """Test for sensitive data in responses"""
    response = api_client.get("/api/v1/users/me",
                               headers={"Authorization": f"Bearer {user_token}"})

    sensitive_fields = ["password", "password_hash", "secret_key", "credit_card"]
    response_fields = response.json().keys()

    for field in sensitive_fields:
        assert field not in response_fields, f"Sensitive field exposed: {field}"
```

### Tools
- Burp Suite (response comparison)
- Custom field enumeration scripts

### Expected Results
- [ ] Mass assignment protection enabled
- [ ] No sensitive fields in responses
- [ ] Field-level filtering by role

---

## API4:2023 - Unrestricted Resource Consumption

### Description
API doesn't properly limit resource consumption, enabling DoS attacks.

### Test Procedures

```yaml
Test Cases:
  1. Rate Limiting:
     - Send 100+ requests in 1 minute
     - Expected: 429 Too Many Requests after threshold

  2. Payload Size:
     - Send 10MB+ request body
     - Expected: 413 Payload Too Large

  3. Pagination Limits:
     - Request ?limit=10000
     - Expected: Capped at reasonable maximum (e.g., 100)

  4. Query Complexity (GraphQL):
     - Send deeply nested queries
     - Expected: Complexity limit enforced

  5. File Upload Limits:
     - Upload oversized files
     - Expected: Size limit enforced
```

### Test Script Example

```python
import time
import concurrent.futures

def test_rate_limiting(api_client, user_token):
    """Test rate limiting is enforced"""
    headers = {"Authorization": f"Bearer {user_token}"}
    responses = []

    # Send 100 requests rapidly
    for _ in range(100):
        response = api_client.get("/api/v1/projects", headers=headers)
        responses.append(response.status_code)

    rate_limited = responses.count(429)
    assert rate_limited > 0, "No rate limiting detected after 100 requests"

def test_pagination_limit(api_client, user_token):
    """Test pagination limits are enforced"""
    response = api_client.get("/api/v1/projects?limit=10000",
                               headers={"Authorization": f"Bearer {user_token}"})

    data = response.json()
    assert len(data["data"]) <= 100, f"Pagination limit not enforced: {len(data['data'])} items returned"
```

### Tools
- Locust (load testing)
- Custom rate limit testing scripts
- Burp Suite Intruder

### Expected Results
- [ ] Rate limiting: 429 after threshold
- [ ] Payload size limits enforced
- [ ] Pagination capped at reasonable maximum
- [ ] GraphQL complexity limits (if applicable)

---

## API5:2023 - Broken Function Level Authorization

### Description
Users can access admin or privileged functions without proper authorization.

### Test Procedures

```yaml
Test Cases:
  1. Admin Endpoint Access:
     - Regular user calls /api/v1/admin/*
     - Expected: 403 Forbidden

  2. HTTP Method Tampering:
     - GET allowed, try DELETE on same resource
     - Expected: 403 if not authorized

  3. Role Escalation:
     - Call user management endpoints as regular user
     - Expected: 403 Forbidden

  4. Hidden Endpoints:
     - Enumerate /api/v1/internal/*, /api/v1/debug/*
     - Expected: 404 or 403, not 200
```

### Test Script Example

```python
def test_admin_endpoint_access(api_client, regular_user_token):
    """Test regular user cannot access admin endpoints"""
    admin_endpoints = [
        "/api/v1/admin/users",
        "/api/v1/admin/settings",
        "/api/v1/admin/audit-logs",
        "/api/v1/users",  # List all users
    ]

    headers = {"Authorization": f"Bearer {regular_user_token}"}

    for endpoint in admin_endpoints:
        response = api_client.get(endpoint, headers=headers)
        assert response.status_code in [403, 404], \
            f"Admin endpoint accessible: {endpoint} returned {response.status_code}"

def test_method_tampering(api_client, user_token):
    """Test HTTP method tampering"""
    headers = {"Authorization": f"Bearer {user_token}"}

    # User should be able to GET their profile
    get_response = api_client.get("/api/v1/users/me", headers=headers)
    assert get_response.status_code == 200

    # But not DELETE another user
    delete_response = api_client.delete("/api/v1/users/other-user-id", headers=headers)
    assert delete_response.status_code in [403, 404]
```

### Tools
- Burp Suite (permission matrix)
- Custom endpoint enumeration
- OWASP ZAP

### Expected Results
- [ ] Admin endpoints return 403 for regular users
- [ ] HTTP method authorization enforced
- [ ] No hidden accessible endpoints

---

## API6:2023 - Unrestricted Access to Sensitive Business Flows

### Description
Attackers can abuse business logic through automation (scraping, mass operations).

### Test Procedures

```yaml
Test Cases:
  1. Mass Creation:
     - Automate account creation (100+ accounts)
     - Expected: CAPTCHA or rate limit after threshold

  2. Enumeration:
     - Enumerate valid usernames/emails
     - Expected: Generic error messages

  3. Business Logic Abuse:
     - Repeat discount code usage
     - Mass ticket/reservation booking
     - Expected: Business rules enforced

  4. Automation Detection:
     - Send requests without typical browser headers
     - Expected: Bot detection or CAPTCHA
```

### Test Script Example

```python
def test_mass_account_creation(api_client):
    """Test protection against mass account creation"""
    created_count = 0
    blocked = False

    for i in range(50):
        response = api_client.post("/api/v1/auth/register", json={
            "email": f"masstest{i}@example.com",
            "password": "Test123!@#",
            "name": f"Mass Test {i}"
        })

        if response.status_code == 429:
            blocked = True
            break
        elif response.status_code == 201:
            created_count += 1

    assert blocked or created_count < 20, \
        f"Mass account creation not limited: {created_count} accounts created"

def test_username_enumeration(api_client):
    """Test for username enumeration"""
    # Test with existing user
    response1 = api_client.post("/api/v1/auth/login", json={
        "email": "existing@example.com",
        "password": "wrongpassword"
    })

    # Test with non-existing user
    response2 = api_client.post("/api/v1/auth/login", json={
        "email": "nonexistent@example.com",
        "password": "wrongpassword"
    })

    # Error messages should be identical
    assert response1.json().get("error") == response2.json().get("error"), \
        "Username enumeration possible through different error messages"
```

### Tools
- Custom automation scripts
- Selenium/Playwright for CAPTCHA testing

### Expected Results
- [ ] Rate limiting on sensitive operations
- [ ] CAPTCHA after suspicious activity
- [ ] Generic error messages (no enumeration)

---

## API7:2023 - Server-Side Request Forgery (SSRF)

### Description
API can be tricked into making requests to unintended internal/external resources.

### Test Procedures

```yaml
Test Cases:
  1. Internal Network Access:
     - URL parameter: http://localhost:8080/admin
     - URL parameter: http://169.254.169.254/ (AWS metadata)
     - Expected: Blocked or validated

  2. Protocol Smuggling:
     - file:///etc/passwd
     - gopher://internal-service
     - Expected: Only http/https allowed

  3. Redirect Following:
     - URL that redirects to internal service
     - Expected: Redirect validation or blocking

  4. DNS Rebinding:
     - Domain that resolves to internal IP
     - Expected: IP validation after DNS resolution
```

### Test Script Example

```python
def test_ssrf_localhost(api_client, user_token):
    """Test SSRF protection against localhost"""
    ssrf_payloads = [
        "http://localhost/admin",
        "http://127.0.0.1/admin",
        "http://[::1]/admin",
        "http://0.0.0.0/admin",
        "http://localhost:8080",
    ]

    headers = {"Authorization": f"Bearer {user_token}"}

    for payload in ssrf_payloads:
        response = api_client.post("/api/v1/webhooks/test", headers=headers,
                                    json={"url": payload})

        assert response.status_code in [400, 403], \
            f"SSRF vulnerability: {payload} was not blocked"

def test_ssrf_cloud_metadata(api_client, user_token):
    """Test SSRF protection against cloud metadata endpoints"""
    metadata_urls = [
        "http://169.254.169.254/latest/meta-data/",  # AWS
        "http://metadata.google.internal/",  # GCP
        "http://169.254.169.254/metadata/instance",  # Azure
    ]

    headers = {"Authorization": f"Bearer {user_token}"}

    for url in metadata_urls:
        response = api_client.post("/api/v1/webhooks/test", headers=headers,
                                    json={"url": url})

        assert response.status_code in [400, 403], \
            f"SSRF vulnerability: Cloud metadata URL not blocked: {url}"
```

### Tools
- Burp Collaborator
- SSRFmap
- Custom URL validation scripts

### Expected Results
- [ ] Internal URLs blocked
- [ ] Cloud metadata endpoints blocked
- [ ] Only http/https schemes allowed
- [ ] Redirect validation enabled

---

## API8:2023 - Security Misconfiguration

### Description
Insecure default configurations, verbose errors, or missing security headers.

### Test Procedures

```yaml
Test Cases:
  1. Debug Mode:
     - Check for stack traces in errors
     - Look for debug endpoints (/debug, /swagger in production)
     - Expected: Generic errors, no debug info

  2. Security Headers:
     - Check response headers
     - Expected: HSTS, CSP, X-Content-Type-Options, etc.

  3. CORS Configuration:
     - Test with Origin: https://evil.com
     - Expected: Not reflected or restricted

  4. Default Credentials:
     - Try admin/admin, root/root
     - Expected: Not working

  5. TLS Configuration:
     - Check for TLS 1.2+ only
     - Verify certificate validity
```

### Test Script Example

```python
def test_security_headers(api_client):
    """Test security headers are present"""
    response = api_client.get("/api/v1/health")

    required_headers = {
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": ["DENY", "SAMEORIGIN"],
        "Strict-Transport-Security": None,  # Just check presence
    }

    for header, expected in required_headers.items():
        actual = response.headers.get(header)
        assert actual is not None, f"Missing security header: {header}"
        if expected and isinstance(expected, list):
            assert actual in expected, f"Invalid {header}: {actual}"
        elif expected:
            assert actual == expected, f"Invalid {header}: {actual}"

def test_cors_configuration(api_client):
    """Test CORS is properly configured"""
    response = api_client.options("/api/v1/users",
        headers={"Origin": "https://evil.com"})

    allowed_origin = response.headers.get("Access-Control-Allow-Origin")

    assert allowed_origin != "*", "CORS allows all origins"
    assert allowed_origin != "https://evil.com", "CORS reflects arbitrary origin"

def test_no_debug_info(api_client, user_token):
    """Test no debug information in errors"""
    # Trigger an error
    response = api_client.get("/api/v1/users/invalid-id-format",
                               headers={"Authorization": f"Bearer {user_token}"})

    response_text = response.text.lower()
    debug_indicators = ["traceback", "stack trace", "line ", "file ", "exception"]

    for indicator in debug_indicators:
        assert indicator not in response_text, \
            f"Debug information leaked: found '{indicator}'"
```

### Tools
- SecurityHeaders.com
- SSL Labs
- Burp Suite

### Expected Results
- [ ] All security headers present
- [ ] CORS properly restricted
- [ ] No debug information in errors
- [ ] TLS 1.2+ only

---

## API9:2023 - Improper Inventory Management

### Description
Outdated API versions or undocumented endpoints remain accessible.

### Test Procedures

```yaml
Test Cases:
  1. Old API Versions:
     - Try /api/v0/, /api/v1-beta/
     - Expected: 404 or properly deprecated

  2. Undocumented Endpoints:
     - Enumerate common paths (/admin, /internal, /debug)
     - Compare OpenAPI spec vs actual endpoints
     - Expected: All endpoints documented

  3. Shadow APIs:
     - Check for test/staging endpoints in production
     - Expected: Not accessible

  4. Deprecated Endpoints:
     - Check if deprecated endpoints return warnings
     - Expected: Deprecation headers or errors
```

### Test Script Example

```python
def test_old_api_versions(api_client):
    """Test old API versions are not accessible"""
    old_versions = ["/api/v0/", "/api/v1-beta/", "/api/v1-old/", "/api/"]

    for version in old_versions:
        response = api_client.get(f"{version}users")

        assert response.status_code == 404, \
            f"Old API version accessible: {version}"

def test_undocumented_endpoints(api_client, openapi_spec):
    """Test no undocumented endpoints exist"""
    documented_paths = set(openapi_spec["paths"].keys())

    # Common undocumented endpoints to check
    common_paths = [
        "/api/v1/admin", "/api/v1/debug", "/api/v1/internal",
        "/api/v1/test", "/api/v1/swagger", "/api/v1/docs",
        "/api/v1/metrics", "/api/v1/health/detailed"
    ]

    for path in common_paths:
        if path not in documented_paths:
            response = api_client.get(path)
            assert response.status_code in [401, 403, 404], \
                f"Undocumented endpoint accessible: {path} returned {response.status_code}"
```

### Tools
- Swagger diff tools
- Endpoint enumeration (ffuf, gobuster)
- API documentation comparison

### Expected Results
- [ ] Only current API version accessible
- [ ] All endpoints documented
- [ ] No test/debug endpoints in production

---

## API10:2023 - Unsafe Consumption of APIs

### Description
Insufficient validation of data from third-party APIs.

### Test Procedures

```yaml
Test Cases:
  1. Third-Party Response Validation:
     - Mock malicious responses from external APIs
     - Include SQL injection, XSS payloads
     - Expected: Payloads sanitized/escaped

  2. Trust Boundaries:
     - Test assumptions about external data
     - Expected: All external data validated

  3. Error Handling:
     - External API returns unexpected data types
     - Expected: Graceful handling, no crashes

  4. Timeout Handling:
     - External API times out
     - Expected: Proper timeout, no hanging
```

### Test Script Example

```python
def test_external_api_injection(api_client, user_token, mock_external_api):
    """Test sanitization of external API data"""
    # Configure mock to return malicious data
    mock_external_api.return_value = {
        "name": "<script>alert('xss')</script>",
        "description": "'; DROP TABLE users; --"
    }

    response = api_client.post("/api/v1/import/external",
                                headers={"Authorization": f"Bearer {user_token}"},
                                json={"source": "external-api"})

    # Check the response doesn't reflect raw malicious content
    assert "<script>" not in response.text
    assert "DROP TABLE" not in response.text

def test_external_api_timeout(api_client, user_token, mock_slow_api):
    """Test timeout handling for external APIs"""
    mock_slow_api.delay = 30  # 30 second delay

    start_time = time.time()
    response = api_client.post("/api/v1/import/external",
                                headers={"Authorization": f"Bearer {user_token}"},
                                json={"source": "slow-api"},
                                timeout=10)
    elapsed = time.time() - start_time

    # Should timeout within reasonable time, not hang for 30s
    assert elapsed < 15, "API didn't timeout properly for slow external service"
```

### Tools
- Mock servers (WireMock)
- Custom fuzzing scripts

### Expected Results
- [ ] External data validated/sanitized
- [ ] Proper timeout handling
- [ ] Graceful error handling

---

## Integration with E2E Testing

### Security Testing Modes

The `e2e-api-testing` skill supports these security testing modes:

```yaml
Security Modes:
  --security-mode idor:
    Tests: API1 (BOLA) - Object ID manipulation

  --security-mode auth:
    Tests: API2 (Authentication) - Token handling, session management

  --security-mode injection:
    Tests: SQL injection, Command injection (related to API7)

  --security-mode graphql:
    Tests: GraphQL-specific vulnerabilities

  --security-mode bypass:
    Tests: API5 (Function Authorization) - 403/401 bypass attempts
```

### Combined Workflow

```bash
# Run functional E2E tests
e2e-api-testing --project . --mode functional

# Run security tests (all OWASP Top 10)
e2e-api-testing --project . --mode security --owasp-all

# Run specific security mode
e2e-api-testing --project . --mode security --security-mode idor
```

---

## Report Template

### Security Testing Report

```markdown
# API Security Testing Report

**Date**: {DATE}
**Project**: {PROJECT}
**Standard**: OWASP API Security Top 10 (2023)
**Tester**: {NAME}

## Executive Summary

| Vulnerability | Status | Severity | Findings |
|---------------|--------|----------|----------|
| API1: BOLA | PASS | Critical | 0 issues |
| API2: Broken Auth | PASS | Critical | 0 issues |
| API3: Property Auth | PASS | High | 0 issues |
| API4: Resource Consumption | WARN | High | 1 issue |
| API5: Function Auth | PASS | Critical | 0 issues |
| API6: Business Flow | PASS | High | 0 issues |
| API7: SSRF | PASS | High | 0 issues |
| API8: Misconfiguration | PASS | Medium | 0 issues |
| API9: Inventory | PASS | Medium | 0 issues |
| API10: Unsafe Consumption | N/A | Medium | Not tested |

## Detailed Findings

### API4: Unrestricted Resource Consumption

**Finding**: Rate limiting threshold too high (1000 req/min)
**Severity**: Medium
**Recommendation**: Reduce to 100 req/min for sensitive endpoints
**Status**: Open

## Recommendations

1. Implement rate limiting on all endpoints
2. Add CAPTCHA for sensitive operations
3. Review and update security headers
```

---

## References

- [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x00-header/)
- [E2E API Testing Workflow](./testing_e2e-api-testing-workflow.md)
- [RFC-SDLC-602](../../../09-Continuous-Improvement/RFC/RFC-SDLC-602-E2E-API-TESTING.md)
