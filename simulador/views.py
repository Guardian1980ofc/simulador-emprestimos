from django.shortcuts import render, redirect
from .models import SimulacaoEmprestimo

# Create your views here.
#criando o CRUD

#CREATE
def criar_simulacao(request):
    if request.method == 'POST':
        valor = request.POST['valor']
        juros = request.POST['juros']
        prazo = request.POST['prazo']
        parcela = request.POST['parcela']
        valor_final = request.POST['valor_final']

        SimulacaoEmprestimo.objects.create(
            valor = valor,
            juros = juros,
            prazo = prazo,
            parcela = parcela,
            valor_final = valor_final
        )
        return redirect('lista_simulacoes')
    
    return render(request, 'simulador/criar.html')

#READ
def lista_simulacoes(request):
    simulacoes = SimulacaoEmprestimo.objects.all()
    return render(request, 'simulador/lista.html', {'simulacoes': simulacoes})

#UPDATE
def editar_simulacao(request, pk):
    simulacao = SimulacaoEmprestimo.objects.get(id=pk)
    if request.method == 'POST':
        simulacao.valor = request.POST['valor']
        simulacao.juros = request.POST['juros']
        simulacao.prazo = request.POST['prazo']
        simulacao.parcela = request.POST['parcela']
        simulacao.valor_final = request.POST['valor_final']
        simulacao.save()
        return redirect('lista_simulacoes')
    
    return render(request, 'simulador/editar.html', {'simulacao': simulacao})

#DELETE
def deletar_simulacao(request, pk):
    simulacao = SimulacaoEmprestimo.objects.get(id=pk)
    if request.method == 'POST':
        simulacao.delete()
        return redirect('lista_simulacoes')
    
    return render(request, 'simulador/deletar.html', {'simulacao': simulacao})
