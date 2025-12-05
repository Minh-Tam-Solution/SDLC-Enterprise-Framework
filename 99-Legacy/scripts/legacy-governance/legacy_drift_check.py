#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""Detect drift between legacy artifacts and their declared successors.
Checks existence and basic heading alignment.
Phase: P3.
"""
from __future__ import annotations
import os, re, sys, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LEGACY = os.path.join(ROOT, '99-Legacy')
SUCCESSOR_REGEX = re.compile(r'^SUPERSEDED BY:\s*(.+)$', re.IGNORECASE | re.MULTILINE)
HEADING_REGEX = re.compile(r'^#\s+(.+)$', re.MULTILINE)

REPORT = []

def read(path: str) -> str:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def extract_successor(md: str) -> str | None:
    m = SUCCESSOR_REGEX.search(md)
    return m.group(1).strip() if m else None

def first_heading(md: str) -> str | None:
    m = HEADING_REGEX.search(md)
    return m.group(1).strip() if m else None

def scan():
    for root, _, files in os.walk(LEGACY):
        for f in files:
            if not f.lower().endswith('.md'):
                continue
            p = os.path.join(root, f)
            text = read(p)
            successor = extract_successor(text)
            if not successor:
                continue
            # naive path resolution: search recursively relative to ROOT
            succ_path = None
            for rroot, _, sfiles in os.walk(ROOT):
                for sf in sfiles:
                    if sf == successor:
                        succ_path = os.path.join(rroot, sf)
                        break
                if succ_path:
                    break
            result = {
                'legacy_file': os.path.relpath(p, ROOT),
                'successor_declared': successor,
                'successor_found': bool(succ_path),
                'successor_path': os.path.relpath(succ_path, ROOT) if succ_path else None,
                'heading_match': None
            }
            if succ_path:
                legacy_head = first_heading(text)
                succ_head = first_heading(read(succ_path))
                result['heading_match'] = legacy_head != succ_head  # expecting difference (evolution)
            REPORT.append(result)

def main():
    scan()
    out = {
        'drift_scan_count': len(REPORT),
        'drift_items': REPORT
    }
    logger.info(json.dumps(out, indent=2))

if __name__ == '__main__':
    sys.exit(main())
