#!/usr/bin/env bash
# check-pr-approver.sh: does this PR have a human approval that counts? (candidate C-A02-1, PRODUCT_CI)
#
# Rule under test: "Human APPROVES the merge" (02-Agent-Accountability, 01 "Approve before merge").
# An approval counts only if ALL of these hold:
#   state == APPROVED                   (COMMENTED / CHANGES_REQUESTED / DISMISSED never count)
#   reviewer login is in the approvers file
#   reviewer != PR author
#   reviewer != operator of the PR author (a human approving their own agent's PR is not independent)
#   reviewer is not a bot               (user.type == Bot or login ends in [bot])
#   review commit_id == current head SHA  (an approval on an older commit does not cover new commits)
#
# Exit codes (v7/01-rule-contract.md): 0 pass · 1 insufficient evidence · 2 violation.
#   1 = approvers file missing/empty · gh/jq missing or unauthenticated · API error ·
#       PR author is marked `shared` in the approvers file (one account used by a human AND an agent:
#       nobody can tell who wrote the change, so "reviewer != author" cannot be evaluated) ·
#       PR author is a listed bot with no `operated_by=` (reason=bot_operator_unknown: its operator
#       could approve the PR and nobody would know).
#   2 = no approval satisfies all six conditions.
# Last stdout line is the label: result=<pass|insufficient_evidence|violation> gate=pr-approver reason=<slug> [fix=<text>]
#   (rule contract: fix= is optional and always the LAST field; it takes the rest of the line, spaces included)
#
# Approvers file: one GitHub login per line; `#` starts a comment; optional second word `shared`
# marks an account that a human and an agent both operate. A line `bot:<bot-login> operated_by=<human-login>`
# maps an agent identity to the human who runs it; bot lines are never approvers. Example:
#   alice
#   bob shared
#   bot:build-agent[bot] operated_by=alice
# Old files (logins and `shared` only) mean the same as before. Only LISTED bots are mapped: an agent
# identity missing from the file is treated as an ordinary author, so list every agent identity.
# Read the approvers file from the PR's BASE commit, not its head: otherwise the PR under review can
# edit its own approver list (the reusable workflow v7-gates-product.yml does this).
#
# Usage: check-pr-approver.sh --repo owner/name --pr N [--approvers FILE]   (default FILE: .approvers)
#        check-pr-approver.sh --selftest    # local JSON fixtures, no network
# GH_FIXTURE_DIR=dir: read pr.json + reviews.json from dir instead of calling the API (used by --selftest).
set -uo pipefail
gate=pr-approver
label() { echo "result=$1 gate=$gate reason=$2${3:+ fix=$3}"; }
unmeasurable() { echo "$1" >&2; label insufficient_evidence "$2"; exit 1; }

REPO=""; PR=""; APPROVERS=.approvers; SELFTEST=0
while [ $# -gt 0 ]; do case $1 in
  --repo) REPO=${2:-}; shift;; --pr) PR=${2:-}; shift;; --approvers) APPROVERS=${2:-}; shift;;
  --selftest) SELFTEST=1;;
  *) unmeasurable "unknown argument: $1" bad_argument;; esac; shift; done

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
  head=aaa111; old=bbb222
  printf 'alice\nbob\ncarol shared\ncopilot-pull-request-reviewer[bot]\nbot:agent-x[bot] operated_by=alice\nbot:agent-y[bot]\nbot:agent-z operated_by=bob\n' > "$t/approvers"
  # case <name> <want_rc> <author> <reviews-json> [approvers-file]
  fails=0
  run_case() {
    d="$t/$1"; mkdir -p "$d"
    printf '{"user":{"login":"%s","type":"User"},"head":{"sha":"%s"}}' "$3" "$head" > "$d/pr.json"
    printf '%s' "$4" > "$d/reviews.json"
    out=$(GH_FIXTURE_DIR="$d" bash "$0" --repo o/r --pr 1 --approvers "${5:-$t/approvers}" 2>"$d/stderr"); rc=$?
    lab=${out##*$'\n'}
    case $2 in 0) w=pass;; 1) w=insufficient_evidence;; 2) w=violation;; esac
    if [ "$rc" = "$2" ] && [[ $lab == "result=$w gate=$gate "* ]]; then echo "ok   $1 (rc=$rc)"
    else echo "FAIL $1: want rc=$2/$w got rc=$rc label=[$lab]"; fails=$((fails+1)); fi
  }
  R() { printf '{"user":{"login":"%s","type":"%s"},"state":"%s","commit_id":"%s"}' "$@"; }
  run_case bot-commented-only   2 alice "[$(R 'copilot-pull-request-reviewer[bot]' Bot COMMENTED $head)]"
  run_case bot-approved         2 alice "[$(R 'copilot-pull-request-reviewer[bot]' Bot APPROVED $head)]"
  run_case approved-right-sha   0 alice "[$(R bob User APPROVED $head)]"
  run_case approved-stale-sha   2 alice "[$(R bob User APPROVED $old)]"
  run_case approver-not-listed  2 alice "[$(R mallory User APPROVED $head)]"
  run_case self-approval        2 alice "[$(R alice User APPROVED $head)]"
  run_case approvers-missing    1 alice "[$(R bob User APPROVED $head)]" "$t/does-not-exist"
  run_case author-shared        1 carol "[$(R bob User APPROVED $head)]"
  run_case no-reviews           2 alice "[]"
  run_case operator-approves-own-bot   2 'agent-x[bot]' "[$(R alice User APPROVED $head)]"
  run_case other-human-approves-bot    0 'agent-x[bot]' "[$(R bob User APPROVED $head)]"
  run_case bot-without-operator        1 'agent-y[bot]' "[$(R bob User APPROVED $head)]"
  run_case operator-of-machine-user    2 agent-z        "[$(R bob User APPROVED $head)]"   # a bot that is a plain User account
  if [ $fails = 0 ]; then echo "selftest OK"; label pass selftest_ok; exit 0; fi
  echo "selftest BROKEN: $fails case(s)"; label insufficient_evidence selftest_broken; exit 1  # broken gate = cannot measure, not a violation
fi

[ -n "$REPO" ] && [ -n "$PR" ] || unmeasurable "need --repo owner/name --pr N" missing_argument
command -v jq >/dev/null || unmeasurable "jq not installed" jq_missing
[ -s "$APPROVERS" ] || unmeasurable "approvers file missing or empty: $APPROVERS" approvers_file_missing
listed=$(sed 's/#.*//' "$APPROVERS" | awk 'NF && $1 !~ /^bot:/ {print $1}')
shared=$(sed 's/#.*//' "$APPROVERS" | awk '$1 !~ /^bot:/ && $2=="shared" {print $1}')
[ -n "$listed" ] || unmeasurable "approvers file has no logins: $APPROVERS" approvers_file_empty

if [ -n "${GH_FIXTURE_DIR:-}" ]; then
  pr_json=$(cat "$GH_FIXTURE_DIR/pr.json") || unmeasurable "fixture pr.json unreadable" fixture_missing
  rv_json=$(cat "$GH_FIXTURE_DIR/reviews.json") || unmeasurable "fixture reviews.json unreadable" fixture_missing
else
  command -v gh >/dev/null || unmeasurable "gh not installed" gh_missing
  gh auth status >/dev/null 2>&1 || [ -n "${GH_TOKEN:-${GITHUB_TOKEN:-}}" ] || unmeasurable "gh not authenticated" gh_unauthenticated
  pr_json=$(gh api "repos/$REPO/pulls/$PR") || unmeasurable "API error reading PR $REPO#$PR" api_error_pr
  # --paginate prints one array per page; jq -s 'add' joins them.
  rv_json=$(gh api --paginate "repos/$REPO/pulls/$PR/reviews" | jq -s 'add // []') || unmeasurable "API error reading reviews" api_error_reviews
fi

author=$(jq -r '.user.login // empty' <<<"$pr_json"); head_sha=$(jq -r '.head.sha // empty' <<<"$pr_json")
[ -n "$author" ] && [ -n "$head_sha" ] || unmeasurable "PR JSON has no author or head sha" pr_json_incomplete
grep -qxF -- "$author" <<<"$shared" && unmeasurable "author $author is a shared human+agent account" author_is_shared_account
# Author is a listed bot? bot="listed <operator>" (operator may be empty) · not listed: bot="".
bot=$(sed 's/#.*//' "$APPROVERS" | awk -v a="$author" '$1=="bot:" a {op=""; for(i=2;i<=NF;i++) if($i ~ /^operated_by=/) op=substr($i,13); print "listed " op; exit}')
operator=${bot#listed }
[ -n "$bot" ] && [ -z "$operator" ] && unmeasurable "author $author is a listed bot with no operated_by=<human>" bot_operator_unknown

# Approver list goes in via ENVIRON, not -v: BSD awk rejects a -v value containing newlines.
# One TSV row per review: login, type, state, commit_id. Deleted users (user=null) become "ghost".
tally=$(jq -r '.[] | [(.user.login // "ghost"), (.user.type // "User"), .state, (.commit_id // "")] | @tsv' <<<"$rv_json" |
  L="$listed" awk -F'\t' -v a="$author" -v o="$operator" -v h="$head_sha" '
    BEGIN { n=split(ENVIRON["L"], x, "\n"); for (i=1;i<=n;i++) ok[x[i]]=1 }
    { total++ }
    $2=="Bot" || $1 ~ /\[bot\]$/ { bot++; next }
    $3!="APPROVED"               { not_approved++; next }
    $1==a                        { self++; next }
    o!="" && $1==o               { operator++; next }
    !($1 in ok)                  { not_listed++; next }
    $4!=h                        { stale_sha++; next }
                                 { valid++; who=$1 }
    END { printf "reviews=%d bot=%d not_approved=%d self=%d operator=%d not_listed=%d stale_sha=%d valid=%d who=%s\n",
          total, bot, not_approved, self, operator, not_listed, stale_sha, valid, (who==""?"-":who) }') || unmeasurable "could not parse reviews JSON" reviews_json_unparseable
echo "$REPO#$PR author=$author operator=${operator:--} head=${head_sha:0:12} $tally" >&2
valid=$(grep -oE 'valid=[0-9]+' <<<"$tally" | cut -d= -f2)
[ "${valid:-0}" -gt 0 ] && { label pass "approved_by_$(grep -oE 'who=[^ ]+' <<<"$tally" | cut -d= -f2)"; exit 0; }
label violation no_valid_approval "request an APPROVED review on the current head from a listed approver who is neither the author nor its operator"
exit 2
