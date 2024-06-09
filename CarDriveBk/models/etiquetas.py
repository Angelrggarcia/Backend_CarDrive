from django.db import models
from .archivos import Archivos


class Etiquetas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nombre


class RelacionesEtiquetas(models.Model):
    id_archivos = models.ForeignKey(Archivos, on_delete=models.CASCADE, related_name='relaciones_etiquetas')
    id_etiquetas = models.ForeignKey(Etiquetas, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.id_archivos}" + f" {self.id_etiquetas}"
