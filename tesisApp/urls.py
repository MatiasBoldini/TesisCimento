from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('ingresaste/', views.ingresaste, name='ingresaste'),
]



