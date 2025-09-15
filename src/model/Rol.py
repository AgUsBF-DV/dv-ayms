class Rol:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Rol({self.id}, {self.nombre})"
