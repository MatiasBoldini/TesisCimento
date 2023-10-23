from django.shortcuts import render, redirect
from .models import Cliente, Obra, Hormigon, Pedido, Modulo, Empleado
from django.db import models


def home(request):
    context = {}
    return render(request, "tesisApp/home.html", context)


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