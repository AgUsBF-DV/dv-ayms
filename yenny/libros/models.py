from django.db import models

# Tabla pivot para la relación many-to-many entre Libro y Autor
class LibroAutor(models.Model):
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE, related_name='libro_autores')
    autor = models.ForeignKey('autores.Autor', on_delete=models.PROTECT, related_name='autor_libros')
    es_autor_principal = models.BooleanField(default=False, help_text="Indica si es el autor principal del libro")
    orden = models.PositiveIntegerField(default=1, help_text="Orden del autor en el libro")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('libro', 'autor')
        ordering = ['orden']
        verbose_name = 'Libro-Autor'
        verbose_name_plural = 'Libros-Autores'

    def __str__(self):
        principal = " (Principal)" if self.es_autor_principal else ""
        return f"{self.libro.titulo} - {self.autor}{principal}"

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.ForeignKey('autores.Autor', on_delete=models.PROTECT, related_name='libros_principal', null=True, blank=True)
    autores = models.ManyToManyField('autores.Autor', through='LibroAutor', related_name='libros_colaboracion', blank=True)
    editorial = models.ForeignKey('editoriales.Editorial', on_delete=models.PROTECT, related_name='libros')
    categoria = models.ForeignKey('categorias.Categoria', on_delete=models.PROTECT, related_name='libros')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID:{self.id} - {self.titulo} (Autor: {self.get_autor_principal()})"

    def get_autor_principal(self):
        if self.autor:
            return self.autor
        autor_principal = self.libro_autores.filter(es_autor_principal=True).first()
        if autor_principal:
            return autor_principal.autor
        primer_autor = self.libro_autores.first()
        return primer_autor.autor if primer_autor else "Sin autor"

    def get_todos_los_autores(self):
        return [la.autor for la in self.libro_autores.all()]

    def get_autores_str(self):
        autores = self.get_todos_los_autores()
        if not autores:
            return str(self.autor) if self.autor else "Sin autor"
        return ", ".join([str(autor) for autor in autores])

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)

        if is_new and self.autor and not self.libro_autores.filter(autor=self.autor).exists():
            LibroAutor.objects.create(
                libro=self,
                autor=self.autor,
                es_autor_principal=True,
                orden=1
            )
