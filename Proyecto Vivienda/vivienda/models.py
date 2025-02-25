from django.db import models

class Hogar(models.Model):
    jefe_hogar = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    anos_residencia = models.IntegerField()

    def __str__(self):
        return self.jefe_hogar

class Miembro(models.Model):
    hogar = models.ForeignKey(Hogar, related_name='miembros_hogar', on_delete=models.CASCADE)
    nombre = models.CharField("Nombre del Miembro", max_length=100)
    es_victima = models.BooleanField("Es víctima de conflicto", default=False)
    es_discapacitado = models.BooleanField("Tiene discapacidad", default=False)
    edad = models.IntegerField("Edad")

    def __str__(self):
        return f"{self.nombre} ({self.hogar.jefe_hogar})"
