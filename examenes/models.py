"""Modelos de la app examenes"""
# Django
from django.db import models
from usuarios.models import Perfil

class Examen(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='')
    fecha_publicacion = models.DateTimeField('Fecha de publicación', auto_now_add=True)
    fecha_modificacion = models.DateTimeField('Fecha de modificación', auto_now=True)

    creado_por = models.ForeignKey('usuarios.Perfil', on_delete=models.SET_DEFAULT)

class Preguntas(models.Model):
    enunciado = models.TextField()
    imagen = models.ImageField()
    examen = models.ForeignKey('Examen', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField('Fecha de publicación', auto_now_add=True)
    fecha_modificacion = models.DateTimeField('Fecha de modificación', auto_now=True)

    creado_por = models.ForeignKey('usuarios.Perfil', on_delete=models.SET_DEFAULT)

class Respuesta(models.Model):
    enunciado = models.CharField(max_length=255)
    imagen = models.ImageField()
    pregunta = models.ForeignKey('Preguntas', on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField('Fecha de publicación', auto_now_add=True)
    fecha_modificacion = models.DateTimeField('Fecha de modificación', auto_now=True)

    creado_por = models.ForeignKey('usuarios.Perfil', on_delete=models.SET_DEFAULT)