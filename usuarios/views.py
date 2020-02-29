"""Vistas de usuarios"""

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error':'Nombre de usuario y contraseña invalida'})

    return render(request, 'login.html')

def forget_password(request, usuario_id):
    return render(request, 'forget_password.html', {'usuario_id':usuario_id})

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')