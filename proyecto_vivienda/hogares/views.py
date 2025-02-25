from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def lista_hogares(request):
    # Aquí irán los datos de hogares. Por ahora, una lista de ejemplo.
    hogares = [
        {'nombre': 'Familia Gómez', 'puntaje': 85},
        {'nombre': 'Familia Pérez', 'puntaje': 72},
    ]
    return render(request, 'hogares/lista_hogares.html', {'hogares': hogares})
