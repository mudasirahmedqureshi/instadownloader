#!/bin/sh
# This tells Railway to install dependencies and start the app

pip install --upgrade pip
pip install -r requirements.txt
gunicorn app:app --bind 0.0.0.0:$PORT
