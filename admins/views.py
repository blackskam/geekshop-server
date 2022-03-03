from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User

from admins.forms import UserAdminRegistrationForm

def index(request):
    context = {"title": 'Geekshop - Aдмин'}
    return render(request, 'admins/index.html', context)

def admins_users(request):
    user = User.objects.all()
    context = {"title": 'Geekshop - Aдмин', 'users': user}
    return render(request, 'admins/admin-users-read.html', context)

def admins_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins_staff:admins_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {"title": 'Geekshop - Aдмин', 'form':form}
    return render(request, 'admins/admin-users-create.html', context)