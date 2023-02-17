from .models import Testimonials
from django import forms

class TestimonialsFrom(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ('full_name', 'score', 'comments')
        lables = {
            'full_name': ('Nombre Completo'),
            'score': ('Puntuacion 1-5'),
            'comments': ('Comentario')
        }