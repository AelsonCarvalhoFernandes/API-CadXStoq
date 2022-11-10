from django.shortcuts import render
from backend.models import Entrada, Saida, Produtos

def index(request):
    return render(request, 'frontend/index.html')

def produtos(request):
    prod = Produtos.objects.all()
    return render(request, 'frontend/produtos.html', {'prod':prod})

def entrada(request):
    ent = Entrada.objects.all()

def saida(request):
    sai = Saida.objects.all()
