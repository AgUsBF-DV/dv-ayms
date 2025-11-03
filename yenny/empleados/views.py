from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import EmpleadoForm
from .models import Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'lista-empleados.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Apellido', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for empleado in objeto_pag:
            registros.append([
                empleado.id,
                getattr(empleado, 'nombre', ''),
                getattr(empleado, 'apellido', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Empleados',
            'path_crear': '/empleados/nuevo/',
            'texto_crear': '+ Nuevo Empleado',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado-form.html'
    success_url = '/empleados/'

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado-form.html'
    success_url = '/empleados/'

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado-confirm-delete.html'
    success_url = '/empleados/'
