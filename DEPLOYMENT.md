# Deployment Guide for Tecky Collections

## Local Development Setup

### 1. Prerequisites
- Python 3.11+
- PostgreSQL (optional, SQLite works for development)
- Git

### 2. Installation Steps

```bash
# Clone the repository
git clone <your-repo-url>
cd tecky_collections

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env file with your settings

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Load sample data (optional)
python manage.py setup_sample_data

# Run development server
python manage.py runserver
```

### 3. Environment Variables (.env file)

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Production Deployment

### Heroku Deployment

#### 1. Prepare for Deployment
```bash
# Install Heroku CLI
# Create Heroku app
heroku create tecky-collections-app

# Add PostgreSQL addon
heroku addons:create heroku-postgresql:hobby-dev

# Set environment variables
heroku config:set SECRET_KEY="your-production-secret-key"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app.herokuapp.com"
```

#### 2. Deploy
```bash
# Add files to git
git add .
git commit -m "Initial deployment"

# Deploy to Heroku
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Load sample data (optional)
heroku run python manage.py setup_sample_data
```

#### 3. Configure Media Files
For production, you'll need to configure media file storage (AWS S3, Cloudinary, etc.)

### VPS/Server Deployment

#### 1. Server Setup (Ubuntu)
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3 python3-pip python3-venv postgresql postgresql-contrib nginx

# Create user
sudo adduser tecky
sudo usermod -aG sudo tecky
```

#### 2. Database Setup
```bash
# Switch to postgres user
sudo -u postgres psql

# Create database and user
CREATE DATABASE tecky_collections;
CREATE USER tecky_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE tecky_collections TO tecky_user;
\q
```

#### 3. Application Setup
```bash
# Switch to app user
sudo su - tecky

# Clone repository
git clone <your-repo-url>
cd tecky_collections

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with production settings

# Run migrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

#### 4. Gunicorn Setup
```bash
# Test gunicorn
gunicorn tecky_collections.wsgi:application --bind 0.0.0.0:8000

# Create systemd service
sudo nano /etc/systemd/system/tecky.service
```

Service file content:
```ini
[Unit]
Description=Tecky Collections Django App
After=network.target

[Service]
User=tecky
Group=www-data
WorkingDirectory=/home/tecky/tecky_collections
Environment="PATH=/home/tecky/tecky_collections/venv/bin"
ExecStart=/home/tecky/tecky_collections/venv/bin/gunicorn --workers 3 --bind unix:/home/tecky/tecky_collections/tecky.sock tecky_collections.wsgi:application

[Install]
WantedBy=multi-user.target
```

#### 5. Nginx Configuration
```bash
sudo nano /etc/nginx/sites-available/tecky_collections
```

Nginx config:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /home/tecky/tecky_collections;
    }
    
    location /media/ {
        root /home/tecky/tecky_collections;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/tecky/tecky_collections/tecky.sock;
    }
}
```

#### 6. Enable Services
```bash
# Enable and start services
sudo systemctl daemon-reload
sudo systemctl start tecky
sudo systemctl enable tecky

sudo ln -s /etc/nginx/sites-available/tecky_collections /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

## Environment Variables for Production

```
SECRET_KEY=your-very-secure-secret-key
DEBUG=False
DATABASE_URL=postgresql://username:password@localhost:5432/tecky_collections
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

## SSL Certificate (Let's Encrypt)

```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## Backup Strategy

### Database Backup
```bash
# Create backup
pg_dump tecky_collections > backup_$(date +%Y%m%d_%H%M%S).sql

# Restore backup
psql tecky_collections < backup_file.sql
```

### Media Files Backup
```bash
# Backup media files
tar -czf media_backup_$(date +%Y%m%d_%H%M%S).tar.gz media/
```

## Monitoring and Maintenance

### Log Files
- Application logs: Check systemd journal with `sudo journalctl -u tecky`
- Nginx logs: `/var/log/nginx/access.log` and `/var/log/nginx/error.log`
- Django logs: Configure in settings.py

### Regular Maintenance
- Update dependencies regularly
- Monitor disk space
- Regular database backups
- Security updates

## Troubleshooting

### Common Issues

1. **Static files not loading**
   - Run `python manage.py collectstatic`
   - Check nginx configuration

2. **Database connection errors**
   - Verify DATABASE_URL in .env
   - Check PostgreSQL service status

3. **Permission errors**
   - Check file permissions
   - Verify user/group ownership

4. **502 Bad Gateway**
   - Check gunicorn service status
   - Verify socket file permissions

### Useful Commands
```bash
# Check service status
sudo systemctl status tecky
sudo systemctl status nginx

# View logs
sudo journalctl -u tecky -f
sudo tail -f /var/log/nginx/error.log

# Restart services
sudo systemctl restart tecky
sudo systemctl restart nginx
```