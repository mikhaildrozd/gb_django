from django.contrib.auth.decorators import user_passes_test
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from mainapp.models import Category
from adminapp.forms.products import CategoryEditForm


@user_passes_test(lambda user: user.is_superuser)
def categories(request: HttpRequest):
    categories_list = Category.objects.all()

    return render(request, 'adminapp/categories/index.html', {
        'objects': categories_list,
    })


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):

    if request.method == 'POST':
        form = CategoryEditForm(request.POST, request.FILES)

        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        form = CategoryEditForm()

    return render(request,'adminapp/categories/update.html', {'form': form})


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id):
    model = get_object_or_404(Category, pk=id)

    if request.method == 'POST':
        form = CategoryEditForm(request.POST, request.FILES, instance=model)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('admin:category_update',args=[model.pk]))
    else:
        form = CategoryEditForm(instance=model)

    return render(request, 'adminapp/categories/update.html', {
        'form': form,
    })


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    category = get_object_or_404(Category, pk=id)

    if request.method == 'POST':
        category.is_valid = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {'category_to_delete': category}
    return render(request,'adminapp/categories/delete.html',content)
