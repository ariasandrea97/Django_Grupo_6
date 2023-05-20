from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

#
from .models import Reservas, User
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic.list import ListView


#Definicion de los formularios:
from .forms import EnviarReservaForm, AltaUsuarioForm



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


#########################################################
def enviar_consulta(request):    # guarda reserva en la tabla Reservas
    context={}
    if request.method == "POST":
        form = EnviarReservaForm(request.POST)
        if form.is_valid():
            print(request.user)
            alta_reserva = form.save(commit=False)
            alta_reserva.usuario= request.user
            alta_reserva.save()  #guardamos la reserva
            # form.save()
            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")
            return render(request, 'Viajeros/index.html', context)

    else:
        # GET
        form = EnviarReservaForm()

    context = {'form': form}
    return render(request, 'Viajeros/paginas/enviar_consulta.html', context)





# #################################
def registro(request):     # Para el alta de un usuario
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


#################################
##
def logout_request(request):
    logout(request)
    messages.info(request,"Sesion finalizada")
    return render(request, 'Viajeros/index.html') 

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


# class listar_reservas(ListView):
#     model= Reservas
#     context_object_name= 'Mis_Reservas'
#     template_name='Viajeros/paginas/mis_reservas.html'
#     ordering=['id']


def listar_reservas(request):
    context = {}

    listado = Reservas.objects.all()

    context['listado_reservas'] = listado

    return render(request, 'Viajeros/paginas/mis_reservas.html', context)


def mi_cuenta(request):
    context = {}

    # listado = User.objects.all()

    # context['listado_user'] = listado

    return render(request, 'Viajeros/paginas/mi_cuenta.html', context)