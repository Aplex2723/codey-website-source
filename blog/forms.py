from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': })
        # }