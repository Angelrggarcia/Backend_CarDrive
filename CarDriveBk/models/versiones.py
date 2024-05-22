from django.db import models
from .archivos import Archivos


class Versiones(models.Model):
    id_archivo = models.ForeignKey(Archivos, on_delete=models.CASCADE)
    iteracion = models.IntegerField()
    archivo = models.BinaryField()
    
    # archivo = models.BinaryField(null=False)
    # tamales = models.FileField(upload_to='documentos/', null=True, default="N/A")

    def __str__(self):
        return self.id_archivo.__str__() + " - " + self.iteracion.__str__()
