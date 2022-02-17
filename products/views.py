import json
from django.shortcuts import render
from django.conf import settings
from products.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request):
    file_path_products = settings.BASE_DIR / 'products/fixtures/products.json'
    file_path_category = settings.BASE_DIR / 'products/fixtures/category.json'
    context = {
        'title': 'GeekShop Products',
        'products': Product.objects.all()

        'links_menu': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
