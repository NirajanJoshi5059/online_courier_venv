from django import forms
from product.models import Product


# class ProductForm(forms.Form):
#     name=forms.CharField()
#     price=forms.CharField()

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        exclude= ('status','remarks',)