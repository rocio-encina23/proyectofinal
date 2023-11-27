from django.test import TestCase

from recetas.models import Curso


class CursoTests(TestCase):
    
    def test_creacion_curso(self):
        # caso uso esperado
        curso = Curso(nombre="Titulo")
        curso.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Curso.objects.count(), 1)
        self.assertEqual(curso.nombre, "Titulo")
        

    def test_curso_str(self):
        curso = Curso(nombre="Panaderia")
        curso.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(curso.__str__(), "Panaderia")