from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'carrera', 'ciclo', 'correo']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not nombre.replace(' ', '').isalpha():
            raise forms.ValidationError('El nombre solo debe contener letras.')
        return nombre

    def clean_carrera(self):
        carrera = self.cleaned_data['carrera']
        if not carrera.replace(' ', '').isalpha():
            raise forms.ValidationError('La carrera solo debe contener letras.')
        return carrera

    def clean_ciclo(self):
        ciclo = self.cleaned_data['ciclo']
        if not ciclo.isdigit():
            raise forms.ValidationError('El ciclo solo debe contener números.')
        if len(ciclo) > 2:
            raise forms.ValidationError('El ciclo debe tener máximo 2 dígitos.')
        return ciclo 