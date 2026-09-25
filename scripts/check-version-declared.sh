#!/usr/bin/env bash
# First v7 MACHINE gate — "which framework version was this document verified against?"
#
# BASIS: Convention A
#   **Version**: X.Y.Z              = the document's OWN semver — allowed, and expected, to differ from the framework
#   sdlc_framework / **SDLC Framework Version**  = which framework version it was verified against
# => This gate does NOT check `**Version**`. It checks the second field.
# => Declaring a version OLDER than the SSOT is NOT an error — bulk version bumps (Convention B)
#    were rejected because they add surface nobody asked for. Counted only, never flagged.
#
# G2 — three buckets, never merged:
#   declared_current : verified against the current SSOT
#   declared_older   : verified against an older version   -> legal, counted only
#   undeclared       : no field at all                     -> NOT MEASURED => this is the finding
#
# Usage: check-version-declared.sh [--block] [--selftest]  (legacy --chan still accepted, deprecated)
#   no flag -> count, exit 0 (step 1 ADVISORY) · --block -> exit 2 if undeclared>0 (step 3 MACHINE)
# Exit codes (v7/01): 0 PASS · 1 CANNOT MEASURE (no SSOT / 0 files scanned / unknown argument) · 2 VIOLATION.
# Last stdout line = label: result=pass|insufficient_evidence|violation gate=check-version-declared reason=<slug>
set -uo pipefail
BLOCK=0; SELFTEST=0
label() { echo "result=$1 gate=check-version-declared reason=$2"; }
for a in "$@"; do case $a in
  --block) BLOCK=1;;
  --chan) echo "DEPRECATED: --chan, use --block (removal 2026-12-31)" >&2; BLOCK=1;;
  --selftest) SELFTEST=1;;
  *) echo "CANNOT MEASURE: unknown argument $a"; label insufficient_evidence unknown_argument; exit 1;; esac; done

if [ $SELFTEST = 1 ]; then
  # Local fixture: copy this script into a temp tree (ROOT = .. of the script, scripts/ at repo root) — never touches the real repo.
  t=$(mktemp -d); S="$t/scripts/$(basename "$0")"
  mkdir -p "$(dirname "$S")" "$t/d"; cp "$0" "$S"
  kq() { local o rc; o=$(bash "$S" "$@"); rc=$?; echo "$rc|$(echo "$o" | grep -oE 'declared_older=[0-9]+  undeclared=[0-9]+')|${o##*$'\n'}"; }
  printf '# r\n**Version**: 9.9.9\n' > "$t/README.md"
  a=$(kq --block)                                                           # only exempt files => 0 scanned => 1 (G1)
  printf '# a\n**SDLC Framework Version**: 9.9.9\n' > "$t/d/current.md";  b=$(kq --block)  # declares the SSOT => 0
  printf -- '---\nsdlc_framework: "1.0.0"\n---\n' > "$t/d/older.md";    c=$(kq --block)  # declared_older is NOT an error => 0
  printf '# undeclared\n' > "$t/d/none.md";                              d=$(kq --block)  # field missing => 2
  e=$(kq)                                                                   # step 1: count only => 0
  g=$(kq --chan)                                                            # legacy --chan still behaves like --block (deprecated)
  rm "$t/README.md";                                                        f=$(kq --block)  # SSOT missing => 1
  rm -rf "$t"
  G=gate=check-version-declared
  want="1|declared_older=0  undeclared=0|result=insufficient_evidence $G reason=scanned_0_files
0|declared_older=0  undeclared=0|result=pass $G reason=undeclared_0
0|declared_older=1  undeclared=0|result=pass $G reason=undeclared_0
2|declared_older=1  undeclared=1|result=violation $G reason=undeclared_1
0|declared_older=1  undeclared=1|result=pass $G reason=step1_count_only_undeclared_1
2|declared_older=1  undeclared=1|result=violation $G reason=undeclared_1
1||result=insufficient_evidence $G reason=ssot_readme_missing"
  got=$(printf '%s\n' "$a" "$b" "$c" "$d" "$e" "$g" "$f")
  [ "$got" = "$want" ] && { echo "selftest OK (7 cases)"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN:"; diff <(echo "$want") <(echo "$got")
  label insufficient_evidence selftest_broken; exit 1  # broken selftest = broken GATE => cannot measure (1), not violation (2)
fi
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Repo META files — not rule documents => exempt. The list is DECLARED by hand, never inferred.
META='^(README|CHANGELOG|CONTENT-MAP|CONTRIBUTING|CODE_OF_CONDUCT|SECURITY|DEPRECATION-POLICY|CLAUDE)\.md$'

# Keep "no README" apart from "README declares no version" — two causes, two labels (G2).
[ -f "$ROOT/README.md" ] || { echo "CANNOT MEASURE: no $ROOT/README.md (SSOT)"; label insufficient_evidence ssot_readme_missing; exit 1; }
SSOT="$(grep -m1 -oE '^\*\*Version\*\*: [0-9]+\.[0-9]+\.[0-9]+' "$ROOT/README.md" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')"
[ -n "$SSOT" ] || { echo "CANNOT MEASURE: README.md declares no '**Version**: x.y.z'"; label insufficient_evidence readme_version_missing; exit 1; }

declared_current=0; declared_older=0; undeclared=0; exempt=0; DS=$(mktemp); trap 'rm -f "$DS"' EXIT  # mktemp: two parallel runs never overwrite each other
while IFS= read -r -d '' f; do
  rel="${f#$ROOT/}"
  if [[ "$rel" =~ / ]]; then base="${rel##*/}"; else base="$rel"; fi
  if [[ ! "$rel" =~ / ]] && [[ "$base" =~ $META ]]; then exempt=$((exempt+1)); continue; fi
  v=$(head -20 "$f" | grep -m1 -oE 'sdlc_framework: *"?[0-9]+\.[0-9]+\.[0-9]+|^\*\*SDLC Framework Version\*\*: *[0-9]+\.[0-9]+\.[0-9]+' | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
  if   [ -z "$v" ];            then undeclared=$((undeclared+1)); echo "$rel" >> "$DS"
  elif [ "$v" = "$SSOT" ];     then declared_current=$((declared_current+1))
  else                              declared_older=$((declared_older+1)); fi
done < <(find "$ROOT" -name '*.md' -not -path '*/.git/*' -not -path '*/10-Archive/*' -not -path '*/site/*' -print0)

total=$((declared_current+declared_older+undeclared+exempt))
echo "SSOT=$SSOT  declared_current=$declared_current  declared_older=$declared_older  undeclared=$undeclared  exempt=$exempt  total=$total"
echo "  declared_older is NOT an error (Convention A) — it only maps verification debt."
# G1: 0 files to measure => "clean" means nothing => cannot measure, not pass.
[ $((total-exempt)) -gt 0 ] || { echo "CANNOT MEASURE: no file outside the exempt list"; label insufficient_evidence scanned_0_files; exit 1; }
[ "$undeclared" -gt 0 ] && { echo "--- $undeclared files have NEVER recorded which version they were verified against (first 10) ---"; head -10 "$DS"; }
[ "$undeclared" = 0 ] && { label pass undeclared_0; exit 0; }
[ "$BLOCK" = 1 ] && { label violation "undeclared_$undeclared"; exit 2; }
label pass "step1_count_only_undeclared_$undeclared"; exit 0
