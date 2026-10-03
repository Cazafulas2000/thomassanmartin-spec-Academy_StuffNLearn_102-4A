from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Curso
from .forms import CursoCrearForm


def inicio(request):
    total = Curso.objects.count()
    ultimos = Curso.objects.order_by('-id')[:3]
    return render(request, 'cursos/inicio.html', {'total': total, 'ultimos': ultimos})


def lista_cursos(request):
    cursos = Curso.objects.all().order_by('nombre')
    return render(request, 'cursos/lista.html', {'cursos': cursos})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoCrearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso creado correctamente.')
            return redirect('lista_cursos')
    else:
        form = CursoCrearForm()
    return render(request, 'cursos/crear.html', {'form': form})
