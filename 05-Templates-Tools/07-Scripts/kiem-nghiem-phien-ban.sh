#!/usr/bin/env bash
# DEPRECATED shim (removal 2026-12-31) — moved to scripts/check-version-declared.sh (F4, 2026-09-25).
exec "$(dirname "$0")/../../scripts/check-version-declared.sh" "$@"
