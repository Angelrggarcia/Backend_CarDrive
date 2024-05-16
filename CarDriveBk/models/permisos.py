from django.db import models
from .users import Usuarios
from .apartado import Apartados
from .proyectos import Proyectos


class Proyectleader(models.Model):
    id_proyecto = models.ForeignKey(Proyectos, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_usuario


class Coordinador(models.Model):
    id_apartado = models.ForeignKey(Apartados, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_usuario


class Miembros(models.Model):
    id_apartado = models.ForeignKey(Apartados, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_usuario
