"""Config Admin de Clases"""

# Django
from django.contrib import admin

# Models
from clases.models import Clase, DetalleClase, Vehiculo

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    pass

