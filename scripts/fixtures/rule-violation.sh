#!/usr/bin/env bash
# Fixture for product-gates-selftest.yml: a PRODUCT_CI rule that deliberately violates.
echo "result=violation gate=fixture-violation reason=planted_violation"; exit 2
