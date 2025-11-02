from django.views.generic import ListView
from .models import Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'lista-empleados.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Apellido', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for empleado in objeto_pag:
            registros.append([
                empleado.id,
                getattr(empleado, 'nombre', ''),
                getattr(empleado, 'apellido', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Empleados',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context
