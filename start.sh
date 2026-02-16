#!/bin/sh

# Install pip if missing
python3 -m ensurepip --upgrade

# Upgrade pip
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install -r requirements.txt

# Start Flask app with Gunicorn on Railway-assigned port
gunicorn backend.app:app --bind 0.0.0.0:$PORT
