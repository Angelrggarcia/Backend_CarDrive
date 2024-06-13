from django.db import models
from .proyectos import Proyectos
from .users import Usuarios
import uuid

class Apartados(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=7, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='imagenes_apartados/', blank=True, null=True)
    id_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subapartados')
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=False)
    id_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, null=False)
    # Create your models here.
    def __str__(self):
        return self.id.__str__() + " - " + self.nombre.__str__()

    def get_ancestors(self):
        ancestors = []
        parent = self.id_padre
        while parent:
            ancestors.append(parent)
            parent = parent.id_padre
        return ancestors[::-1]  # Reverse the list to start from the root