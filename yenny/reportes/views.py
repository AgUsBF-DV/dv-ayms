from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Sum, Count, F
from django.utils import timezone
from ventas.models import Venta, VentaLibro
from libros.models import Libro
from autores.models import Autor
from categorias.models import Categoria


class VentasDiariasView(ListView):
    """Reporte de ventas del día actual con paginado"""
    model = Venta
    template_name = 'ventas_diarias.html'
    context_object_name = 'ventas'
    paginate_by = 10
    ordering = ['-fecha']

    def get_queryset(self):
        # Filtrar solo las ventas de hoy
        hoy = timezone.now().date()
        return Venta.objects.filter(fecha__date=hoy)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fecha_hoy'] = timezone.now().date()
        
        # Calcular total de ventas del día
        ventas_hoy = self.get_queryset()
        context['total_ventas_dia'] = ventas_hoy.aggregate(total=Sum('total'))['total'] or 0
        context['cantidad_ventas'] = ventas_hoy.count()
        
        # Preparar datos para la tabla
        registros = []
        for venta in context['ventas']:
            registros.append({
                'campos': [
                    venta.id,
                    timezone.localtime(venta.fecha).strftime('%H:%M'),
                    str(venta.cliente),
                    str(venta.empleado),
                    f"${venta.total:.2f}",
                    None,  # campo dummy para que Total no sea el último
                ],
                'objeto': venta
            })
        
        context['titulo'] = f'Ventas del Día - {context["fecha_hoy"]}'
        context['columnas'] = ['ID', 'Hora', 'Cliente', 'Empleado', 'Total', '']
        context['registros'] = registros
        context['objeto_pag'] = context['page_obj']
        
        return context


class RankingLibrosView(ListView):
    """Reporte de Top 10 libros más vendidos"""
    model = VentaLibro
    template_name = 'ranking_libros.html'
    context_object_name = 'ranking'

    def get_queryset(self):
        # Agrupar por libro y sumar cantidades
        return (VentaLibro.objects
                .values('libro__id', 'libro__titulo', 'libro__autor__nombre', 'libro__autor__apellido')
                .annotate(total_vendido=Sum('cantidad'))
                .order_by('-total_vendido')[:10])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Preparar datos para la tabla
        registros = []
        for idx, item in enumerate(context['ranking'], start=1):
            autor = f"{item['libro__autor__nombre']} {item['libro__autor__apellido']}"
            registros.append({
                'campos': [
                    idx,
                    item['libro__titulo'],
                    autor,
                    item['total_vendido']
                ],
                'objeto': None
            })
        
        context['titulo'] = 'Top 10 Libros Más Vendidos'
        context['columnas'] = ['Posición', 'Título', 'Autor', 'Cantidad Vendida']
        context['registros'] = registros
        
        return context


class RankingAutoresView(ListView):
    """Reporte de Top 10 autores con más libros vendidos"""
    model = VentaLibro
    template_name = 'ranking_autores.html'
    context_object_name = 'ranking'

    def get_queryset(self):
        # Agrupar por autor y sumar cantidades de todos sus libros
        return (VentaLibro.objects
                .values('libro__autor__id', 'libro__autor__nombre', 'libro__autor__apellido')
                .annotate(total_vendido=Sum('cantidad'))
                .order_by('-total_vendido')[:10])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Preparar datos para la tabla
        registros = []
        for idx, item in enumerate(context['ranking'], start=1):
            autor = f"{item['libro__autor__nombre']} {item['libro__autor__apellido']}"
            registros.append({
                'campos': [
                    idx,
                    autor,
                    item['total_vendido']
                ],
                'objeto': None
            })
        
        context['titulo'] = 'Top 10 Autores Más Vendidos'
        context['columnas'] = ['Posición', 'Autor', 'Cantidad de Libros Vendidos']
        context['registros'] = registros
        
        return context


class RankingCategoriasView(ListView):
    """Reporte de Top 10 categorías con más libros vendidos"""
    model = VentaLibro
    template_name = 'ranking_categorias.html'
    context_object_name = 'ranking'

    def get_queryset(self):
        # Agrupar por categoría y sumar cantidades
        return (VentaLibro.objects
                .values('libro__categoria__id', 'libro__categoria__nombre')
                .annotate(total_vendido=Sum('cantidad'))
                .order_by('-total_vendido')[:10])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Preparar datos para la tabla
        registros = []
        for idx, item in enumerate(context['ranking'], start=1):
            registros.append({
                'campos': [
                    idx,
                    item['libro__categoria__nombre'],
                    item['total_vendido']
                ],
                'objeto': None
            })
        
        context['titulo'] = 'Top 10 Categorías Más Vendidas'
        context['columnas'] = ['Posición', 'Categoría', 'Cantidad de Libros Vendidos']
        context['registros'] = registros
        
        return context
