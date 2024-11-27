from django.db import models
from django.core.validators import RegexValidator, FileExtensionValidator

class SolicitudEmpleo(models.Model):
    # Validación para el campo de RUT
    rut = models.CharField(
        max_length=12, 
        unique=True, 
        validators=[
            RegexValidator(
                regex=r'^\d{7,8}-[0-9kK]{1}$',
                message='El RUT debe tener el formato 12345678-9'
            )
        ],
        verbose_name="RUT"
    )

    # Información personal
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido_paterno = models.CharField(max_length=50, verbose_name="Apellido Paterno")
    apellido_materno = models.CharField(max_length=50, verbose_name="Apellido Materno")

    # Información de contacto
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\+569\d{8}$',
                message='El número debe tener el formato +56912345678'
            )
        ],
        verbose_name="Teléfono"
    )

    # Fecha de nacimiento
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")

    # Dirección
    direccion = models.CharField(max_length=100, verbose_name="Dirección")

    # CV (archivo PDF)
    cv = models.FileField(
        upload_to='cvs/',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf'])
        ],
        verbose_name="Currículum Vitae"
    )

    # Timestamps
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Solicitud de Empleo"
        verbose_name_plural = "Solicitudes de Empleo"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} - {self.rut}"
