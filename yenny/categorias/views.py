from django.views.generic import ListView
from .models import Categoria

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'lista-categorias.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for categoria in objeto_pag:
            registros.append([
                categoria.id,
                getattr(categoria, 'nombre', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Categorias',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context
