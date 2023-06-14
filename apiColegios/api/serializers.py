from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User

class EstudiantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiantes
        fields = ['id','colegio','nombreEstudiante','apellidoEstudiante','fotoEstudiante','edadEstudiante','nombreApoderado','apellidoApoderado','celularApoderado']

class CustomUserSerializer(serializers.ModelSerializer):
    estudiantes = EstudiantesSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','username','contraNoEncriptada','ubicacionCole','nombreCole','nombreDueno','apellidoDueno','confirmacion','estudiantes']