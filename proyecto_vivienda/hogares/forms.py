from django import forms
from .models import Convocatoria

class SeleccionConvocatoriaForm(forms.Form):
    convocatoria = forms.ModelChoiceField(
        queryset=Convocatoria.objects.all(),
        empty_label="Selecciona una convocatoria",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
