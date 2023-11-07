from django.apps import AppConfig

class TesisappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tesisApp'

    def ready(self):
        try:
            from . import signals  # Importa tus señales aquí desde el mismo directorio
        except ImportError:
            pass
