from django.contrib import admin
from .models import Item, Tipo_negocio, Usuario, Resultado_cliente

# Register your models here.
# admin.site.register(Tipo_negocio)
admin.site.register(Item)
admin.site.register(Tipo_negocio)
admin.site.register(Usuario)
admin.site.register(Resultado_cliente)