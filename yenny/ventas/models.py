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
        self.subtotal = (self.precio_unitario or 0) * (self.cantidad or 0)

    def save(self, *args, **kwargs):
        # calcular subtotal y actualizar subtotal del item
        self.calcular_subtotal()
        super().save(*args, **kwargs)
        # recalcular total de la venta y actualizar
        try:
            total = sum(item.subtotal for item in self.venta.libros.all())
            self.venta.total = total
            self.venta.save(update_fields=["total"])
        except Exception:
            pass

    def __str__(self):
        return f"{self.cantidad} x {self.libro.titulo} (${self.precio_unitario}) = ${self.subtotal}"
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
            self.subtotal = (self.precio_unitario or 0) * (self.cantidad or 0)

        def save(self):
            # calcular subtotal y actualizar subtotal del item
            self.calcular_subtotal()
            super().save()
            # recalcular total de la venta y actualizar
            try:
                total = sum(item.subtotal for item in self.venta.libros.all())
                self.venta.total = total
                self.venta.save(update_fields=["total"])
            except Exception:
                pass

        def __str__(self):
            return f"{self.cantidad} x {self.libro.titulo} (${self.precio_unitario}) = ${self.subtotal}"
