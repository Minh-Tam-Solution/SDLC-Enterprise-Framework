#!/usr/bin/env python3
"""SDLC 6.3.1 — Strict document header validator.

Enforces Part 5.1 Active Document Header (or Part 5.2 Archived / 5.3
Migration variants) on every `.md` file in a /docs tree.

Spec source:
  02-Core-Methodology/Documentation-Standards/SDLC-Naming-Standards.md

Designed to run as:
  - pre-commit hook (fails the commit if any active doc lacks the header)
  - CI gate (on pull requests touching docs/**)
  - ad-hoc audit (point at any /docs tree)

Exit codes:
  0 = all docs pass
  1 = one or more docs fail — details on stderr
  2 = usage error

Version: 6.3.1
Date: April 21, 2026
Status: ACTIVE - PRODUCTION READY
Authority: CTO + CPO Office
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Part 5.1 required fields
REQUIRED_ACTIVE = ("Version", "Date", "Status", "Authority")
REQUIRED_ARCHIVED = ("ARCHIVAL STATUS", "Original Version", "Archived Date")
REQUIRED_MIGRATION = ("Migration From", "Migration To", "Migration Date")

FIELD_RE = re.compile(r"^\*\*(?P<key>[A-Z][A-Za-z ]+)\*\*:\s*(?P<val>.+?)\s*$", re.MULTILINE)
# Plain-text variant for Python/shell docstrings + block comments.
PLAIN_FIELD_RE = re.compile(
    r"^(?:#\s*)?(?P<key>Version|Date|Status|Authority):\s*(?P<val>.+?)\s*$",
    re.MULTILINE,
)
VERSION_RE = re.compile(r"^6\.\d+\.\d+$")
DATE_RE = re.compile(r"^(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}$")

# Paths under these prefixes are exempt from active-header requirement
EXEMPT_PREFIXES = (
    "10-archive",
    "node_modules",
    ".git",
    "__pycache__",
)


def parse_header(text: str) -> dict[str, str]:
    """Extract `**Key**: value` pairs from the header block only.

    The header is defined as "everything before the first horizontal rule
    (`---`)". This avoids false positives on template bodies that include
    placeholder example headers like `**Version**: [X.Y.Z]`.
    """
    head_lines: list[str] = []
    for line in text.splitlines()[:60]:
        if line.strip() == "---":
            break
        head_lines.append(line)
    head = "\n".join(head_lines)
    return {m.group("key"): m.group("val") for m in FIELD_RE.finditer(head)}


def classify(fields: dict[str, str]) -> str:
    if "ARCHIVAL STATUS" in fields:
        return "archived"
    if "Migration From" in fields:
        return "migration"
    return "active"


YAML_REQUIRED_KEYS = ("sdlc_framework", "version")


def parse_yaml_frontmatter(text: str) -> dict[str, str] | None:
    """Return {key: value} if the file starts with a YAML frontmatter block.

    SASE artifacts (SOULs, unified specs) use YAML frontmatter instead of
    the markdown `**Key**: value` form; both are Part 5 compliant. Returns
    None if no frontmatter is present.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    out: dict[str, str] = {}
    for line in lines[1:60]:
        if line.strip() == "---":
            return out
        m = re.match(r"^([a-z_][a-z0-9_]*):\s*(.+?)\s*$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def validate_doc(path: Path) -> list[str]:
    """Return a list of violations (empty = passes)."""
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as exc:
        return [f"read error: {exc}"]

    # Skip pure index/README with only frontmatter-less content < 10 lines
    if len(text.splitlines()) < 10:
        return []

    # YAML frontmatter path (SASE artifacts, specs)
    yaml_fields = parse_yaml_frontmatter(text)
    if yaml_fields is not None:
        missing = [k for k in YAML_REQUIRED_KEYS if k not in yaml_fields]
        return [f"missing YAML frontmatter key: {k}" for k in missing]

    # Code-file path: scan docstring / top comments for plain-text fields.
    if path.suffix in {".py", ".sh"}:
        head = "\n".join(text.splitlines()[:80])
        plain = {m.group("key"): m.group("val") for m in PLAIN_FIELD_RE.finditer(head)}
        violations: list[str] = []
        for req in REQUIRED_ACTIVE:
            if req not in plain:
                violations.append(f"missing Part 5.1 field: {req}")
        return violations

    fields = parse_header(text)
    kind = classify(fields)
    violations: list[str] = []

    if kind == "active":
        for req in REQUIRED_ACTIVE:
            if req not in fields:
                violations.append(f"missing Part 5.1 field: {req}")
        if "Version" in fields and not VERSION_RE.match(fields["Version"]):
            violations.append(
                f"Version '{fields['Version']}' does not match SDLC 6.x.y"
            )
        if "Date" in fields and not DATE_RE.match(fields["Date"]):
            violations.append(
                f"Date '{fields['Date']}' does not match 'Month DD, YYYY'"
            )
        if "Status" in fields and not fields["Status"].startswith("ACTIVE"):
            violations.append(
                f"Status '{fields['Status']}' should start with 'ACTIVE - ...'"
            )
    elif kind == "archived":
        for req in REQUIRED_ARCHIVED:
            if req not in fields:
                violations.append(f"missing Part 5.2 field: {req}")
    elif kind == "migration":
        for req in REQUIRED_MIGRATION:
            if req not in fields:
                violations.append(f"missing Part 5.3 field: {req}")

    return violations


def is_exempt(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return any(str(rel).startswith(prefix) for prefix in EXEMPT_PREFIXES)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Strict SDLC Part 5 header validator")
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Directory to scan (default: current dir)",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="Glob-match only these paths (repeatable); default: **/*.md",
    )
    parser.add_argument(
        "--warn-exempt",
        action="store_true",
        help="List exempt paths that were skipped",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"error: {root} is not a directory", file=sys.stderr)
        return 2

    patterns = args.only or ["**/*.md"]
    seen: set[Path] = set()
    failures: dict[Path, list[str]] = {}
    exempt: list[Path] = []
    checked = 0

    for pattern in patterns:
        for path in root.glob(pattern):
            if not path.is_file() or path in seen:
                continue
            seen.add(path)
            if is_exempt(path, root):
                exempt.append(path)
                continue
            violations = validate_doc(path)
            checked += 1
            if violations:
                failures[path] = violations

    for path, viols in sorted(failures.items()):
        rel = path.relative_to(root)
        print(f"FAIL {rel}", file=sys.stderr)
        for v in viols:
            print(f"  - {v}", file=sys.stderr)

    if args.warn_exempt and exempt:
        print(f"\n{len(exempt)} exempt file(s) skipped (archive / node_modules / .git).", file=sys.stderr)

    print(f"\nchecked={checked} passed={checked - len(failures)} failed={len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
