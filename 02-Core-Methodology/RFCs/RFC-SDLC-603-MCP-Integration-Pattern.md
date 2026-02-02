# RFC-SDLC-603: MCP Integration Pattern

**Status**: 📋 DRAFT
**Created**: March 3, 2026
**Author**: Framework Architect
**Sprint**: 143 - Framework-First Track 1
**Related**: Boris Cherny Tactics Analysis (Gap #1 - MCP Integration)
**Framework Version**: SDLC 6.0.3

---

## 1. Problem Statement

### Current Challenge

Modern software development teams face a **context-switching problem** when managing bug reports, feature requests, and incidents across multiple communication platforms (Slack, Discord, Microsoft Teams) and issue tracking systems (GitHub Issues, Jira, Linear). The typical workflow involves:

1. User reports bug in Slack #bugs channel
2. Developer manually creates GitHub issue
3. Developer copies context from Slack thread
4. Developer works on fix, creates PR
5. Developer manually updates Slack thread with PR link
6. After merge, developer manually closes thread

This manual process introduces:
- **Context loss**: Information scattered across platforms
- **Time waste**: 5-10 minutes per bug for context switching
- **Missed updates**: Teams forget to close Slack threads
- **Duplicate work**: Same bug reported in multiple places
- **Delayed response**: Hours/days between report and acknowledgment

### Boris Cherny Insight

Boris Cherny (creator of Claude Code, 4M views) recommends:
> "Bật Slack MCP, dán luồng thảo luận lỗi và nói 'fix'. Đừng quản lý vi mô."
> (Translation: "Enable Slack MCP, paste bug discussion thread, and say 'fix'. Don't micromanage.")

The key insight: **AI should automate the entire bug-fixing pipeline**, not just write code. This requires integration between chat platforms, issue trackers, and version control via MCP (Model Context Protocol).

### Gap Analysis (from Boris Cherny Tactics Study)

**Current State** (SDLC Orchestrator v1.6.0):
- ❌ No MCP (Model Context Protocol) integration
- ❌ No Slack/Discord bot for bug reports
- ✅ Manual bug tracking via GitHub Issues (standard workflow)
- ✅ MCP reference architecture exists (SDLC 6.0.2 OUTER RING)
- ✅ Security controls documented (Mutual TLS, token TTL)
- ❌ No actual MCP server implementation

**Industry Practice** (60K+ repos):
- Standard: Manual issue creation from chat
- Advanced: Zapier/Make automation (limited, no AI)
- Best-in-class: Cursor IDE MCP (GitHub only)

**Competitive Advantage**: Full MCP integration with Evidence Vault audit trail

---

## 2. Current State Analysis

### Existing Infrastructure

**What We Have**:
- FastAPI backend with REST APIs
- GitHub OAuth integration (authentication)
- Evidence Vault (MinIO S3 + audit trail)
- OPA Policy Engine (authorization)
- PostgreSQL database (metadata storage)

**What We're Missing**:
- MCP server implementation
- Chat platform webhooks (Slack, Discord)
- Issue tracker integration beyond read-only (GitHub API write)
- Real-time notification system

### Reference Architecture (from SDLC 6.0.2)

From `CLAUDE.md` lines 458-478 (MCP reference):
```yaml
MCP Status:
  Reference Architecture: ✅ (SDLC 6.0.2 documentation)
  Security Controls: ✅ (Mutual TLS, audit logging)
  Configuration: ✅ (.mcp.json template)
  CLI Commands: ✅ (sdlcctl mcp serve, auth issue/renew)
  Implementation: ❌ (no actual MCP server running)
  OPA MCP: ❌ (only HTTP API integration)
  MinIO MCP: ❌ (only HTTP API calls)
```

The reference architecture exists but is **not implemented**.

---

## 3. Proposed Pattern

### 3.1 MCP Integration Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│ CHAT PLATFORMS (External)                                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐                         │
│  │  Slack   │ │ Discord  │ │  Teams   │                         │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘                         │
│       │            │            │                                │
│       └────────────┴────────────┘                                │
│                    │                                             │
│              MCP Webhook Ingress                                 │
├─────────────────────────────────────────────────────────────────┤
│ MCP SERVER (SDLC Orchestrator - New Component)                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │ MCP Router                                                │   │
│  │  - Platform detection (Slack/Discord/Teams)               │   │
│  │  - Message parsing (thread ID, author, content)           │   │
│  │  - Intent classification (bug/feature/question)           │   │
│  │  - Security validation (HMAC signature verify)            │   │
│  └──────────────────┬───────────────────────────────────────┘   │
│                     │                                            │
│  ┌──────────────────▼───────────────────────────────────────┐   │
│  │ AI Context Engine                                         │   │
│  │  - Thread context retrieval (full conversation)           │   │
│  │  - Semantic analysis (Claude/GPT-4o)                      │   │
│  │  - Action recommendation (create issue / draft PR / ask)  │   │
│  └──────────────────┬───────────────────────────────────────┘   │
│                     │                                            │
│  ┌──────────────────▼───────────────────────────────────────┐   │
│  │ Workflow Orchestrator                                     │   │
│  │  1. Create GitHub issue (with labels, assignee)           │   │
│  │  2. Generate Evidence artifact (audit trail)              │   │
│  │  3. Draft PR (if simple fix, 1-file change)               │   │
│  │  4. Post acknowledgment to chat (with links)              │   │
│  └──────────────────┬───────────────────────────────────────┘   │
│                     │                                            │
├─────────────────────┴───────────────────────────────────────────┤
│ INTEGRATION LAYER (Existing SDLC Components)                    │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐              │
│  │ GitHub API  │ │Evidence Vault│ │   OPA       │              │
│  │ (Issues/PRs)│ │ (Audit Trail)│ │ (Policies)  │              │
│  └─────────────┘ └─────────────┘ └─────────────┘              │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Supported Integrations

| Platform | Integration Type | Capabilities | Priority |
|----------|------------------|--------------|----------|
| **Slack MCP** | Webhooks + Events API | Read threads, post messages, create threads | P0 |
| **GitHub MCP** | REST API + GraphQL | Create issues, draft PRs, auto-assign | P0 |
| **Discord MCP** | Bot + Webhooks | Read threads, post messages | P1 |
| **Jira MCP** | REST API | Create tickets, sync status | P1 |
| **Linear MCP** | GraphQL | Create issues, sync cycle | P2 |
| **Microsoft Teams MCP** | Graph API | Read threads, post messages | P2 |

### 3.3 Workflow Example: Slack Bug Report → GitHub Issue → PR

**Step-by-Step Flow**:

1. **User reports bug in Slack**:
   ```
   [#bugs channel]
   @user: "Login button doesn't work on mobile Safari. Error: 'token expired'"
   ```

2. **MCP triggers Claude analysis**:
   - Slack webhook notifies MCP server
   - MCP fetches full thread context (including screenshots, stack traces)
   - Claude analyzes: "Authentication token expiry issue on mobile Safari"
   - Intent: **BUG** (not question, not feature request)

3. **MCP creates GitHub issue**:
   ```yaml
   Title: "Login fails on mobile Safari: token expired"
   Body: |
     ## Bug Report (via Slack MCP)

     **Reporter**: @user (Slack)
     **Platform**: Mobile Safari
     **Error**: token expired

     ## Context
     [Link to Slack thread: https://slack.com/archives/...]

     ## Reproduction Steps
     1. Open app on mobile Safari
     2. Wait 16+ minutes (token expiry)
     3. Click login button
     4. Observe error

     ## Evidence
     - Screenshot: [attached]
     - Thread: [Slack #bugs]
   Labels: bug, mobile, authentication
   Assignee: @backend-team
   ```

4. **Evidence Vault creates audit artifact**:
   ```json
   {
     "artifact_id": "EVD-2026-03-001",
     "type": "mcp_automation",
     "source": "slack",
     "action": "create_github_issue",
     "issue_url": "https://github.com/org/repo/issues/123",
     "slack_thread": "https://slack.com/archives/C123/p456",
     "timestamp": "2026-03-03T10:15:00Z",
     "signature": "ed25519:..."
   }
   ```

5. **Claude drafts PR (if simple fix)**:
   - If issue is 1-file change (e.g., increase token TTL in config)
   - MCP creates draft PR with fix + test
   - Links PR to issue

6. **MCP posts acknowledgment to Slack**:
   ```
   [@claude-bot in #bugs]
   "✅ Bug confirmed and issue created: #123

   📝 GitHub Issue: https://github.com/org/repo/issues/123
   🔧 Draft PR: https://github.com/org/repo/pull/124
   👀 Assigned to: @backend-team

   Estimated fix time: 2 hours (based on similar issues)"
   ```

7. **Human reviews and approves**:
   - Backend engineer reviews PR
   - Makes adjustments if needed
   - Approves and merges

8. **MCP closes loop**:
   - Detects PR merge
   - Posts to Slack: "✅ Bug fixed in v1.2.3"
   - Updates GitHub issue status
   - Creates Evidence artifact for resolution

**Total Time**: 5 minutes (vs 30 minutes manual)

---

### 3.4 Security Model

**Threat Model**:
- **Spoofing**: Fake Slack webhooks
- **Tampering**: Malicious payloads
- **Repudiation**: Deny creating malicious issues
- **Information Disclosure**: Leak private Slack threads
- **Denial of Service**: Spam MCP server
- **Elevation of Privilege**: Unauthorized GitHub access

**Security Controls**:

| Control | Implementation | Status |
|---------|----------------|--------|
| **Webhook Signature Verification** | HMAC-SHA256 (Slack signing secret) | Required |
| **Mutual TLS** | mTLS for MCP → GitHub API | Required |
| **Token TTL** | 1 hour expiry, renewable | Required |
| **Least Privilege** | Read-only by default, explicit write scope | Required |
| **Rate Limiting** | 100 req/min per platform | Required |
| **Audit Logging** | All MCP calls logged to Evidence Vault | Required |
| **IP Allowlist** | Slack/GitHub IP ranges only | Recommended |
| **Secret Rotation** | 90-day webhook secret rotation | Required |

**OAuth Scopes** (GitHub):
- `repo:write` - Create issues, PRs (explicit grant)
- `repo:read` - Read repository metadata
- `notifications:read` - Check PR status

**Slack App Permissions**:
- `channels:history` - Read public channel threads
- `chat:write` - Post messages to threads
- `files:read` - Access uploaded screenshots

---

### 3.5 Error Handling

**Common Errors**:
1. **Ambiguous Intent** → Ask clarifying question in thread
2. **Missing Context** → Request more information
3. **Rate Limit Hit** → Queue and retry with backoff
4. **API Timeout** → Retry with exponential backoff (3 attempts)
5. **Authorization Failure** → Notify admin in private channel

**Escalation Path**:
```
Error → Auto-retry (3x) → Human notification → Manual intervention
```

---

## 4. Integration with SDLC Framework

### 4.1 Stage 07 (Operate) Alignment

**MCP fits into Stage 07**:
- **Purpose**: Continuous operations, incident response, bug triage
- **When**: Post-launch, during production support
- **Who**: DevOps, Support, QA teams

**Stage 07 Artifacts Enhanced**:
- Incident reports (auto-generated from Slack)
- Runbooks (AI-assisted troubleshooting)
- Post-mortems (Evidence Vault references)

### 4.2 Gate G3 (Ship Ready) Validation

**Before G3 Pass, MCP Integration Must**:
- ✅ All MCP endpoints authenticated (Mutual TLS)
- ✅ Webhook signatures verified (no bypass)
- ✅ Rate limiting enabled (prevent DoS)
- ✅ Evidence Vault integration tested (audit trail)
- ✅ OPA policies enforced (authorization)
- ✅ Penetration test passed (external firm)

**Validation Checklist**:
```yaml
- [ ] MCP Server deployment (Kubernetes, replicas=3)
- [ ] Slack app installed and verified
- [ ] GitHub OAuth app configured
- [ ] Evidence Vault storing MCP artifacts
- [ ] Prometheus metrics exported (latency, errors)
- [ ] Grafana dashboard created (MCP health)
- [ ] On-call rotation notified (MCP alerts)
```

### 4.3 Evidence Vault Audit Trail

**Every MCP Action Creates Evidence**:
```json
{
  "manifest_id": "MANIFEST-2026-03-001",
  "artifacts": [
    {
      "artifact_id": "EVD-2026-03-001",
      "type": "mcp_slack_to_github",
      "source_platform": "slack",
      "source_thread": "https://slack.com/archives/...",
      "destination_platform": "github",
      "destination_issue": "https://github.com/org/repo/issues/123",
      "action": "create_issue",
      "ai_model": "claude-sonnet-4-5",
      "ai_decision": "Bug confirmed: authentication token expiry",
      "timestamp": "2026-03-03T10:15:00Z",
      "signature_algorithm": "ed25519",
      "signature": "...",
      "previous_manifest_hash": "sha256:..."
    }
  ]
}
```

**Immutability**: Hash-chained manifests (Evidence Vault innovation)
**Traceability**: Slack thread → GitHub issue → PR → Deploy → Slack resolution
**Compliance**: HIPAA, SOC 2, GDPR audit trail

---

## 5. Tool-Agnostic Implementation

### 5.1 Works with Any AI Tool

This pattern is **NOT specific to Claude Code**. It works with:

| AI Tool | Integration Method | Example |
|---------|-------------------|---------|
| **Claude Code** (Anthropic) | MCP native support | `cursor .` with MCP config |
| **Cursor IDE** | Custom MCP server | Extensions tab |
| **GitHub Copilot** | GitHub Actions trigger | `.github/workflows/mcp.yml` |
| **OpenAI GPT-4o** | API-based MCP client | `openai.mcp.connect()` |
| **Gemini Pro** | Vertex AI MCP adapter | Google Cloud Run |
| **Ollama** (local) | HTTP MCP bridge | `localhost:11434/mcp` |

**Key Principle**: MCP is a **protocol**, not a product. Any AI tool can implement MCP client.

### 5.2 No Vendor Lock-In

**Portability Checklist**:
- ✅ MCP server is open-source (Apache-2.0 license)
- ✅ Configuration is JSON (no proprietary format)
- ✅ APIs are REST/GraphQL (standard protocols)
- ✅ Evidence format is JSON (no binary blobs)
- ✅ Webhooks are industry-standard (Slack Events API)

**Migration Path**:
```
Orchestrator MCP → Custom MCP → Third-party MCP → No MCP
```

Each step is **reversible** without data loss.

---

## 6. Tradeoffs and Alternatives

### 6.1 Alternatives Considered

| Alternative | Pros | Cons | Decision |
|-------------|------|------|----------|
| **Manual Process** | No automation cost | Slow, error-prone | ❌ Reject |
| **Zapier/Make** | No-code, fast setup | Limited AI, expensive | ❌ Reject (not AI-native) |
| **GitHub Actions Only** | Free, integrated | No Slack/Discord | ❌ Partial (use for CI/CD only) |
| **MCP Integration** | AI-native, flexible | Development cost | ✅ **Approved** |

### 6.2 Tradeoffs Accepted

**Cost**:
- **Development**: 800 LOC, 32 hours (Sprint 144)
- **Infrastructure**: $50/month (MCP server hosting)
- **Maintenance**: 4 hours/month (webhook secret rotation)

**Benefits**:
- **Time Saved**: 25 minutes/bug × 50 bugs/month = 20 hours/month
- **ROI**: Positive after 2 months
- **Competitive Advantage**: Boris Cherny best practice

**Risks**:
- **Dependency**: Relies on third-party APIs (Slack, GitHub)
- **Mitigation**: Graceful degradation (fall back to manual)

---

## 7. Decision

### 7.1 Recommendation

**APPROVE** MCP Integration Pattern for SDLC Framework 6.0.3.

**Reasoning**:
1. ✅ Addresses major gap identified in Boris Cherny analysis
2. ✅ Tool-agnostic (works with any AI tool)
3. ✅ Evidence Vault integration (unique competitive advantage)
4. ✅ Positive ROI (2-month payback period)
5. ✅ Aligns with Stage 07 (Operate) best practices

### 7.2 Implementation Roadmap

**Track 1 (Sprint 143)**: ✅ **This RFC** (methodology documentation)
**Track 2 (Sprint 144)**: Implementation (conditional on Track 1 approval)

**Sprint 144 Implementation**:
```yaml
Component: MCP Server (FastAPI)
LOC: 800
Effort: 32 hours
Files:
  - backend/app/services/mcp/mcp_server.py (300 LOC)
  - backend/app/services/mcp/slack_adapter.py (200 LOC)
  - backend/app/services/mcp/github_adapter.py (200 LOC)
  - backend/app/api/v1/endpoints/mcp.py (100 LOC)
Tests:
  - tests/unit/services/mcp/ (300 LOC)
  - tests/integration/test_mcp_slack.py (200 LOC)
```

**CLI Commands** (Track 2):
```bash
sdlcctl mcp connect --slack --channel bugs
sdlcctl mcp connect --github --repo sdlc-orchestrator
sdlcctl mcp list  # Show connected platforms
sdlcctl mcp disconnect --slack  # Remove integration
```

### 7.3 Success Criteria

**Track 1 Success** (Sprint 143):
- ✅ RFC approved by CTO
- ✅ Tool-agnostic validation passed
- ✅ Security model reviewed

**Track 2 Success** (Sprint 144):
- ✅ MCP server deployed to production
- ✅ Slack app installed and tested
- ✅ GitHub OAuth configured
- ✅ First bug auto-triaged end-to-end
- ✅ Evidence Vault audit trail verified
- ✅ Zero security vulnerabilities (Semgrep scan)

---

## 8. Appendices

### A. Example MCP Configuration

`.mcp.json`:
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
      "app_id": "A123456789",
      "signing_secret": "{{ env.SLACK_SIGNING_SECRET }}",
      "channels": ["bugs", "incidents"],
      "bot_token": "{{ env.SLACK_BOT_TOKEN }}"
    },
    "github": {
      "enabled": true,
      "app_id": "123456",
      "installation_id": "987654",
      "private_key_path": "/etc/mcp/github-app.pem",
      "repositories": ["org/sdlc-orchestrator"]
    }
  },
  "ai": {
    "provider": "anthropic",
    "model": "claude-sonnet-4-5",
    "fallback_model": "gpt-4o"
  },
  "evidence_vault": {
    "enabled": true,
    "bucket": "mcp-artifacts",
    "signature_algorithm": "ed25519"
  }
}
```

### B. References

- [Boris Cherny Implementation Plan](/home/dttai/.claude/plans/parallel-painting-turing.md)
- [MCP Protocol Specification](https://spec.modelcontextprotocol.io/)
- [Slack Events API](https://api.slack.com/events-api)
- [GitHub REST API](https://docs.github.com/en/rest)
- [Evidence Vault Specification](../../02-design/14-Technical-Specs/Evidence-Vault-Spec.md)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x00-header/)

### C. Glossary

- **MCP**: Model Context Protocol - standard for AI tool integrations
- **Webhook**: HTTP callback triggered by platform events
- **Mutual TLS**: Two-way TLS authentication (client + server)
- **Evidence Vault**: Tamper-evident audit trail storage (SDLC innovation)
- **Ed25519**: Asymmetric cryptography algorithm for signatures

---

**RFC Status**: 📋 DRAFT → ⏳ CTO REVIEW → ✅ APPROVED → 🔄 IMPLEMENTED
**Current Phase**: Track 1 (Methodology Documentation)
**Next Phase**: Track 2 (Implementation - Sprint 144, conditional)

**Framework-First Compliance**: ✅ VERIFIED
**Tool-Agnostic**: ✅ VERIFIED
**Boris Cherny Coverage**: ✅ Gap #1 Addressed

---

*SDLC Framework 6.0.3 - MCP Integration Pattern*
