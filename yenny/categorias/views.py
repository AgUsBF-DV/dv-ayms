from .forms import CategoriaForm
from .models import Categoria
from django.db.models.deletion import ProtectedError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'lista-categorias.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener parámetros de filtro
        nombre = self.request.GET.get('nombre')

        # Aplicar filtros
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for categoria in objeto_pag:
            campos = [
                categoria.id,
                getattr(categoria, 'nombre', ''),
                '',  # para la botonera

            ]
            registros.append({'objeto': categoria, 'campos': campos})
        context.update({
            'titulo': 'Lista de Categorias',
            'path_crear': '/categorias/nuevo/',
            'texto_crear': '+ Nueva Categoria',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
            'modelo': 'categoria',
        })

        if self.request.GET.get('error') == 'protected':
            context['error_message'] = "No se puede eliminar la categoria porque tiene libros asociados."

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

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return redirect(self.success_url + '?error=protected')

class CategoriaShowView(CategoriaUpdateView):
    template_name = 'categoria-form.html'

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

