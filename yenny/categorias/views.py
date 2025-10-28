from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Categoria

# Create your views here.
def index(request):
    categorias = Categoria.objects.all()
    paginator = Paginator(categorias, 10)
    page_number = request.GET.get('page')
    objeto_pag = paginator.get_page(page_number)

    columnas = ['ID', 'Nombre', 'Acciones']
    registros = []
    for categoria in objeto_pag:
        registros.append([
            categoria.id,
            getattr(categoria, 'nombre', ''),
            '',  # para la botonera
        ])

    context = {
        'titulo': 'Lista de Categorías',
        'columnas': columnas,
        'registros': registros,
        'objeto_pag': objeto_pag,
    }
    return render(request, 'lista-categorias.html', context)