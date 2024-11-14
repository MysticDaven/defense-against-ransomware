from django import forms
from .models import model_identificar, model_conciencia, model_herramientas, Preguntas, Respuestas, ChecklistDLP, ChecklistAntivirus, ChecklistFirewall, ChecklistGDPR, ChecklistZTNA, ChecklistISO, ChecklistXDR, ChecklistZero

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

DISPOSITIVOS = (
    ('1', '1<=50 (pequeña)'),
    ('2', '51<=150 (mediana)'),
    ('3', '151 en adelante (Grande)')
)

DESICION = (
    ('1', 'Si'),
    ('2', 'No')
)

class RegistrationForm(UserCreationForm):
  password1 = forms.CharField(
      label=_("Contraseña"),
      widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Contraseña'}),
  )
  password2 = forms.CharField(
      label=_("Confirma tu contraseña"),
      widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirma tu contraseña'}),
  )

  class Meta:
    model = User
    fields = ('username', 'email', )

    widgets = {
      'username': forms.TextInput(attrs={
          'class': 'form-control form-control-lg',
          'placeholder': 'Usuario'
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control form-control-lg',
          'placeholder': 'Correo'
      })
    }

class UserLoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control form-control-lg", "placeholder": "Usuario", "name": "correo", "id": "correo"}))
  password = forms.CharField(
      label=_("Contraseña"),
      strip=False,
      widget=forms.PasswordInput(attrs={"class": "form-control form-control-lg", "placeholder": "Contraseña", "name": "password", "id": "password"}),
  )

class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Email'
    }))
  
class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
       max_length=50, 
       widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg',             
        }), 
        label="Contraseña Actual")
    new_password1 = forms.CharField(
       max_length=50, 
       widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg', 
        }), 
        label="Nueva Contraseña")
    new_password2 = forms.CharField(
        max_length=50, 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-lg', 
        }), label="Confirmar Nueva Contraseña")

class Formulario(forms.Form):
    pregunta_1 = forms.ChoiceField(choices=DISPOSITIVOS)
    pregunta_2 = forms.ChoiceField(choices=DESICION)
    pregunta_3 = forms.ChoiceField(choices=DESICION)
    pregunta_4 = forms.ChoiceField(choices=DESICION)
    pregunta_5 = forms.ChoiceField(choices=DESICION)
    pregunta_6 = forms.ChoiceField(choices=DESICION)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class IdentifyForm(forms.ModelForm):
    class Meta:
        model = model_identificar
        fields = '__all__'
        

class ConcienciaForm(forms.ModelForm):
    class Meta:
       model = model_conciencia  
       fields = '__all__'      

class HerramientasForm(forms.ModelForm):
   class Meta:
      model = model_herramientas
      fields = '__all__'

class CheckDLP(forms.ModelForm):
   class Meta:
      model = ChecklistDLP
      fields = '__all__'

class CheckAntivirus(forms.ModelForm):
   class Meta:
      model = ChecklistAntivirus
      fields = ['analisis', 'busqueda', 'sandbox', 'revision', 'permisos', 'gestor', 'usb', 'entrenamiento'] 

class CheckFirewall(forms.ModelForm):
   class Meta:
      model = ChecklistFirewall
      fields = '__all__'

class CheckXDR(forms.ModelForm):
   class Meta:
      model = ChecklistXDR
      fields = '__all__'

class CheckZTNA(forms.ModelForm):
   class Meta:
      model = ChecklistZTNA
      fields = '__all__'

class CheckISO(forms.ModelForm):
   class Meta:
      model = ChecklistISO
      fields = '__all__'

class CheckGDPR(forms.ModelForm):
   class Meta:
      model = ChecklistGDPR
      fields = '__all__'

class CheckZero(forms.ModelForm):
   class Meta:
      model = ChecklistZero
      fields = '__all__'

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Nombre de usuario'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Correo electrónico'
            }),
        }
        labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg', 
                'placeholder': f'Ingrese {self.fields[field].label}'
            })
    def set_labels(self):
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['email'].label = 'Correo electrónico'
