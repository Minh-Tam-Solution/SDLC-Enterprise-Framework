#!/usr/bin/env bash
# Rule L2 (G2): forbid swallowing stderr in scripts/. If truly needed, declare it in .stderr-exemptions with an EXPIRY.
#   Why: `find … 2>/dev/null | wc -l` hits a permission error => prints 0 => the script decides "empty".
#   Burn case: `2>/dev/null` swallowed a missing-module error and the gate printed "README out of sync with YAML" — the wrong cause.
# .stderr-exemptions, one line each:  path<TAB>YYYY-MM-DD(expiry)<TAB>reason
# Exit codes (02-Core-Methodology/01): 0 pass · 1 cannot measure · 2 violation (including an expired exemption). Last stdout line is the label.
set -u
DIR=${1:-scripts}
EXEMPT=.stderr-exemptions
label() { echo "result=$1 gate=rule-no-swallowed-stderr reason=$2"; }
if [ "$DIR" = --selftest ]; then
  t=$(mktemp -d)
  printf '#!/bin/sh\nls x\n' > "$t/clean.sh"; bash "$0" "$t" >/dev/null; a=$?
  printf '#!/bin/sh\nls x 2>/dev/nul''l\n' > "$t/bad.sh"; bash "$0" "$t" >/dev/null; b=$?
  printf 'bad.sh\t2999-01-01\ttest\n' > "$t/$EXEMPT"; bash "$0" "$t" >/dev/null; c=$?
  printf 'bad.sh\t2000-01-01\ttest\n' > "$t/$EXEMPT"; bash "$0" "$t" >/dev/null; d=$?
  bash "$0" "$t/missing" >/dev/null; e=$?
  rm -rf "$t"
  [ "$a$b$c$d$e" = "02021" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: $a$b$c$d$e (want 02021)"; label insufficient_evidence selftest_broken; exit 1  # broken selftest = broken GATE => cannot measure (1), not violation (2)
fi
[ -d "$DIR" ] || { echo "CANNOT MEASURE: $DIR does not exist"; label insufficient_evidence dir_missing; exit 1; }
today=$(date +%F); violations=0; exempt=0; expired=0
while IFS= read -r -d '' f; do
  rel=${f#"$DIR"/}
  n=$(grep -c '2>/dev/nul[l]' "$f"); [ "$n" -gt 0 ] || continue
  until=""; [ -f "$DIR/$EXEMPT" ] && until=$(awk -F'\t' -v r="$rel" '$1==r{print $2; exit}' "$DIR/$EXEMPT")
  if [ -z "$until" ] || ! [[ $until =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then violations=$((violations+n)); echo "RED — violation: $rel ($n places)"
  elif [[ $until < $today ]]; then expired=$((expired+n)); echo "RED — exemption EXPIRED $until: $rel ($n places)"
  else exempt=$((exempt+n)); fi
done < <(find "$DIR" -type f \( -name '*.sh' -o -name '*.py' \) -not -name "$(basename "$0")" -print0)
echo "violations=$violations exempt_active=$exempt exempt_expired=$expired"
[ $((violations+expired)) -gt 0 ] && { label violation "violations_${violations}_expired_$expired"; exit 2; }
label pass clean; exit 0
