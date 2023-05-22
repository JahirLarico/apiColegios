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
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
class ColegioDetail(APIView):
    def get(self, request):
        usuario = request.GET.get('usuario')
        clave = request.GET.get('clave')
        colegio = CustomUser.objects.get(nombreCole=usuario, contraNoEncriptada=clave)
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
            #Linea que era para eliminar la imagen
            #estudiante.fotoEstudiante.delete()
            estudiante.nombreEstudiante = request.data.get('nombreEstudiante')
            estudiante.apellidoEstudiante = request.data.get('apellidoEstudiante')
            #estudiante.fotoEstudiante = request.FILES.get('fotoEstudiante')
            estudiante.edadEstudiante = request.data.get('edadEstudiante')
            estudiante.nombreApoderado = request.data.get('nombreApoderado')
            estudiante.apellidoApoderado = request.data.get('apellidoApoderado')
            estudiante.celularApoderado = request.data.get('celularApoderado')
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
        
