"""Petram Control URL Configuration"""
# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Local
from usuarios import views as usuarios_views
from clases import views as clases_views

urlpatterns = [
    # Django paths
    path('admin/', admin.site.urls),

    # Usuarios paths
    path('', usuarios_views.login_view, name='login'),
    path('logout', usuarios_views.logout_view, name='logout'),
    path('recuperar-password/<int:usuario_id>', usuarios_views.forget_password, name='forget_password'),
    path('dashboard', usuarios_views.dashboard, name='dashboard'),

    # Clases paths
    path('dashboard/horario', clases_views.horario, name='horario')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
