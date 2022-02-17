from django.urls import path
from django.products import index, products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
]

