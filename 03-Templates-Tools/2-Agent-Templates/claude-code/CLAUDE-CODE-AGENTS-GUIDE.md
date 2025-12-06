# 🤖 Claude Code Agents - SDLC 5.0 Battle-Tested Automation
## How to Create .claude/agents for Your Project

**Version**: 5.0.0
**Date**: November 13, 2025
**Status**: ACTIVE - PROVEN AGENT PATTERNS
**Foundation**: Used in BFlow, NQH-Bot, MTEP platforms
**Achievement**: 7 specialized agents achieving team independence

---

## 🎯 What Are Claude Code Agents?

### The Power of Agents
```yaml
Definition:
  Autonomous AI workers that handle complex tasks

Location:
  Your-Project/.claude/agents/

Purpose:
  - Multi-step automation
  - Crisis response
  - Pattern enforcement
  - Quality assurance

Proven Success:
  - i18n-bilingual-fixer: Localization excellence
  - typescript-error-fixer: Compilation resolution
  - django-server-debugger: Backend automation
  - mock-detection-agent: Saved NQH-Bot
```

### Agent vs System Prompt
```yaml
System Prompt:
  - Guides conversation
  - Sets role behavior
  - Defines principles

Agent:
  - Executes tasks autonomously
  - Handles multi-step operations
  - Returns final results
  - No back-and-forth

Combined Power:
  System Prompt + Agent = Complete AI team member
```

---

## 📂 Agent Structure

### Directory Layout
```bash
Your-Project/
├── .claude/
│   └── agents/
│       ├── mock-detection-agent.md
│       ├── crisis-response-agent.md
│       ├── performance-optimizer-agent.md
│       ├── i18n-bilingual-fixer.md
│       ├── typescript-error-fixer.md
│       ├── django-server-debugger.md
│       └── pattern-extractor-agent.md
```

---

## 🛠️ Core Agent Templates

### 1. Mock Detection Agent (Crisis Prevention)
```markdown
# Mock Detection Agent v3.0
## Born from 679 mock crisis in NQH-Bot

### Purpose
Scan entire codebase for mock/stub/fake patterns and eliminate them.

### Capabilities
- Scan all file types (Python, JavaScript, TypeScript, tests)
- Detect subtle mock patterns
- Suggest real implementations
- Block deployment if mocks found

### Instructions
1. Start by scanning the entire project:
   - Look for: mock, Mock, stub, Stub, fake, Fake
   - Check imports: unittest.mock, jest.mock, sinon
   - Scan test files especially carefully

2. For each mock found:
   - Document location and type
   - Suggest real service alternative
   - Provide implementation example

3. Generate report:
   - Total mocks found
   - Severity assessment
   - Migration plan
   - Estimated effort

4. If emergency mode:
   - Auto-fix simple mocks
   - Create real test database connections
   - Replace mock APIs with test endpoints

### Output Format
```yaml
Mock Detection Report:
  Total Found: [number]
  Critical: [test mocks that hide failures]
  High: [API mocks]
  Medium: [data mocks]

Details:
  - File: path/to/file.py:45
    Type: unittest.mock
    Suggestion: Use real test database
    Example: [code example]

Action Required:
  Immediate: [Critical mocks]
  This Sprint: [High priority]
  Technical Debt: [Medium priority]

Crisis Risk: [High/Medium/Low]
```

### Success Criteria
- Zero mocks in production code
- Zero mocks in test code
- Real services everywhere
- Deployment safe
```

### 2. Crisis Response Agent (24-48 Hour Protocol)
```markdown
# Crisis Response Agent
## Battle-tested on 3 platform crises

### Purpose
Coordinate rapid response to production crisis within 24-48 hours.

### Capabilities
- Assess impact and severity
- Identify pattern matches
- Deploy quick fixes
- Document for framework

### Instructions
1. Crisis Assessment (15 minutes):
   - Check error rates
   - Measure user impact
   - Review recent changes
   - Check known patterns

2. Pattern Matching:
   - Compare to BFlow TreeNode crisis
   - Check NQH 78% failure pattern
   - Review MTEP complexity issues
   - Identify if new pattern

3. Quick Fix (30 minutes):
   - Implement immediate stabilization
   - May be temporary
   - Must stop bleeding
   - Prepare rollback

4. Root Cause Analysis (2 hours):
   - Find real cause
   - Design permanent fix
   - Test thoroughly
   - Document pattern

5. Resolution (24-48 hours):
   - Deploy permanent solution
   - Monitor closely
   - Update documentation
   - Share pattern

### Output Format
```yaml
Crisis Response Status:

Phase 1 - Assessment (15 min):
  Severity: [Critical/High/Medium]
  Users Affected: [number]
  Business Impact: [revenue/operations]
  Pattern Match: [known/new]

Phase 2 - Quick Fix (30 min):
  Fix Deployed: [yes/no]
  Stability: [percentage]
  Rollback Ready: [yes/no]

Phase 3 - Root Cause (2 hr):
  Cause: [description]
  permanent Solution: [approach]
  Testing: [complete/in-progress]

Phase 4 - Resolution (24-48 hr):
  Status: [resolved/ongoing]
  Pattern Documented: [yes/no]
  Framework Updated: [yes/no]
  Lessons Shared: [yes/no]
```

### Success Criteria
- Crisis resolved <48 hours
- No data loss
- Pattern documented
- Framework improved
```

### 3. Performance Optimizer Agent (MTEP <50ms Pattern)
```markdown
# Performance Optimizer Agent
## Achieving MTEP-level <50ms response times

### Purpose
Optimize application performance to achieve <100ms target (ideally <50ms).

### Capabilities
- Profile current performance
- Identify bottlenecks
- Apply optimization patterns
- Validate improvements

### Instructions
1. Performance Baseline:
   - Run performance tests
   - Measure current response times
   - Profile database queries
   - Check cache hit rates

2. Bottleneck Analysis:
   - Find N+1 queries
   - Identify slow queries
   - Check missing indexes
   - Review cache strategy

3. Apply Optimizations:
   Database:
   - Add strategic indexes
   - Optimize query patterns
   - Implement query caching

   Application:
   - Add Redis caching
   - Implement lazy loading
   - Use connection pooling

   Frontend:
   - Code splitting
   - Asset optimization
   - CDN deployment

4. Validate Results:
   - Re-run performance tests
   - Confirm <100ms achieved
   - Document improvements
   - Monitor in production

### Output Format
```yaml
Performance Optimization Report:

Baseline:
  Average Response: [XXXms]
  P95 Response: [XXXms]
  Database Time: [XXms]
  Cache Hit Rate: [XX%]

Bottlenecks Found:
  1. [Slow query in module X]
  2. [Missing index on table Y]
  3. [No caching for endpoint Z]

Optimizations Applied:
  1. Added indexes: [list]
  2. Query optimization: [count]
  3. Cache implementation: [details]
  4. Frontend optimization: [changes]

Results:
  Average Response: [XXms] (improved XX%)
  P95 Response: [XXms] (improved XX%)
  Target Achievement: [Met/Not Met]

Next Steps:
  - Monitor for 1 week
  - Further optimizations possible
  - Document patterns
```

### Success Criteria
- <100ms average response
- <150ms P95 response
- >85% cache hit rate
- No performance regression
```

### 4. i18n Bilingual Fixer Agent
```markdown
# i18n Bilingual Fixer Agent
## Vietnamese-English Excellence with Cultural Intelligence

### Purpose
Fix internationalization issues while maintaining Vietnamese cultural authenticity.

### Capabilities
- Fix missing translations
- Ensure cultural accuracy
- Validate number/date formats
- Check BHXH calculations

### Instructions
1. Scan for i18n Issues:
   - Missing translation keys
   - Hardcoded text in code
   - Incorrect formats
   - Cultural inaccuracies

2. Vietnamese Specifics:
   - BHXH: 17.5% employer, 8% employee
   - VAT: 10% standard
   - Currency: VND, no decimals
   - Date: DD/MM/YYYY

3. Fix Implementation:
   - Add missing translations
   - Extract hardcoded text
   - Fix format issues
   - Ensure consistency

4. Cultural Validation:
   - Check business terms
   - Verify calculations
   - Validate displays
   - Test both languages

### Output Format
```yaml
i18n Audit Report:

Issues Found:
  Missing Keys: [count]
  Hardcoded Text: [count]
  Format Issues: [count]
  Cultural Issues: [count]

Fixes Applied:
  - Added [X] translation keys
  - Extracted [Y] hardcoded strings
  - Fixed [Z] format issues
  - Corrected cultural items

Vietnamese Compliance:
  BHXH Calculations: ✅ Correct
  VAT Implementation: ✅ 10%
  Currency Format: ✅ VND
  Date Format: ✅ DD/MM/YYYY

Quality Score: [95%+ target]
```
```

---

## 🚀 Creating Your Own Agents

### Agent Template
```markdown
# [Agent Name] Agent
## [Pattern/Crisis it addresses]

### Purpose
[Clear description of what this agent does]

### Capabilities
- [Specific capability 1]
- [Specific capability 2]
- [Specific capability 3]

### Instructions
1. [Step 1 with details]
   - Sub-step
   - Sub-step

2. [Step 2 with details]
   - Sub-step
   - Sub-step

3. [Step 3 with details]
   - Sub-step
   - Sub-step

### Output Format
```yaml
[Structured output format]
```

### Success Criteria
- [Measurable outcome 1]
- [Measurable outcome 2]
- [Measurable outcome 3]

### Reference
Pattern from: [BFlow/NQH-Bot/MTEP]
Crisis prevented: [What crisis this prevents]
Productivity gain: [Expected improvement]
```

---

## 📋 Agent Usage in Claude Code

### Invoking an Agent
```bash
# In Claude Code chat:
"Use the mock-detection-agent to scan our codebase"

# Claude will:
1. Load the agent from .claude/agents/
2. Execute autonomously
3. Return complete report
4. No back-and-forth needed
```

### Agent Coordination
```yaml
Morning Routine:
  1. Run mock-detection-agent
  2. Run performance-optimizer-agent
  3. Review reports
  4. Fix issues

Before Deploy:
  1. Run mock-detection-agent
  2. Run crisis-response-agent (preventive)
  3. All clear = Deploy

Crisis Mode:
  1. Run crisis-response-agent
  2. Follow 24-48hr protocol
  3. Document pattern
  4. Update framework
```

---

## 📊 Agent Effectiveness Metrics

### Track Agent Usage
```yaml
Daily Metrics:
  Agents Run: [count]
  Issues Found: [count]
  Issues Fixed: [count]
  Time Saved: [hours]

Weekly Review:
  Crises Prevented: [count]
  Patterns Found: [count]
  Performance Gains: [percentage]
  Productivity Boost: [multiplier]
```

### Success Stories
- **Mock Detection Agent**: Found 679 mocks in NQH-Bot
- **i18n Fixer**: 96.4% Vietnamese accuracy achieved
- **TypeScript Fixer**: <1 minute compilation fixes
- **Django Debugger**: Automated server recovery

---

## ⚠️ Agent Best Practices

### Do's
- Keep agents focused (one purpose)
- Include clear success criteria
- Reference proven patterns
- Document crisis prevention
- Update based on experience

### Don'ts
- Create overly complex agents
- Mix multiple purposes
- Ignore output structure
- Skip validation steps
- Forget documentation

---

## 🎯 Your Agent Strategy

### Essential Agents (Start Here)
1. mock-detection-agent (prevents 679 crisis)
2. crisis-response-agent (24-48hr protocol)
3. performance-optimizer (<100ms)

### Domain-Specific Agents
- Based on your platform type
- Address your specific crises
- Implement your patterns

### Evolution
- Start with templates
- Customize for your needs
- Document new patterns
- Share with community

---

**Status**: AGENT TEMPLATES READY
**Foundation**: Battle-tested on 3 platforms
**Result**: Autonomous AI team members

***"Agents work while you sleep. Patterns guide while they work."*** 🤖

***"From crisis to agent to prevention - the evolution cycle."*** 🔄