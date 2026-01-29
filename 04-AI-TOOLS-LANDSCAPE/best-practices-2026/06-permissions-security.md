# Permissions & Security
## Safe AI Execution Patterns

**Version:** 6.0.0
**Status:** ACTIVE
**Date:** January 27, 2026

---

## Overview

AI coding agents have significant access to your codebase and system. This guide covers permission modes, security rules, and safe execution patterns.

---

## Permission Modes

### Normal Mode (Default)

Claude asks before each action.

**Use for:**
- New projects
- Unfamiliar codebases
- Learning workflows

### Plan Mode

Claude shows plan, waits for approval before execution.

**Use for:**
- Complex changes
- Destructive operations
- Multi-file refactoring

### Auto-Accept Mode

Claude makes edits without asking.

**Use for:**
- Trusted operations
- Speed-critical workflows
- Well-understood codebases

### Setting Modes

```bash
# Via CLI
claude --permission-mode=plan

# In VS Code
# Bottom of prompt box: Normal → Plan → Auto-accept

# Default via settings
# claudeCode.initialPermissionMode: "plan"
```

---

## Permission Rules

### Syntax

```json
{
  "permissions": {
    "allow": [
      "Bash(npm:*)",           // All npm commands
      "Bash(git:*)",           // All git commands
      "Read(**/*.{js,ts})",    // Read source files
      "Edit(**/*.{js,ts})"     // Edit source files
    ],
    "ask": [
      "Bash(docker:*)",        // Confirm Docker
      "Edit(**/config/**)"     // Confirm config changes
    ],
    "deny": [
      "Read(./.env*)",         // Block secrets
      "Read(./secrets/**)",
      "Edit(**/production/**)", // Block prod
      "Bash(rm:*)"             // Block destructive
    ]
  }
}
```

### Evaluation Order

```
Deny → Ask → Allow
- First match wins
- Deny ALWAYS wins
```

---

## Sensitive File Protection

### Block Secrets

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(./**/*.key)",
      "Read(./**/*.pem)",
      "Read(./**/*secret*)",
      "Read(./**/password*)"
    ]
  }
}
```

### Block Production

```json
{
  "permissions": {
    "deny": [
      "Edit(**/production/**)",
      "Bash(*production*)",
      "Bash(*--prod*)"
    ]
  }
}
```

---

## Network Security

### Whitelist Approach

```json
{
  "permissions": {
    "allow": [
      "WebFetch(domain:github.com)",
      "WebFetch(domain:npmjs.org)",
      "WebFetch(domain:api.stripe.com)"
    ],
    "deny": [
      "WebFetch(*.internal.corp)",
      "Bash(curl:*)",
      "Bash(wget:*)"
    ]
  }
}
```

**Warning:** If Bash is allowed, agents can bypass WebFetch restrictions via curl/wget.

---

## Hooks for Security

### Block Production Changes

```python
#!/usr/bin/env python3
# hooks/block-production.py
import json
import sys

data = json.load(sys.stdin)
file_path = data.get("tool_input", {}).get("file_path", "")

if "production" in file_path:
    print(json.dumps({
        "decision": "deny",
        "reason": "Production files cannot be modified"
    }))
    sys.exit(1)
```

### Log All Commands

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "jq -r '\"\\(.tool_input.command)\"' >> ~/.claude/bash.log"
      }]
    }]
  }
}
```

### Validate Read-Only Operations

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "./scripts/validate-readonly.sh"
      }]
    }]
  }
}
```

---

## Enterprise Managed Settings

### Cannot Override

```bash
~/.claude/managed/managed-settings.json
~/.claude/managed/managed-mcp.json
~/.claude/managed/CLAUDE.md
```

### Example Configuration

```json
{
  "permissions": {
    "deny": [
      "Bash(rm:-rf:*)",
      "Edit(**/production/**)",
      "WebFetch(*.internal.corp)"
    ]
  },
  "allowManagedHooksOnly": true,
  "environmentVariables": {
    "COMPANY_STANDARDS": "true"
  }
}
```

---

## Security Best Practices

### ✅ DO

1. **Use Plan mode for destructive operations**
2. **Block sensitive files explicitly** (.env, secrets, keys)
3. **Whitelist network access** instead of blacklist
4. **Log all Bash commands** for audit
5. **Use hooks for custom validation**
6. **Review before auto-accepting**

### ❌ DON'T

1. **Auto-accept in production environments**
2. **Allow unrestricted Bash access**
3. **Store secrets in CLAUDE.md**
4. **Skip permission warnings**
5. **Grant WebFetch without domain limits**
6. **Disable security hooks**

---

## SDLC Orchestrator Integration

### AGPL Containment

```json
{
  "permissions": {
    "deny": [
      "Edit(**/minio/**)",
      "Edit(**/grafana/**)",
      "Bash(pip install minio)",
      "Bash(pip install grafana*)"
    ]
  }
}
```

### Evidence Vault Protection

```json
{
  "permissions": {
    "deny": [
      "Edit(**/evidence/**)",
      "Bash(rm:**evidence**)"
    ],
    "ask": [
      "Read(**/evidence/**)"
    ]
  }
}
```

---

**Document Status:** ACTIVE
**Last Updated:** January 22, 2026
