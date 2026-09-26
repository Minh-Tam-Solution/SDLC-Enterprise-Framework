#!/usr/bin/env bash
# check-doc-count — stops the framework from growing back.
#   Counts tracked *.md files outside archive/ and templates/ (git index; untracked files do not count).
#   ADVISORY above 40: prints a warning, exit 0. No hard ceiling since 2026-09-26: a count is a smell, not a
#   health measure. What blocks is DOC-2 (scripts/check-doc-ownership.sh): every live doc names an owner, a
#   consumer and a review-by date. Threshold published in controls/gates.md.
#   Burn case: v6.x reached 189 live docs (502 with the archive); nobody could say which ones were still true.
# Exit codes (controls/rule-contract.md): 0 pass · 1 cannot measure · 2 violation. Last stdout line is the label.
# Usage: check-doc-count.sh [--root DIR] [--selftest]
set -u
ROOT=.; SELFTEST=0; ADVISORY=40
label() { echo "result=$1 gate=doc-count reason=$2${3:+ fix=$3}"; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT=${2:-}; shift;; --selftest) SELFTEST=1;;
  *) label insufficient_evidence unknown_argument; exit 1;; esac; shift; done

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
  mk() { # mk DIR live_docs archived_and_template_docs
    mkdir -p "$1/core" "$1/archive/v6" "$1/templates" && git -C "$1" init -q || return 1
    for i in $(seq 1 "$2"); do : > "$1/core/d$i.md"; done
    for i in $(seq 1 "$3"); do : > "$1/archive/v6/a$i.md"; : > "$1/templates/t$i.md"; done
    : > "$1/core/not-a-doc.txt"; git -C "$1" add -A
  }
  mk "$t/green" 40 100 && mk "$t/advisory" 41 0 && mk "$t/big" 61 0 && mkdir "$t/nogit" \
    || { label insufficient_evidence selftest_setup_failed; exit 1; }
  bash "$0" --root "$t/green" > "$t/out"; a=$?; ga=$(grep -c 'docs=40 ' "$t/out")
  bash "$0" --root "$t/advisory" > "$t/out"; b=$?; gb=$(grep -c 'reason=advisory' "$t/out")
  bash "$0" --root "$t/big" > "$t/out"; c=$?
  bash "$0" --root "$t/nogit" > "$t/out" 2>&1; d=$?
  bash "$0" --root "$t/green/core" > "$t/out" 2>&1; e=$?   # a subdirectory is not a repo root
  got="$a$b$c$d$e $ga$gb"
  # 40 live + 200 archived/templates = green (archive not counted) · 41 and 61 = advisory, still 0 · no repo = 1
  [ "$got" = "00011 11" ] && { echo "selftest OK"; exit 0; }
  echo "selftest FAILED: got=[$got] want=[00011 11]"; exit 1   # a broken selftest = broken gate ⇒ cannot measure
fi

# The root must be the top of a git work tree; otherwise the index we read is not the one we mean.
prefix=$(git -C "$ROOT" rev-parse --show-prefix) || { label insufficient_evidence not_a_git_repo; exit 1; }
[ -z "$prefix" ] || { label insufficient_evidence root_is_subdirectory "run from the repo root"; exit 1; }
list=$(git -C "$ROOT" ls-files -z -- '*.md' ':(exclude)archive/' ':(exclude)templates/' | tr '\0' '\n') \
  || { label insufficient_evidence git_ls_files_failed; exit 1; }
n=$(printf '%s' "$list" | grep -c .)
over=$(( n > ADVISORY ? n - ADVISORY : 0 ))
# count= is what the advisory-deadline gate (G4) reads: docs OVER the threshold, not the total.
echo "docs=$n advisory_over=$ADVISORY count=$over"
[ "$n" -gt "$ADVISORY" ] && { echo "WARNING: $n live docs, advisory threshold is $ADVISORY"; label pass "advisory_count_${n}_over_${ADVISORY}"; exit 0; }
label pass "count_${n}_within_${ADVISORY}"; exit 0
