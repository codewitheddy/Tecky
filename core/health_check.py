from django.http import JsonResponse
from django.db import connection
from django.conf import settings
import os

def health_check(request):
    """Railway-optimized health check endpoint"""
    try:
        # Test database connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        
        db_status = "OK"
        db_engine = connection.vendor
    except Exception as e:
        db_status = f"ERROR: {str(e)}"
        db_engine = "unknown"
    
    # Railway environment detection
    is_railway = bool(os.environ.get('RAILWAY_ENVIRONMENT_NAME') or os.environ.get('RAILWAY_PROJECT_ID'))
    
    return JsonResponse({
        'status': 'OK',
        'service': 'Tecky Collections',
        'version': '1.0.0',
        'database': {
            'status': db_status,
            'engine': db_engine,
            'url_configured': bool(os.environ.get('DATABASE_URL')),
        },
        'environment': {
            'debug': settings.DEBUG,
            'allowed_hosts': settings.ALLOWED_HOSTS,
            'is_railway': is_railway,
            'railway_env': os.environ.get('RAILWAY_ENVIRONMENT_NAME', 'unknown'),
            'railway_project': os.environ.get('RAILWAY_PROJECT_ID', 'unknown'),
        },
        'security': {
            'secret_key_set': bool(settings.SECRET_KEY and len(settings.SECRET_KEY) > 20),
            'ssl_redirect': getattr(settings, 'SECURE_SSL_REDIRECT', False),
            'proxy_ssl_header': getattr(settings, 'SECURE_PROXY_SSL_HEADER', None),
        },
        'request_info': {
            'is_secure': request.is_secure(),
            'scheme': request.scheme,
            'host': request.get_host(),
            'headers': {
                'x-forwarded-proto': request.META.get('HTTP_X_FORWARDED_PROTO'),
                'x-forwarded-for': request.META.get('HTTP_X_FORWARDED_FOR'),
                'user-agent': request.META.get('HTTP_USER_AGENT', '')[:50] + '...',
            }
        }
    })