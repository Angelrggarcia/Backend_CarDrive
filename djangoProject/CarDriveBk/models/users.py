from django.db import models



# Create your models here.
class usuarios(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 40, null = False)
    emial = models.CharField(max_length = 60, null = False)
    contraseña = models.CharField(max_length = 16, null = False)
    fecha = models.DateField(null = False)
    imagen = models.BinaryField()
    
    def __str__(self):
        return self.personas