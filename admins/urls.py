from django.urls import path
from admins.views import index, admins_users, admins_users_create


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admins_users, name='admins_users'),
    path('users-create/', admins_users_create, name='admins_users_create'),
]
