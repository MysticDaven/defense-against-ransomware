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
        fields = ['username', 'first_name', 'last_name', 'email']   

class model_identificar(models.Model):
    tipo_empresa = models.IntegerField(choices=tipos, verbose_name='¿Cuál es el tipo de tu empresa?')
    rol = models.IntegerField(choices=tipos, verbose_name="¿Cuál es su puesto/rol en su organización?")
    incidente = models.IntegerField(choices=tipos, verbose_name="En el caso de un incidente de segurdad informática (ataque por viruso informático u otras formas) usted: ")

class model_conciencia(models.Model):
    ataque_propio = models.IntegerField(choices=decision, verbose_name="¿Alguna vez su organización ha recibido un ciberataque?")
    ataque_tercero = models.IntegerField(choices=decision_2, verbose_name="¿Conoces alguna organización similar a la tuya o con la que tengas negocios que haya sido afectada (vulnerada) en un ciberataque?")
    correo = models.IntegerField(choices=importancia, verbose_name="Correo electrónico")
    datos = models.IntegerField(choices=importancia, verbose_name="Datos personales")
    financiero = models.IntegerField(choices=importancia, verbose_name="Información financiera (Cuentas por pagar)")
    ventas = models.IntegerField(choices=importancia, verbose_name="Información de Ventas (Cuentas por cobrar)")
    proyectos = models.IntegerField(choices=importancia, verbose_name="Generación de proyectos")
    respaldos = models.IntegerField(choices=importancia, verbose_name="Respaldos")
    servidores = models.IntegerField(choices=importancia, verbose_name="Servidores")
    servicios = models.IntegerField(choices=importancia, verbose_name="Servicios de Red")
    div_proyecto = models.IntegerField(choices=importancia, verbose_name="Divulgación de proyectos o cuentas clave con compañías rivales")
    div_info_sens = models.IntegerField(choices=importancia, verbose_name="Divulgación de información sensible de la compañía (Recetas/Patentes)")
    div_info_cliente = models.IntegerField(choices=importancia, verbose_name="Divulgación de información de los clientes/usuarios (Datos personales)")
    div_info_fin = models.IntegerField(choices=importancia, verbose_name="Divulgación de la información financiera de la organización")
    div_db = models.IntegerField(choices=importancia, verbose_name="Divulgación de Bases de Datos internas de la empresa de diferente índole")

class model_herramientas(models.Model):
    antivirus = models.IntegerField(choices=importancia, verbose_name="Antivirus/EDR (Detección y Respuesta en Equipo de Cómputo)")
    dlp = models.IntegerField(choices=importancia, verbose_name="Software DLP (Data Lost Prevention; Prevención de la Pérdida de la Información)")
    protec_correo = models.IntegerField(choices=importancia, verbose_name="Protección de correo electrónico")
    vpn = models.IntegerField(choices=importancia, verbose_name="VPN (Red Privada Virtual) o ZTNA (Zero Trust Network Access; Acceso seguro a la red)")
    xdr = models.IntegerField(choices=importancia, verbose_name="XDR (Detección y Respuesta Extendidos Híbrida, Pública o Privada)")
    firewall = models.IntegerField(choices=importancia, verbose_name="Firewall Nueva Generación (Protección de Red en el perímetro)")
    waf = models.IntegerField(choices=importancia, verbose_name="WAF (Firewall en la Nube)")
    iso = models.IntegerField(choices=importancia, verbose_name="ISO 27001 (Metodología propuesta por la ISO)")
    zero_trust = models.IntegerField(choices=importancia, verbose_name="Zero Trust (Estándar de confianza 0: Roles y niveles de acceso a la información)")
    gdpr = models.IntegerField(choices=importancia, verbose_name="GDPR (Estándar de la unión Europea para la Protección de la Información en General)")
    nist = models.IntegerField(choices=importancia, verbose_name="NIST (Metodología de Seguridad de Norte América)")
    siem = models.IntegerField(choices=importancia, verbose_name="SIEM (Sistema de monitoreo de alertas informáticas)")
    soar = models.IntegerField(choices=importancia, verbose_name="SOAR (Centro de Orquestación y Automatización de Respuesta a Incidentes)")
    soc = models.IntegerField(choices=importancia, verbose_name="SOC (Centro de Operaciones para la Seguridad de la Información)")
    sdsdp = models.IntegerField(choices=importancia, verbose_name="SGSDP (Sistema de Gestión de Datos Personales del INAI México)")
    buenas_prac = models.IntegerField(choices=buenas_practicas, verbose_name="Tomando en cuenta las preguntas anteriores considera que ha aplicado el uso de las buenas prácticas de ciberseguridad dentro de sus organización, indique a continuación las buenas práctas que ha aplicado o si es que no las ha aplicado")
    preparada = models.IntegerField(choices=decision_3, verbose_name="Tomando en cuenta todas las soluciones y metodologías que anteriormente se mencionar, ¿Considera que su organización está prepatada para afronta un ataque de Ransomware?")

    
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
