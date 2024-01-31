from django.urls import path
from . import views

urlpatterns = [
    #Blog
    path('', views.index , name='index'),
    path('estilos', views.estilos, name='estilos'),
    path('AntivirusG', views.AntivirusG, name='AntivirusG'),
    path('Plantilla', views.plantilla, name='plantilla'),
    path('Menu', views.menuPrueba, name='menuPrueba'),

    #Cuenta
    path('cuenta/acceder', views.acceder , name='acceder'),
    path('cuenta/registro', views.Registro, name='registro'),
    path('cuenta/salir', views.salir, name='salir'),
    path('cuenta/formulario', views.formulario, name='formulario'),
    path('cuenta/respuestas', views.respuestas, name='respuestas'),
]