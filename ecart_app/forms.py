from django import forms
from ecart_app.models import register

class registerForm(forms.ModelForm):
    
    class Meta:
        fields="__all__"
        model=register