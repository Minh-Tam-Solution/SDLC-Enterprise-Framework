# 👥 AI UAT Script Creator - Stage 04 (TEST)
## User Acceptance Testing Script Generator

**Version**: 5.0.0  
**Date**: November 13, 2025  
**Stage**: 04 - TEST (User Acceptance Testing)  
**Time Savings**: 85% (4 hours → 36 minutes)  
**BFlow Validation**: 10 pilot users, 94% satisfaction

---

## 🎯 Purpose

Generate structured UAT scripts for real users to validate:
- **Feature usability** (can users complete tasks without training?)
- **User satisfaction** (do users love it?)
- **Problem validation** (does it solve their pain points?)
- **Edge case discovery** (what do real users break?)

---

## 📋 Universal AI Prompt

```
You are an expert UX researcher for SDLC 5.0 Stage 04 (TEST - UAT). Create a User Acceptance Testing script for:

**Feature**: [Feature name]
**Target Users**: [User persona]
**Key User Stories**: [List]
**Success Criteria**: [What defines success?]

Generate a UAT script with:

1. **Participant Profile**
   - Who should test this?
   - Prerequisites/requirements
   - Time commitment

2. **Introduction Script** (5 min)
   - Welcome and purpose
   - Confidentiality and consent
   - Think-aloud protocol explanation

3. **Task Scenarios** (30-45 min)
   - 5-7 realistic tasks
   - Clear context for each task
   - Success criteria (observable)
   - Time limit per task

4. **Observation Checklist**
   - What to watch for
   - Red flags
   - Success indicators

5. **Post-Task Questions**
   - Satisfaction rating (1-5)
   - Difficulty rating (1-5)
   - Open-ended feedback

6. **Wrap-Up** (10 min)
   - Overall satisfaction (SUS score)
   - Top 3 likes
   - Top 3 frustrations
   - Would you use this? (Yes/No/Maybe)

Format: Ready-to-use script for facilitator
Target: 80%+ user satisfaction for Stage 05 (DEPLOY) approval
```

---

## 🎨 BFlow Platform Example

**Generated UAT Script**: BHXH Compliance Calculator

### Participant Profile
- **Role**: HR Manager at Vietnamese SME
- **Experience**: Uses payroll software daily
- **Prerequisites**: Basic computer skills, understands BHXH regulations
- **Time**: 60 minutes
- **Compensation**: 200,000 VND gift card

### Introduction (5 min)
> "Welcome! Thank you for helping us test BFlow's BHXH calculator. This session will take about 60 minutes. Everything you say is confidential. There are no wrong answers - we're testing the software, not you. Please think aloud as you work through tasks. Do you consent to proceed?"

### Task 1: Calculate Monthly BHXH (10 min)
**Context**: You need to calculate BHXH contributions for a new employee with salary 12,000,000 VND.

**Task**: Calculate and show employer + employee BHXH contributions.

**Success Criteria**:
- ✅ User finds BHXH calculator
- ✅ User enters salary correctly
- ✅ Results show: Employer 2,100,000 / Employee 960,000
- ✅ Completed in < 3 minutes

**Observations**:
- Did user find the calculator easily?
- Any confusion about input fields?
- Were results clear and understandable?

**Post-Task Questions**:
1. How easy was this task? (1=Very Hard, 5=Very Easy)
2. Were the results what you expected?
3. What would make this better?

### Task 2-7: [Similar structure for other features]

### Wrap-Up (10 min)
1. **Overall Satisfaction**: "Rate overall experience 1-10"
2. **SUS Score**: [10 standard questions]
3. **Top 3 Likes**: "What did you like most?"
4. **Top 3 Frustrations**: "What frustrated you?"
5. **Usage Intent**: "Would you use this in your daily work?"
   - ☐ Yes, definitely
   - ☐ Maybe, if improved
   - ☐ No, not useful

### BFlow Result
- **Users Tested**: 10 HR managers
- **Satisfaction**: 94% (9.4/10 average)
- **Task Success Rate**: 96% (48/50 tasks completed)
- **Time to Complete**: Avg 42 minutes per user
- **Usage Intent**: 10/10 said "Yes, definitely"
- **Key Finding**: 3 usability improvements identified, all fixed pre-launch

---

## 📊 Success Metrics

**Quality Gate Requirements**:
- ✅ UAT satisfaction > 80% (BFlow: 94%)
- ✅ Task success rate > 90% (BFlow: 96%)
- ✅ Usage intent > 70% (BFlow: 100%)
- ✅ Critical bugs found and fixed (BFlow: 3 found, 3 fixed)

---

**Related**: [test-case-generator.md](./test-case-generator.md), [performance-test-analyzer.md](./performance-test-analyzer.md)

