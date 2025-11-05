from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import VentaForm
from .models import Venta

class VentaListView(ListView):
    model = Venta
    template_name = 'lista-ventas.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Cliente', 'Fecha', 'Total', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for venta in objeto_pag:
            registros.append([
                venta.id,
                getattr(venta, 'cliente', ''),
                getattr(venta, 'fecha', ''),
                getattr(venta, 'total', ''),
                '',  # para la botonera
            ])
        context.update({
            'titulo': 'Lista de Ventas',
            'path_crear': '/ventas/nuevo/',
            'texto_crear': '+ Nueva Venta',
            'columnas': columnas,
            'registros': registros,
            'objeto_pag': objeto_pag,
        })
        return context

class VentaCreateView(CreateView):
    def form_valid(self, form):
        response = super().form_valid(form)
        venta = self.object
        request = self.request
        libros = request.POST.getlist('libro')
        cantidades = request.POST.getlist('cantidad')
        precios = request.POST.getlist('precio_unitario')
        subtotales = request.POST.getlist('subtotal')
        total = 0
        from .models import VentaLibro
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
        return context

class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta-form.html'
    success_url = '/ventas/'

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'venta-confirm-delete.html'
    success_url = '/ventas/'
