# MCP Integration Implementation Guide

**Version**: 6.0.3
**Date**: February 2, 2026
**Status**: ACTIVE
**Framework**: SDLC 6.0.3
**Ring**: 3 (Outer - Implementation)
**Source**: Consolidated from RFC-SDLC-603 (Boris Cherny Tactic #1)

---

## Overview

**Model Context Protocol (MCP)** enables AI coding assistants to access external tools and data sources, eliminating manual context-switching across platforms.

### Problem Addressed

Without MCP, developers spend **5-10 minutes per bug** switching contexts:
- Slack → Read bug report
- GitHub → Create issue
- Jira → Sync ticket
- Back to Slack → Acknowledge

**With MCP**: **< 1 minute** automated triage (6x faster)

### Key Capabilities

- **Automated Bug Triage**: Slack/Discord → GitHub Issues (end-to-end automation)
- **Context Enrichment**: AI analyzes full thread history + attachments
- **Evidence Audit Trail**: All MCP actions logged to Evidence Vault
- **Tool-Agnostic**: Works with Claude Code, Cursor, Copilot, any MCP-compatible AI tool

---

## Use Cases

### Use Case 1: Automated Bug Triage (6x Faster)

**Before MCP** (30 minutes):
1. User reports bug in Slack #bugs channel
2. PM reads Slack, manually creates GitHub issue
3. PM copies context, assigns to developer
4. PM posts acknowledgment in Slack
5. Developer finds issue, starts work

**After MCP** (5 minutes):
1. User reports bug in Slack
2. MCP detects message, triggers Claude analysis
3. Claude auto-creates GitHub issue with full context
4. MCP posts acknowledgment with issue link
5. Developer immediately notified

**Time Saved**: 25 minutes/bug × 50 bugs/month = **20 hours/month**

### Use Case 2: Cross-Platform Sync

**Scenario**: Support ticket in Jira needs engineering input

**MCP Workflow**:
1. Jira ticket created: "Customer reports 504 timeout"
2. MCP fetches ticket via Jira API
3. MCP creates GitHub issue with Jira link
4. Engineer fixes, closes GitHub issue
5. MCP auto-updates Jira ticket: "Fixed in v1.2.3"

**Benefit**: Zero manual sync, no tickets lost between systems

---

## Integration Patterns

### Pattern 1: Slack MCP Server

**Setup**:
```bash
# 1. Create Slack App (https://api.slack.com/apps)
# 2. Enable Event Subscriptions
# 3. Subscribe to events: message.channels, app_mention
# 4. Install app to workspace

# 5. Configure MCP Server
cat > mcp-config.json << 'EOF'
{
  "platforms": {
    "slack": {
      "enabled": true,
      "signing_secret": "YOUR_SLACK_SIGNING_SECRET",
      "bot_token": "xoxb-...",
      "channels": ["bugs", "support", "engineering"],
      "webhook_url": "https://orchestrator.example.com/api/v1/mcp/slack"
    }
  }
}
EOF
```

**Webhook Handling**:
```python
# backend/app/api/v1/endpoints/mcp_slack.py

from fastapi import APIRouter, Request, HTTPException
from app.services.mcp.slack_adapter import SlackMCPAdapter
import hmac
import hashlib

router = APIRouter()

@router.post("/mcp/slack")
async def slack_webhook(request: Request):
    # 1. Verify Slack signature (security critical)
    signature = request.headers.get("X-Slack-Signature")
    timestamp = request.headers.get("X-Slack-Request-Timestamp")
    body = await request.body()

    if not verify_slack_signature(signature, timestamp, body):
        raise HTTPException(status_code=401, detail="Invalid signature")

    # 2. Parse event
    payload = await request.json()
    event = payload.get("event", {})

    # 3. Process via MCP adapter
    adapter = SlackMCPAdapter()
    result = await adapter.process_event(event)

    return {"ok": True, "result": result}

def verify_slack_signature(signature: str, timestamp: str, body: bytes) -> bool:
    """Verify HMAC-SHA256 signature from Slack"""
    signing_secret = get_secret("SLACK_SIGNING_SECRET")
    sig_basestring = f"v0:{timestamp}:{body.decode('utf-8')}"
    computed_sig = 'v0=' + hmac.new(
        signing_secret.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(computed_sig, signature)
```

**AI Analysis**:
```python
# app/services/mcp/slack_adapter.py

async def process_event(self, event: dict):
    channel = event.get("channel")
    text = event.get("text")
    thread_ts = event.get("thread_ts") or event.get("ts")

    # 1. Fetch full thread context
    thread_history = await self.slack_client.conversations_replies(
        channel=channel,
        ts=thread_ts
    )

    # 2. AI analysis (Claude)
    analysis = await self.ai_engine.analyze_bug_report(
        text=text,
        context=thread_history
    )

    # 3. Create GitHub issue if bug confirmed
    if analysis.intent == "BUG":
        issue_url = await self.github_adapter.create_issue(
            title=analysis.title,
            body=analysis.description,
            labels=analysis.labels,
            slack_thread=f"https://slack.com/archives/{channel}/p{thread_ts}"
        )

        # 4. Post acknowledgment
        await self.slack_client.chat_postMessage(
            channel=channel,
            thread_ts=thread_ts,
            text=f"✅ Bug confirmed: {issue_url}"
        )

        # 5. Create Evidence artifact
        await self.evidence_vault.create_artifact(
            type="mcp_slack_to_github",
            source_thread=f"{channel}/{thread_ts}",
            destination_issue=issue_url,
            ai_decision=analysis.reasoning
        )

    return {"status": "processed", "intent": analysis.intent}
```

---

### Pattern 2: GitHub MCP Server

**Setup**:
```bash
# 1. Create GitHub OAuth App
# 2. Request scopes: repo, read:org, notifications
# 3. Configure MCP

cat > mcp-github.json << 'EOF'
{
  "github": {
    "enabled": true,
    "oauth_client_id": "YOUR_OAUTH_CLIENT_ID",
    "oauth_client_secret": "YOUR_SECRET",
    "repositories": [
      "org/sdlc-orchestrator",
      "org/frontend-app"
    ]
  }
}
EOF
```

**Automated PR Creation**:
```python
# app/services/mcp/github_adapter.py

async def create_issue(
    self,
    title: str,
    body: str,
    labels: list[str],
    slack_thread: str
) -> str:
    """Create GitHub issue via MCP"""

    # 1. Create issue
    issue = await self.github_client.create_issue(
        owner="org",
        repo="sdlc-orchestrator",
        title=title,
        body=f"{body}\n\n**Source**: {slack_thread}",
        labels=labels,
        assignees=await self.suggest_assignees(labels)
    )

    # 2. If simple fix, draft PR
    if await self.is_simple_fix(issue):
        pr_url = await self.draft_pr(issue)
        await self.github_client.add_comment(
            issue_number=issue.number,
            body=f"🔧 Draft PR created: {pr_url}"
        )

    return issue.html_url

async def is_simple_fix(self, issue: Issue) -> bool:
    """AI determines if issue is 1-file change"""
    analysis = await self.ai_engine.analyze_complexity(issue.body)
    return analysis.complexity == "LOW" and analysis.files_affected == 1
```

---

### Pattern 3: Jira/Linear MCP Server

**Setup**:
```bash
# Jira REST API integration
cat > mcp-jira.json << 'EOF'
{
  "jira": {
    "enabled": true,
    "base_url": "https://yourcompany.atlassian.net",
    "api_token": "YOUR_JIRA_API_TOKEN",
    "project_key": "SDLC",
    "sync_direction": "bidirectional"
  }
}
EOF
```

**Sync Workflow**:
```python
async def sync_jira_to_github(self, jira_ticket_key: str):
    """Sync Jira ticket to GitHub issue"""

    # 1. Fetch Jira ticket
    ticket = await self.jira_client.get_issue(jira_ticket_key)

    # 2. Create GitHub issue (if not exists)
    github_issue = await self.github_adapter.create_issue(
        title=f"[{jira_ticket_key}] {ticket.summary}",
        body=f"{ticket.description}\n\nJira: {ticket.url}",
        labels=["jira-sync"]
    )

    # 3. Store mapping
    await self.db.create_mapping(
        jira_key=jira_ticket_key,
        github_issue_url=github_issue.html_url
    )

    # 4. Setup webhook for bidirectional sync
    await self.jira_client.add_webhook(
        url=f"{self.base_url}/api/v1/mcp/jira/webhook",
        events=["jira:issue_updated"]
    )
```

---

## Configuration Examples

### Example 1: Multi-Platform MCP Server

**`.mcp.json`**:
```json
{
  "version": "1.0.0",
  "server": {
    "url": "https://orchestrator.example.com/api/v1/mcp",
    "auth": {
      "type": "mutual_tls",
      "cert_path": "/etc/mcp/client.crt",
      "key_path": "/etc/mcp/client.key"
    }
  },
  "platforms": {
    "slack": {
      "enabled": true,
      "signing_secret": "${SLACK_SIGNING_SECRET}",
      "bot_token": "${SLACK_BOT_TOKEN}",
      "channels": ["bugs", "support"],
      "webhook_url": "https://orchestrator.example.com/api/v1/mcp/slack"
    },
    "github": {
      "enabled": true,
      "oauth_client_id": "${GITHUB_OAUTH_CLIENT_ID}",
      "oauth_client_secret": "${GITHUB_OAUTH_SECRET}",
      "repositories": ["org/sdlc-orchestrator"]
    },
    "jira": {
      "enabled": false,
      "base_url": "https://yourcompany.atlassian.net",
      "api_token": "${JIRA_API_TOKEN}"
    }
  },
  "ai_engine": {
    "primary_provider": "ollama",
    "model": "qwen3:32b",
    "fallback_provider": "claude",
    "max_retries": 3
  },
  "evidence_vault": {
    "enabled": true,
    "store_all_mcp_actions": true
  }
}
```

---

## Security Model

### Threat Model

| Threat | Control | Implementation |
|--------|---------|----------------|
| **Spoofing** (fake webhooks) | Signature verification | HMAC-SHA256 with Slack signing secret |
| **Tampering** (malicious payloads) | Request validation | JSON schema validation + sanitization |
| **Information Disclosure** | Access control | OPA policies enforce row-level security |
| **Denial of Service** | Rate limiting | 100 req/min per platform, queue overflow |
| **Elevation of Privilege** | Least privilege | Read-only by default, explicit write scopes |

### OAuth Scopes

**GitHub**:
- `repo:write` - Create issues, PRs (explicit grant required)
- `repo:read` - Read repository metadata
- `notifications:read` - Check PR/issue status

**Slack**:
- `channels:history` - Read public channel threads
- `chat:write` - Post messages to threads
- `files:read` - Access uploaded screenshots

### Webhook Signature Verification (Required)

```python
def verify_slack_signature(signature: str, timestamp: str, body: bytes) -> bool:
    """HMAC-SHA256 signature verification"""
    # Check timestamp freshness (prevent replay attacks)
    if abs(time.time() - int(timestamp)) > 300:  # 5 min window
        return False

    # Compute expected signature
    signing_secret = get_secret("SLACK_SIGNING_SECRET")
    sig_basestring = f"v0:{timestamp}:{body.decode('utf-8')}"
    expected = 'v0=' + hmac.new(
        signing_secret.encode(),
        sig_basestring.encode(),
        hashlib.sha256
    ).hexdigest()

    # Constant-time comparison (prevent timing attacks)
    return hmac.compare_digest(expected, signature)
```

**Mutual TLS (mTLS)** for MCP server ↔ GitHub API:
```yaml
# docker-compose.yml
services:
  mcp-server:
    environment:
      - TLS_CERT=/etc/mcp/client.crt
      - TLS_KEY=/etc/mcp/client.key
      - TLS_CA=/etc/mcp/ca.crt
```

---

## Error Handling & Escalation

### Common Errors

| Error | Handling | Example |
|-------|----------|---------|
| **Ambiguous Intent** | Ask clarifying question | "Is this a bug or feature request?" |
| **Missing Context** | Request more info | "Can you provide error logs?" |
| **Rate Limit Hit** | Queue with backoff | Retry after 60s |
| **API Timeout** | Exponential backoff | 3 retries: 5s, 10s, 20s |
| **Auth Failure** | Notify admin | Private channel alert |

### Escalation Path

```
Error → Auto-retry (max 3x) → Queue for human → Admin notification → Manual intervention
```

**Implementation**:
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=5, max=20)
)
async def call_external_api(url: str):
    response = await httpx.get(url)
    response.raise_for_status()
    return response.json()
```

---

## Tool-Agnostic Implementation

### Works with Any AI Tool

| AI Tool | Integration Method | MCP Support |
|---------|-------------------|-------------|
| **Claude Code** | Native MCP support | ✅ Built-in |
| **Cursor IDE** | Custom MCP server | ✅ Extensions |
| **GitHub Copilot** | GitHub Actions | ⚠️ Indirect (via Actions) |
| **Ollama** (local) | HTTP MCP bridge | ✅ `localhost:11434/mcp` |
| **Gemini Pro** | Vertex AI adapter | ✅ Cloud Run |

**Key Principle**: MCP is a **protocol**, not a product. Any AI tool can implement an MCP client.

### No Vendor Lock-In

**Portability Checklist**:
- ✅ MCP server is open-source (Apache-2.0 license)
- ✅ Configuration is JSON (no proprietary format)
- ✅ APIs are REST/GraphQL (standard protocols)
- ✅ Evidence format is JSON (no binary blobs)

**Migration Path**:
```
Orchestrator MCP → Custom MCP → Third-party MCP → No MCP (manual fallback)
```

Each step is **reversible** without data loss.

---

## Integration with SDLC Framework

### Stage 07 (Operate) Alignment

MCP integration fits **Stage 07 (Operate)**:
- **Purpose**: Continuous operations, incident response, bug triage
- **When**: Post-launch, during production support
- **Who**: DevOps, Support, QA teams

**Stage 07 Artifacts Enhanced**:
- Incident reports (auto-generated from Slack/Discord)
- Runbooks (AI-assisted troubleshooting)
- Post-mortems (Evidence Vault references)

### Evidence Vault Audit Trail

Every MCP action creates an Evidence artifact:
```json
{
  "manifest_id": "MANIFEST-2026-03-001",
  "artifacts": [
    {
      "artifact_id": "EVD-2026-03-001",
      "type": "mcp_slack_to_github",
      "source_platform": "slack",
      "source_thread": "https://slack.com/archives/C123/p456",
      "destination_platform": "github",
      "destination_issue": "https://github.com/org/repo/issues/123",
      "action": "create_issue",
      "ai_model": "claude-sonnet-4-5",
      "ai_decision": "Bug confirmed: token expiry on mobile Safari",
      "timestamp": "2026-03-03T10:15:00Z",
      "signature": "ed25519:..."
    }
  ]
}
```

**Traceability**: Slack thread → GitHub issue → PR → Deploy → Slack resolution

---

## Success Metrics

### Time Savings

| Metric | Before MCP | After MCP | Savings |
|--------|-----------|-----------|---------|
| **Bug triage time** | 30 min | 5 min | **25 min/bug** |
| **Monthly bugs** | 50 | 50 | - |
| **Time saved/month** | - | - | **20 hours** |
| **ROI** | - | 2 months | - |

### Quality Improvements

- **Zero lost tickets**: All Slack bugs auto-synced to GitHub
- **Faster response**: 5 min acknowledgment (vs 2-4 hours manual)
- **Complete context**: Full thread history included in GitHub issues
- **Audit trail**: Evidence Vault tracks all MCP actions (compliance)

---

## References

### Framework Documents

- [Context Management](../03-AI-Governance/05-Context-Management.md) - AGENTS.md and context files
- [Stage 07 (Operate)](../02-Core-Methodology/SDLC-Stage-07-Operate.md) - Operations and incident response
- [Evidence Vault Standards](../02-Core-Methodology/Evidence-Vault-Standards.md) - Audit trail requirements

### External Resources

- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification) - Official MCP spec
- [Slack Events API](https://api.slack.com/events-api) - Slack webhook documentation
- [GitHub REST API](https://docs.github.com/en/rest) - GitHub API reference
- [Jira REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) - Jira integration

### Related Patterns

- [Git Workflow Patterns](../04-AI-Tools-Landscape/best-practices-2026/04-git-workflow-patterns.md) - Parallel development patterns
- [Sub-agent Orchestration](../04-AI-Tools-Landscape/best-practices-2026/03-sub-agent-orchestration.md) - Research delegation patterns

---

**Document Status**: ACTIVE
**Created**: February 2, 2026
**Framework**: SDLC 6.0.3
**Ring**: 3 (Outer - Implementation)
**Source**: Consolidated from RFC-SDLC-603 (Boris Cherny Tactic #1)
**Owner**: Engineering + DevOps Teams
**Approval**: CTO @nqh ✅
