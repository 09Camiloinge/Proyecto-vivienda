from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import Convocatoria, Postulacion
from .forms import ConvocatoriaForm, PostulacionForm, InscripcionForm

def formulario_postulacion(request):
    if request.method == "POST":
        form = PostulacionForm(request.POST)
        if form.is_valid():
            form.save()  # Ahora sí guarda porque PostulacionForm es un ModelForm
            return redirect('seleccionar_convocatoria')  # Ajusta la redirección
    else:
        form = PostulacionForm()

    return render(request, "hogares/formulario_postulacion.html", {"form": form})

def postular(request, convocatoria_id):
    convocatoria = get_object_or_404(Convocatoria, id=convocatoria_id)  # Obtiene la convocatoria

    if request.method == "POST":
        form = PostulacionForm(request.POST)
        if form.is_valid():
            postulacion = form.save(commit=False)
            postulacion.convocatoria = convocatoria  # Asigna la convocatoria a la postulación
            postulacion.save()
            return redirect('lista_convocatorias')  # Redirige a la lista de convocatorias
    else:
        form = PostulacionForm()  # Formulario vacío si es GET

    return render(request, 'hogares/formulario_postulacion.html', {
        'form': form,
        'convocatoria': convocatoria
    })

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

def seleccionar_convocatoria(request):
    convocatorias = Convocatoria.objects.all()
    return render(request, 'hogares/seleccionar_convocatoria.html', {'convocatorias': convocatorias})

def postular_convocatoria(request, convocatoria_id):
    convocatoria = get_object_or_404(Convocatoria, id=convocatoria_id)
    if request.method == "POST":
        # Lógica para postular
        pass
    return render(request, 'hogares/formulario_postulacion.html', {'convocatoria': convocatoria})

@user_passes_test(lambda u: u.is_superuser)
def eliminar_convocatoria(request, convocatoria_id):
    convocatoria = get_object_or_404(Convocatoria, id=convocatoria_id)
    convocatoria.delete()
    return redirect('crud_convocatorias')

@user_passes_test(lambda u: u.is_superuser)
def crud_convocatorias(request):
    convocatorias = Convocatoria.objects.all()
    return render(request, 'crud_convocatorias.html', {'convocatorias': convocatorias})
