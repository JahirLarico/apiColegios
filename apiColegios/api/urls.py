from django.urls import path
from . import views

#Importar los setting y estatics para usarlos 
from django.conf import settings
from django.conf.urls.static import static
app_name = 'api'

# con la linea 12 vamos a poder cargar las imagenes estaticas 
urlpatterns = [ 
    path('colegios/', views.ColegiosList.as_view(), name='colegios_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)