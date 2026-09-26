#!/usr/bin/env bash
# Rule SECRET-1: no secret in the lines a change ADDS. Blocks from day one (recorded exception to the
#   ladder): a pushed secret cannot be un-leaked, and scanning only added lines keeps the noise near zero.
#   Burn case: secrets pushed to shared repos had to be rotated after the fact; deleting them from the
#   tree did not un-leak them (policies/artifact-lifecycle.md).
# Definition, not examples: private-key blocks, and credential formats whose issuer fixes a prefix and a
#   length (cloud access-key ids, code-host tokens, chat-bot tokens, API keys with issuer prefixes).
#   A generic "password = ..." pattern is deliberately NOT here: too noisy to block on.
# Scope: lines added between --base and HEAD. Default base: the merge-base with origin/main; when HEAD is
#   already on origin/main (a push to main), the first parent of HEAD — so a merge commit scans the PR.
# Known findings (old ones, or a false positive) go into .secret-allowlist, one per line:
#   <path>:<first 12 hex of sha256(line)> owner=<who> expires=YYYY-MM-DD reason=<why>
#   An expired entry blocks again. The finding id is printed with each hit.
# --all scans every tracked file at HEAD instead of a diff (report only, exit 0) — to find debt to record.
# Exit codes (controls/rule-contract.md): 0 pass · 1 cannot measure · 2 violation. Last stdout line is the label.
# SECRET_SCAN_TODAY=YYYY-MM-DD overrides today's date (selftest only).
set -u
ROOT=.; BASE=; ALL=0; SELFTEST=0
label() { echo "result=$1 gate=rule-no-new-secrets reason=$2${3:+ fix=$3}"; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT=${2:-}; shift;; --base) BASE=${2:-}; shift;; --all) ALL=1;; --selftest) SELFTEST=1;;
  *) label insufficient_evidence unknown_argument; exit 1;; esac; shift; done

PATTERN='-----BEGIN ((RSA|EC|DSA|OPENSSH|PGP|ENCRYPTED) )?PRIVATE KEY-----|\bAKIA[0-9A-Z]{16}\b|\bgh[pousr]_[A-Za-z0-9]{36,}|\bgithub_pat_[A-Za-z0-9_]{22,}|\bxox[abprs]-[A-Za-z0-9-]{10,}|\bAIza[0-9A-Za-z_-]{35}\b|\bsk-[A-Za-z0-9_-]{20,}|\bglpat-[A-Za-z0-9_-]{20,}'

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
  r="$t/r"; mkdir -p "$r" && git -C "$r" init -q && git -C "$r" config user.email t@t && git -C "$r" config user.name t \
    || { label insufficient_evidence selftest_setup_failed; exit 1; }
  printf 'base\n' > "$r/a.txt"; git -C "$r" add -A && git -C "$r" commit -qm base && base=$(git -C "$r" rev-parse HEAD)
  fake="AKIA""QWERTYUIOPASDFGH"                                   # built at run time: this file holds no key
  printf 'harmless = 1\n' >> "$r/a.txt"; git -C "$r" commit -qam clean
  bash "$0" --root "$r" --base "$base" > "$t/o1"; a=$?                                  # clean diff => 0
  printf 'key = "%s"\n' "$fake" > "$r/cfg.txt"; git -C "$r" add -A; git -C "$r" commit -qm leak
  bash "$0" --root "$r" --base "$base" > "$t/o2"; b=$?                                  # planted key => 2
  id=$(grep -oE 'id=[^ ]+' "$t/o2" | head -1 | cut -d= -f2)
  printf '%s owner=@t expires=2099-01-01 reason=test\n' "$id" > "$r/.secret-allowlist"
  bash "$0" --root "$r" --base "$base" > /dev/null; c=$?                                # allow-listed => 0
  printf '%s owner=@t expires=2000-01-01 reason=test\n' "$id" > "$r/.secret-allowlist"
  bash "$0" --root "$r" --base "$base" > /dev/null; d=$?                                # expired => 2
  bash "$0" --root "$r" --base no-such-ref > /dev/null 2>&1; e=$?                       # bad base => 1
  bash "$0" --root "$t/nope" > /dev/null 2>&1; f=$?                                     # no repo => 1
  got="$a$b$c$d$e$f"
  [ "$got" = "020211" ] && [ -n "$id" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: got=[$got] want=[020211] id=[$id]"; cat "$t/o2"; label insufficient_evidence selftest_broken; exit 1
fi

git -C "$ROOT" rev-parse --git-dir > /dev/null || { label insufficient_evidence not_a_git_repo; exit 1; }
today=${SECRET_SCAN_TODAY:-$(date +%F)}

if [ $ALL = 1 ]; then
  input=$(cd "$ROOT" && git ls-files -z | xargs -0 perl -ne 'if ($. == 1 && -B $ARGV) { close ARGV; next } print "+++ b/$ARGV\n+$_"; close ARGV if eof') \
    || { label insufficient_evidence tree_read_failed; exit 1; }
else
  if [ -z "$BASE" ]; then
    mb=$(git -C "$ROOT" merge-base HEAD origin/main) || { label insufficient_evidence no_origin_main "pass --base <rev> or fetch origin/main"; exit 1; }
    if [ "$mb" = "$(git -C "$ROOT" rev-parse HEAD)" ]; then BASE=$(git -C "$ROOT" rev-parse HEAD^1) || { label insufficient_evidence no_parent; exit 1; }
    else BASE=$mb; fi
  fi
  git -C "$ROOT" rev-parse --verify -q "$BASE^{commit}" > /dev/null || { label insufficient_evidence base_not_found "fetch full history (fetch-depth: 0)"; exit 1; }
  input=$(git -C "$ROOT" diff --no-color --no-ext-diff --unified=0 "$BASE" HEAD) || { label insufficient_evidence diff_failed; exit 1; }
fi

allow="$ROOT/.secret-allowlist"; [ -f "$allow" ] || allow=/dev/null
out=$(printf '%s\n' "$input" | ALLOW="$allow" TODAY="$today" PATTERN="$PATTERN" perl -e '
  use strict; use warnings; use Digest::SHA qw(sha256_hex);
  my (%exp, $f); open(my $a, "<", $ENV{ALLOW}) or exit 3;
  while (<$a>) { next if /^\s*(#|$)/; my ($id) = /^(\S+)/; my ($e) = /expires=(\d{4}-\d{2}-\d{2})/; $exp{$id} = $e // "0000-00-00"; }
  my $re = qr/$ENV{PATTERN}/; my ($hit, $allowed) = (0, 0);
  while (my $l = <STDIN>) {
    if ($l =~ m{^\+\+\+ b/(.*)$}) { $f = $1; next }
    next unless defined $f && $l =~ /^\+/ && $l !~ /^\+\+\+/;
    my $body = substr($l, 1); chomp $body;
    next unless $body =~ $re;
    my $id = "$f:" . substr(sha256_hex($body), 0, 12); my $shown = substr($&, 0, 6) . "…";
    if (exists $exp{$id} && $exp{$id} ge $ENV{TODAY}) { $allowed++; print "ALLOWED id=$id (until $exp{$id})\n"; next }
    $hit++; print "RED — secret-shaped value id=$id match=$shown", (exists $exp{$id} ? " (allow-list entry expired $exp{$id})" : ""), "\n";
  }
  print "count=$hit allowed=$allowed\n";
') || { echo "$out"; label insufficient_evidence scan_failed; exit 1; }
echo "$out"
n=$(grep -oE '^count=[0-9]+' <<<"$out" | cut -d= -f2)
[ -n "$n" ] || { label insufficient_evidence no_count; exit 1; }
[ $ALL = 1 ] && { label pass "report_only_count_$n"; exit 0; }
[ "$n" -gt 0 ] && { label violation "secrets_$n" "remove_the_value_rotate_the_credential_or_record_a_dated_allow-list_entry"; exit 2; }
label pass clean; exit 0
