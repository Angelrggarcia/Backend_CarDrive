from django.db import models
from .users import Usuario
from .archivos import Archivos

# Create your models here.

class Favoritos(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_archivo = models.ForeignKey(Archivos, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.favoritos
    
class Recientes(models.Models):
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_archivo = models.ForeignKey(Archivos, on_delete = models.CASCADE)
    tiempo = models.DateTimeField()