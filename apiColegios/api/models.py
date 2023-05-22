from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    contraNoEncriptada = models.CharField(max_length=100)
    ubicacionCole = models.CharField(max_length=100 , null=True)
    nombreDueno = models.CharField(max_length=100)
    apellidoDueno = models.CharField(max_length=100)
    nombreCole = models.CharField(max_length=100)

class Estudiantes(models.Model):
    colegio = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="estudiantes")
    nombreEstudiante = models.CharField(max_length=100)
    apellidoEstudiante = models.CharField(max_length=100)
    fotoEstudiante = models.ImageField(upload_to='estudiantes', null=True, blank=True)
    edadEstudiante = models.IntegerField()
    nombreApoderado = models.CharField(max_length=100)
    apellidoApoderado = models.CharField(max_length=100)
    celularApoderado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreEstudiante
