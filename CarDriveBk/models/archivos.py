from django.db import models
from .apartado import Apartados
from .users import Usuarios
import uuid


class Archivos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=32, null=False)
    descripcion = models.CharField(max_length=150, blank=True, null=True)
    terminacion = models.CharField(max_length=10, null=False)
    fecha = models.DateField(null=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_apartado = models.ForeignKey(Apartados, on_delete=models.CASCADE, related_name='archivos', default=10)

    def __str__(self):
        return self.nombre