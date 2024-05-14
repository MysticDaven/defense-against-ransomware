# Generated by Django 4.2.6 on 2024-05-01 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='model_conciencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ataque_propio', models.IntegerField(choices=[[0, 'Sí'], [1, 'No']], verbose_name='¿Alguna vez su organización ha recibido un ciberataque?')),
                ('ataque_tercero', models.IntegerField(choices=[[0, 'Sí conozco'], [1, 'No conozco'], [2, 'Desconozco']], verbose_name='¿Conoces alguna organización similar a la tuya o con la que tengas negocios que haya sido afectada (vulnerada) en un ciberataque?')),
                ('correo', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Correo electrónico')),
                ('datos', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Datos personales')),
                ('financiero', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Información financiera (Cuentas por pagar)')),
                ('ventas', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Información de Ventas (Cuentas por cobrar)')),
                ('proyectos', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Generación de proyectos')),
                ('respaldos', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Respaldos')),
                ('servidores', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Servidores')),
                ('servicios', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Servicios de Red')),
                ('div_proyecto', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Divulgación de proyectos o cuentas clave con compañías rivales')),
                ('div_info_sens', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Divulgación de información sensible de la compañía (Recetas/Patentes)')),
                ('div_info_cliente', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Divulgación de información de los clientes/usuarios (Datos personales)')),
                ('div_info_fin', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Divulgación de la información financiera de la organización')),
                ('div_db', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Divulgación de Bases de Datos internas de la empresa de diferente índole')),
            ],
        ),
        migrations.CreateModel(
            name='model_herramientas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antivirus', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Antivirus/EDR (Detección y Respuesta en Equipo de Cómputo)')),
                ('dlp', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Software DLP (Data Lost Prevention; Prevención de la Pérdida de la Información)')),
                ('protec_correo', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Protección de correo electrónico')),
                ('vpn', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='VPN (Red Privada Virtual) o ZTNA (Zero Trust Network Access; Acceso seguro a la red)')),
                ('xdr', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='XDR (Detección y Respuesta Extendidos Híbrida, Pública o Privada)')),
                ('firewall', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Firewall Nueva Generación (Protección de Red en el perímetro)')),
                ('waf', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='WAF (Firewall en la Nube)')),
                ('iso', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='ISO 27001 (Metodología propuesta por la ISO)')),
                ('zero_trust', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='Zero Trust (Estándar de confianza 0: Roles y niveles de acceso a la información)')),
                ('gdpr', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='GDPR (Estándar de la unión Europea para la Protección de la Información en General)')),
                ('nist', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='NIST (Metodología de Seguridad de Norte América)')),
                ('siem', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='SIEM (Sistema de monitoreo de alertas informáticas)')),
                ('soar', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='SOAR (Centro de Orquestación y Automatización de Respuesta a Incidentes)')),
                ('soc', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='SOC (Centro de Operaciones para la Seguridad de la Información)')),
                ('sdsdp', models.IntegerField(choices=[[0, 'Muy Importante'], [1, 'Importante'], [2, 'Neutral'], [3, 'Poco Importante'], [4, 'Nada Importante'], [5, 'Lo desconozco']], verbose_name='SGSDP (Sistema de Gestión de Datos Personales del INAI México)')),
                ('buenas_prac', models.IntegerField(choices=[[0, 'Buenas prácticas de prevención con el uso de herramientas de protección (antivirus, firewall, etc.)'], [1, 'Buenas prácticas de prevención con el uso de metodologías/estándares (iso 27001, gdpr, etc.)'], [2, 'Buenas prácticas de contención con el uso de sistemas de seguridad (soc, siem, etc.)'], [3, 'No las he aplicado']], verbose_name='Tomando en cuenta las preguntas anteriores considera que ha aplicado el uso de las buenas prácticas de ciberseguridad dentro de sus organización, indique a continuación las buenas práctas que ha aplicado o si es que no las ha aplicado')),
                ('preparada', models.IntegerField(choices=[[0, 'Sí'], [1, 'No'], [2, 'Lo desconozco']], verbose_name='Tomando en cuenta todas las soluciones y metodologías que anteriormente se mencionar, ¿Considera que su organización está prepatada para afronta un ataque de Ransomware?')),
            ],
        ),
        migrations.CreateModel(
            name='model_identificar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_empresa', models.IntegerField(choices=[[0, 'Empresa Local (PyME)'], [1, 'Empresa Nacional (Privada o Pública)'], [2, 'Empresa Multinacional (Con Servicios Fuera de México)'], [3, 'Empresa Transnacional o Internacional'], [4, 'Otro']], verbose_name='¿Cuál es el tipo de tu empresa?')),
                ('rol', models.IntegerField(choices=[[0, 'Empresa Local (PyME)'], [1, 'Empresa Nacional (Privada o Pública)'], [2, 'Empresa Multinacional (Con Servicios Fuera de México)'], [3, 'Empresa Transnacional o Internacional'], [4, 'Otro']], verbose_name='¿Cuál es su puesto/rol en su organización?')),
                ('incidente', models.IntegerField(choices=[[0, 'Empresa Local (PyME)'], [1, 'Empresa Nacional (Privada o Pública)'], [2, 'Empresa Multinacional (Con Servicios Fuera de México)'], [3, 'Empresa Transnacional o Internacional'], [4, 'Otro']], verbose_name='En el caso de un incidente de segurdad informática (ataque por viruso informático u otras formas) usted: ')),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=300, verbose_name='Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('respuesta', models.PositiveIntegerField(blank=True, null=True, verbose_name='Respuestas')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='def_rans.preguntas', verbose_name='Pregunta')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]