from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Tarefa


def index(request):
    if request.method == "POST":
        tarefa = Tarefa(texto_tarefa=request.POST['texto_tarefa'], concluida=False)
        tarefa.save()
        return redirect('/tarefas')
    elif request.method == "GET":
        lista_tarefas = Tarefa.objects.order_by('-data_criacao').filter(concluida='False')
        return render(request, 'tarefas/index.html', {'lista_tarefas': lista_tarefas})

def deletar(request, id):
    tarefa = Tarefa.objects.get(id=id)
    tarefa.delete()
    return redirect('/tarefas')
