from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User

from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {"title": 'Geekshop - Aдмин'}
    return render(request, 'admins/index.html', context)


class UserAdminListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Geekshop - Aдмин'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminListView,self).dispatch(request, *args, **kwargs)


#@user_passes_test(lambda u: u.is_staff)
#def admins_users(request):
#    user = User.objects.all()
#    context = {"title": 'Geekshop - Aдмин', 'users': user}
#    return render(request, 'admins/admin-users-read.html', context)


class UserAdminCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins_staff:admins_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminCreateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Geekshop - Aдмин'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminCreateView, self).dispatch(request, *args, **kwargs)


#@user_passes_test(lambda u: u.is_staff)
#def admins_users_create(request):
#    if request.method == 'POST':
#        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#        if form.is_valid():
#            form.save()
#            messages.success(request, 'Пользователь успешно создан!')
#            return HttpResponseRedirect(reverse('admins_staff:admins_users'))
#        else:
#            print(form.errors)
#    else:
#        form = UserAdminRegistrationForm()
#    context = {"title": 'Geekshop - Aдмин', 'form':form}
#    return render(request, 'admins/admin-users-create.html', context)


class UserAdminUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins_staff:admins_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminUpdateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Geekshop - Aдмин'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminUpdateView, self).dispatch(request, *args, **kwargs)

#@user_passes_test(lambda u: u.is_staff)
#def admins_users_update(request, pk):
#    selected_user = User.objects.get(id=pk)
#    if request.method == 'POST':
#        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('admins_staff:admins_users'))
#    else:
#        form = UserAdminProfileForm(instance=selected_user)
#
#    context = {"title": 'Geekshop - Aдмин', 'form': form, 'selected_user': selected_user}
#    return render(request, 'admins/admin-users-update-delete.html', context)


class UserAdminDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins_staff:admins_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.save_delete()
        return HttpResponseRedirect(self.success_url)

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminDeleteView, self).dispatch(request, *args, **kwargs)


#@user_passes_test(lambda u: u.is_staff)
#def admins_users_delete(request, pk):
#    user = User.objects.get(id=pk)
#    user.save_delete()
#    return HttpResponseRedirect(reverse('admins_staff:admins_users'))