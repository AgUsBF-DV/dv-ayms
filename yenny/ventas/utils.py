"""
Utilidades para gestión de ventas e inventario
"""
from libros.models import Libro

def procesar_item_venta(libro_id, cantidad_str, precio_str, subtotal_str):
    """
    Procesa un item de venta validando datos y calculando valores

    Args:
        libro_id (str): ID del libro
        cantidad_str (str): Cantidad como string (puede estar vacío)
        precio_str (str): Precio como string (puede estar vacío)
        subtotal_str (str): Subtotal como string (puede estar vacío)

    Returns:
        dict: Diccionario con libro, cantidad, precio_unitario, subtotal procesados
        None: Si no se puede procesar el item
    """
    try:
        libro = Libro.objects.get(id=libro_id)
    except Libro.DoesNotExist:
        return None

    # Validar y convertir cantidad
    try:
        cantidad = int(cantidad_str) if cantidad_str and cantidad_str.strip() else 1
    except (ValueError, AttributeError):
        cantidad = 1

    # Verificar stock disponible
    if libro.stock < cantidad:
        cantidad = libro.stock

    # Validar y convertir precio_unitario (usar precio del libro si no se proporciona)
    try:
        precio_unitario = float(precio_str) if precio_str and precio_str.strip() else libro.precio
    except (ValueError, AttributeError):
        precio_unitario = libro.precio

    # Validar y convertir subtotal (calcularlo si no se proporciona)
    try:
        subtotal = float(subtotal_str) if subtotal_str and subtotal_str.strip() else 0.0
    except (ValueError, AttributeError):
        subtotal = 0.0

    # Calcular subtotal si no se proporcionó o es 0
    if subtotal == 0.0:
        subtotal = precio_unitario * cantidad

    return {
        'libro': libro,
        'cantidad': cantidad,
        'precio_unitario': precio_unitario,
        'subtotal': subtotal
    }

def descontar_stock_libro(libro, cantidad):
    """
    Descuenta stock de un libro

    Args:
        libro: Instancia del modelo Libro
        cantidad (int): Cantidad a descontar
    """
    libro.stock -= cantidad
    libro.save(update_fields=['stock'])

def restaurar_stock_libro(libro, cantidad):
    """
    Restaura stock de un libro

    Args:
        libro: Instancia del modelo Libro
        cantidad (int): Cantidad a restaurar
    """
    libro.stock += cantidad
    libro.save(update_fields=['stock'])

def restaurar_stock_venta(venta):
    """
    Restaura el stock de todos los libros de una venta

    Args:
        venta: Instancia del modelo Venta
    """
    for venta_libro in venta.libros.all():
        restaurar_stock_libro(venta_libro.libro, venta_libro.cantidad)

def calcular_total_venta(venta):
    """
    Calcula y actualiza el total de una venta

    Args:
        venta: Instancia del modelo Venta

    Returns:
        float: Total calculado
    """
    total = sum(item.subtotal for item in venta.libros.all())
    venta.total = total
    venta.save(update_fields=["total"])
    return total
