from rest_framework import serializers
from aplicacion.models import Item, Tipo_negocio, Usuario, Resultado_cliente
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class Tipo_negocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_negocio
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
class Resultado_clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultado_cliente
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'