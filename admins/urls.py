from django.urls import path
from admins.views import index, UserAdminListView, UserAdminCreateView, admins_users_update, admins_users_delete

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserAdminListView.as_view(), name='admins_users'),
    path('users-create/', UserAdminCreateView.as_view(), name='admins_users_create'),
    path('users-update/<int:pk>', admins_users_update, name='admins_users_update'),
    path('users-delete/<int:pk>', admins_users_delete, name='admins_users_delete'),
]
