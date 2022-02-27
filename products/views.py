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
    product = Product.objects.all()
    links_menu = ProductCategory.objects.all()
    context = {
        'title': 'GeekShop Products',
        'products': product,
        'links_menu': links_menu,
    }
    return render(request, 'products/products.html', context)
