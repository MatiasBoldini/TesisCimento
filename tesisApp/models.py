from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

#Aqui van los modelos de las clases de la base de datos.


ESTADO_PEDIDO_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('Preparacion', 'Preparación'),
    ('Cancelado', 'Cancelado'),
    ('EnCamino', 'En Camino'),
    ('Entregado', 'Entregado'),
]

ROLES = (
    (0, 'Gerente'),
    (1, 'Logística'),
    (2, 'Plantista'),
    (3, 'Transportista'),
    (4, 'Administracion'),
)
    

class Empleado(models.Model):
    DNI = models.CharField(primary_key=True, max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.IntegerField(choices=ROLES)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def set_password(self, password):
        self.clave = make_password(password)

    def check_password(self, password):
        return check_password(password, self.clave)


class Cliente(models.Model):
    DNICliente = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)


    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Obra(models.Model):
    IdObra = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    direccion = models.CharField(max_length=150)
    

    def __str__(self):
        return self.nombre
    

class Hormigon(models.Model):
    IdHormigon = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if self.pk:  
            old_hormigon = Hormigon.objects.get(pk=self.pk)
            if old_hormigon.precio != self.precio:
                registro_precio = RegistroPrecioHormigon(hormigon=old_hormigon, precio_anterior=old_hormigon.precio, precio_nuevo=self.precio)
                registro_precio.save() 
        return super(Hormigon, self).save(*args, **kwargs)


class RegistroPrecioHormigon(models.Model):
    hormigon = models.ForeignKey(Hormigon, on_delete=models.CASCADE)
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2)
    precio_nuevo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.pk is not None:  
            old_price = RegistroPrecioHormigon.objects.get(pk=self.pk).precio_nuevo
            self.precio_anterior = old_price
        return super(RegistroPrecioHormigon, self).save(*args, **kwargs)


class Pedido(models.Model):
    IdPedido = models.AutoField(primary_key=True)
    DNICliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    IdObra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    FechaDeEntrega = models.DateField()
    Hormigones = models.ManyToManyField('Hormigon')
    CantidadM3 = models.DecimalField(max_digits=10, decimal_places=2)
    EstadoPedido = models.CharField(max_length=50, choices=ESTADO_PEDIDO_CHOICES, default='Pendiente')

    def calcular_valor_total(self):
        valor_total = sum(hormigon.precio * self.CantidadM3 for hormigon in self.Hormigones.all())
        return valor_total

    def __str__(self):
        return f'Pedido {self.IdPedido} - Cliente: {self.NombreyApellidoCliente}'
