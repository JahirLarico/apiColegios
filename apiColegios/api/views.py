from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your views here.

class ColegiosList(APIView):
    def get(self, request):
        Colegios = CustomUser.objects.all()
        data = CustomUserSerializer(Colegios, many=True).data
        return Response(data)