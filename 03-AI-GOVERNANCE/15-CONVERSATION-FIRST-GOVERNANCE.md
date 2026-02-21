# 15. Conversation-First Governance Patterns

**Version**: 6.1.1
**Status**: ACTIVE
**Date**: February 21, 2026
**Pillar**: Core AI Governance

---

## 1. Principle

Governance actions should be accessible from a team's **primary communication channel**. When governance lives where work conversations already happen, adoption increases and friction decreases.

**Interface Hierarchy**:

| Priority | Interface | Role | Users |
|----------|-----------|------|-------|
| Primary | Conversation (OTT/Chat) | Team governance actions | All team members |
| Secondary | CLI | Power user / CI/CD automation | DevOps, senior engineers |
| Tertiary | Web Dashboard | Admin, reporting, configuration | Managers, compliance |

**Key invariant**: All three interfaces execute the same governance actions against the same backend. The interface is a presentation concern, not a logic concern.

---

## 2. North Star Governance Loop

The canonical governance flow via conversation:

```
@mention → Gate Action → Evidence → Approve (OOB) → Audit Export
```

| Step | Conversation Action | Example |
|------|---------------------|---------|
| Trigger | @mention or command keyword | `@bot gate status #123` |
| Gate action | Bot evaluates gate criteria | Returns pass/fail with evidence gaps |
| Evidence | User attaches inline or replies with link | Screenshot, test report, PR URL |
| Approval | Out-of-band authentication | Magic link sent via separate channel |
| Audit | Bot confirms and logs | Correlation ID links thread to gate record |

---

## 3. Evidence from Conversation

Conversation threads are first-class evidence sources:

- **Inline attachments**: Files, screenshots, test reports shared in thread
- **Structured responses**: Bot-prompted forms completed in conversation
- **Thread transcript**: The conversation itself serves as decision rationale
- **Correlation ID**: Every governance action generates a unique ID linking the message thread to the gate evaluation record

**Retention**: Evidence captured from conversation follows the same retention policy as web-submitted evidence (90 days default, 1 year for ENTERPRISE).

---

## 4. Command Parity

CLI and conversation interfaces MUST execute from the same command registry. No feature parity drift.

| Property | Requirement |
|----------|-------------|
| Command definitions | Single source of truth (shared registry) |
| Parameters | Identical Pydantic schemas across interfaces |
| Permissions | Same RBAC scopes regardless of interface |
| Aliases | Conversation supports localized aliases (e.g., Vietnamese) |

---

## 5. Enterprise Channel Considerations

Channel selection is an implementation decision. The methodology is identical regardless of channel:

- **Consumer OTT** (Telegram, Discord): Suitable for SME and startup teams
- **Enterprise messaging** (MS Teams, Slack): Required when corporate security policy mandates it
- **Hybrid**: Teams may use consumer OTT for speed and enterprise channels for audited actions

The governance patterns in this document apply to ALL channels without modification.

---

## 6. Security Considerations

Conversation channels introduce external input that requires specific safeguards:

| Concern | Mitigation |
|---------|------------|
| Authentication | Out-of-band (OOB) verification for approval actions (e.g., magic link) |
| Input sanitization | All external channel content sanitized before processing |
| Channel-agnostic model | Security rules defined once, applied across all channels |
| Replay protection | Idempotency keys and webhook deduplication |
| Audit trail | All governance actions logged with channel source identifier |

---

## 7. Tier Applicability

| Tier | Conversation Governance |
|------|------------------------|
| **LITE** | Optional — teams may use web-only |
| **STANDARD** | Recommended — reduces governance friction |
| **ENTERPRISE** | Required — conversation is primary interface for team governance |

---

## 8. Anti-Patterns

| Anti-Pattern | Why It Fails | Correct Pattern |
|-------------|--------------|-----------------|
| Web-only governance | Low adoption, high friction | Conversation-first with web as admin fallback |
| Separate command sets per interface | Feature drift, inconsistent behavior | Single command registry |
| Approvals in same channel | No authentication boundary | OOB approval (magic link, separate channel) |
| Unstructured free-text commands | Parsing errors, ambiguity | Structured command syntax with bot confirmation |

---

## Related Documents

- [01-AI-Human-Collaboration.md](01-AI-Human-Collaboration.md) — Collaboration principle that conversation-first extends
- [12-MULTI-AGENT-PATTERNS.md](12-MULTI-AGENT-PATTERNS.md) — Pattern #10: Canonical Protocol Owner
- [CONTENT-MAP.md](../CONTENT-MAP.md) — Topic mapping

---

**Document Status**: ACTIVE
**Owner**: CTO Office
**Last Updated**: February 21, 2026
**Framework**: SDLC 6.1.1
