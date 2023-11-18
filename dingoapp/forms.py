from django import forms
from .models import *


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name *'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'num_of_g': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of guests *',
                'type': 'number'
            }),
            'fone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number *'
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date * (yyyy-mm-dd)',
                'id': 'datapicker'
            }),
            'time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Time *'
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'Textarea',
                'rows': '4',
                'placeholder': 'Your Note'
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'id': 'message',
                'rows': '9',
                'cols': '30',
                'placeholder': 'Enter Message'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': 'Enter Your Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Phone Number'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'subject',
                'placeholder': 'Enter Subject'
            })

        }
