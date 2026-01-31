from django.http import JsonResponse
from django.db import connection
from django.conf import settings
import os

def health_check(request):
    """Simple health check endpoint for debugging"""
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        db_status = "OK"
    except Exception as e:
        db_status = f"ERROR: {str(e)}"
    
    return JsonResponse({
        'status': 'OK',
        'database': db_status,
        'debug': settings.DEBUG,
        'allowed_hosts': settings.ALLOWED_HOSTS,
        'database_url_set': bool(os.environ.get('DATABASE_URL')),
        'secret_key_set': bool(settings.SECRET_KEY and len(settings.SECRET_KEY) > 10),
        'railway_env': bool(os.environ.get('RAILWAY_ENVIRONMENT')),
    })