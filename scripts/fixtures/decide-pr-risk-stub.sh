#!/usr/bin/env bash
# Fixture for check-decision-contract.py --selftest: a deterministic stand-in for a decision function.
# State on stdin, one option on stdout. A real function calls a model; the contract it meets is the same.
s=$(cat)
[ -n "${s//[[:space:]]/}" ] || { echo insufficient_evidence; exit 0; }
case $s in *migrations/*) echo migration;; *) echo none;; esac
