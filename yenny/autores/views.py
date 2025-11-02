from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Autor

# Create your views here.
from django.views.generic import ListView

class AutorListView(ListView):
    model = Autor
    template_name = 'lista-autores.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Apellido', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for autor in objeto_pag:
            registros.append([
                autor.id,
                getattr(autor, 'nombre', ''),
                getattr(autor, 'apellido', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Autores',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context
