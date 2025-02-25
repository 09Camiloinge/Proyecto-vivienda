from django.urls import path
from . import views

urlpatterns = [
    path('', views.hogar_list, name='hogar_list'),
    path('nuevo/', views.hogar_create, name='hogar_create'),
]
