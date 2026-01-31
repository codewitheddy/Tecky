from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date_completed', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured', 'date_completed', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'date_completed'
    list_editable = ['is_featured']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'category', 'description')
        }),
        ('Images', {
            'fields': ('image', 'additional_images'),
            'description': 'Upload main image and add additional image URLs (one per line)'
        }),
        ('Details', {
            'fields': ('date_completed', 'is_featured')
        }),
    )