from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your views here.

class Index(APIView):
    def get(self, request):
        return Response("Hola Mundo")

class ColegiosList(APIView):
    def get(self, request):
        Colegios = CustomUser.objects.all()
        data = CustomUserSerializer(Colegios, many=True).data
        return Response(data)

class EstudiantesList(APIView):
    def get(self, request):
        estudiantes = Estudiantes.objects.all()
        data = EstudiantesSerializer(estudiantes, many=True).data
        return Response(data)

class EstudiantesListByColegio(APIView):
    def get (self, request, nombreColegio):
        colegio = CustomUser.objects.get(nombreCole=nombreColegio)
        estudiantes = Estudiantes.objects.filter(colegio=colegio)
        data = EstudiantesSerializer(estudiantes, many=True).data
        return Response(data)
    def post(self, request,nombreColegio):
        serializer = EstudiantesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            estudiante = serializer.instance
            estudiante.fotoEstudiante = request.FILES.get('fotoEstudiante')
            estudiante.save()
            serializer_response = EstudiantesSerializer(estudiante)
            return Response(serializer_response.data)
        return Response(serializer.errors)
    
class unEstudianteByColegio(APIView):
    def get(self, request, nombreColegio, nombreEstudiante):
        colegio = CustomUser.objects.get(nombreCole=nombreColegio)
        estudiante = Estudiantes.objects.get(colegio=colegio, nombreEstudiante=nombreEstudiante)
        data = EstudiantesSerializer(estudiante).data
        return Response(data)
    def put(self, request, nombreColegio, nombreEstudiante):
        colegio = CustomUser.objects.get(nombreCole=nombreColegio)
        estudiante = Estudiantes.objects.get(colegio=colegio, nombreEstudiante=nombreEstudiante)
        serializer = EstudiantesSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            estudiante.fotoEstudiante.delete()
            estudiante.fotoEstudiante = request.FILES.get('fotoEstudiante')
            estudiante.save()
            serializer_response = EstudiantesSerializer(estudiante)
            return Response(serializer_response.data)
        return Response(serializer.errors)
    def delete(self, request, nombreColegio, nombreEstudiante):
        colegio = CustomUser.objects.get(nombreCole=nombreColegio)
        estudiante = Estudiantes.objects.get(colegio=colegio, nombreEstudiante=nombreEstudiante)
        estudiante.fotoEstudiante.delete
        estudiante.delete()
        return Response("Estudiante eliminado")
        
class ApoderadosList(APIView):
    def get(self, request):
        apoderados = Apoderado.objects.all()
        data = ApoderadoSerializer(apoderados, many=True).data
        return Response(data)

class ApoderaodsListByEstudiante(APIView):
    def get(self, request, nombreEstudiante):
        estudiante = Estudiantes.objects.get(nombreEstudiante=nombreEstudiante)
        apoderados = Apoderado.objects.filter(estudiante=estudiante)
        data = ApoderadoSerializer(apoderados, many=True).data
        return Response(data)
    def post(self, request,nombreEstudiante):
        serializer = ApoderadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            apoderado = serializer.instance
            apoderado.save()
            serializer_response = ApoderadoSerializer(apoderado)
            return Response(serializer_response.data)
        return Response(serializer.errors)

class unApoderadoByEstudiante(APIView):
    def get(self, request, nombreEstudiante, nombreApoderado):
        estudiante = Estudiantes.objects.get(nombreEstudiante=nombreEstudiante)
        apoderado = Apoderado.objects.get(estudiante=estudiante, nombreApoderado=nombreApoderado)
        data = ApoderadoSerializer(apoderado).data
        return Response(data)
    def put(self, request, nombreEstudiante, nombreApoderado):
        estudiante = Estudiantes.objects.get(nombreEstudiante=nombreEstudiante)
        apoderado = Apoderado.objects.get(estudiante=estudiante, nombreApoderado=nombreApoderado)
        serializer = ApoderadoSerializer(apoderado, data=request.data)
        if serializer.is_valid():
            apoderado.save()
            serializer_response = ApoderadoSerializer(apoderado)
            return Response(serializer_response.data)
        return Response(serializer.errors)
    def delete(self, request, nombreEstudiante, nombreApoderado):
        estudiante = Estudiantes.objects.get(nombreEstudiante=nombreEstudiante)
        apoderado = Apoderado.objects.get(estudiante=estudiante, nombreApoderado=nombreApoderado)
        apoderado.delete()
        return Response("Apoderado eliminado")

class MensajesList(APIView):
    def get(self, request):
        mensaje = Mensaje.objects.all()
        data = MensajeSerializer(mensaje, many=True).data
        return Response(data)
    
class MensajesListByEstudiante(APIView):
    def get(self, request, nombreEstudiante):
        estudiante = Estudiantes.objects.get(nombreEstudiante=nombreEstudiante)
        mensajees = Mensaje.objects.filter(estudiante=estudiante)
        data = MensajeSerializer(mensajees, many=True).data
        return Response(data)
    def post(self, request,nombreEstudiante):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            mensaje = serializer.instance
            mensaje.fotoMensaje = request.FILES.get('fotoMensaje')
            mensaje.save()
            serializer_response = MensajeSerializer(mensaje)
            return Response(serializer_response.data)
        return Response(serializer.errors)

class unMensajeByEstudiante(APIView):
    def get(self, request, nombreEstudiante, idMensaeje):
        estudiante = Estudiantes.objects.get(nombreEstudiante=nombreEstudiante)
        mensaje = Mensaje.objects.get(estudiante=estudiante, id=idMensaeje)
        data = MensajeSerializer(mensaje).data
        return Response(data)
    def put (self, request, nombreEstudiante,idMensaeje):
        estudiante = Estudiantes.objects.get(nombreEstudiante=nombreEstudiante)
        mensaje = Mensaje.objects.get(estudiante=estudiante, id=idMensaeje)
        serializer = MensajeSerializer(mensaje, data=request.data)
        if serializer.is_valid():
            mensaje.fotoMensaje.delete()
            mensaje.fotoMensaje = request.FILES.get('fotoMensaje')
            mensaje.save()
            serializer_response = MensajeSerializer(mensaje)
            return Response(serializer_response.data)
        return Response(serializer.errors)
    def delete(self, request, nombreEstudiante, idMensaeje):
        estudiante = Estudiantes.objects.get(nombreEstudiante=nombreEstudiante)
        mensaje = Mensaje.objects.get(estudiante=estudiante, id=idMensaeje)
        mensaje.fotoMensaje.delete
        mensaje.delete()
        return Response("Mensaje eliminado")