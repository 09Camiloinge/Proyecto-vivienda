from django.urls import path
from . import views
from .views import seleccionar_convocatoria
from .views import seleccionar_convocatoria, inscribirse_convocatoria, crud_convocatorias, eliminar_convocatoria
from .views import agregar_convocatorias
from .views import formulario_postulacion
    
urlpatterns = [
    
    path('admin/convocatorias/', crud_convocatorias, name='crud_convocatorias'),
    path('admin/convocatorias/eliminar/<int:convocatoria_id>/', eliminar_convocatoria, name='eliminar_convocatoria'),
    path('seleccionar/', views.seleccionar_convocatoria, name='seleccionar_convocatoria'),
    path('inscribirse/<int:convocatoria_id>/', views.inscribirse_convocatoria, name='inscribirse_convocatoria'),
    path('agregar_convocatorias/', agregar_convocatorias, name='agregar_convocatorias'),
    path('postulacion/', formulario_postulacion, name='formulario_postulacion'),
    path('postular/', views.postular, name='postular')

]
