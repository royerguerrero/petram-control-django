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
<<<<<<< HEAD
    pregunta = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    correcta = models.BooleanField('Respuesta Correnta', default=False)
=======
    pregunta = models.ForeignKey('Preguntas', on_delete=models.CASCADE)
>>>>>>> 1aa6ba53373c9f5bf72ef8ff30be5d9ce9df2232
    fecha_publicacion = models.DateTimeField('Fecha de publicación', auto_now_add=True)
    fecha_modificacion = models.DateTimeField('Fecha de modificación', auto_now=True)

    creado_por = models.ForeignKey('usuarios.Perfil', on_delete=models.SET_DEFAULT)