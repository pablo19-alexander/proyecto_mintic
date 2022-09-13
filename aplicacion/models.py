from django.db import models

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