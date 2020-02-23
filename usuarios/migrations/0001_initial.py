# Generated by Django 3.0.3 on 2020-02-23 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('tipo_de_id', models.CharField(choices=[('T.I', 'Tarjeta de identidad'), ('C.C', 'Cedula de ciudadania'), ('C.E', 'Cedula de Extrangeria')], max_length=3, verbose_name='Tipo de identificación')),
                ('numero_id', models.CharField(max_length=20, verbose_name='Número de Identificación')),
                ('curso', models.CharField(blank=True, choices=[('A2', 'Moto A2'), ('B1', 'Carro B1'), ('C1', 'Carro C1')], max_length=2, null=True)),
                ('rol', models.PositiveSmallIntegerField(choices=[(1, 'Estudiante'), (2, 'Profesor'), (3, 'Secretaria')])),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]