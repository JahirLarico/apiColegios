from django.contrib import admin
from .models import *
admin.site.register(CustomUser)
admin.site.register(Estudiantes)
admin.site.register(Apoderado)
admin.site.register(Mensaje)

# Register your models here.
