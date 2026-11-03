from rest_framework import serializers
from .models import Curso
from datetime import date


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'descripcion', 'instructor', 'correo_instructor',
                  'categoria', 'nivel', 'duracion_horas', 'precio', 'anio']

    def validate_nombre(self, value):
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError('El nombre debe tener al menos 3 caracteres.')
        qs = Curso.objects.filter(nombre__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('Ya existe un curso con ese nombre.')
        return value

    def validate_duracion_horas(self, value):
        if value <= 0:
            raise serializers.ValidationError('La duración debe ser mayor que cero.')
        if value > 500:
            raise serializers.ValidationError('La duración no puede superar las 500 horas.')
        return value

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError('El precio debe ser mayor que cero.')
        return value

    def validate_anio(self, value):
        actual = date.today().year
        if value < 2000 or value > actual + 1:
            raise serializers.ValidationError(f'El año debe estar entre 2000 y {actual + 1}.')
        return value