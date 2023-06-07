from django.db import models


# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

TIPO_CHOICES = (
        ('Alojamiento', 'Alojamiento'),
        ('Excursion', 'Excursion'),
        ('Gastronomia', 'Gastronomia'),
    )

TIPO_ADULTO = (
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
    )

TIPO_MENOR = (
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
    )

class Hotel(models.Model):
    nombre_hotel = models.CharField(max_length=128, verbose_name="Hotel")
    direccion = models.CharField(max_length=128, verbose_name="Direccion")
    categoria = models.IntegerField(verbose_name="Categoria")
    
    def __str__(self):
	    return self.nombre_hotel

class Servicios(models.Model):
    class Meta: 
        verbose_name_plural = "Servicios"

    servicio = models.CharField(max_length=128)
    hotel = models.ManyToManyField(Hotel)
    
    def __str__(self):
	    return self.servicio


class Restaurante(models.Model):
    nombre_restaurante = models.CharField(max_length=128, verbose_name="Restaurante")
    direccion = models.CharField(max_length=128, verbose_name="Direccion")
    categoria = models.IntegerField(verbose_name="Categoria")
    detalle = models.CharField(max_length=1024, null=True, verbose_name="Detalle")
    
    def __str__(self):
	    return self.nombre_restaurante

class Excursion(models.Model):
    excursion = models.CharField(max_length=128, verbose_name="Excursion")
    detalle = models.CharField(max_length=1024, verbose_name="Detalle")
    diasSalidas = models.CharField(max_length=1024, verbose_name="Dias Salidas")
    duracion = models.CharField(max_length=10, verbose_name="Duracion")
    horario = models.CharField(max_length=20, verbose_name="Horarios")
    
    def __str__(self):
	    return self.excursion


###########################################################################################
# Hotel
class Reservas(models.Model):
    class Meta: 
        verbose_name_plural = "Reservas"

    fecha_registracion= models.DateField(null=True)
    fecha_desde = models.DateField(null=True)
    fecha_hasta = models.DateField(null=True)
    #Tipo_reserva = models.CharField('Tipo de reserva', max_length=15)
    Tipo_reserva = models.CharField('Tipo de reserva', max_length=15, choices=TIPO_CHOICES, default='Hotel')

    adulto = models.CharField('Cantidad de Adultos', max_length=2, choices=TIPO_ADULTO, default='1')
    menor= models.CharField('Cantidad de Menores', max_length=2, choices=TIPO_MENOR, default='0')
    estado = models.BooleanField(default=True)  

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
   # restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, null=True, blank=True)
   # excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
	   # return self.hotel
        return f"{self.usuario} - {self.hotel} - {self.fecha_desde} - {self.fecha_hasta} "
 
##########################################
 # Modelo Restaurantes


class ReservaRestaurante(models.Model):
    fecha_registracion= models.DateField(null=True)
    fecha_reserva = models.DateField(null=True)
   # usuario = models.CharField(max_length=128, verbose_name="usuario ")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Tipo_reserva = models.CharField('Tipo de reserva', max_length=15, choices=TIPO_CHOICES, default='Gastronomia')
   
    adulto = models.CharField('Cantidad de Adultos', max_length=2, choices=TIPO_ADULTO, default='1')
    menor= models.CharField('Cantidad de Menores', max_length=2, choices=TIPO_MENOR, default='0')
    estado = models.BooleanField(default=True)  
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, default=' ') # muchos a uno

    def __str__(self):
	   # return self.usuario + self.restaurante
        return f"{self.usuario} - {self.restaurante} -{self.fecha_reserva} "
 
 #######################################
 # Modelo Excursiones



class ReservaExcursion(models.Model):
    fecha_registracion= models.DateField(null=True)
    fecha_reserva = models.DateField(null=True)
    hora_reserva =  models.TimeField(null=True)
   #usuario = models.CharField(max_length=128, verbose_name="usuario ")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Tipo_reserva = models.CharField('Tipo de reserva', max_length=15, choices=TIPO_CHOICES, default='Excursion')
   
    adulto = models.CharField('Cantidad de Adultos', max_length=2, choices=TIPO_ADULTO, default='1')
    menor= models.CharField('Cantidad de Menores', max_length=2, choices=TIPO_MENOR, default='0')
    estado = models.BooleanField(default=True)  
    traslado = models.BooleanField(default=True)  
    excursion = models.ForeignKey(Excursion, on_delete=models.CASCADE, default=' ') # muchos a uno

    def __str__(self):
	   # return self.excursion
        return f"{self.usuario} - {self.excursion} - {self.fecha_desde} - {self.fecha_hasta} "
 
 
