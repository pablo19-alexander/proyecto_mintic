from django import forms
from .models import Item

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