from django import forms
from .models import Inscripcion
from .models import Convocatoria

class ConvocatoriaForm(forms.ModelForm):
    class Meta:
        model = Convocatoria
        fields = ['nombre', 'descripcion']

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['nombre', 'correo', 'telefono']