from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_hogar, name='registrar_hogar'),
]
