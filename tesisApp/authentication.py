from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from tesisApp.models import Empleado

def authenticate_by_dni(dni, password):
    user = User.objects.filter(empleado__DNI=dni).first()
    
    if user:
        user = authenticate(username=user.username, password=password)

    return user