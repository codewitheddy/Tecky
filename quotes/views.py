from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import transaction
from products.models import Product
from clients.models import Client
from .models import QuoteRequest, Measurements
from .forms import ExistingProductQuoteForm, CustomProjectQuoteForm, MeasurementsForm


def existing_product_quote(request, product_slug):
    """Quote request for existing product"""
    product = get_object_or_404(Product, slug=product_slug)
    
    if request.method == 'POST':
        quote_form = ExistingProductQuoteForm(request.POST)
        measurements_form = MeasurementsForm(request.POST)
        
        if quote_form.is_valid() and measurements_form.is_valid():
            try:
                with transaction.atomic():
                    # Create or get client
                    client, created = Client.objects.get_or_create(
                        phone_number=quote_form.cleaned_data['phone_number'],
                        defaults={
                            'full_name': quote_form.cleaned_data['full_name'],
                            'email': quote_form.cleaned_data['email'],
                        }
                    )
                    
                    # Create measurements
                    measurements = measurements_form.save()
                    
                    # Create quote request
                    quote_request = QuoteRequest.objects.create(
                        client=client,
                        quote_type='existing',
                        product=product,
                        fabric_preference=quote_form.cleaned_data['fabric_preference'],
                        additional_notes=quote_form.cleaned_data['additional_notes'],
                        measurements=measurements
                    )
                    
                    messages.success(
                        request, 
                        f'Your quote request for {product.name} has been submitted successfully! '
                        f'We will contact you at {client.phone_number} soon.'
                    )
                    return redirect('products:detail', slug=product.slug)
                    
            except Exception as e:
                messages.error(request, 'There was an error submitting your quote. Please try again.')
    else:
        quote_form = ExistingProductQuoteForm()
        measurements_form = MeasurementsForm()
    
    context = {
        'product': product,
        'quote_form': quote_form,
        'measurements_form': measurements_form,
    }
    return render(request, 'quotes/existing_product_quote.html', context)


def custom_project_quote(request):
    """Quote request for custom project"""
    if request.method == 'POST':
        quote_form = CustomProjectQuoteForm(request.POST, request.FILES)
        measurements_form = MeasurementsForm(request.POST)
        
        if quote_form.is_valid() and measurements_form.is_valid():
            try:
                with transaction.atomic():
                    # Create or get client
                    client, created = Client.objects.get_or_create(
                        phone_number=quote_form.cleaned_data['phone_number'],
                        defaults={
                            'full_name': quote_form.cleaned_data['full_name'],
                            'email': quote_form.cleaned_data['email'],
                        }
                    )
                    
                    # Create measurements
                    measurements = measurements_form.save()
                    
                    # Create quote request
                    quote_request = QuoteRequest.objects.create(
                        client=client,
                        quote_type='custom',
                        custom_description=quote_form.cleaned_data['custom_description'],
                        fabric_preference=quote_form.cleaned_data['fabric_preference'],
                        reference_image=quote_form.cleaned_data['reference_image'],
                        additional_notes=quote_form.cleaned_data['additional_notes'],
                        measurements=measurements
                    )
                    
                    messages.success(
                        request, 
                        f'Your custom project quote request has been submitted successfully! '
                        f'We will contact you at {client.phone_number} soon.'
                    )
                    return redirect('core:home')
                    
            except Exception as e:
                messages.error(request, 'There was an error submitting your quote. Please try again.')
    else:
        quote_form = CustomProjectQuoteForm()
        measurements_form = MeasurementsForm()
    
    context = {
        'quote_form': quote_form,
        'measurements_form': measurements_form,
    }
    return render(request, 'quotes/custom_project_quote.html', context)