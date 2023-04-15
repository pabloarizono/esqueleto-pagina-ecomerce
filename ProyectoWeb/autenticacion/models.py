from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db import models






class UsuarioManager(BaseUserManager):
    def create_user(self, email, username,nombre,apellido ,password=None):
        if not email:
            raise ValueError('El usuario debe tener una dirección de correo electrónico válida')
        
        usuario = self.model(username=username,email=self.normalize_email(email),nombre=nombre,apellido=apellido)  
        
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email,nombre,apellido ,password):

        usuario = self.create_user(email,username=username,nombre=nombre,apellido=apellido,password=password)   
        usuario.is_admin = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    nombre = models.CharField('Nombres',max_length=255, unique=True)
    apellido = models.CharField('Apellidos',max_length=255, unique=True)
    email = models.EmailField('Correo electronico',max_length=255, null=True)
    username = models.CharField('Nombre de Usuario',unique=True, max_length=255)
    telefono = models.CharField('telefono ',max_length=150, blank=False, null=False)
    domicilio = models.CharField('domicilio',max_length=100,blank=False, null=False )
    ciudad = models.CharField('ciudad',max_length=100,blank=False, null=False )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    object= UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombre','apellido']
    
    def __str__(self):
        return f'{self.nombre},{self.apellido}'

    def has_perm(self, perm, obj=None):         #lo usa el admin de django
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
        
