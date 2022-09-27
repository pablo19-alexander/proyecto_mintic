from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
tipoNegocio = (
    (1, 'restaurante'),
    (2, 'drogueria')
)

class Item(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_tipo_negocio = models.IntegerField(
        null=True,
        choices=tipoNegocio, 
        default=1,
        verbose_name="Tipo de Negocio"
        )
    descripcion = models.TextField(verbose_name="Descripción del requerimiento", null=True)
    
    def __str__(self):
        item = "DESCRIPCION DEL REQUERIMIENTO: " + self.descripcion
        return item
    
class UserProfile(AbstractUser, PermissionsMixin):
    email = models.EmailField(
            ('email address'), 
            unique=True
        )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    class Meta:
        abstract = True