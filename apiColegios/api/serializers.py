from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User

class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['id','estudiante','descripcionMensaje','fotoMensaje','fechaMensaje']

class ApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoderado
        fields = ['id','estudiante','nombreApoderado','apellidoApoderado','celularEncargado','correoEncargado']

class EstudiantesSerializer(serializers.ModelSerializer):
    mensajes = MensajeSerializer(many=True, read_only=True)
    apoderados = ApoderadoSerializer(many=True, read_only=True)
    class Meta:
        model = Estudiantes
        fields = ['id','colegio','nombreEstudiante','apellidoEstudiante','fotoEstudiante','edadEstudiante','gradoEstudiante','apoderados','mensajes']

class CustomUserSerializer(serializers.ModelSerializer):
    estudiantes = EstudiantesSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','contraNoEncriptada','ubicacionCole','nombreCole','estudiantes']