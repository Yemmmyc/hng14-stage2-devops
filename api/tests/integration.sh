#!/bin/bash

set -e

echo "Running integration test..."

curl -f http://localhost:8000/docs > /dev/null

echo "Integration test passed"

