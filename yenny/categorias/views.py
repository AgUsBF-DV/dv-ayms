from django.shortcuts import render
from .models import Categoria

# Create your views here.
def index(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista-categorias.html', {'categorias': categorias})