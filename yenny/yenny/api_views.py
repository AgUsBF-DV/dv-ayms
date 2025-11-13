from django.http import JsonResponse
from django.views import View
from libros.models import Libro
from autores.models import Autor
from clientes.models import Cliente

class LibrosApiView(View):
    """API para obtener información de libros con autores para el formulario de ventas"""

    def get(self, request):
        query = request.GET.get('q', '').strip()
        libros = Libro.objects.select_related('autor', 'editorial', 'categoria').prefetch_related('autores')

        if query:
            libros = libros.filter(
                titulo__icontains=query
            ) | libros.filter(
                autor__nombre__icontains=query
            ) | libros.filter(
                autor__apellido__icontains=query
            ) | libros.filter(
                autores__nombre__icontains=query
            ) | libros.filter(
                autores__apellido__icontains=query
            )
            libros = libros.distinct()

        libros = libros[:20]  # Limitar a 20 resultados

        data = []
        for libro in libros:
            data.append({
                'id': libro.id,
                'titulo': libro.titulo,
                'autores': libro.get_autores_str(),
                'editorial': str(libro.editorial),
                'precio': float(libro.precio),
                'stock': libro.stock,
                'display': f"{libro.titulo} - {libro.get_autores_str()} (${libro.precio})"
            })

        return JsonResponse({'libros': data})

class AutoresApiView(View):
    """API para obtener información de autores"""

    def get(self, request):
        query = request.GET.get('q', '').strip()
        autores = Autor.objects.all()

        if query:
            autores = autores.filter(
                nombre__icontains=query
            ) | autores.filter(
                apellido__icontains=query
            )

        autores = autores[:20]  # Limitar a 20 resultados

        data = []
        for autor in autores:
            libros_count = autor.libros_principal.count() + autor.autor_libros.count()
            data.append({
                'id': autor.id,
                'nombre': autor.nombre,
                'apellido': autor.apellido,
                'nombre_completo': f"{autor.nombre} {autor.apellido}",
                'libros_count': libros_count
            })

        return JsonResponse({'autores': data})

class ClientesApiView(View):
    """API para obtener información de clientes"""

    def get(self, request):
        query = request.GET.get('q', '').strip()
        clientes = Cliente.objects.all()

        if query:
            clientes = clientes.filter(
                nombre__icontains=query
            ) | clientes.filter(
                apellido__icontains=query
            ) | clientes.filter(
                correo__icontains=query
            )

        clientes = clientes[:20]  # Limitar a 20 resultados

        data = []
        for cliente in clientes:
            data.append({
                'id': cliente.id,
                'nombre': cliente.nombre,
                'apellido': cliente.apellido,
                'correo': cliente.correo,
                'nombre_completo': f"{cliente.nombre} {cliente.apellido}",
                'display': f"{cliente.nombre} {cliente.apellido} ({cliente.correo})"
            })

        return JsonResponse({'clientes': data})
