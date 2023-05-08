from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#Importar los setting y estatics para usarlos 
from django.conf import settings
from django.conf.urls.static import static
app_name = 'api'

# con la linea 22 vamos a poder cargar las imagenes estaticas 
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('colegios/', views.ColegiosList.as_view(), name='colegios_list'),
    path('colegio/<str:nombreColegio>/<str:contraseñaColegio>', views.ColegioDetail.as_view(), name='colegio_detail'),
    path('estudiantes/', views.EstudiantesList.as_view(), name='estudiantes_list'),
    path('estudiantes/<int:idColegio>/', views.EstudiantesListByColegio.as_view(), name='estudiantes_list_by_colegio'),
    path('estudiantes/<int:idColegio>/<int:idEstudiante>/', views.unEstudianteByColegio.as_view(), name='un_estudiante_by_colegio'),
    path('apoderados/', views.ApoderadosList.as_view(), name='apoderados_list'),
    path('apoderados/<int:idEstudiante>/', views.ApoderaodsListByEstudiante.as_view(), name='apoderados_list_by_colegio'),
    path('apoderados/<int:idEstudiante>/<int:idApoderado>/', views.unApoderadoByEstudiante.as_view(), name='un_apoderado_by_colegio'),
    path('mensajes/', views.MensajesList.as_view(), name='mensajes_list'),
    #Aprobados los de abajo
    path('mensajes/<int:idEstudiante>/', views.MensajesListByEstudiante.as_view(), name='mensajes_list_by_colegio'),
    path('mensajes/<int:idEstudiante>/<int:idMensaeje>/', views.unMensajeByEstudiante.as_view(), name='un_mensaje_by_colegio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)