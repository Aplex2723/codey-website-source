from django import forms
from .models import ConctactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ConctactModel
        fields = ['name', 'email', 'subject', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu Nombre', 'id': 'name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu Email', 'id': 'email', 'required': True}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto', 'id': 'subject','required': True }),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mensaje', 'rows': 5, 'required': True}),
        }