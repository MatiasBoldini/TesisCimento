from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Obra, Hormigon, Pedido, Empleado
from django.db import models
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect
from .authentication import authenticate_by_dni
from django.contrib.auth.models import User
from. import forms
from .forms import ModificarPrecioForm

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.shortcuts import render
import random




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
            return redirect('ingresaste') #modificar esto
        else:
            print('-------ERROR EN EL INICIO DE SESION-----------')
            message = "Los datos ingresados son incorrectos."
            return render(request, 'tesisApp/login.html', {'message': message})

    return render(request, 'tesisApp/login.html')


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

         
            nuevo_usuario = User.objects.create_user(username=username, password=password, email=email)

          
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








def correoRec(request):
    context = {}
    return render(request, "tesisApp/correoRec.html", context)

    

def generar_codigo_verificacion():
    # Generar un código aleatorio de 4 dígitos
    return ''.join(str(random.randint(0, 9)) for _ in range(4))


def enviar_email(email, codigo):
    # Configuración del servidor SMTP de Gmail
    servidor_smtp = 'smtp.gmail.com'
    puerto = 587
    usuario = 'testnodemailer112@gmail.com'
    clave = 'gbyz hjcd qdde tksf'

    # Crear mensaje MIME
    mensaje = MIMEMultipart()
    mensaje['From'] = 'testnodemailer112@gmail.com'
    mensaje['To'] = email
    mensaje['Subject'] = 'Código de Recuperación | Hormigones Cimento'
    cuerpo = f'Su código de recuperación de contraseña para la web de Hormigones Cimento es: {codigo}'
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        # Establecer conexión con el servidor SMTP y enviar el mensaje
        with smtplib.SMTP(servidor_smtp, puerto) as servidor:
            servidor.starttls()
            servidor.login(usuario, clave)
            servidor.send_message(mensaje)

        return True

    except smtplib.SMTPException as e:
        print(f'Error al enviar el correo: {e}')
        return False



def enviarCod(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Almacenar el email en una variable de sesion
        request.session['email_verificacion'] = email

        # Generar un código de verificación aleatorio
        codigo_verificacion = generar_codigo_verificacion()

        print(codigo_verificacion)

        # Almacenar el código en una variable de sesion
        request.session['codigo_verificacion'] = codigo_verificacion

        # Enviar el código de verificación por correo electrónico
        
        #return render(request, 'tesisApp/codigoVerificacion.html', {'email': email})

        # Para las pruebas, comentar las lineas siguientes
        exito = enviar_email(email, codigo_verificacion)
        if exito: #Si exito es True (el mail se envia correctamente)
            return render(request, 'tesisApp/codigoVerificacion.html', {'email': email})
        else:
            return render(request, 'tesisApp/correoRec.html') 

    else:
        return redirect('home')



def verificarCod(request):
    if request.method == 'POST':
        letra1 = request.POST.get('input1')
        letra2 = request.POST.get('input2')
        letra3 = request.POST.get('input3')
        letra4 = request.POST.get('input4')

        codigoRecibido = letra1 + letra2 + letra3 + letra4

        # Obtener el código de verificación almacenado en la sesión
        codigo_verificacion_guardado = request.session.get('codigo_verificacion')

        # Comparar el código ingresado con el código almacenado
        if codigo_verificacion_guardado and codigoRecibido == codigo_verificacion_guardado:
            del request.session['codigo_verificacion'] 
            return render(request, 'tesisApp/nuevaContrasena.html')
        else:
            mensaje = 'El código de recuperación ingresado es incorrecto'
            return render(request, 'tesisApp/codigoVerificacion.html', {'message': mensaje})
    else:
        return redirect('home')




def actualizarPass(request):
    if request.method == 'POST':

        contra1 = request.POST.get('password')
        contra2 = request.POST.get('password-repeat')

        if contra1 == contra2:
            email_verificacion_guardado = request.session.get('email_verificacion')
            usuario = User.objects.get(email=email_verificacion_guardado)

            nueva_contrasena = contra1
            usuario.set_password(nueva_contrasena)
            usuario.save()    

            print(f'el email al que se le va a cambiar la contraseña es {email_verificacion_guardado}')
            del request.session['email_verificacion']
            return redirect('ingresaste')
        else:
            mensaje = 'Las contraseñas no coinciden. Por favor verifique los datos ingresados.'
            return render(request, 'tesisApp/nuevaContrasena.html', {'message': mensaje})
            
    else:
        return redirect('home')




def nuevaContrasena(request):
    context = {}
    return render(request, "tesisApp/nuevaContrasena.html", context)


def cargaPedidos(request):
    context= {}
    return render(request, "tesisApp/cargaPedidos.html")

def consulta(request):
    context = {}
    return render(request, "tesisApp/consulta.html")

def ubicacionPedido(request):
    context = {}
    return render(request, "tesisApp/ubicacionPedido.html")

def asignacionModulos(request):
    context = {}
    return render(request, "tesisApp/asignacionModulos.html")

def inicio(request):
    context = {}
    return render(request, "tesisApp/inicioVentas.html")

def inicioGerente(request):
    context = {}
    return render (request, "tesisApp/inicioGerente.html")

def inicioPlantista(request):
    context = {}
    return render (request, "tesisApp/inicioPlantista.html")

def inicioAdministracion(request):
    context = {}
    return render (request, "tesisApp/inicioAdministracion.html")



# def calendarioPedidos(request):
    
#     pedidos = Pedido.objects.all()
#     #pedidos = Pedido.objects.filter(FechaDeEntrega='2024-01-04')

#     if pedidos:
#         # Imprimir información sobre los pedidos en la consola
#         print(f'--- Hay pedidos disponibles. --- \n' )
        
#     else:
#         print(f'--- No hay pedidos disponibles. --- \n' )
#     # Renderizar la plantilla 'grilla_pedidos.html' con la lista de pedidos
#     return render(request, 'tesisApp/calendarioPedidos.html', {'pedidos': pedidos})



def calendarioPedidos(request):
    if request.method == 'POST':
        # Obtener la fecha del cuerpo de la solicitud
        formattedDate = request.POST.get('fecha', None)

        if formattedDate:
            # Realizar operaciones con la fecha
            pedidos = Pedido.objects.filter(FechaDeEntrega=formattedDate)

            if pedidos:
                # Imprimir información sobre los pedidos en la consola del servidor
                print(f'--- Hay pedidos disponibles para la fecha {formattedDate}. --- \n')
            else:
                print(f'--- No hay pedidos disponibles para la fecha {formattedDate}. --- \n')

            
            return render(request, 'tesisApp/calendarioPedidos.html', {'pedidos': pedidos})
        else:
            # Si no se proporciona la fecha, devolver un error
            print('Error en la seleccion de fecha')
    else:
        print('Error en la seleccion de fecha')
        pedidos = Pedido.objects.all()
        return render(request, 'tesisApp/calendarioPedidos.html', {'pedidos': pedidos})




def informes(request):
    context = {}
    return render(request, "tesisApp/informes.html")


# def crear_pedido(request):
#     IdPedido = models.AutoField(primary_key=True)

#     # Obtén el cliente, obra y otros datos necesarios para crear el pedido
#     cliente = Cliente.objects.get(id=1)  # Reemplaza con la lógica adecuada para obtener el cliente
#     obra = Obra.objects.get(id=1)  # Reemplaza con la lógica adecuada para obtener la obra
#     cantidad_m3 = 5  # Ejemplo de cantidad_m3, reemplaza con el valor adecuado

#     # Crea una instancia de Pedido con el estado 'Pendiente'
#     pedido = Pedido(
#         DNICliente=cliente,
#         IdObra=obra,
#         CantidadM3=cantidad_m3,
#         EstadoPedido='Pendiente'  # Puedes configurar el estado deseado aquí
#     )

#     # Realiza cualquier otro cálculo necesario en función de los datos proporcionados
#     # Por ejemplo, puedes calcular NombreyApellidoCliente y ValorTotal aquí

#     pedido.save()  # Guarda el objeto Pedido en la base de datos

#     return redirect('detalle_pedido', pedido_id=pedido.IdPedido)  # Redirige a la vista de detalle del pedido


