
from Cliente import Cliente
from Empleado import Empleado
from datetime import datetime
from VentaLibro import VentaLibro

class Venta:
    def __init__(self, id: int, cliente: Cliente, empleado: Empleado,
                 fecha: datetime):
        self.id = id
        self.cliente = cliente
        self.empleado = empleado
        self.fecha = fecha
        self.total = 0
        self.detalles = []

    def agregar_detalle(self, detalle: VentaLibro):
        self.detalles.append(detalle)
        self.total += detalle.subtotal

    def __str__(self):
        return (f"Venta({self.id}, Cliente: {self.cliente.nombre} {self.cliente.apellido}, "
                f"Empleado: {self.empleado.nombre} {self.empleado.apellido}, "
                f"Fecha: {self.fecha}, Total: {self.total})")