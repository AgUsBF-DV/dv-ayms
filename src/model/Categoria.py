class Categoria:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Categoria({self.id}, {self.nombre})"
