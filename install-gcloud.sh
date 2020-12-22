#!/usr/bin/env bash

sudo apt update
mkdir -p gcp
cd gcp
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-307.0.0-linux-x86_64.tar.gz
tar xvzf google-cloud-sdk-307.0.0-linux-x86_64.tar.gz

cd google-cloud-sdk
./install.sh -q
source /home/runner/gcp/google-cloud-sdk/path.bash.inc
