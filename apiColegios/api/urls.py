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
    #Aqui es donde vamos a poder hacer el POST para agregar colegio pero no lo hagas aun , me olvide de hacerlo 
    path('colegios/', views.ColegiosList.as_view(), name='colegios_list'),
    # Esta va a ser la ruta para el login 
    path('colegio/', views.ColegioDetail.as_view(), name='colegio_detail'),

    path('estudiantes/', views.EstudiantesList.as_view(), name='estudiantes_list'),
    # Aqui es la ruta para ver todos los estudiantes , pero necesitas sacarel ID del colegio para que funcione
    path('estudiantes/<int:idColegio>/', views.EstudiantesListByColegio.as_view(), name='estudiantes_list_by_colegio'),
    # Aqui es la ruta para ver todo lo de un Estudiante y hacer PUT DELETE 
    path('estudiantes/<int:idColegio>/<int:idEstudiante>/', views.unEstudianteByColegio.as_view(), name='un_estudiante_by_colegio'),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)