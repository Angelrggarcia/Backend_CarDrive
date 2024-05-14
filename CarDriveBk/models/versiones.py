from django.db import models
from .archivos import Archivos

class Version(models.Model):
    id_archivo = models.ForeignKey(Archivos, on_delete = models.CASCADE)
    iteracion = models.IntegerField()
    archivo = models.BinaryField()


    def __str__(self):
        return self.id_archivo.__str__() + " - " + self.iteracion.__str__()