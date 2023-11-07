from django.shortcuts import render, redirect
from .models import Cliente, Obra, Hormigon, Pedido, Empleado
from django.db import models
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from .authentication import authenticate_by_dni


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
            auth_login(request, user)  # Cambia el nombre de la función de inicio de sesión
            return redirect('ingresaste')
        else:
            message = "Error: Las credenciales son inválidas"
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


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


