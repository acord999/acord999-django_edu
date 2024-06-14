from django.http import HttpResponse
from django.shortcuts import render


from goods.models import Categories


def login(request):
    context = {
        "title": "Авторизация - Home",
    }
    return render(request, "users/login.html", context=context)


def registration(request):
    context = {
        "title": "Регистрация - Home",
    }
    return render(request, "users/registration.html", context=context)


def profile(request):
    context = {
        "title": "Профиль - Home",
    }
    return render(request, "users/profile.html", context=context)


def logout(request):
    pass
