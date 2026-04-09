#!/bin/bash
set -e

# Activate virtual environment
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
else
    echo "Virtual environment not found. Please create it first."
    exit 1
fi

# Run pytest and capture exit code
pytest
TEST_EXIT_CODE=$?

# Deactivate virtual environment
deactivate

# Return appropriate exit code
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed"
    exit 0
else
    echo "Some tests failed"
    exit 1
fi