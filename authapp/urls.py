from django.urls import path
from . import views

app_name = 'authapp'

urlpatterns = [
    path('',views.redirect_to_login, name='index'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
