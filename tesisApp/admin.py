from django.contrib import admin

from .models import Cliente, Obra, Hormigon, Pedido, Empleado

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Obra)
admin.site.register(Hormigon)
admin.site.register(Pedido)
admin.site.register(Empleado)

