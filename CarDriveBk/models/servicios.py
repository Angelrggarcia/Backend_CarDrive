from django.db import models
from .users import Usuarios
from .archivos import Archivos

# Create your models here.

class Favoritos(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)
    id_archivo = models.ForeignKey(Archivos, on_delete = models.CASCADE)


    def __str__(self):
        return self.id_usuario.__str__() + " - " + self.id_archivo.__str__()
    
class Recientes(models.Model):
    id_usuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)
    id_archivo = models.ForeignKey(Archivos, on_delete = models.CASCADE)
    def __str__(self):
        return self.id_usuario.__str__() + " - " + self.id_archivo.__str__()