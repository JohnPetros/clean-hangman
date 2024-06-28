#!/bin/bash

# Create the virtual enviroment
python3 -m venv .venv

# Enter the virtual enviroment
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Start the application
python3 packages/main.py $1