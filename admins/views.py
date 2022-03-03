from django.shortcuts import render
from users.models import User


def index(request):
    context = {"title": 'Geekshop - Aдмин'}
    return render(request, 'admins/index.html', context)

def admins_users(request):
    user = User.objects.all()
    context = {"title": 'Geekshop - Aдмин', 'users': user}
    return render(request, 'admins/admin-users-read.html', context)