#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Wait for DB to be ready needs to be implemented!

# Run migrations
python manage.py migrate --noinput
python manage.py createsuperuser --noinput || true

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn digihike.wsgi:application --workers 5 --bind 0.0.0.0:8098