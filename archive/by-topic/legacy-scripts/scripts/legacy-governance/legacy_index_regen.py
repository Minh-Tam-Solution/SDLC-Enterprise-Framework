#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""Regenerate AI-LEGACY-INDEX.md standardized table from snapshot or live scan.
Phase: P2.
"""
from __future__ import annotations
import os, json, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LEGACY = os.path.join(ROOT, '99-Legacy')
SNAPSHOT = os.path.join(ROOT, '80-Transition-Indexes', 'legacy_index_snapshot.json')
OUTPUT = os.path.join(LEGACY, 'AI-LEGACY-INDEX.md')

HEADER = """# AI Legacy Index (Standardized)

| Artifact ID | Legacy Path | Original Version | Successor | Retention | Hash Status | Migration Batch |
|------------|-------------|------------------|-----------|-----------|-------------|-----------------|
"""

def load_snapshot():
    if not os.path.exists(SNAPSHOT):
        logger.info("Snapshot not found. Run legacy_scan.py first.", file=sys.stderr)
        return None
    with open(SNAPSHOT, 'r', encoding='utf-8') as fh:
        return json.load(fh)

def build_table(data):
    lines = []
    for art in sorted(data.get('artifacts', []), key=lambda a: a['id']):
        lines.append(f"| {art['id']} | {art['legacy_path']} | {art.get('original_version') or ''} | {art.get('superseded_by') or ''} | {art.get('retention_class') or ''} | {art.get('hash_status')} | {art.get('migration_batch') or ''} |")
    return "\n".join(lines)

def main():
    snap = load_snapshot()
    if not snap:
        return 1
    table = build_table(snap)
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as fh:
        fh.write(HEADER + table + "\n")
    logger.info(f"Legacy index regenerated: {OUTPUT}")

if __name__ == '__main__':
    sys.exit(main())
