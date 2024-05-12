from django.db import models
from usuarios.models import usuarios
from unidades.models import unidades

# Create your models here.
class proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=23, null = False)
    desripcion = models.CharField( max_length=300)
    color = models.CharField(max_length=6, null = False)
    imagen = models.BinaryField()
    
    def __str__(self):  
        return self.proyectos
    
class archivados(models.Model):
    id_usuraio = models.ForeignKey(usuarios, on_delete = models.CASCADE)
    id_proyecto = models.ForeignKey(proyecto, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.archivados
    
class miembros(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete = models.CASCADE)
    id_unidades = models.ForeignKey(unidades, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.miembros
    
