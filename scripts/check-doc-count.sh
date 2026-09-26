#!/usr/bin/env bash
# check-doc-count — stops the framework from growing back.
#   Counts tracked *.md files outside 10-Archive/ and 05-Templates-Tools/ (git index; untracked files do not count).
#   ADVISORY above 40: prints a warning, exit 0. MACHINE above 60: exit 2. Thresholds published in 02-Core-Methodology/03-gates.md.
#   Burn case: v6.x reached 189 live docs (502 with the archive); nobody could say which ones were still true.
# Exit codes (02-Core-Methodology/01): 0 pass · 1 cannot measure · 2 violation. Last stdout line is the label.
# Usage: check-doc-count.sh [--root DIR] [--selftest]
set -u
ROOT=.; SELFTEST=0; ADVISORY=40; MACHINE=60
label() { echo "result=$1 gate=doc-count reason=$2${3:+ fix=$3}"; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT=${2:-}; shift;; --selftest) SELFTEST=1;;
  *) label insufficient_evidence unknown_argument; exit 1;; esac; shift; done

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
  mk() { # mk DIR live_docs archived_and_template_docs
    mkdir -p "$1/02-Core-Methodology" "$1/10-Archive/v6" "$1/05-Templates-Tools" && git -C "$1" init -q || return 1
    for i in $(seq 1 "$2"); do : > "$1/02-Core-Methodology/d$i.md"; done
    for i in $(seq 1 "$3"); do : > "$1/10-Archive/v6/a$i.md"; : > "$1/05-Templates-Tools/t$i.md"; done
    : > "$1/02-Core-Methodology/not-a-doc.txt"; git -C "$1" add -A
  }
  mk "$t/green" 40 100 && mk "$t/advisory" 41 0 && mk "$t/red" 61 0 && mkdir "$t/nogit" \
    || { label insufficient_evidence selftest_setup_failed; exit 1; }
  bash "$0" --root "$t/green" > "$t/out"; a=$?; ga=$(grep -c 'count=40' "$t/out")
  bash "$0" --root "$t/advisory" > "$t/out"; b=$?; gb=$(grep -c 'reason=advisory' "$t/out")
  bash "$0" --root "$t/red" > "$t/out"; c=$?
  bash "$0" --root "$t/nogit" > "$t/out" 2>&1; d=$?
  bash "$0" --root "$t/green/02-Core-Methodology" > "$t/out" 2>&1; e=$?   # a subdirectory is not a repo root
  got="$a$b$c$d$e $ga$gb"
  # 40 live + 200 archived/templates = green (archive not counted) · 41 = advisory, still 0 · 61 = red 2 · no repo = 1
  [ "$got" = "00211 11" ] && { echo "selftest OK"; exit 0; }
  echo "selftest FAILED: got=[$got] want=[00211 11]"; exit 1   # a broken selftest = broken gate ⇒ cannot measure
fi

# The root must be the top of a git work tree; otherwise the index we read is not the one we mean.
prefix=$(git -C "$ROOT" rev-parse --show-prefix) || { label insufficient_evidence not_a_git_repo; exit 1; }
[ -z "$prefix" ] || { label insufficient_evidence root_is_subdirectory "run from the repo root"; exit 1; }
list=$(git -C "$ROOT" ls-files -z -- '*.md' ':(exclude)10-Archive/' ':(exclude)05-Templates-Tools/' | tr '\0' '\n') \
  || { label insufficient_evidence git_ls_files_failed; exit 1; }
n=$(printf '%s' "$list" | grep -c .)
echo "count=$n advisory_over=$ADVISORY machine_over=$MACHINE"
if [ "$n" -gt "$MACHINE" ]; then
  label violation "count_${n}_over_${MACHINE}" "archive or merge docs; a new doc needs a named consumer (CONTRIBUTING.md)"; exit 2
fi
[ "$n" -gt "$ADVISORY" ] && { echo "WARNING: $n live docs, advisory threshold is $ADVISORY"; label pass "advisory_count_${n}_over_${ADVISORY}"; exit 0; }
label pass "count_${n}_within_${ADVISORY}"; exit 0
