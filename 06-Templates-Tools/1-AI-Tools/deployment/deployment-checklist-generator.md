# 🚀 AI Deployment Checklist Generator - Stage 05 (DEPLOY)

**Version**: 4.9.0 | **Date**: November 13, 2025 | **Stage**: 05 - DEPLOY  
**Time Savings**: 85% (4 hours → 36 minutes) | **BFlow**: Zero downtime deployments

## Universal AI Prompt
```
Generate a comprehensive deployment checklist for SDLC 4.9 Stage 05:

Feature: [Name]
Environment: [Staging/Production]
Deployment Strategy: [Blue-Green/Canary/Rolling]
Rollback Time: <5 minutes target

Include:
1. Pre-deployment checks (tests passed, approvals, backups)
2. Deployment steps (automated + manual verification)
3. Post-deployment validation (smoke tests, health checks)
4. Rollback procedure (if issues detected)
5. Communication plan (team, stakeholders, users)

BFlow standard: Zero downtime, automated rollback, complete audit trail.
```

## BFlow Example Output
**Pre-Deployment** (30 min):
- ✅ All tests passed (95%+ coverage)
- ✅ CEO/CTO approval obtained
- ✅ Database backup completed
- ✅ Rollback tested (<3 min)

**Deployment** (15 min):
- Blue-green switch via GitHub Actions
- Health checks: API, DB, Redis
- Smoke tests: 10 critical paths

**Result**: Zero downtime, 10+ successful deployments

**Related**: [rollback-plan-creator.md](./rollback-plan-creator.md)
