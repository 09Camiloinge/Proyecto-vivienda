from django.urls import path
from . import views
from .views import seleccionar_convocatoria

urlpatterns = [
     path('seleccionar/', seleccionar_convocatoria, name='seleccionar_convocatoria'),
]
