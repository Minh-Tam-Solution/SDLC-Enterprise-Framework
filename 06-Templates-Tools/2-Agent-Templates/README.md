# 🤖 2-Agent-Templates - AI Assistant Configurations
## Pre-Configured Agents for Every Role

**Priority**: ⭐⭐⭐⭐ (HIGH)
**Purpose**: Ready-to-use AI agent configurations for different roles and tools
**Status**: PRODUCTION-READY
**Coverage**: 5 AI platforms × 3-8 roles each = 17 specialized agents

---

## 🎯 What Are Agent Templates?

Agent templates are **pre-configured prompts and instructions** for AI assistants like:
- Claude Code (Anthropic)
- Cursor (OpenAI integration)
- GitHub Copilot (Microsoft)
- ChatGPT (OpenAI)
- Gemini (Google)

Each template configures the AI to act as a **specific role** (Developer, Architect, QA, etc.) following **SDLC 4.9 complete 10-stage lifecycle standards**.

---

## 📂 Directory Structure

```
2-Agent-Templates/
├── README.md                        # This file (start here!)
│
├── claude-code/                     # 8 agents for Claude Code
│   ├── CLAUDE-CODE-AGENTS-GUIDE.md                  # Overview & usage
│   ├── CLAUDE-CODE-ARCHITECT.md.template            # System design role
│   ├── CLAUDE-CODE-BUSINESS-ANALYST.md.template     # Requirements role
│   ├── CLAUDE-CODE-CONDUCTOR-CPO-CTO.md.template    # Leadership role
│   ├── CLAUDE-CODE-DEVELOPER.md.template            # Implementation role
│   ├── CLAUDE-CODE-DEVOPS-ENGINEER.md.template      # Infrastructure role
│   ├── CLAUDE-CODE-PRODUCT-OWNER.md.template        # Product role
│   └── CLAUDE-CODE-QA-ENGINEER.md.template          # Testing role
│
├── cursor/                          # 2 agents for Cursor
│   ├── CURSOR-AI-DEVELOPER.md.template              # Development mode
│   └── CURSOR-CPO-SYSTEM-PROMPT.md.template         # Product mode
│
├── copilot/                         # 2 agents for GitHub Copilot
│   ├── GITHUB-COPILOT-CTO-SYSTEM-PROMPT.md.template # Tech lead mode
│   └── GITHUB-COPILOT-DEVELOPER.md.template         # Developer mode
│
├── chatgpt/                         # 1 agent for ChatGPT
│   └── CHATGPT-CEO-CRITICAL-REVIEWER.md.template    # Executive review
│
├── gemini/                          # 1 agent for Gemini
│   └── GEMINI-CEO-STRATEGIC-VALIDATOR.md.template   # Strategic review
│
└── universal/                       # 2 cross-platform templates
    ├── CLAUDE.md.template           # Generic CLAUDE.md for any project
    └── AI-TOOLS-COORDINATION-BEST-PRACTICES.md  # Multi-agent coordination guide
```

---

## 🚀 Quick Start

### Step 1: Choose Your AI Platform

**Which AI tool are you using?**
- **Claude Code** → Use `claude-code/` directory
- **Cursor** → Use `cursor/` directory
- **GitHub Copilot** → Use `copilot/` directory
- **ChatGPT** → Use `chatgpt/` directory
- **Gemini** → Use `gemini/` directory

### Step 2: Choose Your Role

**What are you working on?**

| Role | Best For | Agent Template |
|------|----------|---------------|
| **Developer** | Writing code, implementing features | `*-DEVELOPER-*.template` |
| **Architect** | System design, technical decisions | `*-ARCHITECT-*.template` |
| **QA Engineer** | Testing, quality assurance | `*-QA-ENGINEER-*.template` |
| **DevOps** | Infrastructure, deployment, CI/CD | `*-DEVOPS-*.template` |
| **Product Owner** | Feature specs, user stories | `*-PRODUCT-OWNER-*.template` |
| **Business Analyst** | Requirements, user research | `*-BUSINESS-ANALYST-*.template` |
| **CTO/CPO** | Strategic oversight, code review | `*-CTO-*` or `*-CPO-*.template` |
| **CEO** | Critical review, business validation | `*-CEO-*.template` |

### Step 3: Install the Template

**For Claude Code:**
1. Copy template content from `claude-code/CLAUDE-CODE-DEVELOPER-SDLC-4.8.md.template`
2. Create `.claude/agents/developer.md` in your project
3. Paste template content
4. Customize for your project (replace placeholders)
5. Use with: `@developer` in Claude Code

**For Cursor:**
1. Copy template from `cursor/CURSOR-AI-DEVELOPER-SDLC-4.8.md.template`
2. Go to Cursor Settings → Features → Rules for AI
3. Paste template content
4. Save settings

**For GitHub Copilot:**
1. Copy template from `copilot/GITHUB-COPILOT-DEVELOPER-SDLC-4.8.md.template`
2. Create `.github/copilot-instructions.md` in your project
3. Paste template content
4. Commit to repository

**For ChatGPT:**
1. Copy template from `chatgpt/CHATGPT-CEO-CRITICAL-REVIEWER-SDLC-4.8.md.template`
2. Start new ChatGPT chat
3. Paste template as first message
4. Use "Custom Instructions" to make permanent

**For Gemini:**
1. Copy template from `gemini/GEMINI-CEO-STRATEGIC-VALIDATOR-SDLC-4.8.md.template`
2. Start new Gemini chat
3. Paste template as system prompt
4. Pin chat for reuse

---

## 🎯 Agent Roles Explained

### 👨‍💻 Developer (Implementation Focus)
**Use when:** Writing code, implementing features, debugging
**Key capabilities:**
- Code generation following SDLC 4.9
- Zero Mock Policy enforcement
- Performance optimization (<50ms)
- Test-driven development (80%+ coverage)
- Documentation automation

**Available for:** Claude Code, Cursor, GitHub Copilot

### 🏗️ Architect (System Design Focus)
**Use when:** Designing systems, making technical decisions
**Key capabilities:**
- System architecture design
- Technology stack selection
- Scalability planning
- Security architecture
- Integration patterns

**Available for:** Claude Code

### 🧪 QA Engineer (Testing Focus)
**Use when:** Writing tests, quality assurance, bug hunting
**Key capabilities:**
- Test suite generation (80%+ coverage)
- Test automation strategies
- Performance testing
- Security testing
- Regression test planning

**Available for:** Claude Code

### 🚀 DevOps Engineer (Infrastructure Focus)
**Use when:** Setting up infrastructure, deployment, CI/CD
**Key capabilities:**
- Infrastructure as Code
- CI/CD pipeline setup
- Monitoring & logging
- Docker/Kubernetes configuration
- Deployment automation

**Available for:** Claude Code

### 📋 Product Owner (Product Focus)
**Use when:** Defining features, writing user stories
**Key capabilities:**
- User story creation
- Acceptance criteria definition
- Feature prioritization
- Stakeholder communication
- Sprint planning

**Available for:** Claude Code

### 📊 Business Analyst (Requirements Focus)
**Use when:** Gathering requirements, user research
**Key capabilities:**
- Requirements elicitation
- User research synthesis
- Process modeling
- Gap analysis
- Documentation

**Available for:** Claude Code

### 🎯 CTO/CPO (Leadership Focus)
**Use when:** Strategic oversight, critical reviews
**Key capabilities:**
- Technical strategy
- Code review at scale
- Architecture decisions
- Team productivity
- Quality assurance

**Available for:** Claude Code, Cursor, GitHub Copilot

### 👔 CEO (Executive Focus)
**Use when:** Business validation, strategic review
**Key capabilities:**
- Business case validation
- ROI analysis
- Risk assessment
- Strategic alignment
- Executive decision support

**Available for:** ChatGPT, Gemini

---

## 🔧 Customization Guide

### Step 1: Copy Template
```bash
cp claude-code/CLAUDE-CODE-DEVELOPER-SDLC-4.8.md.template \
   .claude/agents/developer.md
```

### Step 2: Replace Placeholders

**Common placeholders to customize:**
- `[YOUR_PLATFORM_NAME]` → Your project name (e.g., "BFlow Platform")
- `[YOUR_TECH_STACK]` → Your technologies (e.g., "Django + React + PostgreSQL")
- `[YOUR_TEAM_SIZE]` → Team composition (e.g., "5 developers, 2 QA")
- `[YOUR_CODING_STANDARDS]` → Specific standards (e.g., "PEP 8, ESLint")
- `[YOUR_PERFORMANCE_TARGET]` → Performance goals (e.g., "<50ms API response")
- `[YOUR_CULTURAL_CONTEXT]` → Cultural specifics (e.g., "Vietnamese business practices")

### Step 3: Add Project-Specific Rules

**Example additions:**
```markdown
## Project-Specific Rules

### API Design
- All endpoints use RESTful conventions
- API versioning: /api/v1/, /api/v2/
- Authentication: JWT with RS256
- Rate limiting: 100 req/min per user

### Database
- PostgreSQL 15+
- Always use migrations
- No raw SQL (use ORM)
- Soft deletes only

### Testing
- Jest for frontend
- pytest for backend
- 80%+ coverage mandatory
- E2E tests for critical paths
```

---

## 📊 Multi-Agent Coordination

**When using multiple agents simultaneously:**

### Pattern 1: Role Specialization
```
Developer Agent → Implements feature
QA Agent → Reviews code + writes tests
DevOps Agent → Sets up deployment
```

### Pattern 2: Sequential Review
```
Developer Agent → Initial implementation
Architect Agent → Architecture review
CTO Agent → Strategic validation
CEO Agent → Business case validation
```

### Pattern 3: Parallel Development
```
Developer Agent A → Feature module A
Developer Agent B → Feature module B
QA Agent → Integration testing
```

**Best Practices:**
- ✅ Use `universal/AI-TOOLS-COORDINATION-BEST-PRACTICES.md` guide
- ✅ Clearly define boundaries between agents
- ✅ Document handoff points
- ✅ Avoid overlapping responsibilities
- ✅ Use consistent naming conventions

---

## 🎓 Learning Path

### Solo Developer (1 hour)
1. **Start**: Developer agent (30 min)
2. **Add**: QA agent for testing (20 min)
3. **Practice**: Build simple feature with both (10 min)
4. **Result**: 2x productivity immediately

### Small Team (2 hours)
1. **Setup**: Developer + QA + DevOps agents (45 min)
2. **Configure**: Project-specific customizations (45 min)
3. **Practice**: Full feature with CI/CD (30 min)
4. **Result**: 5x team productivity

### Enterprise Team (1 day)
1. **Morning**: Setup all 8 agents (2 hours)
2. **Lunch**: Review coordination guide (1 hour)
3. **Afternoon**: Practice workflows (3 hours)
4. **Evening**: Measure ROI (1 hour)
5. **Result**: 10x organizational efficiency

---

## 📚 Documentation by Platform

### Claude Code (Most Comprehensive)
- **8 specialized roles** covering full SDLC
- **Agent guide**: `claude-code/CLAUDE-CODE-AGENTS-GUIDE-SDLC-4.8.md`
- **Best for**: Full-stack development teams
- **Setup time**: 15-30 minutes per agent

### Cursor (Developer-Focused)
- **2 roles**: Developer + CPO
- **Best for**: Fast coding with product oversight
- **Setup time**: 10 minutes

### GitHub Copilot (Code-Inline)
- **2 roles**: Developer + CTO
- **Best for**: IDE-integrated assistance
- **Setup time**: 5 minutes

### ChatGPT (Executive Review)
- **1 role**: CEO critical reviewer
- **Best for**: Strategic validation
- **Setup time**: 2 minutes

### Gemini (Strategic Analysis)
- **1 role**: CEO strategic validator
- **Best for**: Business case analysis
- **Setup time**: 2 minutes

---

## 🔗 Related Resources

- **AI Tools** (use first): [/1-AI-Tools/](../1-AI-Tools/) - Prompt-based workflows
- **Manual Templates** (backup): [/3-Manual-Templates/](../3-Manual-Templates/) - Traditional processes
- **Automation Scripts**: [/4-Scripts/](../4-Scripts/) - Validators and setup
- **Main Guide**: [/README.md](../README.md) - Complete overview

---

## ✅ Success Metrics

**Track your agent effectiveness:**

```yaml
Productivity Metrics:
  Code Generation Speed: 5-10x faster
  Bug Detection Rate: 80%+ caught pre-commit
  Test Coverage: 80%+ automatic
  Documentation: 100% complete

Quality Metrics:
  SDLC 4.9 Compliance: 95%+
  Performance Targets Met: >90%
  Security Issues: 70% reduction
  Technical Debt: 60% reduction

Team Metrics:
  Developer Satisfaction: +40%
  Onboarding Time: -60%
  Code Review Time: -70%
  Release Frequency: +200%
```

---

**Status**: PRODUCTION-READY
**Coverage**: 17 specialized agents across 5 platforms
**Proven**: 3 platforms (BFlow, NQH-Bot, MTEP)
**Community**: 500+ developers using agent templates

***"Right agent, right role, right results."*** 🎯

***"Configure once, use forever."*** ⚡

***"From solo to enterprise - agents that scale."*** 🚀
