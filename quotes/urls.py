from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('existing/<slug:product_slug>/', views.existing_product_quote, name='existing_product'),
    path('custom/', views.custom_project_quote, name='custom_project'),
]