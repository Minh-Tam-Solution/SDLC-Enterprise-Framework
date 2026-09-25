#!/usr/bin/env bash
# Rules v7 Contract gate (§1). Reads ONE canonical table: v7/01-rule-contract.md (owned by F1).
#   FILE section = routing unit · LINE = enforcement unit. A "## Rules v7" section in that file
#   holds the live rules table; anything else in the file is reference (no cmd column value).
#   Table header MUST be |id|class|cmd|burn_case|[run_scope|] — wrong name/order ⇒ misdeclared.
#   Legacy header |id|lop|lenh|ca_dot|[pham_vi_chay|] (and the legacy Vietnamese heading "## Lu?t v7")
#   still ACCEPTED, logs a deprecation notice to stderr, removal 2026-12-31.
#   run_scope ∈ FRAMEWORK_REPO · PRODUCT_CI · RUNTIME_PROBE; missing cell/column = FRAMEWORK_REPO,
#   COUNT ONLY (missing_scope_column). Only rows whose run_scope = --run-scope run (default
#   FRAMEWORK_REPO) — filtered BEFORE running, so a cmd needing another env doesn't fail here for
#   the wrong reason; the rest count as other_scope.
#   Run cmd at repo root. Exit code convention (plan §6.22 A):
#     0 PASS · 1 UNMEASURABLE · 2 VIOLATION · ≥3 reserved (⇒ unmeasurable)
#   1 is the default exit of anything broken (exception, set -e, grep miss) ⇒ it must fall into the
#   honest bucket; "violation" only when the script runs to completion and deliberately returns 2.
#   Label = last line of cmd's STDOUT: result=pass|insufficient_evidence|violation gate=<id> reason=<slug> [fix=<rest of line>]
#     must match the exit code (pass↔0 · insufficient_evidence↔1 · violation↔2); mismatch or bad
#     syntax ⇒ misdeclared; no label ⇒ only counted as missing_label, bucketed by exit code
#     (rung 1, §4 — not escalated into a wall).
#   cmd MUST be one of our own scripts ([bash|sh|python3] scripts/<name> [args]) — external tools
#   define their own meaning for exit code 1 (grep: no match · shellcheck: found issues) ⇒ not
#   readable per this contract.
#   cmd is run by tokenizing argv, NOT `bash -c` — a cmd containing `;` `|` `&&` a backtick or
#   `$(` is rejected as misdeclared (shell-injection guard) instead of silently reinterpreted.
#   --l3: every script named in the cmd column must have --selftest, --selftest must pass, and
#   must not contain `exit $?`.
# Usage: check-rules-v7.sh [--root DIR] [--table FILE] [--run-scope X] [--block] [--l3] [--selftest]
#   default --table: v7/01-rule-contract.md (relative to --root).
#   Legacy flags --goc/--pham-vi/--scope/--pham-vi-chay/--chan still accepted as deprecated
#   aliases (log to stderr) until 2026-12-31. --pham-vi/--scope used to select a DIRECTORY to
#   scan for tables across many files; that feature is gone (single canonical table file now) —
#   their value is taken as the --table path instead.
# This gate's own exit code follows the same convention; --block: 2 if violations+misdeclared>0,
# else 1 if unmeasurable>0, else 0.
# Last stdout line of the gate itself is also a label (gate=check-rules-v7).
# ponytail: no per-cmd timeout — add `timeout` when a rule runs long.
set -u
ROOT_DIR=.; TABLE=v7/01-rule-contract.md; RUN_SCOPE=FRAMEWORK_REPO; BLOCK=0; L3=0; SELFTEST=0
label() { echo "result=$1 gate=check-rules-v7 reason=$2"; }
deprecated() { echo "DEPRECATED: $1 (removal 2026-12-31)" >&2; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT_DIR=$2; shift;;
  --goc) deprecated "--goc, use --root"; ROOT_DIR=$2; shift;;
  --table) TABLE=$2; shift;;
  --pham-vi) deprecated "--pham-vi (directory scan removed), using value as --table"; TABLE=$2; shift;;
  --scope) deprecated "--scope (directory scan removed), using value as --table"; TABLE=$2; shift;;
  --run-scope) RUN_SCOPE=$2; shift;;
  --pham-vi-chay) deprecated "--pham-vi-chay, use --run-scope"; RUN_SCOPE=$2; shift;;
  --block) BLOCK=1;;
  --chan) deprecated "--chan, use --block"; BLOCK=1;;
  --l3) L3=1;;
  --selftest) SELFTEST=1;;
  *) echo "UNMEASURABLE: unknown argument $1"; label insufficient_evidence unknown_argument; exit 1;; esac; shift; done
case $RUN_SCOPE in FRAMEWORK_REPO|PRODUCT_CI|RUNTIME_PROBE) ;;
  *) echo "UNMEASURABLE: unknown --run-scope: $RUN_SCOPE"; label insufficient_evidence unknown_run_scope; exit 1;; esac

# Shared table-scan: read ONE file ($1), print \037-delimited rows to stdout, deprecation notices to stderr.
scan_table() {
  awk -v f="$1" '
    /^## / {
      # ponytail: legacy heading matched without its Vietnamese letter so this file stays English-only; goes 2026-12-31.
      legacy_h = ($0 ~ /^## Lu[^[:space:]]+t v7[[:space:]]*$/) && !($0 ~ /^## Rules v7/)
      new_h    = ($0 ~ /^## Rules v7[[:space:]]*$/)
      t = legacy_h || new_h
      if (legacy_h) print "DEPRECATED legacy heading in " f " — rename to \"## Rules v7\" (removal 2026-12-31)" > "/dev/stderr"
      b = 0; next
    }
    !/^\|/ { b = 0; next }
    !t || /^\|[-: |]+\|$/ { next }
    {
      n = split($0, c, "|"); hd = ""
      for (i = 2; i < n; i++) { gsub(/^[[:space:]]+|[[:space:]]+$/, "", c[i]); hd = hd "|" c[i] }
      if (!b) {
        b = 1
        if (hd == "|id|class|cmd|burn_case") { h = 4 }
        else if (hd == "|id|class|cmd|burn_case|run_scope") { h = 5 }
        else if (hd == "|id|lop|lenh|ca_dot") {
          h = 4; print "DEPRECATED header (lop/lenh/ca_dot) in " f " — rename to class/cmd/burn_case (removal 2026-12-31)" > "/dev/stderr"
        }
        else if (hd == "|id|lop|lenh|ca_dot|pham_vi_chay") {
          h = 5; print "DEPRECATED header (lop/lenh/ca_dot/pham_vi_chay) in " f " — rename to class/cmd/burn_case/run_scope (removal 2026-12-31)" > "/dev/stderr"
        }
        else { h = 0 }
        if (!h) print f "\037__BAD_HEADER__\037" hd "\037\037\037"
        next
      }
      if (h) print f "\037" c[2] "\037" c[3] "\037" c[4] "\037" c[5] "\037" (h == 5 ? c[6] : "")
    }' "$1"
}

# One pass over $bang: consumes \037-delimited rows, runs each cmd, tallies counters. Sets the
# counters named below as globals (bash has no real scoping here, ponytail: not worth a struct).
run_table() {
  local bang=$1
  passed=0; violations=0; unmeasurable=0; reference=0; misdeclared=0; l3_failures=0; missing_scope_column=0; other_scope=0; missing_label=0
  loi=$(mktemp); trap 'rm -f "$loi"' RETURN
  local re='^result=(pass|insufficient_evidence|violation) gate=[^ ]+ reason=[^ ]+( fix=.*)?$'
  while IFS=$'\037' read -r f id class cmd burn_case row_scope; do
    if [ "$id" = __BAD_HEADER__ ]; then misdeclared=$((misdeclared+1)); echo "RED — misdeclared (header must be |id|class|cmd|burn_case[|run_scope], legacy |id|lop|lenh|ca_dot[|pham_vi_chay] also accepted, saw $class): $f"; continue; fi
    cmd=${cmd#\`}; cmd=${cmd%\`}
    if [ -z "$cmd" ]; then reference=$((reference+1)); continue; fi
    if [ -z "$id" ] || [ -z "$class" ] || [ -z "$burn_case" ]; then misdeclared=$((misdeclared+1)); echo "RED — misdeclared (missing field): $id ($f)"; continue; fi
    # Shell-injection guard: cmd no longer runs through `bash -c`, so a cmd that only makes sense
    # as a compound shell command (chaining, substitution) is an authoring mistake, not something
    # to silently tokenize — reject it as misdeclared instead of reinterpreting it.
    case $cmd in *';'*|*'|'*|*'&&'*|*'`'*|*'$('*)
      misdeclared=$((misdeclared+1)); echo "RED — misdeclared (cmd contains a forbidden shell char ; | && \` \$(): $id ($f)"; continue;; esac
    [ -n "$row_scope" ] || { missing_scope_column=$((missing_scope_column+1)); row_scope=FRAMEWORK_REPO; }
    case $row_scope in FRAMEWORK_REPO|PRODUCT_CI|RUNTIME_PROBE) ;;
      *) misdeclared=$((misdeclared+1)); echo "RED — misdeclared (unknown run_scope: $row_scope): $id ($f)"; continue;; esac
    # Filter BEFORE running: a PRODUCT_CI/RUNTIME_PROBE cmd needs the target repo's/machine's env —
    # running it here would go red for the wrong reason.
    [ "$row_scope" = "$RUN_SCOPE" ] || { other_scope=$((other_scope+1)); continue; }
    # One of our own scripts: the first token (after bash/sh/python3) must be a .sh/.py path.
    # Whether it exists is left to the run itself (a missing path exits 127 ⇒ unmeasurable).
    s=$(echo "$cmd" | awk '{i=1; if($1 ~ /^(bash|sh|python3)$/) i=2; print $i}')
    case $s in *.sh|*.py) ;; *) misdeclared=$((misdeclared+1)); echo "RED — misdeclared (cmd is not one of our scripts: $s): $id ($f)"; continue;; esac
    if [ $L3 = 0 ]; then
      # stdout: last line = LABEL · stderr: last line = REASON (G2: a correct label that drops the
      # reason still leaves the reader guessing).
      # Tokenize argv instead of `bash -c "$cmd"` — cmd already passed the shell-char guard above,
      # so plain word-splitting is safe here.
      read -r -a argv <<< "$cmd"
      out=$("${argv[@]}" 2>"$loi" </dev/null); m=$?; err=$(tail -n 1 "$loi"); label_line=${out##*$'\n'}
      if [[ $label_line =~ $re ]]; then
        case ${BASH_REMATCH[1]} in pass) k=0;; insufficient_evidence) k=1;; violation) k=2;; esac
        if [ "$k" != "$m" ]; then misdeclared=$((misdeclared+1)); echo "RED — misdeclared (label ${BASH_REMATCH[1]} ≠ exit $m): $id ($f)"; continue; fi
      elif [[ $label_line == result=* ]]; then misdeclared=$((misdeclared+1)); echo "RED — misdeclared (bad label syntax: $label_line): $id ($f)"; continue
      else missing_label=$((missing_label+1)); label_line=""; fi
      reason="${label_line:+ — $label_line}${err:+ — $err}"
      case $m in 0) passed=$((passed+1));; 2) violations=$((violations+1)); echo "RED — violation: $id ($f)$reason";;
        *) unmeasurable=$((unmeasurable+1)); echo "RED — unmeasurable (exit $m): $id ($f)$reason";; esac
    else
      # --l3 does NOT run cmd: an L3 row calling this very gate would recurse forever.
      if [ ! -f "$s" ] || ! grep -q -- '--selftest' "$s"; then l3_failures=$((l3_failures+1)); echo "RED — L3 missing --selftest: $s ($id)"; continue; fi
      # Only match `exit $?` as a STATEMENT (start of line / after ; && ||) — not inside a comment or string.
      if grep -qE '(^|[;&|])[[:space:]]*exit[[:space:]]+\$\?' "$s"; then l3_failures=$((l3_failures+1)); echo "RED — L3 has \`exit \$?\` (another tool's exit code leaking through): $s ($id)"; continue; fi
      case $s in *.py) runner=python3;; *) runner=bash;; esac
      o=$($runner "$s" --selftest 2>&1) || { l3_failures=$((l3_failures+1)); echo "RED — L3 --selftest failed: $s ($id) — ${o##*$'\n'}"; }
    fi
  done < "$bang"
}

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); mkdir -p "$t/v7" "$t/s"
  printf 'exit 0\n' > "$t/s/pass.sh"; printf 'exit 2\n' > "$t/s/violation.sh"
  printf 'import no_such_module_xyz\n' > "$t/s/broken.py"; printf 'exit 7\n' > "$t/s/weird-code.sh"
  printf '# a\n## Rules v7\n| id | class | cmd | burn_case |\n|---|---|---|---|\n| X1 | MACHINE | `bash s/pass.sh` | case |\n| X2 | MACHINE | `bash s/violation.sh` | case |\n| X3 | MACHINE | `python3 s/broken.py` | case |\n| X4 | MACHINE | `bash s/does-not-exist.sh` | case |\n| X5 | MACHINE | `bash s/weird-code.sh` | case |\n| X6 | ADVISORY |  | case |\n| X7 | MACHINE | `bash s/pass.sh` |  |\n| X8 | MACHINE | `true` | case |\n| X9 | MACHINE | `bash s/pass.sh; echo pwned` | case |\n| X10 | MACHINE | `bash s/pass.sh` | case |\n## Other\n| Y | MACHINE | `bash s/violation.sh` | case |\n' > "$t/v7/01-rule-contract.md"
  out=$(bash "$0" --root "$t"); rc=$?
  # X1,X10 pass · X2 violation · X3 (Python crash = 1) · X4 (127) · X5 (>=3) => unmeasurable · X6 reference
  # X7,X8 missing field / not-a-script => misdeclared · X9 (`;` in cmd) => misdeclared (injection guard)
  want='passed=2 violations=1 unmeasurable=3 reference=1 misdeclared=3'
  got=$(echo "$out" | grep -oE 'passed=[0-9]+ violations=[0-9]+ unmeasurable=[0-9]+ reference=[0-9]+ misdeclared=[0-9]+')
  last_label=${out##*$'\n'}   # last stdout line of the gate itself must be a label matching its own exit code
  bash "$0" --root "$t" --block >/dev/null 2>&1; rc_block=$?
  bash "$0" --root "$t" --table v7/does-not-exist.md >/dev/null 2>&1; rc_missing=$?
  # Legacy flags/header must keep working, with a deprecation notice on stderr, same counts.
  legacy_err=$(bash "$0" --goc "$t" --pham-vi v7/01-rule-contract.md --chan 2>&1 >/dev/null); rc_legacy_flags=$?
  printf '# a\n## Lu\341\272\255t v7\n| id | lop | lenh | ca_dot |\n|---|---|---|---|\n| L1 | MACHINE | `bash s/pass.sh` | case |\n' > "$t/v7/01-rule-contract.md"
  legacy_out=$(bash "$0" --root "$t" 2>"$t/legacy.err"); legacy_hdr_err=$(cat "$t/legacy.err")
  legacy_got=$(echo "$legacy_out" | grep -oE 'passed=[0-9]+ violations=[0-9]+ unmeasurable=[0-9]+ reference=[0-9]+ misdeclared=[0-9]+')
  printf 'case $1 in --selftest) exit 0;; esac\nexit $?\n' > "$t/s/swallows.sh"
  printf '## Rules v7\n| id | class | cmd | burn_case |\n|---|---|---|---|\n| Z | MACHINE | `bash s/swallows.sh` | case |\n' > "$t/v7/01-rule-contract.md"
  bash "$0" --root "$t" --l3 >/dev/null; rc_l3=$?

  # run_scope cases: 5th column · filter by --run-scope · label match/mismatch · block-with-only-unmeasurable · bad header.
  d() { grep -oE 'passed=[0-9]+ violations=.*missing_label=[0-9]+'; }
  B='## Rules v7\n| id | class | cmd | burn_case | run_scope |\n|---|---|---|---|---|\n'
  printf 'echo "result=pass gate=x reason=ok"; exit 0\n' > "$t/s/n-pass.sh"
  printf 'echo "result=pass gate=x reason=lied"; exit 2\n' > "$t/s/n-mismatch.sh"
  printf 'echo "result=violation gate=x reason=had_issue fix=fix a b"; exit 2\n' > "$t/s/n-violation.sh"
  printf 'echo "result=insufficient_evidence gate=x reason=missing_tool"; exit 1\n' > "$t/s/n-unmeasurable.sh"
  printf "$B"'| P1 | MACHINE | `bash s/n-pass.sh` | case | FRAMEWORK_REPO |\n| P2 | MACHINE | `bash s/n-mismatch.sh` | case | FRAMEWORK_REPO |\n| P3 | MACHINE | `bash s/n-violation.sh` | case | PRODUCT_CI |\n| P4 | MACHINE | `bash s/n-pass.sh` | case | XYZ |\n| P5 | MACHINE | `bash s/n-pass.sh` | case |  |\n' > "$t/v7/01-rule-contract.md"
  # P1,P5 pass (P5 blank cell => FRAMEWORK_REPO, missing_scope_column) · P2 label pass + exit 2 => misdeclared
  # · P3 other scope · P4 unknown value => misdeclared
  v1=$(bash "$0" --root "$t" | d)
  v2=$(bash "$0" --root "$t" --run-scope PRODUCT_CI | d)   # only P3 runs => violation, fix= keeps its spaces
  bash "$0" --root "$t" --run-scope WRONG >/dev/null; rc_run_scope=$?
  printf '## Rules v7\n| id | class | cmd | burn_case |\n|---|---|---|---|\n| Q | MACHINE | `bash s/n-pass.sh` | case |\n' > "$t/v7/01-rule-contract.md"
  v3=$(bash "$0" --root "$t" --block | d)                  # 4-column table => count only, never red
  bash "$0" --root "$t" --block >/dev/null; rc_missing_col=$?
  printf "$B"'| K | MACHINE | `bash s/n-unmeasurable.sh` | case | FRAMEWORK_REPO |\n' > "$t/v7/01-rule-contract.md"
  bash "$0" --root "$t" --block >/dev/null; rc_only_unmeasurable=$?    # only "unmeasurable" => 1, not 2
  printf '## Rules v7\n| id | cmd | class | burn_case |\n|---|---|---|---|\n| H | `bash s/n-pass.sh` | MACHINE | case |\n' > "$t/v7/01-rule-contract.md"
  v4=$(bash "$0" --root "$t" | d)
  bash "$0" --root "$t" --block >/dev/null; rc_bad_header=$?           # wrong header => misdeclared => 2
  rm -rf "$t"
  w1='passed=2 violations=0 unmeasurable=0 reference=0 misdeclared=2 run_scope=FRAMEWORK_REPO missing_scope_column=1 other_scope=1 missing_label=0'
  w2='passed=0 violations=1 unmeasurable=0 reference=0 misdeclared=1 run_scope=PRODUCT_CI missing_scope_column=1 other_scope=3 missing_label=0'
  w3='passed=1 violations=0 unmeasurable=0 reference=0 misdeclared=0 run_scope=FRAMEWORK_REPO missing_scope_column=1 other_scope=0 missing_label=0'
  w4='passed=0 violations=0 unmeasurable=0 reference=0 misdeclared=1 run_scope=FRAMEWORK_REPO missing_scope_column=0 other_scope=0 missing_label=0'
  [ "$got" = "$want" ] && [ $rc = 0 ] && [ $rc_block = 2 ] && [ $rc_missing = 1 ] && [ $rc_l3 = 2 ] \
    && [ "$last_label" = "result=pass gate=check-rules-v7 reason=rung1_count_only" ] \
    && [ $rc_legacy_flags = 2 ] && [ -n "$legacy_err" ] \
    && [ "$legacy_got" = "passed=1 violations=0 unmeasurable=0 reference=0 misdeclared=0" ] && [ -n "$legacy_hdr_err" ] \
    && [ "$v1" = "$w1" ] && [ "$v2" = "$w2" ] && [ "$v3" = "$w3" ] && [ "$v4" = "$w4" ] \
    && [ $rc_run_scope = 1 ] && [ $rc_missing_col = 0 ] && [ $rc_only_unmeasurable = 1 ] && [ $rc_bad_header = 2 ] \
    && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest FAILED: got=[$got] rc=$rc block=$rc_block missing=$rc_missing l3=$rc_l3 label=[$last_label] legacy_flags_rc=$rc_legacy_flags legacy_err=[$legacy_err] legacy_got=[$legacy_got] legacy_hdr_err=[$legacy_hdr_err] run_scope=$rc_run_scope missing_col=$rc_missing_col only_unmeasurable=$rc_only_unmeasurable bad_header=$rc_bad_header"
  printf '  v1=[%s]\n  v2=[%s]\n  v3=[%s]\n  v4=[%s]\n' "$v1" "$v2" "$v3" "$v4"
  label insufficient_evidence selftest_failed; exit 1  # a broken selftest = a broken gate => unmeasurable (1), not violation (2)
fi

cd "$ROOT_DIR" || { echo "UNMEASURABLE: cannot cd into $ROOT_DIR"; label insufficient_evidence cannot_cd_root; exit 1; }
[ -f "$TABLE" ] || { echo "UNMEASURABLE: table $TABLE not found"; label insufficient_evidence table_not_found; exit 1; }

# \037 (unit separator), NOT tab: tab is whitespace in IFS => an empty cell gets merged, columns shift.
# The first | line of the "## Rules v7" section is the header, checked by column NAME (not
# position) — wrong => one __BAD_HEADER__ record.
bang=$(mktemp); trap 'rm -f "$bang"' EXIT
scan_table "$TABLE" > "$bang"
run_table "$bang"

echo "table=$TABLE passed=$passed violations=$violations unmeasurable=$unmeasurable reference=$reference misdeclared=$misdeclared run_scope=$RUN_SCOPE missing_scope_column=$missing_scope_column other_scope=$other_scope missing_label=$missing_label$([ $L3 = 1 ] && echo " l3_failures=$l3_failures")"
[ $L3 = 1 ] && [ $l3_failures -gt 0 ] && { label violation "l3_$l3_failures"; exit 2; }
if [ $BLOCK = 1 ]; then
  [ $((violations+misdeclared)) -gt 0 ] && { label violation "violations_${violations}_misdeclared_$misdeclared"; exit 2; }
  [ $unmeasurable -gt 0 ] && { label insufficient_evidence "unmeasurable_$unmeasurable"; exit 1; }
  label pass clean; exit 0
fi
label pass rung1_count_only; exit 0
