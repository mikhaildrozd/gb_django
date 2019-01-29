from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
import datetime
from .models import Category, Product

# Create your views here.

def undex(request: HttpRequest):

    return render(request, 'mainapp/index.html')


def contact(request: HttpRequest):
    title = 'о нас'
    visit_date = datetime.datetime.now()

    locations = [
        {
            'city': 'Москва',
            'phone': '+7-888-888-8888',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД',
        },
        {
            'city': 'Екатеринбург',
            'phone': '+7-777-777-7777',
            'email': 'info_yekaterinburg@geekshop.ru',
            'address': 'Близко к центру',
        },
        {
            'city': 'Владивосток',
            'phone': '+7-999-999-9999',
            'email': 'info_vladivostok@geekshop.ru',
            'address': 'Близко к океану',
        },
    ]

    return render(request, 'mainapp/contact.html', {
        'title': title,
        'visit_date': visit_date,
        'locations': locations
    })

def products(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request,
                  'mainapp/products.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug,):
    categories = Category.objects.all()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request, 'mainapp/product.html', {'product': product,
                                                    'categories': categories,
                                                    })
