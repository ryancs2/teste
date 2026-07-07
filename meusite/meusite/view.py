from django.http import HttpResponse

def teste_view(request):
    return HttpResponse("<h1>Olá, mundo! Esta é uma view de teste. </h1>")

def index_view(request):
    return HttpResponse("<h1>Bem-vindo à página inicial!</h1>")

def administração_view(request):
    return HttpResponse("<h1>Bem-vindo à página de administração!</h1>")