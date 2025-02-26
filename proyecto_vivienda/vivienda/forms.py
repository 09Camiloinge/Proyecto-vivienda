from django import forms
from .models import Hogar

class HogarForm(forms.ModelForm):
    class Meta:
        model = Hogar
        fields = '__all__'
        labels = {
            'calificacion': 'Calificación',
            'fecha_postulacion': 'Fecha de Postulación',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'tipo_documento': 'Tipo de Documento',
            'num_documento': 'Número de Documento',
            'estado_civil': 'Estado Civil',
            'sexo': 'Sexo',
            'radicado': 'Radicado',
            'estado_postulacion': 'Estado de Postulación',
            'ingresos': 'Ingresos',
            'trabajo': 'Trabajo',
            'direccion': 'Dirección',
            'barrio': 'Barrio',
            'email': 'Correo Electrónico',
            'telefono_celular': 'Teléfono Celular',
            'telefono_fijo': 'Teléfono Fijo',
            'estrato': 'Estrato',
            'total_ingresos_nucleo': 'Total Ingresos del Núcleo',
            'tiempo_residencia': 'Tiempo de Residencia (años)',
            'puntaje_sisben': 'Puntaje SISBÉN',
            'sistema_salud': 'Sistema de Salud',
            'caja_compensacion': 'Caja de Compensación',
            'fondo_cesantias': 'Fondo de Cesantías',
            'valor_cesantias': 'Valor de Cesantías',
            'tiene_ahorros': '¿Tiene Ahorros?',
            'entidad_ahorro_programado': 'Entidad de Ahorro Programado',
            'valor_ahorro_programado': 'Valor de Ahorro Programado',
            'reportado_centrales_riesgo': '¿Reportado en Centrales de Riesgo?',
            'tiene_subsidio': '¿Tiene Subsidio?',
            'subsidio': 'Subsidio',
            'credito_hipotecario': '¿Tiene Crédito Hipotecario?',
            'valor_credito_hipotecario': 'Valor Crédito Hipotecario',
            'mi_casa_ya': '¿Aplica para Mi Casa Ya?',
            'valor_mi_casa_ya': 'Valor Mi Casa Ya',
            'empresa': 'Empresa',
            'direccion_empresa': 'Dirección Empresa',
            'barrio_empresa': 'Barrio Empresa',
            'estado': 'Estado',
            'motivo': 'Motivo',
        }
        widgets = {
            'fecha_postulacion': forms.DateInput(attrs={'type': 'date'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'estado_civil': forms.Select(choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('union_libre', 'Unión Libre')]),
            'sexo': forms.Select(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')]),
            'tiene_ahorros': forms.CheckboxInput(),
            'tiene_subsidio': forms.CheckboxInput(),
            'credito_hipotecario': forms.CheckboxInput(),
            'mi_casa_ya': forms.CheckboxInput(),}