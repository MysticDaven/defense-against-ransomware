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
    rol = models.IntegerField(choices=roles, verbose_name="¿Cuál es su puesto/rol en su organización?")
    incidente = models.IntegerField(choices=incidentes, verbose_name="En el caso de un incidente de segurdad informática (ataque por viruso informático u otras formas) usted: ")

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
    sgsdp = models.IntegerField(choices=importancia, verbose_name="SGSDP (Sistema de Gestión de Datos Personales del INAI México)")
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

class RespuestasIdentificar(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    respuesta = models.TextField(verbose_name="Respuesta", null=True, blank=True)
    pregunta = models.TextField(verbose_name="Pregunta", blank=True, null=True)

class RespuestasConciencia(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    respuesta = models.TextField(verbose_name="Respuesta", null=True, blank=True)
    pregunta = models.TextField(verbose_name="Pregunta", blank=True, null=True)

class RespuestasHerramientas(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    respuesta = models.TextField(verbose_name="Respuesta", null=True, blank=True)
    pregunta = models.TextField(verbose_name="Pregunta", null=True, blank=True)    

class ChecklistDLP(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario") 
    analisis = models.BooleanField(
        default=False,
        verbose_name="Hacer un análisis organizacional para identificar las áreas de mayor criticidad para la continuidad operativa, validar la importancia de la información de cada departamento para asi poder identificar los elementos críticos para respaldar."
    )   
    revision = models.BooleanField(
        default=False,
        verbose_name="Revisar continuamente el correcto funcionamiento de los respaldos ya que por una omisión en la configuración en una regla o porque se haya comprometido por un atacante pueden cambiar la frecuencia con la que se realizan los respaldos lo cual después de un tiempo considerable reduciría considerablemente la utilidad de retomar la operación perdiendo la menor información posible."
    )
    copias = models.BooleanField(
        default=False,
        verbose_name="Hacer copias por duplicado o triplicado de los respaldos de la información para garantizar estándares como los que indica la norma ISO 27001 para la alta disponibilidad de la información, para en caso de que alguno se vea comprometido haya más de una opción para la recuperación."
    ) 
    acceso = models.BooleanField(
        default=False,
        verbose_name="Limitar el acceso a los respaldos para evitar filtraciones o manipulaciones no autorizadas."
    )    

class ChecklistAntivirus(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")    
    analisis = models.BooleanField(
        default=False,
        verbose_name="Ejecutar un análisis en busca de Ransomware al recibir un correo de algún correo no registrado o desconocido y sobre todo cuando incluyen archivos adjuntos prestando especial atención a los archivos compartidos."
    )
    busqueda = models.BooleanField(
        default=False, 
        verbose_name="No excluir ninguna carpeta o archivo del análisis para la búsqueda de Ransomware ya que al omitir directorios/archivos se dejan puntos donde el Ransomware puede alojarse y explotar."
    )
    sandbox = models.BooleanField(
        default=False,
        verbose_name='Hacer uso de "Sandbox" para analizar dispositivos USB en busca de Ransomware, para prevenir el "RasS (Ransomware as a Service)" (Ransomware as a Service) o ataques por omisión (accidente).'
    )
    revision = models.BooleanField(
        default=False,
        verbose_name='Revisar periódicamente los resultados de las búsquedas de Ransomware para identificar situaciones de riesgos y corregirlos mediante el proceso de una auditoría interna.'
    )
    permisos = models.BooleanField(
        default=False,
        verbose_name='Desactivar los permisos de auto gestión de usuarios comunes para evitar brechas de seguridad (aplicación de Zero Trust).'
    )
    gestor = models.BooleanField(
        default=False,
        verbose_name="Usar software gestor de contraseñas."
    )
    usb = models.BooleanField(
        default=False,
        verbose_name="Activar el análisis automático al insertar una USB en la computadora."
    )
    entrenamiento = models.BooleanField(
        default=False,
        verbose_name="Entrenamiento regular al personal sobre la amenaza que representa el Ransomware y como identificar un Ransomware para así poder levantar el ticket correspondiente."
    )

class ChecklistFirewall(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario") 
    vlans = models.BooleanField(
        default=False,
        verbose_name='Segmentar la red (VLANS) para contener un posible ataque y contener en la medida de lo posible la afectación.'
    )      
    dmz = models.BooleanField(
        default=False,
        verbose_name='Tener una zona desmilitarizada (DMZ) para separar los servidores en la Red y enviar el tráfico encubierto hacía otro segmento de red cómo la LAN.'
    )  
    ips = models.BooleanField(
        default=False,
        verbose_name='Hacer uso de Sistemas de prevención de intrusos (IPS) para limitar el contenido que se puede visualizar, bloqueando sitios con cierto tipo de contenido cómo pornografía, apuestas online, páginas de descarga de contenido ilegal y sitios de streaming ilegal.'
    )
    ids = models.BooleanField(
        default=False,
        verbose_name='Hacer uso de un Sistema de detección de Intrusos (IDS) para identificar posibles amenazas a nivel de red interna, es importante no solo depender del IDS, pero es de gran utilidad para complementar la seguridad.'
    )
    detectar = models.BooleanField(
        default=False,
        verbose_name='En caso de detectar algún ataque y contenerlo, agregar reglas en el firewall para bloquear las IPs a las cuales se trate de comunicar el Ransomware.'
    )
    red_invitados = models.BooleanField(
        default=False,
        verbose_name='Si se tiene una red de invitados preferentemente mantenerla aislada para no comprometer equipos de la red interna.'
    )
    nac = models.BooleanField(
        default=False,
        verbose_name='Implementar un portal captativo como mínima instancia, preferentemente se sugiere implementar un NAC (Network Access Control).'
    )
    vpn = models.BooleanField(
        default=False,
        verbose_name='Para conexiones remotas o acceso a proveedores de servicios de manera remota se debe implementar una VPN, se sugiere la implementación de un ZTNA (Zero Trust Network Access) para validar los dispositivos remotos de una manera más segura.'
    )
    utm = models.BooleanField(
        default=False,
        verbose_name='Si se utiliza un firewall de Sonic Wall se puede hacer una integración de soluciones (UTM) cómo antivirus, protección de email, gestión de switchs y Access points de Sonic Wall. Al igual que todas las características únicas de protección y cacería de amenazas.'
    )
    control_acceso = models.BooleanField(
        default=False,
        verbose_name='Implementar un control de red para el acceso de los usuarios y prevenir conexiones no autorizadas.'
    )

class ChecklistXDR(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    alcance = models.BooleanField(
        default=False,
        verbose_name='Definir el alcance que tendrá la solución, es recomendable se le brinde el mayor nivel posible de alcance para poder realmente tener una buena visión para su monitoreo.'
    )     
    xdr = models.BooleanField(
        default=False,
        verbose_name='Si la solución XDR a implementar tiene un sensor de red considerar como es que se implementara ya que algunos tienen la función de Bridge (Puente) donde el tráfico pasa a través del sensor para su inspección la desventaja en este escenario por alguna razón se llega a apagar el equipo el tráfico en la Red Interna se podría interrumpir. Algunos de estos sensores también tienen la opción de trabajar con un Mirror Port (Puerto Espejo) al cual se le envía una copia de todo el tráfico que circula por la red por lo que si se llegara apagar el equipo no se interrumpiría el servicio en la red, pero tiene la desventaja de que al solo recibir la copia de la información para poder tener las características de bloqueo contra amenazas se debe de integrar con el Firewall forzosamente para poder mandar las instrucciones de protección.'
    )
    permisos = models.BooleanField(
        default=False,
        verbose_name='Brindarle los permisos necesarios para su correcto funcionamiento.'
    )
    alertas = models.BooleanField(
        default=False,
        verbose_name='Establecer una cadena de comunicación para atender las alertas de las amenazas y así poder tener una respuesta efectiva ante incidentes.'
    )
    revision = models.BooleanField(
        default=False,
        verbose_name="Establecer tiempos para revisión constante de las alertas y reuniones para tomar decisiones de las medidas correctivas a tomar."
    )
    roles = models.BooleanField(
        default=False,
        verbose_name='Dar el rol a una persona para la toma de decisión ante un escenario de ataque crítico para una rápida acción evitando procesos burocráticos ante estos casos, documentando posteriormente el incidente para el análisis posterior.'
    )
    vulnerabilidades = models.BooleanField(
        default=False,
        verbose_name='Revisar constantemente vulnerabilidades y áreas de mejora para corregir áreas que puedan implicar en un riesgo futuro.'
    )

class ChecklistZTNA(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    puntos_criticos = models.BooleanField(
        default=False,
        verbose_name='Identificar los puntos más críticos donde se requiere el acceso remoto y delimitarlos.'
    )        
    acceso = models.BooleanField(
        default=False,
        verbose_name='Definir las personas que deberán de tener acceso a los recursos y de igual manera limitar el acceso solo a los recursos exclusivamente necesarios para cada uno de los usuarios.'
    )
    appgate = models.BooleanField(
        default=False,
        verbose_name='Si se hace uso de Appgate definirlo como control de acceso a la red brindaría la capacidad de evitar el ingreso de dispositivos ajenos a la organización, reduciendo las posibilidades de ataques.'
    )
    seguimiento = models.BooleanField(
        default=False,
        verbose_name='Tener un control y seguimiento de los dispositivos utilizados para las conexiones remotas.'
    )
    recursos_remotos = models.BooleanField(
        default=False,
        verbose_name='Generar un proceso para la solicitud y aprobación del uso de los recursos remotos.'
    )
    manual = models.BooleanField(
        default=False,
        verbose_name='Generar un manual de uso interno para los recursos de red.'
    )

class ChecklistISO(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    alcance = models.BooleanField(
        default=False,
        verbose_name='Definir los alcances que tendrá el sistema con cuidado.'
    )
    comite_revision = models.BooleanField(
        default=False,
        verbose_name='Formar el comité de revisión con elementos de varios departamentos de la organización para así conocer las necesidades de los diferentes elementos de la organización.'
    )
    manuales = models.BooleanField(
        default=False,
        verbose_name='Redactar manuales muy puntuales que definan las responsabilidades de la organización de la empresa hacia su personal a nivel del uso de las herramientas tecnológicas, para de igual manera el usuario este muy consciente de las responsabilidades de el hacia la compañía y las posibles repercusiones que podrían provocar el mal uso de los recursos o información.'
    )
    riesgos = models.BooleanField(
        default=False,
        verbose_name='Analizar meticulosamente los escenarios de riesgos posibles, ya que cuantos más de estos se revisen permitirán tener un mejor sistema de respuesta ante incidentes.'
    )
    analisis = models.BooleanField(
        default=False,
        verbose_name='Utilizar más de una herramienta de análisis de vulnerabilidades para no estar limitado en la visión que se tiene de las brechas de seguridad.'
    )
    documentacion = models.BooleanField(
        default=False,
        verbose_name='Llevar documentación de todos los procesos y revisiones para en caso de un incidente tener un record de cuando se identificó la vulnerabilidad y de esta manera buscar mejorar los tiempos de respuesta y acción.'
    )

class ChecklistGDPR(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    informacion = models.BooleanField(
        default=False,
        verbose_name='Si se le solicitara información a un usuario tener una justificación legal de porque es necesaria esa información.'
    )            
    usuarios = models.BooleanField(
        default=False,
        verbose_name='Hacer del conocimiento de los usuarios que información se almacenara y con que propósitos.'
    )
    proteccion = models.BooleanField(
        default=False,
        verbose_name='Ten en cuenta la protección de datos en todo momento, desde que comienzas a desarrollar un nuevo registro y en cada ocasión que se manipule el registro.'
    )
    encriptar = models.BooleanField(
        default=False,
        verbose_name='Encripta la información personal cada que sea posible.'
    )
    politica = models.BooleanField(
        default=False,
        verbose_name='Crear una política interna de seguridad.'
    )
    conciencia = models.BooleanField(
        default=False,
        verbose_name='Desarrolla la conciencia de la importancia de la protección de la información con campañas de capacitación.'
    )
    evaluacion = models.BooleanField(
        default=False,
        verbose_name='Tomar conciencia de cuando llevar a cabo una evaluación (auditoria) del impacto de la protección de la información.'
    )
    proceso = models.BooleanField(
        default=False,
        verbose_name='Tener un proceso establecido para hacer de conocimiento de los usuarios si es que la información se ve comprometida para que estos puedan tomar medidas de protección.'
    )

class ChecklistZero(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    roles = models.BooleanField(
        default=False,
        name='Roles',
        verbose_name='Se deben definir roles por departamentos, por tipos de usuarios, un usuario común no podría ni debería tener el mismo nivel que un usuario administrador. Se debe implementar una jerarquía en la organización para segmentar los grupos de usuarios teniendo diferentes encargados por departamento se sugiere tener más de uno por departamento para no centralizar la confianza.' 
    )
    acceso_nivel = models.BooleanField(
        default=False,
        name='Accesos',
        verbose_name='Solo los usuarios de más alto nivel tendrán acceso a los servidores, todo deberá de ser supervisado y llevando una bitácora de los cambios.'
    )
    acceso_personal = models.BooleanField(
        default=False,
        name='Accesos',
        verbose_name='Separar los departamentos, el personal de ventas no debería de tener acceso a los recursos del departamento de contabilidad.'
    )
    acceso_confianza = models.BooleanField(
        default=False,
        name='Accesos',
        verbose_name='No centralizar la confianza en un super usuario, tener varios en cargados y cada uno con diferentes accesos a los recursos informáticos.'
    )
    medida_recursos = models.BooleanField(
        default=False,
        name='Medidas de seguridad',
        verbose_name='No compartir recursos sin tomar las medidas de protección correspondientes, evitar el uso de dispositivos ajenos a la compañía en los equipos o la red de la organización (No traer dispositivos de almacenamiento de casa).'
    )
    medida_red = models.BooleanField(
        default=False,
        name='Medidas de seguridad',
        verbose_name='Tener una red particular para los smartphones o en caso de que no usar la de invitados.'
    )
    medida_fisicas = models.BooleanField(
        default=False,
        name='Medidas de seguridad',
        verbose_name='Tener medidas físicas de acceso a recursos como servidores.'
    )
    medida_software = models.BooleanField(
        default=False,
        name='Medidas de seguridad',
        verbose_name='Implementar software especializado como Appgate o Cigent, para aplicar los controles del Zero Trust a nivel digital (Revisar la sección de software especializado).'
    )
    medida_politicas = models.BooleanField(
        default=False,
        name='Medidas de seguridad',
        verbose_name='Tener políticas para controlar el acceso al correo electrónico corporativo en dispositivos ajenos a la empresa.'
    )