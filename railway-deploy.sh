#!/bin/bash

# Railway Deployment Script
# Run this after your app is deployed to set up initial data

echo "🚀 Setting up Tecky Collections on Railway..."

# Run migrations
echo "📊 Running database migrations..."
python manage.py migrate

# Create superuser (if not exists)
echo "👤 Creating admin user..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'TeckyAdmin2024!')
    print('✅ Admin user created: admin / TeckyAdmin2024!')
else:
    print('ℹ️ Admin user already exists')
"

# Load sample data
echo "📦 Loading sample data..."
python manage.py setup_sample_data

# Collect static files (should be done automatically, but just in case)
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "🎉 Setup complete!"
echo ""
echo "🔗 Your app should be available at your Railway URL"
echo "🔐 Admin login: admin / TeckyAdmin2024!"
echo "📊 Dashboard: /dashboard/"
echo "⚙️ Django Admin: /admin/"