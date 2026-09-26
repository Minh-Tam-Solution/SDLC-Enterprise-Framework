---
document_id: "TRAINING-MODULE-03"
title: "Module 03: Zero Mock Policy"
framework: "SDLC 6.3.0"
ring: "Ring 3 — Training"
duration: "4 hours (7 parts)"
audience: "All team members — developers, pod leads, architects, product managers, executives"
prerequisite: "Module 01 (SDLC Overview), Module 02 (Six Pillars)"
format: "Lecture + Case Study + Hands-on Exercises"
---

# Module 03: Zero Mock Policy

> **Core principle**: "If it is not real, it does not exist in our codebase." Zero means zero — no exceptions, no "temporary" mocks, no excuses.

---

## 1. What Is the Zero Mock Policy? (20 minutes)

### Definition

The **Zero Mock Policy** is an absolute requirement: NEVER use mock, fake, dummy data or implementations in any of the 10 SDLC stages. There are no exceptions.

### The Golden Rule

```
"If it is not real, it does not exist in our codebase."

This applies to:
  - Development environments
  - Testing environments
  - Staging environments
  - Proof of concepts
  - Quick demos
  - Every other context
```

---

## 2. The 679 Mock Crisis — Origin Story (30 minutes)

### What Happened (September 2025)

```
Context:
  Routine code quality audit of Platform B codebase

Discovery:
  679 mock instances scattered across the entire codebase
  Many marked as "temporary" — some dating back months

Impact:
  Production failure rate: 78%
  Tests passing but production failing
  Customer complaints increasing

Root Cause:
  "Temporary" mocks became permanent
  Mock data behavior != real data behavior
  No enforcement mechanism existed
```

### Emergency Response Timeline

```
Day 1 (Hours 0-24):
  Crisis identified and escalated
  Team mobilized for emergency sprint
  Scanning tools deployed across codebase

Day 2 (Hours 24-48):
  All 679 mocks catalogued and categorized
  Replacement strategy defined per category
  Implementation of real replacements began

Day 3+:
  Real implementations deployed and tested
  Pre-commit hooks created
  Zero Mock Policy formally established

Result:
  0 mocks remaining in codebase
  95% production success rate (up from 22%)
  Policy enforced via automation from this point forward
```

### Three Lessons Learned

| Lesson | Explanation |
|--------|-------------|
| **Mocks are never temporary** | Every "temporary" mock in the 679 had been there for weeks or months. Technical debt accumulates silently. |
| **Tests lie with mocks** | All tests passed with mock data. Production failed with real data. Passing tests gave false confidence. |
| **Prevention beats cure** | Automated enforcement (pre-commit hooks, CI/CD gates) is essential. Human discipline alone is insufficient. |

---

## 3. What Is Prohibited (30 minutes)

### Prohibited Patterns

```python
# PROHIBITED: Mock data
MOCK_USER = {"id": 1, "name": "Test User"}
fake_users = [{"id": 1}, {"id": 2}]
dummy_products = [{"sku": "TEST-001"}]

# PROHIBITED: Mock API responses
def get_user():
    return {"status": "ok", "data": MOCK_USER}  # hardcoded

# PROHIBITED: Mock database
users_db = {}  # in-memory dict pretending to be a database

# PROHIBITED: Stub functions
def send_email():
    pass  # TODO: implement later

# PROHIBITED: Always-succeed stubs
def process_payment():
    return True  # always succeeds — hides real failures

# PROHIBITED: Deferred implementation
def calculate_tax():
    raise NotImplementedError  # not acceptable
```

### Detection Keywords

```
Code patterns scanned by pre-commit hooks:
  mock_    fake_    dummy_    test_data    sample_
  placeholder    stub_    TODO:    FIXME:    NotImplementedError

File patterns scanned:
  *mock*.py    *fake*.ts    *test_data*.json    *dummy*.js
```

---

## 4. What Is Required Instead (30 minutes)

### Correct Patterns

```python
# CORRECT: Real database connection
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)

# CORRECT: Real API call
import httpx
async def get_user(user_id: int):
    response = await client.get(f"/api/users/{user_id}")
    return response.json()

# CORRECT: Complete implementation
def send_email(to: str, subject: str, body: str):
    smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    smtp.send_message(msg)
    smtp.quit()

# CORRECT: Real Vietnamese data calculations
from decimal import Decimal

def calculate_bhxh(salary: int) -> dict:
    employer_rate = Decimal("0.175")  # 17.5%
    employee_rate = Decimal("0.08")   # 8%
    return {
        "employer": int(salary * employer_rate),
        "employee": int(salary * employee_rate),
    }
```

### Testing Without Mocks

```
Strategy: Use a real test database (PostgreSQL), not in-memory fakes.

Setup:
  1. Create a dedicated test database
  2. Run migrations against it
  3. Seed with real-pattern data using factories
  4. Run tests against real database
  5. Clean up (rollback) after each test

Benefits:
  - Tests reflect actual production behavior
  - Real query performance measured
  - Real constraint validation exercised
```

### Real Data Generation with Factories

```python
from factory import Factory, Faker, LazyAttribute
from decimal import Decimal

class UserFactory(Factory):
    class Meta:
        model = User

    name = Faker("name", locale="vi_VN")
    phone = Faker("phone_number", locale="vi_VN")
    email = Faker("email")

    @LazyAttribute
    def bhxh_employer(self):
        return int(self.salary * Decimal("0.175"))
```

---

## 5. Zero Mock Across All 10 Stages (20 minutes)

| Stage | Prohibited | Required |
|-------|-----------|----------|
| 00 Foundation | Fake stakeholder data | Real interviews, real feedback |
| 01 Planning | Placeholder requirements | Real user stories, real criteria |
| 02 Design | "TBD" in architecture | Complete specifications |
| 03 Integrate | Mock API contracts | Real OpenAPI specifications |
| 04 Build | Mock implementations | Real, complete code |
| 05 Test | Mock test data | Real test database |
| 06 Deploy | Fake deployment scripts | Real deployment automation |
| 07 Operate | Fake monitoring data | Real metrics, real alerts |
| 08 Collaborate | Fake review approvals | Real code reviews |
| 09 Govern | Fake compliance reports | Real audit data |

---

## 6. Enforcement and Consequences (20 minutes)

### Automated Enforcement

```yaml
Pre-commit hooks:
  Tool: scripts/check_zero_mock.py
  Trigger: Every commit attempt
  Action: Reject commit if mock patterns found

CI/CD pipeline:
  Stage: Zero Mock Scan (runs in parallel with tests)
  Action: Fail build, block PR merge

Code review:
  Checklist item: "Zero Mock Policy verified"
  Action: Reject review if violations found
```

### Consequences of Violation

```
Pre-commit:  Commit rejected. Must fix before committing.
CI/CD:       Build fails. PR cannot be merged.
Code review: Review rejected. Must fix and re-submit.
Production:  Incident created. Root cause analysis required.
```

### Common Excuses (All Rejected)

| Excuse | Response |
|--------|----------|
| "But it is just for development" | Development code becomes production code. 679 mocks proved this. |
| "It is temporary until the API is ready" | Temporary becomes permanent. Build the real API first. |
| "Tests are faster with mocks" | Fast wrong tests are worse than slow correct tests. |
| "We do not have test data" | Create real test data with factories. |
| "The external service is down" | Wait, or build a real fallback. Do not fake external services. |

---

## 7. Hands-on Exercises (50 minutes)

### Exercise 1: Identify Violations (20 minutes)

Review the following code snippets and identify which ones violate the Zero Mock Policy:

**Snippet A:**
```python
def test_create_invoice(db_session):
    response = client.post("/invoices", json={
        "customer_id": 42,
        "amount": 15000000
    })
    assert response.status_code == 201
    invoice = db_session.query(Invoice).first()
    assert invoice.amount == 15000000
```

**Snippet B:**
```python
MOCK_INVOICE = {"id": 1, "amount": 100, "status": "paid"}

def test_get_invoice():
    assert get_invoice(1) == MOCK_INVOICE
```

**Snippet C:**
```python
def calculate_vat(amount):
    # TODO: implement real VAT calculation
    return amount * 0.1
```

**Snippet D:**
```python
users_cache = {}  # in-memory cache for performance

def get_cached_user(user_id):
    if user_id not in users_cache:
        users_cache[user_id] = db.query(User).get(user_id)
    return users_cache[user_id]
```

### Exercise 1 Answers

**Snippet A:** COMPLIANT. Uses a real database session and a real API client.
**Snippet B:** VIOLATION. Uses `MOCK_INVOICE` — hardcoded fake data.
**Snippet C:** VIOLATION. Contains `TODO: implement real` — placeholder implementation.
**Snippet D:** COMPLIANT. The `users_cache` is a performance optimization using real database data, not a mock.

### Exercise 2: Fix Violations (30 minutes)

Take Snippets B and C from Exercise 1 and rewrite them to be Zero Mock compliant.

**Expected answer for Snippet B:**
```python
def test_get_invoice(db_session):
    # Create a real invoice in the test database
    invoice = InvoiceFactory.create(amount=15000000, status="paid")
    db_session.add(invoice)
    db_session.commit()

    result = get_invoice(invoice.id)
    assert result["amount"] == 15000000
    assert result["status"] == "paid"
```

**Expected answer for Snippet C:**
```python
from decimal import Decimal

def calculate_vat(amount: int, rate: Decimal = Decimal("0.10")) -> int:
    """Calculate VAT per Vietnamese tax law."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    return int(amount * rate)
```

---

## Reference Materials

| Document | Location |
|----------|----------|
| Zero Mock Policy (origin) | SDLC 6.3.0 Framework, Pillar 2 |
| Quality Gates Framework | `02-Core-Methodology/Governance-Compliance/SDLC-Quality-Gates-Assurance-Framework.md` |
| Code Quality Standards | Module 04 (this training series) |
| 679 Mock Crisis Post-Mortem | `06-Case-Studies/` |

---

## Module Summary

| # | Topic | Duration |
|---|-------|:--------:|
| 1 | What Is the Zero Mock Policy | 20 min |
| 2 | The 679 Mock Crisis — origin story | 30 min |
| 3 | What Is Prohibited — patterns and keywords | 30 min |
| 4 | What Is Required Instead — correct patterns | 30 min |
| 5 | Zero Mock Across All 10 Stages | 20 min |
| 6 | Enforcement and Consequences | 20 min |
| 7 | Hands-on Exercises — identify and fix violations | 50 min |
| | **Total** | **4h** |

### After completing this module, participants must be able to:

1. State the Zero Mock Policy and explain why it has no exceptions.
2. Retell the 679 Mock Crisis and its three key lessons.
3. Identify prohibited code patterns (mock_, fake_, dummy_, TODO:, stub_).
4. Write tests using real databases and factories instead of mocks.
5. Respond to common excuses for using mocks with the correct counter-argument.

> **Remember**: "If it is not real, it does not exist in our codebase." The cost of 679 mocks was a 78% production failure rate. The cost of building it real from day one is zero.

---

## Assessment Questions

**Q1.** How many mock instances triggered the creation of the Zero Mock Policy?
> **Answer**: 679 mock instances in the Platform B codebase.

**Q2.** Is a mock acceptable if it is marked as "temporary"?
> **Answer**: No. The 679 Mock Crisis proved that "temporary" mocks become permanent. Zero means zero.

**Q3.** What is the correct way to test database operations without mocks?
> **Answer**: Use a real test database (PostgreSQL), run real migrations, seed with factory-generated data following real patterns, and clean up after each test.

**Q4.** Name three automated enforcement mechanisms for the Zero Mock Policy.
> **Answer**: (1) Pre-commit hooks scanning for mock patterns, (2) CI/CD pipeline gates failing the build, (3) Code review checklist requiring zero mock verification.

**Q5.** A developer argues "tests run 10x faster with mocks." What is the correct response?
> **Answer**: Fast wrong tests are worse than slow correct tests. Mock-based tests give false confidence — they pass in testing but fail in production with real data.
