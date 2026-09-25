#!/usr/bin/env bash
# C21-4 (G4): every lop=ADVISORY row in a `## Luật v7` table must carry a COUNTER + a DEADLINE.
#   Deadline: token `deadline=YYYY-MM-DD` inside the `ca_dot` cell (no new column — table header stays as in 21 §1).
#   Counter:  the row's `lenh` prints `count=<n>` on stdout (last occurrence wins).
#   Burn case: a "kill" gate for an internal tool ran 8 days past its deadline with its deciding metric still
#   "NOT MEASURED"; nobody escalated it, nobody deleted it — an advisory gate that was dead yet stayed green.
# Exit codes (21 §1): 0 pass · 1 cannot measure · 2 violation.
#   missing/malformed `deadline=` ⇒ 2 (mis-declared, G4) · past deadline ∧ count>0 ⇒ 2 · `lenh` prints no `count=` ⇒ 1
#   --goc missing / no `## Luật v7` table at all ⇒ 1 · tables exist but 0 ADVISORY rows ⇒ 0 (advisory=0).
# Usage: check-advisory-deadline.sh [--goc DIR] [--selftest]
# ponytail: only runs `lenh` of rows with pham_vi_chay=FRAMEWORK_REPO (empty = FRAMEWORK_REPO); other rows get the
#   deadline check only and are counted as other_scope — add --pham-vi-chay once a PRODUCT_CI advisory row exists.
set -u
GOC=.; SELFTEST=0
label() { echo "result=$1 gate=check-advisory-deadline reason=$2"; }
while [ $# -gt 0 ]; do case $1 in
  --goc) GOC=${2:-}; shift;; --selftest) SELFTEST=1;;
  *) echo "CANNOT MEASURE: unknown argument $1"; label insufficient_evidence unknown_argument; exit 1;; esac; shift; done
# An ADVISORY row whose `lenh` calls back into this gate would recurse forever. Stop and report cannot-measure.
[ -n "${CHECK_ADVISORY_DEADLINE_RUNNING:-}" ] && { echo "CANNOT MEASURE: recursion"; label insufficient_evidence recursion; exit 1; }

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); mkdir -p "$t/s"
  printf 'echo "count=3"\nexit 0\n' > "$t/s/count3.sh"; printf 'echo "count=0"\nexit 0\n' > "$t/s/count0.sh"
  printf 'echo "no counter here"\nexit 0\n' > "$t/s/no-count.sh"
  H='# f\n## Luật v7\n| id | lop | lenh | ca_dot | pham_vi_chay |\n|---|---|---|---|---|\n'
  row() { printf "$H"'| A | ADVISORY | `bash s/%s` | %s | FRAMEWORK_REPO |\n| M | MACHINE | `bash s/count3.sh` | case | |\n' "$1" "$2" > "$t/rules.md"
          bash "$0" --goc "$t" >/dev/null; echo -n $?; }
  r=$(row count3.sh 'case deadline=2000-01-01')         # red: past deadline, count=3
  r=$r$(row count3.sh 'case without a deadline')        # red: deadline missing
  r=$r$(row count3.sh 'case deadline=2999-01-01')       # green: deadline in the future
  r=$r$(row count0.sh 'case deadline=2000-01-01')       # green: past deadline but count=0
  r=$r$(row no-count.sh 'case deadline=2999-01-01')     # 1: lenh prints no count=
  bash "$0" --goc "$t/missing" >/dev/null 2>&1; r=$r$?                     # 1: unknown --goc
  printf '# f\n## Luật v7\n| id | lop | lenh | ca_dot |\n|---|---|---|---|\n| M | MACHINE | `bash s/count3.sh` | case |\n' > "$t/rules.md"
  o=$(bash "$0" --goc "$t"); r=$r$?                                        # 0: table, no ADVISORY rows
  case $o in *advisory=0*) ;; *) r=${r}x;; esac
  printf '# f\nno table\n' > "$t/rules.md"; bash "$0" --goc "$t" >/dev/null; r=$r$?   # 1: no table at all
  rm -rf "$t"
  [ "$r" = 22001101 ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: $r (want 22001101)"; label insufficient_evidence selftest_broken; exit 1  # broken selftest = broken GATE ⇒ 1, not 2
fi

[ -n "$GOC" ] && cd "$GOC" || { echo "CANNOT MEASURE: cannot enter --goc '$GOC'"; label insufficient_evidence goc_missing; exit 1; }

# Rows of every `## Luật v7` table in any .md (skip 10-Archive, .git). Columns located by header NAME —
# a wrong header is kiem-luat-v7.sh's job to flag. \037 instead of tab: tab is IFS whitespace ⇒ empty cells collapse.
rows=$(find . -name '*.md' -not -path './10-Archive/*' -not -path './.git/*' -exec awk '
  FNR==1 {t=0; b=0}
  /^## / {t=($0 ~ /^## Luật v7[[:space:]]*$/); b=0; next}
  !/^\|/ {b=0; next}
  !t || /^\|[-: |]+\|$/ {next}
  { n=split($0,c,"|"); for(i=2;i<n;i++) gsub(/^[[:space:]]+|[[:space:]]+$/,"",c[i])
    if (!b) { b=1; split("",k); for(i=2;i<n;i++) k[c[i]]=i; ok=("lop" in k)&&("lenh" in k)&&("ca_dot" in k); print "__TABLE__"; next }
    if (ok) print FILENAME "\037" c[k["lop"]] "\037" c[k["lenh"]] "\037" c[k["ca_dot"]] "\037" (("pham_vi_chay" in k) ? c[k["pham_vi_chay"]] : "") }' {} +)
tables=$(grep -c '^__TABLE__$' <<<"$rows")
[ "$tables" -gt 0 ] || { echo "CANNOT MEASURE: no ## Luật v7 table under $GOC"; label insufficient_evidence no_table; exit 1; }

today=$(date +%F); advisory=0; on_time=0; overdue=0; missing_deadline=0; unmeasurable=0; other_scope=0
while IFS=$'\037' read -r f lop lenh ca_dot pv; do
  [ "$lop" = ADVISORY ] || continue
  lenh=${lenh#\`}; lenh=${lenh%\`}
  [ -n "$lenh" ] || continue   # no lenh ⇒ reference (21 §1), not a rule
  advisory=$((advisory+1))
  dl=$(grep -oE 'deadline=[0-9]{4}-[0-9]{2}-[0-9]{2}' <<<"$ca_dot" | tail -n 1); dl=${dl#deadline=}
  if [ -z "$dl" ]; then missing_deadline=$((missing_deadline+1)); echo "RED — mis-declared G4 (ca_dot has no deadline=YYYY-MM-DD): $lenh ($f)"; continue; fi
  [ "${pv:-FRAMEWORK_REPO}" = FRAMEWORK_REPO ] || { other_scope=$((other_scope+1)); continue; }
  out=$(CHECK_ADVISORY_DEADLINE_RUNNING=1 bash -c "$lenh" </dev/null); m=$?
  n=$(grep -oE 'count=[0-9]+' <<<"$out" | tail -n 1); n=${n#count=}
  if [ -z "$n" ]; then unmeasurable=$((unmeasurable+1)); echo "RED — cannot measure (lenh printed no count=, exit $m): $lenh ($f)"; continue; fi
  if [[ $dl < $today ]] && [ "$n" -gt 0 ]; then
    overdue=$((overdue+1)); echo "RED — deadline $dl passed with count=$n: escalate to REVIEW or delete the rule (G4): $lenh ($f)"
  else on_time=$((on_time+1)); fi
done <<<"$rows"

echo "tables=$tables advisory=$advisory on_time=$on_time overdue=$overdue missing_deadline=$missing_deadline unmeasurable=$unmeasurable other_scope=$other_scope"
[ $((overdue+missing_deadline)) -gt 0 ] && { label violation "overdue_${overdue}_missing_deadline_$missing_deadline"; exit 2; }
[ $unmeasurable -gt 0 ] && { label insufficient_evidence "unmeasurable_$unmeasurable"; exit 1; }
label pass "advisory_$advisory"; exit 0
