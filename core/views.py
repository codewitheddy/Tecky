from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from products.models import Product
from .forms import ContactForm


def home(request):
    """Homepage view with featured products"""
    featured_products = Product.objects.filter(is_featured=True)[:6]
    context = {
        'featured_products': featured_products,
        'business_name': 'Tecky Collections',
        'phone': '0723835202',
        'email': 'teckycollections@gmail.com',
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page view"""
    context = {
        'business_name': 'Tecky Collections',
        'phone': '0723835202',
        'email': 'teckycollections@gmail.com',
    }
    return render(request, 'core/about.html', context)


def contact(request):
    """Contact page view with form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the contact form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            
            # You can add email sending logic here
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'business_name': 'Tecky Collections',
        'phone': '0723835202',
        'email': 'teckycollections@gmail.com',
    }
    return render(request, 'core/contact.html', context)