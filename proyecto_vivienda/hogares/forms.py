from django import forms
from .models import Inscripcion 
from .models import Postulacion

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'


class ConvocatoriaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(widget=forms.Textarea, required=True)
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)

class PostulacionForm(forms.Form):
    numero_documento = forms.IntegerField(
        label="Número de Documento", required=True, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    nombres = forms.CharField(
        max_length=50, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    apellidos = forms.CharField(
        max_length=50, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    correo = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    telefono = forms.CharField(
        max_length=15, required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    genero = forms.ChoiceField(
        choices=[('M', 'Masculino'), ('F', 'Femenino'), ('Otro', 'Otro')], 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    estado_civil = forms.ChoiceField(
        choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Unión Libre', 'Unión Libre')], 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    departamento = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    ciudad = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tipo_vinculacion = forms.ChoiceField(
        choices=[('Empleado', 'Empleado'), ('Independiente', 'Independiente'), ('Otro', 'Otro')], 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    ingresos = forms.IntegerField(
        label="Ingresos Mensuales", required=True, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    egresos = forms.IntegerField(
        label="Egresos Mensuales", required=True, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    tipo_vivienda = forms.ChoiceField(
        choices=[('Propia', 'Propia'), ('Arrendada', 'Arrendada'), ('Familiar', 'Familiar')], 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    numero_habitantes = forms.IntegerField(
        label="Número de Habitantes en la Vivienda", required=True, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )