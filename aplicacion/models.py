from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# tipoNegocio = (
#     (1, 'restaurante'),
#     (2, 'drogueria')
# )
class Tipo_negocio(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_negocio = models.IntegerField(null=True, blank=True, verbose_name="Tipo de Negocio")
    nombre_tipo_negocio = models.CharField(max_length=100, verbose_name="Nombre del nuevo tipo de negocio", null=True, blank=True)
    
    def __str__(self):
        negocio = "" + self.nombre_tipo_negocio
        return negocio

class Item(models.Model):
    
    id = models.AutoField(primary_key=True)
    tipo_negocio = models.ForeignKey(Tipo_negocio, null=True, blank=True, default=1, on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name="Descripción del requerimiento", null=True)
    
    def __str__(self):
        item = "DESCRIPCION DEL REQUERIMIENTO: " + self.descripcion
        return item
# nuevo
class Usuario(models.Model):
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    negocio = models.ForeignKey(Tipo_negocio, null=True, blank=True, default=1, on_delete=models.CASCADE)
    def __str__(self):
        user = "El usuario: " + self.usuario.first_name + " - tiene como negocio: " + self.negocio.nombre_tipo_negocio
        return user
    
class Resultado_cliente(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    requerimiento = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    checked = models.BooleanField('checked', default=False)
    
    def __str__(self):
        resultado = "El usuario: " + self.usuario.usuario.first_name + " - requerimiento: " + self.requerimiento.descripcion
        return resultado