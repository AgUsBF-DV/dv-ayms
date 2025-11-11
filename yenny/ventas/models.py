from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Venta(models.Model):
    cliente = models.ForeignKey(
        "clientes.Cliente", on_delete=models.PROTECT, related_name="ventas"
    )
    empleado = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="ventas"
    )
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Venta {self.id} - Cliente: {self.cliente} - Total: {self.total} - {self.fecha:%Y-%m-%d %H:%M}"

    @property
    def detalle(self):
        """
        Devuelve los objetos VentaLibro asociados a esta venta.
        """
        return self.libros.all() if hasattr(self, 'libros') else []

class VentaLibro(models.Model):
    venta = models.ForeignKey(
        "Venta", on_delete=models.CASCADE, related_name="libros"
    )
    libro = models.ForeignKey(
        "libros.Libro", on_delete=models.PROTECT, related_name="venta_libros"
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def calcular_subtotal(self):
        """Calcula el subtotal basado en cantidad y precio unitario"""
        self.subtotal = (self.precio_unitario or 0) * (self.cantidad or 0)

    def save(self, *args, **kwargs):
        # Si es una nueva instancia y no se ha establecido precio_unitario, usar el del libro
        if not self.pk and not self.precio_unitario:
            self.precio_unitario = self.libro.precio

        # Calcular subtotal antes de guardar
        self.calcular_subtotal()

        # Guardar la instancia
        super().save(*args, **kwargs)

        # Recalcular total de la venta y actualizar
        try:
            from .utils import calcular_total_venta
            if self.venta:
                calcular_total_venta(self.venta)
        except Exception as e:
            # Log the error but don't fail the save operation
            import logging
            logging.warning(f"Error updating venta total: {e}")

    def delete(self, *args, **kwargs):
        """Override delete to restore stock when a VentaLibro is deleted"""
        # Restaurar stock antes de eliminar
        if self.libro:
            from .utils import restaurar_stock_libro
            restaurar_stock_libro(self.libro, self.cantidad)

        # Eliminar la instancia
        super().delete(*args, **kwargs)

        # Recalcular total de la venta
        try:
            from .utils import calcular_total_venta
            if self.venta:
                calcular_total_venta(self.venta)
        except Exception as e:
            import logging
            logging.warning(f"Error updating venta total after delete: {e}")

    def __str__(self):
        return f"{self.cantidad} x {self.libro.titulo} (${self.precio_unitario}) = ${self.subtotal}"
