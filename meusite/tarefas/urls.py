from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefas_home),
    path('adicionar/', views.tarefas_adicionar),
    path('editar/<int:id>/', views.tarefas_editar),
    path('excluir/<int:id>/', views.tarefas_excluir),
]