from django.db import models


class Convocatoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()  # Asegúrate de que este campo exista
    fecha_fin = models.DateField()  # Asegúrate de que este campo exista

    def __str__(self):
        return self.nombre


class Inscripcion(models.Model):
    convocatoria = models.ForeignKey(Convocatoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.convocatoria.nombre}"

