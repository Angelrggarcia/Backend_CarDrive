from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator
from django.core.validators import validate_email
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError(("Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)
 

# Create your models here.
class Usuarios(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, null=False)
    email = models.EmailField(unique=True, null=False, validators=[validate_email])
    password = models.CharField(_("password"), max_length=128, validators=[MinLengthValidator(6)])
    color = models.CharField(max_length=6)
    fecha = models.DateField(null=False)
    imagen = models.ImageField(null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'fecha_nacimiento'] 
    
    objects = UserManager()

    def __str__(self):
        return self.nombre
