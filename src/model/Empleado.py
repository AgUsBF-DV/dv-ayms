
from Rol import Rol

class Empleado:
    def __init__(self, id: int, nombre: str, apellido: str, correo: str,
                 contrasenia: str, rol: Rol, esta_activo: bool = True):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasenia = contrasenia
        self.rol = rol
        self.esta_activo = esta_activo

    def __str__(self):
        return f"Empleado({self.id}, {self.nombre} {self.apellido}, Rol: {self.rol.nombre}, Activo: {self.esta_activo})"
