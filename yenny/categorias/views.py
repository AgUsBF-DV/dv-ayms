from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CategoriaForm
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
            'path_crear': '/categorias/nuevo/',
            'texto_crear': '+ Nueva Categoria',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria-form.html'
    success_url = '/categorias/'

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria-form.html'
    success_url = '/categorias/'

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria-confirm-delete.html'
    success_url = '/categorias/'
