from django.db import models
from .users import usuarios
from .apartado import Apartado
from .proyectos import proyecto

class proyectleader(models.Model):
    id_proyecto = models.ForeignKey(proyecto, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(usuarios, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.proyectleader
    
class coordinador(models.Model):
    id_unidad = models.ForeignKey(unidades, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(usuarios, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.coordinador