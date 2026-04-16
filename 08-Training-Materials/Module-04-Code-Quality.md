---
document_id: "TRAINING-MODULE-04"
title: "Module 04: Code Quality Standards"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "4 hours (7 parts)"
audience: "All team members — developers, pod leads, architects, product managers"
prerequisite: "Module 01-03 (SDLC Overview, Six Pillars, Zero Mock Policy)"
format: "Lecture + Live Demo + Hands-on Exercises"
---

# Module 04: Code Quality Standards

> **Core principle**: "80% coverage is the floor, not the ceiling." Quality is not optional — it is the baseline that enables everything else.

---

## 1. Quality Standards Overview (20 minutes)

SDLC 6.3.0 defines strict quality standards to ensure production-ready, scalable software.

### Core Metrics

| Category | Metric | Minimum | Target |
|----------|--------|---------|--------|
| **Test Coverage** | Unit Tests | 80% | 90% |
| | Integration Tests | 70% | 85% |
| | E2E Tests | 60% | 75% |
| **Performance** | API Response (p50) | <50ms | <30ms |
| | API Response (p95) | <100ms | <50ms |
| | Uptime | 99.9% | 99.95% |
| **Code Quality** | Quality Score | 95%+ | 98%+ |
| | Mock Instances | 0 | 0 |
| | Technical Debt | Zero tolerance | Zero tolerance |

---

## 2. Test Coverage Standards (45 minutes)

### Unit Tests (minimum 80%)

```
Definition:
  Tests individual functions and methods in isolation
  Fast execution (<1 second per test)

Requirements:
  Every public function must have tests
  Edge cases must be covered
  Error conditions must be tested

Example:
  Function: calculate_bhxh(salary)
  Tests required:
    test_normal_salary()
    test_minimum_wage()
    test_maximum_contribution_cap()
    test_negative_salary_raises_error()
    test_decimal_precision()
```

### Integration Tests (minimum 70%)

```
Definition:
  Tests multiple components working together
  Uses real database connections (not mocks)

Requirements:
  All API endpoints must have tests
  Database operations verified end-to-end
  Authentication flows tested
  Error handling verified

Example:
  Endpoint: POST /api/users
  Tests required:
    test_create_user_success()
    test_create_user_duplicate_email()
    test_create_user_invalid_data()
    test_create_user_unauthorized()
```

### E2E Tests (minimum 60%)

```
Definition:
  Tests complete user workflows through real browser/client

Requirements:
  Critical user flows covered
  Responsive design verified
  Performance acceptable

Example:
  Flow: User Registration
  Tests required:
    test_register_with_valid_data()
    test_register_duplicate_prevention()
    test_register_email_verification()
```

---

## 3. Code File Naming Standards (30 minutes)

### Python Files

```
Format:    snake_case
Max:       50 characters
Extension: .py

Correct:                        Incorrect:
  user_service.py                 UserService.py (PascalCase)
  invoice_repository.py           user-service.py (kebab-case)
  bhxh_calculator.py              userservice.py (no separator)
  authentication_middleware.py
```

### TypeScript Files

```
Format:    camelCase
Max:       50 characters
Extension: .ts

Correct:                        Incorrect:
  arService.ts                    ArService.ts (PascalCase)
  paymentSlice.ts                 ar_service.ts (snake_case)
  useAuthHook.ts                  ar-service.ts (kebab-case)
  invoiceApi.ts
```

### React Components

```
Format:    PascalCase
Max:       50 characters
Extension: .tsx

Correct:                        Incorrect:
  ARDashboard.tsx                 arDashboard.tsx (camelCase)
  InvoiceList.tsx                 ar_dashboard.tsx (snake_case)
  UserProfile.tsx                 ar-dashboard.tsx (kebab-case)
  PaymentForm.tsx
```

### Documentation Files

```
Format:    kebab-case
No version in filename
Extension: .md

Correct:                        Incorrect:
  api-design-guide.md             ApiDesignGuide.md
  user-authentication.md          api_design_guide.md
  deployment-guide.md             API-Design-Guide-V1.0.md
```

---

## 4. Code Style Standards (30 minutes)

### Python (PEP 8)

```
Line length:   Max 100 characters
Indentation:   4 spaces
Quotes:        Double quotes for strings
Imports:       Sorted, grouped by type
Tools:         black (formatter), flake8 (linter), isort (import sorter)
```

### TypeScript (ESLint + Prettier)

```
Line length:   Max 100 characters
Indentation:   2 spaces
Quotes:        Single quotes
Semicolons:    Required
Tools:         eslint (linter), prettier (formatter)
```

### Comment Standards (English Only)

```python
# CORRECT: Explain WHY, not WHAT
# Apply 17.5% employer BHXH rate per Vietnamese labor law
employer_bhxh = salary * Decimal("0.175")

# INCORRECT: Explains obvious WHAT
# Multiply salary by 0.175
employer_bhxh = salary * Decimal("0.175")
```

### Docstring Standard

```python
def calculate_vat(amount: Decimal, rate: Decimal = Decimal("0.10")) -> Decimal:
    """
    Calculate VAT for Vietnamese tax system.

    Args:
        amount: Base amount in VND
        rate: VAT rate (default 10%)

    Returns:
        VAT amount in VND

    Raises:
        ValueError: If amount is negative
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return amount * rate
```

---

## 5. Performance Standards (30 minutes)

### API Response Time Targets

| Percentile | Target | Alert Threshold |
|-----------|--------|-----------------|
| p50 (median) | <50ms | >100ms |
| p95 | <100ms | >200ms |
| p99 | <200ms | >500ms |

### Database Query Performance

```
Simple queries:  <10ms
Complex queries:  <50ms
Reports:          <500ms

Best practices:
  - Use indexes appropriately
  - Avoid N+1 queries (use eager loading)
  - Limit result sets
  - Use connection pooling
```

### Frontend Performance

```
First Contentful Paint:  <1.5s
Time to Interactive:     <3s
Main bundle size:        <500KB

Optimization techniques:
  - Code splitting (lazy loading)
  - Image optimization
  - Tree shaking
  - Caching strategies
```

---

## 6. Security Standards (30 minutes)

### OWASP Top 10 Compliance

| # | Vulnerability | Mitigation |
|---|--------------|------------|
| 1 | Injection | Parameterized queries, never concatenate SQL |
| 2 | Broken Authentication | JWT RS256, secure token storage, MFA |
| 3 | Sensitive Data Exposure | Encrypt at rest and in transit (TLS), mask in logs |
| 4 | XXE | Disable XML external entities, prefer JSON |
| 5 | Broken Access Control | RBAC, tenant isolation, resource-level permissions |

### Input Validation

```python
from pydantic import BaseModel, validator

class UserInput(BaseModel):
    name: str
    phone: str
    email: str

    @validator("phone")
    def validate_phone(cls, v):
        # Vietnamese phone: 10 digits, starts with 0
        if not re.match(r"^0\d{9}$", v):
            raise ValueError("Invalid Vietnamese phone number")
        return v
```

### Authentication Standards

```
JWT Algorithm:        RS256
Access Token TTL:     15 minutes
Refresh Token TTL:    7 days
Storage:              HTTPOnly cookies
Password minimum:     8 characters (upper, lower, number, special)
Password hashing:     bcrypt with salt
```

---

## 7. Hands-on Exercises (55 minutes)

### Exercise 1: Code Review Checklist (25 minutes)

Review the following code against the SDLC 6.3.0 quality checklist and identify all violations:

```python
# file: UserService.py

import json

fake_db = {}

def CreateUser(name, phone, salary):
    # tao user moi
    user = {"name": name, "phone": phone, "salary": salary}
    fake_db[len(fake_db)] = user
    bhxh = salary * 0.175
    return user

def getUser(id):
    return fake_db.get(id, None)
```

### Exercise 1 Answers

| # | Violation | Standard |
|---|-----------|----------|
| 1 | `UserService.py` — PascalCase filename | Python files must be snake_case: `user_service.py` |
| 2 | `fake_db = {}` — in-memory mock database | Zero Mock Policy: use real database |
| 3 | `CreateUser` — PascalCase function name | Python functions must be snake_case: `create_user` |
| 4 | `# tao user moi` — Vietnamese comment | Comments must be in English only |
| 5 | `salary * 0.175` — magic number, float | Use `Decimal("0.175")` with named constant |
| 6 | `getUser` — camelCase function name | Python functions must be snake_case: `get_user` |
| 7 | No type hints | Type hints required for public functions |
| 8 | No docstrings | Docstrings required for public functions |
| 9 | No input validation | Phone, salary need validation |
| 10 | No tests | Every public function must have tests |

### Exercise 2: Fix the Code (30 minutes)

Rewrite the code from Exercise 1 to be fully SDLC 6.3.0 compliant.

**Expected structure:**
```python
# file: user_service.py

from decimal import Decimal
from sqlalchemy.orm import Session

BHXH_EMPLOYER_RATE = Decimal("0.175")  # 17.5% per Vietnamese labor law

async def create_user(
    db: Session, name: str, phone: str, salary: int
) -> dict:
    """
    Create a new user with BHXH calculation.

    Args:
        db: Database session
        name: User full name
        phone: Vietnamese phone number (10 digits, starts with 0)
        salary: Monthly salary in VND

    Returns:
        Created user record as dict

    Raises:
        ValueError: If phone format is invalid or salary is negative
    """
    # ... real implementation with db.add(), db.commit()
```

---

## Reference Materials

| Document | Location |
|----------|----------|
| Code File Naming Standards | `02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md` |
| Quality Gates Framework | `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md` |
| Project Structure Standard | `02-Core-Methodology/Documentation-Standards/SDLC-Project-Structure-Standard.md` |
| Zero Mock Policy | Module 03 (this training series) |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | Quality Standards Overview — core metrics | 20 min |
| 2 | Test Coverage Standards — unit, integration, E2E | 45 min |
| 3 | Code File Naming Standards — per language | 30 min |
| 4 | Code Style Standards — PEP 8, ESLint, comments | 30 min |
| 5 | Performance Standards — API, database, frontend | 30 min |
| 6 | Security Standards — OWASP, input validation, auth | 30 min |
| 7 | Hands-on Exercises — review and fix code | 55 min |
| | **Total** | **4h** |

### After completing this module, participants must be able to:

1. State the minimum test coverage requirements (80% unit, 70% integration, 60% E2E).
2. Apply correct file naming conventions for Python, TypeScript, and React.
3. Write code comments in English that explain WHY, not WHAT.
4. Identify performance violations (N+1 queries, missing indexes, magic numbers).
5. Apply input validation using Pydantic or equivalent.

> **Remember**: "80% coverage is the floor, not the ceiling." Meeting the minimum is the starting point — aiming higher protects the team.

---

## Assessment Questions

**Q1.** What is the minimum unit test coverage required by SDLC 6.3.0?
> **Answer**: 80% minimum, with a target of 90%.

**Q2.** What naming convention applies to Python files?
> **Answer**: snake_case, max 50 characters (e.g., `user_service.py`).

**Q3.** What naming convention applies to React component files?
> **Answer**: PascalCase, max 50 characters (e.g., `ARDashboard.tsx`).

**Q4.** What is the target API response time at p50?
> **Answer**: Less than 50 milliseconds.

**Q5.** What language must all code comments be written in?
> **Answer**: English only. Vietnamese comments are not permitted in code.
