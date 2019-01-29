from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='product_list'),
    path('<str:category_slug>/',
         views.products,
         name='product_list_by_category'),
    path('<id>/<str:slug>/',
         views.product_detail,
         name='product_detail'),
]