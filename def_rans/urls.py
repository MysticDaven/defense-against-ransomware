from django.urls import path
from . import views

urlpatterns = [
    #Blog
    path('', views.home , name='home'),
    path('buenas_practicas/', views.buenas_practicas, name='buenas_practicas'),
    path('check/', views.checklist, name='check'),
    path('specialized/', views.specialized, name='specialized'),

    #Cuenta
    path('cuenta/', views.account, name='account'),
    path('cuenta/index/', views.index, name='index'),
    path('cuenta/registro', views.sign_up, name='sign_up'),
    path('cuenta/consultar', views.consult, name='consult'),
    path('cuenta/formulario', views.form, name='form'),
    path('cuenta/ingresar', views.sign_in, name='sign_in'),
    path('logout/', views.sign_out, name='sign_out'),
    path('cuenta/configuracion/', views.settings_user, name='settings_user'),

    #Metodos
    path('cuenta/configuracion/usuario/', views.edit_profile, name='edit_profile'),
    path('cuenta/configuracion/contraseña/', views.edit_password, name='edit_password'),
    path('cuenta/formulario/identificar/', views.save_Identify, name='save_Identify'),


    #Antivirus
    path('cuenta/antivirus_large/', views.l_comp_av, name="large_av"),
    path('cuenta/antivirus_med/', views.m_comp_av, name='medium_av'),
    path('cuenta/antivirus_small/', views.s_bus_av, name='small_av'),

    #Contention
    path('cuenta/close/', views.close, name='close'),
    path('cuenta/first_step/', views.first_step, name='first_step'),
    path('cuenta/identify/', views.identify, name='identify'),

    #Firewall
    path('cuenta/firewall_large/', views.l_comp_f, name='large_f'),
    path('cuenta/firewall_med/', views.m_comp_f, name='medium_f'),
    path('cuenta/firewall_small', views.s_bus_f, name='small_f'),

    #Media
    path('media/brochure/', views.brochur, name='brochure'),
    path('media/data/', views.data, name='data'),
    path('media/video/', views.video, name='video'),

    #Standards
    path('standards/gdpr/', views.gdpr, name='gdpr'),
    path('standards/iso_27001/', views.iso, name='iso'),
    path('standards/siem/', views.siem, name='siem'),
    path('standards/zerotrust/', views.zerotrust, name='zerotrust')
]