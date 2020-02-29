"""Vistas de usuarios"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models
from usuarios.models import Perfil

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # perfil = Perfil.objects.get(user_id=user.id)
            return render(request, 'dashboard.html', {'perfil':perfil})
        else:
            return render(request, 'login.html', {'error':'Nombre de usuario y contraseña invalida'})

    return render(request, 'login.html')

@login_required()
def logout_view(request):
    logout(request)
    return redirect('logout')

def forget_password(request, usuario_id):
    return render(request, 'forget_password.html', {'usuario_id':usuario_id})

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')