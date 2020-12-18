#!/usr/bin/env bash

python train.py

echo "## Model metrics" > report.md
cat metrics.txt >> report.md

echo "## Data viz" >> report.md
cml-publish feature_importance.png --md >> report.md
cml-publish residuals.png --md >> report.md

cat report.md
