from django.db import models
from clients.models import Client
from products.models import Product


class Measurements(models.Model):
    chest = models.DecimalField(max_digits=5, decimal_places=1, help_text="in inches")
    waist = models.DecimalField(max_digits=5, decimal_places=1, help_text="in inches")
    hips = models.DecimalField(max_digits=5, decimal_places=1, help_text="in inches")
    shoulder = models.DecimalField(max_digits=5, decimal_places=1, help_text="in inches")
    sleeve_length = models.DecimalField(max_digits=5, decimal_places=1, help_text="in inches")
    full_length = models.DecimalField(max_digits=5, decimal_places=1, help_text="in inches")
    additional_notes = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Measurements"
    
    def __str__(self):
        return f"Measurements - Chest: {self.chest}, Waist: {self.waist}"


class QuoteRequest(models.Model):
    QUOTE_TYPES = [
        ('existing', 'Existing Product'),
        ('custom', 'Custom Project'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('quoted', 'Quoted'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='quote_requests')
    quote_type = models.CharField(max_length=10, choices=QUOTE_TYPES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    # For existing product quotes
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        help_text="Required for existing product quotes"
    )
    
    # For custom project quotes
    custom_description = models.TextField(
        blank=True,
        help_text="Required for custom project quotes"
    )
    reference_image = models.ImageField(
        upload_to='quote_references/', 
        blank=True, 
        null=True,
        help_text="Optional reference image for custom projects"
    )
    
    # Common fields
    fabric_preference = models.CharField(max_length=200)
    measurements = models.OneToOneField(Measurements, on_delete=models.CASCADE)
    additional_notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        if self.quote_type == 'existing' and self.product:
            return f"Quote for {self.product.name} - {self.client.full_name}"
        else:
            return f"Custom Quote - {self.client.full_name}"
    
    def get_whatsapp_message(self):
        """Generate WhatsApp message for quote follow-up"""
        base_msg = f"Hello {self.client.full_name}, thank you for your quote request"
        if self.quote_type == 'existing' and self.product:
            base_msg += f" for {self.product.name}"
        base_msg += ". We will review your requirements and get back to you soon. - Tecky Collections"
        return base_msg