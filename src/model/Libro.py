
from Autor import Autor
from Editorial import Editorial
from Categoria import Categoria


class Libro:
    def __init__(self, id: int, titulo: str, autor: Autor, editorial: Editorial,
                 categoria: Categoria, precio: float, stock: int):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return (f"Libro({self.id}, {self.titulo}, "
                f"Autor: {self.autor.nombre} {self.autor.apellido}, "
                f"Editorial: {self.editorial.nombre}, "
                f"Categoria: {self.categoria.nombre}, "
                f"Precio: {self.precio}, Stock: {self.stock})")