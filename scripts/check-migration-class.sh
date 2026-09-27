#!/usr/bin/env bash
# Rule MIG-1: the machine classifies each migration from its operations AND their arguments; a person
#   does not, and an operation name alone does not.
#   contract — may break the version that is running now, or cannot be undone by rolling code back:
#              drops, renames, type changes, SET NOT NULL, enum ADD VALUE, a column added NOT NULL without
#              a default, any added constraint (foreign key, primary key, unique, check) or unique index,
#              TRUNCATE, UPDATE, DELETE — and the same operations in migration-framework calls.
#   expand   — only operations on a known-safe list, judged per operation with its arguments: new tables,
#              schemas, sequences, views, extensions, non-unique indexes, a column added nullable or with
#              a default, comments, grants, transaction control.
#   unknown  — everything else, including data inserts (new rows may be state the old code does not
#              understand) and any operation or argument the classifier cannot read. Not recognised is
#              not proof of safe (G2).
#   A file's class is its worst operation (contract > unknown > expand); a change's class is its worst file.
#   Python migrations are read with the Python parser, and only their upgrade path: a downgrade function
#   is not what the deploy runs.
# While MIG-1 is ADVISORY it decides nothing in production: any deploy with a migration follows the human
#   runbook (controls/gates.md). It collects machine class, declared class and the unknown rate so a
#   labelled corpus can later measure its false-expand rate.
# Burn case: migrations that could not be rolled back were found only when rolling back — an enum value
#   that cannot be removed, two migrations that collided on the way down, a dropped policy on a live DB.
# A migration may declare `migration-class: expand|contract` in a comment. Declared expand but classified
#   contract is counted (--enforce: exit 2 — the red case); declared expand but unknown is "unconfirmed".
# Files: --files a b c, or the migration files changed between --base (default: merge-base with
#   origin/main) and HEAD — a path with a `migrations/` or `versions/` segment.
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
  w() { printf '%b' "$2" > "$m/$1"; }
  w 01_expand.sql       '-- migration-class: expand\nCREATE TABLE a (id int);\nALTER TABLE a ADD COLUMN note text;\nCREATE INDEX i ON a (id);\n'
  w 02_liar.sql         '-- migration-class: expand\nALTER TABLE a DROP COLUMN note;\n'
  w 03_enum.sql         "-- migration-class: contract\nALTER TYPE status ADD VALUE 'x';\n"
  w 04_alembic_drop.py  'from alembic import op\n# migration-class: expand\ndef upgrade():\n    op.drop_column("a", "b")\n'
  w 05_policy.sql       '-- migration-class: expand\nCREATE POLICY p ON a USING (true);\n'
  w 06_notnull.sql      'ALTER TABLE a ADD COLUMN must text NOT NULL;\n'
  w 07_alembic_ok.py    'from alembic import op\nimport sqlalchemy as sa\ndef upgrade():\n    op.create_table("t", sa.Column("id", sa.Integer()))\n    op.add_column("t", sa.Column("c", sa.Text(), nullable=True))\ndef downgrade():\n    op.drop_column("t", "c")\n'
  w 08_update_alias.sql "UPDATE core.tables t SET status = 'free' WHERE t.id = 1;\n"
  w 09_fk.sql           'ALTER TABLE orders ADD CONSTRAINT fk_c FOREIGN KEY (customer_id) REFERENCES customers(id);\n'
  w 10_alembic_mixed.py 'from alembic import op\nimport sqlalchemy as sa\ndef upgrade():\n    op.add_column("t", sa.Column("a", sa.Text(), nullable=True))\n    op.add_column("t", sa.Column("b", sa.Text(), nullable=False))\n'
  w 11_django_req.py    'from django.db import migrations, models\nclass Migration(migrations.Migration):\n    operations = [migrations.AddField(model_name="o", name="code", field=models.CharField(max_length=10))]\n'
  w 12_django_null.py   'from django.db import migrations, models\nclass Migration(migrations.Migration):\n    operations = [migrations.AddField(model_name="o", name="note", field=models.TextField(null=True))]\n'
  w 13_insert.sql       "INSERT INTO settings (k, v) VALUES ('a', 'b');\n"
  w 14_multi.sql        'ALTER TABLE a ADD COLUMN x text, ADD COLUMN y text NOT NULL;\n'
  w 15_alembic_fk.py    'from alembic import op\ndef upgrade():\n    op.create_foreign_key("fk", "a", "b", ["b_id"], ["id"])\n'
  w 16_unique_index.sql 'CREATE UNIQUE INDEX u ON a (code);\n'
  w 17_default.sql      "ALTER TABLE a ADD COLUMN state text NOT NULL DEFAULT 'new';\n"
  w 19_django_fk.py     'from django.db import migrations, models\nclass Migration(migrations.Migration):\n    operations = [migrations.AddField(model_name="o", name="c", field=models.ForeignKey("app.C", null=True, on_delete=models.SET_NULL))]\n'
  w 18_alembic_colfk.py 'from alembic import op\nimport sqlalchemy as sa\ndef upgrade():\n    op.add_column("p", sa.Column("c", sa.String(), sa.ForeignKey("m.id"), nullable=True))\n'
  cls() { bash "$0" --root "$t" --files "migrations/$1" | grep -oE '^class=[a-z]+' | cut -d= -f2; }
  got=""
  for f in 01_expand.sql 06_notnull.sql 07_alembic_ok.py 08_update_alias.sql 09_fk.sql 10_alembic_mixed.py 11_django_req.py 12_django_null.py 13_insert.sql 14_multi.sql 15_alembic_fk.py 16_unique_index.sql 17_default.sql 05_policy.sql 18_alembic_colfk.py 19_django_fk.py; do got="$got $(cls $f)"; done
  want=" expand contract expand contract contract contract contract expand unknown contract contract contract expand unknown contract contract"
  bash "$0" --root "$t" --files migrations/02_liar.sql > "$t/o"; r1="$?:$(grep -oE '^count=[0-9]+' "$t/o")"
  bash "$0" --root "$t" --files migrations/02_liar.sql --enforce > /dev/null; r2=$?                 # red case
  bash "$0" --root "$t" --files migrations/04_alembic_drop.py --enforce > /dev/null; r3=$?          # red case, framework call
  bash "$0" --root "$t" --files migrations/05_policy.sql > "$t/o"; r4=$(grep -oE 'unconfirmed=[0-9]+' "$t/o")
  bash "$0" --root "$t" --files migrations/03_enum.sql migrations/01_expand.sql > "$t/o"; r5="$(grep -oE '^class=[a-z]+' "$t/o"):$(grep -oE 'undeclared=[0-9]+' "$t/o")"
  bash "$0" --root "$t" --files migrations/missing.sql > /dev/null 2>&1; r6=$?                      # unreadable => 1
  extra="$r1 $r2 $r3 $r4 $r5 $r6"; wantx="0:count=1 2 2 unconfirmed=1 class=contract:undeclared=0 1"
  [ "$got" = "$want" ] && [ "$extra" = "$wantx" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN:"; echo " classes got=[$got]"; echo "        want=[$want]"; echo " extra got=[$extra] want=[$wantx]"
  label insufficient_evidence selftest_broken; exit 1
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

out=$(cd "$ROOT" && python3 - "${FILES[@]}" <<'PY'
import ast, re, sys
RANK = {"expand": 0, "unknown": 1, "contract": 2}
def worst(a, b): return a if RANK[a] >= RANK[b] else b

def split_top(s, sep):
    parts, depth, cur, q = [], 0, "", None
    for ch in s:
        if q:
            cur += ch
            if ch == q: q = None
            continue
        if ch in "'\"": q = ch; cur += ch; continue
        if ch == "(": depth += 1
        elif ch == ")": depth -= 1
        if ch == sep and depth == 0: parts.append(cur); cur = ""
        else: cur += ch
    parts.append(cur)
    return [p.strip() for p in parts if p.strip()]

def sql_action(a):
    """One action inside ALTER TABLE."""
    u = " ".join(a.upper().split())
    if re.match(r"(DROP|RENAME)\b", u): return "contract", u[:30]
    if re.match(r"ADD\s+(CONSTRAINT|PRIMARY\s+KEY|FOREIGN\s+KEY|UNIQUE|CHECK|EXCLUDE)\b", u): return "contract", u[:30]
    if re.match(r"ADD\b", u):
        if re.search(r"\b(PRIMARY\s+KEY|UNIQUE|REFERENCES|CHECK)\b", u): return "contract", u[:30]
        if re.search(r"\bNOT\s+NULL\b", u) and not re.search(r"\bDEFAULT\b", u): return "contract", u[:30]
        return "expand", ""
    if re.match(r"ALTER\s+(COLUMN\s+)?\S+\s+(TYPE|SET\s+DATA\s+TYPE|SET\s+NOT\s+NULL|DROP\s+DEFAULT|DROP\s+NOT\s+NULL)\b", u): return "contract", u[:30]
    if re.match(r"ALTER\s+(COLUMN\s+)?\S+\s+SET\s+DEFAULT\b", u): return "expand", ""
    return "unknown", u[:30]

def sql_statement(s):
    u = " ".join(s.upper().split())
    if not u: return "expand", ""
    if re.match(r"(BEGIN|COMMIT|START\s+TRANSACTION|SET)\b", u): return "expand", ""
    if re.match(r"(DROP|TRUNCATE|DELETE|UPDATE)\b", u): return "contract", u[:30]
    if re.match(r"ALTER\s+TYPE\b.*\bADD\s+VALUE\b", u): return "contract", u[:30]
    if re.match(r"CREATE\s+UNIQUE\s+INDEX\b", u): return "contract", u[:30]
    if re.match(r"CREATE\s+(INDEX|TABLE|SCHEMA|SEQUENCE|EXTENSION|VIEW|OR\s+REPLACE\s+VIEW)\b", u): return "expand", ""
    if re.match(r"(COMMENT\s+ON|GRANT)\b", u): return "expand", ""
    m = re.match(r"ALTER\s+TABLE\s+(IF\s+EXISTS\s+)?(ONLY\s+)?\S+\s+(.*)$", " ".join(s.split()), re.I | re.S)
    if m:
        c = "expand"; why = ""
        for a in split_top(m.group(3), ","):
            k, w = sql_action(a)
            if RANK[k] > RANK[c]: c, why = k, w
        return c, why
    return "unknown", u[:30]

def classify_sql(text):
    text = re.sub(r"--[^\n]*", "", text); text = re.sub(r"/\*.*?\*/", "", text, flags=re.S)
    if "$$" in text: return "unknown", "dollar-quoted block"
    c, why = "expand", ""; n = 0
    for st in split_top(text, ";"):
        n += 1; k, w = sql_statement(st)
        if RANK[k] > RANK[c]: c, why = k, w
    return (c, why) if n else ("unknown", "no statements")

def kw(call, name):
    for k in call.keywords:
        if k.arg == name: return k.value
    return None
def is_true(v): return isinstance(v, ast.Constant) and v.value is True
def is_false(v): return isinstance(v, ast.Constant) and v.value is False
def strarg(call):
    if call.args and isinstance(call.args[0], ast.Constant) and isinstance(call.args[0].value, str): return call.args[0].value
    v = kw(call, "sql")
    return v.value if isinstance(v, ast.Constant) and isinstance(v.value, str) else None

def column_class(col, django=False):
    """A Column(...) or models.XField(...) being added to an existing table.
    Unstated nullability: a Django field defaults to null=False (required); an Alembic column is left unknown."""
    if not isinstance(col, ast.Call): return "unknown", "column not readable"
    if any(isinstance(a, ast.Call) and getattr(a.func, "attr", getattr(a.func, "id", "")) in ("ForeignKey", "CheckConstraint", "UniqueConstraint") for a in col.args) or kw(col, "to") is not None or getattr(col.func, "attr", "") in ("ForeignKey", "OneToOneField"): return "contract", "constraint on the added column"
    null = kw(col, "nullable") if kw(col, "nullable") is not None else kw(col, "null")
    has_default = any(kw(col, d) is not None for d in ("server_default", "db_default", "default"))
    if kw(col, "primary_key") is not None or kw(col, "unique") is not None and is_true(kw(col, "unique")): return "contract", "key or unique column"
    if null is not None and is_true(null): return "expand", ""
    if has_default: return "expand", ""
    if (null is not None and is_false(null)) or (null is None and django): return "contract", "required column without a default"
    return "unknown", "nullability not stated"

def classify_call(c):
    f = c.func
    if not (isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id in ("op", "migrations")): return None
    who, name = f.value.id, f.attr
    if who == "op":
        if name == "create_table": return "expand", ""
        if name == "add_column":
            col = c.args[1] if len(c.args) > 1 else kw(c, "column")
            return column_class(col)
        if name == "create_index":
            return ("contract", "unique index") if is_true(kw(c, "unique")) else ("expand", "")
        if name in ("create_foreign_key", "create_unique_constraint", "create_check_constraint", "create_primary_key", "create_exclude_constraint"): return "contract", "op." + name
        if name.startswith("drop_") or name == "rename_table": return "contract", "op." + name
        if name == "alter_column":
            if any(kw(c, k) is not None for k in ("type_", "new_column_name")) or is_false(kw(c, "nullable")): return "contract", "op.alter_column"
            return "unknown", "op.alter_column"
        if name == "execute":
            s = strarg(c)
            return classify_sql(s) if s is not None else ("unknown", "op.execute with non-literal SQL")
        if name == "bulk_insert": return "unknown", "op.bulk_insert (new rows)"
        return "unknown", "op." + name
    if name == "CreateModel": return "expand", ""
    if name == "AddField":
        return column_class(kw(c, "field") if kw(c, "field") is not None else (c.args[2] if len(c.args) > 2 else None), django=True)
    if name == "AddIndex": return "expand", ""
    if name in ("AddConstraint", "RemoveField", "DeleteModel", "RenameField", "RenameModel", "AlterField", "RemoveIndex", "RemoveConstraint", "AlterUniqueTogether", "AlterIndexTogether"): return "contract", "migrations." + name
    if name == "RunSQL":
        s = strarg(c)
        return classify_sql(s) if s is not None else ("unknown", "RunSQL with non-literal SQL")
    return "unknown", "migrations." + name

def classify_py(text):
    try: tree = ast.parse(text)
    except SyntaxError: return "unknown", "not parseable"
    scope = tree
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "upgrade": scope = node
    calls = [n for n in ast.walk(scope) if isinstance(n, ast.Call)]
    c, why, seen = "expand", "", 0
    for call in calls:
        r = classify_call(call)
        if r is None: continue
        seen += 1
        if RANK[r[0]] > RANK[c]: c, why = r
    return (c, why) if seen else ("unknown", "no recognised migration operation")

mis = unc = und = 0; overall = "expand"
for f in sys.argv[1:]:
    try: text = open(f, encoding="utf-8").read()
    except OSError: print("UNREADABLE " + f); sys.exit(3)
    m = re.search(r"migration-class:\s*(expand|contract)\b", text, re.I)
    decl = m.group(1).lower() if m else None
    c, why = classify_py(text) if f.endswith(".py") else classify_sql(text)
    why = f" ({why})" if why else ""
    overall = worst(overall, c) if RANK[c] >= RANK[overall] else overall
    if decl is None: und += 1; print(f"UNDECLARED {f}: classified {c}{why}")
    elif decl == "expand" and c == "contract": mis += 1; print(f"RED — {f} declared expand, classified contract{why}")
    elif decl == "expand" and c == "unknown": unc += 1; print(f"UNCONFIRMED {f}: declared expand, machine cannot confirm{why}")
    else: print(f"OK {f}: declared {decl}, classified {c}{why}")
print(f"count={mis} unconfirmed={unc} undeclared={und} files={len(sys.argv) - 1}")
print(f"class={overall}")
PY
) || { echo "$out"; label insufficient_evidence read_failed; exit 1; }
echo "$out"
n=$(grep -oE '^count=[0-9]+' <<<"$out" | cut -d= -f2); [ -n "$n" ] || { label insufficient_evidence no_count; exit 1; }
if [ "$n" -gt 0 ]; then
  [ $ENFORCE = 1 ] && { label violation "mislabelled_$n" "label_it_contract_or_split_it_expand_then_contract"; exit 2; }
  label pass "advisory_count_$n" "label_it_contract_or_split_it_expand_then_contract"; exit 0
fi
label pass clean; exit 0
