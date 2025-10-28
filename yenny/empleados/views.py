from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Empleado

# Create your views here.
def index(request):
    empleados = Empleado.objects.all()
    paginator = Paginator(empleados, 10)
    page_number = request.GET.get('page')
    objeto_pag = paginator.get_page(page_number)

    columnas = ['ID', 'Nombre', 'Apellido', 'Email', 'Rol', 'Acciones']
    registros = []
    for empleado in objeto_pag:
        registros.append([
            empleado.id,
            getattr(empleado, 'first_name', ''),
            getattr(empleado, 'last_name', ''),
            getattr(empleado, 'email', ''),
            getattr(empleado, 'rol', ''),
            '',  # para la botonera
        ])

    context = {
        'titulo': 'Lista de Empleados',
        'columnas': columnas,
        'registros': registros,
        'objeto_pag': objeto_pag,
    }
    return render(request, 'lista-empleados.html', context)