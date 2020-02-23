"""Modelos de Usuarios"""
# Django
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    TIPOS_DE_IDENTIFICACION = (
        ('T.I', 'Tarjeta de identidad'),
        ('C.C', 'Cedula de ciudadania'),
        ('C.E', 'Cedula de Extrangeria'),
    )

    tipo_de_id  = models.CharField('Tipo de identificación', max_length=3, choices=TIPOS_DE_IDENTIFICACION)
    numero_id = models.CharField('Número de Identificación', max_length=20)

    CURSOS = (
        ('A2', 'Moto A2'),
        ('B1', 'Carro B1'),
        ('C1', 'Carro C1'),
    )

    ROLES = (
        (1, 'Estudiante'),
        (2, 'Profesor'),
        (3, 'Secretaria'),
    )

    curso = models.CharField(max_length=2, choices=CURSOS, null=True, blank=True)
    rol = models.PositiveSmallIntegerField(choices=ROLES)

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)