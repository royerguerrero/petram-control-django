"""Modelos de la app de clases"""

# Django
from django.db import models
# Models
from usuarios.models import Perfil

class Clase(models.Model):
    TIPO_CLASE   = [
        ('PR', 'Practica'),
        ('TR', 'Teorica'),
    ]

    tipo_de_clase = models.CharField('Tipo de clase', max_length=2, choices=TIPO_CLASE)
    estudiante = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    duracion = models.DurationField()

    creada = models.DateTimeField(auto_now_add=True)
    modificada = models.DateTimeField(auto_now=True)


class DetalleClase(models.Model):
    clase = models.OneToOneField(Clase, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Perfil, on_delete=models.CASCADE)


class Vehiculo(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    placa = models.CharField(max_length=6)
    imagen = models.ImageField('clases/vehiculos')
    
    añadido = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
