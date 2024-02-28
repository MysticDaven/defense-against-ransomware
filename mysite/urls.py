from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('def_rans.urls')) #Agregamos todas las urls de nuestra aplicacion
]
