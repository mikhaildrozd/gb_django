from django.urls import path

from adminapp.views import product
from adminapp.controllers import user, categorie, products
app_name = 'adminapp'

urlpatterns = [
    # users (create, read, update, delete)
    # path('users/index', users.index, name='users'),
    # path('users/create/', users.create, name='user_create'),  # admin:user_create
    # path('users/read/<int:id>', users.read, name='user_read'),
    # path('users/update/<int:id>', users.update, name='user_update'),
    path('users/delete/<int:pk>/', user.UserDeleteView.as_view(), name='user_delete'),
    path('users/read/', user.UserListView.as_view(), name='users'),
    path('users/create/', user.UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/', user.UserUpdateView.as_view(), name='user_update'),

    # categories (CRUD)
    path('categories/index/', categorie.CategoryListView.as_view(), name='categories'),
    path('categories/create/', categorie.CategoryCreateView.as_view(), name='category_create'),
    path('categories/update/<int:pk>', categorie.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>', categorie.CategoryDeleteView.as_view(), name='category_delete'),

    # products (CRUD, list_by_category)
    path('products/create/category/', products.ProductsCreateView.as_view(), name='product_create'),
    path('products/read/category/<int:pk>/', products.ProductsListView.as_view(), name='products'),
    path('products/read/<int:pk>/', product.product_read, name='product_read'),
    path('products/update/<int:pk>/', products.ProductsUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', products.ProductsDeleteView.as_view(), name='product_delete'),
]
