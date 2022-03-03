from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from users.models import User

from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

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
            messages.success(request, 'Пользователь успешно создан!')
            return HttpResponseRedirect(reverse('admins_staff:admins_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {"title": 'Geekshop - Aдмин', 'form':form}
    return render(request, 'admins/admin-users-create.html', context)

def admins_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins_staff:admins_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)

    context = {"title": 'Geekshop - Aдмин', 'form': form, 'selected_user': selected_user}
    return render(request, 'admins/admin-users-update-delete.html', context)