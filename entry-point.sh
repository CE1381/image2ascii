#!/bin/bash

# Create logs directory
mkdir -p "./logs"

# Create info.log file if it doesn't exist
if [ ! -f ./logs/info.log ]; then
  touch ./logs/info.log
fi

# Run Python command
python3 runner.py
