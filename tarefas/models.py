from django.db import models

# Create your models here.

class Tarefa(models.Model):
    texto_tarefa = models.CharField(max_length=200)
    data_criacao = models.DateTimeField('Data de Criação', auto_now=True)
    concluida = models.BooleanField()
    data_conclusao = models.DateTimeField('Concluído em: ', null=True, blank=True)
