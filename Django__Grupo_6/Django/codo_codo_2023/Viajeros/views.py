from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

#

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic.list import ListView
import datetime
from django.contrib.auth.decorators import login_required


#Definicion de los formularios:
# from .forms import EnviarReservaForm 
from .forms import EnviarReservaHotelForm, EnviarReservaRestauranteForm, EnviarReservaExcursionForm, ConsultaReservasForm
from .forms import AltaUsuarioForm
from .models import ReservaExcursion, ReservaRestaurante, Reservas, Servicios, Hotel, User


def index(request):
    # Hagamos de cuenta que este dato viene de la BBDD

    # usuario = {
    #     'nombre': 'Maria',
    #     'apellido': 'Del Cerro',
    #     'mail': 'maria@delcerro',
    #     'valid': False
    # }

    # listado_usuarios = [
    #     {
    #         'name': 'Maria',
    #         'last_name': 'Del Cerro',
    #         'age': 25,
    #         'valid': False,
    #     },
    #     {
    #         'name': 'Florencia',
    #         'last_name': 'Perez',
    #         'age': 30,
    #         'valid': False,
    #     },
    #     {
    #         'name': 'Martin',
    #         'last_name': 'Del Moro',
    #         'age': 35,
    #         'valid': False,
    #     },
    # ]

    context = {
        # 'first_name': 'Carlos',
        # 'last_name': 'Lopez',
     #   'usuario': usuario,
        #'usuario': usuario_ficticio,
      #  'listado_usuarios': listado_usuarios
    }

    return render(request, 'Viajeros/index.html', context)




def baja_persona(request):
    context={}
    return render(request, 'Viajeros/baja_persona.html', context)

####################  PAGINAS ##########################################
def nosotros(request):
    context={}
    return render(request, 'Viajeros/paginas/nosotros.html', context)

def alojamiento(request):
    context={}
    return render(request, 'Viajeros/paginas/alojamiento.html', context)

def gastronomia(request):
    context={}
    return render(request, 'Viajeros/paginas/gastronomia.html', context)

def circuito_turistico(request):
    context={}
    return render(request, 'Viajeros/paginas/circuito_turistico.html', context)


def ruta_del_vino(request):
    context={}
    return render(request, 'Viajeros/paginas/ruta_del_vino.html', context)




############   alta de un usuario      ######################
def registro(request):     
    if request.method == "POST":
        alta_usuario_form = AltaUsuarioForm(request.POST)
        if alta_usuario_form.is_valid():
            user = alta_usuario_form.save(commit=False)
            user.save()  #guardamos el usuario

            messages.add_message(request, messages.SUCCESS, 'Usuario dado de alta con éxito', extra_tags="tag1")
             
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'Ha iniciado sesion como: ' + alta_usuario_form.cleaned_data.get('username'), extra_tags="tag1")
                              
            return render(request, 'Viajeros/index.html')
    else:
        # GET
        alta_usuario_form = AltaUsuarioForm()
    
    context = {
        'form': alta_usuario_form
    }

    return render(request, 'Viajeros/usuario/registro.html',context) 


############    LOGIN / LOGOUT  #####################

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario =form.cleaned_data.get('username')
            contraseña= form.cleaned_data.get('password')
            user= authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request,user)
                messages.info(request, f"Ha iniciado sesion como: {usuario}")
                return render(request, 'Viajeros/index.html')

    form = AuthenticationForm()
    return render(request, 'Viajeros/usuario/login.html',{"form": form}) 

##
def logout_request(request):
    logout(request)
    messages.info(request,"Sesion finalizada")
    return render(request, 'Viajeros/index.html') 

#####################################################################

def mi_cuenta(request):
    context = {}
    return render(request, 'Viajeros/paginas/mi_cuenta.html', context)

##############  HOTELES  ##########################################
def detalle_hotel_Algodon(request):
    context = {}
    servicios= Servicios.objects.filter(hotel__id=6)
    context = {
        'listado' : servicios,
        'tipo_reservas' : 'hotel'
        }

    return render(request, 'Viajeros/paginas/detalle_hotel_Algodon.html', context)


def detalle_hotel_PuestaSol(request):
    context = {}
    servicios= Servicios.objects.filter(hotel__id=5)
    context['listado'] = servicios

    return render(request, 'Viajeros/paginas/detalle_hotel_PuestaSol.html', context)


def detalle_hotel_Mendoza(request):
    context = {}
    servicios= Servicios.objects.filter(hotel__id=4)
    context['listado'] = servicios

    return render(request, 'Viajeros/paginas/detalle_hotel_Mendoza.html', context)


#######################   ##################################
# def enviar_consulta(request):    # guarda reserva en la tabla Reservas
#     context={}
#     if request.method == "POST":
#         form = EnviarReservaForm(request.POST)
#         if form.is_valid():
#             # print(request.user)
#             alta_reserva = form.save(commit=False)
#             alta_reserva.usuario= request.user
#             # alta_reserva.Tipo_reserva= "Excursion"
#             alta_reserva.save()  #guardamos la reserva
#             messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")
#             return render(request, 'Viajeros/index.html', context)

#     else:
#         # GET
#         form = EnviarReservaForm()

#     context = {'form': form}
#     return render(request, 'Viajeros/paginas/enviar_consulta.html', context)

#########################################################
#@login_required
def enviar_reserva_hotel(request):    # guarda reserva en la tabla Reservas
    context={}
    if request.method == "POST":
        print("POST")
        
        form = EnviarReservaHotelForm(request.POST)
        
        if form.is_valid():
            print("def enviar_reserva_hotel(request) ---  form.is_valid()")
            alta_reserva = form.save(commit=False)
            alta_reserva.usuario= request.user
            
            # alta_reserva.Tipo_reserva=   "Alojamiento"
            
            alta_reserva.fecha_registracion= datetime.date.today()

            alta_reserva.save()  #guardamos la reserva
            messages.add_message(request, messages.SUCCESS, 'Reserva enviada con exito', extra_tags="tag1")
            return render(request, 'Viajeros/index.html', context)

    else:
        # GET
        print("GET")
        form = EnviarReservaHotelForm()

    context = {'form': form}

    return render(request, 'Viajeros/paginas/enviar_reserva_hotel.html', context)




#####################################################################################

def enviar_reserva_restaurante(request):    # guarda reserva en la tabla Reservas
    context={}
    if request.method == "POST":
        form = EnviarReservaRestauranteForm(request.POST)
        if form.is_valid():
            alta_reserva_restaurante = form.save(commit=False)
            alta_reserva_restaurante.usuario= request.user
            alta_reserva_restaurante.Tipo_reserva= "Restaurante"
            alta_reserva_restaurante.fecha_registracion= datetime.date.today()

            alta_reserva_restaurante.save()  #guardamos la reserva
            messages.add_message(request, messages.SUCCESS, 'Reserva enviada con exito', extra_tags="tag1")
            return render(request, 'Viajeros/index.html', context)

    else:
        # GET
        form = EnviarReservaRestauranteForm()

    context = {'form': form}
    return render(request, 'Viajeros/paginas/enviar_reserva_restaurante.html', context)

##################################################################################

def enviar_reserva_excursion(request):    # guarda reserva en la tabla Reservas
    context={}
    if request.method == "POST":
        form = EnviarReservaExcursionForm(request.POST)
        if form.is_valid():
            # print("form.cleaned_data[hotel]",form.cleaned_data["hotel"])
            alta_reserva_excursion = form.save(commit=False)
            alta_reserva_excursion.usuario= request.user
            alta_reserva_excursion.Tipo_reserva= "Excursion"
            alta_reserva_excursion.fecha_registracion= datetime.date.today()

            alta_reserva_excursion.save()  #guardamos la reserva
            messages.add_message(request, messages.SUCCESS, 'Reserva enviada con exito', extra_tags="tag1")
            return render(request, 'Viajeros/index.html', context)

    else:
        # GET
        form = EnviarReservaExcursionForm()

    context = {'form': form}
    return render(request, 'Viajeros/paginas/enviar_reserva_excursion.html', context)

############################# LISTAR  RESERVAS     ##########################################################

# def listar_reservas_gastronomia(request):
#     context = {}
#     listado = ReservaRestaurante.objects.filter(usuario=request.user)
#     context['listado_reservas_gastronomia'] = listado

#     return render(request, 'Viajeros/paginas/mis_reservas_gastronomia.html', context)

# def listar_reservas_excursiones(request):
#     context = {}
#     listado = ReservaExcursion.objects.filter(usuario=request.user)
#     context['listado_reservas_excursiones'] = listado

#     return render(request, 'Viajeros/paginas/mis_reservas_excursiones.html', context)

#####################################################################
def listar_reservas(request):    
    if request.method == 'POST':
        formulario = ConsultaReservasForm(request.POST)
        if formulario.is_valid():
            seleccion = formulario.cleaned_data['seleccion']
            listado_hotel = Reservas.objects.filter(usuario=request.user)
            listado_restaurante = ReservaRestaurante.objects.filter(usuario=request.user)
            listado_excursion = ReservaExcursion.objects.filter(usuario=request.user)


            # Aquí puedes realizar las acciones correspondientes a cada selección
            if seleccion == 'hotel':
                # Lógica para la opción 1
                resultado = 'hotel'
            elif seleccion == 'restaurante':
                # Lógica para la opción 2
                resultado = 'restaurante'
            elif seleccion == 'excursion':
                # Lógica para la opción 3
                resultado = 'excursion'
            elif seleccion == 'todo':
                resultado = 'todo'
            
            print("seleccion = formulario.cleaned_data['seleccion']",resultado )
            context ={
                'listado_hotel' : listado_hotel,
                'listado_restaurante': listado_restaurante,
                'listado_excursion': listado_excursion,
                'formulario': formulario ,
                'resultado': resultado,

            }

            return render(request, 'Viajeros/paginas/mis_reservas.html', context )  #{'formulario': formulario, 'resultado': resultado, }
    else:
        formulario = ConsultaReservasForm()
        
    return render(request, 'Viajeros/paginas/mis_reservas.html', {'formulario': formulario})


###################################################################################

# @login_required
# def buscar_reservas(request):
#     context={}
#     listado_reservas = []

#     if request.method == "POST":
#         consulta_form = ConsultaReservasForm(request.POST)
#         if consulta_form.is_valid():
            
#             listado_reservas = Reservas.objects.filter(usuario=request.user)
#             context['listado_reservas'] = listado_reservas
#             #return render(request, "AppPoliconsultorio/turno_consulta.html", {'consulta_form': consulta_form })
#         else:
#             # print(turno_consulta_form.cleaned_data['fechaDesde'])
#             #messages.add_message(request, messages.WARNING, 'Debe ingresar un rango de fechas correcto, Fecha Desde <= Fechas Hasta', extra_tags="tag1")
#             return render(request, "Viajeros/paginas/buscar_reservas.html", {'consulta_form': consulta_form })
#             #print(request)
#     else:
#         consulta_form = ConsultaReservasForm()

#     context = {
#         "listado_reservas": listado_reservas,
#         "consulta_form": consulta_form,
#     }
#     return render(request, "Viajeros/paginas/buscar_reservas.html", context)




