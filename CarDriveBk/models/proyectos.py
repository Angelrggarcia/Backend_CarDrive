from django.db import models
from .users import usuarios
from .apartado import Apartado
from .proyectos import Proyecto

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=300, blank=True)
    color = models.CharField(max_length=6)
    imagen = models.ImageField(upload_to='imagenes_proyectos/')
    creator = models.ForeignKey(usuarios, on_delete=models.CASCADE)  # Link to the user model
    
    def __str__(self):  
        return self.proyectos
    
class archivados(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete = models.CASCADE)
    id_proyecto = models.ForeignKey(proyecto, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.archivados
    
class miembros(models.Model):
    id_usuario = models.ForeignKey(usuarios, on_delete = models.CASCADE)
    id_unidades = models.ForeignKey(unidades, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.miembros
    
