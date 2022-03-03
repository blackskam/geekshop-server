from django.shortcuts import render


def index(request):
    context = {"title": 'Geekshop - Aдмин. панель'}
    return render(request, 'admins/index.html', context)