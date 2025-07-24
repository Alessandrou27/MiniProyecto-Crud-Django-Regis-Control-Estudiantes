from django.urls import path
from .views import (
    EstudianteListView,
    EstudianteCreateView,
    EstudianteUpdateView,
    EstudianteDeleteView
)

urlpatterns = [
    path('', EstudianteListView.as_view(), name='estudiante_list'),
    path('nuevo/', EstudianteCreateView.as_view(), name='estudiante_create'),
    path('editar/<int:pk>/', EstudianteUpdateView.as_view(), name='estudiante_edit'),
    path('eliminar/<int:pk>/', EstudianteDeleteView.as_view(), name='estudiante_delete'),
]