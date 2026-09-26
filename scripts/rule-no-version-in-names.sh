#!/usr/bin/env bash
# Rule NAME-1: no version number in a live file name, folder name or Markdown heading.
#   A heading is a link anchor, so a version in it breaks links exactly like a version in a path.
#   Burn case: the core lived in `v7/`; moving it to version-neutral folders broke ~100 link lines in
#   four consuming repos on 2026-09-26, and the next major version would have broken them again.
# Counts tracked paths (git index) and headings in tracked *.md. Skips archive/ (read-only record) and
#   CHANGELOG.md (a version log by definition). ADVISORY: prints count=, exits 0; 1 = cannot measure.
# Exit codes (controls/rule-contract.md): 0 pass · 1 cannot measure · 2 violation. Last stdout line is the label.
set -u
ROOT=.; SELFTEST=0
label() { echo "result=$1 gate=rule-no-version-in-names reason=$2${3:+ fix=$3}"; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT=${2:-}; shift;; --selftest) SELFTEST=1;;
  *) label insufficient_evidence unknown_argument; exit 1;; esac; shift; done

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
  mkdir -p "$t/r/core" "$t/r/v7" "$t/r/archive/v6" && git -C "$t/r" init -q \
    || { label insufficient_evidence selftest_setup_failed; exit 1; }
  printf '# Gates\n## Stage gate G0.1\n' > "$t/r/core/gates.md"          # clean: G0.1 is not a version
  printf '# Rules\n' > "$t/r/v7/rules.md"                                  # red: folder v7/
  printf '# Guide\n## What v7 is\n' > "$t/r/core/guide.md"                 # red: heading
  printf '# x\n' > "$t/r/core/spec-6.3.0.md"                               # red: file name
  printf '# CHANGELOG\n## Version 7.0.0\n' > "$t/r/CHANGELOG.md"           # skipped
  printf '# Old\n## v6 notes\n' > "$t/r/archive/v6/old.md"                 # skipped
  git -C "$t/r" add -A
  bash "$0" --root "$t/r" > "$t/out"; a=$?; n=$(grep -oE 'count=[0-9]+' "$t/out")
  bash "$0" --root "$t/nope" > /dev/null 2>&1; b=$?
  rm "$t/r/v7/rules.md" "$t/r/core/guide.md" "$t/r/core/spec-6.3.0.md"; git -C "$t/r" add -A
  bash "$0" --root "$t/r" > "$t/out"; c=$?; m=$(grep -oE 'count=[0-9]+' "$t/out")
  got="$a $n $b $c $m"
  [ "$got" = "0 count=3 1 0 count=0" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: got=[$got] want=[0 count=3 1 0 count=0]"; label insufficient_evidence selftest_broken; exit 1
fi

prefix=$(git -C "$ROOT" rev-parse --show-prefix) || { label insufficient_evidence not_a_git_repo; exit 1; }
[ -z "$prefix" ] || { label insufficient_evidence root_is_subdirectory "run from the repo root"; exit 1; }
files=$(git -C "$ROOT" ls-files -- ':(exclude)archive/') || { label insufficient_evidence git_ls_files_failed; exit 1; }
[ -n "$files" ] || { label insufficient_evidence no_tracked_files; exit 1; }

# Matching in perl, not grep -P: BSD grep has no -P, and a failed match must never read as "clean" (G2).
names=$(printf '%s\n' "$files" | perl -ne 'print if m{(^|[/_.-])v[0-9]+([/_.-]|$)|(^|[/_-])[0-9]+\.[0-9]+(\.[0-9]+)?([/_-]|\.[a-z]+$|$)}') \
  || { label insufficient_evidence name_scan_failed; exit 1; }
mds=$(printf '%s\n' "$files" | perl -ne 'print if /\.md$/ && !m{(^|/)CHANGELOG\.md$}')
heads=""
if [ -n "$mds" ]; then
  heads=$(cd "$ROOT" && printf '%s\n' "$mds" | tr '\n' '\0' | xargs -0 perl -ne 'print "$ARGV:$.: $_" if /^#{1,6} .*(\bv[0-9]+\b|\b[0-9]+\.[0-9]+(\.[0-9]+)?\b)/; close ARGV if eof') \
    || { label insufficient_evidence heading_scan_failed; exit 1; }
fi
count=0
[ -n "$names" ] && while IFS= read -r l; do echo "name: $l"; done <<<"$names" && count=$((count+$(printf '%s\n' "$names" | wc -l)))
[ -n "$heads" ] && while IFS= read -r l; do echo "heading: $l"; done <<<"$heads" && count=$((count+$(printf '%s\n' "$heads" | wc -l)))
count=$((count))
echo "count=$count"
[ $count -gt 0 ] && { label pass "advisory_count_$count" "remove_the_version_from_each_name_or_heading_listed_above"; exit 0; }
label pass clean; exit 0
