from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    contraNoEncriptada = models.CharField(max_length=100)
    ubicacionCole = models.CharField(max_length=100)
    nombreCole = models.CharField(max_length=100)

class Estudiantes(models.Model):
    colegio = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="estudiantes")
    nombreEstudiante = models.CharField(max_length=100)
    apellidoEstudiante = models.CharField(max_length=100)
    fotoEstudiante = models.ImageField(upload_to='estudiantes')
    edadEstudiante = models.IntegerField()
    gradoEstudiante = models.IntegerField()

    def __str__(self):
        return self.nombreEstudiante

class Apoderado(models.Model):
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, related_name="apoderados")
    nombreApoderado = models.CharField(max_length=100)
    apellidoApoderado = models.CharField(max_length=100)
    celularEncargado = models.IntegerField()
    correoEncargado = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreApoderado

class Mensaje(models.Model):
    estudiante = models.ForeignKey(Estudiantes,on_delete=models.CASCADE, retaleted_name="mensajes")
    descripcionMensaje = models.CharField(max_length=100)
    fotoMensaje = models.ImageField(upload_to='mensajes')
    fechaMensaje = models.DateField(null=True)