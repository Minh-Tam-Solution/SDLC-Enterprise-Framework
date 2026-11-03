#!/usr/bin/env bash
# Rule DOC-3: a `file:line` citation in a doc still points inside the cited file, and an anchor still holds.
#   Burn case: standards/documentation.md "One home per fact" — one source is useless if nothing notices when the
#   others diverge; the `Design:` header only checks that a path exists. Model: Minh-Tam-Solution/Mdm PR #465
#   (tests/test_integrate_003_cites.py), re-implemented from its description.
# Definition (tracked *.md under --docs, default docs/; text inside a fence is an example and is not read,
#   except a fence tagged `anchors`):
#   - citation: `dir/file.ext:N` or `dir/file.ext:N-M` (needs a `/`; URLs are stripped first). The file must exist
#     under --root and N (M) must be within 1..lines(file). Absolute or `..` paths are not judged.
#   - anchor: inside a fence tagged `anchors`, one `path:line|text` per line; line `line` of path must contain
#     `text` as a fixed string. A malformed line in that fence is broken, not skipped.
# ADVISORY: prints count=<broken>, exits 0; --block turns count>0 into 2.
# Exit codes (controls/rule-contract.md): 0 pass · 1 cannot measure (not a repo, no docs, nothing to check) ·
#   2 violation (only with --block). Last stdout line is the label.
# Usage: check-doc-cites.sh [--root DIR] [--docs DIR] [--block] [--selftest]
set -u
ROOT=.; DOCS=docs; SELFTEST=0; BLOCK=0
label() { echo "result=$1 gate=check-doc-cites reason=$2${3:+ fix=$3}"; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT=${2:-}; shift;; --docs) DOCS=${2:-}; shift;; --block) BLOCK=1;; --selftest) SELFTEST=1;;
  *) label insufficient_evidence unknown_argument; exit 1;; esac; shift; done

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
  # mk DIR [extra doc line]: one clean doc citing a 3-line file; the extra line plants one case.
  mk() {
    mkdir -p "$1/docs" "$1/src" && git -C "$1" init -q || return 1
    printf 'alpha\nbeta needle\ngamma\n' > "$1/src/a.py"
    { printf '# Doc\n\nSee `src/a.py:2` and src/a.py:1-3, http://h/src/x.py:99 is a URL.\n\n'
      printf '```text\nsrc/a.py:99 is an example in a fence\n```\n\n'
      printf '```anchors\nsrc/a.py:2|needle\n```\n'
      [ -z "${2:-}" ] || printf '%s\n' "$2"; } > "$1/docs/d.md"
    git -C "$1" add -A
  }
  run() { bash "$0" --root "$1" > "$t/out" 2>> "$t/err"; local a=$?
          bash "$0" --root "$1" --block > /dev/null 2>> "$t/err"; local b=$?
          echo "$a$b$(grep -oE '^count=[0-9]+' "$t/out")"; }
  mk "$t/green" || { label insufficient_evidence selftest_setup_failed; exit 1; }
  got="green:$(run "$t/green")"; i=0
  for plant in 'Past the end `src/a.py:4`.' 'Bad range src/a.py:2-9.' 'Gone `src/moved.py:1`.' \
               '```anchors
src/a.py:3|needle
```' '```anchors
not an anchor
```'; do
    i=$((i+1)); mk "$t/red$i" "$plant"; got="$got red$i:$(run "$t/red$i")"
  done
  mk "$t/quiet"; printf 'No citation here.\n' > "$t/quiet/docs/d.md"; git -C "$t/quiet" add -A
  got="$got quiet:$(run "$t/quiet")"                       # nothing to check => 1, not pass
  mkdir "$t/nogit"; got="$got nogit:$(run "$t/nogit")"
  want="green:00count=0 red1:02count=1 red2:02count=1 red3:02count=1 red4:02count=1 red5:02count=1 quiet:11 nogit:11"
  # way out: advisory (no --block) never blocks even when red — the red case above is exit 0 without --block.
  [ "$got" = "$want" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN:"; echo " got=[$got]"; echo "want=[$want]"
  label insufficient_evidence selftest_broken; exit 1
fi

git -C "$ROOT" rev-parse --show-toplevel > /dev/null 2>&1 || { label insufficient_evidence not_a_git_repo; exit 1; }
checked=0; n=0; docs=0
while IFS= read -r -d '' doc; do
  docs=$((docs+1))
  recs=$(awk '
    /^[[:space:]]*```/ { if (fence) { fence = 0; anch = 0 } else { fence = 1; anch = ($0 ~ /^[[:space:]]*```anchors[[:space:]]*$/) } next }
    fence { if (anch && $0 !~ /^[[:space:]]*$/) {
              s = $0; sub(/^[[:space:]]+/, "", s); i = index(s, "|"); p = substr(s, 1, i - 1)
              if (i > 0 && substr(s, i + 1) != "" && match(p, /^[^[:space:]:]+:[0-9]+$/)) { c = index(p, ":"); print "A\t" substr(p, 1, c - 1) "\t" substr(p, c + 1) "\t" substr(s, i + 1) }
              else print "M\t" s }
            next }
    { l = $0; gsub(/https?:\/\/[^[:space:])>]*/, "", l)
      while (match(l, /[A-Za-z0-9_.\/-]+\/[A-Za-z0-9_.-]+\.[A-Za-z0-9]+:[0-9]+(-[0-9]+)?/)) {
        print "C\t" substr(l, RSTART, RLENGTH); l = substr(l, RSTART + RLENGTH) } }' "$ROOT/$doc") || { label insufficient_evidence reader_failed "$doc"; exit 1; }
  while IFS=$'\t' read -r kind a b c; do
    [ -n "$kind" ] || continue
    case $kind in
      M) checked=$((checked+1)); n=$((n+1)); echo "BROKEN $doc: malformed anchor line: $a"; continue;;
      C) tok=$a; p=${tok%%:*}; r=${tok#*:}; lo=${r%%-*}; hi=${r##*-}; txt="";;
      A) p=$a; lo=$b; hi=$b; txt=$c; tok="$a:$b|$c";;
    esac
    case $p in /*|*..*) continue;; esac
    p=${p#./}; checked=$((checked+1))
    [ -f "$ROOT/$p" ] && [ -r "$ROOT/$p" ] || { n=$((n+1)); echo "BROKEN $doc: $tok: no such file"; continue; }
    lines=$(awk 'END { print NR }' "$ROOT/$p") || { label insufficient_evidence reader_failed "$p"; exit 1; }
    if [ "$lo" -lt 1 ] || [ "$hi" -lt "$lo" ] || [ "$hi" -gt "$lines" ]; then
      n=$((n+1)); echo "BROKEN $doc: $tok: outside $p ($lines lines)"; continue; fi
    if [ "$kind" = A ] && ! sed -n "${lo}p" "$ROOT/$p" | command grep -qF -- "$txt"; then
      n=$((n+1)); echo "BROKEN $doc: $tok: text not on that line"; fi
  done <<< "$recs"
done < <(git -C "$ROOT" ls-files -z -- "$DOCS/*.md")
echo "docs=$docs checked=$checked"
# G1: nothing to measure is not "clean".
[ "$docs" -gt 0 ] || { label insufficient_evidence no_docs "pass --docs DIR"; exit 1; }
[ "$checked" -gt 0 ] || { label insufficient_evidence no_citations_found; exit 1; }
echo "count=$n"
[ "$n" -gt 0 ] && [ $BLOCK = 1 ] && { label violation "broken_$n" "fix_or_remove_each_citation_listed_above"; exit 2; }
[ "$n" -gt 0 ] && { label pass "advisory_count_$n" "fix_or_remove_each_citation_listed_above"; exit 0; }
label pass clean; exit 0
