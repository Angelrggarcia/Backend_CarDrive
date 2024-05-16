from django.db import models
from .proyectos import Proyectos
from .users import Usuarios


class Apartados(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=6)
    fecha = models.DateField(null=False)
    imagen = models.ImageField(upload_to='imagenes_apartados/', blank=True, null=True)
    id_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subapartados')
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=False)
    id_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE, null=False)

    # Create your models here.
    def __str__(self):
        return self.id.__str__() + " - " + self.nombre.__str__()
