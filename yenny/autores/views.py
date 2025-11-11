from .forms import AutorForm
from .models import Autor
from django.db.models.deletion import ProtectedError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class AutorListView(ListView):
    model = Autor
    template_name = 'lista-autores.html'
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
        for autor in objeto_pag:
            campos = [
                autor.id,
                getattr(autor, 'nombre', ''),
                getattr(autor, 'apellido', ''),
                '',  # para la botonera
            ]
            registros.append({'objeto': autor, 'campos': campos})
        context.update({
            'titulo': 'Lista de Autores',
            'path_crear': '/autores/nuevo/',
            'texto_crear': '+ Nuevo Autor',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
            'modelo': 'autor',
        })

        if self.request.GET.get('error') == 'protected':
            context['error_message'] = "No se puede eliminar el autor porque tiene libros asociados."
        
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

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return redirect(self.success_url + '?error=protected')

class AutorShowView(AutorUpdateView):
    template_name = 'autor-form.html'
    
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