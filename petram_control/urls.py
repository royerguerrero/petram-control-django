"""Petram Control URL Configuration"""
# Django
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# Local
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usuarios_views.index, name='index'),
    path('recuperar-password/<int:usuario_id>', usuarios_views.forget_password, name='forget_password')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
