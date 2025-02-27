from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Convocatoria
from .forms import ConvocatoriaForm
from django.contrib.auth.decorators import user_passes_test
from .forms import InscripcionForm  # Asegúrate de que tienes el formulario
from django.http import HttpResponse
from hogares.models import Convocatoria

def agregar_convocatorias(request):
    convocatorias = [
        {"nombre": "1", "descripcion": "Convocatoria 1", "fecha_inicio": "2025-03-01", "fecha_fin": "2025-03-31"},
        {"nombre": "2", "descripcion": "Convocatoria 2", "fecha_inicio": "2025-04-01", "fecha_fin": "2025-04-30"},
        {"nombre": "3", "descripcion": "Convocatoria 3", "fecha_inicio": "2025-05-01", "fecha_fin": "2025-05-31"},
        {"nombre": "4", "descripcion": "Convocatoria 4", "fecha_inicio": "2025-06-01", "fecha_fin": "2025-06-30"},
    ]

    for data in convocatorias:
        Convocatoria.objects.create(**data)

    return HttpResponse("Convocatorias agregadas correctamente.")


# Muestra la lista de convocatorias
def seleccionar_convocatoria(request):
    convocatorias = Convocatoria.objects.all()
    return render(request, 'hogares/seleccionar_convocatoria.html', {'convocatorias': convocatorias})

# Redirige al formulario de inscripción con la convocatoria seleccionada
def inscribirse_convocatoria(request, convocatoria_id):
    convocatoria = get_object_or_404(Convocatoria, id=convocatoria_id)

    if request.method == "POST":
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.convocatoria = convocatoria  # Asignamos la convocatoria
            inscripcion.save()
            return redirect('seleccionar_convocatoria')  # Redirige al usuario después de inscribirse
    else:
        form = InscripcionForm()

    return render(request, 'hogares/formulario_convocatoria.html', {'form': form, 'convocatoria': convocatoria})

@user_passes_test(lambda u: u.is_superuser)
def eliminar_convocatoria(request, convocatoria_id):
    convocatoria = get_object_or_404(Convocatoria, id=convocatoria_id)
    convocatoria.delete()
    return redirect('crud_convocatorias')

# Vista para el CRUD (solo superusuario)
@user_passes_test(lambda u: u.is_superuser)
def crud_convocatorias(request):
    convocatorias = Convocatoria.objects.all()
    return render(request, 'crud_convocatorias.html', {'convocatorias': convocatorias})
