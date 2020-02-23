"""Vistas de usuarios"""

from django.shortcuts import render

def index(request):
    return render(request, 'login.html')

def forget_password(request, usuario_id):
    return render(request, 'forget_password.html', {'usuario_id':usuario_id})
