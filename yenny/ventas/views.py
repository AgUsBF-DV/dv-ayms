from .forms import VentaForm
from .models import Venta, VentaLibro
from django.db.models.deletion import ProtectedError
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from datetime import datetime

class VentaListView(ListView):
    model = Venta
    template_name = 'lista-ventas.html'
    paginate_by = 10
    ordering = ['-id']

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener parámetros de filtro
        fecha_desde = self.request.GET.get('fecha_desde')
        fecha_hasta = self.request.GET.get('fecha_hasta')
        cliente_busq = self.request.GET.get('cliente_busq')
        libro_busq = self.request.GET.get('libro_busq')

        # Aplicar filtros
        if fecha_desde:
            try:
                fecha_desde_obj = datetime.strptime(fecha_desde, '%Y-%m-%d').date()
                queryset = queryset.filter(fecha__date__gte=fecha_desde_obj)
            except ValueError:
                pass

        if fecha_hasta:
            try:
                fecha_hasta_obj = datetime.strptime(fecha_hasta, '%Y-%m-%d').date()
                queryset = queryset.filter(fecha__date__lte=fecha_hasta_obj)
            except ValueError:
                pass

        if cliente_busq:
            queryset = queryset.filter(
                Q(cliente__nombre__icontains=cliente_busq) |
                Q(cliente__apellido__icontains=cliente_busq)
            )

        if libro_busq:
            queryset = queryset.filter(
                Q(libros__libro__titulo__icontains=libro_busq) |
                Q(libros__libro__autor__nombre__icontains=libro_busq) |
                Q(libros__libro__autor__apellido__icontains=libro_busq) |
                Q(libros__libro__autores__nombre__icontains=libro_busq) |
                Q(libros__libro__autores__apellido__icontains=libro_busq)
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columnas = ['ID', 'Cliente', 'Empleado', 'Fecha', 'Total', 'Libros', 'Acciones']
        objeto_pag = context['page_obj']
        registros = []
        for venta in objeto_pag:
            # Obtener información de libros vendidos
            libros_vendidos = venta.libros.all()
            libros_info = []
            for vl in libros_vendidos:
                autores_str = vl.libro.get_autores_str()
                libros_info.append(f"{vl.libro.titulo} ({autores_str}) x{vl.cantidad}")
            libros_str = "; ".join(libros_info) if libros_info else "Sin libros"

            campos = [
                venta.id,
                str(venta.cliente),
                str(venta.empleado),
                timezone.localtime(venta.fecha).strftime("%d/%m/%Y %H:%M"),
                f"${venta.total:.2f}",
                libros_str,
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
        from .utils import procesar_item_venta, descontar_stock_libro

        response = super().form_valid(form)
        venta = self.object
        request = self.request
        libros = request.POST.getlist('libro')
        cantidades = request.POST.getlist('cantidad')
        subtotales = request.POST.getlist('subtotal')
        total = 0
        
        for i in range(len(libros)):
            if libros[i]:  # Solo procesar si hay un libro seleccionado
                # Procesar el item usando la utilidad (sin precio_unitario del form)
                item = procesar_item_venta(
                    libros[i],
                    cantidades[i] if i < len(cantidades) else '',
                    '',  # No enviamos precio, se obtiene del libro
                    subtotales[i] if i < len(subtotales) else ''
                )

                if item:  # Si se pudo procesar el item
                    # Descontar del stock del libro
                    descontar_stock_libro(item['libro'], item['cantidad'])

                    # Crear VentaLibro
                    total += item['subtotal']
                    VentaLibro.objects.create(
                        venta=venta,
                        libro=item['libro'],
                        cantidad=item['cantidad'],
                        precio_unitario=item['precio_unitario'],
                        subtotal=item['subtotal']
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
        from .utils import procesar_item_venta, descontar_stock_libro, restaurar_stock_venta

        response = super().form_valid(form)
        venta = self.object

        # Restaurar el stock de los libros vendidos anteriormente
        restaurar_stock_venta(venta)

        # Eliminar VentaLibro existentes
        venta.libros.all().delete()

        request = self.request
        libros = request.POST.getlist('libro')
        cantidades = request.POST.getlist('cantidad')
        subtotales = request.POST.getlist('subtotal')
        total = 0
        
        for i in range(len(libros)):
            if libros[i]:  # Solo procesar si hay un libro seleccionado
                # Procesar el item usando la utilidad (sin precio_unitario del form)
                item = procesar_item_venta(
                    libros[i],
                    cantidades[i] if i < len(cantidades) else '',
                    '',  # No enviamos precio, se obtiene del libro
                    subtotales[i] if i < len(subtotales) else ''
                )

                if item:  # Si se pudo procesar el item
                    # Descontar del stock del libro
                    descontar_stock_libro(item['libro'], item['cantidad'])

                    # Crear VentaLibro
                    total += item['subtotal']
                    VentaLibro.objects.create(
                        venta=venta,
                        libro=item['libro'],
                        cantidad=item['cantidad'],
                        precio_unitario=item['precio_unitario'],
                        subtotal=item['subtotal']
                    )

        venta.total = total
        venta.save(update_fields=["total"])
        return response

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'venta-confirm-delete.html'
    success_url = '/ventas/'

    def form_valid(self, form):
        from .utils import restaurar_stock_venta

        try:
            # Restaurar el stock de los libros vendidos antes de eliminar
            restaurar_stock_venta(self.object)

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
