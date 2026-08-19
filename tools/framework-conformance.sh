#!/usr/bin/env bash
# framework-conformance.sh — the Framework checks ITSELF.
#
# WHY THIS EXISTS
# 6.5.0 states, in its own words at 02-Core-Methodology/SDLC-Core-Methodology.md:679, that the
# anti-pattern is "Own-methodology-but-not-own-enforcement — claiming ST/DT adoption while the
# runtime gate path does not mechanically validate ST/DT evidence."
#
# The Framework's own machine-readable gate contract does not mechanically validate ST/DT evidence.
# The document that names the anti-pattern commits it, and nothing in the repo could notice, because
# the repo had no conformance CI at all — .github/workflows contained only pages.yml.
#
# Standard #20 (03-AI-GOVERNANCE/19-FEDERATED-PLATFORM-STANDARD.md:107) anticipates this and calls
# it a "hypocrisy cascade — prose-mandate without proven-reference-implementation", declaring it
# "mitigated here because two independent tools shipped the pattern before the Standard was written."
# Two federated tools shipping it does not make the Framework's own contract carry it.
#
# The chain this script exists to break:
#     Prose says MUST  ≠  Machine contract says MUST  ≠  CI proves MUST  ≠  Runtime proves MUST
#
# THREE OUTCOMES, never two (a gate that cannot look must not report clean):
#     0 = conformant · 1 = non-conformant · 2 = could-not-look
set -u
cd "$(dirname "$0")/.."
ERR=0; BLIND=0; N=0
red()  { echo "❌ $*"; ERR=1; }
blind(){ echo "🟡 COULD-NOT-LOOK: $*"; BLIND=1; }
ok()   { echo "✅ $*"; }

# ── C1. Framework-version drift.
# ⚠️ Narrowed after a false positive of my own. The first version compared every `version:` field to
# the README, and flagged anti-vibecoding.yaml (1.0.0) and two archived SASE templates. The README
# itself refutes that at line 3: a document's own semver is "independent of Framework version"
# (Schema-Versioning Convention A). Document semver is not a framework claim.
# So this checks only files that assert a FRAMEWORK version — `SDLC Framework <semver>` or a
# `framework_version:` field — and skips 10-Archive, which is archived by definition.
FW=$(grep -m1 -oE '\*\*Version\*\*: [0-9]+\.[0-9]+\.[0-9]+' README.md 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
if [ -z "$FW" ]; then blind "README.md declares no parseable **Version**"; else
  N=$((N+1))
  while IFS= read -r hit; do
    f=${hit%%:*}; rest=${hit#*:}; ln=${rest%%:*}
    v=$(echo "${rest#*:}" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1)
    [ -n "$v" ] || continue
    [ "$v" = "$FW" ] || red "C1 framework-version-drift: $f:$ln asserts Framework $v while README.md asserts $FW"
  done < <(grep -rnE 'SDLC Framework [0-9]+\.[0-9]+\.[0-9]+|framework_version:' --include='*.yaml' --include='*.json' . 2>/dev/null | grep -v '/10-Archive/')
  ok "C1 checked against Framework $FW"

  # ⚠️ C1 stays on MACHINE CONTRACTS ONLY — a trap walked into and backed out of.
  # A second-model audit (Kimi K3) correctly found ~99 markdown files stamping an older
  # `**Framework**: SDLC X.Y.Z`. Widening C1 to markdown turned all 99 red. Then the Framework's
  # own convention refuted it: 02-Core-Methodology/SDLC-Schema-Versioning.md:70 says those markdown
  # patterns "remain valid for backward compatibility" and "mass-migration of field names alone is
  # explicitly NOT required (per MM#9)"; line 49 says blanket-bumping on a Framework patch is
  # EXPLICITLY REJECTED because it would make the Framework violate MM#9 — the principle Amendment B
  # had just added. 98 of 99 were false red BY RATIFIED CONVENTION.
  # Shipping them would have recreated the condition that got the cite-existence gate disarmed to
  # `exit 0` in this estate: a phantom oracle produced 56% false red, and turning off a gate nobody
  # can trust is the rational response. Precision is what decides whether a gate survives.
  # Convention A's backward-compat clause covers PROSE stamps; it does not cover the version a
  # CONTRACT file asserts about the rules it encodes.

  # ── C1b. Verify the ruler before trusting it.
  # C1 treats README.md as ground truth for "which Framework is this". Kimi found README.md:458
  # asserting "SDLC 6.1.0 Framework (THIS REPO)" while README.md:3 asserts 6.5.0 — the authority
  # disagreeing with itself by four minor versions, inside a diagram labelled THIS REPO. A check
  # that trusts a source inherits that source's contradictions in silence.
  N=$((N+1))
  while IFS= read -r hit; do
    ln=${hit%%:*}
    v=$(echo "$hit" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1)
    [ "$v" = "$FW" ] || red "C1b ruler-self-contradiction: README.md:$ln asserts Framework $v while README.md:3 declares $FW — the source C1 trusts disagrees with itself"
  done < <(grep -nE 'SDLC [0-9]+\.[0-9]+\.[0-9]+ Framework' README.md 2>/dev/null)
  ok "C1b checked"
fi

# ── C2. A machine contract may not cite a document that does not exist.
N=$((N+1))
while IFS= read -r y; do
  src=$(grep -m1 -E '^\s*source_document:' "$y" | sed 's/.*source_document:[[:space:]]*//; s/^"//; s/"$//')
  [ -n "$src" ] || continue
  ln=$(grep -n -m1 -E '^\s*source_document:' "$y" | cut -d: -f1)
  base=$(echo "$src" | sed 's|^SDLC-Enterprise-Framework/||')
  [ -f "$base" ] || [ -f "$src" ] || red "C2 dangling-reference: $y:$ln cites '$src' — no such file"
done < <(find . -name '*.yaml' -not -path './.git/*' | sort)
ok "C2 checked"

# ── C3. A normative MUST naming a gate must exist in the machine gate contract.
# This is the first test @ceo specified: 6.5.0 declares ST/DT mandatory at G1/G2 in prose, and CI
# must notice that gates.yaml does not carry it.
GY=02-Core-Methodology/Governance-Compliance/gates.yaml
N=$((N+1))
if [ ! -f "$GY" ]; then blind "$GY absent — cannot check prose-vs-contract"; else
  while IFS= read -r hit; do
    f=${hit%%:*}; rest=${hit#*:}; ln=${rest%%:*}
    grep -qi "ST/DT\|systems.thinking\|design.thinking" "$GY" \
      || { red "C3 normative-without-contract: $f:$ln requires ST/DT gate-enforcement at G1/G2, but $GY has no such rule — prose MUST, machine contract silent"; break; }
  done < <(grep -rn "ST/DT" --include='*.md' . 2>/dev/null | grep -E "MUST|mandatory|Mandatory" | grep -E "G1|G2")
  ok "C3 checked"
fi

# ── C4. Ring-1 normative text may not make a named product mandatory.
# README states the Framework is tool-agnostic and Framework:Platform is 1:N. A requirement naming a
# vendor makes an interchangeable implementation non-conformant by identity rather than by contract.
N=$((N+1))
PRODUCTS='Claude Code|MTClaw|SDLC Orchestrator|EndiorBot|Cursor|SonarQube|Jira'
while IFS= read -r hit; do
  f=${hit%%:*}; rest=${hit#*:}; ln=${rest%%:*}; txt=${rest#*:}
  red "C4 product-pinned-normative: $f:$ln makes a named product mandatory — $(echo "$txt" | cut -c1-80)"
done < <(grep -rnE "($PRODUCTS)" --include='*.md' 03-AI-GOVERNANCE 2>/dev/null | grep -E '\| *(Mandatory|MUST|Required) *\|')
ok "C4 checked ($N checks run)"

echo
if [ "$BLIND" = 1 ] && [ "$ERR" = 0 ]; then
  echo "framework-conformance: COULD-NOT-LOOK — this is not a pass"; exit 2
fi
[ "$ERR" = 0 ] && { echo "framework-conformance: CONFORMANT"; exit 0; }
echo "framework-conformance: NON-CONFORMANT"; exit 1
