class Cliente:
    def __init__(self, id: int, nombre: str, apellido: str, correo: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def __str__(self):
        return f"Cliente({self.id}, {self.nombre} {self.apellido}, {self.correo})"
