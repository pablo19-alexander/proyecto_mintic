from dataclasses import fields
from xml.parsers.expat import model
from django import forms
from .models import Item
from django.contrib.auth.models import User


#---------------- crud ------------------------------------------------------
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = 'id_tipo_negocio','descripcion'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['id_tipo_negocio'].widget.attrs.update({
            'class': 'form-select',
        })
        
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control',
        })
#---------------- form deregistro
class UserForm(forms.ModelForm):
    
    username = forms.CharField(max_length=150, label='Usuario', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    
    password = forms.CharField(max_length=80, label='password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
        }
    ))
    
    first_name = forms.CharField(max_length=50, label='Nombre', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    
    last_name = forms.CharField(max_length=50, label='Apellido', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
        
    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
#---------------- login ----------------------------------------------------------------        
class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        }
    ))
    
    password = forms.CharField(max_length=80, label='Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
        }
    ))