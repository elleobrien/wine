#!/usr/bin/env bash

BASE=${PWD}
sudo apt update
mkdir -p gcp
cd gcp
wget -q https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-307.0.0-linux-x86_64.tar.gz
tar xvzf google-cloud-sdk-307.0.0-linux-x86_64.tar.gz 2>&1 >/dev/null

cd google-cloud-sdk
./install.sh -q
source ${BASE}/gcp/google-cloud-sdk/path.bash.inc
