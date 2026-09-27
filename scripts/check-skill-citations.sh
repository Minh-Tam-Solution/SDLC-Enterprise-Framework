#!/usr/bin/env bash
# Rule SKILL-1: every SEF path a skill cites exists in the same commit, and every skill folder is loadable.
#   Burn case: the sdlc-* skills lived in another repository. From 2026-09-25, when the first generation was
#   archived, until a hand rewrite on 2026-09-27 they cited 20 numbered paths (`05-Templates-Tools/…`,
#   `09-Continuous-Improvement/…`) of which none existed in the live tree. Nothing in this repository could
#   see a citation held outside it.
# Definition (skills/**/*.md, tracked; fenced code blocks are examples and are not read):
#   A citation into the SEF tree is
#     - a relative Markdown link or image target, resolved from the citing file; `#anchor` alone = same file;
#     - a path token inside an inline code span whose first segment is a top-level entry of this tree, or
#       that starts with `<SEF>/`. A path token has a `/` or a file extension. `*` is a glob.
#   It must resolve to a tracked file or folder (a glob to at least one tracked file), inside the tree.
#   A section it names must exist in the target Markdown file:
#     - `#anchor` (link or code span) = the GitHub slug of a heading;
#     - `"Name"` or `("Name"` right after a code span that is only a path, or only a skill folder name
#       (skills/<name>/SKILL.md), = a heading that is Name or starts with Name then `—`, `–`, `-`, `:`, `(`,
#       `,` or `.`; or bold text **Name** (a trailing `.` or `:` ignored); case-insensitive;
#     - `§N` right after such a code span = a heading that starts with §N.
#   Each folder skills/<name>/ has SKILL.md whose front matter has `name: <name>` and a non-empty `description`.
# Not judged, listed as "not checked": path tokens whose first segment is not in this tree — the skill may be
#   naming a path in the adopting repo (`AGENTS.md`, `docs/…`). A typo in a first segment lands there too.
# ADVISORY: prints count=<broken citations + skill defects>, exits 0; --block turns count>0 into 2.
# Exit codes (controls/rule-contract.md): 0 pass · 1 cannot measure (no skills, no citation found, not a repo
#   root, reader failure) · 2 violation (only with --block). Last stdout line is the label.
# Usage: check-skill-citations.sh [--root DIR] [--block] [--selftest]
set -u
ROOT=.; SELFTEST=0; BLOCK=0
label() { echo "result=$1 gate=check-skill-citations reason=$2${3:+ fix=$3}"; }
while [ $# -gt 0 ]; do case $1 in
  --root) ROOT=${2:-}; shift;; --block) BLOCK=1;; --selftest) SELFTEST=1;;
  *) label insufficient_evidence unknown_argument; exit 1;; esac; shift; done

if [ $SELFTEST = 1 ]; then
  t=$(mktemp -d); trap 'rm -rf "$t"' EXIT
  # mk DIR [extra body line]: a tree with one clean skill that cites every form; the extra line plants one case.
  mk() {
    mkdir -p "$1/core" "$1/scripts" "$1/skills/good" && git -C "$1" init -q || return 1
    printf '# Guide\n\n## Two axes\n\n## Two axes\n\n## §1 — Classes\n\n## Kill criteria — examples\n\n- **Pinning.** text\n' > "$1/core/guide.md"
    : > "$1/scripts/x.sh"
    { printf -- '---\nname: good\ndescription: >\n  Use when testing.\n---\n\n# Good\n\n## Steps\n\n'
      printf 'See `core/guide.md` "Two axes", `core/guide.md` §1, `core/guide.md` ("Pinning"), `core/guide.md` "Kill criteria".\n'
      printf 'Run `bash <SEF>/scripts/x.sh --root <repo>` over `core/*.md` and `core/`; `good` ("Steps").\n'
      printf 'Link [g](../../core/guide.md#two-axes-1), [self](#steps). Product paths: `docs/not-sef.md`, `AGENTS.md`.\n'
      printf '```text\n`core/missing-in-a-fence.md` "Nowhere"\n```\n'
      [ -z "${2:-}" ] || printf '%s\n' "$2"; } > "$1/skills/good/SKILL.md"
    git -C "$1" add -A
  }
  n=0
  run() { n=$((n+1)); bash "$0" --root "$1" > "$t/out$n" 2> "$t/err$n"; local a=$?
          bash "$0" --root "$1" --block > /dev/null 2>> "$t/err$n"; local b=$?
          echo "$a$b$(grep -oE '^count=[0-9]+' "$t/out$n")"; }
  mk "$t/green" || { label insufficient_evidence selftest_setup_failed; exit 1; }
  got="green:$(run "$t/green")"
  i=0
  for plant in '`core/missing.md`' '`core/guide.md` "No such section"' '`core/guide.md` §9' \
               '[x](../../core/guide.md#no-such-anchor)' '`bash <SEF>/scripts/missing.sh`' '`core/*.txt`' \
               '[out](../../../outside.md)' '`good` ("No such step")'; do
    i=$((i+1)); mk "$t/red$i" "$plant"; got="$got red$i:$(run "$t/red$i")"
  done
  mk "$t/name"; sed -i.bak 's/^name: good$/name: other/' "$t/name/skills/good/SKILL.md"; got="$got name:$(run "$t/name")"
  mk "$t/desc"; printf -- '---\nname: good\ndescription:\n---\n`core/guide.md`\n' > "$t/desc/skills/good/SKILL.md"; got="$got desc:$(run "$t/desc")"
  mk "$t/noskill"; mkdir -p "$t/noskill/skills/empty"; : > "$t/noskill/skills/empty/notes.md"; git -C "$t/noskill" add -A
  got="$got noskill:$(run "$t/noskill")"
  mkdir -p "$t/none/core" && git -C "$t/none" init -q && : > "$t/none/core/a.md" && git -C "$t/none" add -A
  got="$got none:$(run "$t/none")"                                                   # zero skills => 1, not pass
  mk "$t/quiet"; printf -- '---\nname: good\ndescription: x\n---\nNo citation here.\n' > "$t/quiet/skills/good/SKILL.md"
  got="$got quiet:$(run "$t/quiet")"                                                 # zero citations => 1, not pass
  mkdir "$t/nogit"; got="$got nogit:$(run "$t/nogit")"
  want="green:00count=0"
  for i in 1 2 3 4 5 6 7 8; do want="$want red$i:02count=1"; done
  want="$want name:02count=1 desc:02count=1 noskill:02count=1 none:11 quiet:11 nogit:11"
  [ "$got" = "$want" ] && { echo "selftest OK"; label pass selftest_ok; exit 0; }
  echo "selftest BROKEN:"; echo " got=[$got]"; echo "want=[$want]"; cat "$t/out1"
  label insufficient_evidence selftest_broken; exit 1   # a broken selftest is a broken gate => cannot measure
fi

prefix=$(git -C "$ROOT" rev-parse --show-prefix) || { label insufficient_evidence not_a_git_repo; exit 1; }
[ -z "$prefix" ] || { label insufficient_evidence root_is_subdirectory "run from the repo root"; exit 1; }
list=$(mktemp); trap 'rm -f "$list"' EXIT
git -C "$ROOT" ls-files -z > "$list" || { label insufficient_evidence git_ls_files_failed; exit 1; }

# perl reads and judges; it prints one line per finding and a summary line, and dies (non-zero) on its own failure.
out=$(cd "$ROOT" && LIST="$list" perl -CSD -e '
  use strict; use warnings; use utf8;
  open(my $lh, "<:encoding(UTF-8)", $ENV{LIST}) or die "cannot read file list: $!\n";
  my @files = do { local $/; grep { length } split /\0/, <$lh> }; close $lh;
  my (%file, %dir, %top, %skill);
  for my $f (@files) {
    $file{$f} = 1; my @p = split m{/}, $f; $top{$p[0]} = 1; pop @p;
    my $d = ""; for (@p) { $d = $d eq "" ? $_ : "$d/$_"; $dir{$d} = 1 }
    $skill{$1} = 1 if $f =~ m{^skills/([^/]+)/};
  }
  my ($broken, $cites, %unchecked, %idx) = (0, 0);
  sub red { print "RED $_[0]\n"; $broken++ }
  sub body { my $f = shift; open(my $h, "<:encoding(UTF-8)", $f) or die "cannot read $f: $!\n"; my @l = <$h>; close $h; @l }
  sub index_of {                       # headings, GitHub slugs and bold labels of one Markdown file, outside fences
    my $f = shift; return $idx{$f} if $idx{$f};
    my (%i, %seen); my $fence = 0;
    for my $l (body($f)) {
      if ($l =~ /^\s*(```|~~~)/) { $fence = !$fence; next } next if $fence;
      if ($l =~ /^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$/) {
        (my $h = $1) =~ s/\[([^\]]*)\]\([^)]*\)/$1/g; $h =~ s/[`*]//g; push @{$i{head}}, lc $h;
        (my $s = lc $h) =~ s/[^\p{L}\p{M}\p{N}\p{Pc} -]//g; $s =~ s/ /-/g;
        my $k = $seen{$s}++ ? "$s-" . ($seen{$s} - 1) : $s; $i{slug}{$k} = 1;
      }
      while ($l =~ /\*\*([^*]+?)\*\*/g) { (my $b = lc $1) =~ s/[.:]\s*$//; $i{bold}{$b} = 1 }
    }
    return $idx{$f} = \%i;
  }
  sub section {                        # does file $t have the section named by $kind/$name?
    my ($t, $kind, $name) = @_; my $i = index_of($t);
    return $i->{slug}{$name} if $kind eq "anchor";
    if ($kind eq "number") { return grep { /^\Q$name\E(?!\d)/i } @{$i->{head} || []} }
    my $n = lc $name;
    return 1 if $i->{bold}{$n};
    return grep { $_ eq $n || /^\Q$n\E\s*[—–:(,.-]/ } @{$i->{head} || []};
  }
  sub resolve {                        # path (already relative to the tree root) => "file" | "dir" | ""
    my $p = shift; $p =~ s{/+$}{};
    if ($p =~ /\*/) { (my $re = quotemeta $p) =~ s/\\\*/[^\/]*/g; return (grep { /^$re$/ } keys %file) ? "glob" : "" }
    return $file{$p} ? "file" : $dir{$p} ? "dir" : "";
  }
  sub check {                          # one citation: path + optional section
    my ($where, $shown, $p, $kind, $name) = @_; $cites++;
    my $r = resolve($p);
    return red("$where: $shown: no such file or folder in this tree") unless $r;
    return unless defined $kind;
    return red("$where: $shown: a section is named, but the target is not one Markdown file") unless $r eq "file" && $p =~ /\.md$/;
    red("$where: $shown: $p has no section " . ($kind eq "anchor" ? "#$name" : $kind eq "number" ? $name : "\"$name\""))
      unless section($p, $kind, $name);
  }
  for my $s (sort keys %skill) {
    my $sk = "skills/$s/SKILL.md";
    unless ($file{$sk}) { red("skills/$s/: no SKILL.md"); next }
    my @l = body($sk); my (%fm, $key);
    if (@l && $l[0] =~ /^---\s*$/) {
      for my $x (@l[1 .. $#l]) {
        last if $x =~ /^---\s*$/;
        if ($x =~ /^([A-Za-z_][\w-]*):\s*(.*?)\s*$/) { $key = $1; $fm{$key} = $2 =~ /^[>|][-+]?$/ ? "" : $2 }
        elsif (defined $key && $x =~ /^\s+(\S.*?)\s*$/) { $fm{$key} .= " $1" }
      }
    } else { red("$sk: no front matter"); next }
    my $nm = $fm{name} // ""; $nm =~ s/^(["\x27])(.*)\1$/$2/;
    (my $ds = $fm{description} // "") =~ s/^\s*(["\x27])?\s*(.*?)\s*\1?\s*$/$2/;
    red("$sk: front matter name is \"$nm\", folder is \"$s\"") unless $nm eq $s;
    red("$sk: front matter description is empty") unless length $ds;
  }
  for my $f (sort grep { m{^skills/.*\.md$} } @files) {
    (my $base = $f) =~ s{[^/]*$}{};
    my $fence = 0; my $ln = 0;
    for my $l (body($f)) {
      $ln++; if ($l =~ /^\s*(```|~~~)/) { $fence = !$fence; next } next if $fence;
      my $w = "$f:$ln";
      while ($l =~ /!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)/g) {
        my $tg = $1; next if $tg =~ /^[A-Za-z][A-Za-z0-9+.-]*:/;         # a URL, not a path in this tree
        my ($p, $a) = split /#/, $tg, 2;
        if ($p eq "") { check($w, "#$a", $f, "anchor", $a); next }
        my @seg = $p =~ m{^/} ? () : split m{/}, $base; my $out = 0;
        for (split m{/}, $p) { next if $_ eq "" || $_ eq "."; if ($_ eq "..") { @seg ? pop @seg : ($out = 1) } else { push @seg, $_ } }
        if ($out) { red("$w: $tg: points outside the tree"); $cites++; next }
        check($w, $tg, join("/", @seg), defined $a ? ("anchor", $a) : ());
      }
      while ($l =~ /`([^`]+)`/g) {
        my $span = $1; my $after = substr($l, pos($l));
        my ($kind, $name) = $after =~ /^\s*\(?\s*"([^"]+)"/ ? ("name", $1) : $after =~ /^\s*(§\d+)/ ? ("number", $1) : ();
        my @tok = split " ", $span;
        if (@tok == 1 && $skill{$tok[0]} && defined $kind) { check($w, "`$tok[0]`", "skills/$tok[0]/SKILL.md", $kind, $name); next }
        for my $t (@tok) {
          my $sef = $t =~ s{^<SEF>/}{};
          my ($p, $a) = split /#/, $t, 2;
          next unless $p =~ m{^[\w.*-][\w.*/-]*$} && ($p =~ m{/} || $p =~ /\.\w+$/) && $p !~ /^\.+$/;
          unless ($sef || $top{(split m{/}, $p)[0]}) { $unchecked{$p} //= $w; next }
          my @sec = defined $a ? ("anchor", $a) : (@tok == 1 && defined $kind) ? ($kind, $name) : ();
          check($w, "`$t`", $p, @sec);
        }
      }
    }
  }
  print "not checked (first segment is not in this tree): $_ ($unchecked{$_})\n" for sort keys %unchecked;
  printf "skills=%d citations=%d not_checked=%d broken=%d\n", scalar(keys %skill), $cites, scalar(keys %unchecked), $broken;
') || { echo "$out"; label insufficient_evidence scan_failed; exit 1; }
echo "$out"
sum=$(grep -E '^skills=[0-9]+ citations=[0-9]+ not_checked=[0-9]+ broken=[0-9]+$' <<<"$out")
[ -n "$sum" ] || { label insufficient_evidence no_summary; exit 1; }
skills=$(grep -oE '^skills=[0-9]+' <<<"$sum" | cut -d= -f2); cites=$(grep -oE 'citations=[0-9]+' <<<"$sum" | cut -d= -f2)
n=$(grep -oE 'broken=[0-9]+' <<<"$sum" | cut -d= -f2)
# G1: nothing to measure is not "clean".
[ "$skills" -gt 0 ] || { label insufficient_evidence no_skills "add skills/<name>/SKILL.md or run from the framework root"; exit 1; }
[ "$cites" -gt 0 ] || [ "$n" -gt 0 ] || { label insufficient_evidence no_citations_found; exit 1; }
echo "count=$n"
[ "$n" -gt 0 ] && [ $BLOCK = 1 ] && { label violation "broken_$n" "fix_or_remove_each_citation_listed_above"; exit 2; }
[ "$n" -gt 0 ] && { label pass "advisory_count_$n" "fix_or_remove_each_citation_listed_above"; exit 0; }
label pass clean; exit 0
