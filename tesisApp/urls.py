from . import views
from . import signals
from django.urls import path

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('ingresaste/', views.ingresaste, name='ingresaste'),
    path('crear_usuario_empleado/', views.crear_usuario_empleado, name='crear_usuario_empleado'),
    path('usuariocreado/', views.usuariocreado, name='usuariocreado'),
    path('cambioprecio/', views.modificar_precio, name='cambioprecio_sin_id'),
    path('cambioprecio/<int:IdHormigon>/', views.modificar_precio, name='cambioprecio'),
    path('correoRec/', views.correoRec, name='correoRec'),
    path('nuevaContrasena', views.nuevaContrasena, name='nuevaContrasena'),
    path('cargaPedidos', views.cargaPedidos, name='cargaPedidos'),
    path('consulta', views.consulta, name='consulta'),
    path('ubicacionPedido', views.ubicacionPedido, name="ubicacionPedido"),
    path('asignacionModulos', views.asignacionModulos, name="asignacionModulos"),
    path('calendarioPedidos', views.calendarioPedidos, name="calendarioPedidos"),
    path('informes', views.informes, name="informes"),
    path('enviarCod', views.enviarCod, name='enviarCod'),
    path('verificarCod', views.verificarCod, name='verificarCod'),
    path('actualizarPass', views.actualizarPass, name='actualizarPass'),
    path('inicioVentas', views.inicio, name="inicioVentas"),
    path('inicioGerente', views.inicioGerente, name="inicioGerente"),
    path('inicioPlantista', views.inicioPlantista, name="inicioPlantista"),
    path('inicioAdministracion', views.inicioAdministracion, name="inicioAdministracion")

]



