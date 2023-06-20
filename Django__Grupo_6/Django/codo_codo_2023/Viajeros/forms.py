from django import forms
from django.core.exceptions import ValidationError
from .models import Reservas, Hotel,  Restaurante, ReservaRestaurante, Excursion, ReservaExcursion #, DiaSalida

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import date


# class HotelForm(forms.ModelForm):
#     class Meta:
#         model = Hotel
#         fields = ['nombre', 'ubicacion', 'descripcion', 'imagen', 'servicios']


class EnviarConsultaForm(forms.Form):
#     fecha_desde = forms.DateField(label="Fecha Desde", widget=forms.DateInput(attrs={'type': 'date'}))
#     fecha_hasta = forms.DateField(label="Fecha Hasta", widget=forms.DateInput(attrs={'type': 'date'}))

    name = forms.CharField(label='Nombre', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)


###########################  Formularios para reservas  ################################################
class EnviarReservaHotelForm(forms.ModelForm):  # para reserva de Hotel
    class Meta:
        model = Reservas
        fields= [ 'hotel','fecha_desde', 'fecha_hasta', 'adulto','menor' ] 

    fecha_desde = forms.DateField(label="Fecha de llegada", widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))
    fecha_hasta = forms.DateField(label="Fecha de Salida", widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))
    # hotel=forms.ModelChoiceField(queryset=Hotel.objects.order_by('nombre_hotel') )

    def clean(self):
        cleaned_data = super().clean()
        fechaD = cleaned_data.get("fecha_desde")
        fechaH = cleaned_data.get("fecha_hasta")

        if fechaD is not None and fechaH is not None and fechaD > fechaH:
            raise ValidationError("La Fecha Hasta debe ser posterior a la Fecha Desde")

    # def clean_hotel(self):
    #     hotel = self.cleaned_data['hotel']
    #     print("hotel:", hotel)
    #     return hotel
     
    
    def __init__(self, *args, **kwargs):
        super(EnviarReservaHotelForm, self).__init__(*args, **kwargs)


class EnviarReservaRestauranteForm(forms.ModelForm):  # para reserva gastronomia (restaurante)
    class Meta:
        model = ReservaRestaurante
        fields= [ 'restaurante','fecha_reserva', 'hora_reserva', 'adulto','menor' ]

    fecha_reserva = forms.DateField(label="Fecha de reserva", widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))
    # hora_reserva = forms.TimeField(label="Hora de Reserva", widget=forms.TimeInput(attrs={'type': 'time'}))
    opciones_horas = [('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'),('15:00', '15:00'),('16:00', '16:00'),('17:00', '17:00'),('18:00', '18:00'),('19:00', '19:00'),('20:00', '20:00'),('21:00', '21:00'),('22:00', '22:00'),]
    hora_reserva = forms.ChoiceField(label="Hora de Reserva", choices=opciones_horas, widget=forms.Select)
    # adulto = forms.IntegerField(label='Cantidad de Adultos',required=True, initial=1, widget=forms.NumberInput(attrs={'type': 'number'}))
    # menor= forms.IntegerField(label='Cantidad de Menores', required=True, initial=0, widget=forms.NumberInput(attrs={'type': 'number'}))
    restaurante=forms.ModelChoiceField(queryset=Restaurante.objects.order_by('nombre_restaurante'))

        
    # def clean_restaurante(self):
    #     restaurante = self.cleaned_data['restaurante']
    #     print("restaurante:", restaurante)
    #     return restaurante




class EnviarReservaExcursionForm(forms.ModelForm):  # para reserva Excursion
    class Meta:
        model = ReservaExcursion
        fields= [ 'excursion','fecha_reserva', 'hora_reserva', 'adulto','menor', 'traslado']

    fecha_reserva = forms.DateField(label="Fecha de reserva", widget=forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}))
    # hora_reserva = forms.TimeField(label="Hora Reserva", widget=forms.TimeInput(attrs={'type': 'time'}))
    opciones_horas = [('09:00', '09:00'), ('15:00', '15:00')]
    hora_reserva = forms.ChoiceField(label="Hora Reserva", choices=opciones_horas, widget=forms.Select)
    # adulto = forms.IntegerField(label='Cantidad de Adultos',widget=forms.NumberInput(attrs={'type': 'number'}))
    # menor= forms.IntegerField(label='Cantidad de Menores', widget=forms.NumberInput(attrs={'type': 'number'}))
    traslado = forms.BooleanField(label="Requiere traslado",required=False,initial=False)  
    excursion=forms.ModelChoiceField(queryset=Excursion.objects.order_by('excursion'))
        
    # def clean_excursion(self):
    #     excursion = self.cleaned_data['excursion']
    #     print("excursion:", excursion)
    #     return excursion



##########################  USUARIOS   ############################################

class AltaUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields =  ['first_name', 'last_name', 'email', 'username','password1', 'password2']

    def clean_email(self):
        email_passed = self.cleaned_data.get("email")
        email_already_registered = User.objects.filter(email = email_passed).exists()
        user_is_active = User.objects.filter(email = email_passed, is_active = 1)
        if email_already_registered and user_is_active:
            raise forms.ValidationError("Email already registered.")
        elif email_already_registered:
            User.objects.filter(email = email_passed).delete()

        return email_passed




 #####################      Mis Reservas     #################################################
class ConsultaReservasForm(forms.Form):

    OPCIONES = (
        ('todo', 'Todo'),
        ('hotel', 'Hotel'),
        ('restaurante', 'Gastronomia'),
        ('excursion', 'Excursión'),
    )
    
    seleccion = forms.ChoiceField(choices=OPCIONES)

 

################  Modificar datos de Usuario #############################
class ModificarDatosForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  

    def __init__(self, *args, **kwargs):
        super(ModificarDatosForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['email'].label = 'Email'



# class ReservaForm(forms.ModelForm):
#     class Meta:
#         model = Reservas
#         fields= [ 'hotel','fecha_desde', 'fecha_hasta', 'adulto','menor']

#     def __init__(self, *args, **kwargs):
#         super(ReservaForm, self).__init__(*args, **kwargs)


# class ReservaRestauranteForm(forms.ModelForm):
#     class Meta:
#         model = ReservaRestaurante
#         fields= [ 'restaurante','fecha_reserva', 'hora_reserva', 'adulto', 'menor']

#     def __init__(self, *args, **kwargs):
#         super(ReservaRestauranteForm, self).__init__(*args, **kwargs)

# class ReservaExcursionForm(forms.ModelForm):
#     class Meta:
#         model = ReservaExcursion
#         fields= [ 'excursion','fecha_reserva', 'hora_reserva', 'adulto', 'menor']

#     def __init__(self, *args, **kwargs):
#         super(ReservaExcursionForm, self).__init__(*args, **kwargs)
