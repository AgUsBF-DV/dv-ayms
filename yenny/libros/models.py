from django.db import models

# Create your models here.
class Libro(models.Model):
	titulo = models.CharField(max_length=255)
	autor = models.ForeignKey('autores.Autor', on_delete=models.PROTECT, related_name='libros')
	editorial = models.ForeignKey('editoriales.Editorial', on_delete=models.PROTECT, related_name='libros')
	categoria = models.ForeignKey('categorias.Categoria', on_delete=models.PROTECT, related_name='libros')
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.PositiveIntegerField(default=0)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"ID:{self.id} - {self.titulo} (Autor: {self.autor})"
