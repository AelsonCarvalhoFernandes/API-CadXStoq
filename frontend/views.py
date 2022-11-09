from django.shortcuts import render
from backend.models import Entrada, Saida, Produtos

def index(request):
    return render(request, 'frontend/index.html')
