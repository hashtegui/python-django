from django.db import models
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    
    dados = {
        'receitas': receitas
    }
    return render(request,'index.html',dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_nova = {
        'receita': receita
    }
    return render(request, 'receita.html', receita_nova)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    dados = {
        'receitas' : lista_receitas
        }

    return render(request, 'buscar.html',dados)