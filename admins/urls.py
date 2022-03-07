from django.urls import path
from admins.views import index, UserAdminListView, UserAdminCreateView, UserAdminUpdateView, admins_users_delete, UserAdminDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserAdminListView.as_view(), name='admins_users'),
    path('users-create/', UserAdminCreateView.as_view(), name='admins_users_create'),
    path('users-update/<int:pk>', UserAdminUpdateView.as_view(), name='admins_users_update'),
    path('users-delete/<int:pk>', UserAdminDeleteView.as_view(), name='admins_users_delete'),
]
