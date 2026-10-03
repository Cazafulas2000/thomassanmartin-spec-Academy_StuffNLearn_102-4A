from django.db import models


class Curso(models.Model):
    CATEGORIAS = [
        ('programacion', 'Programación'),
        ('diseno', 'Diseño'),
        ('idiomas', 'Idiomas'),
        ('marketing', 'Marketing'),
        ('negocios', 'Negocios'),
        ('otro', 'Otro'),
    ]

    NIVELES = [
        ('basico', 'Básico'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    instructor = models.CharField(max_length=100)
    correo_instructor = models.EmailField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    nivel = models.CharField(max_length=20, choices=NIVELES)
    duracion_horas = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    anio = models.IntegerField()

    def __str__(self):
        return self.nombre
