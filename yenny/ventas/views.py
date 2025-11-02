from django.views.generic import ListView
from .models import Venta

class VentaListView(ListView):
    model = Venta
    template_name = 'lista-ventas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Cliente', 'Fecha', 'Total', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for venta in objeto_pag:
            registros.append([
                venta.id,
                getattr(venta, 'cliente', ''),
                getattr(venta, 'fecha', ''),
                getattr(venta, 'total', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Ventas',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context
