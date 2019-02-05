from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from .form import ShopUserLoginForm, ShopUserRegisterForm, ShopUserUpdateForm
from django.contrib import auth
from django.urls import reverse

def login(request: HttpRequest):
    title = 'войти на сайт'

    # создать форму для заполнения
    login_form = ShopUserLoginForm(data=request.POST)

    # проверить данные из request
    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']

        # выполнить аутентификацию
        user = auth.authenticate(username=login, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    content = {
        'title': title,
        'login_form': login_form
    }
    return render(request, 'authapp/login.html', content)


def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')

def redirect_to_login(request:HttpRequest):
    return HttpResponseRedirect('/auth/login')

def register(request: HttpRequest):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {
        'title': title,
        'reg_form': register_form
    }

    return render(request, 'authapp/register.html', content)


def edit(request: HttpRequest):
    title = 'профиль'

    if request.method == 'POST':
        update_form = ShopUserUpdateForm(request.POST, instance=request.user)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        update_form = ShopUserUpdateForm(instance=request.user)

    content = {
        'title': title,
        'update_form': update_form
    }

    return render(request, 'authapp/edit.html', content)
