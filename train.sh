#!/usr/bin/env bash

python train.py

echo "## Model metrics" > report.md
cat metrics.txt >> report.md

echo "## Data viz" >> report.md

cat report.md
