from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import connection
from .models import Estudiante
from .forms import EstudianteForm

# Mostrar lista de estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_list.html'
    context_object_name = 'estudiantes'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nombre__icontains=q)
        return queryset

# Crear nuevo estudiante
class EstudianteCreateView(CreateView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_form.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('estudiante_list')

# Editar estudiante
class EstudianteUpdateView(UpdateView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_form.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('estudiante_list')

# Eliminar estudiante
class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'estudiantes/estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante_list')

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        
        if Estudiante.objects.count() == 0:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='estudiantes_estudiante';")
                cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name='estudiantes_estudiante';")
                cursor.execute("INSERT OR IGNORE INTO sqlite_sequence (name, seq) VALUES ('estudiantes_estudiante', 0);")
        
        return response