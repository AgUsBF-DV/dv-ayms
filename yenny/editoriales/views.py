from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Editorial

# Create your views here.
def index(request):
    editoriales = Editorial.objects.all()
    paginator = Paginator(editoriales, 10)
    page_number = request.GET.get('page')
    objeto_pag = paginator.get_page(page_number)

    columnas = ['ID', 'Nombre', 'Acciones']
    registros = []
    for editorial in objeto_pag:
        registros.append([
            editorial.id,
            getattr(editorial, 'nombre', ''),
            '',  # para la botonera
        ])

    context = {
        'titulo': 'Lista de Editoriales',
        'columnas': columnas,
        'registros': registros,
        'objeto_pag': objeto_pag,
    }
    return render(request, 'lista-editoriales.html', context)