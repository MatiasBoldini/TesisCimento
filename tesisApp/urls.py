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
    path('correoRec/', views.correRec, name='correoRec'),
    path('nuevaContrasena', views.nuevaContrasena, name='nuevaContrasena'),
    path('codigoVerificacion', views.codigoVerificacion, name='codigoVerificacion'),
    path('cargaPedidos', views.cargaPedidos, name='cargaPedidos'),
    path('consulta', views.consulta, name='consulta'),
    path('ubicacionPedido', views.ubicacionPedido, name="ubicacionPediedo")
]



