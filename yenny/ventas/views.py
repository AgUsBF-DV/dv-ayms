from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Venta

# Create your views here.
def index(request):
    ventas = Venta.objects.all()
    paginador = Paginator(ventas, 10)
    num_pag = request.GET.get('page')
    objeto_pag = paginador.get_page(num_pag)

    columnas = ['ID', 'Cliente', 'Fecha', 'Total', 'Acciones']
    registros = []
    for venta in objeto_pag:
        registros.append([
            venta.id,
            getattr(venta, 'cliente', ''),
            getattr(venta, 'fecha', ''),
            getattr(venta, 'total', ''),
            '',  # para la botonera
        ])

    context = {
        'titulo': 'Lista de Ventas',
        'columnas': columnas,
        'registros': registros,
        'objeto_pag': objeto_pag,
    }
    return render(request, 'lista-ventas.html', context)
