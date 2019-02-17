from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from mainapp.models import Category


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryListView(ListView):
    model = Category
    template_name = 'adminapp/categories/index.html'


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'adminapp/categories/update.html'
    fields = ('name', 'is_valid',)
    success_url = reverse_lazy('admin:categories')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'adminapp/categories/update.html'
    success_url = reverse_lazy('admin:categories')
    fields = ('name', 'is_valid',)

    def get_context_data(self, **kwargs):
        parent_context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        parent_context['title'] = 'Категории/создание'

        return parent_context

@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'adminapp/categories/delete.html'
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_valid = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

