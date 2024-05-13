from django.shortcuts import render, get_object_or_404, redirect
from django.forms import *
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import *
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import edit_user, RespuestasIdentificar, RespuestasConciencia, RespuestasHerramientas

#Create your views here
#def sign_in2(request):
#    return render(request, 'pages/accounts/sign_in.html')

def sign_in(request):
    form = UserLoginForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        print(username + " " + password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            print("Exitoso")
            return redirect('index')
            ...
        else:
            context={
                'form': form,
                'msg' : '2'
            }
            ...
    print("no exitoso")
    return render(request, 'pages/accounts/sign_in.html', context)
    
def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            formN = RegistrationForm()
            context={
                'form': formN,
                'msg' : '1'
            }
        else:
            context={
                'form': form,
                'msg' : '2'
            }
        return render(request, 'pages/accounts/sign_up.html', context)
    else:
        form = RegistrationForm()

    context = { 'form': form }
    return render(request, 'pages/accounts/sign_up.html', context)

def sign_up2(request):
   return render(request, 'pages/accounts/sign_up.html')

def sign_out(request):
    logout(request)
    return redirect('home')

def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = edit_user(request.POST, instance=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)
            context = {
                'form': form,
                'msg': 'Perfil actualizado existosamente'
            }
        else:
            context = {
                'form': form,
                'msg': 'Hubo un problema al actualizar el perfil'
            }
    else:
        form = edit_user(instance=user)
        context = {
            'form': form
        }
    return render(request, 'pages/accounts/settings_user.html', context)                 

def edit_password(request):
    user = request.user
    if request.method == 'POST':
        password_form = PasswordChangeForm(user, request.POST)        
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, user)
            context = {
                'password_form': password_form,
                'msg': 'Contraseña actualizado correctamente'
            }
        else:
            context = {
                'password_form': password_form,
                'msg': 'Hubo un problema al actualizar la contraseña'                
            }
        return render(request, 'pages/accounts/settings_user.html', context)
    else:
        password_form = PasswordChangeForm(user)
        context = {
            'password_form': password_form
        }
        return render(request, 'pages/accounts/edit_profile.html', context)        


def settings_user(request):
    user = request.user
    form = edit_user(instance=user)
    password_form = PasswordChangeForm(user)
    context = {
        'form': form,
        'password_form': password_form
    }
    return render(request, 'pages/accounts/settings_user.html', context)

@login_required(login_url='sign_in')
def form(request):
    user = request.user
    identify_form = IdentifyForm()
    conciencia_form = ConcienciaForm()
    herramientas_form = HerramientasForm()

    context = {
        'identify_form': identify_form, 
        'conciencia_form': conciencia_form,
        'herramientas_form': herramientas_form,
    }
    context.update(realizado(request, context))

    return render(request, 'pages/accounts/form.html', context)

def realizado(request, context):
    r_Identificar = RespuestasIdentificar.objects.filter(user = request.user.id)
    r_Conciencia = RespuestasConciencia.objects.filter(user = request.user.id)
    r_Herramientas = RespuestasHerramientas.objects.filter(user = request.user.id)

    if r_Identificar.count() >= 3:
        context.update({'hecho_identify': 'True'})
        print("Prueba I", context.get('hecho_identify'))
    else:
        context.update({'hecho_identify': 'False'})
        print("Prueba I", context.get('hecho_identify'))
    if r_Conciencia.count() >= 15:
        context.update({'hecho_conciencia': 'True'})
        print("Prueba C", context.get('hecho_conciencia'))
    else:
        context.update({'hecho_conciencia': 'False'})
        print("Prueba C", context.get('hecho_conciencia'))
    if r_Herramientas.count() >= 17:
        context.update({'hecho_herramientas': 'True'})
        print("Prueba H", context.get('hecho_herramientas'))        
    else:
        context.update({'hecho_herramientas': 'False'})
        print("Prueba H", context.get('hecho_herramientas'))        
    
    return context

@login_required(login_url='sign_in')
def save_Identify(request):
    print(request.user.id)
    print("user")
    form = IdentifyForm()
    context = {
        'form': form
    }     
    if request.method == 'POST':
        
        form = IdentifyForm(request.POST) 
        if form.is_valid():
            tipo_empresa = form.cleaned_data['tipo_empresa']
            rol = form.cleaned_data['rol']
            incidente = form.cleaned_data['incidente']
            try:
                RespuestasIdentificar.objects.create(
                    user=User.objects.get(id=request.user.id),
                    respuesta=form.fields['tipo_empresa'].choices[tipo_empresa + 1][1], 
                    pregunta=form.fields['tipo_empresa'].label
                )
                RespuestasIdentificar.objects.create(
                    user=User.objects.get(id=request.user.id),
                    respuesta=form.fields['rol'].choices[rol + 1][1],
                    pregunta=form.fields['rol'].label
                )
                RespuestasIdentificar.objects.create(
                    user=User.objects.get(id=request.user.id),
                    respuesta=form.fields['incidente'].choices[incidente + 1][1],
                    pregunta=form.fields['incidente'].label
                )
                conciencia_form = ConcienciaForm()
                context.update({'msg': '¡Guardado exitosamente!','conciencia_form':conciencia_form})
                context.update(realizado(request, context))
            except Exception as e:
                context.update({'msg': 'Error al guardar los datos. Por favor, inténtalo de nuevo.'})
                print(e)
    return render(request, 'pages/accounts/form.html', context)
    #return redirect("form")

@login_required(login_url='sign_in')
def save_Conciencia(request):
    form = ConcienciaForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ConcienciaForm(request.POST)
        if form.is_valid():
            ataque_propio  = form.cleaned_data['ataque_propio']
            ataque_tercero = form.cleaned_data['ataque_tercero']
            correo = form.cleaned_data['correo']
            datos = form.cleaned_data['datos']
            financiero = form.cleaned_data['financiero']
            ventas = form.cleaned_data['ventas']
            proyectos = form.cleaned_data['proyectos']
            respaldos = form.cleaned_data['respaldos']
            servidores = form.cleaned_data['servidores']
            servicios = form.cleaned_data['servicios']
            div_proyecto = form.cleaned_data['div_proyecto']
            div_info_sens = form.cleaned_data['div_info_sens']
            div_info_cliente = form.cleaned_data['div_info_cliente']
            div_info_fin = form.cleaned_data['div_info_fin']
            div_db = form.cleaned_data['div_db']
            try:
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['ataque_propio'].choices[ataque_propio + 1 ][1],
                    pregunta = form.fields['ataque_propio'].label
                )
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['ataque_tercero'].choices[ataque_tercero + 1 ][1],
                    pregunta = form.fields['ataque_tercero'].label
                )
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['correo'].choices[correo + 1 ][1],
                    pregunta = form.fields['correo'].label
                ) 
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['datos'].choices[datos + 1 ][1],
                    pregunta = form.fields['datos'].label
                )     
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['financiero'].choices[financiero + 1 ][1],
                    pregunta = form.fields['financiero'].label
                )                                  
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['ventas'].choices[ventas + 1 ][1],
                    pregunta = form.fields['ventas'].label
                )       
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['proyectos'].choices[proyectos + 1 ][1],
                    pregunta = form.fields['proyectos'].label
                )              
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['respaldos'].choices[respaldos + 1 ][1],
                    pregunta = form.fields['respaldos'].label
                )                       
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['servidores'].choices[servidores + 1 ][1],
                    pregunta = form.fields['servidores'].label
                )     
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['servicios'].choices[servicios + 1 ][1],
                    pregunta = form.fields['servicios'].label
                )     
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['div_proyecto'].choices[div_proyecto + 1 ][1],
                    pregunta = form.fields['div_proyecto'].label
                )  
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['div_info_sens'].choices[div_info_sens + 1 ][1],
                    pregunta = form.fields['div_info_sens'].label
                )    
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['div_info_cliente'].choices[div_info_cliente + 1 ][1],
                    pregunta = form.fields['div_info_cliente'].label
                )         
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['div_info_fin'].choices[div_info_fin + 1 ][1],
                    pregunta = form.fields['div_info_fin'].label
                )
                RespuestasConciencia.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['div_db'].choices[div_db + 1 ][1],
                    pregunta = form.fields['div_db'].label
                )                                             
                # conciencia_form = ConcienciaForm()
                herramientas_form = HerramientasForm()
                context.update({'msg': '¡Guardado exitosamente!','herramientas_form':herramientas_form})
                context.update(realizado(request, context))
                print('Hecho herramientas ', context.get('hecho_herramientas'))
                print('HECHO HERRAMIENTAS')
            except Exception as e:
                context.update({'msg': 'Error al guardar los datos. Por favor, inténtalo de nuevo.'})
                print(e)
    return render(request, 'pages/accounts/form.html', context)                

@login_required(login_url='sign_in')
def save_Herramientas(request):
    form = HerramientasForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = HerramientasForm(request.POST)
        if form.is_valid():
            antivirus = form.cleaned_data['antivirus']
            dlp = form.cleaned_data['dlp']
            protec_correo = form.cleaned_data['protec_correo']
            vpn = form.cleaned_data['vpn']
            xdr = form.cleaned_data['xdr']
            firewall = form.cleaned_data['firewall']
            waf = form.cleaned_data['waf']
            iso = form.cleaned_data['iso']
            zero_trust = form.cleaned_data['zero_trust']
            gdpr = form.cleaned_data['gdpr']
            nist = form.cleaned_data['nist']
            siem = form.cleaned_data['siem']
            soar = form.cleaned_data['soar']
            soc = form.cleaned_data['soc']
            sgsdp = form.cleaned_data['sgsdp']
            buenas_prac = form.cleaned_data['buenas_prac']
            preparada = form.cleaned_data['preparada']
            
            try:
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['antivirus'].choices[antivirus + 1][1],
                    pregunta = form.fields['antivirus'].label 
                )
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['dlp'].choices[dlp + 1][1],
                    pregunta = form.fields['dlp'].label 
                )
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['protec_correo'].choices[protec_correo + 1][1],
                    pregunta = form.fields['protec_correo'].label 
                )       
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['vpn'].choices[vpn + 1][1],
                    pregunta = form.fields['vpn'].label 
                )  
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['xdr'].choices[xdr + 1][1],
                    pregunta = form.fields['xdr'].label 
                )        
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['firewall'].choices[firewall + 1][1],
                    pregunta = form.fields['firewall'].label 
                )            
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['waf'].choices[waf + 1][1],
                    pregunta = form.fields['waf'].label 
                )       
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['iso'].choices[iso + 1][1],
                    pregunta = form.fields['iso'].label 
                )
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['zero_trust'].choices[zero_trust + 1][1],
                    pregunta = form.fields['zero_trust'].label 
                )    
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['gdpr'].choices[gdpr + 1][1],
                    pregunta = form.fields['gdpr'].label 
                )       
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['nist'].choices[nist + 1][1],
                    pregunta = form.fields['nist'].label 
                )        
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['siem'].choices[siem + 1][1],
                    pregunta = form.fields['siem'].label 
                )                   
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['soar'].choices[soar + 1][1],
                    pregunta = form.fields['soar'].label 
                )   
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['soc'].choices[soc + 1][1],
                    pregunta = form.fields['soc'].label 
                )                 
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['sgsdp'].choices[sgsdp + 1][1],
                    pregunta = form.fields['sgsdp'].label 
                )           
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['buenas_prac'].choices[buenas_prac + 1][1],
                    pregunta = form.fields['buenas_prac'].label 
                )         
                RespuestasHerramientas.objects.create(
                    user = User.objects.get(id=request.user.id),
                    respuesta = form.fields['preparada'].choices[preparada + 1][1],
                    pregunta = form.fields['preparada'].label 
                )
                context.update({'msg_H': '¡Guaradado exitosamente!'})
            except Exception as e:
                context.update({'msg_H': 'Error al guardar los datos. Por favor, inténtalo de nuevo.'})
                print(e)
            print('Error', context.get('msg_H'))
    return render(request, 'pages/accounts/form.html', context)
            

def home(request):
    return render(request, 'pages/home.html')

def index(request):
    return render(request, 'pages/accounts/index.html')

def buenas_practicas(request):
    return render(request, 'pages/buenas_practicas.html')

def checklist(request):
    return render(request, 'pages/checklist.html')

def specialized(request):
    return render(request, 'pages/specialized_software.html')

def account(request):
    return render(request, 'pages/accounts/account.html')

def consult(request):
    return render(request, 'pages/accounts/consult_form.html')

def l_comp_av(request):
    return render(request, 'pages/antivirus/large_companies_av.html')

def m_comp_av(request):
    return render(request, 'pages/antivirus/medium_companies_av.html')

def s_bus_av(request):
    return render(request, 'pages/antivirus/small_business_av.html')

def close(request):
    return render(request, 'pages/contention/close.html')

def first_step(request):
    return render(request, 'pages/contention/first_step.html')

def identify(request):
    return render(request, 'pages/contention/identify.html')

def l_comp_f(request):
    return render(request, 'pages/firewall/large_companies_fw.html')

def m_comp_f(request):
    return render(request, 'pages/firewall/medium_companies_fw.html')

def s_bus_f(request):
    return render(request, 'pages/firewall/small_business_fw.html')

def brochur(request):
    return render(request, 'pages/media/brochure.html')

def data(request):
    return render(request, 'pages/media/datasheets.html')

def video(request):
    return render (request, 'pages/media/video.html')

def gdpr(request):
    return render(request, 'pages/standards/gdpr.html')

def iso(request):
    return render(request, 'pages/standards/iso_27001.html')

def siem(request):
    return render(request, 'pages/standards/siem.html')

def zerotrust(request):
    return render(request, 'pages/standards/zerotrust.html')








