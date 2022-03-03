from django.urls import path
from admins.views import index, admins_users, admins_users_create, admins_users_update


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', admins_users, name='admins_users'),
    path('users-create/', admins_users_create, name='admins_users_create'),
    path('users-update/<int:pk>', admins_users_update, name='admins_users_update'),
]
