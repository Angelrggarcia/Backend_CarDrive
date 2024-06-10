# from django.db import forms
from django.db import models
from .archivos import Archivos

# forms.Form
class Versiones(models.Model):
    id_archivo = models.ForeignKey(Archivos, on_delete=models.CASCADE)
    iteracion = models.IntegerField()
    archivo = models.FileField(upload_to='documentos/', null=True, default="N/A")
    nombre = models.TextField()

    def __str__(self):
        return self.id_archivo.__str__() + " - " + self.iteracion.__str__()
