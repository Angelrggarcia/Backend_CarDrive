from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extrafields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(("Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a superuser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)
 

# Create your models here.
class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, null=False)
    email = models.EmailField(unique=True, null=False, validators=[validate_email])
    password = models.CharField(_("password"), max_length=128, validators=[MinLengthValidator(6)])
    fecha = models.DateField(null=False)
    imagen = models.ImageField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'fecha_nacimiento'] 
    
    objects = UserManager()

    def __str__(self):
        return self.nombre
