from .forms import VentaForm
from .models import Venta, VentaLibro
from django.db.models.deletion import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class VentaListView(ListView):
    model = Venta
    template_name = 'lista-ventas.html'
    paginate_by = 10
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Cliente', 'Fecha', 'Total', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for venta in objeto_pag:
            campos = [
                venta.id,
                getattr(venta, 'cliente', ''),
                getattr(venta, 'fecha', ''),
                getattr(venta, 'total', ''),
                '',  # para la botonera
            ]
            registros.append({'objeto': venta, 'campos': campos})
        context.update({
            'titulo': 'Lista de Ventas',
            'path_crear': '/ventas/nuevo/',
            'texto_crear': '+ Nueva Venta',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
            'modelo': 'venta',
        })

        if self.request.GET.get('error') == 'protected':
            context['error_message'] = "No se puede eliminar la venta porque tiene registros asociados."
        
        return context

class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta-form.html'
    success_url = '/ventas/'

    def form_valid(self, form):
        response = super().form_valid(form)
        venta = self.object
        request = self.request
        libros = request.POST.getlist('libro')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio_unitario')
        subtotales = request.POST.getlist('subtotal')
        total = 0
        
        for i in range(len(libros)):
            if libros[i]:
                libro_id = libros[i]
                cantidad = int(cantidades[i]) if i < len(cantidades) else 1
                precio_unitario = float(precios[i]) if i < len(precios) else 0
                subtotal = float(subtotales[i]) if i < len(subtotales) else 0
                total += subtotal
                VentaLibro.objects.create(
                    venta=venta,
                    libro_id=libro_id,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    subtotal=subtotal
                )
        
        venta.total = total
        venta.save(update_fields=["total"])
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from libros.models import Libro
        context['libros'] = Libro.objects.all()
        return context

class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta-form.html'
    success_url = '/ventas/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from libros.models import Libro
        context['libros'] = Libro.objects.all()
        context['venta_libros'] = self.object.libros.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        venta = self.object
        # Eliminar VentaLibro existentes
        venta.libros.all().delete()
        request = self.request
        libros = request.POST.getlist('libro')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio_unitario')
        subtotales = request.POST.getlist('subtotal')
        total = 0
        
        for i in range(len(libros)):
            if libros[i]:
                libro_id = libros[i]
                cantidad = int(cantidades[i]) if i < len(cantidades) else 1
                precio_unitario = float(precios[i]) if i < len(precios) else 0
                subtotal = float(subtotales[i]) if i < len(subtotales) else 0
                total += subtotal
                VentaLibro.objects.create(
                    venta=venta,
                    libro_id=libro_id,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    subtotal=subtotal
                )
        
        venta.total = total
        venta.save(update_fields=["total"])
        return response

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'venta-confirm-delete.html'
    success_url = '/ventas/'

    def form_valid(self, form):
        try:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        except ProtectedError:
            return redirect(self.success_url + '?error=protected')

# Vista de solo lectura para mostrar una venta
class VentaShowView(VentaUpdateView):
    template_name = 'venta-form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['readonly'] = True
        return context
    
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
