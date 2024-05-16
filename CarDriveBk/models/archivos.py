from django.db import models
from .apartado import Apartados
from .users import Usuarios


class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32, null=False)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    terminacion = models.CharField(max_length=10, null=False)
    fecha = models.DateField(null=False)
    id_usuarios = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_apartados = models.ForeignKey(Apartados, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
