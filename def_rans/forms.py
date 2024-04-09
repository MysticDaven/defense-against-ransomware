from django import forms
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

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Old Password'
    }), label="New Password")
    new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'New Password'
    }), label="New Password")
    new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg', 'placeholder': 'Confirm New Password'
    }), label="Confirm New Password")

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