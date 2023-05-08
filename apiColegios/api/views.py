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

class ColegioDetail(APIView):
    def get(self, request, nombreColegio, contraseñaColegio):
        colegio = CustomUser.objects.get(nombreCole=nombreColegio, contraNoEncriptada=contraseñaColegio)
        data = CustomUserSerializer(colegio).data
        return Response(data)

class EstudiantesList(APIView):
    def get(self, request):
        estudiantes = Estudiantes.objects.all()
        data = EstudiantesSerializer(estudiantes, many=True).data
        return Response(data)

class EstudiantesListByColegio(APIView):
    def get (self, request, idColegio):
        colegio = CustomUser.objects.get(id=idColegio)
        estudiantes = Estudiantes.objects.filter(colegio=colegio)
        data = EstudiantesSerializer(estudiantes, many=True).data
        return Response(data)
    def post(self, request,idColegio):
        serializer = EstudiantesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer.fotoEstudiante = request.FILES.get('fotoEstudiante')
            return Response(serializer.data)
        return Response(serializer.errors)
    
class unEstudianteByColegio(APIView):
    def get(self, request, idColegio, idEstudiante):
        colegio = CustomUser.objects.get(id=idColegio)
        estudiante = Estudiantes.objects.get(colegio=colegio, id=idEstudiante)
        data = EstudiantesSerializer(estudiante).data
        return Response(data)
    def put(self, request, idColegio, idEstudiante):
        colegio = CustomUser.objects.get(id=idColegio)
        estudiante = Estudiantes.objects.get(colegio=colegio, id=idEstudiante)
        serializer = EstudiantesSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            estudiante.fotoEstudiante.delete()
            estudiante.nombreEstudiante = request.data.get('nombreEstudiante')
            estudiante.apellidoEstudiante = request.data.get('apellidoEstudiante')
            estudiante.fotoEstudiante = request.FILES.get('fotoEstudiante')
            estudiante.edadEstudiante = request.data.get('edadEstudiante')
            estudiante.gradoEstudiante = request.data.get('gradoEstudiante')
            estudiante.save()
            serializer_response = EstudiantesSerializer(estudiante)
            return Response(serializer_response.data)
        return Response(serializer.errors)
    def delete(self, request, idColegio, idEstudiante):
        colegio = CustomUser.objects.get(id=idColegio)
        estudiante = Estudiantes.objects.get(colegio=colegio, id=idEstudiante)
        estudiante.fotoEstudiante.delete
        estudiante.delete()
        return Response("Estudiante eliminado")
        
class ApoderadosList(APIView):
    def get(self, request):
        apoderados = Apoderado.objects.all()
        data = ApoderadoSerializer(apoderados, many=True).data
        return Response(data)

class ApoderaodsListByEstudiante(APIView):
    def get(self, request, idEstudiante):
        estudiante = Estudiantes.objects.get(id=idEstudiante)
        apoderados = Apoderado.objects.filter(estudiante=estudiante)
        data = ApoderadoSerializer(apoderados, many=True).data
        return Response(data)
    def post(self, request,idEstudiante):
        serializer = ApoderadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class unApoderadoByEstudiante(APIView):
    def get(self, request, idEstudiante, idApoderado):
        estudiante = Estudiantes.objects.get(id=idEstudiante)
        apoderado = Apoderado.objects.get(estudiante=estudiante, id=idApoderado)
        data = ApoderadoSerializer(apoderado).data
        return Response(data)
    def put(self, request, idEstudiante, idApoderado):
        estudiante = Estudiantes.objects.get(id=idEstudiante)
        apoderado = Apoderado.objects.get(estudiante=estudiante, id=idApoderado)
        serializer = ApoderadoSerializer(apoderado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer_response = ApoderadoSerializer(apoderado)
            return Response(serializer_response.data)
        return Response(serializer.errors)
    def delete(self, request, idEstudiante, idApoderado):
        estudiante = Estudiantes.objects.get(id=idEstudiante)
        apoderado = Apoderado.objects.get(estudiante=estudiante, id=idApoderado)
        apoderado.delete()
        return Response("Apoderado eliminado")

class MensajesList(APIView):
    def get(self, request):
        mensaje = Mensaje.objects.all()
        data = MensajeSerializer(mensaje, many=True).data
        return Response(data)
    
class MensajesListByEstudiante(APIView):
    def get(self, request, idEstudiante):
        estudiante = Estudiantes.objects.get(id=idEstudiante)
        mensajees = Mensaje.objects.filter(estudiante=estudiante)
        data = MensajeSerializer(mensajees, many=True).data
        return Response(data)
    def post(self, request, idEstudiante):
        serializer = MensajeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.fotoMensaje = request.FILES.get('fotoMensaje')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class unMensajeByEstudiante(APIView):
    def get(self, request, idEstudiante, idMensaeje):
        estudiante = Estudiantes.objects.get(id=idEstudiante)
        mensaje = Mensaje.objects.get(estudiante=estudiante, id=idMensaeje)
        data = MensajeSerializer(mensaje).data
        return Response(data)
    def put(self, request, idEstudiante, idMensaeje):
        estudiante = Estudiantes.objects.get(id=idEstudiante)
        mensaje = Mensaje.objects.get(estudiante=estudiante, id=idMensaeje)
        serializer = MensajeSerializer(mensaje, data=request.data)
        if serializer.is_valid():
            mensaje.fotoMensaje.delete()
            mensaje.fotoMensaje = request.FILES.get('fotoMensaje')
            mensaje.descripcionMensaje = request.data.get('descripcionMensaje')
            mensaje.fechaMensaje = request.data.get('fechaMensaje')
            mensaje.save()
            serializer_response = MensajeSerializer(mensaje)
            return Response(serializer_response.data)
        return Response(serializer.errors)
    def delete(self, request, idEstudiante, idMensaeje):
        estudiante = Estudiantes.objects.get(id=idEstudiante)
        mensaje = Mensaje.objects.get(estudiante=estudiante, id=idMensaeje)
        mensaje.fotoMensaje.delete
        mensaje.delete()
        return Response("Mensaje eliminado")