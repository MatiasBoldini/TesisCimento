from django import forms

class ModificarPrecioForm(forms.Form):
    nuevo_hormigon_nombre = forms.CharField(max_length=100)
    nuevo_precio = forms.DecimalField(max_digits=10, decimal_places=2)
