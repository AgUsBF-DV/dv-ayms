from django.views.generic import ListView
from .models import Cliente

class ClienteListView(ListView):
    model = Cliente
    template_name = 'lista-clientes.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Apellido', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for cliente in objeto_pag:
            registros.append([
                cliente.id,
                getattr(cliente, 'nombre', ''),
                getattr(cliente, 'apellido', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Clientes',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context
