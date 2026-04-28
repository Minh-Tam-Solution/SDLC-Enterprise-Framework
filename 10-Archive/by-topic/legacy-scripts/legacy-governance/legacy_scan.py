#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""Scan legacy directory and produce legacy_index_snapshot.json.
Phase: P1/P2 foundation.
"""
from __future__ import annotations
import hashlib, json, os, sys, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '99-Legacy'))
OUTPUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '80-Transition-Indexes', 'legacy_index_snapshot.json'))
SCHEMA = os.path.abspath(os.path.join(ROOT, 'legacy_artifact_schema.json'))

HEADER_KEYS = [
    'ARCHIVAL STATUS', 'ORIGINAL VERSION', 'SUPERSEDED BY', 'ARCHIVAL DATE',
    'RETENTION CATEGORY', 'CHANGE TYPE', 'AUTHORIZATION', 'INTEGRITY HASH',
    'TRACEABILITY LINK'
]

def extract_header(block: str) -> dict:
    data = {}
    for line in block.splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            key = k.strip().upper()
            if key in HEADER_KEYS:
                data[key] = v.strip()
    return data

def compute_sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def find_md_files() -> list[str]:
    md_files = []
    for root, _, files in os.walk(ROOT):
        for f in files:
            if f.lower().endswith('.md'):
                md_files.append(os.path.join(root, f))
    return md_files

def parse_markdown(path: str) -> dict:
    with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
        text = fh.read()
    # header block assumed within first 1200 chars
    header_slice = text[:1200]
    header = extract_header(header_slice)
    record = {
        'id': os.path.splitext(os.path.basename(path))[0],
        'legacy_path': os.path.relpath(path, ROOT),
        'original_version': header.get('ORIGINAL VERSION'),
        'superseded_by': header.get('SUPERSEDED BY'),
        'retention_class': header.get('RETENTION CATEGORY'),
        'archival_date': header.get('ARCHIVAL DATE'),
        'hash': header.get('INTEGRITY HASH'),
        'hash_status': 'RECORDED' if header.get('INTEGRITY HASH') and header.get('INTEGRITY HASH') != 'PENDING_SHA256' else 'PENDING',
        'migration_batch': None,
        'status': 'ACTIVE-LEGACY',
        'notes': header.get('TRACEABILITY LINK')
    }
    return record

def main():
    md_files = find_md_files()
    records = [parse_markdown(p) for p in md_files]
    snapshot = {
        'generated_at': datetime.datetime.utcnow().isoformat() + 'Z',
        'count': len(records),
        'artifacts': records
    }
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as fh:
        json.dump(snapshot, fh, indent=2)
    logger.info(f"Legacy snapshot written: {OUTPUT} ({snapshot['count']} artifacts)")

if __name__ == '__main__':
    sys.exit(main())
