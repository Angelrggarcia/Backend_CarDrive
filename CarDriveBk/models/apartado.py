from django.db import models
from .proyectos import Proyecto
from .users import Usuario

class Apartado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    color = models.CharField(max_length=6)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    imagen = models.ImageField(upload_to='imagenes_apartados/', blank=True, null=True)
    id_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subapartados')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
# Create your models here.
    def __str__(self):
        return self.apartado

