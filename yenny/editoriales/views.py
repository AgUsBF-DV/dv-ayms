from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import EditorialForm
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
            'path_crear': '/editoriales/nuevo/',
            'texto_crear': '+ Nueva Editorial',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context

class EditorialCreateView(CreateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'editorial-form.html'
    success_url = '/editoriales/'

class EditorialUpdateView(UpdateView):
    model = Editorial
    form_class = EditorialForm
    template_name = 'editorial-form.html'
    success_url = '/editoriales/'

class EditorialDeleteView(DeleteView):
    model = Editorial
    template_name = 'editorial-confirm-delete.html'
    success_url = '/editoriales/'
