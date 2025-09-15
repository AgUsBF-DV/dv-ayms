
from Libro import Libro

class VentaLibro:
    def __init__(self, id: int, libro: Libro, cantidad: int):
        self.id = id
        self.libro = libro
        self.cantidad = cantidad
        self.subtotal = libro.precio * cantidad

    def __str__(self):
        return (f"VentaLibro({self.id}, Libro: {self.libro.titulo}, "
                f"Cantidad: {self.cantidad}, Subtotal: {self.subtotal})")
