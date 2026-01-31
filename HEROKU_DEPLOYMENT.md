# Heroku Deployment Guide - Tecky Collections

## 🚀 **Easy Heroku Deployment**

Heroku is perfect for Django projects and much more reliable than Railway for this type of application.

## 📋 **Prerequisites**

✅ **Heroku Account** - Sign up at [heroku.com](https://heroku.com) (free)
✅ **GitHub Repository** - You already have this
✅ **Project Files Ready** - I've prepared all Heroku config files

## 🔧 **Files I've Prepared**

- `Procfile` - Tells Heroku how to run your app
- `app.json` - One-click deployment configuration
- `runtime.txt` - Python version specification
- Updated `settings.py` - Heroku-specific settings

## 🚀 **Method 1: One-Click Deploy (Easiest)**

### **Step 1: Deploy Button**

Click this button to deploy directly from GitHub:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/codewitheddy/Tecky)

### **Step 2: Configure App**

1. **App Name**: Choose a unique name (e.g., `tecky-collections-2024`)
2. **Region**: Choose your preferred region
3. **Config Variables**: Will be set automatically
4. **Click "Deploy app"**

### **Step 3: Wait for Deployment**

- Heroku will automatically:
  - ✅ Install dependencies
  - ✅ Set up PostgreSQL database
  - ✅ Run migrations
  - ✅ Create admin user
  - ✅ Load sample data
  - ✅ Deploy your app

**Total time: 5-10 minutes**

## 🚀 **Method 2: Heroku CLI (Alternative)**

### **Step 1: Install Heroku CLI**

Download from [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

### **Step 2: Login and Create App**

```bash
# Login to Heroku
heroku login

# Create app
heroku create tecky-collections-2024

# Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# Set environment variables
heroku config:set SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=".herokuapp.com"
```

### **Step 3: Deploy**

```bash
# Deploy to Heroku
git push heroku master

# Run post-deployment commands
heroku run python manage.py createsuperuser --username admin --email admin@tecky.com
heroku run python manage.py setup_sample_data
```

## 🎯 **Your App URLs**

After deployment, your app will be available at:

- **Main Site**: `https://your-app-name.herokuapp.com/`
- **Admin Dashboard**: `https://your-app-name.herokuapp.com/dashboard/`
- **Django Admin**: `https://your-app-name.herokuapp.com/admin/`
- **Health Check**: `https://your-app-name.herokuapp.com/health/`

## 🔐 **Login Credentials**

- **Username**: `admin`
- **Email**: `admin@tecky.com`
- **Password**: You'll set this during deployment

## 💰 **Heroku Pricing**

- **Dyno (App)**: $7/month (Basic plan)
- **PostgreSQL**: $9/month (Mini plan)
- **Total**: ~$16/month
- **Free tier**: Available for testing (sleeps after 30 min inactivity)

## ✅ **Why Heroku is Better for Django**

1. **Mature Django Support** - Built specifically for web apps
2. **Automatic Migrations** - Runs migrations on deployment
3. **PostgreSQL Integration** - Seamless database setup
4. **File Storage Add-ons** - Easy media file handling
5. **Excellent Documentation** - Comprehensive guides
6. **Reliable Deployments** - Proven track record
7. **Easy Scaling** - Simple horizontal scaling

## 🔧 **Post-Deployment Setup**

### **1. Custom Domain (Optional)**

```bash
# Add custom domain
heroku domains:add www.yourdomain.com

# Configure DNS
# Point your domain's CNAME to your-app-name.herokuapp.com
```

### **2. SSL Certificate**

Heroku provides automatic SSL certificates for all apps - no configuration needed!

### **3. Media File Storage**

For production file uploads, add Cloudinary:

```bash
# Add Cloudinary for image storage
heroku addons:create cloudinary:starter

# This automatically sets CLOUDINARY_URL
```

Then update your Django settings to use Cloudinary for media files.

## 📊 **Features That Work Perfectly**

✅ **Modern Admin Dashboard** - All features work flawlessly
✅ **File Uploads** - Product images, quote references
✅ **Database Operations** - PostgreSQL with full ACID compliance
✅ **Static Files** - Served efficiently with WhiteNoise
✅ **HTTPS/SSL** - Automatic SSL certificates
✅ **Custom Domains** - Easy domain configuration
✅ **Scaling** - Horizontal and vertical scaling
✅ **Monitoring** - Built-in metrics and logging
✅ **Backups** - Automatic database backups

## 🔍 **Monitoring & Logs**

```bash
# View logs
heroku logs --tail

# Check app status
heroku ps

# Open app in browser
heroku open

# Access database
heroku pg:psql
```

## 🚨 **Troubleshooting**

### **Common Issues:**

1. **Build Fails**
   ```bash
   # Check build logs
   heroku logs --tail
   ```

2. **Database Issues**
   ```bash
   # Reset database
   heroku pg:reset DATABASE_URL
   heroku run python manage.py migrate
   ```

3. **Static Files Not Loading**
   ```bash
   # Collect static files
   heroku run python manage.py collectstatic --noinput
   ```

## 🎉 **Success Checklist**

After deployment, verify:

- [ ] Main website loads
- [ ] Admin dashboard accessible at `/dashboard/`
- [ ] Can login with admin credentials
- [ ] Product images display correctly
- [ ] Quote system works
- [ ] Database operations function
- [ ] Static files (CSS/JS) load properly
- [ ] Health check shows all green at `/health/`

## 🔗 **Useful Links**

- **Heroku Dashboard**: [dashboard.heroku.com](https://dashboard.heroku.com)
- **Django on Heroku**: [devcenter.heroku.com/articles/django-app-configuration](https://devcenter.heroku.com/articles/django-app-configuration)
- **PostgreSQL on Heroku**: [devcenter.heroku.com/articles/heroku-postgresql](https://devcenter.heroku.com/articles/heroku-postgresql)

## 🚀 **Ready to Deploy!**

**Choose your preferred method:**

1. **One-Click Deploy** (Easiest): Use the deploy button above
2. **Heroku CLI** (More control): Follow the CLI steps

Both methods will give you a fully functional Tecky Collections admin dashboard running on Heroku with PostgreSQL database, SSL certificates, and all features working perfectly!

**Heroku is much more reliable than Railway for Django projects. Your admin dashboard will work flawlessly!** 🎉