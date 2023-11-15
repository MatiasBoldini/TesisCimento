from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Hormigon, RegistroPrecio
from django.core.exceptions import ObjectDoesNotExist

@receiver(pre_save, sender=Hormigon)
def registro_cambio_precio(sender, instance, **kwargs):
    if instance.pk:  # Verificar si es una actualización
        try:
            hormigon = sender.objects.get(pk=instance.pk)
        except ObjectDoesNotExist:
            return  # Si no se encuentra el objeto, salir sin hacer nada
        
        if hormigon.precio != instance.precio:
            RegistroPrecio.objects.create(
                hormigon=hormigon,
                precio_anterior=hormigon.precio,
                nuevo_precio=instance.precio
            )