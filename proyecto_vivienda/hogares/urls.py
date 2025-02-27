from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_hogares, name='lista_hogares'),
     path('seleccionar_convocatoria/', views.seleccionar_convocatoria, name='seleccionar_convocatoria'),

]
