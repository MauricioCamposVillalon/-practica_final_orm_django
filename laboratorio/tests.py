from django.test import TestCase
from .models import Laboratorio
from django.urls import reverse

class LaboratorioTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(nombre='Lab 1', ciudad='Ciudad 1', pais='País 1')

    def test_laboratorio_content(self):
        self.assertEqual(self.laboratorio.nombre, 'Lab 1')

    def test_laboratorio_list_view(self):
        response = self.client.get(reverse('laboratorio_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/lista.html')

    def test_laboratorio_detail_view(self):
        response = self.client.get(reverse('laboratorio_editar', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)

