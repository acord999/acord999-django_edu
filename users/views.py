from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse


from users.forms import UserLoginForm


def login(request):
    # Проверка была ли попытка авторизации 
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        # Проверка на соответстие форме !ТОЧНЫЕ НАЗВАНИЯ ПОЛЕЙ х)!
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            # В случае нахождения в БД совпадений вернет AbstractBaseUser else None
            user = authenticate(username=username, password=password)
            # Проверка на успешность
            if user:
                # Авторизация на сайте
                auth_login(request, user)
                # Переброс на целевую страницу после успешной авторизации
                return HttpResponseRedirect(reverse('main:index'))
    # Иначе считаем, что пользователь не пытался авторизироваться и подготавливаем страничку авторизации
    else:
        form = UserLoginForm()

    
    context = {
        "title": "Авторизация - Home",
        "form": form,
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
