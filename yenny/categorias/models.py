from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre} (ID:{self.id})"