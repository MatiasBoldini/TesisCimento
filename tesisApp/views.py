from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Obra, Hormigon, Pedido, Empleado
from django.db import models
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from .authentication import authenticate_by_dni
from django.contrib.auth.models import User
from. import forms
from .forms import ModificarPrecioForm



def home(request):
    context = {}
    return render(request, "tesisApp/login.html", context)


def ingresaste(request):
    context = {}
    return render(request, 'tesisApp/ingresaste.html', context)


def login_view(request):
    if request.method == 'POST':
        dni = request.POST.get('dni')
        password = request.POST.get('password')
        user = authenticate_by_dni(dni, password)
        
        if user:
            auth_login(request, user)
            return redirect('ingresaste')
        else:
            message = "Error: Las credenciales son inválidas"
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def usuariocreado(request):
    context = {}
    return render(request, 'tesisApp/usuariocreado.html', context)


def crear_usuario_empleado(request):
    if request.method == 'POST':
        try:
         
            username = request.POST.get('username')
            password = request.POST.get('password')
            rol = int(request.POST.get('rol'))
            dni = request.POST.get('dni')
            nombre = request.POST.get('nombre')
            apellido = request.POST.get('apellido')
            email = request.POST.get('email')
            telefono = request.POST.get('telefono')

         
            nuevo_usuario = User.objects.create_user(username=username, password=password)

          
            if nuevo_usuario:
               
                nuevo_empleado = Empleado(DNI=dni, user=nuevo_usuario, rol=rol, nombre=nombre, apellido=apellido, email=email, telefono=telefono)
                nuevo_empleado.save()

                return redirect('ingresaste')
            else:
                return render(request, 'usuariocreado.html')
        except Exception as e:
            print("Error:", e)  
            return render(request, 'usuariocreado.html')
    else:
        return render(request, 'usuariocreado.html')


def modificar_precio(request, IdHormigon=None):
    hormigon = None

    if IdHormigon:
        
        hormigon = get_object_or_404(Hormigon, IdHormigon=IdHormigon)

    exito = False

    if request.method == 'POST':
        form = ModificarPrecioForm(request.POST)
        if form.is_valid():
            nuevo_precio = form.cleaned_data['nuevo_precio']

            if hormigon:
              
                hormigon.precio = nuevo_precio
                hormigon.save()
                exito = True
            else:
               
                nuevo_hormigon_nombre = form.cleaned_data['nuevo_hormigon_nombre']
                hormigones = Hormigon.objects.filter(nombre=nuevo_hormigon_nombre)

             
                for h in hormigones:
                    h.precio = nuevo_precio
                    h.save()

                exito = True

    else:
        form = ModificarPrecioForm()

    return render(request, 'tesisApp/cambioprecio.html', {'form': form, 'hormigon': hormigon, 'exito': exito})


def correRec(request):
    context = {}
    return render(request, "tesisApp/correoRec.html", context)

def nuevaContrasena(request):
    context = {}
    return render(request, "tesisApp/nuevaContrasena.html", context)



##def crear_pedido(request):
    IdPedido = models.AutoField(primary_key=True)
    # Obtén el cliente, obra y otros datos necesarios para crear el pedido
    cliente = Cliente.objects.get(id=1)  # Reemplaza con la lógica adecuada para obtener el cliente
    obra = Obra.objects.get(id=1)  # Reemplaza con la lógica adecuada para obtener la obra
    cantidad_m3 = 5  # Ejemplo de cantidad_m3, reemplaza con el valor adecuado

    # Crea una instancia de Pedido con el estado 'Pendiente'
    pedido = Pedido(
        DNICliente=cliente,
        IdObra=obra,
        CantidadM3=cantidad_m3,
        EstadoPedido='Pendiente'  # Puedes configurar el estado deseado aquí
    )

    # Realiza cualquier otro cálculo necesario en función de los datos proporcionados
    # Por ejemplo, puedes calcular NombreyApellidoCliente y ValorTotal aquí

    pedido.save()  # Guarda el objeto Pedido en la base de datos

    return redirect('detalle_pedido', pedido_id=pedido.IdPedido)  # Redirige a la vista de detalle del pedido


