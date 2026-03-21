from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_simulacoes, name='lista_simulacoes'),
    path('criar/', views.criar_simulacao, name="criar_simulacoes"),
    path('editar/<int:pk>/', views.editar_simulacao, name="editar_simulacao"),
    path('deletar/<int:pk>/', views.deletar_simulacao, name='deletar_simulacao'),
]