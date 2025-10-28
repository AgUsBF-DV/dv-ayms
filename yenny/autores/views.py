from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Autor

# Create your views here.
def index(request):
    autores = Autor.objects.all()
    paginator = Paginator(autores, 10)
    page_number = request.GET.get('page')
    objeto_pag = paginator.get_page(page_number)

    columnas = ['ID', 'Nombre', 'Apellido', 'Acciones']
    registros = []
    for autor in objeto_pag:
        registros.append([
            autor.id,
            getattr(autor, 'nombre', ''),
            getattr(autor, 'apellido', ''),
            '',  # para la botonera
        ])

    context = {
        'titulo': 'Lista de Autores',
        'columnas': columnas,
        'registros': registros,
        'objeto_pag': objeto_pag,
    }
    return render(request, 'lista-autores.html', context)