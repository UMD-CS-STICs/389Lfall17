#!/bin/bash

# Substitute username dynamically in setup.py
USERNAME='{username}'

sudo apt-get update
sudo apt-get -y install git python-pip make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev

# Install Python (via pyenv)
## Download pyenv
curl -sL https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

## Setup pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"

## Install Python
pyenv install 3.6.2
pyenv global 3.6.2

# Install Python packages
pip install pillow boto3 awscli

# Create all temporary directories for image processing
mkdir -p ~/tmp/originals
mkdir -p ~/tmp/thumbnails

# Sync code files from S3
aws s3 sync s3://cmsc389l-$USERNAME-codelab-04-code ~

# Set default region
export AWS_DEFAULT_REGION='us-east-1'

# Run thumbnailing code
echo "Running image.py..."
python ~/image.py --tmp ~/tmp
