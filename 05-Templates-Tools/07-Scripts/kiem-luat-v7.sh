#!/usr/bin/env bash
# DEPRECATED shim (removal 2026-12-31) — moved to scripts/check-rules-v7.sh (2026-09-25).
exec "$(dirname "$0")/../../scripts/check-rules-v7.sh" "$@"
