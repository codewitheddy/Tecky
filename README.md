# Tecky Collections - Tailoring Business Web Application

A Django web application for Tecky Collections, a premium tailoring business in Kenya. The application allows the business to showcase finished projects, manage client quote requests, and handle custom tailoring orders.

## Features

### Public Features
- **Homepage**: Business introduction with featured projects
- **Portfolio**: Display of finished tailoring projects with categories
- **Quote Requests**: Forms for existing product quotes and custom projects
- **Contact**: Business contact information and contact form
- **Mobile-friendly**: Responsive design optimized for mobile devices

### Admin Features
- **Product Management**: Add, edit, and manage finished projects
- **Category Management**: Organize products by categories (Men, Women, Wedding, etc.)
- **Quote Management**: View and manage client quote requests
- **Client Management**: Track client information and history
- **Measurements**: Detailed measurement tracking for each quote

## Business Information
- **Business Name**: Tecky Collections
- **Phone**: 0723835202
- **Email**: teckycollections@gmail.com
- **Market**: Kenya (KES currency, mobile-first)

## Technology Stack
- **Backend**: Django 4.2.7
- **Database**: PostgreSQL (with SQLite fallback for development)
- **Frontend**: Bootstrap 5.3.0 + Django Templates
- **Media**: Pillow for image handling
- **Deployment**: Gunicorn + WhiteNoise

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd tecky_collections
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Environment Variables

Create a `.env` file with the following variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://username:password@localhost:5432/tecky_collections
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Database Configuration

### PostgreSQL (Production)
```
DATABASE_URL=postgresql://username:password@localhost:5432/tecky_collections
```

### SQLite (Development)
```
DATABASE_URL=sqlite:///db.sqlite3
```

## App Structure

- **core**: Homepage, about, contact functionality
- **products**: Product/portfolio management and display
- **quotes**: Quote request handling (existing products and custom projects)
- **clients**: Client information management

## Admin Access

1. Create superuser: `python manage.py createsuperuser`
2. Access admin at: `http://localhost:8000/admin/`
3. Manage categories, products, quotes, and clients

## Key Features

### Quote System
- **Existing Product Quotes**: Clients can request quotes for displayed products
- **Custom Project Quotes**: Clients can submit custom design requests
- **Measurements**: Detailed measurement collection (chest, waist, hips, etc.)
- **WhatsApp Integration**: Direct WhatsApp links for easy communication

### Mobile Optimization
- Responsive Bootstrap design
- Phone-first contact approach
- WhatsApp-friendly messaging
- Touch-friendly interface

## Deployment

### Heroku Deployment
1. Install Heroku CLI
2. Create Heroku app: `heroku create your-app-name`
3. Add PostgreSQL: `heroku addons:create heroku-postgresql:hobby-dev`
4. Set environment variables: `heroku config:set SECRET_KEY=your-secret-key`
5. Deploy: `git push heroku main`
6. Run migrations: `heroku run python manage.py migrate`
7. Create superuser: `heroku run python manage.py createsuperuser`

### Environment Variables for Production
```
SECRET_KEY=your-production-secret-key
DEBUG=False
DATABASE_URL=your-postgresql-url
ALLOWED_HOSTS=your-domain.com,your-app.herokuapp.com
```

## Usage

### Adding Products
1. Login to admin panel
2. Go to Products → Products
3. Add new product with images, description, category
4. Mark as featured if desired

### Managing Quotes
1. View quote requests in admin panel
2. Contact clients via phone/WhatsApp
3. Update quote status as needed
4. Use WhatsApp message generator for follow-ups

### Categories
Common categories to set up:
- Men's Wear
- Women's Wear
- Wedding Attire
- Uniforms
- Casual Wear
- Formal Wear

## Support

For technical support or questions about the application:
- Email: teckycollections@gmail.com
- Phone: 0723835202
- WhatsApp: https://wa.me/254723835202

## License

This project is proprietary software for Tecky Collections.