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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class']='form-control'