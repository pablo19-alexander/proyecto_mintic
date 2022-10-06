from dataclasses import fields
from xml.parsers.expat import model
from django import forms
from .models import Item, Usuario, Resultado_cliente
from django.contrib.auth.models import User

# -------------- formularios -----------------------
class NegocioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['negocio']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['negocio'].widget.attrs.update({
            'class': 'form-select',
        })
        
#---------------- formulario de restaurantes --------------------
class Form_res(forms.ModelForm):
    class Meta:
        model = Resultado_cliente
        fields = ['requerimiento','checked']
        widgets ={
            'requerimiento': forms.Select(attrs={'class': 'form-control'}),
            'checked': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
        
    #     self.fields['requerimiento'].widget.attrs.update({
    #         'class': 'form-select',
    #     })
        
    #     self.fields['checked'].widget.attrs.update({
    #         'class': 'form-check',
    #     })
    
        
#---------------- crud ------------------------------------------------------
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = 'tipo_negocio','descripcion'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['tipo_negocio'].widget.attrs.update({
            'class': 'form-select',
        })
        
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control',
        })
        
#---------------- form de registro
class UserForm(forms.ModelForm):
    
    password = forms.CharField(max_length=80, label='password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
        }
    ))
    
    email = forms.EmailField(label='E-mail', required= True, widget=forms.EmailInput(
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
        fields = ['first_name', 'last_name', 'email', 'password']
#---------------- login ----------------------------------------------------------------        
class LoginForm(forms.Form):
    email = forms.CharField(label='Correo', widget=forms.TextInput(
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