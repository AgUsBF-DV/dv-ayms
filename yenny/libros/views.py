from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import LibroForm
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
            'path_crear': '/libros/nuevo/',
            'texto_crear': '+ Nuevo Libro',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context

class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro-form.html'
    success_url = '/libros/'

class LibroUpdateView(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro-form.html'
    success_url = '/libros/'

class LibroDeleteView(DeleteView):
    model = Libro
    template_name = 'libro-confirm-delete.html'
    success_url = '/libros/'
