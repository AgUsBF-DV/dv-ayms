class Autor:
    def __init__(self, id: int, nombre: str, apellido: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Autor({self.id}, {self.nombre} {self.apellido})"
