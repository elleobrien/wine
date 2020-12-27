#!/usr/bin/env bash

BASE=${PWD}
mkdir -p gcp
cd gcp
curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-307.0.0-linux-x86_64.tar.gz > google-cloud-sdk-307.0.0-linux-x86_64.tar.gz
tar xvzf google-cloud-sdk-307.0.0-linux-x86_64.tar.gz 2>&1 >/dev/null

cd google-cloud-sdk
./install.sh -q
source ${BASE}/gcp/google-cloud-sdk/path.bash.inc
