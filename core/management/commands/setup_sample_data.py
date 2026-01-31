from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from products.models import Category, Product
from clients.models import Client
from quotes.models import QuoteRequest, Measurements


class Command(BaseCommand):
    help = 'Create sample data for Tecky Collections'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create categories
        categories_data = [
            {'name': 'Men\'s Wear', 'description': 'Custom suits, shirts, and formal wear for men'},
            {'name': 'Women\'s Wear', 'description': 'Elegant dresses, blouses, and custom designs for women'},
            {'name': 'Wedding Attire', 'description': 'Special occasion wear for weddings and ceremonies'},
            {'name': 'Uniforms', 'description': 'Professional uniforms and corporate wear'},
            {'name': 'Casual Wear', 'description': 'Comfortable everyday clothing'},
        ]
        
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create sample products
        products_data = [
            {
                'name': 'Executive Business Suit',
                'category': 'Men\'s Wear',
                'description': 'Premium tailored business suit in charcoal grey. Perfect fit with attention to detail. Made from high-quality wool blend fabric.',
                'date_completed': date.today() - timedelta(days=30),
                'is_featured': True,
            },
            {
                'name': 'Elegant Evening Dress',
                'category': 'Women\'s Wear',
                'description': 'Stunning evening dress in navy blue silk. Custom fitted with intricate beadwork and flowing silhouette.',
                'date_completed': date.today() - timedelta(days=15),
                'is_featured': True,
            },
            {
                'name': 'Traditional Wedding Suit',
                'category': 'Wedding Attire',
                'description': 'Classic wedding suit with modern touches. Includes jacket, trousers, and matching vest. Perfect for your special day.',
                'date_completed': date.today() - timedelta(days=45),
                'is_featured': True,
            },
            {
                'name': 'Corporate Uniform Set',
                'category': 'Uniforms',
                'description': 'Professional uniform set for corporate environment. Includes blazer, trousers/skirt, and matching accessories.',
                'date_completed': date.today() - timedelta(days=20),
                'is_featured': False,
            },
            {
                'name': 'Casual Cotton Shirt',
                'category': 'Casual Wear',
                'description': 'Comfortable cotton shirt perfect for everyday wear. Available in multiple colors and patterns.',
                'date_completed': date.today() - timedelta(days=10),
                'is_featured': False,
            },
            {
                'name': 'Bridal Gown',
                'category': 'Wedding Attire',
                'description': 'Exquisite bridal gown with lace details and cathedral train. Custom designed for the perfect wedding day look.',
                'date_completed': date.today() - timedelta(days=60),
                'is_featured': True,
            },
        ]
        
        for prod_data in products_data:
            category = Category.objects.get(name=prod_data['category'])
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'category': category,
                    'description': prod_data['description'],
                    'date_completed': prod_data['date_completed'],
                    'is_featured': prod_data['is_featured'],
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')
        
        # Create sample clients
        clients_data = [
            {'full_name': 'John Kamau', 'phone_number': '0712345678', 'email': 'john.kamau@email.com'},
            {'full_name': 'Mary Wanjiku', 'phone_number': '0723456789', 'email': ''},
            {'full_name': 'David Ochieng', 'phone_number': '0734567890', 'email': 'david.ochieng@email.com'},
        ]
        
        for client_data in clients_data:
            client, created = Client.objects.get_or_create(
                phone_number=client_data['phone_number'],
                defaults={
                    'full_name': client_data['full_name'],
                    'email': client_data['email'] if client_data['email'] else None,
                }
            )
            if created:
                self.stdout.write(f'Created client: {client.full_name}')
        
        # Create sample quote requests
        if QuoteRequest.objects.count() == 0:
            clients = Client.objects.all()
            products = Product.objects.all()
            
            quotes_data = [
                {
                    'client': clients[0],
                    'quote_type': 'existing',
                    'product': products[0],
                    'fabric_preference': 'Wool blend, charcoal grey',
                    'status': 'pending',
                    'measurements': {
                        'chest': 42.0, 'waist': 36.0, 'hips': 40.0,
                        'shoulder': 18.0, 'sleeve_length': 25.0, 'full_length': 30.0,
                        'additional_notes': 'Client prefers slim fit'
                    }
                },
                {
                    'client': clients[1],
                    'quote_type': 'custom',
                    'custom_description': 'Traditional African dress with modern touches for wedding ceremony',
                    'fabric_preference': 'Ankara print, bright colors',
                    'status': 'reviewed',
                    'measurements': {
                        'chest': 36.0, 'waist': 28.0, 'hips': 38.0,
                        'shoulder': 15.0, 'sleeve_length': 22.0, 'full_length': 45.0,
                        'additional_notes': 'Floor length preferred'
                    }
                },
                {
                    'client': clients[2],
                    'quote_type': 'existing',
                    'product': products[3],
                    'fabric_preference': 'Navy blue cotton blend',
                    'status': 'quoted',
                    'measurements': {
                        'chest': 40.0, 'waist': 34.0, 'hips': 38.0,
                        'shoulder': 17.0, 'sleeve_length': 24.0, 'full_length': 29.0,
                        'additional_notes': 'Regular fit, professional look'
                    }
                },
                {
                    'client': clients[0],
                    'quote_type': 'custom',
                    'custom_description': 'Casual weekend shirt with unique pattern',
                    'fabric_preference': 'Cotton, light blue with subtle pattern',
                    'status': 'accepted',
                    'measurements': {
                        'chest': 42.0, 'waist': 36.0, 'hips': 40.0,
                        'shoulder': 18.0, 'sleeve_length': 25.0, 'full_length': 28.0,
                        'additional_notes': 'Comfortable fit for casual wear'
                    }
                }
            ]
            
            for quote_data in quotes_data:
                # Create measurements first
                measurements = Measurements.objects.create(**quote_data['measurements'])
                
                # Create quote request
                quote_request = QuoteRequest.objects.create(
                    client=quote_data['client'],
                    quote_type=quote_data['quote_type'],
                    product=quote_data.get('product'),
                    custom_description=quote_data.get('custom_description', ''),
                    fabric_preference=quote_data['fabric_preference'],
                    status=quote_data['status'],
                    measurements=measurements
                )
                
                self.stdout.write(f'Created quote request for {quote_request.client.full_name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )