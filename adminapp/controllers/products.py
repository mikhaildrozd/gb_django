from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect, get_list_or_404
from mainapp.models import Product


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductsListView(ListView):
    # model = Product
    template_name = 'adminapp/product/index.html'

    def get_queryset(self):
        category_id = self.request.path.split('/')[-2]
        queryset = get_list_or_404(Product, category_id=category_id)
        return queryset


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductsCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product/update.html'
    fields = '__all__'

    def get_success_url(self):
        success_url = reverse_lazy('admin:products', kwargs={'pk': self.object.category.pk})
        return success_url


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductsUpdateView(UpdateView):
    model = Product
    template_name = 'adminapp/product/update.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        parent_context = super(ProductsUpdateView, self).get_context_data(**kwargs)
        parent_context['title'] = 'Товары/создание'

        return parent_context

    def get_success_url(self):
        success_url = reverse_lazy('admin:products', kwargs={'pk': self.object.category.pk})
        return success_url


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product/delete.html'

    def get_success_url(self):
        success_url = reverse_lazy('admin:products', kwargs={'pk': self.object.category.pk})
        return success_url

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.available = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
