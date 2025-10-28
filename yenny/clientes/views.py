from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Cliente

# Create your views here.
def index(request):
    clientes = Cliente.objects.all()
    paginator = Paginator(clientes, 10)
    page_number = request.GET.get('page')
    objeto_pag = paginator.get_page(page_number)

    columnas = ['ID', 'Nombre', 'Apellido', 'Acciones']
    registros = []
    for cliente in objeto_pag:
        registros.append([
            cliente.id,
            getattr(cliente, 'nombre', ''),
            getattr(cliente, 'apellido', ''),
            '',  # para la botonera
        ])

    context = {
        'titulo': 'Lista de Clientes',
        'columnas': columnas,
        'registros': registros,
        'objeto_pag': objeto_pag,
    }
    return render(request, 'lista-clientes.html', context)