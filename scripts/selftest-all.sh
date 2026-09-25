#!/usr/bin/env bash
# Runs --selftest on every script in this directory that supports it. Lazy aggregator — no
# framework, no manifest to keep in sync: a script is included iff it accepts --selftest.
set -u
dir="$(cd "$(dirname "$0")" && pwd)"
fail=0; ran=0
for f in "$dir"/*.sh "$dir"/*.py; do
  [ -f "$f" ] || continue
  [ "$f" = "$dir/selftest-all.sh" ] && continue
  grep -q -- '--selftest' "$f" || continue
  ran=$((ran+1))
  case $f in *.py) runner=python3;; *) runner=bash;; esac
  printf '%s: ' "$(basename "$f")"
  if out=$($runner "$f" --selftest 2>&1); then
    echo "OK"
  else
    echo "FAILED"
    echo "$out" | sed 's/^/  /'
    fail=$((fail+1))
  fi
done
if [ $ran -eq 0 ]; then
  echo "UNMEASURABLE: no script in $dir supports --selftest"; exit 1
fi
[ $fail -eq 0 ] && { echo "selftest-all: $ran/$ran OK"; exit 0; }
echo "selftest-all: $fail/$ran FAILED"; exit 1
