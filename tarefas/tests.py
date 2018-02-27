from django.test import TestCase
from django.urls import reverse
from .models import Tarefa
# Create your tests here.


def criar_tarefa(texto_tarefa):
    return Tarefa(texto_tarefa=texto_tarefa, concluida=False)

class TarefaIndexViewTestes(TestCase):
    def test_nenhuma_tarefa(self):
        response = self.client.get(reverse('tarefas:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nenhuma Tarefa")
        self.assertQuerysetEqual(response.context['lista_tarefas'], [])

    def test_add_tarefa(self):
        self.client.post(reverse('tarefas:index'), {'texto_tarefa': 'Tarefa 1'})
        response = self.client.get(reverse('tarefas:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tarefa 1")
