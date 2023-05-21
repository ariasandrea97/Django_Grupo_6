from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone


# usuarios/models.py
# from django.contrib.auth.models import AbstractUser


class Usuario(models.Model):

    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)
    mail =models.EmailField(max_length=128)
    # first_name = models.CharField('Nombre', max_length=60)
    # last_name = models.CharField('Apellidos', max_length=120)

    def __str__(self):
	    return self.mail


class Hotel(models.Model):
    nombre_hotel = models.CharField(max_length=128, verbose_name="Hotel")
    direccion = models.CharField(max_length=128, verbose_name="Direccion")
    categoria = models.IntegerField(verbose_name="Categoria")


class Reservas(models.Model):
    TIPO_CHOICES = (
        ('Alojamiento', 'Alojamiento'),
        ('Excursion', 'Excursion'),
        ('Gastronomia', 'Gastronomia'),
        # ('3', 'RECURSOS HUMANOS'),
        # ('4', 'OTROS'),
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

    fecha_desde = models.DateField(null=True)
    fecha_hasta = models.DateField(null=True)
    # Tipo_reserva = models.CharField(max_length=128, verbose_name="Tipo")
    # Cantidad_adultos= models.IntegerField(verbose_name="Cantidad de Adultos")
    # Cantidad_menor= models.IntegerField(verbose_name="Cantidad de Menores")
    usuario = models.CharField(max_length=128, verbose_name="usuario ")
    # hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)

    Tipo_reserva = models.CharField('Tipo de reserva', max_length=15, choices=TIPO_CHOICES)
    adulto = models.CharField('Cantidad de Adultos', max_length=2, choices=TIPO_ADULTO, default='1')
    menor= models.CharField('Cantidad de Menores', max_length=2, choices=TIPO_MENOR, default='0')
    estado = models.BooleanField(default=True)  # my_boolean = forms.BooleanField(required=False, initial=True)
    # hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    # usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # 1 usuario puede tener muchas reservas


 