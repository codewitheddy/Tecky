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
        'railway_project': bool(os.environ.get('RAILWAY_PROJECT_ID')),
        'ssl_redirect': getattr(settings, 'SECURE_SSL_REDIRECT', 'Not set'),
        'proxy_ssl_header': getattr(settings, 'SECURE_PROXY_SSL_HEADER', 'Not set'),
        'request_is_secure': request.is_secure(),
        'request_scheme': request.scheme,
        'request_headers': {
            'x-forwarded-proto': request.META.get('HTTP_X_FORWARDED_PROTO'),
            'x-forwarded-for': request.META.get('HTTP_X_FORWARDED_FOR'),
            'host': request.META.get('HTTP_HOST'),
        }
    })