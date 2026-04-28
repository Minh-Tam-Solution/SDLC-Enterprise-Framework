# MCP Integration — Case Study (SDLC Orchestrator)

**Version**: 6.3.1
**Status**: ACTIVE — Case Study (vendor-specific implementation example)
**Audience**: Platform / DevOps teams integrating AI tools with an SDLC governance platform

> **Note on framing**: This document was originally authored as an integration guide inside `04-AI-TOOLS-LANDSCAPE/`. It has been relocated to `06-Case-Studies/` because its content is **specific to the SDLC Orchestrator implementation** of the Framework, not a tool-agnostic integration pattern. Adopters implementing MCP on other platforms should treat this as **one reference example**, not as the Framework's normative guidance. Generic MCP integration tactics live in [`07-Implementation-Guides/MCP-Integration-Guide.md`](../07-Implementation-Guides/MCP-Integration-Guide.md).

---

## Purpose

Model Context Protocol (MCP) unlocks deep, governed integration between SDLC Orchestrator and AI development tools. This case study documents the reference architecture, security controls, and validation steps required to onboard MCP-capable tools (e.g., Claude Code) into the enterprise environment **as implemented in SDLC Orchestrator**.

---

## Reference Architecture

```
┌────────────────────┐        ┌────────────────────┐
│ SDLC Orchestrator  │        │ AI Tool (Client)   │
│ • Policy Engine    │◀──────▶│ • MCP Client SDK   │
│ • Evidence Vault   │        │ • CLAUDE.md / etc. │
└────────────────────┘        └────────────────────┘
         ▲                               ▲
         │                               │
         │ WebSocket (mutual TLS)        │ Local filesystem
         │                               │
┌────────┴────────┐             ┌────────┴────────┐
│ Identity Broker │────────────▶│ Secret Store    │
└─────────────────┘             └─────────────────┘
```

- **Transport**: Secure WebSocket (WSS) with mutual TLS.
- **Authentication**: Short-lived service tokens issued by Identity Broker (Okta, Auth0, etc.).
- **Evidence Flow**: Tool sends execution logs + diffs → Evidence Vault for audit.

---

## MCP Server Configuration

```json
{
  "servers": {
    "sdlc-orchestrator": {
      "command": "sdlcctl",
      "args": ["mcp", "serve"],
      "env": {
        "SDLC_PROJECT_ID": "${PROJECT_ID}",
        "EVIDENCE_VAULT_URL": "https://evidence.internal/api/v1",
        "MCP_TOKEN": "${SDLC_TOKEN}"
      }
    }
  }
}
```

### Required Environment Variables

- `SDLC_PROJECT_ID` – UUID matching Orchestrator project registry.
- `MCP_TOKEN` – Short-lived token minted via `sdlcctl auth issue --ttl 4h`.
- `EVIDENCE_VAULT_URL` – HTTPS endpoint for governance evidence ingestion.

> **Tip**: Store secrets in OS keychain or enterprise secrets manager; avoid committing `.env` with MCP credentials.

---

## Security Controls

| Control | Requirement | Implementation |
|---------|-------------|----------------|
| Mutual TLS | ✅ Required | Client certificate issued per device |
| Token TTL | ✅ Max 4 hours | Automated refresh via `sdlcctl auth renew` |
| Least Privilege | ✅ Project scoped | Token tied to single project ID |
| Audit Logging | ✅ Mandatory | All MCP commands logged to Evidence Vault |
| Offline Revocation | ✅ Supported | `sdlcctl auth revoke <token>` |

---

## Integration Checklist

1. **Provision Project** – `sdlcctl project register --name <repo>`.
2. **Issue Token** – `sdlcctl auth issue --project <id> --ttl 4h`.
3. **Update Tool Config** – Add `.mcp.json` to repository root.
4. **Verify Context Overlay** – Run `sdlcctl agents validate --repo .`.
5. **Test Governance Hooks**:
   - Trigger Planning Mode request.
   - Run verification command (`pytest`, `npm test`).
   - Submit evidence (`sdlcctl evidence push`).
6. **Record Evidence** – Confirm session log appears in Evidence Vault.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| `401 Unauthorized` | Token expired | Re-run `sdlcctl auth issue` |
| `TLS handshake failed` | Missing client cert | Install enterprise certificate bundle |
| Evidence not captured | Vault URL misconfigured | Update env var + retry |
| Planning Mode ignored | Context file >60 lines | Refactor CLAUDE.md / `.cursorrules` |

---

## Compliance Alignment

- **Agent Accountability** – Human approvals logged in Evidence Vault.
- **Verification-First** – MCP enforces pre-merge test execution.
- **Context Management** – Server validates context files per policy.
- **Audit Trail** – Every MCP command generates immutable evidence.

---

## Change Log

| Date | Change |
|------|--------|
| Jan 2026 | Initial guide for SDLC Framework 6.3.0 |

---

**Owner**: DevOps & Platform Engineering  
**Review Cycle**: Every major MCP release or quarterly (whichever comes first)
