"""Petram Control URL Configuration"""
# Django
from django.contrib import admin
from django.urls import path

# Local
from usuarios import views as usuarios_views

urlpatterns = [
    path('', usuarios_views.index, name='index'),
    path('recuperar-password/<int:usuario_id>', usuarios_views.forget_password, name='forget_password')
]
