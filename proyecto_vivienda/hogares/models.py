from django.db import models

class Convocatoria(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return self.nombre

class Postulacion(models.Model):
    numero_documento = models.IntegerField()
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=255, default="correo@example.com")
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)
    estado_civil = models.CharField(max_length=20, choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Unión Libre', 'Unión Libre')])
    tipo_vinculacion = models.CharField(max_length=20, choices=[('Empleado', 'Empleado'), ('Independiente', 'Independiente'), ('Otro', 'Otro')])
    ingresos = models.IntegerField(default=0)
    egresos = models.IntegerField(default=0)
    tipo_vivienda = models.CharField(max_length=20, choices=[('Propia', 'Propia'), ('Arrendada', 'Arrendada'), ('Familiar', 'Familiar')])
    numero_habitantes = models.IntegerField()
    descripcion_llegada = models.TextField(blank=True, null=True)
    medio_transporte = models.CharField(max_length=50, blank=True, null=True)
    predio_suelo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre
