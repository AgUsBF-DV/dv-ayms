from django.views.generic import ListView
from .models import Editorial

class EditorialListView(ListView):
    model = Editorial
    template_name = 'lista-editoriales.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for editorial in objeto_pag:
            registros.append([
                editorial.id,
                getattr(editorial, 'nombre', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Editoriales',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context
