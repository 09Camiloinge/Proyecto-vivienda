from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_hogares, name='lista_hogares'),
     path('formulario/', views.formulario_hogar, name='formulario_hogar'),
]
