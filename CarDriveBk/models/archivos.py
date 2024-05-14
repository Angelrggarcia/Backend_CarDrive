from django.db import models
from .apartado import Apartado
from .users import Usuario


class Archivos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32, null=False)
    descripcion = models.CharField(max_length=150)
    terminacion = models.CharField(max_length=10, null=False)
    fecha = models.DateField()
    id_usuarios = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_apartados = models.ForeignKey(Apartado, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre
