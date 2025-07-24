from django.db import models

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    ciclo = models.CharField(max_length=10)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre