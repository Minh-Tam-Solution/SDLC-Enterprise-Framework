#!/usr/bin/env bash
# C21-4 (G4): every class=ADVISORY row in a `## Rules v7` table (controls/rule-contract.md) must carry a COUNTER + a DEADLINE.
#   Deadline: token `deadline=YYYY-MM-DD` inside the `burn_case` cell (no extra column).
#   Counter:  the row's `cmd` prints `count=<n>` on stdout (last occurrence wins).
#   Burn case: a "kill" gate for an internal tool ran 8 days past its deadline with its deciding metric still
#   "NOT MEASURED"; nobody escalated it, nobody deleted it — an advisory gate that was dead yet stayed green.
# Exit codes (controls/rule-contract.md §1): 0 pass · 1 cannot measure · 2 violation.
#   missing/malformed `deadline=` ⇒ 2 (mis-declared, G4) · past deadline ∧ count>0 ⇒ 2 · `cmd` prints no `count=` ⇒ 1
#   cmd exits other than 0/2 ⇒ 1 (a count from a failing cmd is not evidence) · a table header without
#   class/cmd/burn_case ⇒ 1 (its rows are invisible here — G1, not "clean")
#   --goc missing / no `## Rules v7` table at all ⇒ 1 · tables exist but 0 ADVISORY rows ⇒ 0 (advisory=0).
# Usage: check-advisory-deadline.sh [--goc DIR] [--selftest]
# ponytail: only runs `cmd` of rows with run_scope=FRAMEWORK_REPO (empty = FRAMEWORK_REPO); other rows get the
#   deadline check only and are counted as other_scope — add a --run-scope flag once a PRODUCT_CI advisory row exists.
set -u
GOC=.; SELFTEST=0
label() { echo "result=$1 gate=check-advisory-deadline reason=$2"; }
while [ $# -gt 0 ]; do case $1 in
  --goc) GOC=${2:-}; shift;; --selftest) SELFTEST=1;;
  *) echo "CANNOT MEASURE: unknown argument $1"; label insufficient_evidence unknown_argument; exit 1;; esac; shift; done
# An ADVISORY row whose `cmd` calls back into this gate would recurse forever. Stop and report cannot-measure.
[ -n "${CHECK_ADVISORY_DEADLINE_RUNNING:-}" ] && { echo "CANNOT MEASURE: recursion"; label insufficient_evidence recursion; exit 1; }

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); mkdir -p "$t/s"
  printf 'echo "count=3"\nexit 0\n' > "$t/s/count3.sh"; printf 'echo "count=0"\nexit 0\n' > "$t/s/count0.sh"
  printf 'echo "no counter here"\nexit 0\n' > "$t/s/no-count.sh"; printf 'echo "count=0"\nexit 1\n' > "$t/s/count0-broken.sh"
  H='# f\n## Rules v7\n| id | class | cmd | burn_case | run_scope |\n|---|---|---|---|---|\n'
  row() { printf "$H"'| A | ADVISORY | `bash s/%s` | %s | FRAMEWORK_REPO |\n| M | MACHINE | `bash s/count3.sh` | case | |\n' "$1" "$2" > "$t/rules.md"
          bash "$0" --goc "$t" >/dev/null; echo -n $?; }
  r=$(row count3.sh 'case deadline=2000-01-01')         # red: past deadline, count=3
  r=$r$(row count3.sh 'case without a deadline')        # red: deadline missing
  r=$r$(row count3.sh 'case deadline=2999-01-01')       # green: deadline in the future
  r=$r$(row count0.sh 'case deadline=2000-01-01')       # green: past deadline but count=0
  r=$r$(row no-count.sh 'case deadline=2999-01-01')     # 1: cmd prints no count=
  r=$r$(row count0-broken.sh 'case deadline=2000-01-01') # 1: count=0 but cmd exited 1
  bash "$0" --goc "$t/missing" >/dev/null 2>&1; r=$r$?                     # 1: unknown --goc
  printf '# f\n## Rules v7\n| id | class | cmd | burn_case |\n|---|---|---|---|\n| M | MACHINE | `bash s/count3.sh` | case |\n' > "$t/rules.md"
  o=$(bash "$0" --goc "$t"); r=$r$?                                        # 0: table, no ADVISORY rows
  case $o in *advisory=0*) ;; *) r=${r}x;; esac
  printf '# f\nno table\n' > "$t/rules.md"; bash "$0" --goc "$t" >/dev/null; r=$r$?   # 1: no table at all
  printf '# f\n## Rules v7\n| id | lop | lenh | ca_dot |\n|---|---|---|---|\n| A | ADVISORY | `bash s/count3.sh` | case |\n' > "$t/rules.md"
  bash "$0" --goc "$t" >/dev/null; r=$r$?                                  # 1: header without class/cmd/burn_case
  rm -rf "$t"
  [ "$r" = 2200111011 ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: $r (want 2200111011)"; label insufficient_evidence selftest_broken; exit 1  # broken selftest = broken GATE ⇒ 1, not 2
fi

[ -n "$GOC" ] && cd "$GOC" || { echo "CANNOT MEASURE: cannot enter --goc '$GOC'"; label insufficient_evidence goc_missing; exit 1; }

# Rows of every `## Rules v7` table in any .md (skip archive, .git). Columns located by header NAME —
# a wrong header is the rules runner's job to flag. \037 instead of tab: tab is IFS whitespace ⇒ empty cells collapse.
rows=$(find . -name '*.md' -not -path './archive/*' -not -path './.git/*' -exec awk '
  FNR==1 {t=0; b=0}
  /^## / {t=($0 ~ /^## Rules v7[[:space:]]*$/); b=0; next}
  !/^\|/ {b=0; next}
  !t || /^\|[-: |]+\|$/ {next}
  { n=split($0,c,"|"); for(i=2;i<n;i++) gsub(/^[[:space:]]+|[[:space:]]+$/,"",c[i])
    if (!b) { b=1; split("",k); for(i=2;i<n;i++) k[c[i]]=i; ok=("class" in k)&&("cmd" in k)&&("burn_case" in k); print (ok ? "__TABLE__" : "__BAD_HEADER__\037" FILENAME); next }
    if (ok) print FILENAME "\037" c[k["class"]] "\037" c[k["cmd"]] "\037" c[k["burn_case"]] "\037" (("run_scope" in k) ? c[k["run_scope"]] : "") }' {} +)
tables=$(grep -c '^__TABLE__$' <<<"$rows"); bad_header=$(grep -c '^__BAD_HEADER__' <<<"$rows")
grep '^__BAD_HEADER__' <<<"$rows" | while IFS=$'\037' read -r _ f; do echo "RED — cannot measure (header lacks class/cmd/burn_case): $f"; done
[ $((tables+bad_header)) -gt 0 ] || { echo "CANNOT MEASURE: no ## Rules v7 table under $GOC"; label insufficient_evidence no_table; exit 1; }

today=$(date +%F); advisory=0; on_time=0; overdue=0; missing_deadline=0; unmeasurable=0; other_scope=0
while IFS=$'\037' read -r f class cmd burn_case scope; do
  [ "$class" = ADVISORY ] || continue   # also skips the __TABLE__/__BAD_HEADER__ marker lines
  cmd=${cmd#\`}; cmd=${cmd%\`}
  [ -n "$cmd" ] || continue   # no cmd ⇒ reference (§1), not a rule
  advisory=$((advisory+1))
  dl=$(grep -oE 'deadline=[0-9]{4}-[0-9]{2}-[0-9]{2}' <<<"$burn_case" | tail -n 1); dl=${dl#deadline=}
  if [ -z "$dl" ]; then missing_deadline=$((missing_deadline+1)); echo "RED — mis-declared G4 (burn_case has no deadline=YYYY-MM-DD): $cmd ($f)"; continue; fi
  [ "${scope:-FRAMEWORK_REPO}" = FRAMEWORK_REPO ] || { other_scope=$((other_scope+1)); continue; }
  out=$(CHECK_ADVISORY_DEADLINE_RUNNING=1 bash -c "$cmd" </dev/null); m=$?
  n=$(grep -oE 'count=[0-9]+' <<<"$out" | tail -n 1); n=${n#count=}
  if [ -z "$n" ]; then unmeasurable=$((unmeasurable+1)); echo "RED — cannot measure (cmd printed no count=, exit $m): $cmd ($f)"; continue; fi
  case $m in 0|2) ;; *) unmeasurable=$((unmeasurable+1)); echo "RED — cannot measure (cmd exited $m; its count=$n is not evidence): $cmd ($f)"; continue;; esac
  if [[ $dl < $today ]] && [ "$n" -gt 0 ]; then
    overdue=$((overdue+1)); echo "RED — deadline $dl passed with count=$n: escalate to REVIEW or delete the rule (G4): $cmd ($f)"
  else on_time=$((on_time+1)); fi
done <<<"$rows"

echo "tables=$tables bad_header=$bad_header advisory=$advisory on_time=$on_time overdue=$overdue missing_deadline=$missing_deadline unmeasurable=$unmeasurable other_scope=$other_scope"
[ $((overdue+missing_deadline)) -gt 0 ] && { label violation "overdue_${overdue}_missing_deadline_$missing_deadline"; exit 2; }
[ $((unmeasurable+bad_header)) -gt 0 ] && { label insufficient_evidence "unmeasurable_${unmeasurable}_bad_header_$bad_header"; exit 1; }
label pass "advisory_$advisory"; exit 0
