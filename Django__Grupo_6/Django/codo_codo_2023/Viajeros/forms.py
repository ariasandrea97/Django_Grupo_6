from django import forms
from django.core.exceptions import ValidationError
from .models import Reservas, Hotel, Servicios, Restaurante, ReservaRestaurante, Excursion, ReservaExcursion


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm



# class EnviarReservaForm(forms.ModelForm):
#     fecha_desde = forms.DateField(label="Fecha Desde", widget=forms.DateInput(attrs={'type': 'date'}))
#     fecha_hasta = forms.DateField(label="Fecha Hasta", widget=forms.DateInput(attrs={'type': 'date'}))


#     class Meta:
#         model = Reservas
#         fields= [ 'fecha_desde', 'fecha_hasta', 'adulto','menor']
    
#     def clean(self):
#         cleaned_data = super().clean()
#         fechaD = cleaned_data.get("fecha_desde")
#         fechaH = cleaned_data.get("fecha_hasta")

#         # print(cleaned_data)
#         if fechaD is not None and fechaH is not None and fechaD > fechaH:
#             raise ValidationError("La Fecha Hasta debe ser posterior a la Fecha Desde")
        
#         return cleaned_data

###########################  Formularios para reservas  ################################################
class EnviarReservaHotelForm(forms.ModelForm):  # para reserva de Hotel
    fecha_desde = forms.DateField(label="Fecha Desde", widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_hasta = forms.DateField(label="Fecha Hasta", widget=forms.DateInput(attrs={'type': 'date'}))
  
    hotel=forms.ModelChoiceField(queryset=Hotel.objects.order_by('nombre_hotel') )
    # restaurante=forms.ModelChoiceField(queryset=Restaurante.objects.order_by('nombre_restaurante'))
    # excursion =forms.ModelChoiceField(queryset=Excursion.objects.order_by('excursion'))


    def clean(self):
        cleaned_data = super().clean()
        fechaD = cleaned_data.get("fecha_desde")
        fechaH = cleaned_data.get("fecha_hasta")

        if fechaD is not None and fechaH is not None and fechaD > fechaH:
            raise ValidationError("La Fecha Hasta debe ser posterior a la Fecha Desde")

        
    def clean_hotel(self):
        hotel = self.cleaned_data['hotel']
        print("hotel:", hotel)
        return hotel
    

    class Meta:
        model = Reservas
        fields= [ 'fecha_desde', 'fecha_hasta', 'adulto','menor', 'hotel']

        


class EnviarReservaRestauranteForm(forms.ModelForm):  # para reserva gastronomia (restaurante)
    fecha_reserva = forms.DateField(label="Fecha reserva", widget=forms.DateInput(attrs={'type': 'date'}))
    hora_reserva = forms.TimeField(label="Hora Reserva", widget=forms.TimeInput(attrs={'type': 'time'}))
    # adulto = forms.IntegerField(label='Cantidad de Adultos',required=True, initial=1, widget=forms.NumberInput(attrs={'type': 'number'}))
    # menor= forms.IntegerField(label='Cantidad de Menores', required=True, initial=0, widget=forms.NumberInput(attrs={'type': 'number'}))
    restaurante=forms.ModelChoiceField(queryset=Restaurante.objects.order_by('nombre_restaurante'))

        
    def clean_restaurante(self):
        restaurante = self.cleaned_data['restaurante']
        print("restaurante:", restaurante)
        return restaurante

    class Meta:
        model = ReservaRestaurante
        fields= [ 'fecha_reserva', 'hora_reserva', 'adulto','menor', 'restaurante']


class EnviarReservaExcursionForm(forms.ModelForm):  # para reserva Excursion
    fecha_reserva = forms.DateField(label="Fecha reserva", widget=forms.DateInput(attrs={'type': 'date', 'disabled_days_of_week': [2, 4]}))
    hora_reserva = forms.TimeField(label="Hora Reserva", widget=forms.TimeInput(attrs={'type': 'time'}))
    adulto = forms.IntegerField(label='Cantidad de Adultos',widget=forms.NumberInput(attrs={'type': 'number'}))
    menor= forms.IntegerField(label='Cantidad de Menores', widget=forms.NumberInput(attrs={'type': 'number'}))
    traslado = forms.BooleanField(label="Requiere traslado",required=False,initial=False)  
    
    excursion=forms.ModelChoiceField(queryset=Excursion.objects.order_by('excursion'))
        
    def clean_excursion(self):
        excursion = self.cleaned_data['excursion']
        print("excursion:", excursion)
        return excursion

    class Meta:
        model = ReservaExcursion

        fields= [ 'fecha_reserva', 'hora_reserva', 'adulto','menor', 'traslado','excursion']



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
            print('email_already_registered and user_is_active')
            raise forms.ValidationError("Email already registered.")
        elif email_already_registered:
            print('email_already_registered')
            User.objects.filter(email = email_passed).delete()

        return email_passed




 ##################### Mis Reservas     #############
class ConsultaReservasForm(forms.Form):

    OPCIONES = (
        ('todo', 'Todo'),
        ('hotel', 'Hotel'),
        ('restaurante', 'Gastronomia'),
        ('excursion', 'Excursión'),
    )
    
    seleccion = forms.ChoiceField(choices=OPCIONES)

    # fechaDesde = forms.DateField(label=' Fecha Desde',widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    # fechaHasta = forms.DateField(label=' Fecha Hasta',widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    # listado_hotel = Reservas.objects.filter(usuario=request.user)
    # listado_restaurante = ReservaRestaurante.objects.filter(usuario=request.user)
    # listado_excursion = ReservaExcursion.objects.filter(usuario=request.user)


    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     dataD = cleaned_data.get("fechaDesde")
    #     dataH = cleaned_data.get("fechaHasta")

    #     print(cleaned_data)
    #     print(dataD)
    #     print(dataH)
    #     if dataD is not None and dataH is not None:
    #         print(dataD > dataH)
    #         print('Ingreso al 1er if')

    #     if dataD is not None and dataH is not None and dataD > dataH:
    #         print('Ingreso al 2do if')
    #         raise ValidationError("La Fecha Desde debe ser anterior a la Fecha Hasta")
        
    #     return cleaned_data
