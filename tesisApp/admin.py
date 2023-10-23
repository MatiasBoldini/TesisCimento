from django.contrib import admin

from .models import Cliente, Obra, Hormigon, Pedido, Modulo, Empleado

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Obra)
admin.site.register(Hormigon)
admin.site.register(Pedido)
admin.site.register(Modulo)
admin.site.register(Empleado)

