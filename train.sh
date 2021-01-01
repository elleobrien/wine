#!/usr/bin/env bash

dvc pull
dvc repro

echo "## Model metrics" > report.md
cat metrics/metrics.json >> report.md
cat report.md
