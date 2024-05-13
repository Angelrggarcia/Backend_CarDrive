from django.db import models

from .apartado import Apartado
from .users import Usuario
# Create your models here.

class Archivos(models.Model):
    id = models.AutoField(prymary_key = True)
    nombre = models.CharField(max_length = 32, null = False)
    descripcion = models.CharField(max_length = 150)
    terminacion = models.CharField(max_length = 10, null = False)
    fecha = models.DateField()
    # llaves foraneas 
    id_usuarios = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    id_apartados = models.ForeignKey(Apartado, on_delete = models.CASCADE)

    def __str__(self):
        return self.archivos

class Etiquetas(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 20, null = False)
    def __str__(self):
        return self.etiquetas
    
class Asociar_etiquetas(models.Model):
    id_archivos = models.ForeignKey(Archivos, on_delete = models.CASCADE)
    id_etiquetas = models.ForeignKey(Etiquetas, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.asociar_etiquetas