# Generated by Django 5.1.3 on 2024-11-26 23:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitudEmpleo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12, unique=True, validators=[django.core.validators.RegexValidator(message='El RUT debe tener el formato 12345678-9', regex='^\\d{7,8}-[0-9kK]{1}$')], verbose_name='RUT')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido_paterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('apellido_materno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('telefono', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='El número debe tener el formato +56912345678', regex='^\\+569\\d{8}$')], verbose_name='Teléfono')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('direccion', models.CharField(max_length=100, verbose_name='Dirección')),
                ('cv', models.FileField(upload_to='cvs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Currículum Vitae')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
            ],
            options={
                'verbose_name': 'Solicitud de Empleo',
                'verbose_name_plural': 'Solicitudes de Empleo',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]