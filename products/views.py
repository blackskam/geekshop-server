import json
from django.shortcuts import render
from django.conf import settings


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
        'products': json.load(open(file_path_products, encoding='utf-8')),
        'links_menu': json.load(open(file_path_category, encoding='utf-8')),
    }
    return render(request, 'products/products.html', context)
