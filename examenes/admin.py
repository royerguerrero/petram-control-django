"""Config Admin de Examenes"""

# Django
from django.contrib import admin

# Models
from examenes.models import Examen, Pregunta, Respuesta

class RespuestaInline(admin.TabularInline):
    model = Respuesta

class PreguntaInline(admin.StackedInline):
    model = Pregunta

@admin.register(Examen)
class ExamenAdmin(admin.ModelAdmin):
    inlines = [
        PreguntaInline,
    ]

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    inlines = [
        RespuestaInline,
    ]