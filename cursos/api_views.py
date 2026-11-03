from rest_framework import viewsets
from .models import Curso
from .serializers import CursoSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('nombre')
    serializer_class = CursoSerializer