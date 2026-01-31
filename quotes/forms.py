from django import forms
from .models import QuoteRequest, Measurements
from clients.models import Client
from products.models import Product


class MeasurementsForm(forms.ModelForm):
    class Meta:
        model = Measurements
        fields = [
            'chest', 'waist', 'hips', 'shoulder', 
            'sleeve_length', 'full_length', 'additional_notes'
        ]
        widgets = {
            'chest': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., 38.5',
                'step': '0.1'
            }),
            'waist': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., 32.0',
                'step': '0.1'
            }),
            'hips': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., 40.0',
                'step': '0.1'
            }),
            'shoulder': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., 16.5',
                'step': '0.1'
            }),
            'sleeve_length': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., 24.0',
                'step': '0.1'
            }),
            'full_length': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'e.g., 42.0',
                'step': '0.1'
            }),
            'additional_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Any additional measurement notes...'
            }),
        }


class ExistingProductQuoteForm(forms.Form):
    # Client information
    full_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Full Name'
        })
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '0723835202'
        })
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com (Optional)'
        })
    )
    
    # Quote details
    fabric_preference = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., Cotton, Silk, Polyester blend'
        })
    )
    additional_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Any special requirements or notes...'
        })
    )


class CustomProjectQuoteForm(forms.Form):
    # Client information
    full_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Full Name'
        })
    )
    phone_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '0723835202'
        })
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com (Optional)'
        })
    )
    
    # Custom project details
    custom_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Describe your custom project in detail...'
        })
    )
    fabric_preference = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g., Cotton, Silk, Polyester blend'
        })
    )
    reference_image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        })
    )
    additional_notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Any additional requirements...'
        })
    )