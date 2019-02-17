from mainapp.models import Category, Product
from django.forms import ModelForm


class CategoryEditForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'is_valid',)


class ProductEditForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('slug',)
