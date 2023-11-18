from django import forms
from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'id': 'message',
                'placeholder': 'Enter Message'
            })
        }