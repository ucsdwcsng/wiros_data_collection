#!/bin/bash

# Check if boto3 is installed
if ! python3 -c "import boto3" &> /dev/null; then
    echo "boto3 is not installed. Installing..."
    pip3 install boto3
else
    echo "boto3 is working"
fi

# Run the Python script

mkdir -p binary_data

python3 collector.py