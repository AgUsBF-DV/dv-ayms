from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AutorForm
from .models import Autor

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
            'path_crear': '/autores/nuevo/',
            'texto_crear': '+ Nuevo Autor',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor-form.html'
    success_url = '/autores/'

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'autor-form.html'
    success_url = '/autores/'

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'autor-confirm-delete.html'
    success_url = '/autores/'