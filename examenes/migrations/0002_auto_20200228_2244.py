# Generated by Django 3.0.3 on 2020-02-28 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='examen',
            options={'verbose_name_plural': 'Examenes'},
        ),
        migrations.AlterField(
            model_name='examen',
            name='imagen',
            field=models.ImageField(upload_to='examenes/pictures/examenes'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='imagen',
            field=models.ImageField(upload_to='examenes/pictures/preguntas'),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='imagen',
            field=models.ImageField(upload_to='examenes/pictures/respuestas'),
        ),
    ]
