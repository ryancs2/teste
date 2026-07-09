from django.shortcuts import render

# Create your views here.

def tarefas_home(request):
    contexto = {
        'nome': 'Ryan'
    }
    return render(request, 'pagetarefas/home.html', contexto)

def tarefas_adicionar(request):
    return render(request, 'pagetarefas/adicionar.html')

def tarefas_editar(request):
    return render(request, 'pagetarefas/editar.html')

def tarefas_excluir(request):
    return render(request, 'pagetarefas/excluir.html')