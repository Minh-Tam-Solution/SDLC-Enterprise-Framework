# AI CODEX SYSTEM PROMPT INTEGRATION GUIDE

## SDLC 4.4 Adaptive Governance Framework (Adaptive Governance + Predictive Integrity)

**Version**: 4.4  
**Date**: September 16, 2025  
**Status**: ACTIVE  
**Framework**: SDLC 4.4 Adaptive Governance Framework (DFT)  
**Compliance**: MANDATORY  

---

## 🎯 **OVERVIEW**

This guide provides comprehensive instructions for integrating AI Codex system prompts into any project using the SDLC 4.4 Adaptive Governance Framework. Version 4.4 introduces integrity instrumentation (continuity scoring + hash chain), drift detection lifecycle, KPI governance enforcement, structured override protocol, gating mode evolution, and predictive readiness index. These capabilities extend the earlier design-first and role-based standards into measurable adaptive governance.

---

## 🔄 4.4 UPGRADE DELTA (FROM 4.2 / 4.3)

| Capability | Pre‑4.4 State | 4.4 Enhancement | Prompt Integration Requirement |
|------------|---------------|-----------------|-------------------------------|
| Integrity / Continuity | None / manual recency awareness | Automated continuity score (freshness, coverage, orphan, chain) | Surface continuity score context in system prompts |
| Drift Detection | Not present | Shadow → Advisory → Enforced → Adaptive scanner | Include latest drift anomalies & suppression rationale |
| KPI Governance | Ad hoc quality metrics | Central KPI catalog + compliance gate | Provide KPI compliance % & failing KPIs in prompt pre-merge |
| Overrides | Informal decisions | Dual approval, time‑boxed ledger | Instruct AI not to suggest override unless evidence & escalation path supplied |
| Gating Modes | Static quality gates | Mode flag (shadow/advisory/enforced/adaptive) | AI behavior must adapt to current gating mode |
| Readiness Index | N/A | Composite: continuity + drift stability + KPI + override density | Include readiness_index.json summary into context |
| Audit Chain | Logs scattered | Hash‑chained JSONL events | AI must append structured event notes (no mutation of prior entries) |
| Certification Tiers | Compliance % only | Tiered adoption maturity | Show current tier + next tier gap analysis |

### Environment Variables (New / Standardized)

```bash
export GOVERNANCE_GATING_MODE=shadow   # shadow|advisory|enforced|adaptive
export CONTINUITY_BASELINE_PATH=.adaptive/continuity/baseline.json
export DRIFT_REPORT_PATH=.adaptive/drift/latest_report.json
export KPI_CATALOG_PATH=config/kpis/catalog.yaml
export KPI_COMPLIANCE_REPORT=.adaptive/kpi/kpi_compliance.json
export OVERRIDE_LEDGER_PATH=.adaptive/overrides/override_ledger.jsonl
export READINESS_INDEX_PATH=.adaptive/readiness/readiness_index.json
export INTEGRITY_CHAIN_LOG=.adaptive/integrity/deployment_integrity.jsonl
```

### Minimum Prompt Context (Inject Pre-Task)

Provide the AI agent with a structured system preamble fragment:

```json
{
   "governance": {
      "gating_mode": "shadow",
      "continuity_score": 0.68,
      "drift_anomalies": 3,
      "kpi_compliance_pct": 82.5,
      "override_active": false,
      "readiness_index": 0.61,
      "certification_tier": "Tier-2 (Emerging)"
   }
}
```

AI must treat continuity_score < 0.70 or kpi_compliance_pct < target as a signal to prioritize remediation over feature acceleration unless an approved override exists.

### **🏆 FRAMEWORK BENEFITS**

- **Universal Application**: Can be applied to any project type
- **Proven Methodology**: Tested and refined through BFlow development
- **AI-Native Design**: Built for AI-assisted development
- **Enterprise-Grade**: Meets enterprise quality standards
- **Scalable Architecture**: Supports projects of any size

---

## 🔬 **SDLC 4.4 ADAPTIVE FRAMEWORK PRINCIPLES**

### **PRINCIPLE 0: AI-NATIVE FOUNDATION**

- **AI Integration** from project inception
- **Agent-Driven Standardization** with production-ready agents
- **AI+Human Collaborative Methodology** for optimal development
- **Natural Language Documentation Generation** powered by AI

### **PRINCIPLE 1: SCIENTIFIC ORGANIZATION STANDARD (SOS)**

- **Level 0-1-2-3 Architecture** mandatory implementation
- **8 or fewer root directories** vs industry 15-20 average
- **Functionality-based grouping** with logical progression
- **Enterprise standard compliance** with scalability considerations

### **PRINCIPLE 2: LEGACY MANAGEMENT PROTOCOL (LMP)**

- **99-Legacy Pattern** for centralized legacy management
- **Zero knowledge loss** during reorganization
- **Pattern recognition algorithms** for legacy content
- **95%+ legacy management efficiency** target

### **PRINCIPLE 3: ZERO-DISRUPTION REORGANIZATION (ZDR)**

- **100% backward compatibility** maintained
- **Symlinks** for file location compatibility
- **Zero business disruption** guarantee
- **36,500% ROI** transformation efficiency target

### **PRINCIPLE 4: ENTERPRISE PLATFORM STANDARDS (EPS)**

- **Multi-entity support** with tenant isolation
- **Scalable architecture** for enterprise growth
- **Performance optimization** with <50ms response times
- **Security compliance** with enterprise standards

### **PRINCIPLE 5: SYSTEM THINKING INTEGRATION (STI)**

- **Cross-module dependency mapping** mandatory
- **Holistic system understanding** required
- **Integration testing** for all modules
- **End-to-end workflow** validation

### **PRINCIPLE 6: DESIGN-FIRST ENFORCEMENT (DFT)**

- **NO-DOC/NO-DESIGN = NO-MERGE** mandatory
- **Architecture Brief** required before coding
- **Sequence/Data Flow** documentation mandatory
- **API Contract** specification required
- **Stakeholder Approval** process enforced

---

## 🤖 **AI CODEX TOOLS SUPPORTED**

### **1. CLAUDE CODE - 6 SPECIALIZED ROLES (Update to 4.4 Templates)**

- **Primary Tool**: Main AI development assistant with 6 specialized roles
- **Templates**:
   - `CLAUDE-CODE-TECHNICAL-WRITER-SDLC-4.4.md.template`
   - `CLAUDE-CODE-SOFTWARE-ARCHITECT-SDLC-4.4.md.template`
   - `CLAUDE-CODE-DEVELOPER-SDLC-4.4.md.template`
   - `CLAUDE-CODE-DEVOPS-ENGINEER-SDLC-4.4.md.template`
   - `CLAUDE-CODE-QUALITY-ASSURANCE-ENGINEER-SDLC-4.4.md.template`
      - `CLAUDE-CODE-CONDUCTOR-CPO-CTO-SDLC-4.4.md.template`
   (Legacy 4.3 templates may remain in `99-legacy/` for historical diff analysis.)
- **Focus**: Documentation, implementation, quality assurance, and team orchestration
- **Integration**: SDLC Compliance Auditor Agent
- **Best For**: Specialized development tasks, documentation, testing, team coordination

### **2. CURSOR AI (CPO Governance Alignment)**

- **Primary Tool**: CPO role for code review and quality assurance
- **Template**: `CURSOR-CPO-SYSTEM-PROMPT-SDLC-4.4.md.template` (use legacy path only for migration diff)
- **Focus**: Skeptical deep review, quality gate enforcement
- **Integration**: CPO executive oversight
- **Best For**: Code review, quality assurance, strategic direction

### **3. GITHUB COPILOT (CTO Integrity & Drift Oversight)**

- **Primary Tool**: CTO role for technical leadership
- **Template**: `GITHUB-COPILOT-CTO-SYSTEM-PROMPT-SDLC-4.4.md.template`
- **Focus**: Technical excellence, security, performance
- **Integration**: CTO technical oversight
- **Best For**: Technical implementation, security compliance

---

## 📋 **IMPLEMENTATION STEPS**

### **STEP 1: PROJECT SETUP (Add Adaptive Directories)**

1. **Create Project Structure**

   ```text
   project-root/
   ├── docs/
   │   └── SDLC-Enterprise-Framework/
   │       └── 06-Templates-Tools/
   │           ├── CLAUDE-CODE-SYSTEM-PROMPT-SDLC-4.4.md.template
   │           ├── CURSOR-CPO-SYSTEM-PROMPT-SDLC-4.4.md.template
   │           ├── GITHUB-COPILOT-CTO-SYSTEM-PROMPT-SDLC-4.4.md.template
   │           └── AI-CODEX-SYSTEM-PROMPT-INTEGRATION-GUIDE.md
   ├── .adaptive/
   │   ├── continuity/
   │   ├── drift/
   │   ├── integrity/
   │   ├── kpi/
   │   └── overrides/
   ├── .claude/
   │   └── agents/
   │       └── sdlc-compliance-auditor.json
   └── [project-specific files]
   ```

2. **Copy Templates**
   - Copy all template files to your project
   - Rename templates to remove `.template` extension
   - Customize placeholders with project-specific information

### **STEP 2: CUSTOMIZE TEMPLATES (Inject Integrity Context)**

1. **Replace Placeholders**
   - `[Project Name]` → Your actual project name
   - `[Current Date]` → Current date
   - `[Next Review Date]` → Next review date
   - `[Project Type]` → Web Application/API/Mobile/etc.

2. **Customize Project-Specific Content**
   - Update project description
   - Modify technical stack information
   - Adjust business requirements
   - Configure security requirements

3. **Configure AI Agents**
   - Set up SDLC Compliance Auditor Agent
   - Configure continuity scanner & drift shadow runner integration
   - Define KPI catalog ingestion & compliance thresholds
   - Register override approval workflow (CTO + CPO dual signature)
   - Enable integrity chain appender (append-only JSONL)

### **STEP 3: INTEGRATE WITH AI TOOLS (Adaptive Governance Signals)**

1. **Claude Code Integration**
   - Use `CLAUDE-CODE-SYSTEM-PROMPT-SDLC-4.4.md`
   - Provide continuity_score, gating_mode, drift delta summary in system context
   - Include last readiness_index.json (or partial) truncated to essential fields

2. **Cursor AI Integration**
   - Use 4.4 CPO prompt
   - Feed KPI compliance report + failing KPIs list
   - Provide pending overrides requiring CPO decision

3. **GitHub Copilot Integration**
   - Use 4.4 CTO prompt
   - Inject architecture integrity / drift anomalies
   - In enforced/adaptive gating: instruct to block code suggestions that bypass design-first or reduce continuity coverage

### **STEP 4: CONFIGURE SDLC COMPLIANCE (Adaptive & Predictive)**

1. **Set Up Compliance Auditor Agent**
   - Create `.claude/agents/sdlc-compliance-auditor.json`
   - Configure project-specific compliance rules
   - Set up automated compliance checking

2. **Configure Quality & Governance Gates**
   - Map gating mode progression criteria:
     - Shadow → Advisory: continuity ≥0.60 & drift scan stable 2 runs
     - Advisory → Enforced: continuity ≥0.70 & KPI compliance ≥80% & drift FP rate <5%
     - Enforced → Adaptive: continuity ≥0.75 & KPI compliance ≥85% & drift FP rate <3% & override_density <2%
   - Automate readiness index computation each pipeline
   - Escalate gating mode changes via integrity chain event + dual approval

3. **Set Up Documentation & Evidence Standards**
   - Enforce hash-chained evidence for architecture briefs, sequence diagrams, KPI deltas
   - Auto-link code changes to continuity impacts in PR description
   - Reject merges lacking updated readiness index delta rationale (enforced/adaptive modes)

---

## 🛠️ **CONFIGURATION OPTIONS**

### **PROJECT TYPE CONFIGURATIONS**

#### **Web Application**

- **Architecture**: Monolithic or Microservices
- **Frontend**: React/Vue/Angular
- **Backend**: Node.js/Python/Java
- **Database**: PostgreSQL/MySQL/MongoDB
- **Deployment**: Docker/Kubernetes

#### **API Service**

- **Architecture**: Microservices
- **Framework**: FastAPI/Express/Spring Boot
- **Database**: PostgreSQL/Redis
- **Authentication**: JWT/OAuth2
- **Documentation**: OpenAPI 3.0

#### **Mobile Application**

- **Platform**: iOS/Android/Cross-platform
- **Framework**: React Native/Flutter/Native
- **Backend**: REST API/GraphQL
- **Database**: SQLite/Cloud Database
- **Deployment**: App Store/Play Store

### **TEAM SIZE CONFIGURATIONS (Adaptive Adjustments)**

#### **Small Team (1-5 developers)**

- **Simplified Workflow**: Core continuity + drift shadow only until stability
- **Lightweight Documentation**: Essential architecture briefs + integrity chain only
- **Direct Communication**: Gating remains shadow/advisory longer for speed
- **Quick Iterations**: Readiness index used informally (trend focus)

#### **Medium Team (6-20 developers)**

- **Standard Workflow**: Full 4.4 baseline (continuity + drift advisory)
- **Structured Documentation**: All design-first assets + KPI catalog mapping
- **Governance Escalation**: Move to enforced once continuity ≥0.70
- **Readiness Reviews**: Weekly readiness index + anomaly discussion

#### **Large Team (20+ developers)**

- **Enterprise Workflow**: Enforced → Adaptive gating progression
- **Predictive Monitoring**: Real-time continuity / drift dashboards
- **Override Governance**: Strict ledger audits (expiry & regression metrics)
- **Quarterly Tier Audit**: Certification tier recalculated + gap plan

---

## 📊 **QUALITY STANDARDS**

### **MANDATORY QUALITY & GOVERNANCE GATES (4.4)**

1. **Design Gate (Integrity Anchored)**
   - Architecture Brief complete + hash appended to integrity chain
   - Sequence/Data Flow diagrams stored & referenced in continuity coverage
   - API Contract specified (diff tracked for drift analysis)
   - Stakeholder approval obtained (logged as signed event)

2. **Code Gate (Continuity Sensitive)**
   - Code quality & security pass
   - Test coverage does not reduce continuity score trajectory
   - Drift anomalies introduced < threshold OR suppression justification documented
   - KPI impact assessment updated

3. **Documentation & Evidence Gate**
   - Documentation updated & integrity chain entry added
   - API documentation + change hash recorded
   - KPI catalog diff justification
   - Evidence chain continuity (no broken hash sequence)

4. **Deployment / Governance Gate**
   - Readiness index ≥ mode threshold
   - No critical unresolved drift anomalies (severity ≥ high)
   - Override ledger clean (no expired overrides active)
   - Monitoring covers new components (continuity coverage increment)

### **PERFORMANCE & INTEGRITY STANDARDS**

- **API Response Time**: <50ms for all endpoints
- **Database Queries**: <10ms for simple queries
- **Page Load Time**: <2s for initial load
- **Test Coverage**: 95%+ code coverage (continuity weighted)
- **Continuity Score**: ≥0.75 (target), alert if negative slope 3 consecutive runs
- **Drift False Positive Rate**: <3% in enforced/adaptive
- **Override Density**: <2% of deployments per 30-day window
- **Readiness Index**: ≥0.70 adaptive target
- **Security**: Zero vulnerabilities

---

## 🔒 **SECURITY REQUIREMENTS**

### **MANDATORY SECURITY STANDARDS**

- **Authentication**: JWT-based authentication
- **Authorization**: Role-based access control (RBAC)
- **Data Protection**: Encryption at rest and in transit
- **Audit Logging**: Comprehensive audit trails
- **Compliance**: SOC 2 Type II compliance target

### **SECURITY CHECKLIST**

- [ ] No secrets in code
- [ ] No unsafe eval usage
- [ ] Proper CORS configuration
- [ ] Auth guards implemented
- [ ] Input validation complete
- [ ] SQL injection prevention
- [ ] XSS protection enabled
- [ ] CSRF protection active

---

## 📈 **SUCCESS METRICS**

### **DEVELOPMENT METRICS (4.4)**

- **SDLC 4.4 Adaptive Compliance**: Target 90%+ (weighted by governance maturity)
- **Continuity Score**: ≥0.75 stable
- **Gating Mode Progression**: Achieve adaptive within 120 days
- **KPI Compliance**: ≥85% enforced, ≥90% adaptive
- **Drift FP Rate**: <3% adaptive
- **Override Regression Rate**: <5% (post-expiry incidents)

### **BUSINESS & GOVERNANCE METRICS**

- **Time to Market**: 50% improvement
- **Quality**: 90%+ defect-free releases
- **Performance**: <50ms response time
- **User Satisfaction**: 95%+ satisfaction rate
- **Readiness Index Trend**: Positive 3-period moving average
- **Governance Tier Advancement**: At least one tier per quarter until Tier-4

---

## 🚀 **BEST PRACTICES**

### **IMPLEMENTATION BEST PRACTICES (4.4 Augmented)**

1. **Start Small**: Begin with core features
2. **Iterate Quickly**: Fast feedback loops
3. **Document Everything**: Comprehensive documentation
4. **Test Thoroughly**: 95%+ test coverage
5. **Monitor Continuously**: Real-time monitoring (continuity + drift + readiness)
6. **Surface Integrity Early**: Always inject governance JSON before major reasoning
7. **Avoid Unnecessary Overrides**: Recommend remediation first
8. **Explain Drift Suppressions**: Provide rationale & expiry suggestion

### **MAINTENANCE BEST PRACTICES (Adaptive)**

- **Regular Updates**: Keep system prompts current
- **Continuous Improvement**: Regular process refinement
- **Team Training**: Regular team education
- **Tool Updates**: Keep AI tools updated
- **Compliance Monitoring**: Automated integrity chain + readiness index delta reviews
- **Drift Baseline Recalibration**: Quarterly or after major architecture shifts
- **KPI Catalog Hygiene**: Remove obsolete metrics; version changes

---

## 📞 **SUPPORT & ESCALATION**

### **IMMEDIATE ESCALATION TRIGGERS (Governance + Integrity)**

- **SDLC 4.4 Compliance Violations**
- **Security Vulnerabilities**
- **Performance Issues**
- **Gating Mode Regression (unexpected downgrade)**
- **Continuity Score Crash (>10% drop)**
- **Drift Critical Anomaly Unsuppressed**
- **Integrity Chain Break (hash mismatch)**
- **Documentation Gaps**

### **ESCALATION PROCESS**

1. **Identify Issue**: Document the problem
2. **Assess Impact**: Evaluate severity
3. **Escalate**: Notify appropriate stakeholders
4. **Resolve**: Implement solution
5. **Document**: Update documentation

---

## 🎯 **SUCCESS CRITERIA**

### **IMPLEMENTATION SUCCESS (Adaptive)**

- **SDLC 4.4 Compliance**: ≥90% weighted
- **Zero Unauthorized Gate Bypasses**: All gating transitions logged
- **Design-First Integrity**: All merges have architecture evidence hash
- **95%+ Team Satisfaction**: High team morale
- **Readiness Index Growth**: ≥0.15 improvement over first 90 days

### **PROJECT SUCCESS**

- **On-Time Delivery**: Meet all deadlines
- **Quality Excellence**: 95%+ defect-free
- **Performance Targets**: <50ms response time
- **User Satisfaction**: 95%+ satisfaction rate
- **Business Value**: Measurable ROI

---

**Remember**: This framework is universal and can be applied to any project. The BFlow Platform development experience has been used to refine and validate these practices, making them ready for universal application.

**Status**: ACTIVE - Adaptive Governance Enabled
**Last Updated**: [Current Date]
**Next Review**: [Next Review Date]
**Integrity Chain Ref**: (Latest entry hash here)
