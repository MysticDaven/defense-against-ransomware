from django.contrib import admin
from .models import model_identificar, model_conciencia, model_herramientas

# Register your models here.
admin.site.register(model_identificar)
admin.site.register(model_conciencia)
admin.site.register(model_herramientas)