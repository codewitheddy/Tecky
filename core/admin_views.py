from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.core.paginator import Paginator

from clients.models import Client
from products.models import Product, Category
from quotes.models import QuoteRequest, Measurements


@staff_member_required
def admin_dashboard(request):
    """Modern admin dashboard with statistics and recent activity"""
    
    # Get date ranges
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    
    # Statistics
    stats = {
        'total_clients': Client.objects.count(),
        'new_clients_this_week': Client.objects.filter(created_at__date__gte=week_ago).count(),
        'total_products': Product.objects.count(),
        'featured_products': Product.objects.filter(is_featured=True).count(),
        'total_quotes': QuoteRequest.objects.count(),
        'pending_quotes': QuoteRequest.objects.filter(status='pending').count(),
        'quotes_this_month': QuoteRequest.objects.filter(created_at__date__gte=month_ago).count(),
    }
    
    # Recent activity
    recent_quotes = QuoteRequest.objects.select_related('client', 'product').order_by('-created_at')[:5]
    recent_clients = Client.objects.order_by('-created_at')[:5]
    recent_products = Product.objects.select_related('category').order_by('-created_at')[:5]
    
    # Quote status distribution
    quote_status_data = QuoteRequest.objects.values('status').annotate(count=Count('id'))
    
    # Monthly quote trends (last 6 months)
    monthly_quotes = []
    for i in range(6):
        month_start = today.replace(day=1) - timedelta(days=i*30)
        month_end = month_start + timedelta(days=30)
        count = QuoteRequest.objects.filter(
            created_at__date__gte=month_start,
            created_at__date__lt=month_end
        ).count()
        monthly_quotes.append({
            'month': month_start.strftime('%b %Y'),
            'count': count
        })
    monthly_quotes.reverse()
    
    context = {
        'stats': stats,
        'recent_quotes': recent_quotes,
        'recent_clients': recent_clients,
        'recent_products': recent_products,
        'quote_status_data': list(quote_status_data),
        'monthly_quotes': monthly_quotes,
    }
    
    return render(request, 'admin/dashboard.html', context)


@staff_member_required
def admin_clients(request):
    """Client management page"""
    search_query = request.GET.get('search', '')
    clients = Client.objects.prefetch_related('quote_requests').all()
    
    if search_query:
        clients = clients.filter(
            Q(full_name__icontains=search_query) |
            Q(phone_number__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    clients = clients.order_by('-created_at')
    
    # Add quote counts to each client
    for client in clients:
        client.total_quotes = client.quote_requests.count()
        client.pending_quotes = client.quote_requests.filter(status='pending').count()
    
    # Pagination
    paginator = Paginator(clients, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'total_clients': Client.objects.count(),
    }
    
    return render(request, 'admin/clients.html', context)


@staff_member_required
def admin_products(request):
    """Product management page"""
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    featured_filter = request.GET.get('featured', '')
    
    products = Product.objects.select_related('category')
    
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    if category_filter:
        products = products.filter(category_id=category_filter)
    
    if featured_filter == 'true':
        products = products.filter(is_featured=True)
    elif featured_filter == 'false':
        products = products.filter(is_featured=False)
    
    products = products.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'category_filter': category_filter,
        'featured_filter': featured_filter,
        'total_products': Product.objects.count(),
    }
    
    return render(request, 'admin/products.html', context)


@staff_member_required
def admin_quotes(request):
    """Quote management page"""
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    quote_type_filter = request.GET.get('quote_type', '')
    
    quotes = QuoteRequest.objects.select_related('client', 'product', 'measurements')
    
    if search_query:
        quotes = quotes.filter(
            Q(client__full_name__icontains=search_query) |
            Q(client__phone_number__icontains=search_query) |
            Q(product__name__icontains=search_query)
        )
    
    if status_filter:
        quotes = quotes.filter(status=status_filter)
    
    if quote_type_filter:
        quotes = quotes.filter(quote_type=quote_type_filter)
    
    quotes = quotes.order_by('-created_at')
    
    # Pagination
    paginator = Paginator(quotes, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'quote_type_filter': quote_type_filter,
        'status_choices': QuoteRequest.STATUS_CHOICES,
        'quote_type_choices': QuoteRequest.QUOTE_TYPES,
        'total_quotes': QuoteRequest.objects.count(),
    }
    
    return render(request, 'admin/quotes.html', context)


@staff_member_required
def admin_quote_detail(request, quote_id):
    """Quote detail and edit page"""
    quote = get_object_or_404(QuoteRequest, id=quote_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(QuoteRequest.STATUS_CHOICES):
            quote.status = new_status
            quote.save()
            messages.success(request, f'Quote status updated to {quote.get_status_display()}')
            return redirect('admin:quote_detail', quote_id=quote.id)
    
    context = {
        'quote': quote,
        'status_choices': QuoteRequest.STATUS_CHOICES,
    }
    
    return render(request, 'admin/quote_detail.html', context)


@staff_member_required
def admin_analytics_api(request):
    """API endpoint for dashboard analytics"""
    # Quote status distribution
    status_data = list(QuoteRequest.objects.values('status').annotate(count=Count('id')))
    
    # Monthly trends
    today = timezone.now().date()
    monthly_data = []
    for i in range(12):
        month_start = today.replace(day=1) - timedelta(days=i*30)
        month_end = month_start + timedelta(days=30)
        quotes_count = QuoteRequest.objects.filter(
            created_at__date__gte=month_start,
            created_at__date__lt=month_end
        ).count()
        clients_count = Client.objects.filter(
            created_at__date__gte=month_start,
            created_at__date__lt=month_end
        ).count()
        monthly_data.append({
            'month': month_start.strftime('%b'),
            'quotes': quotes_count,
            'clients': clients_count
        })
    monthly_data.reverse()
    
    return JsonResponse({
        'status_distribution': status_data,
        'monthly_trends': monthly_data
    })