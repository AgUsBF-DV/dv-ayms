from .forms import EditorialForm
from .models import Editorial
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class EditorialListView(ListView):
    model = Editorial
    template_name = 'lista-editoriales.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Nombre', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for editorial in objeto_pag:
            campos = [
                editorial.id,
                getattr(editorial, 'nombre', ''),
                '',  # para la botonera
            ]
            registros.append({'objeto': editorial, 'campos': campos})
        context.update({
            'titulo': 'Lista de Editoriales',
            'path_crear': '/editoriales/nuevo/',
            'texto_crear': '+ Nueva Editorial',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
            'modelo': 'editorial',
        })

        if self.request.GET.get('error') == 'protected':
            context['error_message'] = "No se puede eliminar la editorial porque tiene libros asociados."
        
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

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return redirect(self.success_url + '?error=protected')

class EditorialShowView(EditorialUpdateView):
    template_name = 'editorial-form.html'
    
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
