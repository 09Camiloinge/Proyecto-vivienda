from django.shortcuts import render, redirect
from .models import Hogar
from .forms import HogarForm

def hogar_list(request):
    hogares = Hogar.objects.all()
    return render(request, 'vivienda/hogar_list.html', {'hogares': hogares})

def hogar_create(request):
    if request.method == 'POST':
        form = HogarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hogar_list')
    else:
        form = HogarForm()
    return render(request, 'vivienda/hogar_form.html', {'form': form})
