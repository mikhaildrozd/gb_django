from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from mainapp.models import Product, Category
from adminapp.forms.products import ProductEditForm

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/product/index.html', content)

@user_passes_test(lambda user: user.is_superuser)
def product_create(request: HttpRequest,pk):
    products = Product.objects.filter()
    return HttpResponse('action -> create')

@user_passes_test(lambda user: user.is_superuser)
def product_read(request: HttpRequest, pk):
    title = 'продукт/подробнее'

    product = get_object_or_404(Product, pk=pk)

    content = {'title': title, 'object': product, }

    return render(request, 'adminapp/product/read.html', content)

@user_passes_test(lambda user: user.is_superuser)
def list_by_category(request: HttpRequest, category):
    return HttpResponse('action -> list')

@user_passes_test(lambda user: user.is_superuser)
def product_update(request, pk):
    title = 'продукт/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form, 'category': edit_product.category}

    return render(request, 'adminapp/product/update.html', content)

@user_passes_test(lambda user: user.is_superuser)
def product_delete(request, pk):
    title = 'продукт/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.available = False
        product.save()
        return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))

    content = {
        'title': title,
        'product_to_delete': product
    }

    return render(request, 'adminapp/product/delete.html', content)