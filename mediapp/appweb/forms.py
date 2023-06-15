from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__" #muestra todos los campos del modelo en el formulario