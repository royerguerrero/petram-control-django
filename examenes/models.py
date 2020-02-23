"""Modelos de la app examenes"""
# Django
from django.db import models

class Examen(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()

    publicado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)
    imagen = models.ImageField(null=True, blank=True)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=200)
    imagen = models.ImageField(null=True, blank=True)
    selecionada = models.IntegerField(default=0)
