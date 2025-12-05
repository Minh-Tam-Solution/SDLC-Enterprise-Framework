#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""Update INTEGRITY HASH in archived markdown headers if placeholder present.
Phase: P2 (future chain integration placeholder).
"""
from __future__ import annotations
import hashlib, os, sys, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '99-Legacy'))
PLACEHOLDER = 'PENDING_SHA256'

HEADER_PATTERN = re.compile(r'^(INTEGRITY HASH:\s*)(.*)$', re.IGNORECASE | re.MULTILINE)


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()


def process_file(path: str) -> bool:
    with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
        content = fh.read()
    if PLACEHOLDER not in content:
        return False
    digest = sha256(path)
    new_content, count = HEADER_PATTERN.subn(rf'\1{digest}', content)
    if count:
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        logger.info(f"Updated hash {digest[:12]}... in {path}")
        return True
    return False


def main():
    updated = 0
    for root, _, files in os.walk(ROOT):
        for f in files:
            if f.lower().endswith('.md'):
                if process_file(os.path.join(root, f)):
                    updated += 1
    logger.info(f"Hash update complete. Files updated: {updated}")

if __name__ == '__main__':
    sys.exit(main())
