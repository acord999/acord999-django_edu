from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse


from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


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
                messages.success(request, f"{user.username}, Вы успешно вошли в аккаунт")
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
     # Проверка была ли попытка авторизации 
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        # Проверка на соответстие форме !ТОЧНЫЕ НАЗВАНИЯ ПОЛЕЙ х)!
        if form.is_valid():
            form.save()
            user = form.instance
            messages.success(request, f"{user.username}, Вы успешно создали аккаунт")
            auth_login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    # Иначе считаем, что пользователь не пытался авторизироваться и подготавливаем страничку авторизации
    else:
        form = UserRegistrationForm()

    
    context = {
        "title": "Регистрация - Home",
        "form": form,
    }
    return render(request, "users/registration.html", context=context)

@login_required
def profile(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профайл успешно обновлен")
            return HttpResponseRedirect(reverse('user:profile'))
    # Иначе считаем, что пользователь не пытался авторизироваться и подготавливаем страничку авторизации
    else:
        form = ProfileForm(instance=request.user)


    context = {
        "title": "Кабинет - Home",
        "form": form,
    }
    return render(request, "users/profile.html", context=context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth_logout(request)
    return HttpResponseRedirect(reverse('main:index'))
