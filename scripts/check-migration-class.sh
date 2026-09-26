#!/usr/bin/env bash
# Rule MIG-1: the machine classifies each migration from its statements; a person does not.
#   contract — removes or changes what the running version may use, or rewrites existing data:
#              DROP, RENAME, enum ADD VALUE, column type change, SET NOT NULL, a NOT NULL column with
#              no default, TRUNCATE, UPDATE ... SET, DELETE FROM, and the same operations in
#              migration-framework calls.
#   expand   — ONLY when every statement is on a known-safe list: create table / index / schema /
#              sequence / view / extension, add a nullable column or one with a default, insert,
#              comment, grant, transaction control, and the matching framework calls.
#   unknown  — anything else. Not recognised is not proof of safe (G2): an unknown statement gets the
#              human runbook, exactly like contract.
#   A file's class is its worst statement (contract > unknown > expand); the change's class is its
#   worst file. Automatic rollback is allowed only after `none` or `expand` (controls/gates.md).
# Burn case: migrations that could not be rolled back were found only when rolling back — an enum value
#   that cannot be removed, two migrations that collided on the way down, a dropped policy on a live DB.
# A migration may declare `migration-class: expand|contract` in a comment. Declared expand but classified
#   contract is a VIOLATION (the label would have allowed a rollback it cannot survive); declared expand
#   but classified unknown is counted as unconfirmed. No declaration is counted, not blocked.
# Files: --files a b c, or the migration files changed between --base (default: merge-base with
#   origin/main) and HEAD — a path with a `migrations/` or `versions/` segment.
# ADVISORY: prints count= (declared-expand-but-contract) and class=<none|expand|unknown|contract>; exit 0.
#   --enforce: exit 2 on such a mismatch (the red case, and the switch for when the rule moves up).
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
  printf -- '-- migration-class: expand\nCREATE TABLE a (id int);\nALTER TABLE a ADD COLUMN note text;\nCREATE INDEX i ON a (id);\n' > "$m/01_add.sql"
  printf -- '-- migration-class: expand\nALTER TABLE a DROP COLUMN note;\n' > "$m/02_liar.sql"
  printf -- '-- migration-class: contract\nALTER TYPE status ADD VALUE %s;\n' "'x'" > "$m/03_enum.sql"
  printf 'from alembic import op\n# migration-class: expand\ndef upgrade():\n    op.drop_column("a", "b")\n' > "$m/04_py.py"
  printf 'CREATE INDEX j ON a (id);\n' > "$m/05_undeclared.sql"
  printf -- '-- migration-class: expand\nCREATE POLICY p ON a USING (true);\n' > "$m/06_unknown.sql"
  printf 'ALTER TABLE a ADD COLUMN must text NOT NULL;\n' > "$m/07_notnull.sql"
  printf 'from alembic import op\ndef upgrade():\n    op.create_table("t")\n    op.add_column("t", sa.Column("c", sa.Text(), nullable=True))\n' > "$m/08_py_expand.py"
  printf 'UPDATE core.tables t SET status = %s WHERE t.id = 1;\n' "'free'" > "$m/09_update_alias.sql"
  cls() { grep -oE '^class=[a-z]+' "$t/o" | cut -d= -f2; }
  bash "$0" --root "$t" --files migrations/01_add.sql > "$t/o"; a="$?:$(cls)"
  bash "$0" --root "$t" --files migrations/02_liar.sql > "$t/o"; b="$?:$(grep -oE '^count=[0-9]+' "$t/o")"
  bash "$0" --root "$t" --files migrations/02_liar.sql --enforce > /dev/null; c=$?          # red case
  bash "$0" --root "$t" --files migrations/03_enum.sql migrations/05_undeclared.sql > "$t/o"; d="$?:$(cls):$(grep -oE 'undeclared=[0-9]+' "$t/o")"
  bash "$0" --root "$t" --files migrations/04_py.py --enforce > /dev/null; e=$?             # framework call, red
  bash "$0" --root "$t" --files migrations/06_unknown.sql > "$t/o"; f="$?:$(cls):$(grep -oE 'unconfirmed=[0-9]+' "$t/o")"
  bash "$0" --root "$t" --files migrations/07_notnull.sql > "$t/o"; g="$(cls)"
  bash "$0" --root "$t" --files migrations/08_py_expand.py > "$t/o"; h="$(cls)"
  bash "$0" --root "$t" --files migrations/09_update_alias.sql > "$t/o"; j="$(cls)"
  bash "$0" --root "$t" --files migrations/missing.sql > /dev/null 2>&1; i=$?
  got="$a $b $c $d $e $f $g $h $j $i"
  want="0:expand 0:count=1 2 0:contract:undeclared=1 2 0:unknown:unconfirmed=1 contract expand contract 1"
  [ "$got" = "$want" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN: got=[$got] want=[$want]"; cat "$t/o"; label insufficient_evidence selftest_broken; exit 1
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
if [ ${#FILES[@]} -eq 0 ]; then echo "count=0 unconfirmed=0 undeclared=0 files=0"; echo "class=none"; label pass no_migrations; exit 0; fi

out=$(cd "$ROOT" && perl -e '
  use strict; use warnings;
  my $contract = qr/\bDROP\s+(TABLE|COLUMN|INDEX|CONSTRAINT|TYPE|POLICY|VIEW|SCHEMA|TRIGGER|FUNCTION|SEQUENCE|DEFAULT|NOT\s+NULL)\b|\bRENAME\b|\bADD\s+VALUE\b|\bALTER\s+COLUMN\b[^;]*?\b(TYPE|SET\s+NOT\s+NULL)\b|\bADD\s+(COLUMN\s+)?\S+\s+[^;,]*\bNOT\s+NULL\b(?![^;,]*\bDEFAULT\b)|\bTRUNCATE\b|\bUPDATE\s+\S+(\s+(AS\s+)?\w+)?\s+SET\b|\bDELETE\s+FROM\b|\bop\.(drop_\w+|rename_table)\s*\(|\bop\.alter_column\s*\([^)]*\b(type_|nullable\s*=\s*False|new_column_name)\b|\bmigrations\.(RemoveField|DeleteModel|RenameField|RenameModel|AlterField|RemoveIndex|RemoveConstraint|AlterUniqueTogether)\b/is;
  # known-safe statements; anything not here and not contract is unknown
  my $safe_sql = qr/^\s*(CREATE\s+(UNIQUE\s+)?INDEX\b|CREATE\s+(TABLE|SCHEMA|SEQUENCE|EXTENSION|VIEW)\b|CREATE\s+OR\s+REPLACE\s+VIEW\b|ALTER\s+TABLE\s+\S+\s+ADD\s+(COLUMN\s+)?\S+\s+[^;]*$|INSERT\s+INTO\b|COMMENT\s+ON\b|GRANT\b|BEGIN\b|COMMIT\b|START\s+TRANSACTION\b|SET\s+\w+\s*(=|TO)\b)/is;
  my $safe_call = qr/^(op\.(create_table|create_index|add_column|bulk_insert|create_foreign_key)|migrations\.(CreateModel|AddField|AddIndex))$/;
  my %rank = (expand => 0, unknown => 1, contract => 2);
  my ($mis, $unc, $und, $worst) = (0, 0, 0, "expand");
  for my $f (@ARGV) {
    open(my $h, "<", $f) or do { print "UNREADABLE $f\n"; exit 3 };
    local $/; my $s = <$h>; close $h;
    my ($decl) = $s =~ /migration-class:\s*(expand|contract)\b/i;
    my ($cls, $why) = ("expand", "");
    if ($s =~ $contract) { ($cls, $why) = ("contract", substr($&, 0, 30)) }
    elsif ($f =~ /\.py$/) {
      my @calls = $s =~ /\b((?:op|migrations)\.\w+)\s*\(/g;
      my @odd = grep { $_ !~ $safe_call } @calls;
      if (!@calls) { ($cls, $why) = ("unknown", "no recognised migration call") }
      elsif (@odd) { ($cls, $why) = ("unknown", $odd[0]) }
      elsif ($s =~ /\bop\.add_column\b/ && $s !~ /nullable\s*=\s*True|server_default\s*=/) { ($cls, $why) = ("unknown", "add_column without nullable=True or a default") }
    } else {
      (my $body = $s) =~ s/--[^\n]*//g; $body =~ s{/\*.*?\*/}{}gs;
      my @st = grep { /\S/ } split /;/, $body;
      if (!@st) { ($cls, $why) = ("unknown", "no statements") }
      else { for my $x (@st) { next if $x =~ $safe_sql; ($cls, $why) = ("unknown", substr($x =~ s/^\s+//r, 0, 30)); last } }
    }
    $why = $why ? " (" . ($why =~ s/\s+/ /gr) . ")" : "";
    $worst = $cls if $rank{$cls} > $rank{$worst};
    if (!defined $decl) { $und++; print "UNDECLARED $f: classified $cls$why\n" }
    elsif (lc $decl eq "expand" && $cls eq "contract") { $mis++; print "RED — $f declared expand, classified contract$why: automatic rollback would not survive it\n" }
    elsif (lc $decl eq "expand" && $cls eq "unknown") { $unc++; print "UNCONFIRMED $f: declared expand, machine cannot confirm$why — human runbook\n" }
    else { print "OK $f: declared $decl, classified $cls$why\n" }
  }
  print "count=$mis unconfirmed=$unc undeclared=$und files=", scalar(@ARGV), "\nclass=$worst\n";
' "${FILES[@]}") || { echo "$out"; label insufficient_evidence read_failed; exit 1; }
echo "$out"
n=$(grep -oE '^count=[0-9]+' <<<"$out" | cut -d= -f2); [ -n "$n" ] || { label insufficient_evidence no_count; exit 1; }
if [ "$n" -gt 0 ]; then
  [ $ENFORCE = 1 ] && { label violation "mislabelled_$n" "label_it_contract_or_split_it_expand_then_contract"; exit 2; }
  label pass "advisory_count_$n" "label_it_contract_or_split_it_expand_then_contract"; exit 0
fi
label pass clean; exit 0
