#!/bin/bash

# Build script for Vercel deployment
echo "Building the project..."

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "Build completed successfully!"