#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt
# Clear existing staticfiles
rm -rf BirdVisionApp/staticfiles/*
# Convert static asset files
cd BirdVisionApp
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

gunicorn BirdVisionApp.asgi:application --worker-class uvicorn.workers.UvicornWorker --timeout 600