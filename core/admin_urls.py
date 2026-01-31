from django.urls import path
from django.contrib.auth.views import LogoutView
from . import admin_views
from .admin_auth import AdminLoginView

app_name = 'dashboard'

urlpatterns = [
    path('', admin_views.admin_dashboard, name='dashboard'),
    path('clients/', admin_views.admin_clients, name='clients'),
    path('products/', admin_views.admin_products, name='products'),
    path('quotes/', admin_views.admin_quotes, name='quotes'),
    path('quotes/<int:quote_id>/', admin_views.admin_quote_detail, name='quote_detail'),
    path('api/analytics/', admin_views.admin_analytics_api, name='analytics_api'),
    path('login/', AdminLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]