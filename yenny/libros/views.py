from django.views.generic import ListView
from .models import Libro

class LibroListView(ListView):
    model = Libro
    template_name = 'lista-libros.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Título', 'Autor', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for libro in objeto_pag:
            registros.append([
                libro.id,
                getattr(libro, 'titulo', ''),
                getattr(libro, 'autor', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Libros',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context
