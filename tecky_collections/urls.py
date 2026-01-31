"""
URL configuration for tecky_collections project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.admin_redirect import admin_redirect
from core.health_check import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-dashboard/', admin_redirect),
    path('dashboard/', include('core.admin_urls')),
    path('health/', health_check),  # Health check endpoint
    path('', include('core.urls')),
    path('products/', include('products.urls')),
    path('quotes/', include('quotes.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Admin site customization
admin.site.site_header = "Tecky Collections Admin"
admin.site.site_title = "Tecky Collections"
admin.site.index_title = "Welcome to Tecky Collections Administration"