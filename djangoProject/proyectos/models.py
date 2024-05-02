from django.db import models

# Create your models here.
class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=23, null = False)
    desripcion = models.CharField( max_length=300)
    color = models.CharField(max_length=6, null = False)
    imagen = models.BinaryField()
    
    def __str__(self):  
        return self.proyectos
    
