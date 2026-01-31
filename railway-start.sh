#!/bin/bash

# Railway startup script for Django
echo "🚀 Starting Tecky Collections on Railway..."

# Wait for database to be ready
echo "⏳ Waiting for database..."
python -c "
import os
import time
import psycopg2
from urllib.parse import urlparse

if os.environ.get('DATABASE_URL'):
    url = urlparse(os.environ['DATABASE_URL'])
    for i in range(30):
        try:
            conn = psycopg2.connect(
                host=url.hostname,
                port=url.port,
                user=url.username,
                password=url.password,
                database=url.path[1:]
            )
            conn.close()
            print('✅ Database is ready!')
            break
        except:
            print(f'⏳ Waiting for database... ({i+1}/30)')
            time.sleep(2)
    else:
        print('❌ Database connection timeout')
        exit(1)
"

# Run migrations
echo "📊 Running database migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "👤 Creating admin user..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@tecky.com', 'TeckyAdmin2024!')
    print('✅ Admin user created: admin / TeckyAdmin2024!')
else:
    print('ℹ️ Admin user already exists')
"

# Load sample data
echo "📦 Loading sample data..."
python manage.py setup_sample_data

# Collect static files
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "🎉 Setup complete! Starting server..."

# Start the server
exec gunicorn tecky_collections.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile -