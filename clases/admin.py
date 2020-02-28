"""Config Admin de Clases"""

# Django
from django.contrib import admin

# Models
from clases.models import Clase, DetalleClase, Vehiculo

class DetClaseInline(admin.StackedInline):
    model = DetalleClase

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    inlines = [DetClaseInline]

