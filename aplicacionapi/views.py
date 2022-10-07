from rest_framework import viewsets
from aplicacion.models import Item, Tipo_negocio, Usuario, Resultado_cliente
from .serializers import ItemSerializer, Tipo_negocioSerializer, UsuarioSerializer, Resultado_clienteSerializer


class ItemView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
class Tipo_negocioView(viewsets.ModelViewSet):
    serializer_class = Tipo_negocioSerializer
    queryset = Tipo_negocio.objects.all()
    
class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
    
class Resultado_clienteView(viewsets.ModelViewSet):
    serializer_class = Resultado_clienteSerializer
    queryset = Resultado_cliente.objects.all()