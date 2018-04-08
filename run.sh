#!/bin/bash

rm -rf __pycache__
rm -rf .pytest_cache

if [ -z $TMPDIR ];then
    rm -rf /tmp/tmp*
else
    rm -rf $TMPDIR/tmp*
fi

mkdir -p results
py.test --benchmark-autosave --benchmark-enable --benchmark-compare=0001 --benchmark-json=./results/benchmark.json pybenchmark.py
