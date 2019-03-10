from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from .form import ShopUserLoginForm, ShopUserRegisterForm, ShopUserUpdateForm
from django.contrib import auth
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import send_mail
from django.conf import settings
from .models import ShopUser


def login(request: HttpRequest):
    title = 'войти на сайт'

    # создать форму для заполнения
    login_form = ShopUserLoginForm(data=request.POST or None)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    # проверить данные из request
    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']
        # try:
        # next_url = request.POST.get('next') or '/'
        # except MultiValueDictKeyError:
        #     next_url = '/'
        # выполнить аутентификацию
        user = auth.authenticate(username=login, password=password)

        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))

    content = {
        'title': title,
        'login_form': login_form,
        'next': next
    }
    return render(request, 'authapp/login.html', content)



def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')


def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect('/auth/login')


def register(request: HttpRequest):
    title = 'регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save()

            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('Ошибка  отправки сообщения')
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

def send_verify_mail(user):
    verify_link = reverse(
        'auth:verify',
        args=[user.email, user.activation_key])

    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} \
    на портале {settings.DOMAIN_NAME} перейдите по ссылке: \
    \n{settings.DOMAIN_NAME}{verify_link}'

    print(f'from: {settings.EMAIL_HOST_USER}, to: {user.email}')
    return send_mail(
            title,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )

def verify(request:HttpRequest, email, activation_key):

    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            print(f'user {user} is activated')
            user.is_active = True
            user.save()
            auth.login(request, user)

            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')

    except Exception as e:
        print(f'error activation user : {e.args}0000')

    return HttpResponseRedirect(reverse('main'))