from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ClienteForm
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
            'path_crear': '/clientes/nuevo/',
            'texto_crear': '+ Nuevo Cliente',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente-form.html'
    success_url = '/clientes/'

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente-form.html'
    success_url = '/clientes/'

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente-confirm-delete.html'
    success_url = '/clientes/'
