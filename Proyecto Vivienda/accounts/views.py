from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'accounts/home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio
        else:
            messages.error(request, 'Identificación o contraseña incorrecta.')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
