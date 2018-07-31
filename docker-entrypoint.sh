#!/bin/sh
set -e

if [ "$1" = test ]; then
    pytest -v tests/
    /bin/sh
else
    exec python sort_csv.py "$@"
fi