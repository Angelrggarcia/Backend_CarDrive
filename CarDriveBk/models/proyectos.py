from django.db import models
from .users import Usuarios


# Create your models here.
class Proyectos(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    descripcion = models.CharField(max_length=300, blank=True)
    color = models.CharField(max_length=6, null=False)
    imagen = models.ImageField(upload_to='imagenes_proyectos/', null=False)
    activo = models.BooleanField(default=True, null=False)
    creator = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=False)  # Link to the user model

    def __str__(self):
        return self.nombre
