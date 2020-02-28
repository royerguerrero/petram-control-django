"""Admin Config Users"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Models 
from usuarios.models import Perfil

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name = 'Perfiles'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)