from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ConvocatoriaForm

def seleccionar_convocatoria(request):
    form = ConvocatoriaForm()
    convocatoria_seleccionada = None

    if request.method == 'POST':
        form = ConvocatoriaForm(request.POST)
        if form.is_valid():
            convocatoria_seleccionada = form.cleaned_data['convocatoria']

    return render(request, 'hogares/seleccionar_convocatoria.html', {
        'form': form,
        'convocatoria_seleccionada': convocatoria_seleccionada
    })


@login_required
def formulario_hogar(request):
    return render(request, 'hogares/formulario_hogar.html')

@login_required(login_url='login')
def lista_hogares(request):
    # Aquí irán los datos de hogares. Por ahora, una lista de ejemplo.
    hogares = [
        {'nombre': 'Familia Gómez', 'puntaje': 85},
        {'nombre': 'Familia Pérez', 'puntaje': 72},
    ]
    return render(request, 'hogares/lista_hogares.html', {'hogares': hogares})
