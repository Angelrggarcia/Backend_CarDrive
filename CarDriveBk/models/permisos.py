from django.db import models
from users import Usuario
from apartado import Apartado
from proyectos import Proyecto

class Proyectleader(models.Model):
    id_proyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.proyectleader
    
class Coordinador(models.Model):
    id_apartado = models.ForeignKey(Apartado, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.coordinador

class Miembro(models.Model):
    id_apartado = models.ForeignKey(Apartado, on_delete = models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    def __str__(self):
        return self.miembro