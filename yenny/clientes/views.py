from .forms import ClienteForm
from .models import Cliente
from django.db.models.deletion import ProtectedError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class ClienteListView(ListView):
    model = Cliente
    template_name = 'lista-clientes.html'
    paginate_by = 10
    ordering = ['apellido', 'nombre']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener parámetros de filtro
        nombre = self.request.GET.get('nombre')
        apellido = self.request.GET.get('apellido')

        # Aplicar filtros
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Apellido', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for cliente in objeto_pag:
            campos = [
                cliente.id,
                getattr(cliente, 'nombre', ''),
                getattr(cliente, 'apellido', ''),
                '',  # para la botonera
            ]
            registros.append({'objeto': cliente, 'campos': campos})
        context.update({
            'titulo': 'Lista de Clientes',
            'path_crear': '/clientes/nuevo/',
            'texto_crear': '+ Nuevo Cliente',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
            'modelo': 'cliente',
        })

        if self.request.GET.get('error') == 'protected':
            context['error_message'] = "No se puede eliminar el cliente porque tiene ventas asociadas."
        
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

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return redirect(self.success_url + '?error=protected')

# Vista de solo lectura para mostrar un cliente
class ClienteShowView(ClienteUpdateView):
    template_name = 'cliente-form.html'
    
    # Cargar el formulario en modo solo lectura
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True
        return form

    # No permitir POST (no guardar cambios)
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
