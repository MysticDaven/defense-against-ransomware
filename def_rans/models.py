from django.db import models
from django import forms
from django.contrib.auth.models import User

#Choices
tipos = [
    [0, 'Empresa Local (PyME)'],
    [1, 'Empresa Nacional (Privada o Pública)'],
    [2, 'Empresa Multinacional (Con Servicios Fuera de México)'],
    [3, 'Empresa Transnacional o Internacional'],
    [4, 'Otro']
]

roles = [
    [0, 'Administrativo'],
    [1, 'Directivo'],
    [2, 'Servicio'],
    [3, 'Sistemas/Informática/TICs'],
    [4, 'Soporte'],
    [5, 'Otro']
]

incidentes = [
    [0, 'Toma las decisiones sobre como actuar'],
    [1, 'Lo reporta ante un directivo para obtener el plan de acción'],
    [2, 'Depende de un tercero que le brinda servicios de seguridad para actuar ante el incidente'],
    [3, 'Otro']
]

decision = [
    [0, 'Sí'],
    [1, 'No']
]

decision_2 = [
    [0, 'Sí conozco'],
    [1, 'No conozco'],
    [2, 'Desconozco']
]

decision_3 = [
    [0, 'Sí'],
    [1, 'No'],
    [2, 'Lo desconozco']
]

importancia = [
    [0, 'Muy Importante'],
    [1, 'Importante'],
    [2, 'Neutral'],
    [3, 'Poco Importante'],
    [4, 'Nada Importante'],
    [5, 'Lo desconozco']
]

buenas_practicas = [
    [0, 'Buenas prácticas de prevención con el uso de herramientas de protección (antivirus, firewall, etc.)'],
    [1, 'Buenas prácticas de prevención con el uso de metodologías/estándares (iso 27001, gdpr, etc.)'], 
    [2, 'Buenas prácticas de contención con el uso de sistemas de seguridad (soc, siem, etc.)'],
    [3, 'No las he aplicado']
]
# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=200)

class edit_user(forms.ModelForm):
    class Meta:
        model = User
<<<<<<< Updated upstream
        fields = ['username', 'first_name', 'last_name', 'email']   

class form_identificar(forms.Form):
    tipo_empresa = forms.ChoiceField(choices=tipos)
    rol = forms.ChoiceField(choices=roles)
    indicente = forms.ChoiceField(choices=incidentes)

class form_conciencia(forms.Form):
    ataque_propio = forms.ChoiceField(choices=decision)
    ataque_tercero = forms.ChoiceField(choices=decision_2)
    correo = forms.ChoiceField(choices=importancia)
    datos = forms.ChoiceField(choices=importancia)
    financiero = forms.ChoiceField(choices=importancia)
    ventas = forms.ChoiceField(choices=importancia)
    proyectos = forms.ChoiceField(choices=importancia)
    respaldos = forms.ChoiceField(choices=importancia)
    servidores = forms.ChoiceField(choices=importancia)
    servicios = forms.ChoiceField(choices=importancia)
    div_proyecto = forms.ChoiceField(choices=importancia)
    div_info_sens = forms.ChoiceField(choices=importancia)
    div_info_cliente = forms.ChoiceField(choices=importancia)
    div_info_fin = forms.ChoiceField(choices=importancia)
    div_db = forms.ChoiceField(choices=importancia)

class form_herramientas(forms.Form):
    antivirus = forms.ChoiceField(choices=importancia)
    dlp = forms.ChoiceField(choices=importancia)
    protec_correo = forms.ChoiceField(choices=importancia)
    vpn = forms.ChoiceField(choices=importancia)
    xdr = forms.ChoiceField(choices=importancia)
    firewall = forms.ChoiceField(choices=importancia)
    waf = forms.ChoiceField(choices=importancia)
    iso = forms.ChoiceField(choices=importancia)
    zero_trust = forms.ChoiceField(choices=importancia)
    gdpr = forms.ChoiceField(choices=importancia)
    nist = forms.ChoiceField(choices=importancia)
    siem = forms.ChoiceField(choices=importancia)
    sdar = forms.ChoiceField(choices=importancia)
    soc = forms.ChoiceField(choices=importancia)
    sdsdp = forms.ChoiceField(choices=importancia)
    buenas_prac = forms.ChoiceField(choices=buenas_practicas)
    preparada = forms.ChoiceField(choices=decision_3)
    




=======
        fields = ['username', 'first_name', 'last_name', 'email']


class Preguntas(models.Model):
    id = models.AutoField(primary_key=True)
    pregunta = models.CharField(verbose_name="Pregunta", max_length=300)

    def __str__(self):
        return str(self.id) + ' - ' + self.pregunta
    
class Respuestas(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    respuesta = models.PositiveIntegerField(verbose_name="Respuestas", null=True, blank=True)
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE, verbose_name="Pregunta")
>>>>>>> Stashed changes
