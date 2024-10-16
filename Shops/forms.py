from django import forms
from .models import Shop

class ShopRegistrationForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
        }
