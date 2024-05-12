from django.db import models
from usuarios.models import usuarios
from unidades.models import unidades
from proyectos.models import proyecto

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