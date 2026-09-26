#!/usr/bin/env bash
# Rule MIG-1: the machine classifies each migration from its statements; a person does not.
#   contract — removes or changes what the running version may use, or rewrites existing data:
#              DROP, RENAME, enum ADD VALUE, column type change, SET NOT NULL, TRUNCATE, UPDATE ... SET,
#              DELETE FROM, and the same operations in migration-framework calls.
#   expand   — everything else (new tables, columns, indexes, nullable additions, inserts).
#   Automatic rollback is allowed after `none` or `expand`; `contract` follows the human runbook
#   (controls/gates.md, deploy log and rollback).
# Burn case: migrations that could not be rolled back were found only when rolling back — an enum value
#   that cannot be removed, two migrations that collided on the way down, a dropped policy on a live DB.
# A migration may declare `migration-class: expand|contract` in a comment. Declared expand but classified
#   contract is a VIOLATION: the label would have allowed an automatic rollback it cannot survive.
#   Declared contract on an expand is fine (more careful). No declaration is counted, not blocked.
# Files: --files a b c, or the migration files changed between --base (default: merge-base with
#   origin/main) and HEAD — a path with a `migrations/` or `versions/` segment.
# ADVISORY: prints count= (mismatches) and class=<none|expand|contract> for the deploy log; exit 0.
#   --enforce: exit 2 on a mismatch (the red case, and the switch for when the rule moves up the ladder).
# Exit codes (controls/rule-contract.md): 0 pass · 1 cannot measure · 2 violation. Last stdout line is the label.
set -u
ROOT=.; BASE=; ENFORCE=0; SELFTEST=0; FILES=()
label() { echo "result=$1 gate=check-migration-class reason=$2${3:+ fix=$3}"; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT=${2:-}; shift;; --base) BASE=${2:-}; shift;; --enforce) ENFORCE=1;;
  --files) shift; while [ $# -gt 0 ] && [ "${1#--}" = "$1" ]; do FILES+=("$1"); shift; done; continue;;
  --selftest) SELFTEST=1;;
  *) label insufficient_evidence unknown_argument; exit 1;; esac; shift; done

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT; m="$t/migrations"; mkdir -p "$m"
  printf -- '-- migration-class: expand\nCREATE TABLE a (id int);\nALTER TABLE a ADD COLUMN note text;\n' > "$m/0001_add.sql"
  printf -- '-- migration-class: expand\nALTER TABLE a DROP COLUMN note;\n' > "$m/0002_liar.sql"
  printf -- '-- migration-class: contract\nALTER TYPE status ADD VALUE %s;\n' "'x'" > "$m/0003_enum.sql"
  printf 'from alembic import op\n# migration-class: expand\ndef upgrade():\n    op.drop_column("a", "b")\n' > "$m/0004_py.py"
  printf 'CREATE INDEX i ON a (id);\n' > "$m/0005_undeclared.sql"
  bash "$0" --root "$t" --files migrations/0001_add.sql > "$t/o"; a=$?; ca=$(grep -oE 'class=[a-z]+' "$t/o")
  bash "$0" --root "$t" --files migrations/0002_liar.sql > "$t/o"; b=$?; nb=$(grep -oE '^count=[0-9]+' "$t/o")
  bash "$0" --root "$t" --files migrations/0002_liar.sql --enforce > /dev/null; c=$?   # the red case
  bash "$0" --root "$t" --files migrations/0003_enum.sql migrations/0005_undeclared.sql > "$t/o"; d=$?; cd_=$(grep -oE 'class=[a-z]+' "$t/o"); ud=$(grep -oE 'undeclared=[0-9]+' "$t/o")
  bash "$0" --root "$t" --files migrations/0004_py.py --enforce > /dev/null; e=$?      # framework call, labelled expand
  bash "$0" --root "$t" --files migrations/missing.sql > /dev/null 2>&1; f=$?           # unreadable => 1
  got="$a $ca $b $nb $c $d $cd_ $ud $e $f"
  want="0 class=expand 0 count=1 2 0 class=contract undeclared=1 2 1"
  [ "$got" = "$want" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: got=[$got] want=[$want]"; label insufficient_evidence selftest_broken; exit 1
fi

if [ ${#FILES[@]} -eq 0 ]; then
  git -C "$ROOT" rev-parse --git-dir > /dev/null || { label insufficient_evidence not_a_git_repo; exit 1; }
  if [ -z "$BASE" ]; then
    BASE=$(git -C "$ROOT" merge-base HEAD origin/main) || { label insufficient_evidence no_origin_main "pass --base <rev> or --files"; exit 1; }
  fi
  list=$(git -C "$ROOT" diff --name-only --diff-filter=AM "$BASE" HEAD) || { label insufficient_evidence diff_failed; exit 1; }
  while IFS= read -r p; do
    case "/$p" in */migrations/*|*/versions/*) FILES+=("$p");; esac
  done <<<"$list"
fi
if [ ${#FILES[@]} -eq 0 ]; then echo "count=0 undeclared=0 files=0"; echo "class=none"; label pass no_migrations; exit 0; fi

out=$(cd "$ROOT" && perl -e '
  use strict; use warnings;
  my $contract = qr/\bDROP\s+(TABLE|COLUMN|INDEX|CONSTRAINT|TYPE|POLICY|VIEW|SCHEMA|TRIGGER|FUNCTION|SEQUENCE|DEFAULT|NOT\s+NULL)\b|\bRENAME\b|\bADD\s+VALUE\b|\bALTER\s+COLUMN\b[^;]*?\b(TYPE|SET\s+NOT\s+NULL)\b|\bTRUNCATE\b|\bUPDATE\s+\S+\s+SET\b|\bDELETE\s+FROM\b|\bop\.(drop_\w+|rename_table)\s*\(|\bop\.alter_column\s*\([^)]*\b(type_|nullable\s*=\s*False|new_column_name)\b|\bmigrations\.(RemoveField|DeleteModel|RenameField|RenameModel|AlterField|RemoveIndex|RemoveConstraint|AlterUniqueTogether)\b/is;
  my ($mis, $und, $worst) = (0, 0, "expand");
  for my $f (@ARGV) {
    open(my $h, "<", $f) or do { print "UNREADABLE $f\n"; exit 3 };
    local $/; my $s = <$h>; close $h;
    my ($decl) = $s =~ /migration-class:\s*(expand|contract)\b/i;
    my $cls = ($s =~ $contract) ? "contract" : "expand";
    my $why = $cls eq "contract" ? " (" . substr($&, 0, 30) =~ s/\s+/ /gr . ")" : "";
    $worst = "contract" if $cls eq "contract";
    if (!defined $decl) { $und++; print "UNDECLARED $f: classified $cls$why\n"; }
    elsif (lc $decl eq "expand" && $cls eq "contract") { $mis++; print "RED — $f declared expand, classified contract$why: automatic rollback would not survive it\n"; }
    else { print "OK $f: declared $decl, classified $cls$why\n"; }
  }
  print "count=$mis undeclared=$und files=", scalar(@ARGV), "\nclass=$worst\n";
' "${FILES[@]}") || { echo "$out"; label insufficient_evidence read_failed; exit 1; }
echo "$out"
n=$(grep -oE '^count=[0-9]+' <<<"$out" | cut -d= -f2); [ -n "$n" ] || { label insufficient_evidence no_count; exit 1; }
if [ "$n" -gt 0 ]; then
  [ $ENFORCE = 1 ] && { label violation "mislabelled_$n" "label_it_contract_or_split_it_expand_then_contract"; exit 2; }
  label pass "advisory_count_$n" "label_it_contract_or_split_it_expand_then_contract"; exit 0
fi
label pass clean; exit 0
