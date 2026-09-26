#!/usr/bin/env bash
# Rule L4: forbid `\b` in `git grep -E`. It matches NOTHING and still returns SUCCESS — silently.
#   Burn case: `git grep -E '\bMUST\b'` returned 0 lines (the string was there). The same session then
#   miscounted in the opposite direction (5 vs. hundreds) — both silent, both exposed only by a positive control.
#   Use `-w` or `-P`.
# Scans RUNNABLE files (*.sh *.py *.yml *.yaml Makefile), not prose — a doc that tells the burn case is not a command.
# Exit codes (controls/rule-contract.md): 0 pass · 1 cannot measure · 2 violation. Last stdout line is the label.
set -u
ROOT=${1:-.}
label() { echo "result=$1 gate=rule-git-grep-no-word-boundary reason=$2"; }
if [ "$ROOT" = --selftest ]; then
  t=$(mktemp -d)
  printf 'git grep -w MUST\n' > "$t/clean.sh"; bash "$0" "$t" >/dev/null; a=$?
  printf 'git grep -E %s\n' "'\\bMUST\\b'" > "$t/bad.sh"; bash "$0" "$t" >/dev/null; b=$?
  bash "$0" "$t/missing" >/dev/null; c=$?
  rm -rf "$t"
  [ "$a$b$c" = "021" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: $a$b$c (want 021)"; label insufficient_evidence selftest_broken; exit 1  # broken selftest = broken GATE => cannot measure (1), not violation (2)
fi
[ -d "$ROOT" ] || { echo "CANNOT MEASURE: $ROOT does not exist"; label insufficient_evidence root_missing; exit 1; }
violations=0
while IFS= read -r -d '' f; do
  while IFS= read -r l; do violations=$((violations+1)); echo "RED — violation: ${f#"$ROOT"/}: $l"; done \
    < <(grep -nE 'git grep' "$f" | grep -E -- '(-E|--extended-regexp)' | grep -F '\''b' )
done < <(find "$ROOT" -type f \( -name '*.sh' -o -name '*.py' -o -name '*.yml' -o -name '*.yaml' -o -name Makefile \) \
          -not -path '*/.git/*' -not -path '*/archive/*' -not -name "$(basename "$0")" -print0)
echo "violations=$violations"
[ $violations -gt 0 ] && { label violation "violations_$violations"; exit 2; }
label pass clean; exit 0
