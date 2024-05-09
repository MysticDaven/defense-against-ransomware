from django.contrib import admin
from .models import model_identificar, model_conciencia, model_herramientas,RespuestasIdentificar, RespuestasConciencia, RespuestasHerramientas

# Register your models here.
admin.site.register(model_identificar)
admin.site.register(RespuestasIdentificar)
admin.site.register(model_conciencia)
admin.site.register(RespuestasConciencia)
# admin.site.register(model_herramientas)
admin.site.register(RespuestasHerramientas)