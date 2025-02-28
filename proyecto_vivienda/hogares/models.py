from django.db import models

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha = models.DateField()

class Convocatoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre


class Postulacion(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    medio_transporte = models.CharField(max_length=20, choices=[
        ("bus", "Bus"), ("moto", "Moto"), ("bicicleta", "Bicicleta")
    ])
    predio_suelo = models.CharField(max_length=10, choices=[("rural", "Rural"), ("urbano", "Urbano")])
    descripcion_llegada = models.TextField()

    def __str__(self):
        return self.nombre
