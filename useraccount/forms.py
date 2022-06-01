from pyexpat import model
import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomSingupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Need valid email address')

    class Meta:
        model=User
        fields=('username','email','password1','password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text=''
        self.fields['username'].help_text=''
        self.fields['email'].help_text=''
        self.fields['password2'].help_text=''

        self.fields['username'].widget.attrs['placeholder'] = 'UserName'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        self.fields['email'].widget.attrs['placeholder']='E-mail'

        self.fields['password2'].label='Confirm Password'

    
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if "@" not in email and ".com" not in email:
            raise forms.ValidationError("Invalid Email address.")