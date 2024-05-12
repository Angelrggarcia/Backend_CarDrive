from django.db import models
from .users import Usuario
from .archivos import archivos

# Create your models here.

class favoritos(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_archivo = models.ForeignKey(archivos, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.favoritos
    
class recientes(models.Models):
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_archivo = models.ForeignKey(archivos, on_delete = models.CASCADE)
    tiempo = models.DateTimeField()