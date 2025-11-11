from django.contrib import admin
from .models import Libro, LibroAutor

class LibroAutorInline(admin.TabularInline):
    model = LibroAutor
    extra = 1
    fields = ('autor', 'es_autor_principal', 'orden')
    ordering = ['orden']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'get_autor_principal', 'editorial', 'categoria', 'precio', 'stock']
    list_filter = ['editorial', 'categoria', 'created_at']
    search_fields = ['titulo', 'autor__nombre', 'autor__apellido']
    inlines = [LibroAutorInline]

    def get_autor_principal(self, obj):
        return obj.get_autor_principal()
    get_autor_principal.short_description = 'Autor Principal'

@admin.register(LibroAutor)
class LibroAutorAdmin(admin.ModelAdmin):
    list_display = ['libro', 'autor', 'es_autor_principal', 'orden']
    list_filter = ['es_autor_principal', 'created_at']
    search_fields = ['libro__titulo', 'autor__nombre', 'autor__apellido']
    ordering = ['libro', 'orden']
