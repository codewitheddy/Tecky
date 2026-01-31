from django.contrib import admin
from .models import QuoteRequest, Measurements


class MeasurementsInline(admin.StackedInline):
    model = Measurements
    extra = 0


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = [
        'client', 'quote_type', 'product', 'status', 'created_at'
    ]
    list_filter = ['quote_type', 'status', 'created_at']
    search_fields = ['client__full_name', 'client__phone_number', 'product__name']
    readonly_fields = ['created_at', 'updated_at', 'get_whatsapp_message']
    list_editable = ['status']
    
    fieldsets = (
        ('Client Information', {
            'fields': ('client', 'status')
        }),
        ('Quote Details', {
            'fields': ('quote_type', 'product', 'custom_description', 'reference_image')
        }),
        ('Requirements', {
            'fields': ('fabric_preference', 'additional_notes')
        }),
        ('WhatsApp Follow-up', {
            'fields': ('get_whatsapp_message',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_whatsapp_message(self, obj):
        return obj.get_whatsapp_message()
    get_whatsapp_message.short_description = "WhatsApp Message"


@admin.register(Measurements)
class MeasurementsAdmin(admin.ModelAdmin):
    list_display = ['chest', 'waist', 'hips', 'shoulder', 'sleeve_length', 'full_length']
    search_fields = ['quoterequest__client__full_name']