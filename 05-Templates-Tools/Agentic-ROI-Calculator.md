---
title: "Agentic ROI Calculator"
version: "6.3.1"
ring: 2
sdlc_version: "6.3.1"
last_updated: "2026-03-18"
status: "ACTIVE"
---

# Agentic ROI Calculator

> **Ring 2 (Governance)** — Template for measuring AI agent return on investment.

## 1. Core ROI Formula

```
Agent ROI = (Time Saved × Hourly Rate) / Agent Cost

Where:
  Time Saved = (Manual Hours - Agent-Assisted Hours) per period
  Hourly Rate = Fully-loaded cost (salary + benefits + overhead)
  Agent Cost  = API costs + infrastructure + maintenance per period
```

## 2. Measurement Template

| Variable | Description | How to Measure | Example |
|----------|------------|---------------|---------|
| `manual_hours` | Hours without AI | Time tracking (before adoption) | 40 hrs/month |
| `assisted_hours` | Hours with AI | Time tracking (after adoption) | 15 hrs/month |
| `hourly_rate` | Fully-loaded cost/hour | Finance team provides | $75/hr |
| `api_cost` | Monthly API/token costs | Provider billing | $200/month |
| `infra_cost` | Monthly infrastructure | Cloud billing | $50/month |
| `maintenance_hours` | Hours maintaining AI tooling | Team estimate | 5 hrs/month |

### Example Calculation

```
Time Saved     = 40 - 15 = 25 hours/month
Dollar Saved   = 25 × $75 = $1,875/month
Total Cost     = $200 + $50 + (5 × $75) = $625/month
Net Benefit    = $1,875 - $625 = $1,250/month
ROI            = $1,250 / $625 = 200%
Payback Period = $625 / $1,250 = 0.5 months
```

## 3. Output Volume Metric

> "AI enables productivity primarily through greater output — more features shipped, more bugs fixed — rather than simply doing the same work faster."

| Metric | Description | Target |
|--------|------------|--------|
| Features shipped/sprint | Completed features | +30% vs baseline |
| Bugs fixed/sprint | Resolved issues | +50% vs baseline |
| "New work" tasks | Tasks that wouldn't exist without AI | Track count (industry avg: 27%) |
| Papercuts fixed | Minor improvements typically deprioritized | Track count |

## 4. Productivity Paradox Detection

**Warning signs**:
- Productivity ↑ but revenue flat → Building faster, but building wrong things
- Time saved but not reinvested → Efficiency without strategy
- Individual productivity ↑ but team velocity flat → Coordination overhead eating gains

**Diagnostic**: If ROI >100% but business KPIs flat, investigate: Is saved time being reinvested in high-value work?

## 5. Cost Comparison Worksheet

| Dimension | Manual | Agent-Assisted | Fully Autonomous |
|-----------|--------|---------------|-----------------|
| Time per task | __ hrs | __ hrs | __ hrs |
| Error rate | __% | __% | __% |
| Review overhead | 0 hrs | __ hrs | __ hrs |
| Setup cost (one-time) | $0 | $__ | $__ |
| Ongoing cost/month | $__ | $__ | $__ |
| Net monthly benefit | Baseline | $__ | $__ |

---

## Further Reading

- Anthropic: "2026 Agentic Coding Trends Report" — Trend 6
- McKinsey: "AI adds $4.4T to global economy"

---

**Framework Version**: SDLC 6.3.1 | **Last Updated**: March 18, 2026
