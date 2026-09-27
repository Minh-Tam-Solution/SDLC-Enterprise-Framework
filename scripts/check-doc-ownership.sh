#!/usr/bin/env bash
# Rule DOC-2: every live document states its Status and names an Owner, a Consumer and a Review-by date,
#   and the date has not passed.
#   Burn case: v6.x reached 189 live docs and nobody could say which were still true; DEPRECATION-POLICY.md
#   still said ACTIVE for Framework 6.3.0 six months and one major version later. A count ceiling only
#   limited the number; it said nothing about whether a document had an owner, a reader, or was still right.
# Live documents = tracked *.md outside archive/ and templates/ (the same set check-doc-count.sh counts).
# Fields are read from the first 30 lines outside fenced code blocks (an example header in a code block is
#   not the document's header), as `**Owner**: <value>` (a value ends at " · ", " | " or end of line):
#   Status     — DRAFT · ACTIVE · DEPRECATED · SUPERSEDED (policies/artifact-lifecycle.md); ARCHIVED is not a
#                live status — an archived document lives under archive/, which this gate does not scan
#   Owner      — who answers questions and keeps it true (a role or handle; not empty, "<…>", TBD, TODO)
#   Consumer   — who reads or runs it, named (same rule)
#   Review by  — YYYY-MM-DD, a real date, not earlier than today
# Exit codes (controls/rule-contract.md): 0 pass · 1 cannot measure · 2 violation. Last stdout line is the label.
# DOC_OWNERSHIP_TODAY=YYYY-MM-DD overrides today's date (selftest only).
set -u
ROOT=.; SELFTEST=0
label() { echo "result=$1 gate=check-doc-ownership reason=$2${3:+ fix=$3}"; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT=${2:-}; shift;; --selftest) SELFTEST=1;;
  *) label insufficient_evidence unknown_argument; exit 1;; esac; shift; done

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
  mkdir -p "$t/r/core" "$t/r/archive" "$t/r/templates" && git -C "$t/r" init -q \
    || { label insufficient_evidence selftest_setup_failed; exit 1; }
  ok='**Status**: ACTIVE\n**Owner**: @maintainer\n**Consumer**: developers starting a repo\n**Review by**: 2026-12-31\n'
  printf "# Good\n\n$ok" > "$t/r/core/good.md"
  printf '# Inline\n\n**Version**: 1.0.0 | **Status**: DRAFT · **Owner**: @m · **Consumer**: gate authors · **Review by**: 2026-12-31\n' > "$t/r/core/inline.md"
  git -C "$t/r" add -A
  bash "$0" --root "$t/r" > "$t/out"; a=$?                                            # clean => 0
  printf '# No owner\n\n**Status**: ACTIVE\n**Consumer**: x\n**Review by**: 2026-12-31\n' > "$t/r/core/no-owner.md"
  printf '# Placeholder\n\n**Status**: ACTIVE\n**Owner**: @m\n**Consumer**: <who reads this>\n**Review by**: 2026-12-31\n' > "$t/r/core/placeholder.md"
  printf '# Overdue\n\n**Status**: ACTIVE\n**Owner**: @m\n**Consumer**: x\n**Review by**: 2026-01-01\n' > "$t/r/core/overdue.md"
  printf '# Bad date\n\n**Status**: ACTIVE\n**Owner**: @m\n**Consumer**: x\n**Review by**: 2026-02-30\n' > "$t/r/core/bad-date.md"
  printf '# Fenced only\n\n```\n**Status**: ACTIVE\n**Owner**: @m\n**Consumer**: x\n**Review by**: 2026-12-31\n```\n' > "$t/r/core/fenced.md"
  printf '# Bad status\n\n**Status**: ALPHA\n**Owner**: @m\n**Consumer**: x\n**Review by**: 2026-12-31\n' > "$t/r/core/bad-status.md"
  printf '# Archived but live\n\n**Status**: ARCHIVED\n**Owner**: @m\n**Consumer**: x\n**Review by**: 2026-12-31\n' > "$t/r/core/archived-live.md"
  printf '# Archived\n' > "$t/r/archive/old.md"; printf '# Template\n' > "$t/r/templates/t.md"   # skipped
  git -C "$t/r" add -A
  bash "$0" --root "$t/r" > "$t/out"; b=$?; n=$(grep -oE 'count=[0-9]+' "$t/out")
  bash "$0" --root "$t/nope" > /dev/null 2>&1; c=$?                                   # no repo => 1
  got="$a $b $n $c"
  [ "$got" = "0 2 count=10 1" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: got=[$got] want=[0 2 count=10 1]"; cat "$t/out"; label insufficient_evidence selftest_broken; exit 1
fi

prefix=$(git -C "$ROOT" rev-parse --show-prefix 2>&1) || { label insufficient_evidence not_a_git_repo; exit 1; }
[ -z "$prefix" ] || { label insufficient_evidence root_is_subdirectory "run from the repo root"; exit 1; }
docs=$(git -C "$ROOT" ls-files -- '*.md' ':(exclude)archive/' ':(exclude)templates/') \
  || { label insufficient_evidence git_ls_files_failed; exit 1; }
[ -n "$docs" ] || { label insufficient_evidence no_live_docs; exit 1; }
today=${DOC_OWNERSHIP_TODAY:-$(date +%F)}

# perl does the reading and the date check; it prints one line per problem and exits 3 on its own failure.
out=$(cd "$ROOT" && printf '%s\n' "$docs" | TODAY="$today" perl -e '
  use strict; use warnings; use Time::Local qw(timegm);
  my $today = $ENV{TODAY}; my $bad = 0;
  while (my $f = <STDIN>) {
    chomp $f; next unless length $f;
    open(my $fh, "<", $f) or do { print "UNREADABLE $f\n"; exit 3 };
    my %v; my $n = 0; my $fence = 0;
    while (my $l = <$fh>) {
      last if ++$n > 30;
      if ($l =~ /^\s*(```|~~~)/) { $fence = !$fence; next }
      next if $fence;
      for my $k ("Status", "Owner", "Consumer", "Review by") {
        $v{$k} //= $1 if $l =~ /\*\*\Q$k\E\*\*:\s*(.*?)\s*(?: · | \| |$)/;
      }
    }
    close $fh;
    my $st = $v{"Status"} // "";
    unless ($st =~ /^(DRAFT|ACTIVE|DEPRECATED|SUPERSEDED)\b/) { print "RED $f: Status missing or not a live status (DRAFT, ACTIVE, DEPRECATED, SUPERSEDED)\n"; $bad++; }
    for my $k ("Owner", "Consumer") {
      my $x = $v{$k} // "";
      if ($x eq "" || $x =~ /^<.*>$/ || $x =~ /^(TBD|TODO|tbd|todo)$/) { print "RED $f: $k missing or placeholder\n"; $bad++; }
    }
    my $d = $v{"Review by"} // "";
    if ($d !~ /^(\d{4})-(\d{2})-(\d{2})$/) { print "RED $f: Review by missing or not YYYY-MM-DD\n"; $bad++; next; }
    my ($y, $m, $dd) = ($1, $2, $3);
    unless (eval { timegm(0, 0, 0, $dd, $m - 1, $y); 1 }) { print "RED $f: Review by is not a real date ($d)\n"; $bad++; next; }
    if ($d lt $today) { print "RED $f: review overdue since $d\n"; $bad++; }
  }
  print "count=$bad\n";
') || { echo "$out"; label insufficient_evidence scan_failed; exit 1; }
echo "$out"
n=$(grep -oE '^count=[0-9]+' <<<"$out" | cut -d= -f2)
[ -n "$n" ] || { label insufficient_evidence no_count; exit 1; }
[ "$n" -gt 0 ] && { label violation "docs_$n" "add_Status_Owner_Consumer_Review-by_to_each_listed_doc_or_review_it_and_move_the_date"; exit 2; }
label pass clean; exit 0
