from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class RolChoices(models.TextChoices):
    ADMIN = 'ADMIN', 'Administrador'
    ENCARGADO = 'ENCARGADO', 'Encargado'
    VENDEDOR = 'VENDEDOR', 'Vendedor'


class Empleado(AbstractUser):
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=RolChoices.choices, default=RolChoices.VENDEDOR)
    
    # Config de autenticación
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID:{self.id} - {self.email} - {self.rol})"