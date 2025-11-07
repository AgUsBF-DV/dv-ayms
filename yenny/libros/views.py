from .forms import LibroForm
from .models import Libro
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class LibroListView(ListView):
    model = Libro
    template_name = 'lista-libros.html'
    paginate_by = 10
    ordering = ['autor__apellido', 'titulo']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Título', 'Autor', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for libro in objeto_pag:
            campos = [
                libro.id,
                getattr(libro, 'titulo', ''),
                getattr(libro, 'autor', ''),
                '',  # para la botonera
            ]
            registros.append({'objeto': libro, 'campos': campos})
        context.update({
            'titulo': 'Lista de Libros',
            'path_crear': '/libros/nuevo/',
            'texto_crear': '+ Nuevo Libro',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
            'modelo': 'libro',
        })

        if self.request.GET.get('error') == 'protected':
            context['error_message'] = "No se puede eliminar el libro porque tiene ventas asociadas."
        
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

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return redirect(self.success_url + '?error=protected')

# Vista de solo lectura para mostrar un libro
class LibroShowView(LibroUpdateView):
    template_name = 'libro-form.html'
    
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
