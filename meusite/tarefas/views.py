from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.

def tarefas_home(request):
    return HttpResponse("<h1>Bem-vindo à página de tarefas!</h1>")

def tarefas_adicionar(request):
    return HttpResponse("<h1>Adicionar uma nova tarefa</h1>")

def tarefas_editar(request, id):
    return HttpResponse(f"<h1>Editar a tarefa com ID: {id}</h1>")

def tarefas_excluir(request, id):
    return HttpResponse(f"<h1>Excluir a tarefa com ID: {id}</h1>")
