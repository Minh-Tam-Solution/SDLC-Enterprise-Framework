# SDLC Observability Checklist

**Version**: 5.0.0
**Date**: December 5, 2025
**Stage**: 02 - Core Methodology (Governance & Compliance)
**Status**: ACTIVE - Production Standard
**Authority**: CTO Office
**Industry Standards**: Google SRE, DORA, OpenTelemetry

---

## Purpose

Define **observability requirements** for production systems. Observability answers: "What is happening in my system and why?"

---

## Three Pillars of Observability

```
┌─────────────────────────────────────────────────────────────────┐
│                    OBSERVABILITY                                │
├─────────────────┬─────────────────┬─────────────────────────────┤
│    METRICS      │     LOGS        │         TRACES              │
│  (Numbers)      │   (Events)      │       (Request Flow)        │
├─────────────────┼─────────────────┼─────────────────────────────┤
│ Request rate    │ Error messages  │ Cross-service request path  │
│ Error rate      │ Audit events    │ Latency breakdown           │
│ Latency (p50,   │ Debug info      │ Dependency mapping          │
│  p95, p99)      │ Security events │ Bottleneck identification   │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

---

## Observability Requirements by Tier

### LITE Tier (1-2 people)

```yaml
Metrics:
  - Not required (basic cloud provider metrics acceptable)

Logging:
  - Console logging (structured recommended)
  - Cloud provider log aggregation (if applicable)

Tracing:
  - Not required

Alerting:
  - Email notifications for critical errors (optional)
```

### STANDARD Tier (3-10 people)

```yaml
Metrics:
  - Application health metrics
  - Request/response counts
  - Basic latency tracking
  Tools: CloudWatch, Datadog basic, Prometheus (simple)

Logging:
  - Structured logging (JSON)
  - Log levels (DEBUG, INFO, WARN, ERROR)
  - Centralized log aggregation
  Tools: CloudWatch Logs, Papertrail, Loki

Tracing:
  - Optional but recommended for microservices

Alerting:
  - Error rate spikes
  - Health check failures
  - Resource exhaustion (disk, memory)
  Channels: Email, Slack
```

### PROFESSIONAL Tier (10-50 people)

```yaml
Metrics (RED Method):
  Rate:
    □ Request rate (req/sec)
    □ Request rate by endpoint
    □ Request rate by status code
  Errors:
    □ Error rate (%)
    □ Error rate by type
    □ 5xx vs 4xx breakdown
  Duration:
    □ Latency p50, p95, p99
    □ Latency by endpoint
    □ Latency by dependency

  Business Metrics:
    □ Active users
    □ Transaction volume
    □ Feature usage

  Tools: Prometheus + Grafana, Datadog, New Relic

Logging:
  Required Fields:
    □ timestamp (ISO 8601)
    □ level (DEBUG/INFO/WARN/ERROR)
    □ service_name
    □ trace_id (correlation)
    □ user_id (if applicable)
    □ request_id
    □ message
    □ error (stack trace for errors)

  Format: JSON (machine-parseable)
  Retention: 30 days minimum
  Tools: ELK Stack, Loki + Grafana, Datadog Logs

Tracing:
  Required: YES (for distributed systems)
  Coverage: All service-to-service calls
  Sampling: 100% for errors, 10% for success
  Tools: Jaeger, Zipkin, Datadog APM, OpenTelemetry

Alerting:
  SLO-Based:
    □ Error budget consumption
    □ Latency SLO breach
    □ Availability SLO breach

  Infrastructure:
    □ CPU > 80% for 5 min
    □ Memory > 85% for 5 min
    □ Disk > 90%
    □ Pod restarts > 3 in 10 min

  Channels: PagerDuty/Opsgenie, Slack, Email
  Escalation: Defined on-call rotation
```

### ENTERPRISE Tier (50+ people)

```yaml
All PROFESSIONAL requirements, PLUS:

Metrics:
  Custom Business Metrics:
    □ Revenue impact metrics
    □ Customer journey metrics
    □ SLA compliance tracking

  Capacity Planning:
    □ Growth projections
    □ Resource utilization trends
    □ Cost per transaction

Logging:
  Audit Logging:
    □ All authentication events
    □ All authorization decisions
    □ All data access (sensitive)
    □ All configuration changes

  Compliance:
    □ Immutable audit trail
    □ Log integrity verification
    □ Retention per compliance (7 years for finance)

Tracing:
  Full Coverage:
    □ 100% sampling for all requests
    □ Cross-team trace correlation
    □ Business transaction tracing

Alerting:
  Advanced:
    □ Anomaly detection (ML-based)
    □ Predictive alerting
    □ Correlation across services
    □ Automated incident creation

Dashboards:
  Required:
    □ Executive dashboard (business metrics)
    □ SRE dashboard (SLOs, error budgets)
    □ Per-service dashboards
    □ Dependency health dashboard
```

---

## Gate-Specific Observability Requirements

### G2 (Design Ready)

```yaml
Observability Design:
  □ Metrics strategy defined
  □ Logging format standardized
  □ Tracing approach documented
  □ Alerting strategy defined
  □ SLOs proposed
```

### G3 (Ship Ready)

```yaml
Observability Checklist:
  □ Metrics collecting correctly
  □ Logs flowing to aggregator
  □ Traces connecting across services
  □ Alerts configured and tested
  □ Dashboards created
  □ Runbooks documented
  □ On-call rotation established (PROFESSIONAL+)

Test Observability:
  □ Generate test error → appears in logs
  □ Generate high latency → metric reflects
  □ Cross-service call → trace connected
  □ Trigger alert condition → notification received
```

---

## Metrics Implementation

### RED Method (Recommended)

```yaml
For Every Service, Track:

Rate:
  http_requests_total{service, method, endpoint, status}

  Example PromQL:
    rate(http_requests_total{service="api"}[5m])

Errors:
  http_requests_total{status=~"5.."}
  http_errors_total{service, error_type}

  Example PromQL:
    rate(http_requests_total{status=~"5.."}[5m]) /
    rate(http_requests_total[5m])

Duration:
  http_request_duration_seconds{service, method, endpoint}

  Example PromQL:
    histogram_quantile(0.95,
      rate(http_request_duration_seconds_bucket[5m]))
```

### Custom Business Metrics

```yaml
Examples:
  # User activity
  active_users_total{tier, region}

  # Business transactions
  transactions_total{type, status}
  transaction_value_total{currency}

  # Feature adoption
  feature_usage_total{feature, action}
```

---

## Logging Implementation

### Structured Log Format

```json
{
  "timestamp": "2025-12-05T10:30:45.123Z",
  "level": "ERROR",
  "service": "api-gateway",
  "trace_id": "abc123xyz",
  "span_id": "def456",
  "request_id": "req-789",
  "user_id": "user-123",
  "method": "POST",
  "path": "/api/v1/orders",
  "status_code": 500,
  "duration_ms": 234,
  "message": "Failed to process order",
  "error": {
    "type": "DatabaseError",
    "message": "Connection timeout",
    "stack": "..."
  },
  "context": {
    "order_id": "order-456",
    "amount": 99.99
  }
}
```

### Log Levels

```yaml
DEBUG:
  - Detailed diagnostic information
  - Variable values, function entry/exit
  - Disabled in production (unless troubleshooting)

INFO:
  - Normal operation events
  - Request received, processed successfully
  - Business events (order created, user signed up)

WARN:
  - Unexpected but recoverable situations
  - Deprecated feature usage
  - Approaching resource limits

ERROR:
  - Failure requiring attention
  - Request failed, exception caught
  - Always includes stack trace

FATAL/CRITICAL:
  - Application cannot continue
  - Immediate attention required
  - Triggers alert
```

---

## Tracing Implementation

### OpenTelemetry Example

```python
# Python with OpenTelemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Initialize
provider = TracerProvider()
provider.add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint="http://jaeger:4317"))
)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)

# Usage
@tracer.start_as_current_span("process_order")
def process_order(order_id: str):
    span = trace.get_current_span()
    span.set_attribute("order.id", order_id)

    with tracer.start_as_current_span("validate_order"):
        validate(order)

    with tracer.start_as_current_span("charge_payment"):
        charge(order.payment)
```

### Trace Context Propagation

```yaml
Required Headers:
  - traceparent: W3C Trace Context
  - tracestate: Optional vendor-specific

Example:
  traceparent: 00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01

Propagate through:
  - HTTP headers
  - Message queue metadata
  - gRPC metadata
```

---

## Alerting Strategy

### Alert Categories

```yaml
Page (Wake someone up):
  - Service completely down
  - Error rate > 10% for 5 minutes
  - P0 SLO breach
  - Security incident detected

Ticket (Fix during business hours):
  - Error rate > 5% for 15 minutes
  - Latency p95 > SLO for 30 minutes
  - Resource usage > 80%
  - Certificate expiring in 30 days

Log (Informational):
  - Deployment completed
  - Scaling events
  - Warning conditions
```

### Alert Template

```yaml
Alert Name: [Service] [Metric] [Condition]
Severity: Critical/Warning/Info
Condition: [PromQL or metric condition]
Duration: [How long before firing]
Runbook: [Link to runbook]
Escalation: [On-call → Team Lead → Manager]

Example:
  Name: API Gateway Error Rate High
  Severity: Critical
  Condition: rate(http_errors_total[5m]) / rate(http_requests_total[5m]) > 0.1
  Duration: 5 minutes
  Runbook: https://wiki/runbooks/api-gateway-errors
  Escalation: On-call → API Team Lead → CTO
```

---

## Dashboards

### Required Dashboards (PROFESSIONAL+)

```yaml
1. Service Health Dashboard:
   - Request rate (current vs baseline)
   - Error rate (with target line)
   - Latency percentiles (p50, p95, p99)
   - Active instances/pods
   - Resource utilization

2. SLO Dashboard:
   - Error budget remaining
   - SLO compliance over time
   - Burn rate
   - Time to SLO breach

3. Dependency Dashboard:
   - Downstream service health
   - Database connection pool
   - Cache hit rate
   - External API latency

4. Business Dashboard (ENTERPRISE):
   - Active users
   - Transaction volume
   - Revenue metrics
   - Feature adoption
```

---

## Runbooks

### Runbook Template

```markdown
# Runbook: [Alert Name]

## Overview
- **Service**: [Service name]
- **Alert**: [Alert condition]
- **Impact**: [User/business impact]
- **Owner**: [Team/individual]

## Symptoms
- [What you'll see]
- [Related metrics/logs]

## Diagnosis Steps
1. Check [specific metric/log]
2. Verify [dependency/service]
3. Look for [common cause]

## Resolution Steps

### Scenario A: [Common cause 1]
1. [Step 1]
2. [Step 2]
3. [Verification]

### Scenario B: [Common cause 2]
1. [Step 1]
2. [Step 2]

## Escalation
- If not resolved in 15 min: [Contact]
- If customer impact: [Notify]

## Post-Incident
- [ ] Update incident log
- [ ] Schedule post-mortem if needed
- [ ] Update this runbook if new cause found
```

---

**Document Status**: ACTIVE
**Compliance**: MANDATORY for PROFESSIONAL+ tiers
**Last Updated**: December 5, 2025
**Owner**: CTO Office
