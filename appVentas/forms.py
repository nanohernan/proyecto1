from django import forms
from .models import Cliente, Tienda, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ['nombre', 'direccion']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['fecha', 'monto', 'id_cliente', 'id_tienda']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }
