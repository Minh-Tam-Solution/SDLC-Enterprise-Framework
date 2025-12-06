# 🧪 AI Test Case Generator - Stage 04 (TEST)
## Automated Test Case Generation for Quality Assurance

**Version**: 5.0.0  
**Date**: November 13, 2025  
**Stage**: 04 - TEST (Quality Assurance & Validation)  
**Time Savings**: 90% (8 hours → 45 minutes)  
**BFlow Validation**: 150+ test cases generated, 98% pass rate

---

## 🎯 Purpose

Generate comprehensive test cases covering:
- **Functional testing** (happy paths, edge cases, error scenarios)
- **Integration testing** (API contracts, database interactions)
- **Regression testing** (ensure no breaking changes)
- **User acceptance testing** (UAT scripts for real users)

---

## 📋 Universal AI Prompt Template

### Input Requirements
```markdown
Feature/Component: [Name]
Functionality: [What it does]
User Stories: [List acceptance criteria]
Tech Stack: [Backend/Frontend technologies]
```

### AI Prompt
```
You are an expert QA engineer for SDLC 5.0 Stage 04 (TEST). Generate comprehensive test cases for the following feature:

**Feature**: [Feature name]
**Functionality**: [Brief description]
**User Stories**:
[List acceptance criteria]

**Tech Stack**: [Technologies used]

Please generate test cases covering:

1. **Functional Testing** (Happy Paths)
   - Primary user flows
   - Expected outcomes
   - Validation rules

2. **Edge Cases**
   - Boundary conditions
   - Invalid inputs
   - Null/empty states

3. **Error Scenarios**
   - Network failures
   - Timeout handling
   - Invalid permissions

4. **Integration Points**
   - API endpoints
   - Database operations
   - External services

5. **Performance Criteria**
   - Response time expectations
   - Load requirements
   - Resource usage

For each test case, provide:
- Test ID
- Test Name
- Description
- Preconditions
- Test Steps
- Expected Result
- Actual Result (to be filled)
- Pass/Fail (to be marked)

Format: Markdown table for easy tracking
Coverage Target: 95%+ test coverage
Zero Mock Policy: Use real data, no mocks
```

---

## 🎨 BFlow Platform Example

### Input
```markdown
Feature: BHXH Compliance Calculator
Functionality: Calculate Vietnamese social insurance contributions (employer 17.5%, employee 8.0%)
User Stories:
- AS an HR manager, I want to calculate BHXH contributions accurately
- GIVEN salary input, WHEN I click calculate, THEN show employer + employee amounts
- MUST be exact to Vietnamese regulations (BHXH 17.5%/8.0%)

Tech Stack: Python/Django backend, React frontend, PostgreSQL database
```

### AI-Generated Test Cases (Sample)

| Test ID | Test Name | Description | Preconditions | Test Steps | Expected Result | Actual | Pass/Fail |
|---------|-----------|-------------|---------------|------------|-----------------|--------|-----------|
| TC-001 | Valid Salary Calculation | Calculate BHXH for standard salary | User logged in, salary = 10,000,000 VND | 1. Enter 10,000,000<br/>2. Click Calculate | Employer: 1,750,000<br/>Employee: 800,000 | - | - |
| TC-002 | Minimum Wage Boundary | Test minimum regional wage | User logged in | 1. Enter 4,680,000<br/>2. Click Calculate | Employer: 819,000<br/>Employee: 374,400 | - | - |
| TC-003 | Maximum Contribution Cap | Test maximum contribution limit | User logged in | 1. Enter 100,000,000<br/>2. Click Calculate | Apply 20x minimum wage cap | - | - |
| TC-004 | Invalid Input - Negative | Test negative salary input | User logged in | 1. Enter -1,000,000<br/>2. Click Calculate | Error: "Salary must be positive" | - | - |
| TC-005 | Invalid Input - Zero | Test zero salary | User logged in | 1. Enter 0<br/>2. Click Calculate | Error: "Salary must be greater than 0" | - | - |
| TC-006 | Invalid Input - Non-numeric | Test non-numeric input | User logged in | 1. Enter "abc"<br/>2. Click Calculate | Error: "Please enter valid number" | - | - |
| TC-007 | API Response Time | Test performance | User logged in | 1. Make API call<br/>2. Measure time | Response < 50ms (P95) | - | - |
| TC-008 | Database Integration | Verify data persistence | User logged in | 1. Calculate<br/>2. Save to DB<br/>3. Query DB | Record saved correctly | - | - |
| TC-009 | Concurrent Users | Test load handling | 100 concurrent users | 1. Simulate 100 users<br/>2. All calculate | All succeed, <50ms avg | - | - |
| TC-010 | Regression - Old Data | Ensure backward compatibility | Existing records | 1. Load old record<br/>2. Recalculate | Still accurate | - | - |

**BFlow Result**: 150+ test cases generated in 45 minutes (manual: 8 hours), 98% pass rate, 87% code coverage achieved.

---

## 🎯 Quality Gates (SDLC 5.0 Stage 04)

Before moving to Stage 05 (DEPLOY), ensure:

- ✅ 95%+ test cases passed
- ✅ Zero critical bugs
- ✅ Performance targets met (<50ms API, <2s page load)
- ✅ Security scans passed (no critical vulnerabilities)
- ✅ UAT satisfaction > 80%

---

## 💡 Best Practices

### Test Case Quality
- **Specificity**: Each test case tests ONE thing
- **Repeatability**: Can be executed multiple times with same result
- **Independence**: Tests don't depend on each other
- **Clear Expected Results**: No ambiguity in pass/fail criteria

### Zero Mock Policy (Pillar 1)
- ❌ Don't use mock data in tests
- ✅ Use real test database with real data
- ✅ Use staging environment that mirrors production
- ✅ Test with actual API endpoints

### Coverage Targets
- **Unit Tests**: 80%+ code coverage
- **Integration Tests**: All API endpoints covered
- **E2E Tests**: All critical user journeys
- **UAT**: 5-10 real users, 80%+ satisfaction

---

## 🔗 Related Tools

**Stage 03 (BUILD)**:
- Pre-commit hooks ensure tests run before commit
- CI/CD pipeline runs full test suite

**Stage 05 (DEPLOY)**:
- Only deploy if all tests pass
- Smoke tests run post-deployment

**Stage 06 (OPERATE)**:
- Production incidents inform new test cases
- Regression tests prevent repeat issues

---

## 📊 Time Savings

**Manual Process**: 8 hours
- Brainstorm test scenarios: 2 hours
- Write test cases: 4 hours
- Format and organize: 2 hours

**With AI**: 45 minutes
- Prepare feature specs: 15 minutes
- Run AI prompt: 5 minutes
- Review and refine: 25 minutes

**Savings**: 90% (8 hours → 45 minutes)

---

## 🎯 Success Metrics

**BFlow Platform** (Stage 04 TEST):
- Test Cases Generated: 150+ cases
- Time Taken: 45 minutes (vs 8 hours manual)
- Pass Rate: 98% (147/150 passed)
- Coverage Achieved: 87% code coverage
- Bugs Found: 23 bugs (18 fixed, 5 minor deferred)
- UAT Satisfaction: 94% (10 pilot users)

**Result**: Ready for Stage 05 (DEPLOY) ✅

---

## 📝 Output Template

Save AI output as:
```
tests/
├── functional/
│   ├── test_bhxh_calculator.py
│   ├── test_vat_compliance.py
│   └── test_fifo_inventory.py
├── integration/
│   ├── test_api_endpoints.py
│   └── test_database_operations.py
├── performance/
│   └── test_load_stress.py
└── test_cases.md  # This AI-generated document
```

---

**Next Stage**: [Stage 05 (DEPLOY) - Deployment Tools](../deployment/)

**Documentation**: [SDLC-Core-Methodology.md - Stage 04](../../../02-Core-Methodology/SDLC-Core-Methodology.md)

