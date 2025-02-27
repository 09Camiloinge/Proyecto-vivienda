from django import forms

class ConvocatoriaForm(forms.Form):
    CONVOCATORIAS = [
        ('convocatoria_1', 'Convocatoria 1'),
        ('convocatoria_2', 'Convocatoria 2'),
        ('convocatoria_3', 'Convocatoria 3'),
        ('convocatoria_4', 'Convocatoria 4'),
    ]
    convocatoria = forms.ChoiceField(
        choices=CONVOCATORIAS,
        label='Seleccionar convocatoria',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
