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

