from django.test import TestCase
from .models import Estudiante

class EstudianteModelTest(TestCase):
    def test_crear_estudiante(self):
        estudiante = Estudiante.objects.create(
            nombre="Juan Pérez",
            carrera="Ingeniería de Sistemas",
            ciclo="3",
            correo="juan.perez@email.com"
        )
        self.assertEqual(estudiante.nombre, "Juan Pérez")
        self.assertEqual(estudiante.carrera, "Ingeniería de Sistemas")
        self.assertEqual(estudiante.ciclo, "3")
        self.assertEqual(estudiante.correo, "juan.perez@email.com") 