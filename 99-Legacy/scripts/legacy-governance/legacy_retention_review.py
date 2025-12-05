#!/usr/bin/env python3
import logging
logger = logging.getLogger(__name__)

"""Identify purge candidates based on retention class + age.
Phase: P3.
"""
from __future__ import annotations
import os, re, sys, datetime, json

LEGACY = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '99-Legacy'))
HEADER_DATE_RE = re.compile(r'^ARCHIVAL DATE:\s*(\d{4}-\d{2}-\d{2})', re.MULTILINE | re.IGNORECASE)
HEADER_RETENTION_RE = re.compile(r'^RETENTION CATEGORY:\s*(.+)$', re.MULTILINE | re.IGNORECASE)

RETENTION_MONTHS = {
  'REGULATORY': 36,
  'AUDIT': 24,
  'HISTORICAL': 24,
  'REFERENCE': 18,
  'DEPRECATE-CANDIDATE': 6
}

def parse_header(md: str):
    d = HEADER_DATE_RE.search(md)
    r = HEADER_RETENTION_RE.search(md)
    return (d.group(1) if d else None, r.group(1).strip() if r else None)

def months_between(a: datetime.date, b: datetime.date) -> int:
    return (a.year - b.year) * 12 + (a.month - b.month) - (1 if a.day < b.day else 0)

def main():
    today = datetime.date.today()
    candidates = []
    for root, _, files in os.walk(LEGACY):
        for f in files:
            if not f.lower().endswith('.md'):
                continue
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fh:
                text = fh.read()
            archival_date, retention = parse_header(text)
            if not archival_date or not retention:
                continue
            if retention not in RETENTION_MONTHS:
                continue
            adate = datetime.date.fromisoformat(archival_date)
            age_months = months_between(today, adate)
            limit = RETENTION_MONTHS[retention]
            purge = age_months >= limit
            if purge or retention == 'DEPRECATE-CANDIDATE':
                candidates.append({
                  'file': path,
                  'retention': retention,
                  'age_months': age_months,
                  'limit_months': limit,
                  'purge_recommended': purge
                })
    report = {
      'generated': today.isoformat(),
      'candidate_count': len(candidates),
      'candidates': candidates
    }
    logger.info(json.dumps(report, indent=2))

if __name__ == '__main__':
    sys.exit(main())
