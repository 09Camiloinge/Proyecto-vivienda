from django import forms
from .models import Hogar, Miembro

class HogarForm(forms.ModelForm):
    class Meta:
        model = Hogar
        fields = ['jefe_hogar', 'direccion', 'anos_residencia']

class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['hogar', 'nombre', 'es_victima', 'es_discapacitado', 'edad']
