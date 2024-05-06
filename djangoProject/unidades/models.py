from django.db import models

class unidades(models.Model):
    id = models.AutoField(primary_key = true)
    nombre = models.CharFiled(max_length = 20, null = False)
    color = models.CharFiled(max_length = 6, null  = False)
    imagen = models.BinaryField()
    proyectoId = models.ForeignKey('proyectos.Proyecto', on_delete = models.CASCADE)
# Create your models here.
    def __str__(self):
        return self.unidades

