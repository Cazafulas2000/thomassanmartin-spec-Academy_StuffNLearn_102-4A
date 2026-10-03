from datetime import date
from django import forms
from .models import Curso


class CursoCrearForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'instructor', 'correo_instructor', 'categoria', 'nivel', 'duracion_horas', 'precio', 'anio']
        labels = {
            'nombre': 'Nombre del curso',
            'descripcion': 'Descripción',
            'instructor': 'Instructor',
            'correo_instructor': 'Correo del instructor',
            'categoria': 'Categoría',
            'nivel': 'Nivel',
            'duracion_horas': 'Duración (horas)',
            'precio': 'Precio (CLP)',
            'anio': 'Año',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'instructor': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_instructor': forms.EmailInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'nivel': forms.Select(attrs={'class': 'form-select'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        if Curso.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError('Ya existe un curso con ese nombre.')
        return nombre

    def clean_duracion_horas(self):
        duracion = self.cleaned_data['duracion_horas']
        if duracion <= 0:
            raise forms.ValidationError('La duración debe ser mayor que cero.')
        if duracion > 500:
            raise forms.ValidationError('La duración no puede superar las 500 horas.')
        return duracion

    def clean_precio(self):
        precio = self.cleaned_data['precio']
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio

    def clean_anio(self):
        anio = self.cleaned_data['anio']
        actual = date.today().year
        if anio < 2000 or anio > actual + 1:
            raise forms.ValidationError('El año debe estar entre 2000 y ' + str(actual + 1) + '.')
        return anio
