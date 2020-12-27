#!/usr/bin/env bash

pipenv run dvc pull
pipenv run dvc repro

pipenv run python train.py

echo "## Model metrics" > report.md
cat metrics/metrics.json >> report.md
cat report.md
