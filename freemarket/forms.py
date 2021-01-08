from django import forms
from .models import Product

class UploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'genre', 'explanation', 'condition', 'price', 'shipping_cost', 'picture_1', 'picture_2', 'picture_3', 'picture_4')
        