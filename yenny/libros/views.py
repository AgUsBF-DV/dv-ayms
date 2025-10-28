from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Libro

# Create your views here.
def index(request):
    libros = Libro.objects.all()
    paginator = Paginator(libros, 10)
    page_number = request.GET.get('page')
    objeto_pag = paginator.get_page(page_number)

    columnas = ['ID', 'Título', 'Autor', 'Acciones']
    registros = []
    for libro in objeto_pag:
        registros.append([
            libro.id,
            getattr(libro, 'titulo', ''),
            getattr(libro, 'autor', ''),
            '',  # para la botonera
        ])

    context = {
        'titulo': 'Lista de Libros',
        'columnas': columnas,
        'registros': registros,
        'objeto_pag': objeto_pag,
    }
    return render(request, 'lista-libros.html', context)
