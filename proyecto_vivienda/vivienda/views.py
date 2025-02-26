from django.shortcuts import render, redirect
from .forms import HogarForm


def registrar_hogar(request):
    if request.method == 'POST':
        form = HogarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_hogares')  # Asegúrate de tener esta vista creada
    else:
        form = HogarForm()
    return render(request, 'vivienda/formulario_hogar.html', {'form': form})