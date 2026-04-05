from django import forms
from .models import Gasto

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = '__all__' 

        widgets = {
            'valor': forms.NumberInput(attrs={
                'class': 'block w-full pl-12 pr-4 py-4 bg-gray-50 border-none rounded-xl text-2xl font-bold text-indigo-600 focus:ring-2 focus:ring-indigo-500',
                'placeholder': '0,00'
            }),
            'data': forms.DateInput(attrs={
                'class': 'w-full p-3 bg-gray-50 border-gray-100 rounded-lg focus:ring-2 focus:ring-indigo-500',
                'type': 'date'
            }),
            'tipo': forms.Select(attrs={
                'class': 'w-full p-3 bg-gray-50 border-gray-100 rounded-lg focus:ring-2 focus:ring-indigo-500',
                'id': 'tipo_gasto'
            }),
            'descricao': forms.TextInput(attrs={
                'class': 'w-full p-3 bg-gray-50 border-gray-100 rounded-lg focus:ring-2 focus:ring-indigo-500',
                'placeholder': 'Ex: Aluguel, Supermercado...'
            }),
            'meta_relacionada': forms.Select(attrs={
                'class': 'w-full p-2 bg-white border-none rounded-lg text-sm',
            }),
        }