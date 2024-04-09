from django.shortcuts import *
from django.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import *
from .forms import *

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

def logout(request):
    logout(request)
    return redirect('home')

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

def form(request):
    return render(request, 'pages/accounts/form.html')

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








