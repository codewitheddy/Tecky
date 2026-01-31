# Railway Deployment Guide - Tecky Collections

## 🚀 Quick Railway Deployment

Railway is perfect for Django projects like Tecky Collections. Here's your complete deployment guide:

## 📋 Prerequisites

✅ **You have a Railway account** - Great!
✅ **Project files are ready** - I've prepared all necessary config files
✅ **Git repository** - You'll need to push to GitHub/GitLab

## 🔧 Files I've Prepared for You

### New Configuration Files:
- `railway.json` - Railway project configuration
- `nixpacks.toml` - Build configuration for Railway
- Updated `requirements.txt` - Includes gunicorn for production
- Updated `settings.py` - Railway-specific settings

## 🚀 Deployment Steps

### Method 1: Deploy from GitHub (Recommended)

#### Step 1: Push to GitHub
```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit changes
git commit -m "Prepare for Railway deployment"

# Add your GitHub repository
git remote add origin https://github.com/yourusername/tecky-collections.git

# Push to GitHub
git push -u origin main
```

#### Step 2: Deploy on Railway
1. **Go to [railway.app](https://railway.app/)**
2. **Click "New Project"**
3. **Select "Deploy from GitHub repo"**
4. **Choose your tecky-collections repository**
5. **Railway will automatically:**
   - Detect it's a Django project
   - Install dependencies
   - Set up PostgreSQL database
   - Deploy your app

#### Step 3: Add PostgreSQL Database
1. **In your Railway project dashboard**
2. **Click "New Service"**
3. **Select "Database" → "PostgreSQL"**
4. **Railway automatically connects it to your Django app**

#### Step 4: Set Environment Variables
In Railway dashboard, go to your Django service → Variables tab:

```
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
DEBUG=False
ALLOWED_HOSTS=.railway.app
```

**Generate a secure SECRET_KEY:**
```python
# Run this in Python to generate a secure key
import secrets
print(secrets.token_urlsafe(50))
```

#### Step 5: Run Initial Setup
Railway will automatically run migrations, but you need to create a superuser:

1. **Go to your service in Railway dashboard**
2. **Click on "Deployments" tab**
3. **Click on the latest deployment**
4. **Open the "Deploy Logs"**
5. **Once deployed, go to service settings**
6. **Use the "Command" feature to run:**

```bash
python manage.py createsuperuser
```

Or create one programmatically by adding this to your deployment:

```bash
python manage.py shell -c "
from django.contrib.auth.models import User;
User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'your-secure-password')
"
```

#### Step 6: Load Sample Data (Optional)
```bash
python manage.py setup_sample_data
```

### Method 2: Railway CLI (Alternative)

If you prefer command line:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login to Railway
railway login

# Initialize project in your Django directory
railway init

# Add PostgreSQL database
railway add postgresql

# Deploy
railway up

# Set environment variables
railway variables set SECRET_KEY="your-secret-key"
railway variables set DEBUG="False"

# Run migrations and create superuser
railway run python manage.py migrate
railway run python manage.py createsuperuser
railway run python manage.py setup_sample_data
```

## 🎯 What Railway Provides Automatically

✅ **PostgreSQL Database** - Fully managed, automatically connected
✅ **HTTPS/SSL** - Automatic SSL certificates
✅ **Custom Domain** - You can add your own domain
✅ **Environment Variables** - Secure configuration management
✅ **Automatic Deployments** - Deploys on every git push
✅ **Logs & Monitoring** - Real-time application logs
✅ **File Storage** - Persistent file system for uploads
✅ **Scaling** - Easy horizontal scaling

## 🔗 Your App URLs

After deployment, you'll get:
- **Main Site**: `https://your-app-name.railway.app/`
- **Admin Dashboard**: `https://your-app-name.railway.app/dashboard/`
- **Django Admin**: `https://your-app-name.railway.app/admin/`

## 📊 Expected Deployment Time

- **Initial Setup**: 5-10 minutes
- **Build Time**: 3-5 minutes
- **Database Setup**: 1-2 minutes
- **Total**: ~10-15 minutes

## 🎨 Features That Work Perfectly on Railway

✅ **Modern Admin Dashboard** - All features work
✅ **File Uploads** - Product images, quote references
✅ **Database Operations** - PostgreSQL with full ACID compliance
✅ **Static Files** - CSS, JS, images served efficiently
✅ **Email Sending** - Configure SMTP for notifications
✅ **Background Tasks** - Can add Celery later if needed
✅ **WebSocket Support** - For real-time features
✅ **Custom Domains** - Professional URLs

## 🔧 Post-Deployment Configuration

### 1. Custom Domain (Optional)
1. Go to Railway dashboard → Your service → Settings
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed

### 2. Email Configuration (Optional)
Add to your Railway environment variables:
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
```

### 3. Media File Storage (For Production)
For production, consider using:
- **Cloudinary** (recommended for images)
- **AWS S3**
- **Railway's persistent volumes**

## 💰 Railway Pricing

- **Hobby Plan**: $5/month per service
- **Pro Plan**: $20/month per service
- **Free Trial**: Available for testing

For your project, you'll need:
- Django app service: $5/month
- PostgreSQL database: $5/month
- **Total**: ~$10/month

## 🚨 Important Notes

### Environment Variables You Must Set:
```
SECRET_KEY=your-generated-secret-key
DEBUG=False
ALLOWED_HOSTS=.railway.app
```

### Database Connection:
Railway automatically provides `DATABASE_URL` - no manual configuration needed!

### Static Files:
Handled automatically by WhiteNoise - no additional setup required!

## 🔍 Troubleshooting

### Common Issues:

1. **Build Fails**
   - Check `requirements.txt` has all dependencies
   - Verify Python version compatibility

2. **Database Connection Error**
   - Ensure PostgreSQL service is added
   - Check `DATABASE_URL` is automatically set

3. **Static Files Not Loading**
   - Run `python manage.py collectstatic` (done automatically)
   - Check WhiteNoise is in MIDDLEWARE

4. **Admin Login Issues**
   - Create superuser: `railway run python manage.py createsuperuser`
   - Check SECRET_KEY is set

### Useful Railway Commands:
```bash
# View logs
railway logs

# Run commands
railway run python manage.py migrate
railway run python manage.py shell

# Check environment variables
railway variables

# Redeploy
railway up --detach
```

## 🎉 Success Checklist

After deployment, verify:
- [ ] Main website loads at your Railway URL
- [ ] Admin dashboard works at `/dashboard/`
- [ ] Can login with superuser credentials
- [ ] Product images display correctly
- [ ] Quote system functions properly
- [ ] Database operations work
- [ ] Static files (CSS/JS) load properly

## 🔗 Helpful Links

- **Railway Dashboard**: [railway.app/dashboard](https://railway.app/dashboard)
- **Railway Docs**: [docs.railway.app](https://docs.railway.app/)
- **Django on Railway**: [railway.app/template/django](https://railway.app/template/django)

## 🚀 Ready to Deploy!

Your project is now fully configured for Railway deployment. The configuration files I've created will ensure:

1. **Automatic PostgreSQL setup**
2. **Proper static file handling**
3. **Production-ready settings**
4. **Secure environment configuration**

Just push to GitHub and deploy through Railway's web interface - it's that simple!

**Need help with any step? Let me know and I'll guide you through it!**