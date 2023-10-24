from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

#Aqui van los modelos de las clases de la base de datos.


ESTADO_PEDIDO_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('Preparacion', 'Preparación'),
    ('Cancelado', 'Cancelado'),
    ('EnCamino', 'En Camino'),
    ('Entregado', 'Entregado'),
]


class Modulo(models.Model):
    IdModulos = models.AutoField(primary_key=True)  # Clave primaria automática
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Empleado(models.Model):
    DNI = models.CharField(primary_key=True, max_length=15)  # Clave primaria
    IdModulos = models.ForeignKey(Modulo, on_delete=models.CASCADE)  # Clave foránea
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    clave = models.CharField(max_length=20)

    def set_password(self, password):
        self.clave = make_password(password)

    def check_password(self, password):
        return check_password(password, self.clave)

class Cliente(models.Model):
    DNICliente = models.CharField(primary_key=True, max_length=15)  # Clave primaria
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    historial_cliente = models.TextField()
    anotaciones = models.TextField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    

class Obra(models.Model):
    IdObra = models.AutoField(primary_key=True)  # Clave primaria automática
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class Hormigon(models.Model):
    IdHormigon = models.AutoField(primary_key=True)  # Clave primaria automática
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para precio

    def __str__(self):
        return self.nombre
    

class Pedido(models.Model):
    IdPedido = models.AutoField(primary_key=True)  # Configura la clave primaria para que se genere automáticamente
    DNICliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    NombreyApellidoCliente = models.CharField(max_length=200, editable=False)
    IdObra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    FechaDeEntrega = models.DateField()
    Hormigones = models.ManyToManyField('Hormigon')
    CantidadM3 = models.DecimalField(max_digits=10, decimal_places=2)
    EstadoPedido = models.CharField(max_length=50, choices=ESTADO_PEDIDO_CHOICES, default='Pendiente')


    def save(self, *args, **kwargs):
        self.NombreyApellidoCliente = f'{self.DNICliente.nombre} {self.DNICliente.apellido}'
        super(Pedido, self).save(*args, **kwargs)

    def calcular_valor_total(self):
        valor_total = sum(hormigon.precio * self.CantidadM3 for hormigon in self.Hormigones.all())
        return valor_total

    def __str__(self):
        return f'Pedido {self.IdPedido} - Cliente: {self.NombreyApellidoCliente}'