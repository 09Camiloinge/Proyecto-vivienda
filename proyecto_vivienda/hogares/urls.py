from django.urls import path
from . import views
from .views import inscribirse_convocatoria

urlpatterns = [
    path('admin/convocatorias/', views.crud_convocatorias, name='crud_convocatorias'),
    path('admin/convocatorias/eliminar/<int:convocatoria_id>/', views.eliminar_convocatoria, name='eliminar_convocatoria'),
    path('seleccionar/', views.seleccionar_convocatoria, name='seleccionar_convocatoria'),
    path('hogares/postular/<int:convocatoria_id>/', views.postular_convocatoria, name='postular'),
    path('agregar_convocatorias/', views.agregar_convocatorias, name='agregar_convocatorias'),
    path('postulacion/', views.formulario_postulacion, name='formulario_postulacion'),
    path('postular/<int:convocatoria_id>/', views.postular, name='postular'),

]	
