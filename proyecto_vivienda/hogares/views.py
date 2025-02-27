from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from hogares.models import Convocatoria
from .forms import SeleccionConvocatoriaForm

def seleccionar_convocatoria(request):
    form = SeleccionConvocatoriaForm()

    if request.method == 'POST':
        form = SeleccionConvocatoriaForm(request.POST)
        if form.is_valid():
            convocatoria_seleccionada = form.cleaned_data['convocatoria']
            return render(request, 'hogares/convocatoria_seleccionada.html', {'convocatoria': convocatoria_seleccionada})

    return render(request, 'hogares/seleccionar_convocatoria.html', {'form': form})

@login_required
def formulario_hogar(request):
    return render(request, 'hogares/formulario_hogar.html')

