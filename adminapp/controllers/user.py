from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from authapp.models import ShopUser


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/user/users.html'


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user/update.html'
    fields = ('username', 'first_name', 'password', 'email')
    success_url = reverse_lazy('admin:users')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user/update.html'
    success_url = reverse_lazy('admin:users')
    fields = ('username', 'first_name', 'age', 'password', 'email', 'avatar', 'sity',)

    def get_context_data(self, **kwargs):
        parent_context = super(UserUpdateView, self).get_context_data(**kwargs)
        parent_context['title'] = 'пользователи/создание'

        return parent_context


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user/delete.html'
    success_url = reverse_lazy('admin:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
