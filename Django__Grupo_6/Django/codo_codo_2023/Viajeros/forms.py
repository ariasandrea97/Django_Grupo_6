from django import forms
from django.core.exceptions import ValidationError
from .models import Reservas #Usuario


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


BIRTH_YEAR_CHOICES = range(1980,2006)
TYPE_CHOICES = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
]

TYPE_CHOICES2 = [
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
]

TYPE_RESERVA = [
    ("Alojamiento", "Alojamiento"),
    ("Excursion", "Excursion"),
    ("Otros", "Otros"),
]


# class EnviarConsultaForm(forms.Form):
#         nombre = forms.CharField(label="Nombre ",widget=forms.TextInput(), required=True)
#         apellido = forms.CharField(label="Apellido ", required=True)
#         mail = forms.EmailField(label="Mail", required=True)
#         telefono = forms.CharField(label="Telefono", required=True)


#         # fecha_ingreso = forms.DateField(
#         #     widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
#         # )
#         tipo = forms.ChoiceField(
#             label="Tipo de reserva",
#             widget=forms.Select,
#             choices=TYPE_RESERVA,
#         )
#         # Campo Fecha con date picker en el chrome.
#         fecha_desde = forms.DateField(label="Fecha Desde", widget=forms.DateInput(attrs={'type': 'date'}))
#         fecha_hasta = forms.DateField(label="Fecha Hasta", widget=forms.DateInput(attrs={'type': 'date'}))
#         #validar que la fecha hasta sea mayor que la fecha desde

#         adultos = forms.ChoiceField(
#             label="Adultos",
#             widget=forms.Select,
#             choices=TYPE_CHOICES,
#         )
#         niños  = forms.ChoiceField(
#             label="Niños",
#             widget=forms.Select,
#             choices=TYPE_CHOICES2,
#         )

#         mensaje = forms.CharField(widget=forms.Textarea)
        
#         # def clean(self):
#         #     # Validación de fechas

#         #     if self.fecha_desde >self.fecha_hasta :
#         #         print('La fecha hasta debe ser mayor a la fecha de inicio')
#         #         #raise forms.ValidationError("La fecha hasta debe ser mayor a la fecha de inicio")
#         #         #raise ValidationError('La fecha hasta debe ser mayor a la fecha de inicio')

class EnviarReservaForm(forms.ModelForm):
    fecha_desde = forms.DateField(label="Fecha Desde", widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_hasta = forms.DateField(label="Fecha Hasta", widget=forms.DateInput(attrs={'type': 'date'}))
#         
    class Meta:
        model = Reservas

        fields= ['Tipo_reserva', 'fecha_desde', 'fecha_hasta', 'adulto','menor']


class AltaUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields =  ['first_name', 'last_name', 'email', 'username','password1', 'password2']

    # Check unique email
    # Email exists && account active -> email_already_registered
    # Email exists && account not active -> delete previous account and register new one
    def clean_email(self):
        email_passed = self.cleaned_data.get("email")
        email_already_registered = User.objects.filter(email = email_passed).exists()
        user_is_active = User.objects.filter(email = email_passed, is_active = 1)
        if email_already_registered and user_is_active:
            print('email_already_registered and user_is_active')
            raise forms.ValidationError("Email already registered.")
        elif email_already_registered:
            print('email_already_registered')
            User.objects.filter(email = email_passed).delete()

        return email_passed