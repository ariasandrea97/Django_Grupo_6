from django.contrib import admin

from .models import  Hotel, Servicios, Restaurante, Excursion, Reservas, ReservaRestaurante, ReservaExcursion


# Register your models here.


admin.site.register(Hotel)
admin.site.register(Servicios)
admin.site.register(Restaurante)
admin.site.register(Excursion)
admin.site.register(Reservas)
admin.site.register(ReservaRestaurante)
admin.site.register(ReservaExcursion)




