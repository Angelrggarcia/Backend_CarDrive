from django.db import models
from unidades.models import unidades
from usuarios.models import usuarios
# Create your models here.

class archivos(models.Model):
    id = models.AutoField(prymary_key = True)
    nombre = models.CharField(max_length = 32, null = False)
    descripcion = models.CharField(max_length = 150)
    terminacion = models.CharField(max_length = 10, null = False)
    fecha = models.DateField()
    # llaves foraneas 
    id_usuarios = models.ForeignKey(usurio, on_delete = models.CASCADE)
    id_carpetas = models.ForeignKey(carpetas, on_delete = models.CASCADE)
    id_unidades = models.ForeignKey(unidades, on_delete = models.CASCADE)

    def __str__(self):
        return self.rchivos

class carpetas(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 20, null = False)
    color = models.CharField(max_length = 6, null = False)
    fecha = models.DateField()
    # llaves foraneas
    id_uniddes = models.ForeignKey(unidades, on_delete = models.CASCADE)
    id_carpetas = models.ForeignKey(cacrpetas, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.carpetas

class etiquetas(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 20, null = False)
    def __str__(self):
        return self.etiquetas
    
class asociar_etiquetas(models.Model):
    id_archivos = models.ForeignKey(archivos, on_delete = models.CASCADE)
    id_etiquetas = models.ForeignKey(etiquetas, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.asociar_etiquetas