from django import forms
from .models import Inscripcion, Postulacion

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'

class ConvocatoriaForm(forms.ModelForm):  # Cambio de forms.Form a forms.ModelForm
    class Meta:
        model = Postulacion  # Asignado al modelo correcto
        fields = ['nombre', 'correo', 'telefono', 'direccion', 'medio_transporte', 'predio_suelo', 'descripcion_llegada']
        widgets = {
            'descripcion_llegada': forms.Textarea(attrs={'rows': 3}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

from .models import Postulacion

class PostulacionForm(forms.ModelForm):
    class Meta:
        model = Postulacion
        fields = '__all__'
